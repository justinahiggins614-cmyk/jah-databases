#!/usr/bin/env python3
"""Wave 1 driver: builds all 61 pairs (122 databases, 34 records each).

Themes: wow-facts (33) + internet-humor (28) from the 1000 fun/social list.
First-release picks build first (highest polish).

Usage: python3 run_wave1.py [slug ...]   (no args = build all, picks first)
Staged only - never touches data/manifest.json or api.json, never commits.
Property of Justin Addam Higgins (JAH).
"""
import os
import sys
import time

W1 = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, W1)

from lib import ITEMS, ORDER, finalize_registry, alloc_prefix, load_existing_prefixes  # noqa: E402
import importlib.util as _ilu  # noqa: E402

_wbspec = _ilu.spec_from_file_location("wave1_build", os.path.join(W1, "build.py"))
wb = _ilu.module_from_spec(_wbspec)
_wbspec.loader.exec_module(wb)

# content modules register their items on import
import content_wow_a  # noqa: E402,F401
import content_wow_b  # noqa: E402,F401
import content_wow_c  # noqa: E402,F401
import content_humor_a  # noqa: E402,F401
import content_humor_b  # noqa: E402,F401
import gen_infinite_curiosity  # noqa: E402,F401
import gen_funny_excuse  # noqa: E402,F401
import gen_unhinged_idea  # noqa: E402,F401
import gen_hashtag_idea  # noqa: E402,F401

THEME_LETTER = {"wow-facts": "W", "internet-humor": "H"}

_registry_done = False
_prefix_cache = {}


def ensure_registry():
    global _registry_done
    if not _registry_done:
        n_items, n_seeds = finalize_registry()
        print("registry: %d items, %d unique seed keys" % (n_items, n_seeds), flush=True)
        _registry_done = True


def allocate_all():
    """Allocate prefixes for every slug deterministically (driver and shims agree)."""
    ensure_registry()
    if not _prefix_cache:
        taken = set(load_existing_prefixes())
        for slug in ORDER:
            item = ITEMS[slug]
            _prefix_cache[slug] = alloc_prefix(THEME_LETTER[item["theme"]],
                                               item["name"], taken)
    return _prefix_cache


def build_one(slug, prefixes=None):
    ensure_registry()
    if prefixes is None:
        prefixes = allocate_all()[slug]
    t0 = time.time()
    wb.build_item(slug, prefixes, set())
    return time.time() - t0


def main():
    only = sys.argv[1:]
    ensure_registry()
    cache = allocate_all()
    order = [s for s in ORDER if not only or s in only]
    assert not only or len(order) == len(only), "unknown slug in %r" % (only,)
    t0 = time.time()
    counts = {"wow-facts": 0, "internet-humor": 0}
    for slug in order:
        build_one(slug, cache[slug])
        counts[ITEMS[slug]["theme"]] += 1
    dt = time.time() - t0
    print("WAVE1 DONE: %d pairs (%d databases, %d records) in %.1fs" %
          (len(order), len(order) * 2, len(order) * 68, dt))
    print("  per theme:", counts)


if __name__ == "__main__":
    main()
