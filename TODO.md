# TODO / Known Risks

This file tracks weaknesses and improvement opportunities identified during review.

## 1. No Automated Tests
- **Risk**: Regressions are only caught by manually running the three demo scripts.
- **Action**: Add a `test_demo.py` that asserts expected output for each demo scenario across `neuro_symbolic_demo.py`, `neuro_symbolic_demo_prolog.py`, and `neuro_symbolic_demo_ollama.py`.

## 2. Regex NL Layer Is a Stand-In
- **Risk**: The base (`neuro_symbolic_demo.py`) and Prolog (`neuro_symbolic_demo_prolog.py`) demos use a regex-based Discourse module. This does not exercise real LLM behavior and limits natural-language coverage to the hard-coded patterns.
- **Action**: Keep the regex layer as a fallback, but document its coverage limits. Consider adding a lightweight API-based LLM option (e.g., OpenAI-compatible) for users without Ollama.

## 3. Mixed Audience Friction
- **Risk**: Philosophers may skip the code; engineers may skip the essays. The README mitigates this, but the repo lacks a quick-start path for either camp.
- **Action**: Add a `QUICKSTART.md` with (a) a 5-minute code-only path and (b) a reading-order guide for the essays.

## 4. No Continuous Integration
- **Risk**: No automated verification that the code still runs after edits.
- **Action**: Add a GitHub Actions workflow (or equivalent) that runs `python -m py_compile` on all `.py` files and executes the zero-dependency demo on every push.

## 5. Dependency Documentation
- **Risk**: The Ollama and Prolog versions require external system dependencies (SWI-Prolog, Ollama) that are not captured in a `requirements.txt` or `pyproject.toml`.
- **Action**: Add a `requirements.txt` for Python deps and a `SETUP.md` with platform-specific install instructions for SWI-Prolog and Ollama.
