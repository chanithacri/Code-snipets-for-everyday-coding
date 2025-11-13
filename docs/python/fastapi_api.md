# fastapi_api

**Language:** Python

## Overview
Create a tiny FastAPI application for quick integration tests.

Usage example
-------------
>>> from python import fastapi_api
>>> fastapi_api.create_app({'title': 'demo'})  # doctest: +SKIP
<fastapi.applications.FastAPI object ...>

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
See: tests/python/test_fastapi_api.py

_Generated: 2025-11-13T17:21:27.099924Z_
