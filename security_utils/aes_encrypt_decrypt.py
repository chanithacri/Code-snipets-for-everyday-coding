"""Encrypt and decrypt strings using Fernet (AES-128 in CBC mode).

Usage example
-------------
>>> from security_utils import aes_encrypt_decrypt as aes
>>> key = aes.generate_key()  # doctest: +SKIP
>>> aes.decrypt(aes.encrypt('secret', key), key)  # doctest: +SKIP
'secret'
"""

from __future__ import annotations

from typing import Any

try:  # pragma: no cover - optional dependency
    from cryptography.fernet import Fernet
except Exception:  # pragma: no cover
    Fernet = None

__all__ = ["generate_key", "encrypt", "decrypt"]


def _require_fernet() -> None:
    if Fernet is None:
        raise RuntimeError("cryptography must be installed to use AES helpers")


def generate_key() -> bytes:
    """Return a random key suitable for :func:`encrypt`."""

    _require_fernet()
    return Fernet.generate_key()


def encrypt(plaintext: str, key: bytes) -> bytes:
    """Return the encrypted bytes for ``plaintext``."""

    _require_fernet()
    token = Fernet(key)
    return token.encrypt(plaintext.encode("utf-8"))


def decrypt(ciphertext: bytes, key: bytes) -> str:
    """Return the decrypted string for ``ciphertext``."""

    _require_fernet()
    token = Fernet(key)
    return token.decrypt(ciphertext).decode("utf-8")
