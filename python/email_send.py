"""Send emails via SMTP using :class:`email.message.EmailMessage`.

Usage example
-------------
>>> from python import email_send
>>> email_send.send_email(  # doctest: +SKIP
...     subject='Hi', body='Hello world', sender='bot@example.com', recipients=['user@example.com'],
...     smtp={'host': 'smtp.example.com', 'port': 587, 'username': 'bot', 'password': 'secret'},
... )
"""

from __future__ import annotations

import smtplib
from email.message import EmailMessage
from typing import Iterable, Mapping

__all__ = ["SMTPSettings", "send_email"]


class SMTPSettings(dict):
    """Simple mapping holding SMTP configuration values."""

    @property
    def host(self) -> str:
        return self.get("host", "localhost")

    @property
    def port(self) -> int:
        return int(self.get("port", 587))

    @property
    def username(self) -> str | None:
        return self.get("username")

    @property
    def password(self) -> str | None:
        return self.get("password")

    @property
    def use_tls(self) -> bool:
        return bool(self.get("use_tls", True))


def send_email(
    *,
    subject: str,
    body: str,
    sender: str,
    recipients: Iterable[str],
    smtp: Mapping[str, object] | SMTPSettings | None = None,
    headers: Mapping[str, str] | None = None,
    connection_factory=smtplib.SMTP,
) -> None:
    """Send an email using the provided SMTP configuration."""

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = ", ".join(recipients)
    if headers:
        for key, value in headers.items():
            message[key] = value
    message.set_content(body)

    settings = SMTPSettings(smtp or {})

    with connection_factory(settings.host, settings.port) as client:
        if settings.use_tls:
            client.starttls()
        username = settings.username
        password = settings.password
        if username and password:
            client.login(username, password)
        client.send_message(message)
