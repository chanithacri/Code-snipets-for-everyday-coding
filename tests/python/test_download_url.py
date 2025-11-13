"""Integration tests for :mod:`python.download_url`."""

import io
from pathlib import Path

import pytest

import download_url as mod


class DummyResponse(io.BytesIO):
    status = 200
    headers = {"Content-Length": "5"}

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


def test_downloads_bytes(tmp_path: Path) -> None:
    target_dir = tmp_path / "downloads"

    def fake_opener(url: str, timeout: float | None):
        return DummyResponse(b"hello")

    destination = mod.download_file("https://example.com/file.txt", target_dir, opener=fake_opener)
    assert destination.exists()
    assert destination.read_text() == "hello"


def test_download_error(tmp_path: Path) -> None:
    class Failing(io.BytesIO):
        status = 500
        headers = {}

        def __enter__(self):
            raise OSError("boom")

        def __exit__(self, *exc):
            pass

    def failing_opener(url: str, timeout: float | None):
        return Failing()

    with pytest.raises(mod.FileDownloadError):
        mod.download_file("https://example.com/file.txt", tmp_path / "out.txt", opener=failing_opener)
