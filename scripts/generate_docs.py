"""generate_docs.py
Scans language folders for snippet files, extracts top-level docstrings/comments,
and produces Markdown files in /docs. Designed to be lightweight and project-agnostic.
"""
from __future__ import annotations
import os, re, json, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent
LANG_DIRS = {
    "python": ("python", ".py"),
    "java": ("java", ".java"),
    "javascript": ("javascript", ".js"),
}

DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)

def extract_header_text(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix == ".py":
        m = re.search(r'^\s*"""([\s\S]*?)"""', text)
        return (m.group(1).strip() if m else "").strip()
    if path.suffix == ".js":
        m = re.search(r'/\*\*([\s\S]*?)\*/', text)
        return (m.group(1).strip() if m else "").strip()
    if path.suffix == ".java":
        m = re.search(r'/\*\*([\s\S]*?)\*/', text)
        return (m.group(1).strip() if m else "").strip()
    return ""

DOC_TMPL = """# {name}

**Language:** {language}

## Overview
{overview}

## Usage
```{codeblock}
# TODO: add example
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: {test_path}

_Generated: {timestamp}_
"""

def write_doc(language: str, file: pathlib.Path):
    rel = file.relative_to(ROOT)
    name = file.stem
    overview = extract_header_text(file) or "TODO: Add header comment/docstring in snippet."
    lang_dir = DOCS / language
    lang_dir.mkdir(parents=True, exist_ok=True)
    out = lang_dir / f"{name}.md"
    test_path = f"tests/{language}/{'test_' if language=='python' else ''}{name}{'.py' if language=='python' else ('Test.java' if language=='java' else '.test.js')}"
    out.write_text(DOC_TMPL.format(
        name=name,
        language=language.capitalize(),
        overview=overview,
        codeblock=language if language!='javascript' else 'javascript',
        test_path=test_path,
        timestamp=datetime.datetime.utcnow().isoformat()+'Z'
    ), encoding='utf-8')

def main():
    for language, (folder, ext) in LANG_DIRS.items():
        lang_path = ROOT / folder
        if not lang_path.exists():
            continue
        for file in lang_path.rglob(f"*{ext}"):
            write_doc(language, file)
    # Update progress.json timestamp if present
    pjson = ROOT / "progress.json"
    if pjson.exists():
        try:
            data = json.loads(pjson.read_text(encoding="utf-8"))
            data["last_updated"] = datetime.datetime.utcnow().isoformat() + "Z"
            pjson.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except Exception:
            pass

if __name__ == "__main__":
    main()
