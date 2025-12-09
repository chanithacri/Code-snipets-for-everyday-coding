# pytest_example

**Language:** Python

## Overview
Helpers used by doctests and pytest demonstrations.

Usage example
-------------
>>> from python.pytest_example import add
>>> add(1, 2)
3

## Usage
```python
from pytest_example import *  # import helpers
result = example()  # replace with a function from python/pytest_example.py
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/python/test_pytest_example.py

_Generated: 2025-12-08T17:27:58.290687Z_
