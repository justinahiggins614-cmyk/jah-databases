#!/usr/bin/env python3
"""Repo/file size guard for JAH Data Bases drips.

Exits 0 when safe, non-zero when a limit is breached:
  - data/ total exceeds 800 MB  (repo soft cap ~850 MB)
  - any single file under data/ exceeds 90 MB (file cap 100 MB)

Usage: python3 code/guard.py
"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
MAX_DATA_MB = 800
MAX_FILE_MB = 90

failures = []

total = 0
for dirpath, _dirs, files in os.walk(DATA):
    for f in files:
        fp = os.path.join(dirpath, f)
        try:
            sz = os.path.getsize(fp)
        except OSError:
            continue
        total += sz
        if sz > MAX_FILE_MB * 1024 * 1024:
            failures.append(
                f"FILE OVER LIMIT: {os.path.relpath(fp, ROOT)} "
                f"is {sz/1024/1024:.1f} MB (cap {MAX_FILE_MB} MB)"
            )

total_mb = total / 1024 / 1024
print(f"data/ total: {total_mb:.1f} MB (guard {MAX_DATA_MB} MB)")
if total_mb > MAX_DATA_MB:
    failures.append(
        f"REPO OVER LIMIT: data/ is {total_mb:.1f} MB (cap {MAX_DATA_MB} MB) — "
        "do not push; shard sideways per docs/LIMITS.md"
    )

if failures:
    print("\n".join(failures))
    sys.exit(1)
print("guard: OK")
