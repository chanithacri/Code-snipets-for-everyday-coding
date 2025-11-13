"""Helpers used by doctests and pytest demonstrations.

Usage example
-------------
>>> from python.pytest_example import add
>>> add(1, 2)
3
"""

from __future__ import annotations

from dataclasses import dataclass

__all__ = ["add", "Counter"]


def add(a: int, b: int) -> int:
    """Return ``a + b`` with a descriptive docstring for tests."""

    return a + b


@dataclass
class Counter:
    """Simple mutable counter used in tests."""

    value: int = 0

    def increment(self, step: int = 1) -> int:
        self.value += step
        return self.value
