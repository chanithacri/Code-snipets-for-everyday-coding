"""Input validation helpers using regular expressions.

Usage example
-------------
>>> from security_utils.validate_inputs import is_valid_email
>>> is_valid_email('user@example.com')
True
"""

from __future__ import annotations

import re

__all__ = ["is_valid_email", "is_valid_url", "require"]

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_URL_RE = re.compile(r"^https?://[\w.-]+(:\d+)?(/.*)?$")


def is_valid_email(value: str) -> bool:
    """Return ``True`` when ``value`` looks like an email address."""

    return bool(_EMAIL_RE.match(value))


def is_valid_url(value: str) -> bool:
    """Return ``True`` when ``value`` looks like an HTTP URL."""

    return bool(_URL_RE.match(value))


def require(condition: bool, message: str) -> None:
    """Raise :class:`ValueError` when ``condition`` is false."""

    if not condition:
        raise ValueError(message)
