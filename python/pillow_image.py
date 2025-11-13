"""Helpers for loading and resizing images using Pillow.

Usage example
-------------
>>> from python import pillow_image
>>> pillow_image.resize_image  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

from pathlib import Path

try:  # pragma: no cover - optional dependency
    from PIL import Image
except Exception:  # pragma: no cover
    Image = None  # type: ignore

PathLike = str | Path

__all__ = ["open_image", "resize_image", "save_image"]


def _require_pillow() -> None:
    if Image is None:
        raise RuntimeError("Pillow must be installed to manipulate images")


def open_image(path: PathLike) -> "Image.Image":
    """Open ``path`` returning a Pillow image instance."""

    _require_pillow()
    return Image.open(path)


def resize_image(image: "Image.Image", size: tuple[int, int], *, resample: int | None = None) -> "Image.Image":
    """Return a resized copy of ``image``."""

    _require_pillow()
    resample = resample or Image.LANCZOS
    return image.copy().resize(size, resample=resample)


def save_image(image: "Image.Image", path: PathLike, *, format: str | None = None) -> Path:
    """Persist ``image`` to ``path`` returning the output path."""

    _require_pillow()
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target, format=format)
    return target
