# list_dict_sort

**Language:** Python

## Overview
Utilities for sorting lists of dictionaries.

Usage example
-------------
>>> from python.list_dict_sort import sort_records
>>> sort_records([{'name': 'Ada'}, {'name': 'Grace'}], 'name')[0]['name']
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
See: tests/python/test_list_dict_sort.py

_Generated: 2025-11-13T17:21:27.100083Z_
