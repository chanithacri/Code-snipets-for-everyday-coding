"""Environment variable helpers with predictable defaults.

Usage example
-------------
>>> from general.env_vars import get_env, as_bool
>>> get_env("APP_NAME", default="demo", env={})
'demo'
>>> as_bool("TRUE")
True
"""

from __future__ import annotations

import os
from typing import Any, Callable, Mapping

__all__ = ["get_env", "require_env", "as_bool"]


def get_env(name: str, default: Any | None = None, *, cast: Callable[[str], Any] | None = None, env: Mapping[str, str] | None = None) -> Any:
    """Return ``name`` from ``env`` converting it with ``cast`` if provided."""

    source = env or os.environ
    raw = source.get(name)
    if raw is None:
        return default
    return cast(raw) if cast else raw


def require_env(name: str, *, env: Mapping[str, str] | None = None) -> str:
    """Return ``name`` or raise :class:`KeyError` when missing."""

    source = env or os.environ
    if name not in source:
        raise KeyError(f"Missing required environment variable: {name}")
    return source[name]


def as_bool(value: str) -> bool:
    """Interpret ``value`` using a permissive set of truthy tokens."""

    return value.strip().lower() in {"1", "true", "yes", "on"}
