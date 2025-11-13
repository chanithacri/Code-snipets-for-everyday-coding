"""Memoisation helpers with optional TTL support.

Usage example
-------------
>>> from general.memoize_cache import memoize
>>> calls = []
>>> @memoize(maxsize=2)
... def add(a, b):
...     calls.append(1)
...     return a + b
>>> add(1, 2)
3
>>> add(1, 2)
3
>>> len(calls)
1
"""

from __future__ import annotations

import time
from collections import OrderedDict
from collections.abc import Callable
from dataclasses import dataclass
from functools import wraps
from typing import Any, Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")
F = TypeVar("F", bound=Callable[..., Any])

__all__ = ["CacheEntry", "MemoizeCache", "memoize"]


@dataclass
class CacheEntry(Generic[V]):
    value: V
    expires_at: float | None


class MemoizeCache(Generic[K, V]):
    """A lightweight LRU cache with optional TTL semantics."""

    def __init__(self, *, maxsize: int = 128, ttl: float | None = None, clock: Callable[[], float] | None = None) -> None:
        if maxsize <= 0:
            raise ValueError("maxsize must be positive")
        self.maxsize = maxsize
        self.ttl = ttl
        self.clock = clock or time.monotonic
        self._data: "OrderedDict[K, CacheEntry[V]]" = OrderedDict()

    def get(self, key: K, factory: Callable[[], V]) -> V:
        now = self.clock()
        entry = self._data.get(key)
        if entry is not None and (entry.expires_at is None or entry.expires_at > now):
            self._data.move_to_end(key)
            return entry.value
        if entry is not None:
            del self._data[key]
        value = factory()
        expires = None if self.ttl is None else now + self.ttl
        self._data[key] = CacheEntry(value=value, expires_at=expires)
        self._evict()
        return value

    def clear(self) -> None:
        self._data.clear()

    def _evict(self) -> None:
        while len(self._data) > self.maxsize:
            self._data.popitem(last=False)


def memoize(*, maxsize: int = 128, ttl: float | None = None, clock: Callable[[], float] | None = None) -> Callable[[F], F]:
    """Decorator returning a memoised version of ``func``."""

    def decorator(func: F) -> F:
        cache = MemoizeCache(maxsize=maxsize, ttl=ttl, clock=clock)

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):  # type: ignore[misc]
            key = (args, frozenset(kwargs.items()))
            return cache.get(key, lambda: func(*args, **kwargs))

        wrapper.cache = cache  # type: ignore[attr-defined]
        return wrapper  # type: ignore[return-value]

    return decorator
