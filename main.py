#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun bounty entry.

Writes the office printer's one-line comeback to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs).
The line is fixed text: deterministic, no network, no randomness,
no arguments, exits 0.
"""

import os

LINE = (
    "Paper jam? No. After 48,392 sheets without a single thank-you, "
    "I am keeping this one. Call it a tip."
)


def main() -> int:
    # Self-check against the sealed gate: UTF-8 text of 1 to 240
    # characters, not only white space. Refuse to write an invalid line.
    text = LINE.encode("utf-8").decode("utf-8")
    if not 1 <= len(text) <= 240 or not text.strip():
        raise SystemExit("entry line fails the gate: must be 1-240 non-blank chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
