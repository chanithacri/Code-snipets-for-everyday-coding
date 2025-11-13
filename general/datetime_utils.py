"""Datetime helpers that respect timezones.

Usage example
-------------
>>> from general.datetime_utils import utc_now, format_datetime, parse_datetime
>>> stamp = format_datetime(utc_now())
>>> parse_datetime(stamp).tzinfo is not None
True
"""

from __future__ import annotations

from datetime import UTC, datetime, timezone

__all__ = ["utc_now", "local_now", "format_datetime", "parse_datetime"]


def utc_now() -> datetime:
    """Return the current UTC datetime with timezone information."""

    return datetime.now(tz=UTC)


def local_now(tz: timezone | None = None) -> datetime:
    """Return the current local datetime.

    ``tz`` defaults to the system timezone when ``None``.
    """

    return datetime.now(tz=tz)


def format_datetime(value: datetime, *, fmt: str = "%Y-%m-%dT%H:%M:%S%z") -> str:
    """Format ``value`` using ``fmt`` and require timezone awareness."""

    if value.tzinfo is None:
        raise ValueError("value must be timezone-aware")
    return value.strftime(fmt)


def parse_datetime(value: str, *, fmt: str = "%Y-%m-%dT%H:%M:%S%z") -> datetime:
    """Parse ``value`` according to ``fmt`` and ensure the result is timezone-aware."""

    dt = datetime.strptime(value, fmt)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt
