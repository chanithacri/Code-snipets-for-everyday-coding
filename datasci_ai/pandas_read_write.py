"""Read and write tabular data using pandas when available.

Usage example
-------------
>>> from datasci_ai import pandas_read_write as prw
>>> prw.read_table  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

try:  # pragma: no cover - optional dependency
    import pandas as pd
except Exception:  # pragma: no cover
    pd = None

PathLike = str | Path

__all__ = ["read_table", "write_table"]


def _require_pandas() -> Any:
    if pd is None:
        raise RuntimeError("pandas must be installed to use this helper")
    return pd


def read_table(path: PathLike, *, format: str = "csv", **kwargs: Any):
    """Return a DataFrame read from ``path``."""

    pandas = _require_pandas()
    if format == "csv":
        return pandas.read_csv(path, **kwargs)
    if format in {"xlsx", "xls"}:
        return pandas.read_excel(path, **kwargs)
    raise ValueError(f"Unsupported format: {format}")


def write_table(frame, path: PathLike, *, format: str = "csv", **kwargs: Any) -> Path:
    """Persist ``frame`` to ``path`` returning the output path."""

    pandas = _require_pandas()
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    if format == "csv":
        frame.to_csv(target, index=False, **kwargs)
    elif format in {"xlsx", "xls"}:
        frame.to_excel(target, index=False, **kwargs)
    else:
        raise ValueError(f"Unsupported format: {format}")
    return target
