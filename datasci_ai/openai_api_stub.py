"""Stub helpers for calling an OpenAI compatible API.

Usage example
-------------
>>> from datasci_ai import openai_api_stub
>>> openai_api_stub.create_request('hello')
{'model': 'gpt-3.5-turbo', 'messages': [{'role': 'user', 'content': 'hello'}], 'temperature': 0.7}
"""

from __future__ import annotations

import json
from typing import Any, Callable, Mapping
from urllib.request import Request, urlopen

HttpSender = Callable[[Request], Any]

__all__ = ["create_request", "call_completion"]


def create_request(prompt: str, *, model: str = "gpt-3.5-turbo", temperature: float = 0.7) -> Mapping[str, Any]:
    """Return the JSON payload for chat completion requests."""

    return {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
    }


def call_completion(
    prompt: str,
    *,
    api_key: str,
    endpoint: str = "https://api.openai.com/v1/chat/completions",
    sender: HttpSender | None = None,
    model: str = "gpt-3.5-turbo",
    temperature: float = 0.7,
) -> Mapping[str, Any]:
    """Call the completion endpoint returning the parsed JSON body."""

    payload = create_request(prompt, model=model, temperature=temperature)
    data = json.dumps(payload).encode("utf-8")
    request = Request(
        endpoint,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    opener = sender or urlopen
    with opener(request) as response:
        body = response.read().decode("utf-8")
        return json.loads(body)
