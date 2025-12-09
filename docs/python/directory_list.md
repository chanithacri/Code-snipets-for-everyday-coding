# directory_list

**Language:** Python

## Overview
Directory listing helpers built on :mod:`pathlib`.

Usage example
-------------
>>> from python import directory_list
>>> directory_list.glob_paths('.', '*.py')  # doctest: +ELLIPSIS
[PosixPath(...)]

## Usage
```python
from directory_list import *  # import helpers
result = example()  # replace with a function from python/directory_list.py
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/python/test_directory_list.py

_Generated: 2025-12-08T17:27:58.294932Z_
