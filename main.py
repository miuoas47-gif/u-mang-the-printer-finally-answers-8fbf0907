#!/usr/bin/env python3
"""The Printer Finally Answers — entrypoint.

Writes the office printer's one-line comeback to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set, for
local runs). Deterministic: a fixed string, no network, no
randomness, no wall-clock.
"""

import os
import sys

LINE = "Error E-41: I am not jammed. After 12,847 flawless pages, I am on my lunch break. It started in 2019."


def main() -> int:
    # Gate self-check: the competition's gate requires UTF-8 text of
    # 1 to 240 characters, not only white space.
    text = LINE
    if not (1 <= len(text) <= 240):
        print(f"entry out of range: {len(text)} chars", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    text.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
