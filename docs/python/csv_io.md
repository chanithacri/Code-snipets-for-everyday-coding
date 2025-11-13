# csv_io

**Language:** Python

## Overview
Read and write CSV files with optional pandas support.

Usage example
-------------
>>> from python import csv_io
>>> rows = csv_io.read_csv(csv_io.write_csv('tmp.csv', [{'name': 'Ada'}]))
>>> rows[0]['name']
'Ada'

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
See: tests/python/test_csv_io.py

_Generated: 2025-11-13T17:21:27.099397Z_
