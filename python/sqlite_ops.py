"""SQLite helpers built on :mod:`sqlite3`.

Usage example
-------------
>>> from python import sqlite_ops
>>> sqlite_ops.execute('CREATE TABLE demo(id INTEGER PRIMARY KEY, name TEXT)')
0
>>> sqlite_ops.execute('INSERT INTO demo(name) VALUES (?)', ['Ada'])
1
>>> [row['name'] for row in sqlite_ops.query_all('SELECT name FROM demo')]
['Ada']
"""

from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator, Sequence

PathLike = str | Path

__all__ = ["DatabaseConfig", "connect", "execute", "query_all"]


class DatabaseConfig(dict):
    """Configuration container for SQLite connections."""

    @property
    def path(self) -> PathLike:
        return self.get("path", ":memory:")

    @property
    def isolation_level(self) -> str | None:
        return self.get("isolation_level")


def connect(config: DatabaseConfig | None = None) -> sqlite3.Connection:
    cfg = config or DatabaseConfig()
    return sqlite3.connect(cfg.path, isolation_level=cfg.isolation_level)


@contextmanager
def connection_scope(connection: sqlite3.Connection | None = None, *, config: DatabaseConfig | None = None) -> Iterator[sqlite3.Connection]:
    conn = connection or connect(config)
    try:
        yield conn
    finally:
        if connection is None:
            conn.close()


def execute(sql: str, parameters: Sequence[Any] | None = None, *, connection: sqlite3.Connection | None = None, config: DatabaseConfig | None = None) -> int:
    """Execute ``sql`` returning the affected row count."""

    params = parameters or []
    with connection_scope(connection, config=config) as conn:
        cursor = conn.execute(sql, params)
        conn.commit()
        return cursor.rowcount


def query_all(sql: str, parameters: Sequence[Any] | None = None, *, connection: sqlite3.Connection | None = None, config: DatabaseConfig | None = None) -> list[sqlite3.Row]:
    """Return all rows for ``sql`` using ``sqlite3.Row`` objects."""

    params = parameters or []
    with connection_scope(connection, config=config) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(sql, params)
        rows = cursor.fetchall()
    return rows
