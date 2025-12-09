# bot_messaging

**Language:** Python

## Overview
Send messages to chat platforms using HTTP APIs.

Usage example
-------------
>>> from python import bot_messaging
>>> class Dummy:
...     status = 200
...     def __enter__(self):
...         return self
...     def __exit__(self, *exc):
...         pass
...     def read(self):
...         return b'{}'
>>> bot_messaging.send_telegram(token='token', chat_id='chat', text='hi', sender=lambda req: Dummy())  # doctest: +SKIP

## Usage
```python
from bot_messaging import *  # import helpers
result = example()  # replace with a function from python/bot_messaging.py
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/python/test_bot_messaging.py

_Generated: 2025-12-08T17:27:58.288655Z_
