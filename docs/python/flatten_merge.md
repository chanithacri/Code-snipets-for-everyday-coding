# flatten_merge

**Language:** Python

## Overview
Flatten nested iterables and merge dictionaries.

Usage example
-------------
>>> from python.flatten_merge import flatten, merge_dicts
>>> flatten([1, [2, 3]])
[1, 2, 3]
>>> merge_dicts({'a': 1}, {'a': 2}, strategy='first')['a']
1

## Usage
```python
from flatten_merge import *  # import helpers
result = example()  # replace with a function from python/flatten_merge.py
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/python/test_flatten_merge.py

_Generated: 2025-12-08T17:27:58.296316Z_
