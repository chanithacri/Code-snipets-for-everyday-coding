# exceptions

**Language:** Python

## Overview
Custom exception hierarchy for predictable error handling.

Usage example
-------------
>>> from python import exceptions
>>> raise exceptions.ValidationError('invalid input')
Traceback (most recent call last):
...
ValidationError: invalid input

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
See: tests/python/test_exceptions.py

_Generated: 2025-11-13T17:21:27.098689Z_
