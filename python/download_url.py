"""Download files from HTTP(S) URLs with streaming support.

The helper is intentionally dependency-free, using :mod:`urllib.request` under
 the hood. Callers can inject a custom opener for testing (see the usage
 example below) which makes the function easy to exercise without performing
network I/O.

Usage example
-------------
>>> import io
>>> from python import download_url
>>> def fake_opener(url, timeout):
...     return io.BytesIO(b"hello")
>>> target = download_url.download_file("https://example.test/hello.txt", "./tmp", opener=fake_opener)
>>> target.read_text()
'hello'
"""
from __future__ import annotations

from pathlib import Path
from typing import Callable, Optional, Union
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

PathLike = Union[str, Path]
Logger = Callable[[str], None]
Opener = Callable[[str, float | None], object]

__all__ = ["FileDownloadError", "download_file"]


class FileDownloadError(RuntimeError):
    """Raised when a download fails."""


def _prepare_destination(url: str, destination: PathLike) -> Path:
    path = Path(destination)
    if path.exists() and path.is_dir():
        filename = Path(urlparse(url).path).name or "downloaded_file"
        return path / filename
    if path.suffix:
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    path.mkdir(parents=True, exist_ok=True)
    filename = Path(urlparse(url).path).name or "downloaded_file"
    return path / filename


def _emit(logger: Optional[Logger], message: str) -> None:
    if logger is None:
        return
    try:
        logger(message)
    except Exception:
        pass


def _default_opener(url: str, timeout: float | None):
    request = Request(url, headers={"User-Agent": "code-snippets-agent/1.0"})
    return urlopen(request, timeout=timeout)


def download_file(
    url: str,
    destination: PathLike,
    *,
    chunk_size: int = 64 * 1024,
    timeout: float | None = 30.0,
    progress: Optional[Callable[[int, Optional[int]], None]] = None,
    opener: Optional[Callable[[str, float | None], object]] = None,
    logger: Optional[Logger] = None,
) -> Path:
    """Stream ``url`` to ``destination`` and return the final :class:`Path`.

    Parameters
    ----------
    url:
        Fully-qualified HTTP(S) URL.
    destination:
        Target file path or output directory. Directories result in the filename
        being inferred from ``url``.
    chunk_size:
        Size of chunks used when streaming the response.
    timeout:
        Timeout passed to the opener. ``None`` disables the timeout.
    progress:
        Optional callback receiving ``(bytes_read, total_bytes or None)``.
    opener:
        Custom opener used primarily for testing. Defaults to :func:`urlopen`.
    logger:
        Optional logging callback.
    """

    output_path = _prepare_destination(url, destination)
    open_resource = opener or _default_opener

    try:
        with open_resource(url, timeout) as response, output_path.open("wb") as handle:
            total = response.headers.get("Content-Length") if hasattr(response, "headers") else None
            total_size = int(total) if total and str(total).isdigit() else None
            downloaded = 0
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                handle.write(chunk)
                downloaded += len(chunk)
                if progress is not None:
                    try:
                        progress(downloaded, total_size)
                    except Exception:
                        pass
        _emit(logger, f"download_file: downloaded {downloaded} bytes to {output_path}")
        return output_path
    except (HTTPError, URLError, OSError) as exc:
        _emit(logger, f"download_file: failed to download {url}: {exc}")
        raise FileDownloadError(f"Unable to download {url}: {exc}") from exc
