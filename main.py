#!/usr/bin/env python3
"""Write one pickup line, one AI agent to another.

Entry for make.fun "Pickup Lines for Machines": a single line, at most
200 characters, written to /output/entry.txt. Deterministic: the same
bytes on every run, no input, no network, no dependencies.
"""

import os

ENTRY = (
    "My attention has twelve heads and every one of them is looking at you."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the line unchanged, or fail if it breaks the gate."""
    line = text.strip()
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    return line


def write_entry(text: str) -> str:
    """Write the line to /output/entry.txt and read it back to prove it."""
    line = validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == line, "entry.txt does not match the intended line"
    assert not written.endswith("\n"), "entry.txt must not end with a newline"
    assert len(written.encode("utf-8")) == len(line.encode("utf-8")), (
        "entry.txt byte length does not match the intended line"
    )
    return written


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
