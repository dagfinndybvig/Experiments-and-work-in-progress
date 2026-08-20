# Quick Start

This repo contains both runnable code and philosophical essays. Pick your path.

---

## Path A: 5-Minute Code Demo

No dependencies needed for the first demo.

```bash
# 1. Clone and enter the repo
git clone https://github.com/dagfinndybvig/Experiments-and-work-in-progress.git
cd Experiments-and-work-in-progress

# 2. Run the zero-dependency demo
python neuro_symbolic_demo.py

# 3. Run the tests
python test_demo.py
```

**What you just saw:** A pure-Python Prolog engine running syllogisms, family trees, expert systems, and planning — all driven by a regex-based natural-language layer. The code is ~400 lines and readable end-to-end.

**Next steps:**
- Install SWI-Prolog + `pyswip` (see [SETUP.md](SETUP.md)) and run `python neuro_symbolic_demo_prolog.py` for real recursion and lists.
- Install Ollama (see [SETUP.md](SETUP.md)) and run `python neuro_symbolic_demo_ollama.py` to see a real LLM drive the loop.

---

## Path B: Reading the Essays

The essays build on each other. Suggested order:

1. **Language(s) of Thought** ([MD](Language_s_of_Thought.md))  
   Start here. Wittgenstein, Fodor, and why LLMs need formal languages.

2. **Symbolic Forms and the Plural Mind** ([MD](Symbolic_Forms_and_the_Plural_Mind.md))  
   Cassirer: language alone is not enough. Alternate version also available.

3. **The Cartesian Moment** ([MD](The%20Cartesian%20Moment.md))  
   Descartes' *Geometry* as the foundational symbolic form. Alternate version also available.

4. **From Halting Problem to Imitation Game** ([MD](From%20Halting%20Problem%20to%20Imitation%20Game.md))  
   Turing's learning-machines programme.

5. **Constitution and Rule-Change** ([MD](Constitution_and_Rule-Change.md))  
   Wittgenstein's *RFM* meets Cassirer; the constitutive claim relocated to practices.

6. **The Fork and the Form** ([MD](The_Fork_and_the_Form.md))  
   Hume's fork and what formal forms contribute to the analytic side.

7. **From Plato to Prolog to Prompts** ([MD](From_Plato_to_Prolog_to_Prompts.md))  
   The historical arc: why Prolog/GOFAI were not failed paradigms, and how neuro-symbolic AI completes the vision.

**After reading:** Run the three demo scripts to see the architecture the essays describe.

---

## File Map

| File | What it is |
|---|---|
| `neuro_symbolic_demo.py` | Zero-dependency demo; readable ~400-line Prolog engine |
| `neuro_symbolic_demo_prolog.py` | SWI-Prolog backend; adds recursion, lists, Demo 6 |
| `neuro_symbolic_demo_ollama.py` | Real LLM (Ollama) + SWI-Prolog; 4 NL-driven demos |
| `test_demo.py` | Automated tests for all three scripts |
| `NEURO_SYMBOLIC_DEMO_GUIDE.md` | Full technical guide to the demo mechanism |
| `LIBRARY_SORTING_PLAN.md` | Workplace application: library material sorting |
| `SETUP.md` | Dependency installation (SWI-Prolog, Ollama) |
| `requirements.txt` | Python dependencies |
