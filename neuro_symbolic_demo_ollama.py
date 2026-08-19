#!/usr/bin/env python3
"""
Neuro-Symbolic AI Demonstration (Ollama-backed Discourse)
=========================================================

This is the real-LLM counterpart to ``neuro_symbolic_demo_prolog.py``. It
keeps the SWI-Prolog "Geometry" half unchanged and replaces the regex
"Discourse" half with a local LLM served by **Ollama** -- so the
neuro-symbolic loop now runs on an actual model instead of an ELIZA-style
pattern matcher.

    Interpret (LLM)  -> Formalize (LLM)  -> Derive (Prolog)
    -> Verify (Prolog) -> Reinterpret (LLM) -> Revise (Loop)

Why Ollama
----------
It is local, offline, needs no API key, and needs no GPU to be useful at
small sizes. That matches the no-network, no-credentials stance of the
other two demo files. A hosted API (Mistral, OpenAI, ...) would plug in at
the same single function -- see "Using a hosted API" below.

Why the SWI-Prolog backend
-------------------------
This module imports ``PrologEngine`` and ``LLMDiscourse`` from
``neuro_symbolic_demo_prolog``. A real LLM emits idiomatic Prolog --
recursive rules, lists, DCGs -- that the pure-Python toy engine in
``neuro_symbolic_demo.py`` cannot run. Only the real Prolog backend lets
the formal-constraint half of the loop do what the essay claims for it, so
the Ollama layer is bound to that backend. (The two ``LLMDiscourse``
copies also differ in how they clear the knowledge base, so the subclass
is bound to one of them; this one uses the Prolog copy.)

Graceful fallback
-----------------
If Ollama is not running (not installed, not started, model not pulled),
every overridden method silently falls back to the inherited regex
implementation. So this file runs *today*, with no LLM, and produces the
same results as ``neuro_symbolic_demo_prolog.py``. The moment Ollama is
up, the same code paths start using the model -- no edits required.

Prerequisites
-------------
1. SWI-Prolog + ``pyswip`` (same as ``neuro_symbolic_demo_prolog.py``):
       winget install SWI-Prolog.SWI-Prolog
       pip install pyswip
2. The Python ``requests`` library:  pip install requests
3. Ollama (only needed for the LLM path; fallback works without it):
       Windows:  winget install Ollama.Ollama
       macOS:     brew install ollama
       Linux:     curl -fsSL https://ollama.com/install.sh | sh
   Then start it and pull a model:
       ollama serve            # if not already running as a service
       ollama pull qwen2.5:7b   # or any instruct model you prefer

Running
-------
       python neuro_symbolic_demo_ollama.py                 # run the demos
       python neuro_symbolic_demo_ollama.py --status         # show Ollama state
       python neuro_symbolic_demo_ollama.py --interactive    # REPL
       python neuro_symbolic_demo_ollama.py --model llama3.1:8b --demo
       python neuro_symbolic_demo_ollama.py --host http://gpu-box:11434 --demo

The model and host can also be set via the ``OLLAMA_MODEL`` and
``OLLAMA_HOST`` environment variables (Ollama's own convention).

Using a hosted API
------------------
Replace the body of ``OllamaClient.chat`` with a call to your provider's
chat endpoint (Mistral, OpenAI, Anthropic, ...). Everything upstream --
the prompts, the JSON contract, the validation, the fallback -- stays the
same. The rest of the system never knows which backend produced the text.
"""

import json
import os
import re
import sys
import time
from typing import List, Dict, Optional

import requests

# Reuse the SWI-Prolog backend and the regex Discourse (our fallback base).
from neuro_symbolic_demo_prolog import PrologEngine, LLMDiscourse


# ============================================================================
# Ollama HTTP client
# ============================================================================

class OllamaClient:
    """
    Minimal client for the Ollama HTTP API (``/api/chat``).

    Only two things matter to the rest of the system:
      * ``is_available()`` -- can we reach a running Ollama right now?
      * ``chat(system, user, json_mode)`` -- get a completion string back.

    Availability is cached for a short TTL so a down server does not add a
    timeout to every single call (the loop makes three calls per query).
    """

    def __init__(self, host: str = "http://localhost:11434",
                 model: str = "qwen2.5:7b", timeout: float = 60.0):
        self.host = host.rstrip("/")
        self.model = model
        self.timeout = timeout
        self._avail: Optional[bool] = None
        self._avail_checked_at: float = 0.0
        self._avail_ttl: float = 15.0  # seconds to trust the last probe

    # -- availability ------------------------------------------------------

    def is_available(self) -> bool:
        """True iff Ollama responds on /api/tags within a short timeout."""
        now = time.time()
        if self._avail is not None and (now - self._avail_checked_at) < self._avail_ttl:
            return self._avail
        try:
            r = requests.get(f"{self.host}/api/tags", timeout=2.0)
            self._avail = (r.status_code == 200)
        except requests.RequestException:
            self._avail = False
        self._avail_checked_at = now
        return self._avail

    def list_models(self) -> List[str]:
        """Return installed model names (empty if Ollama is down)."""
        try:
            r = requests.get(f"{self.host}/api/tags", timeout=2.0)
            r.raise_for_status()
            return [m.get("name", "") for m in r.json().get("models", [])]
        except requests.RequestException:
            return []

    # -- chat --------------------------------------------------------------

    def chat(self, system: str, user: str, json_mode: bool = False,
             temperature: float = 0.2) -> str:
        """
        One-shot (non-streaming) chat completion. Returns the assistant
        message content as a string. Raises ``requests.RequestException`` /
        ``ValueError`` / ``OSError`` on any failure; callers catch and fall
        back to the regex layer.
        """
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "stream": False,
            "options": {"temperature": temperature},
        }
        if json_mode:
            payload["format"] = "json"
        r = requests.post(f"{self.host}/api/chat", json=payload, timeout=self.timeout)
        r.raise_for_status()
        data = r.json()
        content = data.get("message", {}).get("content", "")
        if not content:
            raise ValueError("empty completion from Ollama")
        return content


# ============================================================================
# Discourse: Ollama-backed LLM layer (regex fallback inherited)
# ============================================================================

class OllamaDiscourse(LLMDiscourse):
    """
    Real-LLM Discourse layer. Overrides the three NL touch points of the
    neuro-symbolic loop -- ``interpret`` (NL -> facts/rules), ``_extract_query``
    (NL -> one Prolog goal), and ``reinterpret`` (solutions -> NL answer) --
    to call a local Ollama model. Every override falls back to the inherited
    regex implementation if Ollama is unreachable or the model's output fails
    validation, so the system degrades gracefully to the offline behavior.

    The inherited ``loop`` is unchanged: it calls these overrides in
    sequence, loads the returned clauses into the Prolog engine, runs the
    query, and reinterprets. No other method needs to change.
    """

    def __init__(self, prolog_engine: PrologEngine, client: Optional[OllamaClient] = None,
                 model: str = "qwen2.5:7b", host: str = "http://localhost:11434"):
        super().__init__(prolog_engine)
        self.client = client or OllamaClient(host=host, model=model)
        # Per-call accounting so demos can show which path ran.
        self.paths: Dict[str, str] = {"interpret": "", "query": "", "reinterpret": ""}
        self.llm_calls = 0
        self.fallback_calls = 0

    # -- prompt templates --------------------------------------------------

    _INTERPRET_SYSTEM = (
        "You are a Prolog formalizer. Given a natural-language statement, "
        "output ONLY a JSON object with two keys: \"facts\" and \"rules\". "
        "Each value is a list of strings; each string is one valid Prolog "
        "clause. Facts look like \"man(socrates).\". Rules look like "
        "\"mortal(X) :- man(X).\". Use lowercase atoms and uppercase "
        "variables. Formalize only declarative statements; ignore any "
        "question in the input. Emit no comments, no queries, no prose, "
        "no markdown -- just the JSON object."
    )

    _QUERY_SYSTEM = (
        "You are a Prolog query extractor. Given a natural-language "
        "question, output ONLY a single Prolog query goal that can be "
        "posed against the knowledge base, ending with a period. Examples: "
        "\"mortal(socrates).\", \"parent(X, mary).\", "
        "\"grandfather(X, bob).\". Use uppercase for variables. Output the "
        "goal only -- no prose, no markdown, no explanation."
    )

    _REINTERPRET_SYSTEM = (
        "You explain formal results in plain language. Given a Prolog "
        "query and its solutions (a list of variable bindings, possibly "
        "empty), write one concise natural-language answer. If the "
        "solutions list is empty, state that the claim is false given the "
        "available knowledge. Do not mention Prolog syntax or variables."
    )

    # -- interpret: NL -> facts + rules -----------------------------------

    def interpret(self, text: str, domain: str = None) -> List[str]:
        """Formalize NL into Prolog clauses via the LLM, else regex fallback."""
        if not self.client.is_available():
            return self._fallback_interpret(text, domain)
        try:
            user = f"Domain hint: {domain or 'general'}\nStatement: {text}"
            raw = self.client.chat(self._INTERPRET_SYSTEM, user, json_mode=True)
            spec = self._parse_json(raw)
            # Structurally validate, then drop clauses whose head predicate is
            # a static builtin/library predicate (is/2, member/2, ...) that
            # assertz cannot redefine -- otherwise the loop would raise.
            candidates = [self._clean_clause(x)
                          for x in spec.get("facts", []) + spec.get("rules", [])]
            clauses = [c for c in candidates if c and self.prolog.is_assertable(c)]
            if not clauses:
                # Nothing usable came back; let the regex layer have a go.
                return self._fallback_interpret(text, domain)
            self.paths["interpret"] = "ollama"
            self.llm_calls += 1
            return clauses
        except Exception:
            return self._fallback_interpret(text, domain)

    # -- _extract_query: NL -> one Prolog goal ----------------------------

    def _extract_query(self, text: str, domain: str) -> str:
        """Extract a single Prolog query goal via the LLM, else regex fallback."""
        if not self.client.is_available():
            return self._fallback_query(text, domain)
        try:
            user = f"Domain hint: {domain or 'general'}\nQuestion: {text}"
            raw = self.client.chat(self._QUERY_SYSTEM, user, json_mode=False, temperature=0.0)
            goal = self._clean_clause(raw)
            if not goal:
                return self._fallback_query(text, domain)
            self.paths["query"] = "ollama"
            self.llm_calls += 1
            return goal
        except Exception:
            return self._fallback_query(text, domain)

    # -- reinterpret: solutions -> NL answer ------------------------------

    def reinterpret(self, solutions: List[Dict[str, str]], original_query: str = None) -> str:
        """Render solutions as a natural-language answer via the LLM, else regex."""
        if not self.client.is_available():
            return self._fallback_reinterpret(solutions, original_query)
        try:
            user = (f"Prolog query: {original_query or '(unknown)'}\n"
                    f"Solutions: {json.dumps(solutions)}")
            raw = self.client.chat(self._REINTERPRET_SYSTEM, user, json_mode=False)
            answer = raw.strip()
            if not answer:
                return self._fallback_reinterpret(solutions, original_query)
            self.paths["reinterpret"] = "ollama"
            self.llm_calls += 1
            return answer
        except Exception:
            return self._fallback_reinterpret(solutions, original_query)

    # -- fallbacks (delegate to the inherited regex layer) ----------------

    def _fallback_interpret(self, text: str, domain: Optional[str]) -> List[str]:
        self.paths["interpret"] = "regex"
        self.fallback_calls += 1
        return super().interpret(text, domain)

    def _fallback_query(self, text: str, domain: str) -> str:
        self.paths["query"] = "regex"
        self.fallback_calls += 1
        return super()._extract_query(text, domain)

    def _fallback_reinterpret(self, solutions: List[Dict[str, str]],
                              original_query: Optional[str]) -> str:
        self.paths["reinterpret"] = "regex"
        self.fallback_calls += 1
        return super().reinterpret(solutions, original_query)

    # -- output cleaning / validation -------------------------------------

    @staticmethod
    def _strip_fences(text: str) -> str:
        """Remove ```lang ... ``` markdown wrappers if present."""
        text = text.strip()
        if text.startswith("```"):
            lines = text.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip().startswith("```"):
                lines = lines[:-1]
            text = "\n".join(lines).strip()
        return text

    @classmethod
    def _parse_json(cls, text: str) -> dict:
        """Parse JSON from a model response, tolerating fences/extra text."""
        text = cls._strip_fences(text)
        start, end = text.find("{"), text.rfind("}")
        if start != -1 and end > start:
            text = text[start:end + 1]
        return json.loads(text)

    @classmethod
    def _clean_clause(cls, raw: str) -> Optional[str]:
        """
        Validate a single Prolog clause string. Returns the cleaned clause
        or None if it should be dropped. We are deliberately strict: the
        Prolog engine's ``assertz`` raises on a malformed clause, and the
        inherited ``loop`` does not catch that, so anything we return must
        be loadable.
        """
        s = cls._strip_fences(raw)
        # A clause is one line; take the first non-empty one.
        s = next((ln.strip() for ln in s.splitlines() if ln.strip()), "")
        if not s:
            return None
        if not s.endswith("."):
            s += "."
        # Balanced parentheses (rules/facts must have them around args).
        if s.count("(") != s.count(")"):
            return None
        # Reject prose / formatting leakage that has no place in a clause.
        low = s.lower()
        if any(bad in low for bad in ("?", "```", "json", "output", "answer")):
            return None
        # Must look like name(...) or name(...) :- body.
        if not re.match(r"^[a-z][a-zA-Z0-9_]*\(", s):
            return None
        return s

    # -- reporting ---------------------------------------------------------

    def path_summary(self) -> str:
        """One-line summary of which Discourse path each step used."""
        return (
            f"interpret={self.paths['interpret'] or '-'}, "
            f"query={self.paths['query'] or '-'}, "
            f"reinterpret={self.paths['reinterpret'] or '-'}"
        )


# ============================================================================
# Neuro-Symbolic System (Ollama Discourse + SWI-Prolog Geometry)
# ============================================================================

class NeuroSymbolicSystem:
    """
    Complete neuro-symbolic system: an Ollama-backed Discourse wired to a
    SWI-Prolog Geometry. Same shape as the other two versions, so the
    three are directly comparable.
    """

    def __init__(self, model: str = "qwen2.5:7b", host: str = "http://localhost:11434"):
        self.geometry = PrologEngine()
        self.discourse = OllamaDiscourse(self.geometry, model=model, host=host)

    def run_loop(self, query: str, domain: str = None) -> Dict:
        return self.discourse.loop(query, domain)

    def status_line(self) -> str:
        client = self.discourse.client
        if client.is_available():
            models = client.list_models()
            have = client.model in models
            tag = f"model '{client.model}' {'loaded' if have else 'NOT pulled'}"
            return f"Ollama UP at {client.host} ({tag})"
        return f"Ollama DOWN at {client.host} -> regex fallback in use"

    def demonstrate(self):
        """Run natural-language scenarios through the real neuro-symbolic loop."""
        print("=" * 80)
        print("NEURO-SYMBOLIC AI DEMONSTRATION (Ollama Discourse + SWI-Prolog)")
        print("From Plato to Prolog to Prompts: The 2,500-Year Journey to Artificial Reason")
        print("=" * 80)
        print()
        print(f"Discourse layer: {self.status_line()}")
        print(f"Geometry layer:   SWI-Prolog via pyswip")
        print()

        scenarios = [
            ("DEMO 1: CLASSICAL LOGIC (Aristotle's Syllogism)", "classical_logic",
             "All men are mortal. Socrates is a man. Is Socrates mortal?"),
            ("DEMO 2: FAMILY RELATIONSHIPS (Ontology)", "family",
             "John is the father of Mary. Mary is the mother of Bob. "
             "Who is the grandparent of Bob?"),
            ("DEMO 3: NOVEL SYLLOGISM (generalization)", "classical_logic",
             "All cats are animals. Whiskers is a cat. Is Whiskers an animal?"),
            ("DEMO 4: RECURSION (the point of real Prolog)", "family",
             "John is a parent of Mary. Mary is a parent of Bob. "
             "Bob is a parent of Charlie. An ancestor is a parent, or a parent "
             "of an ancestor. Who are the ancestors of Charlie?"),
        ]

        for title, domain, nl in scenarios:
            print("-" * 80)
            print(title)
            print(f"  NL: {nl}")
            print()
            self.discourse.paths = {"interpret": "", "query": "", "reinterpret": ""}
            try:
                trace = self.run_loop(nl, domain)
            except Exception as e:
                # A bad LLM clause can still escape validation; keep the
                # demo running and surface the failure honestly.
                print(f"  [loop failed: {e}]")
                print(f"  discourse path: {self.discourse.path_summary()}")
                print()
                continue

            print(f"  Interpretations : {trace['interpretations']}")
            print(f"  Formal query     : {trace['formal_query']}")
            print(f"  Solutions        : {trace['solutions']}")
            print(f"  Verification     : {trace['verification']}")
            print(f"  Reinterpretation  : {trace['reinterpretation']}")
            print(f"  Discourse path   : {self.discourse.path_summary()}")
            print()

        print("=" * 80)
        print("NOTES")
        print("=" * 80)
        print("When Ollama is up, the Interpret/Formalize/Reinterpret steps are")
        print("done by the model; Derive/Verify stay in SWI-Prolog. Demo 4 emits")
        print("a recursive ancestor/2 rule -- runnable only because the Geometry")
        print("is real Prolog, and formalizable only because the Discourse is a")
        print("real LLM. Neither the toy engine nor the regex layer can do this.")
        print("When Ollama is down, every step falls back to the regex layer, so")
        print("the output matches neuro_symbolic_demo_prolog.py exactly.")
        print("=" * 80)


# ============================================================================
# Interactive Mode
# ============================================================================

def interactive_mode(model: str, host: str):
    """Run in interactive mode: feed natural-language queries to the loop."""
    system = NeuroSymbolicSystem(model=model, host=host)

    print("Interactive Neuro-Symbolic System (Ollama + SWI-Prolog)")
    print(f"  {system.status_line()}")
    print("Type a natural-language statement+question, 'demo', 'status', 'quit'.")
    print()

    while True:
        try:
            cmd = input("ns> ").strip()
            if not cmd:
                continue
            low = cmd.lower()
            if low in ("quit", "exit", "q"):
                print("Goodbye!")
                break
            if low in ("help", "h", "?"):
                print("  <text>   run the neuro-symbolic loop on the text")
                print("  demo      run the demonstration scenarios")
                print("  status    show Ollama availability and model")
                print("  quit      exit")
            elif low == "demo":
                system.demonstrate()
            elif low == "status":
                print(f"  {system.status_line()}")
            else:
                system.discourse.paths = {"interpret": "", "query": "", "reinterpret": ""}
                trace = system.run_loop(cmd)
                print("\nTrace:")
                print(f"  Domain          : {trace['domain']}")
                print(f"  Interpretations : {trace['interpretations']}")
                print(f"  Formal query    : {trace['formal_query']}")
                print(f"  Solutions       : {trace['solutions']}")
                print(f"  Verification    : {trace['verification']}")
                print(f"  Reinterpretation : {trace['reinterpretation']}")
                print(f"  Discourse path  : {system.discourse.path_summary()}")
        except KeyboardInterrupt:
            print("\nUse 'quit' to exit")
        except EOFError:
            print()
            break
        except Exception as e:
            print(f"Error: {e}")


# ============================================================================
# Main Entry Point
# ============================================================================

def _defaults():
    host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
    model = os.environ.get("OLLAMA_MODEL", "qwen2.5:7b")
    return host, model


def _print_help():
    host, model = _defaults()
    print("Usage: python neuro_symbolic_demo_ollama.py [options]")
    print("  (no args)            Run the demonstration scenarios")
    print("  --demo, -d           Run the demonstration scenarios")
    print("  --interactive, -i    Interactive REPL")
    print("  --status             Show Ollama availability and installed models")
    print("  --model NAME         Ollama model (default: %(m)s, env OLLAMA_MODEL)" % {"m": model})
    print("  --host URL           Ollama host   (default: %(h)s, env OLLAMA_HOST)" % {"h": host})
    print("  --help, -h           Show this help")
    print()
    print("Prerequisites:")
    print("  SWI-Prolog + 'pip install pyswip requests'")
    print("  Ollama (optional): 'ollama serve' then 'ollama pull <model>'")
    print("  Without Ollama the demo runs in regex-fallback mode.")


def main(argv: List[str]):
    host, model = _defaults()
    mode = "demo"

    i = 1
    while i < len(argv):
        a = argv[i]
        if a in ("--demo", "-d"):
            mode = "demo"
        elif a in ("--interactive", "-i"):
            mode = "interactive"
        elif a == "--status":
            mode = "status"
        elif a in ("--help", "-h"):
            _print_help()
            return 0
        elif a == "--model" and i + 1 < len(argv):
            model = argv[i + 1]; i += 1
        elif a == "--host" and i + 1 < len(argv):
            host = argv[i + 1]; i += 1
        else:
            print(f"Unknown option: {a}")
            print("Use --help for usage information.")
            return 1
        i += 1

    if mode == "status":
        client = OllamaClient(host=host, model=model)
        if client.is_available():
            print(f"Ollama UP at {host}")
            models = client.list_models()
            print(f"Installed models: {models if models else '(none)'}")
            if model in models:
                print(f"Configured model: {model} (present)")
            else:
                print(f"Configured model: {model} (NOT pulled -- run: ollama pull {model})")
        else:
            print(f"Ollama DOWN at {host}")
            print("Start it with 'ollama serve' (or install: winget install Ollama.Ollama).")
        return 0

    if mode == "interactive":
        interactive_mode(model, host)
        return 0

    system = NeuroSymbolicSystem(model=model, host=host)
    system.demonstrate()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
