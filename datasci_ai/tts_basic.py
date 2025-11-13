"""Convert text to speech using pyttsx3 when available.

Usage example
-------------
>>> from datasci_ai import tts_basic
>>> tts_basic.speak  # doctest: +ELLIPSIS
<function ...>
"""

from __future__ import annotations

try:  # pragma: no cover - optional dependency
    import pyttsx3
except Exception:  # pragma: no cover
    pyttsx3 = None

__all__ = ["speak"]


def speak(text: str, *, voice: str | None = None, rate: int | None = None) -> None:
    """Speak ``text`` using the system TTS engine."""

    if pyttsx3 is None:
        raise RuntimeError("pyttsx3 must be installed for TTS")
    engine = pyttsx3.init()
    if voice is not None:
        engine.setProperty("voice", voice)
    if rate is not None:
        engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()
