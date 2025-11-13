"""Produce naive summaries by selecting the leading sentences.

Usage example
-------------
>>> from datasci_ai.auto_summarize import summarize
>>> summarize('One. Two. Three.', max_sentences=2)
'One. Two.'
"""

from __future__ import annotations

import re

__all__ = ["summarize"]

_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")


def summarize(text: str, *, max_sentences: int = 3) -> str:
    """Return the first ``max_sentences`` sentences from ``text``."""

    sentences = _SENTENCE_RE.split(text.strip())
    return " ".join(sentences[:max_sentences])
