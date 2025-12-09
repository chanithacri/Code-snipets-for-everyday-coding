# pdf_create

**Language:** Python

## Overview
Create simple PDF documents with ReportLab.

Usage example
-------------
>>> from python import pdf_create
>>> pdf_create.create_pdf('example.pdf', ['Hello'])  # doctest: +SKIP
PosixPath('example.pdf')

## Usage
```python
from pdf_create import *  # import helpers
result = example()  # replace with a function from python/pdf_create.py
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/python/test_pdf_create.py

_Generated: 2025-12-08T17:27:58.291255Z_
