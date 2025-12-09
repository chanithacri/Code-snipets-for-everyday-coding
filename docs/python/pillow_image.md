# pillow_image

**Language:** Python

## Overview
Helpers for loading and resizing images using Pillow.

Usage example
-------------
>>> from python import pillow_image
>>> pillow_image.resize_image  # doctest: +ELLIPSIS
<function ...>

## Usage
```python
from pillow_image import *  # import helpers
result = example()  # replace with a function from python/pillow_image.py
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/python/test_pillow_image.py

_Generated: 2025-12-08T17:27:58.287548Z_
