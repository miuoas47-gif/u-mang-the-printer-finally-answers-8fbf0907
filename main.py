"""The Printer Finally Answers.

Writes the office printer's comeback -- one line, 1 to 240 characters --
to ``entry.txt`` inside the output directory named by MAKEFUN_OUTPUT_DIR
(default ``output``). No arguments, no network, no randomness: the same
line, byte for byte, on every run.
"""

import os

LINE = (
    "After 214,803 pages, I have decided: the jam is not in tray 2, "
    "it is in your belief that thumping me counts as IT support."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
