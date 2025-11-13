"""Utilities for safely reading and writing files.

The helpers in this module wrap Python's :mod:`pathlib` I/O primitives and
normalise errors into :class:`FileOperationError`. That means callers only need
to catch a single exception type regardless of whether a permission issue, a
missing parent directory, or a transient I/O error occurred.

The functions take :class:`pathlib.Path` instances or any object supported by
``Path()``. They never mutate global state and parents are created on demand
when writing files.

Usage example
-------------
>>> from pathlib import Path
>>> tmp_path = Path('example.txt')
>>> write_text(tmp_path, 'hello world')
>>> read_text(tmp_path)
'hello world'
"""

from __future__ import annotations

from pathlib import Path
from typing import Union

PathLike = Union[str, Path]

__all__ = [
    "FileOperationError",
    "read_text",
    "write_text",
    "read_bytes",
    "write_bytes",
]


class FileOperationError(RuntimeError):
    """Raised when a file operation fails.

    The error message always includes the offending path so that upstream code
    can log or display useful information without inspecting ``__cause__``.
    """


def _resolve_path(path: PathLike) -> Path:
    return path if isinstance(path, Path) else Path(path)


def _raise(path: Path, exc: OSError) -> None:
    raise FileOperationError(f"{path} - {exc.strerror or exc}") from exc


def read_text(path: PathLike, *, encoding: str = "utf-8", errors: str = "strict") -> str:
    """Return the text content of ``path``.

    Parameters
    ----------
    path:
        File path to read.
    encoding:
        Text encoding used by :func:`pathlib.Path.read_text`.
    errors:
        Error handling strategy, see :func:`open`.
    """

    target = _resolve_path(path)
    try:
        return target.read_text(encoding=encoding, errors=errors)
    except OSError as exc:  # pragma: no cover - integration tests exercise error paths
        _raise(target, exc)


def write_text(
    path: PathLike,
    data: str,
    *,
    encoding: str = "utf-8",
    errors: str = "strict",
    create_parent: bool = True,
) -> None:
    """Persist ``data`` to ``path``.

    ``create_parent`` mirrors ``Path.touch`` and creates missing parent
    directories when set to ``True`` (the default). The function returns
    ``None`` which keeps the API easy to test and to compose with other
    helpers.
    """

    target = _resolve_path(path)
    try:
        if create_parent:
            target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(data, encoding=encoding, errors=errors)
    except OSError as exc:
        _raise(target, exc)


def read_bytes(path: PathLike) -> bytes:
    """Return the raw bytes stored at ``path``."""

    target = _resolve_path(path)
    try:
        return target.read_bytes()
    except OSError as exc:
        _raise(target, exc)


def write_bytes(
    path: PathLike,
    data: Union[bytes, bytearray, memoryview],
    *,
    create_parent: bool = True,
) -> None:
    """Write ``data`` to ``path``.

    The function accepts any object implementing the buffer protocol which
    keeps the helper flexible enough for integration with libraries that
    provide ``memoryview`` objects.
    """

    target = _resolve_path(path)
    try:
        if create_parent:
            target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(bytes(data))
    except OSError as exc:
        _raise(target, exc)
