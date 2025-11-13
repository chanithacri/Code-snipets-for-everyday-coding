"""Utilities for sorting lists of dictionaries.

Usage example
-------------
>>> from python.list_dict_sort import sort_records
>>> sort_records([{'name': 'Ada'}, {'name': 'Grace'}], 'name')[0]['name']
'Ada'
"""

from __future__ import annotations

from typing import Any, Iterable, Sequence

__all__ = ["sort_records"]


def sort_records(records: Iterable[dict[str, Any]], keys: Sequence[str] | str, *, reverse: bool = False, missing: Any = None) -> list[dict[str, Any]]:
    """Return a new list sorted by ``keys``.

    ``keys`` can be a single key or a sequence of keys which will be applied in
    order. Missing keys fall back to ``missing`` to keep the comparator stable.
    """

    if isinstance(keys, str):
        keys = [keys]

    def sort_key(record: dict[str, Any]) -> tuple[Any, ...]:
        return tuple(record.get(key, missing) for key in keys)  # type: ignore[arg-type]

    return sorted((dict(item) for item in records), key=sort_key, reverse=reverse)
