#!/usr/bin/env python3
"""Build The Unsolved Data Science Database (unsolved-data-science) and its
Signature half (unsolved-data-science-signature).

Manon's 2026-10-17 16:15 orders, Unsolved Problems Solved series batch 5.

34 famous unsolved data science problems, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems (JAH-USDS-).
Signature half: the SAME 34 problems through the Signature lens
(JAH-USDSS-), titles suffixed " (Signature Edition)", src signature,
clearly labeled Signature-made.

ID prefixes JAH-USDS- / JAH-USDSS- verified free: zero hits in manifest
id_prefix values (exact + substring, both directions).

Honesty rule: every sig_solution opens with the exact label
"Signature-generated proposed solution \u2014 not established science";
never claims proof, never implies peer acceptance, never presents
speculation as settled. Label gate asserts how_it_works startswith the
label on all 68 records and zero hyphenated leftovers.

Demos: solution-explorer walkthroughs with confirm/refute panels,
machine-executed, real computed values, tight-bounds asserts.

CONCURRENCY: this script never touches data/manifest.json, api.json,
hub index.html, README.md, or docs/AI_ACCESS.md; never commits or pushes.
A merger handles registration. It only writes:
  db/unsolved-data-science/ + db/unsolved-data-science-signature/
  shard data dirs under ~/workspace/jah-databases-data-1/data/
  merger fragment under ~/workspace/hidden_files/missing-builds/fragments/
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "unsolved-batch5-lib"))
import shared

sys.path.insert(0, HERE)
from entries_data_science import ENTRIES, FIELD


def main():
    return shared.run_pair(FIELD, ENTRIES, "data-science")


if __name__ == "__main__":
    sys.exit(main())
