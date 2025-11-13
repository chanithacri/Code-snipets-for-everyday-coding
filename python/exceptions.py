"""Custom exception hierarchy for predictable error handling.

Usage example
-------------
>>> from python import exceptions
>>> raise exceptions.ValidationError('invalid input')
Traceback (most recent call last):
...
ValidationError: invalid input
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, TypeVar

__all__ = ["ApplicationError", "NotFoundError", "ValidationError", "wrap_errors"]


@dataclass
class ApplicationError(Exception):
    message: str
    code: str = "error"
    details: dict[str, Any] | None = None

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.message


class NotFoundError(ApplicationError):
    code = "not_found"


class ValidationError(ApplicationError):
    code = "validation_error"


T = TypeVar("T")


def wrap_errors(func: Callable[..., T], *, error_cls: type[ApplicationError] = ApplicationError) -> Callable[..., T]:
    """Wrap ``func`` translating generic exceptions into ``error_cls``."""

    def wrapper(*args: Any, **kwargs: Any) -> T:
        try:
            return func(*args, **kwargs)
        except ApplicationError:
            raise
        except Exception as exc:
            raise error_cls(str(exc)) from exc

    return wrapper
