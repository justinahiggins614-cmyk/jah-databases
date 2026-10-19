#!/usr/bin/env python3
"""Build The Unsolved Petroleum Engineering Database
(unsolved-petroleum-engineering) and its Signature half
(unsolved-petroleum-engineering-signature).

Manon's 2026-10-17 16:15 orders, Unsolved Problems Solved series batch 5.

34 famous unsolved petroleum engineering problems, ladder-ordered (rank 1 =
most approachable, rank 34 = most complex). Public half: real, fact-checked
problems (JAH-USPE-). Signature half: the SAME 34 through the Signature lens
(JAH-USPES-), titles suffixed " (Signature Edition)", src signature.

ID prefixes JAH-USPE- / JAH-USPES- verified free in manifest id_prefix
values (exact + substring, both directions).

Honesty rule: every sig_solution opens with the exact label
"Signature-generated proposed solution \u2014 not established science".
Label gate asserts how_it_works startswith the label on all 68 records,
zero hyphenated leftovers.

CONCURRENCY: never touches data/manifest.json, api.json, hub index.html,
README.md, or docs/AI_ACCESS.md; never commits or pushes.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "unsolved-batch5-lib"))
import shared

sys.path.insert(0, HERE)
from entries_petroleum_engineering import ENTRIES, FIELD


def main():
    return shared.run_pair(FIELD, ENTRIES, "petroleum-engineering")


if __name__ == "__main__":
    sys.exit(main())
