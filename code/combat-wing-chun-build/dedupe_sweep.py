#!/usr/bin/env python3
"""Pre-authoring whole-system dedupe sweep for the Wing Chun Combat build.

Checks all 68 titles (34 public + 34 Signature Edition) against:
  1. the DedupeGate exact store (data/dedupe/exact),
  2. a RAW sweep of every shard index title in jah-databases-data-1/data,
  3. any index files in the main repo data dir.
Normalization matches code/build_global_dedupe.norm_title.
Exit 0 with 'ZERO COLLISIONS' or exit 1 listing collisions.
"""
import gzip
import json
import os
import sys

REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(REPO, "code"))
sys.path.insert(0, HERE)
from build_global_dedupe import norm_title
from dedupe_gate import DedupeGate
from entries_combat_wing_chun import ENTRIES

titles = []
for e in ENTRIES:
    titles.append(e["name"])
    titles.append(e["name"] + " (Signature Edition)")
assert len(titles) == 68

collisions = []

# 1. gate store
gate = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))
for t in titles:
    hits = [h for h in gate.check("combat-wing-chun", t) if h[0] != "combat-wing-chun"]
    if hits:
        collisions.append(("gate", t, hits))

# 2. raw shard index sweep
mine = {norm_title(t): t for t in titles}
idx_files = []
for slug in sorted(os.listdir(os.path.join(SHARD, "data"))):
    p = os.path.join(SHARD, "data", slug, "index.jsonl.gz")
    if os.path.exists(p):
        idx_files.append((slug, p))
print("sweeping %d shard index files..." % len(idx_files), flush=True)
n_lines = 0
for slug, p in idx_files:
    try:
        with gzip.open(p, "rt", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                n_lines += 1
                try:
                    row = json.loads(line)
                except Exception:
                    continue
                t = row.get("t")
                if not t:
                    continue
                nt = norm_title(t)
                if nt in mine and slug not in ("combat-wing-chun", "combat-wing-chun-signature"):
                    collisions.append(("shard", mine[nt], [(slug, row.get("id"))]))
    except Exception as ex:
        print("WARN: could not read %s: %s" % (p, ex), flush=True)
print("scanned %d index lines" % n_lines, flush=True)

# 3. main repo data dir index files
for root, _dirs, files in os.walk(os.path.join(REPO, "data")):
    for fn in files:
        if fn.endswith(".jsonl.gz") and "index" in fn:
            p = os.path.join(root, fn)
            try:
                with gzip.open(p, "rt", encoding="utf-8") as f:
                    for line in f:
                        try:
                            row = json.loads(line)
                        except Exception:
                            continue
                        t = row.get("t")
                        if t and norm_title(t) in mine:
                            collisions.append(("repo-data", mine[norm_title(t)], [(p, row.get("id"))]))
            except Exception:
                pass

if collisions:
    print("COLLISIONS: %d" % len(collisions))
    for src, t, hits in collisions[:50]:
        print("  [%s] %r hits %s" % (src, t, hits))
    sys.exit(1)
print("ZERO COLLISIONS across %d titles" % len(titles))
