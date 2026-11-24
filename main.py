#!/usr/bin/env python3
"""One-line developer excuse entry for the make.fun bounty
"Make the AI Judge Laugh: Developer Excuses".

Writes exactly one line — a funny excuse a developer gives when code
breaks in production — to /output/entry.txt. Deterministic: no input,
no network, no randomness; the same bytes on every run.

Craft notes: the excuse works because of one word doing double duty —
"passed". Every test passed, and the bug passed too, right past them
into production: the safety net itself waved the bug through. That
fits the judge brief: one funny single-line developer excuse for when
code breaks in production, under 200 characters, clear on first read,
and a different joke mechanism from the previous round's line (which
blamed the developer's optimism as the only test environment).
"""

import os

EXCUSE = (
    "All my tests passed \u2014 unfortunately, so did the bug, "
    "straight into production."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} characters"
    assert "\n" not in EXCUSE and EXCUSE == EXCUSE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
