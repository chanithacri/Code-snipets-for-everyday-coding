# async_tasks

**Language:** Python

## Overview
Asyncio helpers for running tasks with concurrency limits.

Usage example
-------------
>>> from python import async_tasks
>>> async def square(x):
...     return x * x
>>> async_tasks.run(async_tasks.gather_limited([square(2), square(3)], limit=1))
[4, 9]

## Usage
```python
from async_tasks import *  # import helpers
result = example()  # replace with a function from python/async_tasks.py
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/python/test_async_tasks.py

_Generated: 2025-12-08T17:27:58.292373Z_
