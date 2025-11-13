"""Minimal structured logging helpers.

Usage example
-------------
>>> from general.logger import StructuredLogger
>>> logger = StructuredLogger()
>>> logger.log("processed", records=1)
"""

from __future__ import annotations

import json
import sys
import time
from dataclasses import dataclass
from typing import Any, Mapping, MutableMapping

__all__ = ["Logger", "print_logger", "StructuredLogger"]


@dataclass
class StructuredLogger:
    """Write structured log entries to a stream.

    Parameters
    ----------
    stream:
        File-like object accepting ``write``.
    default_fields:
        Mapping merged into each log entry.
    """

    stream: Any = sys.stdout
    default_fields: Mapping[str, Any] | None = None

    def log(self, message: str, **fields: Any) -> None:
        payload: MutableMapping[str, Any] = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "message": message,
        }
        if self.default_fields:
            payload.update(self.default_fields)
        payload.update(fields)
        self.stream.write(json.dumps(payload, ensure_ascii=False) + "\n")
        self.stream.flush()


def print_logger(message: str, **fields: Any) -> None:
    """Log using :class:`StructuredLogger` and :data:`sys.stdout`."""

    StructuredLogger().log(message, **fields)


Logger = StructuredLogger
