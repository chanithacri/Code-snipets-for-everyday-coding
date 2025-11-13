"""Persist scikit-learn models using joblib.

Usage example
-------------
>>> from datasci_ai import save_load_model
>>> save_load_model.save_model  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

from pathlib import Path

try:  # pragma: no cover - optional dependency
    import joblib
except Exception:  # pragma: no cover
    joblib = None

PathLike = str | Path

__all__ = ["save_model", "load_model"]


def _require_joblib():
    if joblib is None:
        raise RuntimeError("joblib must be installed to save models")
    return joblib


def save_model(model: object, path: PathLike) -> Path:
    """Serialise ``model`` to ``path``."""

    lib = _require_joblib()
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lib.dump(model, target)
    return target


def load_model(path: PathLike) -> object:
    """Load a model from ``path``."""

    lib = _require_joblib()
    return lib.load(path)
