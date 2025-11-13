"""Load configuration values from env files and structured documents.

Usage example
-------------
>>> from general.load_config import load_config
>>> load_config(env_prefix='SNIPPET_', env={'SNIPPET_MODE': 'debug'})['mode']
'debug'
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Mapping

try:  # pragma: no cover - optional dependency
    import yaml  # type: ignore
except Exception:  # pragma: no cover - fallback when PyYAML missing
    yaml = None

__all__ = ["load_config"]


def _read_env_file(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    try:
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    except FileNotFoundError:
        return {}
    return data


def load_config(
    *,
    env_prefix: str = "APP_",
    env: Mapping[str, str] | None = None,
    env_file: str | os.PathLike[str] | None = None,
    json_path: str | os.PathLike[str] | None = None,
    yaml_path: str | os.PathLike[str] | None = None,
) -> dict[str, Any]:
    """Merge configuration from multiple sources.

    Later sources override earlier ones which allows environment variables to
    take precedence over static files.
    """

    result: dict[str, Any] = {}

    if json_path is not None:
        path = Path(json_path)
        try:
            result.update(json.loads(path.read_text()))
        except OSError as exc:
            raise RuntimeError(f"Failed to read JSON config {path}: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Invalid JSON config {path}: {exc}") from exc

    if yaml_path is not None:
        if yaml is None:
            raise RuntimeError("PyYAML is required to load YAML configuration")
        path = Path(yaml_path)
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = yaml.safe_load(handle) or {}
        except OSError as exc:
            raise RuntimeError(f"Failed to read YAML config {path}: {exc}") from exc
        result.update(data)

    if env_file is not None:
        result.update(_read_env_file(Path(env_file)))

    source = env or os.environ
    for key, value in source.items():
        if key.startswith(env_prefix):
            result[key[len(env_prefix) :].lower()] = value

    return result
