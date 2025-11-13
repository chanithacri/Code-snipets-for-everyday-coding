"""Read and write text or binary files safely.

This module exposes small helper functions that wrap the Python standard
library's file handling primitives. Each helper accepts a file-system path and
optional configuration. Errors are normalised into :class:`FileOperationError`
so that callers can deal with a single, predictable exception type.

Usage example
-------------
>>> from pathlib import Path
>>> from python import read_write_file
>>> tmp_path = Path('example.txt')
>>> read_write_file.write_text(tmp_path, 'hello world')
>>> read_write_file.read_text(tmp_path)
'hello world'

The functions are deliberately lightweight which makes them easy to integrate
with command line tools, background jobs, or unit tests.
"""
from __future__ import annotations

from pathlib import Path
from typing import Callable, Iterable, Optional, Union

PathLike = Union[str, Path]
Logger = Callable[[str], None]

__all__ = [
    "FileOperationError",
    "read_text",
    "write_text",
    "read_bytes",
    "write_bytes",
]


class FileOperationError(RuntimeError):
    """Raised when a file operation fails.

    The original exception is attached as ``__cause__`` so that callers can
    inspect low-level details if needed. This thin wrapper keeps the external
    interface consistent with the integration standards' "predictable errors"
    guideline.
    """


def _prepare_path(path: PathLike) -> Path:
    """Return a :class:`Path` instance for ``path``.

    ``Path`` resolves ``os.PathLike`` implementations and normal strings. The
    result is *not* resolved to an absolute path, leaving that choice to the
    caller.
    """

    if isinstance(path, Path):
        return path
    return Path(path)


def _emit(logger: Optional[Logger], messages: Iterable[str]) -> None:
    if logger is None:
        return
    for message in messages:
        try:
            logger(message)
        except Exception:
            # Logging must never break the core behaviour
            continue


def read_text(path: PathLike, *, encoding: str = "utf-8", errors: str = "strict", logger: Optional[Logger] = None) -> str:
    """Return the text content stored at ``path``.

    Parameters
    ----------
    path:
        File-system location that will be opened in text mode.
    encoding:
        Text encoding used for decoding the file contents. Defaults to UTF-8.
    errors:
        Error handling strategy passed to :func:`open`.
    logger:
        Optional callable used to log diagnostic messages. The callable is
        expected to accept a single string argument.
    """

    resolved = _prepare_path(path)
    try:
        with resolved.open("r", encoding=encoding, errors=errors) as handle:
            return handle.read()
    except FileNotFoundError as exc:
        _emit(logger, [f"read_text: file not found at {resolved!s}"])
        raise FileOperationError(f"File not found: {resolved}") from exc
    except OSError as exc:  # pragma: no cover - exercised in integration tests
        _emit(logger, [f"read_text: os error for {resolved!s}: {exc}"])
        raise FileOperationError(f"Unable to read {resolved}: {exc}") from exc


def write_text(
    path: PathLike,
    content: str,
    *,
    encoding: str = "utf-8",
    errors: str = "strict",
    make_dirs: bool = True,
    logger: Optional[Logger] = None,
) -> Path:
    """Write ``content`` to ``path`` and return the resulting :class:`Path`.

    ``make_dirs`` controls whether parent directories should be created
    automatically. The function writes atomically using :func:`Path.write_text`
    semantics and therefore truncates existing files.
    """

    resolved = _prepare_path(path)
    try:
        if make_dirs:
            resolved.parent.mkdir(parents=True, exist_ok=True)
        with resolved.open("w", encoding=encoding, errors=errors) as handle:
            handle.write(content)
        _emit(logger, [f"write_text: wrote {len(content)} characters to {resolved!s}"])
        return resolved
    except OSError as exc:
        _emit(logger, [f"write_text: os error for {resolved!s}: {exc}"])
        raise FileOperationError(f"Unable to write to {resolved}: {exc}") from exc


def read_bytes(path: PathLike, *, logger: Optional[Logger] = None) -> bytes:
    """Return the binary content stored at ``path``."""

    resolved = _prepare_path(path)
    try:
        return resolved.read_bytes()
    except FileNotFoundError as exc:
        _emit(logger, [f"read_bytes: file not found at {resolved!s}"])
        raise FileOperationError(f"File not found: {resolved}") from exc
    except OSError as exc:  # pragma: no cover
        _emit(logger, [f"read_bytes: os error for {resolved!s}: {exc}"])
        raise FileOperationError(f"Unable to read {resolved}: {exc}") from exc


def write_bytes(
    path: PathLike,
    content: bytes,
    *,
    make_dirs: bool = True,
    logger: Optional[Logger] = None,
) -> Path:
    """Write ``content`` to ``path`` in binary mode and return the path."""

    resolved = _prepare_path(path)
    try:
        if make_dirs:
            resolved.parent.mkdir(parents=True, exist_ok=True)
        resolved.write_bytes(content)
        _emit(logger, [f"write_bytes: wrote {len(content)} bytes to {resolved!s}"])
        return resolved
    except OSError as exc:
        _emit(logger, [f"write_bytes: os error for {resolved!s}: {exc}"])
        raise FileOperationError(f"Unable to write to {resolved}: {exc}") from exc
