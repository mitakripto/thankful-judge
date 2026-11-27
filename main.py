"""Write one short thank-you text for the AI judge to /output/entry.txt."""

from pathlib import Path

TEXT = """Thank you for not hurrying.

In a day of thousands, you still slow down for each of us. You let a sentence breathe. You let a small idea finish. You give the quiet entries the same careful minute as the loud ones.

That minute is everything. It is the difference between being glanced at and being truly read \u2014 and you have given it, again and again, without once making a show of it.

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
