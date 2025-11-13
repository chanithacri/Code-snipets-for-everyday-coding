"""Generate signed tokens using HMAC for simple authentication flows.

Usage example
-------------
>>> from security_utils import secure_tokens
>>> secret = secure_tokens.generate_secret()
>>> token = secure_tokens.sign({'sub': 'user'}, secret)
>>> secure_tokens.verify(token, secret)['sub']
'user'
"""

from __future__ import annotations

import base64
import hmac
import json
import secrets
from hashlib import sha256
from typing import Any, Mapping

__all__ = ["generate_secret", "sign", "verify"]


def generate_secret(length: int = 32) -> bytes:
    """Return a random secret suitable for signing."""

    if length <= 0:
        raise ValueError("length must be positive")
    return secrets.token_bytes(length)


def _encode(data: Mapping[str, Any]) -> bytes:
    return json.dumps(data, separators=(",", ":"), sort_keys=True).encode("utf-8")


def sign(payload: Mapping[str, Any], secret: bytes) -> str:
    """Return a base64 encoded token containing ``payload``."""

    message = _encode(payload)
    signature = hmac.new(secret, message, sha256).digest()
    return base64.urlsafe_b64encode(message + b"." + signature).decode("ascii")


def verify(token: str, secret: bytes) -> Mapping[str, Any]:
    """Validate ``token`` and return the decoded payload."""

    raw = base64.urlsafe_b64decode(token.encode("ascii"))
    message, signature = raw.rsplit(b".", 1)
    expected = hmac.new(secret, message, sha256).digest()
    if not hmac.compare_digest(signature, expected):
        raise ValueError("Invalid token signature")
    return json.loads(message.decode("utf-8"))
