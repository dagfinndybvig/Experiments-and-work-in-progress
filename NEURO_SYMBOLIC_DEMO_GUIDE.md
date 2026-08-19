# Neuro-Symbolic AI Demonstration: Guide and Explanation

*Part of the essay series: From Plato to Prolog to Prompts*

## Overview

This document explains the neuro-symbolic AI demonstration system that accompanies the essay *From Plato to Prolog to Prompts: The 2,500-Year Journey to Artificial Reason*.

The demonstration implements the **neuro-symbolic architecture** described in the essay — a bidirectional loop that combines the linguistic capabilities of large language models (LLMs) with the formal reasoning power of symbolic systems like Prolog. This architecture realizes the ancient Platonic-Aristotelian vision of intelligence as the manipulation of structured representations according to structured rules.

---

## Three Implementations

There are three implementations of the same system, kept directly comparable by sharing class names, public interface, and demo scenarios:

| | `neuro_symbolic_demo.py` | `neuro_symbolic_demo_prolog.py` | `neuro_symbolic_demo_ollama.py` |
|---|---|---|---|
| Reasoning engine (Geometry) | Pure-Python toy Prolog (~400 lines) | Real SWI-Prolog via `pyswip` | Real SWI-Prolog via `pyswip` |
| NL layer (Discourse) | Regex pattern-action (ELIZA-style) | Regex pattern-action (identical) | **Real LLM via Ollama** (regex fallback) |
| Dependencies | None (standard library only) | SWI-Prolog + `pip install pyswip` | SWI-Prolog + `pyswip` + `requests` + Ollama (optional) |
| Recursion, lists, negation, CLP | No | Yes | Yes |
| Demos 1-5 (syllogism, family, expert, planning, loop) | Yes | Yes (identical results) | — |
| Demo 6 (recursive `ancestor`, list `member`) | No | Yes | — |
| Ollama demos (NL -> LLM -> Prolog -> NL) | No | No | Yes (4 scenarios) |
| Runs offline, no API key | Yes | Yes | Yes (LLM is local; fallback needs nothing) |
| Best for | Reading the whole engine; running anywhere | Plugging in a real LLM that emits idiomatic Prolog | **Running the loop on an actual LLM** |

The zero-dependency version is a readable artifact: the entire backward-chaining engine is ~400 lines you can follow. The Prolog-backed version removes the ceiling of the toy engine (no lists, no real recursion, depth-limited chaining) so the formal-constraint half of the loop can do what the essay actually claims for it. The Ollama-backed version then replaces the regex Discourse with a real local LLM, so the Interpret/Formalize/Reinterpret steps are done by a model rather than a pattern matcher — while Derive/Verify stay in SWI-Prolog. It degrades gracefully: if Ollama is not running, every step falls back to the inherited regex layer and the output matches the Prolog version. Most of this guide describes the architecture and demos in terms that apply to **all three** versions; differences are noted where they matter (Installation, System Components, Technical Implementation Details, Demo 6, and the Ollama section).

---

## Table of Contents

1. [The Historical and Philosophical Context](#the-historical-and-philosophical-context)
2. [Architecture: Discourse and Geometry](#architecture-discourse-and-geometry)
3. [The Neuro-Symbolic Loop](#the-neuro-symbolic-loop)
4. [System Components](#system-components)
5. [Installation and Setup](#installation-and-setup)
6. [Running the Demonstrations](#running-the-demonstrations)
7. [Interactive Mode](#interactive-mode)
8. [Technical Implementation Details](#technical-implementation-details)
9. [Demonstration Walkthroughs](#demonstration-walkthroughs)
10. [Extending the System](#extending-the-system)
11. [Relationship to the Essay](#relationship-to-the-essay)

---

## The Historical and Philosophical Context

### From Plato and Aristotle to Modern AI

The essay traces a lineage of thought about intelligence and reasoning:

1. **Plato (c. 400 BCE)**: Theory of Forms — the idea that true knowledge concerns eternal, unchanging structures that underlie sensory appearances. This is the origin of **ontology** — the study of what exists at the most fundamental level.

2. **Aristotle (c. 350 BCE)**: Formalized the syllogism in *Prior Analytics* — the first **formal method** in Western thought. Together, Plato and Aristotle established that **intelligence consists in the manipulation of structured representations according to structured rules**.

3. **René Descartes (1637)**: In *La Géométrie*, transformed the Platonic-Aristotelian template by inventing coordinate geometry — a **domain-specific realization** where spatial extension becomes formally operable through algebraic notation.

4. **Prolog and GOFAI (1970s)**: Attempted to make the Platonic-Aristotelian template **computational** — a system that could represent the world in terms of facts (ontology) and rules (method), and derive new knowledge through logical inference.

5. **Modern Neuro-Symbolic AI**: Provides the missing interface. LLMs offer the **Discourse** (natural language understanding and generation) that Prolog lacked, while Prolog provides the **Geometry** (formal reasoning) that LLMs lack.

### The Central Thesis

Prolog was not wrong. It was not even just early. It was a **necessary stage** in the long development of artificial reason — the first computational instantiation of the Platonic-Aristotelian vision. The problem was never the formalism; the problem was the **interface** between the formal system and the world. That interface is now here, in the form of large language models.

---

## Architecture: Discourse and Geometry

The neuro-symbolic system is built on two complementary components:

### Descartes' Dual Legacy

In his two great works, Descartes provided both components:
- *Discourse on Method* — the **Discourse**: a natural language exposition of how to think
- *La Géométrie* — the **Geometry**: a formal system for mechanical reasoning about space

Our neuro-symbolic system mirrors this architecture:

```
┌─────────────────────────────────────────────────────────────┐
│                    NEURO-SYMBOLIC SYSTEM                         │
├─────────────────────────────────┬─────────────────────────────┤
│         DISCOURSE (LLM)           │        GEOMETRY (Prolog)      │
│  ┌─────────────────────────────┐ │  ┌─────────────────────────┐ │
│  │ - Natural language           │ │  │ - Formal representation    │ │
│  │   understanding               │ │  │ - Structured reasoning     │ │
│  │ - Knowledge acquisition      │ │  │ - Logical inference         │ │
│  │ - Interface to the world     │ │  │ - Constraint satisfaction   │ │
│  │ - Interpretation &            │ │  │ - Verification              │ │
│  │   reinterpretation            │ │  └─────────────────────────┘ │
│  └─────────────────────────────┘ │                                 │
└─────────────────────────────────┴─────────────────────────────┘
                                      │
                                      ▼
                             ┌─────────────────────┐
                             │   THE LOOP           │
                             │   (Bidirectional)    │
                             └─────────────────────┘
```

### Why Both Are Necessary

| Aspect | LLM (Discourse) | Prolog (Geometry) |
|--------|----------------|------------------|
| Strengths | Understands natural language, learns from data, handles ambiguity | Precise reasoning, enforces constraints, verifies correctness |
| Weaknesses | Cannot enforce formal rules, hits an "asymptote" of reliability | Cannot understand natural language, requires manual formalization |
| Role in System | **Interface** to the world, **translator** between natural and formal | **Engine** of reasoning, **enforcer** of constraints |

The neuro-symbolic approach combines the best of both: **LLMs provide the means to connect formal systems to the open world, while formal systems provide the structure that makes reasoning reliable and necessary.**

---

## The Neuro-Symbolic Loop

The core of the system is a bidirectional loop that connects linguistic interpretation with formal constraint:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  INTERPRET    │────▶│  FORMALIZE    │────▶│    DERIVE    │
│  (Discourse)  │     │  (Discourse)  │     │  (Geometry)   │
└──────────────┘     └──────────────┘     └──────────────┘
         ▲                        │                        │
         │                        ▼                        │
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   REVISE      │◀────│   VERIFY     │◀────│  REINTERPRET  │
│  (Loop)       │     │  (Geometry)   │     │  (Discourse)  │
└──────────────┘     └──────────────┘     └──────────────┘
```

### Step-by-Step Process

1. **INTERPRET** (LLM/Discourse)
   - The LLM reads a natural language query or statement
   - Extracts meaning, identifies entities, relationships, and intents
   - Example: "John is the father of Mary. Mary is the mother of Bob. Who is the grandfather of Bob?"

2. **FORMALIZE** (LLM/Discourse)
   - The LLM translates the interpreted content into formal representations
   - Generates Prolog facts and rules that capture the knowledge
   - Example: Generates `parent(john, mary).`, `parent(mary, bob).`, `male(john).`

3. **DERIVE** (Prolog/Geometry)
   - The Prolog engine performs logical inference on the formal representation
   - Applies rules, resolves queries, finds solutions
   - Example: Given the query `grandfather(X, bob)`, derives `X = john`

4. **VERIFY** (Prolog/Geometry)
   - The Prolog engine checks the validity of derivations
   - Ensures results satisfy all constraints and follow from the premises
   - Example: Verifies that `grandfather(john, bob)` is true

5. **REINTERPRET** (LLM/Discourse)
   - The LLM translates formal results back into natural language
   - Explains the reasoning and any limitations
   - Example: "John is the grandfather of Bob"

6. **REVISE** (Loop)
   - If results are unsatisfactory, the LLM refines the formalization
   - The loop continues with improved understanding
   - This is how the system learns and adapts

---

## System Components

### 1. PrologEngine (Geometry Component)

Both versions expose a `PrologEngine` class with the same public interface (`add_fact`, `add_rule`, `load_program`, `query`, `format_solutions`), so the rest of the system is identical. They differ in what the engine can actually do.

#### Zero-dependency version (`neuro_symbolic_demo.py`)

The `PrologEngine` class implements a Prolog-like logic programming engine in pure Python.

**Features:**
- **Facts**: Ground truths stored in the knowledge base (e.g., `parent(john, mary)`)
- **Rules**: Logical implications that define relationships (e.g., `grandparent(X, Z) :- parent(X, Y), parent(Y, Z)`)
- **Queries**: Questions posed to the knowledge base (e.g., `grandparent(X, bob)`)
- **Backward Chaining**: Goal-directed reasoning that works backward from queries to facts
- **Variable Unification**: Matching variables with values according to logical patterns
- **Conjunction Handling**: Support for queries with multiple conditions (e.g., `diagnosis(D, patient1), severe(D)`)
- **Built-in Predicates**: Comparison operators (`=`, `!=`, `<`, `>`, both prefix and infix) and arithmetic (`is`)

**Limitations:**
- No list data type
- No real recursion (depth-limited backward chaining)
- No negation, no constraint solving
- One fact per line in `load_program`

**Implementation Details:**
- Uses a set for facts (O(1) lookup)
- Uses a list for rules
- Implements depth-limited search to prevent infinite recursion
- Supports variables (uppercase names) and constants (lowercase names)

#### SWI-Prolog version (`neuro_symbolic_demo_prolog.py`)

The `PrologEngine` class is a thin wrapper around SWI-Prolog via `pyswip`. It delegates all reasoning to the real engine, so it inherits full Prolog semantics: unbounded recursion, lists, negation, arithmetic, and constraint solving. The public interface is identical to the zero-dependency version, so the demos and the `LLMDiscourse` layer run unchanged.

**Implementation Details:**
- `add_fact`/`add_rule` call `assertz`; `query` calls `Prolog.query`
- Tracks asserted predicates (name/arity) at the class level so `clear()` can retract them precisely. Class-level tracking is necessary because `pyswip.Prolog` is a singleton — all `PrologEngine` instances share one SWI-Prolog database.
- `format_solutions` is identical to the zero-dep version, so output formatting matches.

### 2. LLMDiscourse (Discourse Component)

The `LLMDiscourse` class simulates an LLM's role in the neuro-symbolic loop. In the zero-dep and Prolog versions it is a regex-based pattern-action interpreter; in the Ollama version it is subclassed by `OllamaDiscourse`, which replaces the regex `interpret`/`_extract_query`/`reinterpret` with calls to a local LLM (falling back to the regex layer when Ollama is down). See [Replacing the Regex Layer with a Real LLM](#replacing-the-regex-layer-with-a-real-llm) for the full mechanism.

**Features:**
- **Domain-Specific Knowledge**: Pre-configured patterns for classical logic, family relationships, and planning
- **Natural Language Interpretation**: Extracts meaning from text using regex patterns (or, in the Ollama version, asks the LLM)
- **Formalization**: Converts natural language to Prolog code
- **Reinterpretation**: Translates formal results back to natural language
- **Loop Management**: Orchestrates the complete neuro-symbolic cycle

**Domain Knowledge:**
- **Classical Logic**: Handles syllogisms ("All X are Y", "Some X are Y")
- **Family Relationships**: Recognizes parent/child relationships
- **Planning**: Understands task constraints and dependencies
- **General**: Fallback patterns for unknown domains

### 3. NeuroSymbolicSystem

The top-level class that combines both components and provides the demonstration interface.

---

## Installation and Setup

### Prerequisites

**For the zero-dependency version (`neuro_symbolic_demo.py`):**

- **Python 3.6 or higher** (Python 3.10+ recommended)
- **No additional packages required** — the system uses only Python's standard library

**For the SWI-Prolog version (`neuro_symbolic_demo_prolog.py`):**

- **Python 3.6 or higher**
- **SWI-Prolog** (>= 9.1 recommended; 10.x tested):
  - Windows: `winget install SWI-Prolog.SWI-Prolog`
  - macOS: `brew install swi-prolog`
  - Ubuntu: `sudo apt install swi-prolog`
- **pyswip**: `pip install pyswip`

`pyswip` locates the SWI-Prolog shared library automatically on Windows and via `swipl` on PATH on Unix. If you get `SwiPrologNotFoundError`, SWI-Prolog is not installed or not on PATH.

**For the Ollama version (`neuro_symbolic_demo_ollama.py`):**

- Everything the SWI-Prolog version needs, **plus**:
- **requests**: `pip install requests`
- **Ollama** (only for the LLM path; the regex fallback runs without it):
  - Windows: `winget install Ollama.Ollama`
  - macOS: `brew install ollama`
  - Linux: `curl -fsSL https://ollama.com/install.sh | sh`
- Then start it and pull a model:
  - `ollama serve` (if not already running as a service)
  - `ollama pull qwen2.5:7b` (or any instruct model; set with `--model` or `OLLAMA_MODEL`)

The Ollama version imports `PrologEngine` and `LLMDiscourse` from `neuro_symbolic_demo_prolog`, so it inherits that file's prerequisites. Without Ollama running it still works — every Discourse step falls back to the regex layer, so you get the same output as the Prolog version. Run `python neuro_symbolic_demo_ollama.py --status` to see whether Ollama is reachable and which model is configured.

### Installation Steps

#### Option 1: Clone the Repository (Recommended)

```bash
# Clone the repository
git clone https://github.com/dagfinndybvig/Experiments-and-work-in-progress.git
cd Experiments-and-work-in-progress

# Verify you can run Python
python --version

# (Prolog and Ollama versions) install the Python bindings
pip install pyswip requests
```

#### Option 2: Download Just the Demo File

```bash
# Download the demo script directly
curl -O https://raw.githubusercontent.com/dagfinndybvig/Experiments-and-work-in-progress/main/neuro_symbolic_demo.py

# Make it executable (Linux/Mac)
chmod +x neuro_symbolic_demo.py
```

#### Option 3: Set Up a Virtual Environment (Optional but Recommended)

```bash
# Create a virtual environment
python -m venv ns_demo_env

# Activate it
# On Linux/Mac:
source ns_demo_env/bin/activate
# On Windows:
ns_demo_env\Scripts\activate

# The zero-dep version has no external dependencies.
# For the Prolog version:
pip install pyswip
# For the Ollama version (adds requests; Ollama itself installed separately):
pip install pyswip requests
```

### Verifying Installation

```bash
# Check Python version
python --version

# Zero-dependency version
python -c "from neuro_symbolic_demo import NeuroSymbolicSystem; print('Installation successful!')"

# SWI-Prolog version (requires SWI-Prolog + pyswip)
python -c "from neuro_symbolic_demo_prolog import NeuroSymbolicSystem; print('Installation successful!')"

# Ollama version (requires SWI-Prolog + pyswip + requests; Ollama optional)
python -c "from neuro_symbolic_demo_ollama import NeuroSymbolicSystem; print('Installation successful!')"
python neuro_symbolic_demo_ollama.py --status   # shows Ollama up/down + configured model
```

If you see "Installation successful!", the system is ready to use.

---

## Running the Demonstrations

### Basic Usage

To run all demonstrations with the zero-dependency version:

```bash
python neuro_symbolic_demo.py
```

Or with the SWI-Prolog version (requires SWI-Prolog + pyswip):

```bash
python neuro_symbolic_demo_prolog.py
```

Or with the Ollama version (requires SWI-Prolog + pyswip + requests; Ollama optional — runs in regex-fallback mode without it):

```bash
python neuro_symbolic_demo_ollama.py            # run the 4 NL->LLM->Prolog->NL demos
python neuro_symbolic_demo_ollama.py --status   # show Ollama up/down + configured model
python neuro_symbolic_demo_ollama.py --model llama3.1:8b --demo
python neuro_symbolic_demo_ollama.py --interactive
```

This will execute the demonstrations sequentially:
1. Classical Logic (Aristotle's Syllogism)
2. Family Relationships (Platonic Ontology)
3. Expert System (Medical Diagnosis)
4. Planning (Constraint-Based Reasoning)
5. Complete Neuro-Symbolic Loop
6. Real Prolog Power (recursion and lists) — **Prolog version only**

Demos 1-5 produce identical results in the zero-dep and Prolog versions. Demo 6 runs only in the Prolog-backed version because it exercises unbounded recursion and list membership, which the toy engine cannot do. The Ollama version runs its own set of four natural-language scenarios through the real loop (syllogism, family, novel syllogism, and a recursive `ancestor/2` case) — when Ollama is up the LLM does the Interpret/Formalize/Reinterpret steps; when it is down, the regex layer takes over and the syllogism demos still succeed while the family/recursion ones report "no solutions" (the regex layer cannot synthesize the missing rules — which is exactly the limitation the LLM removes).

### Command-Line Options

The zero-dep and Prolog versions accept the same flags:

```bash
# Run demonstrations
python neuro_symbolic_demo.py --demo
python neuro_symbolic_demo.py -d

# Run in interactive mode
python neuro_symbolic_demo.py --interactive
python neuro_symbolic_demo.py -i

# Show help
python neuro_symbolic_demo.py --help
python neuro_symbolic_demo.py -h
```

Substitute `neuro_symbolic_demo_prolog.py` for the SWI-Prolog version. The Ollama version adds `--model NAME`, `--host URL`, and `--status`, and honors the `OLLAMA_MODEL` / `OLLAMA_HOST` environment variables:

```bash
python neuro_symbolic_demo_ollama.py --model qwen2.5:7b --host http://localhost:11434 --demo
python neuro_symbolic_demo_ollama.py --status
python neuro_symbolic_demo_ollama.py --help
```

### Sample Output

Running `python neuro_symbolic_demo.py` will produce output similar to:

```
================================================================================
NEURO-SYMBOLIC AI DEMONSTRATION
From Plato to Prolog to Prompts: The 2,500-Year Journey to Artificial Reason
================================================================================

DEMO 1: CLASSICAL LOGIC (Aristotle's Syllogism)
--------------------------------------------------------------------------------

Scenario: Aristotle's classic syllogism
  Natural language: "All men are mortal. Socrates is a man. Is Socrates mortal?"

Formal representation (Geometry):
  man(socrates).
  man(plato).
  man(aristotle).
  mortal(X) :- man(X).

Query: mortal(socrates).
Result: true.

Reinterpretation (Discourse):
  Yes, Socrates is mortal.

... (more demonstrations follow)
```

---

## Interactive Mode

The interactive mode allows you to experiment with the neuro-symbolic system directly.

### Starting Interactive Mode

```bash
python neuro_symbolic_demo.py --interactive
```

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `help`, `h`, `?` | Show help | `help` |
| `quit`, `exit`, `q` | Exit the system | `quit` |
| `demo`, `demos` | Run all demonstrations | `demo` |
| `clear`, `reset` | Clear the knowledge base | `clear` |
| `load <file>` | Load a Prolog program from file | `load knowledge.pl` |
| `assert <fact>` | Add a fact | `assert parent(john, mary).` |
| `rule <rule>` | Add a rule | `rule grandfather(X,Z) :- parent(X,Y), parent(Y,Z).` |
| `query <goal>` | Query the knowledge base | `query grandfather(X, bob).` |
| `natural <text>` | Process natural language | `natural John is the father of Mary.` |

### Interactive Session Example

```
Interactive Neuro-Symbolic System
Type 'help' for commands, 'quit' to exit, 'demo' to run demonstrations

ns> clear
Knowledge base cleared.

ns> assert parent(john, mary).
Added fact: parent(john, mary)

ns> assert parent(mary, bob).
Added fact: parent(mary, bob)

ns> rule grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
Added rule: grandparent(X, Z) :- parent(X, Y), parent(Y, Z)

ns> query grandparent(X, bob).
{X = john}.

ns> natural John is the father of Mary. Mary is the mother of Bob. Who is the grandfather of Bob?

Trace:
  Domain: family
  Interpretations: ['parent(john, mary).', 'parent(mary, bob).']
  Formal query: grandfather(X, bob).
  Solutions: [{'X': 'john'}]
  Verification: True
  Reinterpretation: Solution: X is john

ns> quit
Goodbye!
```

Note: ground queries (e.g., `query mortal(socrates)`) print `true.` rather than leaking internal rule variables, because the formatter filters bindings to the query's own variables.

---

## Technical Implementation Details

### PrologEngine Internals

The two versions share the same public interface but differ entirely in internals.

#### Zero-dependency version (`neuro_symbolic_demo.py`)

##### Data Structures

```python
# Facts are stored as strings in a set
self.facts = {"parent(john, mary)", "parent(mary, bob)", ...}

# Rules are stored as tuples of (head, [body_atoms])
self.rules = [
    ("mortal(X)", ["man(X)"]),
    ("grandparent(X, Z)", ["parent(X, Y)", "parent(Y, Z)"]),
    ...
]

# Built-in predicates (both prefix and infix forms are recognized)
self.builtins = {
    '=': self._builtin_equals,
    '!=': self._builtin_not_equals,
    '<': lambda a, b: float(a) < float(b),
    '>': lambda a, b: float(a) > float(b),
    'is': self._builtin_is,
}
```

##### Key Algorithms

1. **Unification (`_match` and `_match_with_bindings`)**
   - Matches a pattern against a fact or rule head
   - Returns variable bindings that make the match work
   - Example: Matching `mortal(X)` against `mortal(socrates)` returns `{'X': 'socrates'}`

2. **Backward Chaining (`_solve_goal`)**
   - Goal-directed reasoning
   - Starts with the query and works backward to find supporting facts
   - Uses depth-first search with a depth limit to prevent infinite recursion
   - Handles both facts and rules
   - Recognizes builtins in both prefix (`>(A, B)`) and infix (`A > B`) form

3. **Conjunction Solving (`_solve_conjunction`)**
   - Solves queries with multiple conditions (e.g., `A, B, C`)
   - Solves each condition in sequence
   - Combines the solutions

4. **Body Parsing (`_parse_body`)**
   - Parses rule bodies and conjunctions
   - Handles commas inside parentheses correctly
   - Example: `"parent(X, Y), parent(Y, Z)"` → `['parent(X, Y)', 'parent(Y, Z)']`

#### SWI-Prolog version (`neuro_symbolic_demo_prolog.py`)

The `PrologEngine` class is a thin wrapper around `pyswip.Prolog`. There is no custom unification or backward-chaining code — all reasoning is delegated to SWI-Prolog:

- `add_fact(f)` / `add_rule(r)` → `self._prolog.assertz(...)`, with the predicate indicator tracked for later retraction
- `query(g)` → `list(self._prolog.query("catch(call_with_inference_limit((g), 10000, _), error(existence_error(procedure, _), _), fail)"))`, normalized to string-valued dicts. The `call_with_inference_limit/3` wrapper caps total inferences at 10000 so mutually recursive LLM-emitted rules (e.g. `cat(X):-animal(X)` + `animal(X):-cat(X)`) cannot hang the loop; the `catch/3` wrapper turns a call to an undefined predicate into a graceful failure (`[]`) instead of raising `existence_error`. Legitimate recursive queries stay well under the limit. Other errors still propagate.
- `is_assertable(clause)` / `is_static_predicate(name, arity)` → `predicate_property(Head, static)`, used by the Ollama layer to drop LLM-emitted clauses whose head is a static builtin/library predicate (`is/2`, `member/2`, ...) that `assertz` cannot redefine.
- `clear()` → `retractall` for every tracked predicate indicator
- `format_solutions` is identical to the zero-dep version

Because `pyswip.Prolog` is a singleton (all instances share one SWI-Prolog database), predicate tracking is kept at the class level so `clear()` retracts everything any instance ever asserted, not just the current one.

### LLMDiscourse Internals

#### Domain Knowledge Structure

```python
self.domain_knowledge = {
    'classical_logic': {
        'interpreters': {
            r'(?i)\b(all|every)\s+(\w+)\s+are\s+(\w+)':
                lambda m: f"{self._singularize(m.group(3))}(X) :- {self._singularize(m.group(2))}(X).",
            # More patterns...
        },
        'reinterpreters': {...}
    },
    'family': {
        'interpreters': {
            r'(?i)(\w+)\s+is\s+the\s+(mother|father|parent)\s+of\s+(\w+)':
                lambda m: f"parent({m.group(1).lower()}, {m.group(3).lower()}).",
            # More patterns...
        }
    },
    # More domains...
}
```

The `interpret` method iterates matches with `re.finditer` (not `re.findall`) so each handler receives a match object and can call `.group()`. Constants are lowercased so proper nouns like "Socrates" become Prolog constants (`socrates`), not variables. A `_singularize` helper reduces plural nouns ("men" → "man") for the `all X are Y` rule.

#### Natural Language Processing

The system uses **regex-based pattern matching** to interpret natural language:

1. **Domain Inference**: Determines the most likely domain based on keywords
2. **Pattern Matching**: Applies domain-specific patterns to extract meaning
3. **Fallback**: Uses general patterns if no domain-specific ones match
4. **Query Extraction**: Converts natural language questions into Prolog queries

---

## Demonstration Walkthroughs

### Demo 1: Classical Logic (Aristotle's Syllogism)

**Scenario**: "All men are mortal. Socrates is a man. Is Socrates mortal?"

**Process**:

1. **Formalization**: The LLM converts the statements to:
   ```prolog
   man(socrates).
   man(plato).
   man(aristotle).
   mortal(X) :- man(X).
   ```

2. **Query**: `mortal(socrates).`

3. **Derivation**:
   - The Prolog engine matches `mortal(socrates)` against the rule head `mortal(X)`
   - Binds `X = socrates`
   - Needs to prove `man(socrates)`
   - Finds the fact `man(socrates)` ✓

4. **Result**: `true.` → "Yes, Socrates is mortal."

**Key Insight**: This demonstrates how a simple rule (`mortal(X) :- man(X)`) captures Aristotle's syllogistic reasoning in computational form.

### Demo 2: Family Relationships (Platonic Ontology)

**Scenario**: "John is the father of Mary. Mary is the mother of Bob. Who is the grandparent of Bob?"

**Process**:

1. **Formalization**:
   ```prolog
   parent(john, mary).
   parent(mary, bob).
   male(john).
   female(mary).
   father(X, Y) :- parent(X, Y), male(X).
   mother(X, Y) :- parent(X, Y), female(X).
   grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
   ```

2. **Query**: `grandparent(X, bob).`

3. **Derivation**:
   - Match `grandparent(X, bob)` against rule head `grandparent(X, Z)` → `Z = bob`
   - Need to prove: `parent(X, Y), parent(Y, bob)`
   - For `parent(Y, bob)`: matches `parent(mary, bob)` → `Y = mary`
   - For `parent(X, mary)`: matches `parent(john, mary)` → `X = john`

4. **Result**: `{X = john}.` → "John is the grandfather of Bob."

**Key Insight**: This shows **multi-hop reasoning** — the system can chain multiple relationships together, just as Plato's Forms organize the world into structured kinds.

### Demo 3: Expert System (MYCIN-like Medical Diagnosis)

**Scenario**: "The patient has fever and cough. What could be the diagnosis?"

**Process**:

1. **Formalization**:
   ```prolog
   symptom(patient1, fever).
   symptom(patient1, cough).
   symptom(patient1, headache).
   
   diagnosis(flu, X) :- symptom(X, fever), symptom(X, cough).
   diagnosis(cold, X) :- symptom(X, cough), symptom(X, headache).
   
   severe(flu).
   mild(cold).
   ```

2. **Query**: `diagnosis(Disease, patient1).`

3. **Derivation**:
   - For `diagnosis(flu, patient1)`: needs `symptom(patient1, fever), symptom(patient1, cough)` ✓
   - For `diagnosis(cold, patient1)`: needs `symptom(patient1, cough), symptom(patient1, headache)` ✓

4. **Result**: `{Disease = flu}.` and `{Disease = cold}.`

5. **Conjunction Query**: `diagnosis(D, patient1), severe(D).`
   - Finds only flu (since cold is mild)

**Key Insight**: This mirrors the **MYCIN expert system** from the 1970s, which used Prolog-like rules for medical diagnosis — a classic GOFAI application.

### Demo 4: Planning (Constraint-Based Reasoning)

**Scenario**: "We need to build a house. The foundation must be built before the walls. The roof must be built after the walls. What is a valid order?"

**Process**:

1. **Formalization**:
   ```prolog
   task(foundation).
   task(walls).
   task(roof).
   task(plumbing).
   task(electrical).
   
   before(foundation, walls).
   before(walls, roof).
   before(foundation, plumbing).
   before(foundation, electrical).
   
   valid_sequence([H|T]) :-
       task(H),
       valid_sequence(T),
       all_before(H, T).
   valid_sequence([H]) :- task(H).
   ```

2. **Query**: `valid_sequence(Order).`

3. **Derivation**: The engine generates valid permutations where all `before` constraints are satisfied.

**Key Insight**: This shows **constraint satisfaction** — a key capability of Prolog that was used in planning and scheduling systems.

### Demo 5: The Complete Neuro-Symbolic Loop

**Scenario**: "John is the father of Mary. Mary is the mother of Bob. Who is the grandfather of Bob?"

This demonstration shows all steps of the loop:

1. **INTERPRET & FORMALIZE**: LLM generates Prolog facts and rules
2. **DERIVE**: Prolog engine finds the answer
3. **VERIFY**: Prolog engine confirms the result
4. **REINTERPRET**: LLM translates back to natural language
5. **REVISE**: (If needed) LLM refines and loop continues

**Key Insight**: This is the **complete neuro-symbolic architecture** — the fusion of LLM and Prolog that the essay argues is the future of AI.

### Demo 6: Real Prolog Power (recursion and lists) — Prolog version only

**Scenario**: Programs the toy engine cannot run — unbounded recursion and list membership.

**Process**:

1. **Formalization**:
   ```prolog
   parent(john, mary).
   parent(mary, bob).
   parent(bob, alice).
   parent(alice, charlie).

   ancestor(X, Y) :- parent(X, Y).
   ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).

   member(X, [X|_]).
   member(X, [_|T]) :- member(X, T).
   ```

2. **Queries**:
   - `ancestor(X, charlie).` — all ancestors of Charlie, 4 generations deep
   - `ancestor(john, X).` — all descendants of John
   - `member(3, [1, 2, 3, 4]).` — list membership test
   - `member(X, [socrates, plato, aristotle]).` — enumerate a list

3. **Derivation**: SWI-Prolog resolves the recursive `ancestor/2` rule to arbitrary depth and enumerates list elements via `member/2`.

**Key Insight**: The toy engine has a hard depth limit and no list data type, so it cannot run either program. This demo shows why a real Prolog backend matters: the formal-constraint half of the neuro-symbolic loop is no longer the bottleneck. An LLM that emits idiomatic Prolog (recursive rules, lists, DCGs) can be paired with an engine that actually runs it.

---

## Extending the System

### Adding New Domains

To add support for a new domain (e.g., legal reasoning):

1. **Add to `domain_knowledge`** in `LLMDiscourse.__init__`:

```python
self.domain_knowledge['legal'] = {
    'interpreters': {
        r'(?i)(\w+)\s+is\s+(guilty|not\s+guilty)\s+of\s+(\w+)':
            lambda m: f"verdict({m.group(1)}, {m.group(2)}, {m.group(3)}).",
        # More patterns...
    },
    'reinterpreters': {
        # Translation mappings
    }
}
```

2. **Update domain inference** in `_infer_domain`:

```python
elif any(word in text_lower for word in ['guilty', 'innocent', 'law', 'legal']):
    return 'legal'
```

3. **Add query extraction patterns** in `_extract_query`:

```python
elif domain == 'legal':
    # Add legal-specific query patterns
    pass
```

### Adding Built-in Predicates

To add a new built-in predicate to the **zero-dependency** `PrologEngine`:

```python
self.builtins = {
    # ... existing builtins ...
    'member': self._builtin_member,  # Check if element is in list
    'length': self._builtin_length,  # Get list length
}

def _builtin_member(self, element, list_str):
    # Implement list membership check
    pass
```

The **SWI-Prolog version** does not need this — predicates like `member/2`, `length/2`, `append/3`, and `between/3` are built into real Prolog. This is the core advantage of the Prolog backend: capabilities that require hand-implementation in the toy engine come for free.

### Loading External Knowledge Bases

You can load Prolog programs from files:

```python
# In interactive mode
ns> load family_knowledge.pl

# Programmatically
with open('family_knowledge.pl', 'r') as f:
    program = f.read()
    engine.load_program(program)
```

Example `family_knowledge.pl`:
```prolog
% Family relationships
parent(john, mary).
parent(john, tom).
parent(mary, bob).
parent(mary, alice).
parent(susan, john).

male(john).
male(tom).
male(bob).
female(mary).
female(alice).
female(susan).

father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X != Y.
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
```

Note: the recursive `ancestor/2` rule runs only in the SWI-Prolog version. The toy engine's depth limit prevents it from resolving the full chain.

### Replacing the Regex Layer with a Real LLM

The `LLMDiscourse` class in the zero-dep and Prolog versions is a stand-in for a real LLM — a regex-based pattern-action interpreter in the ELIZA tradition. `neuro_symbolic_demo_ollama.py` is the real-LLM version: it subclasses the Prolog `LLMDiscourse` and overrides the three natural-language touch points of the loop to call a local model served by **Ollama**.

#### What it overrides

`OllamaDiscourse(LLMDiscourse)` overrides exactly the methods that do NL work, and leaves the rest (including `loop`) inherited:

- `interpret(text, domain)` — asks the LLM to emit JSON `{"facts": [...], "rules": [...]}` (each item a single Prolog clause), validates each clause, and returns the survivors. This is the Interpret + Formalize steps.
- `_extract_query(text, domain)` — asks the LLM to emit one Prolog query goal (e.g. `mortal(socrates).` or `ancestor(X, charlie).`).
- `reinterpret(solutions, original_query)` — asks the LLM to render the Prolog solutions as a concise natural-language answer.

`Derive` and `Verify` stay in SWI-Prolog, unchanged. The inherited `loop` calls these overrides in sequence, loads the returned clauses into the engine, runs the query, and reinterprets — so the LLM is wired in by overriding three methods and nothing else.

#### The contract: structured output, not free text

Each LLM call asks for a constrained output — JSON for `interpret`, a single goal for `_extract_query`, a short answer for `reinterpret` — and Ollama's `format: "json"` mode forces valid JSON for the formalization step. The response is then cleaned and validated before it touches the engine:

- `_clean_clause` strips markdown fences, takes the first non-empty line, ensures a trailing period, requires balanced parentheses, requires a lowercase `name(...)` head, and rejects prose markers (`?`, ```` ``` ````, `json`, `output`, `answer`).
- `PrologEngine.is_assertable` then asks Prolog itself — via `predicate_property(Head, static)` — whether the clause's head predicate is a static builtin/library predicate (`is/2`, `=/2`, `member/2`, ...) that `assertz` cannot redefine. Such clauses are dropped; the rest are kept. This is why the validation is not a brittle blocklist: Prolog is the source of truth for what it can accept.

Clauses that fail either check are silently dropped. If *no* clause survives, `interpret` falls back to the regex layer for that call.

#### Graceful fallback

Every override first checks `OllamaClient.is_available()` (a cached probe of `/api/tags`). If Ollama is not running — not installed, not started, or the model not pulled — the call delegates to the inherited regex implementation and tags itself `regex` in `discourse.paths`; otherwise it uses the model and tags itself `ollama`. So the file runs today with no LLM installed and produces the same output as the Prolog version; the moment Ollama is up, the same code paths use the model with no edits. Each demo prints `discourse.path_summary()` so you can see which path each step took.

#### Two engine changes that make the LLM path robust

Wiring a real LLM to real Prolog exposed three latent issues in the shared regex layer and engine, now fixed in `neuro_symbolic_demo_prolog.py` (and the identical regex code in `neuro_symbolic_demo.py`):

1. **`is/2` collisions.** The regex `_extract_query` built `is(X, bob)` from "Who is the *grandparent* of Bob?" (it used the captured `is` instead of the relation), and `_general_interpretation`'s verb pattern emitted `is(john, a).` from "John is a parent". Both collide with SWI-Prolog's static `is/2`. Fixed: the family query now uses the relation (`grandparent(X, bob).`), and the verb pattern skips copulas/stopwords (`is`, `are`, `a`, `the`, ...). The toy engine tolerated these because it has no `is/2` builtin; real Prolog does not.

2. **Undefined-predicate queries.** When the Discourse layer asks about a predicate it never formalized (e.g. `grandparent(X, bob)` with only `parent/2` loaded), SWI-Prolog raises `existence_error` where the toy engine returns no solutions. `PrologEngine.query` now wraps each goal in `catch/3` so an undefined predicate fails gracefully (returns `[]`) instead of crashing the loop. Other errors (type errors, syntax errors) still propagate. This is what makes the regex fallback for the family/recursion demos report "no solutions" instead of aborting.

3. **Infinite loops from LLM-generated rules.** An LLM can emit mutually recursive rules with no terminating base case (e.g. `cat(X) :- animal(X).` + `animal(X) :- cat(X).`). Without protection, Prolog backtracks between them forever and the loop hangs. `PrologEngine.query` now wraps each goal in `call_with_inference_limit/3` (limit 10000) so runaway recursion is cut off and the goal simply fails. Legitimate queries — including recursive `ancestor/2` over several generations — stay well under the limit.

#### Verdict consistency: the formal system is authoritative

The `reinterpret` step computes the verdict (true/false) from Prolog's solutions and hands it to the LLM to phrase. But a small model can still contradict the verdict — saying "No" when Prolog proved true. `OllamaDiscourse._verdict_consistent` checks the first word of the LLM's answer against the verdict: if the polarity mismatches (e.g. "No" for a true verdict), the answer is rejected and the deterministic regex reinterpretation is used instead. This is the neuro-symbolic thesis made concrete: the formal constraint catches the LLM's error, and the loop never lets the language model override the formal result.

#### The showcase: recursion the regex layer cannot do

The Ollama demo's fourth scenario feeds the model a natural-language description of `ancestor/2` ("an ancestor is a parent, or a parent of an ancestor"). A capable model emits the two recursive rules and the `parent/2` facts; SWI-Prolog runs them and returns all ancestors of Charlie. Neither the regex layer (which cannot synthesize the rule) nor the toy engine (which cannot run the recursion) can do this — it is the concrete payoff of pairing a real LLM with real Prolog.

#### Using a hosted API instead of Ollama

Ollama is a local, offline, no-API-key choice that matches the other two demos' stance. To use a hosted provider (Mistral, OpenAI, Anthropic, ...), replace the body of `OllamaClient.chat` with a call to that provider's chat endpoint. Everything upstream — the prompts, the JSON contract, the validation, the fallback — stays the same; the rest of the system never knows which backend produced the text.

---

## Relationship to the Essay

The demonstration system concretely illustrates the historical and philosophical arguments made in *From Plato to Prolog to Prompts*:

### 1. Plato and Aristotle: The Origin (Section 2 of Essay)

- **Essay**: "Plato's Forms and Aristotle's Logic as the origin of ontology and formal method"
- **Demonstration**: The Prolog engine implements **ontology** (facts as structured representations) and **method** (rules as structured reasoning). Every Prolog program is a computational realization of the Platonic-Aristotelian template.

### 2. Descartes: From Forms to Functions (Section 3 of Essay)

- **Essay**: "Descartes' coordinate system was dynamic and generative... By assigning numerical coordinates to geometric points and expressing curves as algebraic equations, he created a medium in which spatial problems could be transformed into syntactic operations"
- **Demonstration**: Prolog does the same for **any domain** — it creates a medium where domain problems (family relationships, medical diagnosis, planning) can be transformed into syntactic operations (facts, rules, queries).

### 3. Prolog: The Computational Instantiation (Section 4 of Essay)

- **Essay**: "Prolog was the attempt to make the template itself computational... It could implement ontologies, reason with constraints, power expert systems"
- **Demonstration**: The `PrologEngine` class **is** this computational instantiation. It shows exactly how Prolog (or a Prolog-like system) can represent and reason about structured knowledge.

- **Essay**: "The Knowledge Acquisition Bottleneck: Prolog required that the world be manually formalized in its terms"
- **Demonstration**: The `LLMDiscourse` class solves this — it **automates** the formalization process, translating natural language into Prolog representations.

- **Essay**: "The problem was not Prolog's reasoning engine, which was sound. The problem was the interface between the formal system and the world it was meant to represent"
- **Demonstration**: The neuro-symbolic loop **is** the interface — LLMs connect Prolog to the world.

### 4. Modern AI: The Discourse Joins the Geometry (Section 5 of Essay)

- **Essay**: "LLMs provide the Discourse that Prolog lacked... But LLMs... can describe formal domains without submitting to their norms"
- **Demonstration**: The system shows **both** — LLMs handle the linguistic side (Discourse), Prolog handles the formal side (Geometry), and together they achieve what neither can alone.

- **Essay**: "The solution... is the loop: Interpret (LLM) → Formalize (LLM) → Derive (Formal System) → Verify (Formal System) → Reinterpret (LLM) → Revise (Loop)"
- **Demonstration**: This is **literally** what the code implements. The `NeuroSymbolicSystem.loop()` method executes exactly this loop.

### 5. The 2,500-Year Circle (Section 6 of Essay)

- **Essay**: "Prolog was not wrong. It was not even just early. It was a necessary stage... The circle is full. From Plato's Forms to Prolog's facts and rules to the prompts of modern LLMs"
- **Demonstration**: Running the system shows this circle in action — ancient philosophical insights made computational through the synthesis of modern AI technologies.

---

## Conclusion

This demonstration system provides a **concrete, working example** of the neuro-symbolic architecture described in the essay. It shows that:

1. **Prolog was not wrong** — it correctly implemented the Platonic-Aristotelian vision of structured representation and reasoning
2. **The interface problem is solvable** — LLMs can provide the connection between formal systems and the open world
3. **The synthesis is powerful** — combining both creates systems that are more capable than either alone
4. **The historical arc continues** — from Plato to Prolog to Prompts, we are building the machinery of thought

### The Big Picture

The neuro-symbolic approach represents a **return to fundamentals** — a recognition that the ancient insight about intelligence (structured representation + structured reasoning) was correct all along. Modern AI succeeds to the extent that it finally provides the means to **connect** formal systems to the world, completing the vision that began 2,500 years ago in ancient Greece.

---

## References

- [From Plato to Prolog to Prompts: The 2,500-Year Journey to Artificial Reason](From_Plato_to_Prolog_to_Prompts.md)
- [Language(s) of Thought: A Wittgensteinian View of Fodor and the Gradually Increasing Capabilities of LLMs](Language_s_of_Thought.md)
- [Symbolic Forms and the Plural Mind](Symbolic_Forms_and_the_Plural_Mind.md)
- [The Cartesian Moment: Analytical Geometry as Language of Thought](The_Cartesian_Moment_Alternate_Version.md)
- [Constitution and Rule-Change: Wittgenstein's Remarks, Cassirer's Forms, and the Asymptote of Language-Only Reasoning](Constitution_and_Rule-Change.md)

---

## License

This demonstration system is provided as part of the *Experiments-and-work-in-progress* repository. It is open source and available for educational and research purposes.

---

*Documentation generated for the neuro-symbolic AI demonstration system*
*Part of the essay series: From Plato to Prolog to Prompts*
