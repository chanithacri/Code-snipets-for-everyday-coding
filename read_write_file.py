"""Public shim for :mod:`python.read_write_file`.

The tests import the module from the repository root, while the actual
implementation lives under :mod:`python.read_write_file`. This shim keeps the
import stable without duplicating logic.
"""
from __future__ import annotations

from python import read_write_file as _impl

__doc__ = _impl.__doc__
FileOperationError = _impl.FileOperationError
read_text = _impl.read_text
write_text = _impl.write_text
read_bytes = _impl.read_bytes
write_bytes = _impl.write_bytes

__all__ = _impl.__all__
