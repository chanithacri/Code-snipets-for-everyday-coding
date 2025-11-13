"""Public shim for :mod:`python.download_url`."""
from __future__ import annotations

from python import download_url as _impl

__doc__ = _impl.__doc__
FileDownloadError = _impl.FileDownloadError
download_file = _impl.download_file

__all__ = _impl.__all__
