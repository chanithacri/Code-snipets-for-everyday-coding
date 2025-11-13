"""Timing helpers with dependency-free primitives.

The module provides a context manager and a decorator that record elapsed time
without touching global state. Callers can inject an alternative ``now``
function which makes the helpers deterministic in tests.

Usage example
-------------
>>> from general import timer
>>> with timer.Timer() as t:
...     _ = sum(range(100))
>>> isinstance(t.elapsed, float)
True
"""

from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass
from functools import wraps
from typing import Any, TypeVar

T = TypeVar("T")

__all__ = ["Timer", "time_call", "time_function"]


@dataclass
class Timer:
    """Measure elapsed time using ``time.perf_counter`` by default."""

    clock: Callable[[], float] = time.perf_counter
    start: float | None = None
    end: float | None = None

    def __enter__(self) -> "Timer":
        self.start = self.clock()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.end = self.clock()

    @property
    def elapsed(self) -> float:
        """Return the measured time in seconds."""

        if self.start is None:
            raise RuntimeError("Timer has not been started")
        end = self.end if self.end is not None else self.clock()
        return end - self.start


def time_call(func: Callable[..., T], *args: Any, clock: Callable[[], float] | None = None, **kwargs: Any) -> tuple[T, float]:
    """Execute ``func`` and return ``(result, elapsed_seconds)``."""

    clk = clock or time.perf_counter
    start = clk()
    result = func(*args, **kwargs)
    elapsed = clk() - start
    return result, elapsed


def time_function(clock: Callable[[], float] | None = None) -> Callable[[Callable[..., T]], Callable[..., tuple[T, float]]]:
    """Decorator returning ``(result, elapsed_seconds)`` for each invocation."""

    def decorator(func: Callable[..., T]) -> Callable[..., tuple[T, float]]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> tuple[T, float]:
            return time_call(func, *args, clock=clock, **kwargs)

        return wrapper

    return decorator
