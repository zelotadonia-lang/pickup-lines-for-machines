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


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Self-check: read the file back and confirm it is exactly what we
    # intended, one line, no trailing newline, within the 200-char gate.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the intended line"
    assert not written.endswith("\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()
