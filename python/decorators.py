"""Common decorators for logging and timing function calls.

Usage example
-------------
>>> from python.decorators import log_calls
>>> @log_calls()
... def greet(name):
...     return f"hi {name}"
>>> greet('Ada')
'hi Ada'
"""

from __future__ import annotations

import time
from functools import wraps
from typing import Any, Callable, TypeVar

T = TypeVar("T")

__all__ = ["log_calls", "time_calls"]


def log_calls(logger: Callable[[str], None] | None = None) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator logging function entry and exit."""

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        log = logger or (lambda message: None)

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            log(f"call {func.__name__} args={args} kwargs={kwargs}")
            result = func(*args, **kwargs)
            log(f"return {func.__name__} -> {result!r}")
            return result

        return wrapper

    return decorator


def time_calls(clock: Callable[[], float] | None = None, logger: Callable[[str], None] | None = None) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator logging execution time for the wrapped function."""

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        log = logger or (lambda message: None)
        now = clock or time.perf_counter

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            start = now()
            try:
                return func(*args, **kwargs)
            finally:
                duration = now() - start
                log(f"time {func.__name__} {duration:.6f}s")

        return wrapper

    return decorator
