# email_send

**Language:** Python

## Overview
Send emails via SMTP using :class:`email.message.EmailMessage`.

Usage example
-------------
>>> from python import email_send
>>> email_send.send_email(  # doctest: +SKIP
...     subject='Hi', body='Hello world', sender='bot@example.com', recipients=['user@example.com'],
...     smtp={'host': 'smtp.example.com', 'port': 587, 'username': 'bot', 'password': 'secret'},
... )

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
See: tests/python/test_email_send.py

_Generated: 2025-11-13T17:21:27.100952Z_
