# telegram-markdown-entities

## Stop fighting Telegram’s Markdown/HTML parser.

Ship text + entities for zero-escape, zero-surprise, exact rendering—where unsupported bits safely fall back to plain text.

If you’re tired of Telegram MarkdownV2/HTML parse errors:
- “Can’t parse entities” from MarkdownV2 — special characters not escaped (_ * [ ] ( ) ~ > # + - = | { } . !`), or escaping in the wrong context (e.g., inside code).
- Unbalanced delimiters — missing/misplaced *, _, `, ~~, ||, or code fences ….
- Illegal nesting/overlap — e.g., mixing **bold _italic**_ or putting styles inside code/pre.
- Broken links — [label](url) with spaces/parentheses not URL-encoded ( , ), (), or unmatched brackets.
- HTML tag issues — unknown/disallowed tags/attributes, mis-nested tags like <b><i>…</b></i>, unclosed tags.
- Double parsing — sending both parse_mode and manual entities leads to surprises; Telegram’s parser still interferes.
- Edge text — underscores in words/URLs, emoji/ZWJ sequences that shift what the parser thinks are boundaries.

## The new paradigm: entities-only (no parse_mode)

We don’t ask Telegram to parse.
We send text + entities, so **formatting is explicit and deterministic**.

- No escaping ever. Special characters stay as-is; styles are applied by offsets/lengths, not by punctuation.
- UTF-16–correct offsets. Emoji, non-BMP symbols, ZWJ sequences—handled; entity bounds stay valid.
- No illegal overlaps. code/pre are atomic; we prevent forbidden nests before sending.
- Graceful fallback. Anything we don’t support is left as plain text—safe, readable, no runtime errors.
- Future-proof. Parser changes on Telegram’s side don’t break you; your rendering remains stable.


## Convert Markdown(or any) text into plain(valid) telegram messages and with ease.

This library takes a string written in standard Markdown (such as the
output of a language model or contents of a README) and returns two
objects:

1. **Plain text** with all Markdown delimiters removed.
2. A list of **message entity dictionaries** that tell the Telegram
   Bot API how to format the text (bold, italic, links, lists,
   block quotes, etc.).

By sending the text together with the `entities` array (and *not*
specifying a `parse_mode`) you avoid the pitfalls of Telegram’s own
Markdown parser – there’s no need to escape special characters, and
your messages render exactly as intended.

Send the text with an entities array and without parse_mode to bypass Telegram’s Markdown quirks—no escaping needed, and the message renders exactly as you designed.

Pair your text with entities (skip parse_mode) to sidestep Telegram’s Markdown parser: no special-char escaping, just precise, predictable rendering.

Use entities instead of parse_mode to avoid Telegram’s Markdown pitfalls—no escape gymnastics, and the output matches your intent.

Deliver text plus entities (no parse_mode) and you’ll dodge parser surprises: zero escaping and faithful, deterministic formatting.

By sending entities alongside the text and omitting parse_mode, you eliminate Markdown parsing issues—nothing to escape, and the result is pixel-perfect.

Ship the message with entities only; don’t set parse_mode. You’ll skip Telegram’s parser entirely, so special characters are safe and formatting is exact.

## Features

* **Inline formatting**: supports bold (`**text**`), italic (`*text*` or
  `_text_`), underline (`__text__`), strikethrough (`~~text~~`),
  spoilers (`||text||`), inline code (`` `code` ``), code blocks
  (```lang\ncode```), and links (`[label](url)`).
* **Headings**: lines starting with `#` are converted to bold text.
* **Block quotes**: lines beginning with `>` produce a `blockquote`
  entity; prefixing the quote with `||` (e.g. `>|| quote`) marks it
  as **collapsed/expandable**.  This maps to the `collapsed` flag on
  Telegram’s `messageEntityBlockquote` type【885819747867534†L114-L123】.
* **Lists**: unordered lists use Unicode bullets – `•`, `◦` and `▪`
  depending on nesting depth – and indent with non‑breaking spaces; ordered
  lists align numbers using figure spaces and support nested numbering.
* **Nested formatting**: bold inside italics, links inside quotes and
  other combinations all work as expected.
* **UTF‑16 offsets**: entity offsets and lengths are calculated
  according to the UTF‑16 code unit rules used by Telegram【16645222028428†L69-L79】.

## Installation

Install the package from PyPI:

```bash
pip install telegram-markdown-entities
```

Requires Python 3.7 or newer.  **There are no external dependencies.**

## Usage

Here’s a minimal example of how to use the library with the Bot API:

```python
from telegram_markdown import parse_markdown_to_entities
import requests

md = """
# Heading Example

>|| This is a collapsed quote\n> It continues here.

* Item 1
    * Nested item
1. First
2. Second\n   continuation

Inline example: **bold**, _italic_, [link](https://example.com) and `code`.
"""

text, entities = parse_markdown_to_entities(md)

# Send via HTTP API (replace TOKEN and CHAT_ID with your own)
payload = {
    'chat_id': CHAT_ID,
    'text': text,
    'entities': entities
}
requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', json=payload)
```

The `text` variable will contain the plain message (with list markers
and quote markers removed), and `entities` will be a list of
dictionaries like `{'type': 'bold', 'offset': 0, 'length': 6}`.  Pass
these directly to `sendMessage`.  There is no need to set the
`parse_mode` parameter.

## Packaging and publishing

This project uses a modern `pyproject.toml` with [`setuptools`](https://setuptools.pypa.io).
To build a source distribution and wheel, install the build tool and
run:

```bash
pip install build
python -m build
```

Distributions will be created in the `dist/` directory.  To upload
them to the Python Package Index (PyPI), install `twine` and run:

```bash
pip install twine
twine upload dist/*
```

You will be prompted for your PyPI username and password.  See
<https://packaging.python.org/tutorials/packaging-projects/> for
full details.

## License

MIT – see the [LICENSE](LICENSE) file for details.


# Links

[Telegram message entities](https://core.telegram.org/api/entities)
