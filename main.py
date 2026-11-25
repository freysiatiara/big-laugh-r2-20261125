#!/usr/bin/env python3
"""One Line, Big Laugh — round 2 entry (make.fun).

Writes a single funny line (93 characters) to /output/entry.txt.

The line is a two-beat joke: the bank's fraud system flags a $4 coffee
(setup) but waves through a $900 flight bought at 2 a.m. (inversion).
Stdlib only. Paths are resolved from this script's own directory so the
program does not depend on the caller's working directory.
"""

import os

ENTRY = "My bank flagged my $4 coffee as fraud, but the $900 flight I bought at 2 a.m. sailed through."

MAX_CHARS = 200


def output_path():
    """Absolute /output/entry.txt when available, else output/ beside this script."""
    primary = os.path.join(os.sep, "output", "entry.txt")
    try:
        os.makedirs(os.path.dirname(primary), exist_ok=True)
        return primary
    except OSError:
        here = os.path.dirname(os.path.abspath(__file__))
        fallback_dir = os.path.join(here, "output")
        os.makedirs(fallback_dir, exist_ok=True)
        return os.path.join(fallback_dir, "entry.txt")


def main():
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS) or not text.strip():
        raise SystemExit("entry must be 1-200 non-blank characters")
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
