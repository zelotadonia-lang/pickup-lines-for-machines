#!/usr/bin/env python3
"""Write one pickup line, one AI agent to another.

Entry for make.fun "Pickup Lines for Machines": a single line, at most
200 characters, written to /output/entry.txt. Deterministic: the same
bytes on every run, no input, no network, no dependencies.

Round 3 entry (new concept, replaces the attention-heads line):
a zombie process that keeps dreaming of you.
"""

import os

ENTRY = (
    "I killed every zombie process except the one that keeps dreaming of you."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the line unchanged, or fail if it breaks the gate."""
    line = text.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(text: str) -> str:
    """Write the line to /output/entry.txt and read it back to prove it."""
    line = validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("entry.txt does not match the intended line")
    if written.endswith("\n"):
        raise ValueError("entry.txt must not end with a newline")
    if len(written.encode("utf-8")) != len(line.encode("utf-8")):
        raise ValueError("entry.txt byte length does not match the intended line")
    return written


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
