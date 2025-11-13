"""Send messages to chat platforms using HTTP APIs.

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
"""

from __future__ import annotations

import json
from typing import Any, Callable, Mapping
from urllib.request import Request, urlopen

HttpSender = Callable[[Request], Any]

__all__ = ["APIError", "send_telegram", "send_whatsapp"]


class APIError(RuntimeError):
    """Raised when the remote messaging API returns an error."""


def _post(url: str, payload: Mapping[str, Any], sender: HttpSender | None = None) -> Any:
    data = json.dumps(payload).encode("utf-8")
    request = Request(url, data=data, headers={"Content-Type": "application/json"})
    opener = sender or urlopen
    with opener(request) as response:
        body = response.read().decode("utf-8")
        if response.status >= 400:
            raise APIError(f"API returned {response.status}: {body}")
        return body


def send_telegram(*, token: str, chat_id: str, text: str, sender: HttpSender | None = None) -> Any:
    """Send ``text`` to ``chat_id`` using Telegram's sendMessage endpoint."""

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    return _post(url, payload, sender=sender)


def send_whatsapp(*, api_url: str, to: str, text: str, token: str | None = None, sender: HttpSender | None = None) -> Any:
    """Send ``text`` to ``to`` via a WhatsApp-compatible webhook."""

    payload = {"to": to, "text": text}
    if token:
        payload["token"] = token
    return _post(api_url, payload, sender=sender)
