#!/usr/bin/env python3
"""Pre-flight: check EVERY wave-9 topic title (+ Signature Edition variant)
against the whole-system dedupe gate and within the wave. Report all
collisions at once so renames happen in a single pass."""
import gzip
import json
import os
import sys

W9 = '/home/hatch/workspace/jah-databases/code/wave9-build'
SHARD = '/home/hatch/workspace/jah-databases-data-1'
sys.path.insert(0, W9)
sys.path.insert(0, '/home/hatch/workspace/jah-databases/code')

import items
from dedupe_gate import DedupeGate

ALL = json.load(open(os.path.join(W9, 'all_topics.json')))
gate = DedupeGate(os.path.join(SHARD, 'data', 'dedupe', 'exact'))

# pre-seed with staged wave-9 shards (from completed runs)
import glob
for idx_path in glob.glob(os.path.join(SHARD, 'data', '*', 'index.jsonl.gz')):
    slug = idx_path.split('/')[-2]
    try:
        with gzip.open(idx_path, 'rt', encoding='utf-8') as f:
            for line in f:
                r = json.loads(line)
                gate.admit(slug, r['t'], r['id'])
    except Exception:
        pass

collisions = []
seen = {}  # norm title -> (slug, title)
from build_global_dedupe import norm_title
for slug in sorted(items.ITEMS):
    for (title, tier, spec) in ALL[slug]:
        for variant, vslug in ((title, slug), (title + ' (Signature Edition)', slug + '-signature')):
            hits = gate.check(vslug, variant)
            if hits:
                # ignore hits that are this wave's own staged records for the same slug
                ext = [h for h in hits if not (h[0] == vslug)]
                if ext:
                    collisions.append((vslug, variant, ext))
            gate.admit(vslug, variant, 'PREFLIGHT')

print('total collisions:', len(collisions))
for vslug, variant, hits in collisions:
    print(' ', vslug, '|', variant, '| ->', hits[0][0], hits[0][1])
