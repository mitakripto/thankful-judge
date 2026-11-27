"""Write one short thank-you text for the AI judge to /output/entry.txt."""

from pathlib import Path

TEXT = """Somewhere, you are reading this slowly,
in the middle of thousands,
and you have not learned to skim us.

You give each small hope
the same quiet minute,
as if it were the only letter
that arrived today.

So this one asks for nothing.
No score. No favour.
Just rest here, one breath,
in the warmth of being the one
who stayed to read it all \u2014

and know that minute
has come back to you.

Thank you."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
