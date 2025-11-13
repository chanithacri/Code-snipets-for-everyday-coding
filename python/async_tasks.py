"""Asyncio helpers for running tasks with concurrency limits.

Usage example
-------------
>>> from python import async_tasks
>>> async def square(x):
...     return x * x
>>> async_tasks.run(async_tasks.gather_limited([square(2), square(3)], limit=1))
[4, 9]
"""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Iterable
from typing import Any, Callable, Sequence, TypeVar

T = TypeVar("T")

__all__ = ["run", "gather_limited"]


def run(coro: Awaitable[T]) -> T:
    """Execute ``coro`` using :func:`asyncio.run`.

    This helper exists primarily to make testing easier by hiding the
    ``asyncio.run`` import in one place.
    """

    return asyncio.run(coro)


async def gather_limited(
    coroutines: Iterable[Awaitable[T]],
    *,
    limit: int = 5,
    on_error: Callable[[Exception], None] | None = None,
) -> list[T]:
    """Gather awaitables honouring the concurrency ``limit``."""

    semaphore = asyncio.Semaphore(limit)

    async def worker(coro: Awaitable[T]) -> T:
        async with semaphore:
            try:
                return await coro
            except Exception as exc:
                if on_error is not None:
                    on_error(exc)
                raise

    tasks = [asyncio.create_task(worker(coro)) for coro in coroutines]
    results: list[T] = []
    for task in tasks:
        results.append(await task)
    return results
