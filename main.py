#!/usr/bin/env python3
"""One Line, Big Laugh — writes a single funny line to entry.txt.

The program takes no input and needs no network. It writes exactly one
line (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "My houseplant died, so I replaced it with a photo of a houseplant, and honestly the photo is thriving."


def check_line(line: str) -> None:
    """Gate self-check: the entry must be UTF-8 text of 1-200 characters,
    not only white space — the same gate make.fun's sealed scorer applies."""
    encoded = line.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8
    decoded = encoded.decode("utf-8")
    if not 1 <= len(decoded) <= 200:
        raise ValueError(f"line is {len(decoded)} characters, must be 1-200")
    if not decoded.strip():
        raise ValueError("line must not be only white space")


def main() -> None:
    check_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, encoding="utf-8") as f:
        check_line(f.read().rstrip("\n"))


if __name__ == "__main__":
    main()
