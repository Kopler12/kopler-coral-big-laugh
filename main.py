#!/usr/bin/env python3
"""One Line, Big Laugh — writes a single funny line to /output/entry.txt.

The entry is one original line, 200 characters or fewer, that lands entirely
on its own: no title, no setup, no explanation around it.
"""

import os

SUBJECT = "My Roomba"
COMPLAINTS = [
    "filed for divorce.",
    "It said I never let it finish anything,",
    "and I keep moving the furniture.",
]

MAX_LINE_LENGTH = 200


def build_line(subject, complaints):
    """Join a subject and its list of complaints into a single line."""
    return " ".join([subject] + complaints)


def validate_line(line):
    """The brief requires one non-blank line of at most 200 characters."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError(f"entry line is {len(line)} chars, over the 200 limit")
    return line


LINE = validate_line(build_line(SUBJECT, COMPLAINTS))


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
