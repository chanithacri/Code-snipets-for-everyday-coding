# read_write_file

**Language:** Python

## Overview
Read and write text or binary files safely.

This module exposes small helper functions that wrap the Python standard
library's file handling primitives. Each helper accepts a file-system path and
optional configuration. Errors are normalised into :class:`FileOperationError`
so that callers can deal with a single, predictable exception type.

Usage example
-------------
>>> from pathlib import Path
>>> from python import read_write_file
>>> tmp_path = Path('example.txt')
>>> read_write_file.write_text(tmp_path, 'hello world')
>>> read_write_file.read_text(tmp_path)
'hello world'

The functions are deliberately lightweight which makes them easy to integrate
with command line tools, background jobs, or unit tests.

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
See: tests/python/test_read_write_file.py

_Generated: 2025-11-13T13:55:58.546919Z_
