"""Flatten nested iterables and merge dictionaries.

Usage example
-------------
>>> from python.flatten_merge import flatten, merge_dicts
>>> flatten([1, [2, 3]])
[1, 2, 3]
>>> merge_dicts({'a': 1}, {'a': 2}, strategy='first')['a']
1
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

__all__ = ["flatten", "merge_dicts"]


def flatten(values: Iterable[Any]) -> list[Any]:
    """Return a flat list from arbitrarily nested ``values``."""

    result: list[Any] = []
    for value in values:
        if isinstance(value, (list, tuple, set)):
            result.extend(flatten(value))
        else:
            result.append(value)
    return result


def merge_dicts(*mappings: dict[str, Any], strategy: str = "override") -> dict[str, Any]:
    """Merge dictionaries using ``strategy``.

    ``override`` (default) keeps the last value, while ``first`` preserves the
    first occurrence of a key.
    """

    if strategy not in {"override", "first"}:
        raise ValueError("strategy must be 'override' or 'first'")
    result: dict[str, Any] = {}
    for mapping in mappings:
        for key, value in mapping.items():
            if strategy == "first" and key in result:
                continue
            result[key] = value
    return result
