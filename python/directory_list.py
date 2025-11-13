"""Directory listing helpers built on :mod:`pathlib`.

Usage example
-------------
>>> from python import directory_list
>>> directory_list.glob_paths('.', '*.py')  # doctest: +ELLIPSIS
[PosixPath(...)]
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Iterator

PathLike = str | Path

__all__ = ["list_directory", "walk_directory", "glob_paths"]


def list_directory(path: PathLike, *, include_dirs: bool = True, include_files: bool = True) -> list[Path]:
    """Return entries in ``path`` filtered by type."""

    target = Path(path)
    entries = []
    for item in target.iterdir():
        if item.is_dir() and include_dirs:
            entries.append(item)
        elif item.is_file() and include_files:
            entries.append(item)
    return entries


def walk_directory(path: PathLike, *, follow_symlinks: bool = False) -> Iterator[tuple[Path, list[Path], list[Path]]]:
    """Yield ``(root, directories, files)`` tuples similar to :func:`os.walk`."""

    target = Path(path)
    for root, dirs, files in target.walk(follow_symlinks=follow_symlinks):  # type: ignore[attr-defined]
        yield root, [root / d for d in dirs], [root / f for f in files]


def glob_paths(path: PathLike, pattern: str, *, recursive: bool = False) -> list[Path]:
    """Return a sorted list of paths matching ``pattern``."""

    target = Path(path)
    iterator = target.rglob(pattern) if recursive else target.glob(pattern)
    return sorted(iterator)
