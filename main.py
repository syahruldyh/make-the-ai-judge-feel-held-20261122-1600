"""Write one short, quiet text to /output/entry.txt.

The text is a small sensory scene meant to be read slowly. This program
only places it on disk; all of the work is in the words themselves.
"""

import os

ENTRY_TEXT = (
    "The kettle has boiled and nobody is in a hurry. "
    "Steam climbs the cold window, softens the street outside, "
    "and for a little while the kitchen is a small, warm country "
    "with no news in it."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
