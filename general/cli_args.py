"""Thin wrapper around :mod:`argparse` for declarative CLI parsing.

The helpers keep configuration entirely argument driven which makes it trivial
for callers to inject alternative ``argv`` sequences or use a different parser
class during testing.

Usage example
-------------
>>> from general.cli_args import Argument, parse_arguments
>>> spec = [
...     Argument("--name", help="Name to greet", required=True),
...     Argument("--times", type=int, default=1),
... ]
>>> args = parse_arguments(spec, argv=["--name", "Ada", "--times", "2"])
>>> (args.name, args.times)
('Ada', 2)
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Iterable, Sequence

__all__ = ["Argument", "build_parser", "parse_arguments"]


@dataclass(frozen=True)
class Argument:
    """Declarative argument specification.

    Parameters mirror :meth:`argparse.ArgumentParser.add_argument` which keeps
    the wrapper lightweight. ``flag`` can be a positional name (``"filename"``)
    or a flag (``"--verbose"``).
    """

    flag: str
    *aliases: str
    help: str | None = None
    action: str | None = None
    default: object | None = None
    required: bool | None = None
    type: type | None = None
    choices: Sequence[object] | None = None
    metavar: str | None = None

    def register(self, parser: argparse.ArgumentParser) -> None:
        flags = (self.flag, *self.aliases)
        kwargs: dict[str, object] = {}
        for field in ("help", "action", "default", "required", "type", "choices", "metavar"):
            value = getattr(self, field)
            if value is not None:
                kwargs[field] = value
        parser.add_argument(*flags, **kwargs)


def build_parser(
    arguments: Iterable[Argument],
    *,
    description: str | None = None,
    prog: str | None = None,
    parser_class: type[argparse.ArgumentParser] = argparse.ArgumentParser,
) -> argparse.ArgumentParser:
    """Return an :class:`ArgumentParser` with ``arguments`` registered."""

    parser = parser_class(description=description, prog=prog)
    for argument in arguments:
        argument.register(parser)
    return parser


def parse_arguments(
    arguments: Iterable[Argument],
    *,
    argv: Sequence[str] | None = None,
    description: str | None = None,
    prog: str | None = None,
    parser_class: type[argparse.ArgumentParser] = argparse.ArgumentParser,
) -> argparse.Namespace:
    """Parse command line arguments defined by ``arguments``.

    The ``argv`` parameter defaults to :data:`sys.argv[1:]` which means callers
    can easily inject their own argument sequences while testing.
    """

    parser = build_parser(arguments, description=description, prog=prog, parser_class=parser_class)
    return parser.parse_args(list(argv) if argv is not None else None)
