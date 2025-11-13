"""Basic web scraping helpers with optional BeautifulSoup integration.

Usage example
-------------
>>> from python import web_scrape
>>> html = "<html><body><a href='https://example.com'>Example</a></body></html>"
>>> web_scrape.extract_links(html)
['https://example.com']
"""

from __future__ import annotations

from html.parser import HTMLParser
from typing import Callable
from urllib.request import urlopen

try:  # pragma: no cover - optional dependency
    import bs4
except Exception:  # pragma: no cover
    bs4 = None

Fetcher = Callable[[str], str]

__all__ = ["fetch_html", "extract_links", "scrape_text"]


def fetch_html(url: str, *, opener: Callable[[str], str] | None = None) -> str:
    """Return the HTML body for ``url``."""

    if opener:
        return opener(url)
    with urlopen(url) as response:
        return response.read().decode("utf-8", errors="replace")


def extract_links(html: str) -> list[str]:
    """Return all anchor href attributes found in ``html``."""

    if bs4 is not None:
        soup = bs4.BeautifulSoup(html, "html.parser")
        return [a.get("href", "") for a in soup.find_all("a") if a.get("href")]

    class _LinkParser(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.links: list[str] = []

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag == "a":
                for attr, value in attrs:
                    if attr == "href" and value:
                        self.links.append(value)

    parser = _LinkParser()
    parser.feed(html)
    return parser.links


def scrape_text(html: str) -> str:
    """Return visible text content from ``html``."""

    if bs4 is not None:
        soup = bs4.BeautifulSoup(html, "html.parser")
        return " ".join(soup.stripped_strings)
    parser = HTMLParser()
    parts: list[str] = []

    class _TextParser(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.chunks: list[str] = []

        def handle_data(self, data: str) -> None:
            text = data.strip()
            if text:
                self.chunks.append(text)

    parser = _TextParser()
    parser.feed(html)
    return " ".join(parser.chunks)
