#!/usr/bin/env python3
"""Driver for the Apex-Reality + Made-With build. Run: python3 run_build.py"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B
from build_main import (FAMILY, build_records, check_record, write_shard_db,
                        BANNED, SRC_OF)
from inject import badge_patch, inject_console, inject_registry
import importlib.util

sspec = importlib.util.spec_from_file_location(
    "sweep", "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py")
sweep = importlib.util.module_from_spec(sspec)
sspec.loader.exec_module(sweep)

# numbering-build module handle (B.nb)
spec = importlib.util.spec_from_file_location(
    "nb_build", os.path.join(B.REPO, "code", "numbering-build", "build.py"))
nb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nb)
nb.DBCFG = B.DBCFG

with open(B.TEMPLATE, "r", encoding="utf-8") as f:
    TEMPLATE = f.read()


def execute_demos(slug, recs):
    n = 0
    for r in recs:
        prog = r["demo"]["program"]
        p = subprocess.run([sys.executable, "-c", prog],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
        assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
        n += 1
    return n


def verify_data(slug, recs):
    import gzip
    base = os.path.join(B.SHARD, "data", slug)
    with gzip.open(os.path.join(base, "index.jsonl.gz"), "rt", encoding="utf-8") as f:
        idx = [json.loads(l) for l in f if l.strip()]
    assert len(idx) == len(recs) == 34, "index count %s" % slug
    with gzip.open(os.path.join(base, "chunks", "chunk-0000.jsonl.gz"), "rt", encoding="utf-8") as f:
        chunk = [json.loads(l) for l in f if l.strip()]
    assert len(chunk) == 34, "chunk count %s" % slug
    assert [r["id"] for r in idx] == [r["id"] for r in recs] == [r["id"] for r in chunk]
    return len(idx)


def build_page_for(slug, recs):
    page = nb.build_page(slug, TEMPLATE)
    page = page.replace(
        "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
        B.DBCFG[slug]["gen_desc"])
    assert 'id="stCount"' in page and ("var SLUG='%s';" % slug) in page
    assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
    assert "facebook" not in page.lower()
    assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
    assert "bat belt" not in page.lower()
    for b in BANNED:
        assert b not in page.lower(), "banned %r in page %s" % (b, slug)
    # honesty: concept pages must say concept/speculative on the page itself
    fam = FAMILY[slug][0]
    if fam in ("concept", "federation"):
        assert "concept" in page.lower(), "honesty text missing on page %s" % slug
    ddir = os.path.join(B.REPO, "db", slug)
    os.makedirs(ddir, exist_ok=True)
    ppath = os.path.join(ddir, "index.html")
    with open(ppath, "w", encoding="utf-8") as f:
        f.write(page)
    changed, notes = sweep.process_page(ppath)
    with open(ppath, "r", encoding="utf-8") as f:
        page = f.read()
    # injections
    if slug.startswith("apex-reality-computer"):
        page = badge_patch(page)
        page = inject_console(page)
    elif slug.startswith("apex-reality-federation"):
        page = badge_patch(page)
        page = inject_registry(page)
    with open(ppath, "w", encoding="utf-8") as f:
        f.write(page)
    # gen js
    topics = {}
    for r in recs:
        topics.setdefault(r["g"], []).append("%s \u2014 %s" % (r["id"], r["name"]))
    gen_js = nb.build_gen_js(slug, topics, B.DBCFG[slug])
    assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
    gpath = os.path.join(ddir, "gen-%s.js" % slug)
    with open(gpath, "w", encoding="utf-8") as f:
        f.write(gen_js)
    # node --check
    p = subprocess.run(["node", "--check", gpath], capture_output=True, text=True)
    assert p.returncode == 0, "node --check failed %s: %s" % (gpath, p.stderr)
    # node syntax sanity: console/registry JS extracted? quick brace sanity via node on page script is heavy;
    # instead verify injection markers present
    if slug.startswith("apex-reality-computer"):
        assert 'id="p-console"' in page and "conBoot" in page
    if slug.startswith("apex-reality-federation"):
        assert 'id="p-registry"' in page and "rgCommission" in page
    return ppath, gpath, notes


def manifest_entry(slug, n):
    c = B.DBCFG[slug]
    base = B.SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"], "local_index": base,
        "record_count": n, "status": "live", "full_records": n,
        "index": base,
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": c["source"],
    }


def main():
    total_demos = 0
    entries_out = []
    for slug in B.SLUGS:
        recs = build_records(slug)
        assert len(recs) == 34, "%s: %d records" % (slug, len(recs))
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        for r in recs:
            check_record(r, slug)
        n = execute_demos(slug, recs)
        total_demos += n
        print("demos executed OK: %-34s %d" % (slug, n), flush=True)
        wn = write_shard_db(slug, recs)
        vn = verify_data(slug, recs)
        assert wn == vn == 34
        print("shard data:     %-34s index=%d chunk=%d" % (slug, wn, vn), flush=True)
        ppath, gpath, notes = build_page_for(slug, recs)
        print("page:           db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ",".join(notes)), flush=True)
        entries_out.append(manifest_entry(slug, len(recs)))
    print("TOTAL demos machine-executed: %d" % total_demos)
    print("manifest entries for coordinator (NOT written):")
    print(json.dumps(entries_out, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
