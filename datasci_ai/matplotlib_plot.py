"""Plot simple charts using matplotlib with dependency injection.

Usage example
-------------
>>> from datasci_ai import matplotlib_plot
>>> matplotlib_plot.plot_line  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

try:  # pragma: no cover - optional dependency
    import matplotlib.pyplot as plt
except Exception:  # pragma: no cover
    plt = None

PathLike = str | Path

__all__ = ["plot_line", "plot_bar"]


def _require_matplotlib():
    if plt is None:
        raise RuntimeError("matplotlib must be installed to create plots")
    return plt


def plot_line(x: Sequence[float], y: Sequence[float], *, title: str = "Line Plot", output: PathLike | None = None) -> Path | None:
    """Plot ``y`` against ``x`` returning the saved file when ``output`` provided."""

    mpl = _require_matplotlib()
    fig, ax = mpl.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    if output is None:
        return None
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    mpl.close(fig)
    return path


def plot_bar(labels: Sequence[str], values: Sequence[float], *, title: str = "Bar Plot", output: PathLike | None = None) -> Path | None:
    """Create a bar chart for ``labels`` and ``values``."""

    mpl = _require_matplotlib()
    fig, ax = mpl.subplots()
    ax.bar(labels, values)
    ax.set_title(title)
    if output is None:
        return None
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    mpl.close(fig)
    return path
