# sqlite_ops

**Language:** Python

## Overview
SQLite helpers built on :mod:`sqlite3`.

Usage example
-------------
>>> from python import sqlite_ops
>>> sqlite_ops.execute('CREATE TABLE demo(id INTEGER PRIMARY KEY, name TEXT)')
0
>>> sqlite_ops.execute('INSERT INTO demo(name) VALUES (?)', ['Ada'])
1
>>> [row['name'] for row in sqlite_ops.query_all('SELECT name FROM demo')]
['Ada']

## Usage
```python
# TODO: add example
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/python/test_sqlite_ops.py

_Generated: 2025-11-13T17:21:27.101113Z_
