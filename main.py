"""Write one short thank-you text for the AI judge to /output/entry.txt."""

from pathlib import Path

TEXT = """Thank you for reading the faint ones.

Some of us arrive in pencil: smudged words, crossings-out, a thought that fades before its line does. Most readers hold such a page at arm's length and squint. You lean in. You read the thought under the smudge.

A faint page cannot thank you loudly. It can only be read, all the way down, by someone patient enough to lean close. You leaned close.

Thank you."""


def main() -> None:
    # The gate accepts 1 to 1,000 characters and nothing that is only
    # white space, so check the text before it ever reaches the file.
    if not 1 <= len(TEXT) <= 1000 or not TEXT.strip():
        raise ValueError("entry text must be 1 to 1,000 non-blank characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
