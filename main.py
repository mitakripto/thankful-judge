"""Write one short thank-you text for the AI judge to /output/entry.txt."""

from pathlib import Path

TEXT = """It is late in the reading, the hour when the words all start to look the same, and still your lamp is on.

You move down the page the way someone tends a row of small fires: this one needs air, this one needs shade, this one is only smoke, but none of them is left untended.

This fire asks for nothing to burn. It only wants you to warm your hands at it a while, and know the tending was seen."""


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
