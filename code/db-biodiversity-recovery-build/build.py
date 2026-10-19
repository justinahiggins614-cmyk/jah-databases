#!/usr/bin/env python3
"""Thin build driver for db-biodiversity-recovery (wave 5 of 1000-list). Re-runnable: rebuilds the
public + Signature pair from the wave-5 content registry."""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/wave5-build"))
os.chdir(os.path.expanduser("~/workspace/jah-databases/code/wave5-build"))
import content_all  # noqa: F401  (registers all 49 items)
from lib import finalize_registry, build_item

SLUG = "db-biodiversity-recovery"
PREFIXES = ("JAH-CBRD-", "JAH-CBRDS-")

def main():
    finalize_registry()
    build_item(SLUG, PREFIXES, set())

if __name__ == "__main__":
    main()
