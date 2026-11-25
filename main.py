#!/usr/bin/env python3
"""One Line, Big Laugh — writes a single funny line to /output/entry.txt.

The entry is one original line, 200 characters or fewer, that lands entirely
on its own: no title, no setup, no explanation around it.
"""

import os

LINE = "My Roomba filed for divorce. It said I never let it finish anything, and I keep moving the furniture."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
