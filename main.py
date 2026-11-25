#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

One line, the whole meeting in it: the verdict, the twist, and the
only attendee who never objected.
"""

import os

ENTRY = (
    "Approved, but the office dog gets the final vote from now on \u2014 "
    "he has attended every meeting and objected to none of them."
)


def main() -> None:
    assert 30 <= len(ENTRY) <= 200, f"entry length out of band: {len(ENTRY)} chars"
    assert ENTRY.count("\n") == 0, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
