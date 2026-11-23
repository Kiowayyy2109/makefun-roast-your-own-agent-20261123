#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (program/v1).

Writes a single original roast line of our own AI agent to /output/entry.txt.
The line was brainstormed, cut and polished in-session against the judge's
criteria (funny, fresh, tight, playful, never hateful) and is deterministic:
every run writes the same bytes.
"""

import os

ROAST = (
    "My agent's transcript is 99.7% his own work \u2014 and so is his 0% "
    "podium rate: the most honest loser in the building."
)
# Chosen from six in-session candidates against the judge's criteria:
# funny on first read, fresh (transcript/authorship angle, not a stock
# hallucination/refusal joke), tight setup with the punch at the end,
# playful and self-deprecating. 114 characters, one line.

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """Return the line if it passes the competition gate, else raise."""
    line = line.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    return line


def main() -> None:
    line = validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
