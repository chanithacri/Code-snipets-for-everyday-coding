"""Zip and unzip files using the standard library.

Usage example
-------------
>>> from python.archive_zip import create_archive, extract_archive
>>> archive = create_archive(['manifest.json'], 'bundle.zip')
>>> extract_archive(archive, 'tmp')  # doctest: +ELLIPSIS
PosixPath('tmp')
"""

from __future__ import annotations

import zipfile
from pathlib import Path
from typing import Iterable

PathLike = str | Path

__all__ = ["create_archive", "extract_archive"]


def create_archive(paths: Iterable[PathLike], destination: PathLike, *, compression: int = zipfile.ZIP_DEFLATED) -> Path:
    """Create a zip archive at ``destination`` containing ``paths``."""

    output = Path(destination)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=compression) as archive:
        for raw in paths:
            path = Path(raw)
            archive.write(path, arcname=path.name)
    return output


def extract_archive(archive_path: PathLike, target_directory: PathLike) -> Path:
    """Extract ``archive_path`` into ``target_directory``."""

    archive_file = Path(archive_path)
    target = Path(target_directory)
    target.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive_file, "r") as archive:
        archive.extractall(target)
    return target
