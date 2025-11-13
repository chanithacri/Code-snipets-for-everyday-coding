"""Generate UUIDs and short identifiers without global state.

Usage example
-------------
>>> from general.uuid_gen import generate_uuid, generate_short_id
>>> isinstance(generate_uuid(), str)
True
>>> len(generate_short_id(length=6))
6
"""

from __future__ import annotations

import secrets
import string
import uuid
from typing import Iterable

__all__ = ["generate_uuid", "generate_short_id", "UUID_ALPHABET"]

UUID_ALPHABET = string.ascii_lowercase + string.digits


def generate_uuid() -> str:
    """Return a random UUID4 string."""

    return str(uuid.uuid4())


def generate_short_id(*, length: int = 8, alphabet: Iterable[str] | None = None) -> str:
    """Return a URL-safe identifier with ``length`` characters."""

    if length <= 0:
        raise ValueError("length must be positive")
    chars = alphabet or UUID_ALPHABET
    if isinstance(chars, str):
        population = chars
    else:
        population = "".join(chars)
    if not population:
        raise ValueError("alphabet must contain at least one character")
    return "".join(secrets.choice(population) for _ in range(length))
