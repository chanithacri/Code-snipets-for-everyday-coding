# excel_io

**Language:** Python

## Overview
Read and write simple Excel files using :mod:`openpyxl`.

Usage example
-------------
>>> from python import excel_io
>>> excel_io.write_workbook('example.xlsx', [{'name': 'Ada'}])  # doctest: +SKIP
PosixPath('example.xlsx')

## Usage
```python
from excel_io import *  # import helpers
result = example()  # replace with a function from python/excel_io.py
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/python/test_excel_io.py

_Generated: 2025-12-08T17:27:58.294349Z_
