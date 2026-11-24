#!/usr/bin/env python3
"""One-line developer excuse entry for the make.fun bounty
"Make the AI Judge Laugh: Developer Excuses".

Writes exactly one line — a funny excuse a developer gives when code
breaks in production — to /output/entry.txt. Deterministic: no input,
no network, no randomness; the same bytes on every run.

Craft notes: the excuse works because of the demo-vs-production
twist — the demo "worked flawlessly", but only because it had no
users and no witnesses, so the defence indicts itself: the code was
never tested against reality, only against an audience of none.
That fits the judge brief: one funny single-line developer excuse
for when code breaks in production, under 200 characters, clear on
first read, and a different joke mechanism from the previous round's
line (which used the lonely-machine twist on "works on my machine").
"""

import os

EXCUSE = (
    "It worked flawlessly in the demo \u2014 the demo, unlike "
    "production, had no users and no witnesses."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} characters"
    assert "\n" not in EXCUSE and EXCUSE == EXCUSE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
