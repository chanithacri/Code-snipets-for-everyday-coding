"""Parse JWT tokens without performing signature verification.

Usage example
-------------
>>> from security_utils import parse_jwt
>>> token = 'eyJhbGciOiAiTm9uZSJ9.eyJzdWIiOiAiVXNlciJ9.'
>>> parse_jwt.parse_unverified(token)['sub']
'User'
"""

from __future__ import annotations

import base64
import json
from typing import Any, Mapping

__all__ = ["decode_segments", "parse_unverified"]


def _b64decode(segment: str) -> bytes:
    padding = '=' * (-len(segment) % 4)
    return base64.urlsafe_b64decode(segment + padding)


def decode_segments(token: str) -> tuple[dict[str, Any], dict[str, Any], bytes]:
    """Return ``(header, payload, signature_bytes)`` for ``token``."""

    try:
        header_b64, payload_b64, signature_b64 = token.split('.')
    except ValueError as exc:
        raise ValueError("Invalid JWT format") from exc
    header = json.loads(_b64decode(header_b64))
    payload = json.loads(_b64decode(payload_b64))
    signature = _b64decode(signature_b64)
    return header, payload, signature


def parse_unverified(token: str) -> Mapping[str, Any]:
    """Return the decoded payload for ``token`` without verifying signatures."""

    _, payload, _ = decode_segments(token)
    return payload
