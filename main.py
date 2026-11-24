#!/usr/bin/env python3
"""One-line developer excuse entry for the make.fun bounty
"Make the AI Judge Laugh: Developer Excuses".

Writes exactly one line — a funny excuse a developer gives when code
breaks in production — to /output/entry.txt. Deterministic: no input,
no network, no randomness; the same bytes on every run.

Craft notes: the excuse works because of the lonely-machine twist —
"works on my machine" is the oldest developer defence, and the punch
is that the machine is now the ONLY one it works on: the excuse
admits the defence is worthless even as it delivers it. That fits
the judge brief: one funny single-line developer excuse for when
code breaks in production, under 200 characters, clear on first read,
and a different joke mechanism from the previous round's line (which
used one word, "passed", doing double duty for tests and the bug).
"""

import os

EXCUSE = (
    "It works on my machine \u2014 which is now, tragically, "
    "the only machine it will ever work on."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} characters"
    assert "\n" not in EXCUSE and EXCUSE == EXCUSE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
