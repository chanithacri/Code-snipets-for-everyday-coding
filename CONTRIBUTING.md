# 🤝 Contributing Guidelines

Thank you for contributing to **Code Snippets for Everyday Coding**!  
This repository is designed for both human developers and automation agents (like Codex or Windsurf)  
to collaborate efficiently and safely.

---

## 🧭 Overview

Our goal is to maintain a **clean, modular, and framework-agnostic** library of code snippets that can be:
- Implemented automatically by AI agents  
- Tested, documented, and versioned with minimal effort  
- Easily integrated into any existing project  

---

## 🧠 General Principles

- ✅ **Keep code portable:** no hardcoded paths or platform dependencies.  
- 🧩 **Inject config:** via env vars or parameters (see `adapters/`).  
- 🧱 **Use standard libraries:** avoid unnecessary dependencies.  
- 🧾 **Document everything:** include top-level docstrings or header comments.  
- ⚡ **Keep functions pure:** separate business logic from I/O or APIs.  
- 🧪 **Always include tests:** each snippet should have a matching file under `/tests/<language>/`.  
- 🔁 **One snippet = one responsibility.**

---

## 🧩 Folder Structure

| Folder | Purpose |
|:--|:--|
| `python/`, `java/`, `javascript/` | Core snippet stubs by language |
| `tests/` | Unit tests for each snippet |
| `docs/` | Auto-generated Markdown documentation |
| `adapters/` | Framework-agnostic helpers for logging & config |
| `scripts/` | Automation tools (e.g., doc generator) |
| `standards/` | Integration & architecture guidelines |
| `config/` | Default `.env` and example configs |

---

## ⚙️ Adding a New Snippet

1. **Pick the right folder** (language category).
2. **Create the file** — e.g., `python/example_snippet.py`.
3. **Add a docstring/header:**
   ```python
   """
   example_snippet: Demonstrates X feature
   Add a concise summary of the core logic here.
   """
