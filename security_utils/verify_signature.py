"""Verify file signatures using deterministic digests.

Usage example
-------------
>>> from pathlib import Path  # doctest: +SKIP
>>> from security_utils import hash_strings, verify_signature  # doctest: +SKIP
>>> tmp = Path('example.txt')  # doctest: +SKIP
>>> _ = tmp.write_text('data')  # doctest: +SKIP
>>> digest = hash_strings.hash_file(tmp)  # doctest: +SKIP
>>> verify_signature.verify_digest(tmp, digest)  # doctest: +SKIP
True
"""

from __future__ import annotations

from pathlib import Path
from typing import Callable

from .hash_strings import hash_file

PathLike = str | Path

__all__ = ["verify_digest", "Verifier"]

Verifier = Callable[[PathLike, str], bool]


def verify_digest(path: PathLike, signature_hex: str, *, algorithm: str = "sha256") -> bool:
    """Return ``True`` when the digest of ``path`` matches ``signature_hex``."""

    actual = hash_file(path, algorithm=algorithm)
    expected = signature_hex.lower()
    int(expected, 16)
    return actual == expected
