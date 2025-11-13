"""Generate QR codes as PNG files or ASCII art.

Usage example
-------------
>>> from python.qr_code import to_ascii
>>> art = to_ascii('hello')  # doctest: +ELLIPSIS
>>> isinstance(art, str)
True
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

try:  # pragma: no cover - optional dependency
    import qrcode
except Exception:  # pragma: no cover
    qrcode = None

PathLike = str | Path

__all__ = ["create_qr", "save_png", "to_ascii"]


def _require_qrcode() -> None:
    if qrcode is None:
        raise RuntimeError("The 'qrcode' package is required for QR generation")


def create_qr(data: str, *, version: int | None = None, box_size: int = 10, border: int = 4) -> Any:
    """Return a ``qrcode.QRCode`` instance for ``data``."""

    _require_qrcode()
    qr = qrcode.QRCode(version=version, box_size=box_size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    return qr


def save_png(data: str, path: PathLike, **kwargs: Any) -> Path:
    """Create a QR code image saved to ``path``."""

    qr = create_qr(data, **{k: kwargs[k] for k in ("version", "box_size", "border") if k in kwargs})
    image = qr.make_image(fill_color=kwargs.get("fill_color", "black"), back_color=kwargs.get("back_color", "white"))
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target)
    return target


def to_ascii(data: str, *, fill: str = "██", empty: str = "  ") -> str:
    """Return an ASCII representation of the QR code."""

    qr = create_qr(data)
    matrix = qr.get_matrix()
    lines = []
    for row in matrix:
        line = "".join(fill if cell else empty for cell in row)
        lines.append(line)
    return "\n".join(lines)
