#!/usr/bin/env python3
"""Whole-system dedupe gate for build scripts (his standing rule: every
generator checks the WHOLE system before generating — no time limit,
correctness first).

Bulk generation happens on build machines, where the full exact index can
be consulted with no time pressure. Every build script that writes records
must call gate.check() BEFORE writing each record.

Usage in a build script:
    import sys; sys.path.insert(0, '<jah-databases>/code')
    from dedupe_gate import DedupeGate
    gate = DedupeGate('<jah-databases>/data/dedupe')   # exact/ shards
    ...
    for seed, rec in candidates:
        hits = gate.check('my-slug', rec['title'])
        if hits:
            continue            # or reseed / regenerate — never write a dupe
        write(rec); gate.admit('my-slug', rec['title'], rec['id'])

Also usable as an audit:
    python3 dedupe_gate.py --audit --repo ~/workspace/jah-databases
        -> reports existing cross-database duplicate titles.

The normalization/hashing MUST match code/build_global_dedupe.py and
core/jahdb-dedupe.js. Import them from build_global_dedupe to avoid drift:
"""
import gzip
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_global_dedupe import norm_title, fnv1a64_hex, local_index_path


class DedupeGate:
    def __init__(self, exact_dir):
        self.exact_dir = exact_dir
        self._cache = {}          # xx -> {hashhex: [[slug,id],...]}
        self._admitted = {}       # hashhex -> [[slug,id],...] (this run)

    def _shard(self, xx):
        if xx not in self._cache:
            p = os.path.join(self.exact_dir, xx + ".json.gz")
            if os.path.exists(p):
                with gzip.open(p, "rt", encoding="utf-8") as f:
                    self._cache[xx] = json.load(f).get("m", {})
            else:
                self._cache[xx] = {}
        return self._cache[xx]

    def check(self, slug, title):
        """Return list of [slug, id] already holding this normalized title."""
        hx = fnv1a64_hex(norm_title(title))
        shard = self._shard(hx[:2])
        hits = [h for h in shard.get(hx, [])]
        for h in self._admitted.get(hx, []):
            if h not in hits:
                hits.append(h)
        return hits

    def admit(self, slug, title, rec_id):
        hx = fnv1a64_hex(norm_title(title))
        self._admitted.setdefault(hx, []).append([slug, rec_id])

    def check_and_raise(self, slug, title):
        hits = self.check(slug, title)
        if hits:
            raise ValueError(
                "whole-system duplicate: %r already in %s"
                % (title, ", ".join("%s:%s" % (s, i) for s, i in hits)))
        return True


def audit(repo):
    """Report existing duplicate titles across ALL databases (read-only)."""
    from collections import defaultdict
    manifest = json.load(open(os.path.join(repo, "data", "manifest.json")))
    seen = {}
    dupes = defaultdict(list)
    n = 0
    for e in manifest["databases"]:
        slug = e["slug"]
        p = local_index_path(repo, e)
        if not p or not os.path.exists(p):
            continue
        try:
            with gzip.open(p, "rt", encoding="utf-8") as f:
                head = f.read(2); f.seek(0)
                rows = json.load(f) if head.lstrip().startswith("[") else [
                    json.loads(l) for l in f if l.strip()]
        except OSError:
            continue
        for r in rows:
            if not isinstance(r, dict):
                continue
            t = r.get("t") or r.get("title") or r.get("name")
            if not t:
                continue
            nt = norm_title(t)
            if not nt:
                continue
            n += 1
            if nt in seen:
                dupes[nt].append((slug, r.get("id")))
            else:
                seen[nt] = (slug, r.get("id"))
    print("records scanned: %d" % n)
    print("duplicate normalized titles: %d" % len(dupes))
    items = sorted(dupes.items(), key=lambda kv: -len(kv[1]))[:50]
    for nt, occ in items:
        print("  %r -> %s (+%d more)" % (nt[:60], seen[nt], len(occ)))
    return dupes


if __name__ == "__main__":
    repo = os.path.expanduser("~/workspace/jah-databases")
    args = sys.argv[1:]
    if "--repo" in args:
        repo = args[args.index("--repo") + 1]
    if "--audit" in args:
        audit(repo)
    else:
        print("usage: dedupe_gate.py --audit [--repo PATH]")
