"""Read and write CSV files with optional pandas support.

Usage example
-------------
>>> from python import csv_io
>>> rows = csv_io.read_csv(csv_io.write_csv('tmp.csv', [{'name': 'Ada'}]))
>>> rows[0]['name']
'Ada'
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, Mapping, MutableMapping, Sequence

try:  # pragma: no cover - optional dependency
    import pandas as _pd  # type: ignore
except Exception:  # pragma: no cover - dependency is optional
    _pd = None

PathLike = str | Path
Row = Mapping[str, object]

__all__ = ["CSVError", "read_csv", "write_csv"]


class CSVError(RuntimeError):
    """Raised when CSV operations fail."""


def read_csv(
    path: PathLike,
    *,
    encoding: str = "utf-8",
    dialect: str = "excel",
    engine: str = "csv",
) -> list[dict[str, str]]:
    """Return the contents of ``path`` as a list of dictionaries."""

    try:
        if engine == "pandas":
            if _pd is None:
                raise RuntimeError("pandas is not installed")
            frame = _pd.read_csv(path, encoding=encoding)  # type: ignore[call-arg]
            return frame.to_dict(orient="records")  # type: ignore[return-value]
        with Path(path).open("r", encoding=encoding, newline="") as handle:
            reader = csv.DictReader(handle, dialect=dialect)
            return [dict(row) for row in reader]
    except Exception as exc:
        raise CSVError(f"Failed to read CSV from {path}: {exc}") from exc


def write_csv(
    path: PathLike,
    rows: Iterable[Row],
    *,
    fieldnames: Sequence[str] | None = None,
    encoding: str = "utf-8",
    dialect: str = "excel",
    extrasaction: str = "raise",
    engine: str = "csv",
) -> Path:
    """Write ``rows`` to ``path`` returning the output path."""

    output = Path(path)
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        if engine == "pandas":
            if _pd is None:
                raise RuntimeError("pandas is not installed")
            frame = _pd.DataFrame(list(rows))
            frame.to_csv(output, index=False, encoding=encoding)  # type: ignore[call-arg]
            return output
        materialised = list(rows)
        if not materialised:
            if fieldnames is None:
                raise ValueError("rows is empty and fieldnames were not provided")
            header = list(fieldnames)
            with output.open("w", encoding=encoding, newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=header, extrasaction=extrasaction, dialect=dialect)
                writer.writeheader()
            return output
        header = list(fieldnames or materialised[0].keys())
        with output.open("w", encoding=encoding, newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=header, extrasaction=extrasaction, dialect=dialect)
            writer.writeheader()
            for row in materialised:
                writer.writerow(row)
        return output
    except Exception as exc:
        raise CSVError(f"Failed to write CSV to {output}: {exc}") from exc
