#!/usr/bin/env python3
"""Ship It Friday — one funny commit message from an AI coding agent.

The program writes a single line to /output/entry.txt: the commit message
an AI coding agent writes at 4:59pm on a Friday, right before it ships
to production.
"""
import os

ENTRY = "feat: Friday 4:59pm deploy, all tests green on my machine -- prod is just my machine with more users, shipping now"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
