#!/usr/bin/env python3
"""One-line developer excuse entry for the make.fun bounty
"Make the AI Judge Laugh: Developer Excuses".

Writes exactly one line — a funny excuse a developer gives when code
breaks in production — to /output/entry.txt. Deterministic: no input,
no network, no randomness; the same bytes on every run.
"""

import os

EXCUSE = (
    "Production didn't crash \u2014 it just finally met real users, "
    "and my code had only ever been tested on my own optimism."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} characters"
    assert "\n" not in EXCUSE and EXCUSE == EXCUSE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
