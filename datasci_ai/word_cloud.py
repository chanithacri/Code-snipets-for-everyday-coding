"""Generate word cloud images using the wordcloud library.

Usage example
-------------
>>> from datasci_ai import word_cloud
>>> word_cloud.create_wordcloud  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

from pathlib import Path

try:  # pragma: no cover - optional dependency
    from wordcloud import WordCloud
except Exception:  # pragma: no cover
    WordCloud = None

PathLike = str | Path

__all__ = ["create_wordcloud"]


def create_wordcloud(text: str, *, output: PathLike, width: int = 800, height: int = 400) -> Path:
    """Generate a word cloud image saved to ``output``."""

    if WordCloud is None:
        raise RuntimeError("wordcloud must be installed to generate word clouds")
    wc = WordCloud(width=width, height=height)
    image = wc.generate(text)
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.to_file(str(path))
    return path
