# telegram-markdown-entities

Convert Markdown text into plain messages and [Telegram message entities](https://core.telegram.org/api/entities) with ease.

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

Requires Python 3.7 or newer.  There are no external dependencies.

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