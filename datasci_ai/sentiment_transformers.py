"""Run sentiment analysis using a transformers pipeline.

Usage example
-------------
>>> from datasci_ai import sentiment_transformers
>>> sentiment_transformers.load_pipeline  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

from typing import Any, Iterable

try:  # pragma: no cover - optional dependency
    from transformers import pipeline
except Exception:  # pragma: no cover
    pipeline = None

__all__ = ["load_pipeline", "predict"]


def load_pipeline(model: str = "distilbert-base-uncased-finetuned-sst-2-english"):
    """Return a configured transformers pipeline."""

    if pipeline is None:
        raise RuntimeError("transformers must be installed to load pipelines")
    return pipeline("sentiment-analysis", model=model)


def predict(pipe, texts: Iterable[str]) -> list[dict[str, Any]]:
    """Run ``texts`` through ``pipe`` returning a list of predictions."""

    return list(pipe(list(texts)))
