"""Train a simple scikit-learn linear regression model.

Usage example
-------------
>>> from datasci_ai import simple_model
>>> simple_model.train  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

from typing import Sequence

try:  # pragma: no cover - optional dependency
    from sklearn.linear_model import LinearRegression
except Exception:  # pragma: no cover
    LinearRegression = None

__all__ = ["train", "predict"]


def train(features: Sequence[Sequence[float]], targets: Sequence[float]) -> object:
    """Fit a linear regression model returning the estimator."""

    if LinearRegression is None:
        raise RuntimeError("scikit-learn must be installed to train models")
    model = LinearRegression()
    model.fit(features, targets)
    return model


def predict(model: object, features: Sequence[Sequence[float]]) -> list[float]:
    """Run predictions using ``model``."""

    if not hasattr(model, "predict"):
        raise TypeError("model must provide a predict method")
    return list(model.predict(features))
