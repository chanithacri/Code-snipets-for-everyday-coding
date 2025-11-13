"""Compute and optionally plot correlation heatmaps.

Usage example
-------------
>>> from datasci_ai import correlation_heatmap
>>> correlation_heatmap.compute  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

try:  # pragma: no cover - optional dependency
    import pandas as pd
except Exception:  # pragma: no cover
    pd = None

try:  # pragma: no cover - optional dependency
    import seaborn as sns
    import matplotlib.pyplot as plt
except Exception:  # pragma: no cover
    sns = None
    plt = None

PathLike = str | Path

__all__ = ["compute", "plot"]


def compute(frame) -> Any:
    """Return the correlation matrix for ``frame``."""

    if pd is None:
        raise RuntimeError("pandas must be installed to compute correlations")
    return frame.corr(numeric_only=True)


def plot(matrix, *, output: PathLike | None = None, annot: bool = True) -> Path | None:
    """Plot ``matrix`` as a heatmap returning ``output`` when provided."""

    if sns is None or plt is None:
        raise RuntimeError("seaborn and matplotlib must be installed to plot heatmaps")
    ax = sns.heatmap(matrix, annot=annot)
    fig = ax.get_figure()
    if output is None:
        return None
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    plt.close(fig)
    return path
