"""Apply callable to a pandas DataFrame column.

Usage example
-------------
>>> from datasci_ai import apply_function
>>> apply_function.apply_to_column  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

from typing import Any, Callable

try:  # pragma: no cover - optional dependency
    import pandas as pd
except Exception:  # pragma: no cover
    pd = None

__all__ = ["apply_to_column"]


def apply_to_column(frame, column: str, func: Callable[[Any], Any]):
    """Return a copy of ``frame`` with ``func`` applied to ``column``."""

    if pd is None:
        raise RuntimeError("pandas must be installed to use this helper")
    copy = frame.copy()
    copy[column] = copy[column].map(func)
    return copy
