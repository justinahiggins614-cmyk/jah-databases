#!/usr/bin/env python3
"""Shared build driver for gap-audit part-2 pairs (11 pairs, 22 DBs).

Each pair build.py defines PAIR (config), ENTRIES (34 tuples), DEMOS (dict of
demo-builder functions) and calls driver.run_pair(PAIR, ENTRIES, DEMOS).

Pipeline per DB (public + signature):
  1. whole-system dedupe gate on every title (his standing rule)
  2. record assembly (ladder-ordered, full schema)
  3. sanity gates: unique ids, prefix, required keys, no stubs, no banned
     content, profanity screen
  4. EVERY demo program: compile() + machine-executed via subprocess, must
     exit 0 and print the OK marker
  5. shard write: data/<slug>/index.jsonl.gz (light) + chunks/chunk-0000.jsonl.gz (full)
  6. page build from the canonical template via numbering-build helpers +
     staged sweep process_page + required-element assertions
  7. gen JS build via numbering-build helper + node --check
  8. manifest/api entry fragments STAGED to the pair build dir — NEVER merged
     into data/manifest.json or api.json (the coordinator merges).

Never commits. Never touches data/manifest.json or api.json.
"""
import gzip
import importlib.util
import json
import os
import re
import subprocess
import sys

REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
SWEEP = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate

GATE = None


def get_gate():
    global GATE
    if GATE is None:
        GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))
    return GATE


_nb = None


def get_nb(dbcfg):
    global _nb
    if _nb is None:
        spec = importlib.util.spec_from_file_location(
            "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
        _nb = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_nb)
    _nb.DBCFG = dbcfg
    _nb.SHARD_BASE = SHARD_BASE
    return _nb


_sweep = None


def get_sweep():
    global _sweep
    if _sweep is None:
        spec = importlib.util.spec_from_file_location("sweep", SWEEP)
        _sweep = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_sweep)
    return _sweep


BANNED = ["facebook", "bat belt"]
PROFANE = ["fuck", "shit", "bitch", " bastard", "cunt", "dick ", " porn",
           "whore", "slut", "nigger", "faggot"]


def content_ok(blob, rid):
    bl = blob.lower()
    for b in BANNED:
        assert b not in bl, "banned %r in %s" % (b, rid)
    for p in PROFANE:
        assert p not in bl, "profane-adjacent %r in %s" % (p, rid)
    # no religious framing
    for r in ["jesus", "christ ", "allah", "buddha", "scripture", "gospel ",
              "prayer", "worship", "church ", "mosque", "temple worship"]:
        assert r not in bl, "religious framing %r in %s" % (r, rid)


def demo_hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name.replace('"""', '"'), rid, group))


def build_records(slug, cfg, entries, demos, source):
    gate = get_gate()
    recs = []
    for i, e in enumerate(entries):
        group, name, desc, points, req, demo_key = e
        title = name + " (Signature Edition)" if source == "signature" else name
        hits = [h for h in gate.check(slug, title) if h[0] != slug]
        if hits:
            print("  gate refused (cross-db dupe): %s -> %s" % (title, hits[0]), flush=True)
            raise SystemExit("dedupe gate refused: %s" % title)
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        description = desc
        if source == "signature":
            description = ("Signature original treatment: " + desc +
                           " Reframed in the Signature system as his original expanded treatment.")
        rank = i + 1
        tier = "foundations" if rank <= 12 else ("compounded" if rank <= 24 else "advanced")
        tier_label = tier.capitalize()
        if source == "signature":
            how = ("The Signature edition of %s is his original Signature treatment: it takes the "
                   "public-record subject and rebuilds it as Signature science — the same verified "
                   "facts, reframed through the Signature system's expanded doctrine, with every "
                   "Signature addition clearly labeled and never presented as authentic public "
                   "record. The demonstration program below exercises the real computation." % name)
        else:
            how = ("In real-world practice, %s works as documented in the cited references: the "
                   "description above states the established facts, the key points isolate what a "
                   "practitioner must get right, and the demonstration program below performs the "
                   "actual computation a practitioner would run." % name)
        rec = {
            "id": rid, "t": title, "g": tier_label, "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(points),
            "requirements": req,
            "standards": list(cfg["standards"]),
            "citations": cfg["citations"],
            "src": "signature" if source == "signature" else "public-harvest",
            "ladder_rank": rank, "ladder_tier": tier,
        }
        dfn = demos.get(demo_key)
        assert dfn is not None, "missing demo %s for %s" % (demo_key, rid)
        program = dfn(name, rid, tier_label)
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable, stdlib-only Python)."}
        gate.admit(slug, title, rid)
        recs.append(rec)
    return recs


def sanity_and_execute(slug, cfg, recs):
    ids = [r["id"] for r in recs]
    assert len(ids) == len(set(ids)), "dup ids in %s" % slug
    assert all(x.startswith(cfg["prefix"]) for x in ids), "prefix drift in %s" % slug
    assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
    for r in recs:
        for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                  "key_points", "requirements", "standards", "citations", "src",
                  "ladder_rank", "ladder_tier", "demo"):
            assert k in r, "missing %s in %s" % (k, r["id"])
        assert len(r["description"]) > 200, "stub description in %s" % r["id"]
        assert len(r["how_it_works"]) > 100, "stub how_it_works in %s" % r["id"]
        assert len(r["key_points"]) >= 4, "thin key_points in %s" % r["id"]
        prog = r["demo"]["program"]
        assert prog and len(prog) > 200, "stub demo in %s" % r["id"]
        compile(prog, r["id"], "exec")
        content_ok(json.dumps(r, ensure_ascii=False), r["id"])
    # machine-execute EVERY demo
    for r in recs:
        prog = r["demo"]["program"]
        p = subprocess.run([sys.executable, "-c", prog], capture_output=True,
                           text=True, timeout=120)
        assert p.returncode == 0, "demo failed %s:\n%s" % (r["id"], p.stderr[-800:])
        assert "OK:" in p.stdout, "demo no OK marker %s:\n%s" % (r["id"], p.stdout[-400:])
    print("  gates+execute: %s %d records, %d demos ran OK" % (slug, len(recs), len(recs)), flush=True)


def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    # verify round-trip
    with gzip.open(os.path.join(base, "index.jsonl.gz"), "rt", encoding="utf-8") as f:
        n_idx = sum(1 for _ in f)
    with gzip.open(os.path.join(base, "chunks", "chunk-0000.jsonl.gz"), "rt", encoding="utf-8") as f:
        rows = [json.loads(l) for l in f]
    assert n_idx == len(recs) == len(rows), "shard count mismatch %s" % slug
    assert rows[0]["id"] == recs[0]["id"] and "description" in rows[0]
    print("  shard: %s index=%d full=%d" % (slug, n_idx, len(rows)), flush=True)


def build_pages(slug, cfg, recs, pair_dir):
    nb = get_nb({slug: cfg})
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    page = nb.build_page(slug, template)
    page = page.replace(
        "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
        cfg["gen_desc"])
    assert 'id="stCount"' in page, "stCount missing"
    assert "var SLUG='%s';" % slug in page
    assert "minmax(120px,1fr)" in page, "kv grid rule missing"
    assert "pre.codeblock" in page
    assert 'id="qmerge"' in page and "All Database Merger" in page, "merger button missing"
    assert 'id="mergePanel"' in page
    assert 'id="qex"' in page and ">Exhaustive</button>" in page, "exhaustive pill missing"
    assert "dataset.p" in page, "tab guard missing"
    assert "facebook" not in page.lower()
    assert "synthetic intelligence" not in page.lower(), "template leftover"
    assert "bat belt" not in page.lower()
    content_ok(page, slug + "/index.html")
    ddir = os.path.join(REPO, "db", slug)
    os.makedirs(ddir, exist_ok=True)
    ppath = os.path.join(ddir, "index.html")
    with open(ppath, "w", encoding="utf-8") as f:
        f.write(page)
    sweep = get_sweep()
    changed, notes = sweep.process_page(ppath)
    topics = {}
    for r in recs:
        topics.setdefault(r["g"], []).append("%s — %s" % (r["t"], r["g"]))
    gen_js = nb.build_gen_js(slug, topics, cfg)
    assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
    gpath = os.path.join(ddir, "gen-%s.js" % slug)
    with open(gpath, "w", encoding="utf-8") as f:
        f.write(gen_js)
    p = subprocess.run(["node", "--check", gpath], capture_output=True, text=True)
    assert p.returncode == 0, "node --check failed %s: %s" % (gpath, p.stderr[-500:])
    # gen-js self-test: generate+validate one record per field
    test = ("var g=require(%s);var f=g.fields[0];var r=g.generate(7,{field:f});"
            "var v=g.validate(r);if(!v.ok)throw new Error(JSON.stringify(v.errors));"
            "if(!/^%s/.test(r.id))throw new Error('id prefix');"
            "console.log('gen-ok '+r.id);"
            % (json.dumps(gpath), cfg["prefix"].replace("-", "\\-")))
    p = subprocess.run(["node", "-e", test], capture_output=True, text=True)
    assert p.returncode == 0 and "gen-ok" in p.stdout, "gen self-test failed: %s" % p.stderr[-500:]
    print("  page: db/%s/index.html + gen-%s.js [%s] node-ok" % (slug, slug, ",".join(notes)), flush=True)


def stage_fragments(pair_dir, slug, cfg, n):
    frag_m = {
        "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
        "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
        "ai_name": cfg["ai"], "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "status": "staged", "full_records": n,
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": cfg["source"],
    }
    frag_a = {
        "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
        "record_kind": cfg["record_kind"], "record_count": n, "status": "staged",
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
    }
    with open(os.path.join(pair_dir, "manifest-fragment-%s.json" % slug), "w") as f:
        json.dump(frag_m, f, indent=1)
    with open(os.path.join(pair_dir, "api-fragment-%s.json" % slug), "w") as f:
        json.dump(frag_a, f, indent=1)


def pair_cfgs(slug_base, name_base, tagline, record_kind, prefix_pub,
              prefix_sig, ai_base, role_pub, role_sig, search_ph, chat_ph,
              archive_topic, gen_kind, standards, cit_pub, cit_sig,
              hero_pub, hero_sig):
    """Build the (public, signature) cfg pair. name_base like 'Scientific Datasets'
    -> 'The Scientific Datasets Database' / 'The Scientific Datasets Signature Database'."""
    def one(slug, name, tagline, rk, prefix, ai, role, source, cit, hero):
        sig = source == "signature"
        return {
            "slug": slug, "name": name, "tagline": tagline, "record_kind": rk,
            "prefix": prefix, "ai": ai, "role": role,
            "hero_p": hero,
            "sig_type": ("Signature originals organized in the Signature system"
                         if sig else "Public records organized in the Signature system"),
            "search_ph": search_ph, "chat_ph": chat_ph,
            "archive_blurb": ("Seeded %s %s, marching toward one million records. "
                              "Presented in teaching-ladder order: foundations, compounded, advanced."
                              % ("Signature-original" if sig else "public-record", archive_topic)),
            "schema": ("id, t, g, name, title, description, how_it_works, key_points, "
                       "requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
            "fields": "Foundations · Compounded · Advanced - each tier opens on demand and loads only what you open",
            "gen_desc": ("Generate clearly-labeled %s. Seeded archive records are the authoritative entries." % archive_topic),
            "greet": "I am the %s. %s" % (ai, chat_ph.replace("Ask about ", "Ask me about ").rstrip(".") + "."),
            "gen_fields": ["Foundations", "Compounded", "Advanced"],
            "gen_kind": gen_kind, "gen_demo_kind": gen_kind + "-demo",
            "source": source, "standards": standards, "citations": cit,
        }
    pub = one(slug_base, "The %s Database" % name_base, tagline, record_kind,
              prefix_pub, ai_base, role_pub, "public", cit_pub, hero_pub)
    sig = one(slug_base + "-signature", "The %s Signature Database" % name_base, tagline,
              record_kind, prefix_sig, ai_base + " (Signature)", role_sig,
              "signature", cit_sig, hero_sig)
    return pub, sig


def run_pair(pair_dir, cfg_pub, cfg_sig, entries, demos):
    """cfg_pub/cfg_sig: dicts with keys name, tagline, record_kind, prefix, ai,
    role, hero_p, sig_type, search_ph, chat_ph, archive_blurb, schema, fields,
    gen_desc, greet, gen_fields, gen_kind, gen_demo_kind, source, standards,
    citations."""
    assert len(entries) == 34, "need 34 entries, got %d" % len(entries)
    os.makedirs(pair_dir, exist_ok=True)
    built = {}
    for slug, cfg in ((cfg_pub["slug"], cfg_pub), (cfg_sig["slug"], cfg_sig)):
        source = cfg["source"]
        print("building %s ..." % slug, flush=True)
        recs = build_records(slug, cfg, entries, demos, source)
        sanity_and_execute(slug, cfg, recs)
        write_shard_db(slug, recs)
        build_pages(slug, cfg, recs, pair_dir)
        stage_fragments(pair_dir, slug, cfg, len(recs))
        built[slug] = len(recs)
    # id_prefix uniqueness within pair
    assert cfg_pub["prefix"] != cfg_sig["prefix"]
    print("pair done: %s" % built, flush=True)
    return built
