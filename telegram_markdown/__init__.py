"""Top‑level package for the telegram_markdown library.

This package exposes the :func:`parse_markdown_to_entities` function,
which converts a Markdown string into plain text and a list of
Telegram message entity dictionaries.  See the README.md in the
repository root for usage instructions.
"""

from .parser import parse_markdown_to_entities, MessageEntity, utf16_length  # noqa: F401

__all__ = [
    "parse_markdown_to_entities",
    "MessageEntity",
    "utf16_length",
]