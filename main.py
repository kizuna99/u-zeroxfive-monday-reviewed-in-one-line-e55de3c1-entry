#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Monday, Reviewed in One Line — writes the winning one-line review."""

import os

LINE = (
    "One star \u2014 Monday spilled my coffee, hit me with 112 unread emails, "
    "and locked me in a 9 a.m. 'quick sync' now applying for permanent residency."
)


def main() -> None:
    # The grader provides /output; OUTPUT_DIR only overrides it for local runs.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
