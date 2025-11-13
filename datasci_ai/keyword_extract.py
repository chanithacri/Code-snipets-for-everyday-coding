"""Extract keywords using a TF-IDF vectorizer.

Usage example
-------------
>>> from datasci_ai import keyword_extract
>>> keyword_extract.extract_keywords  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

from typing import Iterable

try:  # pragma: no cover - optional dependency
    from sklearn.feature_extraction.text import TfidfVectorizer
except Exception:  # pragma: no cover
    TfidfVectorizer = None

__all__ = ["extract_keywords"]


def extract_keywords(documents: Iterable[str], *, top_n: int = 5) -> list[list[str]]:
    """Return ``top_n`` keywords for each document."""

    if TfidfVectorizer is None:
        raise RuntimeError("scikit-learn must be installed to extract keywords")
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    results: list[list[str]] = []
    for row in matrix:
        scores = row.toarray().ravel()
        indices = scores.argsort()[::-1][:top_n]
        results.append([feature_names[idx] for idx in indices if scores[idx] > 0])
    return results
