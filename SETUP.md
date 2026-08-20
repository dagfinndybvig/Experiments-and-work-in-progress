# Setup Guide

This document covers platform-specific installation of the external dependencies required by the neuro-symbolic demo suite.

## Quick Start

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Install SWI-Prolog (required for Prolog and Ollama demos)
#    See platform-specific instructions below.

# 3. (Optional) Install Ollama for real-LLM demos
#    See platform-specific instructions below.

# 4. Run the zero-dependency demo (no external deps needed)
python neuro_symbolic_demo.py

# 5. Run tests
python test_demo.py
```

---

## SWI-Prolog

Required for `neuro_symbolic_demo_prolog.py` and `neuro_symbolic_demo_ollama.py`.

### Windows

```powershell
winget install SWI-Prolog.SWI-Prolog
```

After installation, ensure `swipl.exe` is on your PATH. The installer usually adds it automatically.

### macOS

```bash
brew install swi-prolog
```

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install swi-prolog
```

### Verify installation

```bash
swipl --version
```

---

## Ollama (Optional)

Required only if you want the Ollama-backed natural-language layer in `neuro_symbolic_demo_ollama.py`. Without Ollama, that demo falls back to the regex layer and still runs.

### Windows

```powershell
winget install Ollama.Ollama
```

### macOS

```bash
brew install ollama
```

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Pull a model and start

```bash
# Start the Ollama server (if not already running as a service)
ollama serve

# In another terminal, pull a model
ollama pull qwen2.5:7b
```

### Verify installation

```bash
python neuro_symbolic_demo_ollama.py --status
```

---

## Python Version

The demos are tested on Python 3.10+. They may work on earlier versions but are not guaranteed.

---

## Troubleshooting

### `SwiPrologNotFoundError` when running Prolog demos

SWI-Prolog is either not installed or not on your PATH. Re-run the platform-specific installation steps above and verify with `swipl --version`.

### `ModuleNotFoundError: No module named 'pyswip'`

Run `pip install pyswip` (or `pip install -r requirements.txt`).

### Ollama demo hangs or times out

Ensure Ollama is running (`ollama serve`) and the model is pulled (`ollama pull qwen2.5:7b`). The demo will fall back to regex mode if Ollama is unreachable, but this check has a short timeout; if Ollama is starting up, wait a moment and retry.
