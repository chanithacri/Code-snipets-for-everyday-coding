# 🤖 Agent Setup Guide

This document explains how a coding agent (like Codex, Windsurf, or a custom automation runner)  
should interact with this repository.

---

## 1️⃣ Initialization

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Code-snippets-for-everyday-coding.git
   cd Code-snippets-for-everyday-coding
   ```

2. **Load manifest and tasks**
   - `manifest.json` → file paths, languages, and descriptions  
   - `tasks.json` → automation goals, test files, and success criteria  

3. **Optional: Set up dependencies**
   - Python:  
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     pip install pytest
     ```
   - JavaScript:  
     ```bash
     npm install jest
     ```
   - Java:  
     Use built-in JDK 17+ compiler and JUnit if tests are added.

---

## 2️⃣ Implementation Cycle

1. **Select next pending task**  
   Example task object from `tasks.json`:
   ```json
   {
     "id": "python_read_write_file",
     "file": "python/read_write_file.py",
     "goal": "Implement read and write file operations with error handling.",
     "test": "tests/python/test_read_write_file.py",
     "criteria": [
       "Must read a file safely using 'with open'",
       "Must handle FileNotFoundError gracefully"
     ]
   }
   ```

2. **Implement snippet**
   - Follow `standards/INTEGRATION_STANDARDS.md`
   - Use adapters for logging and configuration
   - Keep functions pure and return simple data (no framework objects)
   - Add a short docstring with usage example

3. **Run tests**
   ```bash
   pytest -q tests/python/test_read_write_file.py
   # or
   npx jest tests/javascript/fetch_get_post.test.js
   # or
   javac $(find . -name "*.java")
   ```

4. **Update progress**
   - Mark task as complete in `progress.json`
   - Add timestamp and completion notes  
   Example:
   ```json
   {
     "id": "python_read_write_file",
     "status": "done",
     "timestamp": "2025-11-12T13:30Z",
     "notes": "Implemented and tested successfully"
   }
   ```

5. **Generate documentation**
   ```bash
   python scripts/generate_docs.py
   ```

6. **Commit & push**
   ```bash
   git add .
   git commit -m "Implemented: python_read_write_file ✅"
   git push
   ```

---

## 3️⃣ Continuous Integration

The repository includes two GitHub Actions workflows:
- `.github/workflows/codex_test.yml` → runs all language tests
- `.github/workflows/docs.yml` → regenerates documentation on push

These workflows ensure code quality, test success, and up-to-date documentation.

---

## 4️⃣ Optional Enhancements

Agents can optionally:
- **Auto-create issues** for incomplete or failed tasks
- **Auto-generate changelogs**
- **Auto-deploy docs** to GitHub Pages
- **Create releases/tags** for completed milestones (e.g., `v1.0.0`)

---

## 5️⃣ Expected Agent Output

Each successfully implemented task should result in:
1. ✅ A working, tested snippet  
2. 📄 A generated doc file under `/docs/<language>/`  
3. 🧠 An updated `progress.json` entry  
4. 📤 A committed and pushed update  

---

## 6️⃣ Example Full Cycle

1. Agent clones the repo  
2. Reads `tasks.json` and selects first pending task  
3. Implements the snippet and test  
4. Runs tests until they pass  
5. Generates docs  
6. Updates `progress.json`  
7. Commits and pushes the changes  

This process repeats automatically until all tasks are complete.

---

## 💡 Notes for Agents

- Never overwrite manual changes unless explicitly allowed.  
- Avoid adding large dependencies — prefer standard libraries.  
- Keep output consistent with integration standards.  
- Update `progress.json` and `docs` after each snippet completion.  
- Always include a usage example in the snippet docstring.

---

With this setup, your agent can independently:
🧠 **implement**, 🧪 **test**, 📚 **document**, and 📈 **track** its progress — all while staying compatible with any language or framework.