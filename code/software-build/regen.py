#!/usr/bin/env python3
"""Rollout Phase 1 step 4: regen archive data for patched occupation + hobby DBs.

For each affected DB:
  - run the fixed gen-*.js under Node (window shim), seeds 1..record_count
  - validate each candidate with the new validate()
  - pipe through DedupeGate.check() (whole-system); same-slug hits are ignored
    because the old records are being REPLACED
  - survivors are re-ID'd sequentially and written to data/<slug>/
  - manifest record_count updated to the survivor count

Writes a manifest delta JSON for review before applying.
"""
import glob
import gzip
import json
import os
import subprocess
import sys

REPO = "/home/hatch/workspace/jah-databases"
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate

EXACT_DIR = "/home/hatch/workspace/jah-databases-data-1/data/dedupe/exact"
REGEN_JS = os.path.join(REPO, "code", "software-build", "regen-one.cjs")


def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def find_gen_js(slug):
    pats = glob.glob(os.path.join(REPO, "db", slug, "gen-*.js"))
    return pats[0] if pats else None


def light_row(r):
    # index light row: id + title-ish + group-ish
    t = r.get("title") or r.get("t") or ""
    g = r.get("aspect") or r.get("genre") or r.get("g") or ""
    return {"id": r["id"], "t": t, "g": g}


def main():
    slugs = sys.argv[1:]
    if not slugs:
        print("usage: regen.py <slug> [<slug> ...]")
        return 1
    gate = DedupeGate(EXACT_DIR)
    delta = {}
    for slug in slugs:
        gen = find_gen_js(slug)
        if not gen:
            print("SKIP (no gen): %s" % slug)
            continue
        # current record count from manifest
        m = json.load(open(os.path.join(REPO, "data", "manifest.json")))
        entry = next((d for d in m["databases"] if d["slug"] == slug), None)
        n = (entry or {}).get("record_count") or 50
        try:
            raw = subprocess.run(
                ["node", REGEN_JS, gen, str(n)],
                capture_output=True, text=True, timeout=120, cwd=REPO)
        except Exception as e:
            print("SKIP (node fail): %s %s" % (slug, e))
            continue
        if raw.returncode != 0:
            print("SKIP (node err): %s %s" % (slug, raw.stderr[:200]))
            continue
        try:
            cands = json.loads(raw.stdout)
        except Exception as e:
            print("SKIP (json): %s %s" % (slug, e))
            continue
        survivors = []
        seen_titles = set()
        for c in cands:
            if not c["ok"]:
                continue
            r = c["record"]
            title = r.get("title") or ""
            if not title or title in seen_titles:
                continue
            hits = [h for h in gate.check(slug, title) if h[0] != slug]
            if hits:
                continue  # whole-system duplicate elsewhere — refuse
            seen_titles.add(title)
            gate.admit(slug, title, r["id"])
            survivors.append(r)
        if not survivors:
            print("SKIP (no survivors): %s" % slug)
            continue
        # re-ID sequentially preserving the generator's prefix
        prefix = survivors[0]["id"].rstrip("0123456789")
        if not prefix:
            prefix = "JAH-"
        for i, r in enumerate(survivors, 1):
            r["id"] = "%s%06d" % (prefix, i)
        # write shard data (main repo data/ for these families)
        base = os.path.join(REPO, "data", slug)
        write_gz_jsonl(os.path.join(base, "index.jsonl.gz"),
                       [light_row(r) for r in survivors])
        # chunks of 100, numbered from 1 to match existing convention
        for f in glob.glob(os.path.join(base, "chunks", "*.jsonl.gz")):
            os.remove(f)
        for ci in range(0, len(survivors), 100):
            write_gz_jsonl(
                os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100 + 1)),
                survivors[ci:ci + 100])
        delta[slug] = {"old": n, "new": len(survivors)}
        print("regen: %-50s %d -> %d" % (slug, n, len(survivors)), flush=True)
    outp = os.path.join(REPO, "code", "software-build", "regen-delta.json")
    with open(outp, "w") as f:
        json.dump(delta, f, indent=1)
    print("delta written to %s (%d dbs)" % (outp, len(delta)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
