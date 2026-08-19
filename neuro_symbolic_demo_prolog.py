#!/usr/bin/env python3
"""
Neuro-Symbolic AI Demonstration (SWI-Prolog backend)
====================================================

This is the Prolog-backed counterpart to ``neuro_symbolic_demo.py``.

The zero-dependency ``neuro_symbolic_demo.py`` ships a minimal Prolog-like
engine written in pure Python (~400 lines) so the whole system runs anywhere.
This file swaps the "Geometry" half for a real SWI-Prolog engine via the
``pyswip`` binding, while keeping the same class names, public interface,
demo scenarios, and interactive mode -- so the two versions are directly
comparable.

Why a real Prolog backend?
-------------------------
The toy engine implements only ground facts, definite rules, and a fixed
depth-limited backward chainer. It has no lists, no real recursion, no
negation, no arithmetic beyond a few builtins, and no constraint solving.
The moment you plug in a real LLM that emits idiomatic Prolog, the toy
engine becomes the bottleneck: it cannot run ``member/2``, recursive
``ancestor/2``, DCGs, or CLP(FD). A real Prolog removes that ceiling and
lets the formal-constraint half of the neuro-symbolic loop do what the
essay actually claims for it.

Prerequisites
-------------
1. SWI-Prolog (>= 9.1 recommended; 10.x tested).
   Windows:  winget install SWI-Prolog.SWI-Prolog
   macOS:    brew install swi-prolog
   Ubuntu:   sudo apt install swi-prolog

2. The Python binding ``pyswip``:
   pip install pyswip

``pyswip`` locates the SWI-Prolog shared library automatically on Windows
and via ``swipl`` on PATH on Unix. If you get ``SwiPrologNotFoundError``,
SWI-Prolog is not installed or not on PATH.

What is identical to the zero-dep version
----------------------------------------
- Class names and public API: ``PrologEngine``, ``LLMDiscourse``,
  ``NeuroSymbolicSystem``.
- The ``LLMDiscourse`` natural-language layer (regex-based pattern
  interpretation, query extraction, reinterpretation). It is deliberately
  kept identical so the two versions differ only in the reasoning engine
  and can be compared directly. It also keeps this version runnable
  offline with no API key.

What is different
-----------------
- ``PrologEngine`` is a thin wrapper around ``pyswip.Prolog``. Real
  backward chaining, unification, recursion, lists, and builtins are
  delegated to SWI-Prolog.
- Demo 6 ("Real Prolog Power") exercises recursion and lists -- programs
  the toy engine cannot run at all.

Extension point
---------------
The regex ``LLMDiscourse`` is a stand-in for a real LLM. To use an actual
LLM, subclass ``LLMDiscourse`` and override ``interpret`` and
``_extract_query`` to call a model (local via Ollama, or a hosted API)
that returns structured ``{facts, rules, query}`` output. The
``PrologEngine`` half needs no changes -- real Prolog accepts idiomatic
clauses an LLM will naturally produce.
"""

import re
import sys
from typing import List, Dict, Tuple, Optional, Set

try:
    from pyswip import Prolog
except ImportError as e:
    raise ImportError(
        "pyswip is required for neuro_symbolic_demo_prolog.py. "
        "Install it with: pip install pyswip\n"
        "SWI-Prolog must also be installed (see the module docstring)."
    ) from e


# ============================================================================
# GEOMETRY: SWI-Prolog wrapper (same interface as the toy engine)
# ============================================================================

class PrologEngine:
    """
    Thin wrapper around SWI-Prolog via pyswip, exposing the same public
    interface as the pure-Python engine in neuro_symbolic_demo.py.

    Real Prolog provides: full backward chaining, unification, recursion,
    lists, negation, arithmetic, and constraint solving. The toy engine
    provides only a subset; this wrapper removes that ceiling.

    Interface parity with the zero-dep version:
        add_fact(fact), add_rule(rule), load_program(program),
        query(goal), query_all(goal), format_solutions(solutions, query),
        facts (set-like, for clear()), rules (list-like, for clear()).
    """

    # Class-level: pyswip.Prolog is a singleton, so all PrologEngine instances
    # share one SWI-Prolog database. Track asserted predicates here so clear()
    # retracts everything any instance ever loaded, not just the current one.
    _loaded_preds: Set[str] = set()

    def __init__(self):
        self._prolog = Prolog()
        # Expose facts/rules attributes for compatibility with code that
        # calls .facts.clear() / .rules.clear() (the demos do this).
        self.facts = _ClearProxy(self)
        self.rules = _ClearProxy(self)

    # -- predicate tracking -------------------------------------------------

    def _pred_indicator(self, clause: str) -> Optional[str]:
        """Extract 'name/arity' from a clause's head (for retractall)."""
        clause = clause.strip().rstrip('.')
        head = clause.split(':-')[0].strip()
        if '(' in head and head.endswith(')'):
            name, args_str = head.split('(', 1)
            args_str = args_str.rstrip(')')
            # Count top-level commas (args may contain no nested commas in
            # the demo programs; for robustness we count naively).
            arity = 1 + args_str.count(',') if args_str.strip() else 0
            return f"{name.strip()}/{arity}"
        return f"{head}/0"

    def _track(self, clause: str):
        ind = self._pred_indicator(clause)
        if ind:
            self._loaded_preds.add(ind)

    # -- clause validation --------------------------------------------------

    def is_static_predicate(self, name: str, arity: int) -> bool:
        """
        True if ``name/arity`` is an existing static predicate -- a builtin
        (``is/2``, ``=/2``) or a library predicate (``member/2``, ``append/2``)
        -- that cannot be (re)defined via ``assertz``. Undefined predicates
        and predicates the user has already asserted (which become dynamic)
        return False. Used to drop LLM-emitted clauses that would otherwise
        raise ``permission_error(modify, static_procedure, ...)``.
        """
        head = name if arity <= 0 else f"{name}({', '.join(['_'] * arity)})"
        try:
            return bool(list(self._prolog.query(
                f"predicate_property({head}, static)")))
        except Exception:
            return False

    def is_assertable(self, clause: str) -> bool:
        """False if ``clause``'s head predicate is a static builtin/library
        predicate (so it cannot be asserted); True otherwise."""
        ind = self._pred_indicator(clause)
        if not ind:
            return True
        name, arity = ind.split("/")
        return not self.is_static_predicate(name, int(arity))

    # -- mutation ----------------------------------------------------------

    def add_fact(self, fact: str):
        """Add a fact to the knowledge base."""
        fact = fact.strip()
        if fact and not fact.startswith('%') and not fact.startswith('/*'):
            fact = fact.rstrip('.')
            self._prolog.assertz(fact)
            self._track(fact)

    def add_rule(self, rule: str):
        """Add a rule to the knowledge base."""
        rule = rule.strip()
        if rule and not rule.startswith('%') and not rule.startswith('/*'):
            rule = rule.rstrip('.')
            self._prolog.assertz(rule)
            self._track(rule)

    def load_program(self, program: str):
        """Load a complete Prolog program, replacing the current KB."""
        self.clear()
        for line in program.split('\n'):
            line = line.strip()
            if not line or line.startswith('%') or line.startswith('/*'):
                continue
            if ':-' in line:
                self.add_rule(line)
            elif line.endswith('.'):
                self.add_fact(line)
            else:
                self.add_fact(line + '.')

    def clear(self):
        """Retract all user-asserted predicates."""
        for ind in self._loaded_preds:
            name, arity = ind.split('/')
            arity = int(arity)
            if arity == 0:
                self._prolog.retractall(name)
            else:
                self._prolog.retractall(f"{name}({', '.join(['_'] * arity)})")
        self._loaded_preds.clear()

    # -- querying -----------------------------------------------------------

    def query(self, goal: str) -> List[Dict[str, str]]:
        """
        Query the knowledge base. Returns a list of binding dicts.
        A ground query that succeeds returns [{}] (truthy, non-empty);
        a failing query returns [] (falsy). This matches the semantics
        the rest of the code relies on (``len(solutions) > 0``).

        The goal is wrapped in catch/3 so that calling an undefined
        predicate (one the Discourse layer asked about but never
        formalized -- e.g. ``grandparent(X, bob)`` when only ``parent/2``
        facts were loaded) fails gracefully with no solutions instead of
        raising ``existence_error``. This matches the toy engine's lenient
        behavior and keeps the neuro-symbolic loop from crashing when the
        LLM/regex emits a query whose predicate has no clauses. Other
        errors (type errors, syntax errors, ...) still propagate.
        """
        goal = goal.strip().rstrip('.')
        wrapped = f"catch(({goal}), error(existence_error(procedure, _), _), fail)"
        solutions = list(self._prolog.query(wrapped))
        # Normalize values to plain strings for display parity with the
        # toy engine. Lists and numbers stringify naturally.
        normalized = []
        for sol in solutions:
            norm = {k: self._stringify(v) for k, v in sol.items()}
            normalized.append(norm)
        return normalized

    def query_all(self, goal: str) -> List[Dict[str, str]]:
        """Find all solutions to a query."""
        return self.query(goal)

    @staticmethod
    def _stringify(value) -> str:
        """Render a Prolog value as a display string."""
        return str(value)

    # -- formatting (same output format as the toy engine) -----------------

    def _extract_query_vars(self, query: str) -> Set[str]:
        """Extract variable names from a query string."""
        vars_found = set()
        for match in re.finditer(r'\b[A-Z][A-Za-z0-9_]*\b', query):
            vars_found.add(match.group())
        return vars_found

    def format_solutions(self, solutions: List[Dict[str, str]], query: str = None) -> str:
        """Format query solutions readably, showing only query variables."""
        if not solutions:
            return "false."

        query_vars = self._extract_query_vars(query) if query else None

        results = []
        for sol in solutions:
            if sol:
                if query_vars is not None:
                    filtered = {k: v for k, v in sol.items() if k in query_vars}
                    if filtered:
                        bindings = ", ".join(f"{k} = {v}" for k, v in sorted(filtered.items()))
                        results.append(f"{{{bindings}}}")
                    else:
                        results.append("true")
                else:
                    bindings = ", ".join(f"{k} = {v}" for k, v in sorted(sol.items()))
                    results.append(f"{{{bindings}}}")
            else:
                results.append("true")

        return " ;\n".join(results) + "."


class _ClearProxy:
    """
    Minimal proxy so code written for the toy engine's ``.facts.clear()``
    and ``.rules.clear()`` works unchanged. Both delegate to the engine's
    full ``clear()`` (real Prolog does not separate facts from rules).
    """

    def __init__(self, engine: PrologEngine):
        self._engine = engine

    def clear(self):
        self._engine.clear()


# ============================================================================
# DISCOURSE: LLM Interface Simulator (identical to the zero-dep version)
# ============================================================================

class LLMDiscourse:
    """
    Simulates an LLM as the 'Discourse' component.

    This is the same regex-based pattern-action interpreter as in
    neuro_symbolic_demo.py, kept identical so the two versions differ
    only in the reasoning engine. See the module docstring for how to
    replace it with a real LLM.
    """

    def __init__(self, prolog_engine: PrologEngine):
        self.prolog = prolog_engine
        self.domain_knowledge = {}
        self._init_domain_knowledge()

    @staticmethod
    def _singularize(word: str) -> str:
        """Reduce a plural noun to its singular form (best-effort heuristic)."""
        word = word.lower()
        if word in ('men', 'women'):
            return word[:-2] + 'an'  # men -> man, women -> woman
        if word.endswith('ies') and len(word) > 3:
            return word[:-3] + 'y'   # cities -> city
        if word.endswith('s') and not word.endswith('ss'):
            return word[:-1]         # dogs -> dog
        return word

    def _init_domain_knowledge(self):
        """Initialize with some domain-specific templates"""
        # Classical logic
        self.domain_knowledge['classical_logic'] = {
            'interpreters': {
                r'(?i)\b(all|every)\s+(\w+)\s+are\s+(\w+)':
                    lambda m: f"{self._singularize(m.group(3))}(X) :- {self._singularize(m.group(2))}(X).",
                r'(?i)\b(some|a|an)\s+(\w+)\s+are\s+(\w+)':
                    lambda m: f"{self._singularize(m.group(3))}(X) :- {self._singularize(m.group(2))}(X).",
                r'(?i)(\w+)\s+is\s+a\s+(\w+)':
                    lambda m: f"{m.group(2).lower()}({m.group(1).lower()}).",
                r'(?i)(\w+)\s+is\s+(?!a\b|an\b|the\b)(\w+)':
                    lambda m: f"{m.group(2).lower()}({m.group(1).lower()}).",
            },
            'reinterpreters': {
                'true': 'Yes, that is correct.',
                'false': 'No, that is not true based on the available knowledge.',
            }
        }

        # Family relationships
        self.domain_knowledge['family'] = {
            'interpreters': {
                r'(?i)(\w+)\s+is\s+the\s+(mother|father|parent)\s+of\s+(\w+)':
                    lambda m: f"parent({m.group(1).lower()}, {m.group(3).lower()}).",
                r'(?i)(\w+)\s+is\s+the\s+(son|daughter|child)\s+of\s+(\w+)':
                    lambda m: f"parent({m.group(3).lower()}, {m.group(1).lower()}).",
                r'(?i)(\w+)\s+and\s+(\w+)\s+are\s+siblings':
                    lambda m: f"parent(X, {m.group(1).lower()}), parent(X, {m.group(2).lower()}).",
            },
            'reinterpreters': {}
        }

        # Planning/Logistics
        self.domain_knowledge['planning'] = {
            'interpreters': {
                r'(?i)\b(create|define)\s+a\s+task\s+(\w+)\s+that\s+requires\s+(.+)':
                    lambda m: self._parse_requirements(m.group(2), m.group(1)),
                r'(?i)\b(task\s+(\w+)\s+requires\s+(.+))':
                    lambda m: self._parse_requirements(m.group(2), m.group(1)),
            },
            'reinterpreters': {}
        }

    def _parse_requirements(self, requirements: str, task: str) -> str:
        """Parse task requirements into Prolog rules"""
        return f"requires({task}, {requirements})."

    def interpret(self, text: str, domain: str = None) -> List[str]:
        """Interpret natural language text and generate Prolog representations."""
        results = []

        if domain is None:
            domain = self._infer_domain(text)

        if domain in self.domain_knowledge:
            patterns = self.domain_knowledge[domain].get('interpreters', {})
            for pattern, handler in patterns.items():
                for match in re.finditer(pattern, text):
                    try:
                        prolog_text = handler(match)
                        if prolog_text:
                            results.append(prolog_text)
                    except:
                        pass

        # General fallbacks
        if not results:
            results = self._general_interpretation(text)

        return results

    def _infer_domain(self, text: str) -> str:
        """Infer the most likely domain from the text"""
        text_lower = text.lower()

        if any(word in text_lower for word in ['mother', 'father', 'parent', 'sibling', 'child']):
            return 'family'
        elif any(word in text_lower for word in ['task', 'require', 'plan', 'schedule']):
            return 'planning'
        elif any(word in text_lower for word in ['all', 'every', 'some', 'are', 'is a']):
            return 'classical_logic'
        else:
            return 'general'

    def _general_interpretation(self, text: str) -> List[str]:
        """General interpretation fallback"""
        results = []

        # Pattern: X is a Y
        matches = re.findall(r'(\w+)\s+is\s+(?:a|an|the)\s+(\w+)', text, re.IGNORECASE)
        for subj, obj in matches:
            results.append(f"{obj.lower()}({subj.lower()}).")

        # Pattern: X are Y
        matches = re.findall(r'(\w+)\s+are\s+(\w+)', text, re.IGNORECASE)
        for subj, obj in matches:
            results.append(f"{obj.lower()}({subj.lower()}).")

        # Pattern: X has Y
        matches = re.findall(r'(\w+)\s+has\s+(\w+)', text, re.IGNORECASE)
        for subj, obj in matches:
            results.append(f"has({subj.lower()}, {obj.lower()}).")

        # Pattern: X Y Z (verb pattern) -- skip copulas/stopwords so we never
        # emit clauses like is(X, Y) that collide with Prolog builtins.
        matches = re.findall(r'(\w+)\s+(\w+)\s+(\w+)', text)
        for subj, verb, obj in matches:
            v = verb.lower()
            if v in ('is', 'are', 'was', 'were', 'a', 'an', 'the', 'has', 'have', 'had'):
                continue
            results.append(f"{v}({subj.lower()}, {obj.lower()}).")

        return results if results else [f"% Interpreted: {text}"]

    def formalize(self, text: str, domain: str = None) -> str:
        """Convert natural language to a complete Prolog program."""
        interpretations = self.interpret(text, domain)
        return "\n".join(interpretations)

    def derive(self, query_text: str, context: str = None) -> Tuple[str, List[Dict[str, str]]]:
        """Derive answers from the formal system."""
        solutions = self.prolog.query(query_text)
        formal_query = query_text
        return formal_query, solutions

    def verify(self, statement: str) -> bool:
        """Verify if a statement is true in the formal system"""
        solutions = self.prolog.query(statement)
        return len(solutions) > 0

    def reinterpret(self, solutions: List[Dict[str, str]], original_query: str = None) -> str:
        """Reinterpret formal results back into natural language."""
        if not solutions:
            return "No solutions found. The statement is false given the current knowledge."

        results = []
        for sol in solutions:
            if not sol:
                results.append("Yes, that is true.")
            else:
                bindings = ", ".join(f"{k} is {v}" for k, v in sol.items())
                results.append(f"Solution: {bindings}")

        return "\n".join(results)

    def loop(self, natural_language_query: str, domain: str = None,
             max_iterations: int = 3) -> Dict:
        """Execute the complete neuro-symbolic loop."""
        trace = {
            'natural_query': natural_language_query,
            'domain': domain or self._infer_domain(natural_language_query),
            'interpretations': [],
            'formal_query': None,
            'solutions': [],
            'verification': None,
            'reinterpretation': None,
            'iterations': []
        }

        # Start from a clean knowledge base so the loop is self-contained
        self.prolog.clear()

        for iteration in range(max_iterations):
            iteration_trace = {
                'iteration': iteration + 1,
                'input': natural_language_query if iteration == 0 else trace['reinterpretation']
            }

            # Step 1: Interpret (LLM)
            if iteration == 0:
                interpretations = self.interpret(natural_language_query, trace['domain'])
                trace['interpretations'] = interpretations
                iteration_trace['interpretations'] = interpretations

                # Step 2: Formalize (LLM) - load into Prolog
                # Accumulate facts and rules rather than reloading (which clears)
                for prog in interpretations:
                    if ':-' in prog:
                        self.prolog.add_rule(prog)
                    else:
                        self.prolog.add_fact(prog)

                # For demo, we'll use a hardcoded query or extract one
                formal_query = self._extract_query(natural_language_query, trace['domain'])
                trace['formal_query'] = formal_query
                iteration_trace['formal_query'] = formal_query

                # Step 3: Derive (Prolog/Geometry)
                formal_query_for_engine, solutions = self.derive(formal_query)
                trace['solutions'] = solutions
                iteration_trace['solutions'] = solutions

                # Step 4: Verify (Prolog)
                verification = self.verify(formal_query)
                trace['verification'] = verification
                iteration_trace['verification'] = verification

                # Step 5: Reinterpret (LLM)
                reinterpretation = self.reinterpret(solutions, formal_query)
                trace['reinterpretation'] = reinterpretation
                iteration_trace['reinterpretation'] = reinterpretation

            trace['iterations'].append(iteration_trace)

            # Step 6: Revise - check if we need another iteration
            break

        return trace

    def _extract_query(self, text: str, domain: str) -> str:
        """Extract a Prolog query from natural language"""
        text_lower = text.lower()

        if domain == 'family':
            # "Who is the parent of Mary?" -> parent(X, mary)
            matches = re.findall(r'(?i)who\s+(is|are)\s+the\s+(\w+)\s+of\s+(\w+)', text)
            if matches:
                _, rel, obj = matches[0]
                return f"{rel}(X, {obj.lower()})."

            # "Is John the parent of Mary?" -> parent(john, mary)
            matches = re.findall(r'(?i)is\s+(\w+)\s+the\s+(\w+)\s+of\s+(\w+)', text)
            if matches:
                subj, rel, obj = matches[0]
                return f"{rel}({subj.lower()}, {obj.lower()})."

            # "Are X and Y siblings?" -> parent(Z, X), parent(Z, Y)
            matches = re.findall(r'(?i)are\s+(\w+)\s+and\s+(\w+)\s+siblings', text)
            if matches:
                a, b = matches[0]
                return f"parent(Z, {a.lower()}), parent(Z, {b.lower()})."

        elif domain == 'classical_logic':
            # Yes/no question: "Is Socrates a man?" -> man(socrates)
            m = re.search(r'(?i)\bis\s+(\w+)\s+(?:a|an)\s+(\w+)\s*\?', text)
            if m:
                return f"{m.group(2).lower()}({m.group(1).lower()})."
            # Yes/no question: "Is Socrates mortal?" -> mortal(socrates)
            m = re.search(r'(?i)\bis\s+(\w+)\s+(\w+)\s*\?', text)
            if m:
                return f"{m.group(2).lower()}({m.group(1).lower()})."
            # "Who is mortal?" -> mortal(X)
            m = re.search(r'(?i)\bwho\s+(?:is|are)\s+(\w+)', text)
            if m:
                return f"{m.group(1).lower()}(X)."

        # Default: try to find a predicate pattern
        words = text.split()
        if words:
            clean = re.sub(r'[?\.]', '', text).strip()
            first_word = words[0].lower()
            if first_word in ['who', 'what', 'which', 'is', 'are']:
                if len(words) > 1:
                    return f"{words[1].lower()}(X)."
            return f"{first_word}(X)."

        return "true."


# ============================================================================
# Neuro-Symbolic System: Combining Discourse and Geometry
# ============================================================================

class NeuroSymbolicSystem:
    """
    Complete neuro-symbolic AI system combining LLM (Discourse) and Prolog (Geometry).

    Identical in role to the zero-dep version; the difference is that the
    Geometry half is real SWI-Prolog, so it can run programs the toy engine
    cannot (recursion, lists, negation, constraints).
    """

    def __init__(self):
        self.geometry = PrologEngine()
        self.discourse = LLMDiscourse(self.geometry)

    def run_loop(self, query: str, domain: str = None) -> Dict:
        """Run the complete neuro-symbolic loop"""
        return self.discourse.loop(query, domain)

    def demonstrate(self):
        """Run a series of demonstrations showing the neuro-symbolic approach"""
        print("=" * 80)
        print("NEURO-SYMBOLIC AI DEMONSTRATION (SWI-Prolog backend)")
        print("From Plato to Prolog to Prompts: The 2,500-Year Journey to Artificial Reason")
        print("=" * 80)
        print()

        print("DEMO 1: CLASSICAL LOGIC (Aristotle's Syllogism)")
        print("-" * 80)
        self.demo_classical_logic()
        print()

        print("DEMO 2: FAMILY RELATIONSHIPS (Platonic Ontology)")
        print("-" * 80)
        self.demo_family_relationships()
        print()

        print("DEMO 3: EXPERT SYSTEM (Medical Diagnosis - like MYCIN)")
        print("-" * 80)
        self.demo_expert_system()
        print()

        print("DEMO 4: PLANNING (Constraint-Based Reasoning)")
        print("-" * 80)
        self.demo_planning()
        print()

        print("DEMO 5: THE COMPLETE NEURO-SYMBOLIC LOOP")
        print("-" * 80)
        self.demo_complete_loop()
        print()

        print("DEMO 6: REAL PROLOG POWER (recursion and lists)")
        print("-" * 80)
        self.demo_real_prolog_power()
        print()

        print("=" * 80)
        print("CONCLUSION")
        print("=" * 80)
        print("Demos 1-5 mirror the zero-dependency version and produce the same")
        print("results, showing the toy engine and SWI-Prolog agree on the basics.")
        print("Demo 6 goes beyond what the toy engine can do: unbounded recursion")
        print("(ancestor/2) and list membership (member/2) -- programs the pure-Python")
        print("engine cannot run at all.")
        print()
        print("This is the point of using a real Prolog: the formal-constraint half")
        print("of the neuro-symbolic loop is no longer the bottleneck. An LLM that")
        print("emits idiomatic Prolog can be paired with an engine that actually runs it.")
        print("=" * 80)

    def demo_classical_logic(self):
        """Demonstrate classical syllogistic reasoning"""
        print("\nScenario: Aristotle's classic syllogism")
        print('  Natural language: "All men are mortal. Socrates is a man. Is Socrates mortal?"')
        print()

        self.geometry.clear()
        program = """
% Classical logic: Aristotle's syllogism
man(socrates).
man(plato).
man(aristotle).

mortal(X) :- man(X).
        """
        self.geometry.load_program(program)

        print("Formal representation (Geometry):")
        print("  man(socrates).")
        print("  man(plato).")
        print("  man(aristotle).")
        print("  mortal(X) :- man(X).")
        print()

        print("Query: mortal(socrates).")
        solutions = self.geometry.query("mortal(socrates)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'mortal(socrates)')}")
        print()

        print("Reinterpretation (Discourse):")
        print("  Yes, Socrates is mortal.")
        print()

        print("Query: mortal(X).")
        solutions = self.geometry.query("mortal(X)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'mortal(X)')}")
        print()
        print("Reinterpretation: All known men (Socrates, Plato, Aristotle) are mortal.")

    def demo_family_relationships(self):
        """Demonstrate ontology and relationship reasoning"""
        print("\nScenario: Family tree reasoning")
        print('  Natural language: "John is the father of Mary. Mary is the mother of Bob.')
        print('                     Who is the grandparent of Bob?"')
        print()

        self.geometry.clear()
        program = """
% Family relationships
parent(john, mary).
parent(mary, bob).
parent(john, tom).
parent(susan, mary).

% Gender facts
male(john).
male(tom).
male(bob).
female(mary).
female(susan).

% Define parent relationships
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

% Grandparent relationship
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
        """
        self.geometry.load_program(program)

        print("Formal representation (Geometry):")
        print("  parent(john, mary).")
        print("  parent(mary, bob).")
        print("  father(X, Y) :- parent(X, Y), male(X).")
        print("  grandparent(X, Z) :- parent(X, Y), parent(Y, Z).")
        print()

        print("Query: grandparent(X, bob).")
        solutions = self.geometry.query("grandparent(X, bob)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'grandparent(X, bob)')}")
        print()
        print("Reinterpretation (Discourse):")
        print("  John and Susan are the grandparents of Bob.")
        print()

        print("Query: father(X, mary).")
        solutions = self.geometry.query("father(X, mary)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'father(X, mary)')}")
        print()
        print("Reinterpretation: John is the father of Mary.")

    def demo_expert_system(self):
        """Demonstrate expert system reasoning (like MYCIN)"""
        print("\nScenario: Medical diagnosis (simplified MYCIN-like system)")
        print('  Natural language: "The patient has fever and cough.')
        print('                     What could be the diagnosis?"')
        print()

        self.geometry.clear()
        program = """
% Medical expert system

% Symptoms
symptom(patient1, fever).
symptom(patient1, cough).
symptom(patient1, headache).
symptom(patient2, rash).
symptom(patient2, fever).

% Possible diagnoses
diagnosis(flu, X) :- symptom(X, fever), symptom(X, cough).
diagnosis(cold, X) :- symptom(X, cough), symptom(X, headache).
diagnosis(measles, X) :- symptom(X, rash), symptom(X, fever).

% Severity
severe(flu).
mild(cold).
mild(measles).
        """
        self.geometry.load_program(program)

        print("Formal representation (Geometry):")
        print("  symptom(patient1, fever).")
        print("  symptom(patient1, cough).")
        print("  diagnosis(flu, X) :- symptom(X, fever), symptom(X, cough).")
        print()

        print("Query: diagnosis(Disease, patient1).")
        solutions = self.geometry.query("diagnosis(Disease, patient1)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'diagnosis(Disease, patient1)')}")
        print()
        print("Reinterpretation (Discourse):")
        for sol in solutions:
            disease = sol.get('Disease', 'unknown')
            print(f"  Possible diagnosis: {disease.capitalize()}")
        print()

        print("Query: diagnosis(D, patient1), severe(D).")
        solutions = self.geometry.query("diagnosis(D, patient1), severe(D)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'diagnosis(D, patient1), severe(D)')}")
        print()
        print("Reinterpretation: Flu is a severe diagnosis for patient1.")

    def demo_planning(self):
        """Demonstrate constraint-based planning"""
        print("\nScenario: Task scheduling with prerequisites")
        print('  Natural language: "We need to build a house.')
        print('                     Foundation must come before walls.')
        print('                     Walls must come before roof.')
        print('                     Roof must come before painting.')
        print('                     What tasks must come before painting?"')
        print()

        self.geometry.clear()
        program = """
% Task planning with prerequisites
task(foundation).
task(walls).
task(roof).
task(painting).

before(foundation, walls).
before(walls, roof).
before(roof, painting).

% Direct prerequisite
direct_prereq(A, B) :- before(A, B).

% Two-step prerequisite
two_step_prereq(A, C) :- before(A, B), before(B, C).

% Three-step prerequisite
three_step_prereq(A, D) :- before(A, B), before(B, C), before(C, D).
        """
        self.geometry.load_program(program)

        print("Formal representation (Geometry):")
        print("  task(foundation). task(walls). task(roof). task(painting).")
        print("  before(foundation, walls). before(walls, roof). before(roof, painting).")
        print("  direct_prereq(A, B) :- before(A, B).")
        print("  two_step_prereq(A, C) :- before(A, B), before(B, C).")
        print()

        print("Query: direct_prereq(X, painting).")
        solutions = self.geometry.query("direct_prereq(X, painting)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'direct_prereq(X, painting)')}")
        print()

        print("Query: two_step_prereq(X, painting).")
        solutions = self.geometry.query("two_step_prereq(X, painting)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'two_step_prereq(X, painting)')}")
        print()

        print("Query: three_step_prereq(X, painting).")
        solutions = self.geometry.query("three_step_prereq(X, painting)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'three_step_prereq(X, painting)')}")
        print()

        print("Reinterpretation (Discourse):")
        print("  To paint, you must first complete: roof (direct),")
        print("  walls (2-step), and foundation (3-step).")

    def demo_complete_loop(self):
        """Demonstrate the complete neuro-symbolic loop"""
        print("\nScenario: Complete loop - from natural language to formal reasoning and back")
        print()

        natural_query = "John is the father of Mary. Mary is the mother of Bob. Who is the grandfather of Bob?"

        print(f"Natural language query: {natural_query}")
        print()

        print("Step 1-2: INTERPRET & FORMALIZE (Discourse -> Geometry)")
        self.geometry.clear()

        print("  LLM interprets the relationships and generates:")
        formal_facts = [
            "parent(john, mary).",
            "parent(mary, bob).",
            "male(john).",
            "female(mary)."
        ]
        for fact in formal_facts:
            print(f"    {fact}")
            self.geometry.add_fact(fact)

        formal_rule = "grandfather(X, Z) :- parent(X, Y), parent(Y, Z), male(X)."
        print(f"    {formal_rule}")
        self.geometry.add_rule(formal_rule)
        print()

        print("Step 3: DERIVE (Geometry)")
        query = "grandfather(X, bob)"
        print(f"  Query: {query}")
        solutions = self.geometry.query(query)
        print(f"  Formal result: {self.geometry.format_solutions(solutions, query)}")
        print()

        print("Step 4: VERIFY (Geometry)")
        is_verified = self.geometry.query("grandfather(john, bob)")
        print(f"  Verify grandfather(john, bob): {self.geometry.format_solutions(is_verified, 'grandfather(john, bob)')}")
        print()

        print("Step 5: REINTERPRET (Discourse)")
        if solutions:
            binding = solutions[0]
            grandfather = binding.get('X', 'unknown')
            print(f"  Natural language answer: {grandfather.capitalize()} is the grandfather of Bob.")
        else:
            print("  Natural language answer: No grandfather found for Bob.")
        print()

        print("Step 6: REVISE (Loop)")
        print("  If the answer is unsatisfactory, the LLM can refine the formalization")
        print("  and the loop continues. In this case, the answer is correct,")
        print("  so we stop here.")

    def demo_real_prolog_power(self):
        """
        Demonstrate capabilities the pure-Python toy engine cannot provide:
        unbounded recursion and list membership.

        The toy engine has a hard depth limit and no list data type, so it
        cannot run either of these programs. SWI-Prolog runs them natively.
        """
        print("\nScenario: Programs the toy engine cannot run")
        print("  (unbounded recursion + list membership)")
        print()

        self.geometry.clear()
        program = """
% Recursive ancestor: the toy engine's depth limit caps this; real Prolog
% resolves it to arbitrary depth via proper recursion.
parent(john, mary).
parent(mary, bob).
parent(bob, alice).
parent(alice, charlie).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).

% List membership: the toy engine has no list data type at all.
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).
        """
        self.geometry.load_program(program)

        print("Formal representation (Geometry):")
        print("  parent(john, mary). parent(mary, bob). parent(bob, alice). parent(alice, charlie).")
        print("  ancestor(X, Y) :- parent(X, Y).")
        print("  ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).")
        print("  member(X, [X|_]).")
        print("  member(X, [_|T]) :- member(X, T).")
        print()

        print("Query: ancestor(X, charlie).  (4 generations deep)")
        solutions = self.geometry.query("ancestor(X, charlie)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'ancestor(X, charlie)')}")
        print()

        print("Query: ancestor(john, X).  (all descendants of john)")
        solutions = self.geometry.query("ancestor(john, X)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'ancestor(john, X)')}")
        print()

        print("Query: member(3, [1, 2, 3, 4]).  (list membership)")
        solutions = self.geometry.query("member(3, [1, 2, 3, 4])")
        print(f"Result: {self.geometry.format_solutions(solutions, 'member(3, [1, 2, 3, 4])')}")
        print()

        print("Query: member(X, [socrates, plato, aristotle]).  (enumerate list)")
        solutions = self.geometry.query("member(X, [socrates, plato, aristotle])")
        print(f"Result: {self.geometry.format_solutions(solutions, 'member(X, [socrates, plato, aristotle])')}")
        print()

        print("Reinterpretation (Discourse):")
        print("  John is an ancestor of Charlie through 4 generations; the recursive")
        print("  rule resolves the full chain. List membership enumerates or tests")
        print("  membership in O(n) -- neither is expressible in the toy engine.")


# ============================================================================
# Interactive Mode
# ============================================================================

def interactive_mode():
    """Run in interactive mode"""
    system = NeuroSymbolicSystem()

    print("Interactive Neuro-Symbolic System (SWI-Prolog backend)")
    print("Type 'help' for commands, 'quit' to exit, 'demo' to run demonstrations")
    print()

    while True:
        try:
            cmd = input("ns> ").strip()

            if not cmd:
                continue

            if cmd.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break

            elif cmd.lower() in ['help', 'h', '?']:
                print("\nCommands:")
                print("  help, h, ?      - Show this help")
                print("  quit, exit, q   - Quit the system")
                print("  demo            - Run all demonstrations")
                print("  clear           - Clear the knowledge base")
                print("  load <file>     - Load a Prolog program from file")
                print("  assert <fact>   - Add a fact to the knowledge base")
                print("  rule <rule>     - Add a rule to the knowledge base")
                print("  query <goal>    - Query the knowledge base")
                print("  natural <text>  - Process natural language query")
                print()

            elif cmd.lower() in ['demo', 'demos']:
                system.demonstrate()

            elif cmd.lower() in ['clear', 'reset']:
                system.geometry.clear()
                print("Knowledge base cleared.")

            elif cmd.lower().startswith('load '):
                filename = cmd[5:].strip()
                try:
                    with open(filename, 'r') as f:
                        program = f.read()
                    system.geometry.load_program(program)
                    print(f"Loaded {filename}")
                except FileNotFoundError:
                    print(f"File not found: {filename}")
                except Exception as e:
                    print(f"Error: {e}")

            elif cmd.lower().startswith('assert '):
                fact = cmd[7:].strip().rstrip('.')
                system.geometry.add_fact(fact)
                print(f"Added fact: {fact}")

            elif cmd.lower().startswith('rule '):
                rule = cmd[5:].strip().rstrip('.')
                system.geometry.add_rule(rule)
                print(f"Added rule: {rule}")

            elif cmd.lower().startswith('query '):
                query = cmd[6:].strip().rstrip('.')
                solutions = system.geometry.query(query)
                print(system.geometry.format_solutions(solutions, query))

            elif cmd.lower().startswith('natural '):
                text = cmd[8:].strip()
                trace = system.run_loop(text)
                print("\nTrace:")
                print(f"  Domain: {trace['domain']}")
                print(f"  Interpretations: {trace['interpretations']}")
                print(f"  Formal query: {trace['formal_query']}")
                print(f"  Solutions: {trace['solutions']}")
                print(f"  Verification: {trace['verification']}")
                print(f"  Reinterpretation: {trace['reinterpretation']}")

            else:
                # Try as a query
                solutions = system.geometry.query(cmd)
                print(system.geometry.format_solutions(solutions, cmd))

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

if __name__ == "__main__":
    # Check if there are command-line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--demo', '-d']:
            system = NeuroSymbolicSystem()
            system.demonstrate()
        elif sys.argv[1] in ['--interactive', '-i']:
            interactive_mode()
        elif sys.argv[1] in ['--help', '-h']:
            print("Usage: python neuro_symbolic_demo_prolog.py [--demo | --interactive | --help]")
            print("  --demo, -d        Run demonstrations")
            print("  --interactive, -i  Run in interactive mode")
            print("  --help, -h        Show this help")
            print()
            print("Prerequisites: SWI-Prolog installed + 'pip install pyswip'")
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Use --help for usage information")
    else:
        # Default: run demonstrations
        system = NeuroSymbolicSystem()
        system.demonstrate()
