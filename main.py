#!/usr/bin/env python3
"""Invent a Word We Need — entry writer (stdlib only, deterministic).

Writes the single invented-word entry to /output/entry.txt.
"""

import os

ENTRY = (
    "tabnesia (n.) \u2014 the instant amnesia of opening a browser tab "
    "and forgetting why you opened it."
)


def main() -> None:
    entry = ENTRY
    assert 1 <= len(entry) <= 140, f"entry length {len(entry)} out of range 1-140"
    assert entry.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
