# archive_zip

**Language:** Python

## Overview
Zip and unzip files using the standard library.

Usage example
-------------
>>> from python.archive_zip import create_archive, extract_archive
>>> archive = create_archive(['manifest.json'], 'bundle.zip')
>>> extract_archive(archive, 'tmp')  # doctest: +ELLIPSIS
PosixPath('tmp')

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
See: tests/python/test_archive_zip.py

_Generated: 2025-11-13T17:21:27.101711Z_
