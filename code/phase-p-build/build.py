#!/usr/bin/env python3
"""PHASE P — the combined Super Intelligence master database (Manon's order:
"Super Intelligence database and all scales of intelligence to God mode",
final compound master after Phase O's 7 scale databases).

2 compound databases:
  super-intelligence             — public-harvest cross-scale comparison records
  super-intelligence-signature   — Signature-original cross-scale designs

Records are COMPARISONS (dyads, capability ladders, ascension paths,
gaps/limits) + an index of the 7 scale databases — never copies of the 144
scale records. Every comparison names the JAH-ANII/HUMI/NARAI/AGII/SUPRI/
COLI/GODI records it draws on (xdb contract: the material is actually used).

Canon: code/dbtype-build pattern (template page, gzipped index chunks in
jah-databases-data-1, unique ID prefixes, manifest/api.json entries, dedupe
gate, sweep patch, generator JS). No website references, no Facebook, no
banned phrases. Superintelligence/God-mode entries are descriptive frameworks.
"""
import gzip
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_p import ENTRIES_P, PUB, SIG

# ---- reuse the proven demo library from the dbtype build
spec = importlib.util.spec_from_file_location(
    "dbb", os.path.join(REPO, "code", "dbtype-build", "build.py"))
dbb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dbb)
DEMOS = dbb.DEMOS
DEMO_NOTE = dbb.DEMO_NOTE
check_record = dbb.check_record
write_gz_jsonl = dbb.write_gz_jsonl
gz_jsonl_rows = dbb.gz_jsonl_rows
next_id = dbb.next_id

# ============================================================ record assembly
def how_it_works_pub(name, desc, points):
    return ("In comparative study, %s works as follows. %s The operating principles are: %s"
            % (name, desc, " ".join("%s." % p for p in points)))

def how_it_works_sig(name, desc, points):
    return ("The Signature edition of %s is an original Signature cross-scale design: "
            "it specifies the design, how to apply it, and the working demonstration "
            "as a complete design in the Signature system. %s "
            "The Signature design principles are: %s"
            % (name, desc, " ".join("%s." % p for p in points)))

def build_record_p(title, name, group, desc, points, req, standards, citations,
                   src, demo_kind, rid):
    if src == "signature":
        title = title + " (Signature Edition)"
        description = ("Signature original cross-scale design: " + desc +
                       " Key aspects include: " + "; ".join(points) + "." +
                       " Designed in the Signature system as an original cross-scale design.")
        hiw = how_it_works_sig(name, desc, points)
    else:
        description = (desc + " Key aspects include: " + "; ".join(points) + ".")
        hiw = how_it_works_pub(name, desc, points)
    rec = {
        "id": rid, "t": title, "g": group, "name": name, "title": title,
        "description": description, "how_it_works": hiw,
        "key_points": list(points), "requirements": req,
        "standards": list(standards), "citations": citations,
        "src": src,
    }
    prog = DEMOS[demo_kind](name, rid, group, points, req)
    note = "Working demonstration program (real, runnable Python%s)." % DEMO_NOTE.get(demo_kind, "")
    rec["demo"] = {"kind": "python", "language": "python",
                   "program": prog, "note": note}
    return rec

# ============================================================ database configs
def _cfg(slug, name, tagline, rk, prefix, ai, role, citation):
    return {
        "name": name, "tagline": tagline, "record_kind": rk,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s Every record carries the full entry: description, how it compares, "
                   "how to apply it, key points, requirements, standards, "
                   "citations, and a working demonstration program." % tagline),
        "sig_type": "Public records and Signature originals organized in the Signature system",
        "search_ph": "Search %s..." % rk,
        "chat_ph": "Ask about %s..." % rk,
        "archive_blurb": "Seeded public-record and Signature-original %s, marching toward one million records." % rk,
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "cross-scale intelligence comparisons",
        "gen_desc": ("Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries."),
        "greet": "I am the %s. Ask me about %s." % (ai, rk),
        "gen_fields": ["cross-scale intelligence comparisons"], "gen_kind": slug,
        "gen_demo_kind": "python", "source": "public+signature",
    }

DBCFG = {
    PUB: _cfg(
        PUB, "The Super Intelligence Database",
        "Cross-scale intelligence comparisons: what each of the seven intelligence scales can do that the others cannot, capability ladders, ascension paths between scales, and honest gaps — plus Signature editions.",
        "cross-scale intelligence comparison", "JAH-SUPER-",
        "JAH Super Intelligence Archivist",
        "super intelligence archivist — cross-scale comparisons and Signature designs",
        "Comparative cognition (standard literature)."),
    SIG: _cfg(
        SIG, "Signature Super Intelligence Database",
        "Signature-developed cross-scale intelligence designs, instruments, and God-mode canon.",
        "signature cross-scale intelligence design", "JAH-SUPER-SIG",
        "JAH Signature Super Intelligence Creator",
        "signature super intelligence creator — cross-scale designs and instruments",
        "Signature canon."),
}

def collision_check():
    manifest = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    slugs = {d["slug"] for d in manifest["databases"]}
    prefixes = {d.get("id_prefix") for d in manifest["databases"]}
    for slug, c in DBCFG.items():
        assert slug not in slugs, "slug collision: " + slug
        assert c["prefix"] not in prefixes, "prefix collision: " + c["prefix"]
    print("collision check: slugs + prefixes free", flush=True)

def build_new_records():
    built = {PUB: [], SIG: []}
    for (key, dbslug, title, desc, points, req, standards, citations,
         demo_kind, src) in ENTRIES_P:
        cfg = DBCFG[dbslug]
        ftitle = title + " (Signature Edition)" if src == "signature" else title
        if [h for h in GATE.check(dbslug, ftitle) if h[0] != dbslug]:
            print("  gate refused (cross-db dupe): %s" % ftitle, flush=True)
            continue
        recs = built[dbslug]
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        rec = build_record_p(title, title, dbslug, desc, points, req,
                             standards, citations, src, demo_kind, rid)
        check_record(rec)
        GATE.admit(dbslug, ftitle, rid)
        recs.append(rec)
    for slug, recs in built.items():
        assert recs, "empty db " + slug
    return built

def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)

# ============================================================ manifest / api entries
def manifest_entry(slug, n):
    c = DBCFG[slug]
    url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": url,
            "record_count": n, "status": "live", "full_records": n,
            "index": url,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public+signature"}

def api_entry(slug, n):
    c = DBCFG[slug]
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "record_count": n, "status": "live",
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"}

def update_json_list(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    have = {d["slug"] for d in data["databases"]}
    for e in entries:
        if e["slug"] not in have:
            data["databases"].append(e)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")

# ============================================================ main
def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    nbspec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(nbspec)
    nbspec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    assert os.path.exists(sweep_path), "sweep script missing: " + sweep_path
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    # ---- step 1: collision check (slug + ID prefix vs whole manifest)
    collision_check()

    # ---- step 2: build the 2 compound databases
    built = build_new_records()
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        total += len(recs)
        n = write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # ---- step 3: execute one demo per archetype used (all must run OK)
    # recover the demo kind per admitted record by matching titles to entries
    rec_kind = {}
    for (key, dbslug, title, _d, _p, _r, _s, _c, demo_kind, src) in ENTRIES_P:
        ftitle = title + " (Signature Edition)" if src == "signature" else title
        for r in built[dbslug]:
            if r["t"] == ftitle and r["id"] not in rec_kind:
                rec_kind[r["id"]] = demo_kind
                break
    kinds = set(rec_kind.values())
    print("demo archetypes used: %d (%s)" % (len(kinds), ", ".join(sorted(kinds))), flush=True)
    for k in sorted(kinds):
        rid = next(rid for rid, kk in rec_kind.items() if kk == k)
        rec = next(r for slug, recs in built.items() for r in recs if r["id"] == rid)
        prog = rec["demo"]["program"]
        p = subprocess.run([sys.executable, "-c", prog],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "demo failed %s: %s" % (rid, p.stderr[-500:])
        assert "OK:" in p.stdout, "demo no OK marker %s" % rid
        print("demo ok: %-12s %s" % (k, rid), flush=True)
    print("demo execution: %d archetypes ran OK" % len(kinds))

    # ---- step 4: pages + generators
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        field = DBCFG[slug]["fields"]
        topics = {field: ["%s — %s" % (r["t"], field) for r in recs]}
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ",".join(notes)), flush=True)

    entries_m = [manifest_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [api_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
