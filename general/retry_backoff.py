"""Retry helpers with exponential backoff.

Usage example
-------------
>>> from general.retry_backoff import retry, RetryConfig
>>> attempts = []
>>> def flaky():
...     attempts.append('x')
...     if len(attempts) < 2:
...         raise RuntimeError('fail')
...     return 'ok'
>>> retry(flaky, config=RetryConfig(attempts=3, backoff=0))
'ok'
"""

from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

__all__ = ["RetryConfig", "retry"]


@dataclass
class RetryConfig:
    """Configuration for :func:`retry`.

    Attributes
    ----------
    attempts:
        Number of tries before giving up (default 3).
    backoff:
        Initial backoff delay in seconds.
    multiplier:
        Backoff multiplier applied after each failure.
    exceptions:
        Tuple of exception types triggering a retry.
    """

    attempts: int = 3
    backoff: float = 0.5
    multiplier: float = 2.0
    exceptions: tuple[type[Exception], ...] = (Exception,)


def retry(
    func: Callable[..., Any],
    *args: Any,
    config: RetryConfig | None = None,
    sleep: Callable[[float], None] = time.sleep,
    **kwargs: Any,
) -> Any:
    """Invoke ``func`` retrying on configured exceptions."""

    cfg = config or RetryConfig()
    delay = cfg.backoff
    attempt = 0
    while True:
        try:
            return func(*args, **kwargs)
        except cfg.exceptions as exc:
            attempt += 1
            if attempt >= cfg.attempts:
                raise
            sleep(delay)
            delay *= cfg.multiplier
