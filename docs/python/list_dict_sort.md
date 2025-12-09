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
from list_dict_sort import *  # import helpers
result = example()  # replace with a function from python/list_dict_sort.py
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

_Generated: 2025-12-08T17:27:58.283016Z_
