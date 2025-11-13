"""Create simple PDF documents with ReportLab.

Usage example
-------------
>>> from python import pdf_create
>>> pdf_create.create_pdf('example.pdf', ['Hello'])  # doctest: +SKIP
PosixPath('example.pdf')
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

try:  # pragma: no cover - optional dependency
    from reportlab.pdfgen import canvas
except Exception:  # pragma: no cover
    canvas = None

PathLike = str | Path

__all__ = ["create_pdf"]


def create_pdf(path: PathLike, lines: Iterable[str], *, title: str = "Document") -> Path:
    """Write ``lines`` to a PDF at ``path``."""

    if canvas is None:
        raise RuntimeError("reportlab must be installed to create PDFs")
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(target))
    pdf.setTitle(title)
    width, height = pdf._pagesize
    y = height - 72
    for line in lines:
        pdf.drawString(72, y, line)
        y -= 14
        if y < 72:
            pdf.showPage()
            y = height - 72
    pdf.save()
    return target
