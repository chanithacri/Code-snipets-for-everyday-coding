"""Hash strings or files using algorithms from :mod:`hashlib`.

Usage example
-------------
>>> from security_utils.hash_strings import hash_string
>>> hash_string('hello')
'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
"""

from __future__ import annotations

import hashlib
from pathlib import Path

PathLike = str | Path

__all__ = ["hash_string", "hash_file", "verify_hash"]


def _new_hasher(algorithm: str) -> hashlib._Hash:
    try:
        return hashlib.new(algorithm)
    except ValueError as exc:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}") from exc


def hash_string(value: str, *, algorithm: str = "sha256", encoding: str = "utf-8") -> str:
    """Return the hexadecimal digest for ``value``."""

    hasher = _new_hasher(algorithm)
    hasher.update(value.encode(encoding))
    return hasher.hexdigest()


def hash_file(path: PathLike, *, algorithm: str = "sha256", chunk_size: int = 1024 * 64) -> str:
    """Return the hexadecimal digest for the file at ``path``."""

    hasher = _new_hasher(algorithm)
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def verify_hash(value: str, expected_hex: str, *, algorithm: str = "sha256") -> bool:
    """Return ``True`` when ``value`` hashes to ``expected_hex``."""

    digest = hash_string(value, algorithm=algorithm)
    return hashlib.compare_digest(digest, expected_hex)
