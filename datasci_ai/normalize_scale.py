"""Normalise or standardise numeric arrays.

Usage example
-------------
>>> from datasci_ai.normalize_scale import min_max_scale
>>> min_max_scale([1, 2, 3])
[0.0, 0.5, 1.0]
"""

from __future__ import annotations

from typing import Sequence

__all__ = ["min_max_scale", "z_score"]


def min_max_scale(values: Sequence[float]) -> list[float]:
    """Scale ``values`` to the ``[0, 1]`` range."""

    if not values:
        return []
    minimum = min(values)
    maximum = max(values)
    if minimum == maximum:
        return [0.0 for _ in values]
    span = maximum - minimum
    return [(value - minimum) / span for value in values]


def z_score(values: Sequence[float]) -> list[float]:
    """Return z-scores for ``values``."""

    if not values:
        return []
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    if variance == 0:
        return [0.0 for _ in values]
    std = variance ** 0.5
    return [(value - mean) / std for value in values]
