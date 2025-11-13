"""Read and write syslog style log files in a portable way.

Usage example
-------------
>>> from security_utils import syslog_rw
>>> line = syslog_rw.format_entry(message='started')
>>> syslog_rw.parse_line(line)['message']
'started'
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable

__all__ = ["format_entry", "parse_line", "read_log", "write_log"]

_SYSLOG_FORMAT = "%b %d %H:%M:%S"


def format_entry(*, timestamp: datetime | None = None, host: str = "localhost", app: str = "app", pid: int | None = None, message: str) -> str:
    """Return a syslog formatted line."""

    timestamp = timestamp or datetime.utcnow()
    header = timestamp.strftime(_SYSLOG_FORMAT)
    identity = f"{app}[{pid}]" if pid is not None else app
    return f"{header} {host} {identity}: {message}"


def parse_line(line: str) -> dict[str, str]:
    """Parse a syslog formatted line."""

    parts = line.strip().split(" ", 4)
    if len(parts) < 5:
        raise ValueError("Invalid syslog line")
    month, day, time_part, host, remainder = parts
    identity, message = remainder.split(":", 1)
    return {
        "month": month,
        "day": day,
        "time": time_part,
        "host": host,
        "identity": identity,
        "message": message.strip(),
    }


def read_log(path: str | Path, *, limit: int | None = None) -> list[dict[str, str]]:
    """Return parsed entries from ``path``."""

    entries: list[dict[str, str]] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            entries.append(parse_line(line))
            if limit is not None and len(entries) >= limit:
                break
    return entries


def write_log(path: str | Path, entries: Iterable[str]) -> Path:
    """Append ``entries`` to ``path``."""

    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(entry + "\n")
    return target
