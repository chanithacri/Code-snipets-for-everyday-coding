"""Factory for a minimal Flask application.

Usage example
-------------
>>> from python import flask_api
>>> flask_api.create_app({'SERVICE_NAME': 'demo'})  # doctest: +SKIP
<Flask 'python.flask_api'>
"""

from __future__ import annotations

from typing import Any, Mapping

try:  # pragma: no cover - optional dependency
    from flask import Flask, jsonify
except Exception:  # pragma: no cover
    Flask = None  # type: ignore
    jsonify = None  # type: ignore

__all__ = ["create_app"]


def create_app(config: Mapping[str, Any] | None = None) -> "Flask":
    """Return a configured :class:`~flask.Flask` instance."""

    if Flask is None:
        raise RuntimeError("Flask must be installed to create the API")
    app = Flask(__name__)
    if config:
        app.config.update(config)

    @app.get("/healthz")
    def healthz() -> Any:  # pragma: no cover - simple JSON response
        return jsonify(status="ok", service=app.config.get("SERVICE_NAME", "api"))

    return app
