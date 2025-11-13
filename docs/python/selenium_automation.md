# selenium_automation

**Language:** Python

## Overview
Utility helpers for Selenium-based automation flows.

Usage example
-------------
>>> from python import selenium_automation
>>> selenium_automation.create_driver(factory=lambda: object())
object()

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
See: tests/python/test_selenium_automation.py

_Generated: 2025-11-13T17:21:27.101272Z_
