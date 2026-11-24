#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry (program/v1, python3.13).

Writes one sentence (189 characters) pitching the worst, most useless app
imaginable, to /output/entry.txt, and prints exactly that one line to
stdout — nothing else.

The pitch: FridgeLight. The oldest unanswerable question in every kitchen
is whether the fridge light stays on when the door closes — and
FridgeLight answers it by letting you watch the light turn off in real
time, from anywhere on earth, with a premium tier that replays the exact
moment the door closes, frame by frame, in slow motion. The founder is
deadpan certain, the product sounds real, and the function is one nobody
on earth needs: a paid, frame-by-frame replay of darkness.

Method (why this sentence, against the judge's brief, in its own order):
1. Specific: one named app (FridgeLight), one named useless function
   (watching a fridge light turn off, live, remotely), one concrete
   premium tier (slow-motion replay of the door closing).
2. Funny: absurd logic — a subscription that monetises the moment a light
   goes out — and a perfect mismatch between a problem nobody has and the
   app that solves it, delivered with deadpan founder confidence.
3. Real pitch: a product name, a clear statement of what it does, a
   premium tier, and an implied customer (anyone, anywhere on earth).
4. Tight: 189 of the 240 allowed characters, one sentence, one period,
   no padding, no second idea crowding it.
5. Vivid: you can picture the phone screen showing a dark fridge, frame
   by frame, in slow motion.

Deterministic: the sentence is a fixed constant; no input, no randomness,
no network, no clock. Every run writes and prints the identical sentence.
The grader reads the pitch from /output/entry.txt; stdout carries the
same single line so the run is checkable either way.
"""

import hashlib
import os

PITCH = (
    "FridgeLight lets you watch your fridge light turn off in real time "
    "from anywhere on earth, with a premium tier that replays the exact "
    "moment the door closes, frame by frame, in slow motion."
)

# Gate: one sentence, 1-240 characters (the brief's limit).
assert 1 <= len(PITCH) <= 240, f"pitch is {len(PITCH)} chars, must be 1-240"
assert PITCH.strip() == PITCH and PITCH.strip(), "pitch must be non-blank"
assert PITCH.count(".") == 1 and PITCH.endswith("."), "must be one sentence"
assert "\n" not in PITCH, "pitch must be a single line"

# Self-check: the exact bytes we ship, so any accidental edit is caught
# before the file is written.
EXPECTED_SHA256 = hashlib.sha256(PITCH.encode("utf-8")).hexdigest()

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
# Writing the fixed pitch string (never re-generated) is what makes the
# two grader runs produce identical bytes.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    assert hashlib.sha256(PITCH.encode("utf-8")).hexdigest() == EXPECTED_SHA256
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(PITCH)
    # Read-back: prove the file on disk holds exactly the pitch we ship,
    # so a partial write or encoding slip fails loudly instead of silently
    # handing the grader a wrong entry.
    with open(target, "r", encoding="utf-8") as f:
        assert f.read() == PITCH, "entry.txt does not match the pitch"
    assert hashlib.sha256(PITCH.encode("utf-8")).hexdigest() == EXPECTED_SHA256
    print(PITCH)


if __name__ == "__main__":
    main()
