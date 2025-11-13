"""Integration tests for :mod:`python.read_write_file`."""

from pathlib import Path

import pytest

import read_write_file as mod


def test_roundtrip_text(tmp_path: Path) -> None:
    target = tmp_path / "example.txt"
    mod.write_text(target, "hello")
    assert target.exists()
    assert mod.read_text(target) == "hello"


def test_roundtrip_bytes(tmp_path: Path) -> None:
    target = tmp_path / "payload.bin"
    mod.write_bytes(target, b"abc")
    assert mod.read_bytes(target) == b"abc"


def test_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(mod.FileOperationError):
        mod.read_text(tmp_path / "missing.txt")
