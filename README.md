<img width="1254" height="1254" alt="Thinker" src="https://github.com/user-attachments/assets/2eb48e46-a29c-476f-a962-5c53acfaa6d0" />
<br><br>
I think, therefore I am...
<br><br>

In the beginning I was mostly using gen AI for code generation, but in the end that became almost trivial because the agents could clearly build anything I wanted.

Now I am experimenting more with text generation. Mostly as a way of creating a record of things that I am thinking about. This repo stil contains some code though! (More and more actually, as the ideas develop...)

Note that these days I am not focusing on writing for publication - it is more about looking for insights that I can actually use. For what exactly? Making Gen AI more trustworthy ansd accountable, which is something I care deepy about both personally and as AI Teamleader at the NTNU University Library.

Broadly speaking this repo tends towards what is called the Neuro-Symbolic tradition, combining Symbolic AI and LLMs.

The philosophical foundations range far and wide, reflecting my background in that subject.

## The Trilogy: Intelligence, Symbol, and Form

This repo hosts a trilogy of essays exploring how symbolic forms shape what intelligence can do:

1. **Language(s) of Thought: A Wittgensteinian View of Fodor and the Gradually Increasing Capabilities of LLMs** ([MD](Language_s_of_Thought.md)) — on why cognition requires acquired formal languages, not a single innate Mentalese.
2. **Symbolic Forms and the Plural Mind** — on Cassirer, the plurality of symbolic forms, and why language alone is not enough.
3. **The Cartesian Moment: Analytical Geometry as Language of Thought** — on Descartes' *Geometry* as the foundational symbolic form that made extension computable, unlocking calculus and mathematical physics.

Together they argue that artificial intelligence, to reach the level of practical scientific reasoning, must master formal symbolic systems — not just natural language.

A related standalone essay, **From Halting Problem to Imitation Game**, explores Turing's learning-machines programme and the subordination of imitation to learning.

A fourth essay in the series, **Constitution and Rule-Change** ([MD](Constitution_and_Rule-Change.md)), brings Wittgenstein's *Remarks on the Foundations of Mathematics* into conversation with Cassirer, arguing that the constitutive claim can be relocated from objects to practices — and that this normative reading is both more defensible and more directly testable against the reasoning-compute trend.

A fifth essay, **The Fork and the Form** ([MD](The_Fork_and_the_Form.md)), situates the series in the empiricism-rationalism debate, arguing that the constitutive claim challenges Hume's fork at its strongest point — the analytic necessity of relations of ideas — and that the asymptote of language-only reasoning is the empirical trace of Hume's underestimation of what formal forms contribute even to the analytic side.

A sixth essay, **From Plato to Prolog to Prompts** ([MD](From_Plato_to_Prolog_to_Prompts.md)), extends the historical arc back to its origins in ancient Greece, arguing that Prolog and GOFAI were not failed paradigms but early instantiations of the Platonic-Aristotelian vision of structured representation and reasoning — and that modern neuro-symbolic AI finally provides the missing interface between formal systems and the open world.

Alternate versions of the second and third essays are also available: **Symbolic Forms and the Plural Mind (Alternate Version)** ([MD](Symbolic_Forms_and_the_Plural_Mind_Alternate_Version.md)) and **The Cartesian Moment (Alternate Version)** ([MD](The_Cartesian_Moment_Alternate_Version.md)).

## Neuro-Symbolic AI Demonstration

To test the ideas from the Plato-to-Prolog essay, three implementations of the neuro-symbolic architecture are included. All implement the bidirectional loop between linguistic interpretation (LLM/Discourse) and formal constraint (Prolog/Geometry) described in the essay. They share the same class names, public interface, and demo scenarios, so they can be compared directly.

### Three versions

| | `neuro_symbolic_demo.py` | `neuro_symbolic_demo_prolog.py` | `neuro_symbolic_demo_ollama.py` |
|---|---|---|---|
| Reasoning engine | Pure-Python toy Prolog (~400 lines) | Real SWI-Prolog via `pyswip` | Real SWI-Prolog via `pyswip` |
| NL layer | Regex (ELIZA-style) | Regex (identical) | **Real LLM via Ollama** (regex fallback) |
| Dependencies | None | SWI-Prolog + `pip install pyswip` | SWI-Prolog + `pyswip` + `requests` + Ollama (optional) |
| Recursion, lists, negation, CLP | No | Yes | Yes |
| Demos 1-5 (syllogism, family, expert, planning, loop) | Yes | Yes (identical) | — |
| Demo 6 (recursive `ancestor`, list `member`) | No | Yes | — |
| Ollama demos (NL -> LLM -> Prolog -> NL) | No | No | Yes (4 scenarios) |
| Best for | Reading the whole engine; running anywhere | Plugging in a real LLM that emits idiomatic Prolog | **Running the loop on an actual LLM** |

The zero-dependency version is a readable artifact: the entire backward-chaining engine is ~400 lines you can follow. The Prolog-backed version removes the ceiling of the toy engine (no lists, no real recursion, depth-limited) so the formal-constraint half of the loop can do what the essay actually claims for it. The Ollama-backed version then replaces the regex Discourse with a real local LLM — and degrades gracefully to the regex layer when Ollama is not running, so it works with no LLM installed.

### Running the zero-dependency version

```bash
python neuro_symbolic_demo.py
python neuro_symbolic_demo.py --interactive
```

### Running the SWI-Prolog version

Prerequisites:
1. **SWI-Prolog** — Windows: `winget install SWI-Prolog.SWI-Prolog`; macOS: `brew install swi-prolog`; Ubuntu: `sudo apt install swi-prolog`
2. **pyswip** — `pip install pyswip`

```bash
python neuro_symbolic_demo_prolog.py
python neuro_symbolic_demo_prolog.py --interactive
```

### Running the Ollama version

Prerequisites: the SWI-Prolog version's prerequisites, plus `pip install requests`, plus Ollama (optional — without it the demo runs in regex-fallback mode):
1. **Ollama** — Windows: `winget install Ollama.Ollama`; macOS: `brew install ollama`; Linux: `curl -fsSL https://ollama.com/install.sh | sh`
2. Start it and pull a model: `ollama serve` then `ollama pull qwen2.5:7b`

```bash
python neuro_symbolic_demo_ollama.py            # run the 4 NL->LLM->Prolog->NL demos
python neuro_symbolic_demo_ollama.py --status   # show Ollama up/down + configured model
python neuro_symbolic_demo_ollama.py --model llama3.1:8b --demo
python neuro_symbolic_demo_ollama.py --interactive
```

The `OLLAMA_MODEL` and `OLLAMA_HOST` environment variables are also honored. See `NEURO_SYMBOLIC_DEMO_GUIDE.md` for the full mechanism (structured-output contract, clause validation, graceful fallback).

### What the demonstrations show

The zero-dep and Prolog versions demonstrate:
- Classical logic (Aristotle's syllogisms)
- Family relationship reasoning (ontology)
- Expert systems (MYCIN-like medical diagnosis)
- Planning with constraints
- The complete neuro-symbolic loop

The Prolog-backed version adds a sixth demo showing unbounded recursion (`ancestor/2`) and list membership (`member/2`) — programs the toy engine cannot run at all. The Ollama version runs four natural-language scenarios through the real loop with the LLM doing the Interpret/Formalize/Reinterpret steps — including a recursive `ancestor/2` case that neither the regex layer nor the toy engine can handle.

The natural-language layer in both is a regex-based pattern-action interpreter (in the ELIZA tradition): a stand-in for a real LLM. To use an actual LLM, subclass `LLMDiscourse` and override `interpret` and `_extract_query` to call a model that returns structured `{facts, rules, query}` output. The `PrologEngine` half needs no changes — real Prolog accepts the idiomatic clauses an LLM will naturally produce.

It shows concretely how Prolog provides the formal reasoning structure that LLMs lack, while LLMs provide the natural language interface that Prolog lacks — together realizing the 2,500-year-old vision of intelligence as structured representation plus structured reasoning.

