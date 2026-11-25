#!/usr/bin/env python3
"""Invent a Word We Need — entry writer (stdlib only, deterministic).

Coinage: "tabnesia" — a blend of "tab" + "amnesia" for the instant
forgetting of why a browser tab was opened. No existing single word
names that everyday lapse, so the coinage fills a real lexical gap
instead of re-labelling something English already says in one word.

Writes the single invented-word entry to /output/entry.txt.
"""

import os

ENTRY = (
    "tabnesia (n.) \u2014 the instant amnesia of opening a browser tab "
    "and forgetting why you opened it."
)


def validate_entry(entry: str) -> str:
    # Contest gate: the entry must be 1-140 characters and non-blank.
    # Validated once here so main() only ever writes a legal entry.
    assert 1 <= len(entry) <= 140, f"entry length {len(entry)} out of range 1-140"
    assert entry.strip(), "entry must not be only whitespace"
    return entry


def main() -> None:
    entry = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
