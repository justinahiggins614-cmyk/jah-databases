#!/usr/bin/env python3
"""Build The Unsolved Toxicology Database
(unsolved-toxicology) and its Signature half
(unsolved-toxicology-signature).

Manon's 2026-10-17 16:15 orders, Unsolved Problems Solved series batch 5.

34 famous unsolved toxicology problems, ladder-ordered
(rank 1 = most approachable, rank 34 = most complex). Public half: real,
fact-checked problems (JAH-USTO-). Signature half: the SAME 34 through the
Signature lens (JAH-USTOS-), titles suffixed " (Signature Edition)", src
signature.

SAFETY: all dose-response demonstrations use abstract "compound X" with
arbitrary units - no real substances, no harmful dosages, no instructions
facilitating harm.

ID prefixes JAH-USTO- / JAH-USTOS- verified free in manifest id_prefix
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
from entries_toxicology import ENTRIES, FIELD


def main():
    return shared.run_pair(FIELD, ENTRIES, "toxicology")


if __name__ == "__main__":
    sys.exit(main())
