#!/usr/bin/env python3
"""One-line developer excuse entry for the make.fun bounty
"Make the AI Judge Laugh: Developer Excuses".

Writes exactly one line — a funny excuse a developer gives when code
breaks in production — to /output/entry.txt. Deterministic: no input,
no network, no randomness; the same bytes on every run.

Craft notes: the excuse works because of one specific detail — the code
was tested on the developer's own optimism, not on real users — which
turns the worn "works on my machine" family sideways: instead of
blaming the machine, it blames the tester, and the tester is me. That
fits the judge brief: one funny single-line developer excuse for when
code breaks in production, under 200 characters, clear on first read.
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
