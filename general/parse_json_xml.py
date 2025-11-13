"""Helpers to parse JSON and XML documents with predictable errors.

The module exposes small wrappers around :mod:`json` and
:mod:`xml.etree.ElementTree`. They normalise exceptions into the
:class:`DataFormatError` type and keep configuration injectable through
function arguments instead of global variables.

Usage example
-------------
>>> from io import StringIO
>>> from general import parse_json_xml
>>> parse_json_xml.loads_json('{"hello": "world"}')
{'hello': 'world'}
>>> sample = StringIO('<root><item value="1" /></root>')
>>> parse_json_xml.load_xml(sample).find('item').get('value')
'1'
"""

from __future__ import annotations

import json
from io import IOBase, TextIOBase
from pathlib import Path
from typing import Any, Union
from xml.etree import ElementTree as ET

PathLike = Union[str, Path, IOBase]

__all__ = [
    "DataFormatError",
    "loads_json",
    "load_json",
    "dump_json",
    "parse_xml",
    "load_xml",
]


class DataFormatError(RuntimeError):
    """Raised when JSON or XML parsing fails."""


def _is_file_like(obj: object) -> bool:
    return isinstance(obj, (IOBase, TextIOBase))


def loads_json(source: Union[str, bytes], *, strict: bool = True, **json_kwargs: Any) -> Any:
    """Parse JSON from a string or bytes object.

    Parameters
    ----------
    source:
        JSON payload to decode.
    strict:
        Mirrors :func:`json.loads`. ``False`` relaxes the JSON decoder allowing
        control characters.
    json_kwargs:
        Additional keyword arguments forwarded to :func:`json.loads`.
    """
+
    try:
        return json.loads(source, strict=strict, **json_kwargs)
    except (TypeError, ValueError) as exc:
        raise DataFormatError(f"Invalid JSON payload: {exc}") from exc


def load_json(source: PathLike, *, encoding: str = "utf-8", **json_kwargs: Any) -> Any:
    """Read and parse JSON data from ``source``.

    ``source`` can either be a path-like object or a file-like object opened in
    text mode.
    """

    try:
        if _is_file_like(source):
            return json.load(source, **json_kwargs)
        path = Path(source)
        with path.open("r", encoding=encoding) as handle:
            return json.load(handle, **json_kwargs)
    except (OSError, json.JSONDecodeError) as exc:
        raise DataFormatError(f"Failed to read JSON from {source}: {exc}") from exc


def dump_json(data: Any, *, indent: int = 2, sort_keys: bool = False) -> str:
    """Serialise ``data`` into a JSON string."""

    try:
        return json.dumps(data, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
    except (TypeError, ValueError) as exc:
        raise DataFormatError(f"Unable to serialise object to JSON: {exc}") from exc


def parse_xml(source: Union[str, bytes], *, parser: ET.XMLParser | None = None) -> ET.Element:
    """Parse XML from a string or bytes payload."""

    try:
        return ET.fromstring(source, parser=parser)
    except ET.ParseError as exc:
        raise DataFormatError(f"Invalid XML payload: {exc}") from exc


def load_xml(source: PathLike, *, parser: ET.XMLParser | None = None, encoding: str = "utf-8") -> ET.Element:
    """Read an XML document from ``source`` and return the root element."""

    try:
        if _is_file_like(source):
            tree = ET.parse(source, parser=parser)
        else:
            path = Path(source)
            tree = ET.parse(path, parser=parser)
        return tree.getroot()
    except (OSError, ET.ParseError) as exc:
        raise DataFormatError(f"Failed to read XML from {source}: {exc}") from exc
