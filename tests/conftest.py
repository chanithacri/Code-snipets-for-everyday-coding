"""Test configuration utilities."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNIPPET_ROOTS = [ROOT, ROOT / "python", ROOT / "javascript", ROOT / "java"]

for candidate in SNIPPET_ROOTS:
    candidate_str = str(candidate)
    if candidate_str not in sys.path:
        sys.path.insert(0, candidate_str)
