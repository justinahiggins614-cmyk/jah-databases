#!/usr/bin/env python3
"""Wave 7 driver: builds all 67 pairs (134 databases, 34 records each).

Usage: python3 build_all.py [slug ...]   (no args = build all, first-release first)
Staged only — never touches data/manifest.json or api.json.
Property of Justin Addam Higgins (JAH).
"""
import os
import sys

W7 = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, W7)
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

import fw  # noqa: E402
import items_food  # noqa: E402
try:
    import items_travel  # noqa: E402
except ImportError:
    items_travel = None
try:
    import items_animals  # noqa: E402
except ImportError:
    items_animals = None
try:
    import items_travel2  # noqa: E402
except ImportError:
    items_travel2 = None

ITEMS = {}
for mod in (items_food, items_travel, items_animals, items_travel2):
    if mod is None:
        continue
    for it in mod.ITEMS:
        assert it["slug"] not in ITEMS, "dup slug " + it["slug"]
        ITEMS[it["slug"]] = it

FIRST = ["gen-build-your-own-burger", "gen-food-presentation-studio", "gen-unusual-pet-names"]


def build_slug(slug):
    item = ITEMS[slug]
    return fw.build_one(item)


def main():
    only = sys.argv[1:]
    order = FIRST + [s for s in ITEMS if s not in FIRST]
    if only:
        order = [s for s in order if s in only]
        assert len(order) == len(only), "unknown slug in %r" % (only,)
    all_built = {}
    for slug in order:
        built = build_slug(slug)
        all_built.update(built)
    # cross-pair dedupe across everything built in this run
    import lib as pairlib
    pairlib.cross_pair_dedupe(all_built)
    print("WAVE7 DONE: %d databases, %d records" %
          (len(all_built), sum(len(v) for v in all_built.values())))


if __name__ == "__main__":
    main()
