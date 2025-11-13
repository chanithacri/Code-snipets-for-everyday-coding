# decorators

**Language:** Python

## Overview
Common decorators for logging and timing function calls.

Usage example
-------------
>>> from python.decorators import log_calls
>>> @log_calls()
... def greet(name):
...     return f"hi {name}"
>>> greet('Ada')
'hi Ada'

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
See: tests/python/test_decorators.py

_Generated: 2025-11-13T17:21:27.099588Z_
