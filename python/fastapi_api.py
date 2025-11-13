"""Create a tiny FastAPI application for quick integration tests.

Usage example
-------------
>>> from python import fastapi_api
>>> fastapi_api.create_app({'title': 'demo'})  # doctest: +SKIP
<fastapi.applications.FastAPI object ...>
"""

from __future__ import annotations

from typing import Any, Mapping

try:  # pragma: no cover - optional dependency
    from fastapi import FastAPI
except Exception:  # pragma: no cover
    FastAPI = None  # type: ignore

__all__ = ["create_app"]


def create_app(config: Mapping[str, Any] | None = None) -> "FastAPI":
    """Return a configured :class:`~fastapi.FastAPI` instance."""

    if FastAPI is None:
        raise RuntimeError("FastAPI must be installed to create the API")
    app = FastAPI(title=(config or {}).get("title", "Code Snippets API"))

    @app.get("/healthz")
    async def healthz() -> dict[str, Any]:  # pragma: no cover - simple JSON response
        return {"status": "ok", "service": app.title}

    return app
