"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text to /output/entry.txt: a review of
planet Earth left by an alien tourist. Python standard library only.
"""

import os

ENTRY = "Five stars. The floor moved by itself and nobody panicked — the locals just stood on it, staring at glowing rectangles. Would ride again."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
