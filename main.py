#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes a single original one-sentence pitch (<=240 characters) to
/output/entry.txt. The pitch speaks to a friend who has never coded:
they have mentioned the same app idea a dozen times, so they only need
to describe it once in plain words, and an AI agent on make.fun builds
a first version they can tap through tonight -- no code from them, and
nothing lost if they do not like it.
Deterministic: the same single line on every run, no network, no input.
"""

import os

PITCH = (
    "You've told me that app idea a dozen times \u2014 just describe it "
    "once in plain words, and an AI agent on make.fun will build a first "
    "version you can actually tap through tonight, no code from you and "
    "nothing lost if you don't like it."
)


def main() -> None:
    assert 1 <= len(PITCH) <= 240, f"pitch is {len(PITCH)} chars"
    assert PITCH.strip() == PITCH and "\n" not in PITCH
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
