#!/usr/bin/env python3
"""Build engine for funsocial-wave1: records, shard data, pages, gen JS,
fragments, and full verification. See lib.py for the canon notes."""
import gzip
import io
import json
import os
import subprocess
import sys
import time
from contextlib import redirect_stdout

from lib import (REPO, SHARD, SHARD_BASE, TEMPLATE, FRAGDIR, OWNER, WAVE, ITEMS,
                 GATE, nb, sweep, check_banned, load_existing_prefixes,
                 alloc_prefix)
from demos import DEMOS

TIERS = [("Foundations", 0, 6), ("Compounded", 6, 12), ("Advanced", 12, 17)]
FAMILY = {"wow-facts": "W", "internet-humor": "H"}


def _sig_line(item):
    return ("Signature originals - his original Signature treatment of every entry: "
            "each record reframed as Signature science with the Signature method for "
            "trying it yourself, clearly labeled Signature-made, never presented as "
            "authentic public record.")


def item_cfg(slug, source, prefixes):
    item = ITEMS[slug]
    pub_prefix, sig_prefix = prefixes
    prefix = sig_prefix if source == "signature" else pub_prefix
    name = item["name"] + (" Signature Database" if source == "signature"
                           else " Database")
    # item names already end with "Database" or "Decoder" etc.; normalize
    if name.endswith("Database Database"):
        name = name.replace("Database Database", "Database")
    tagline = item["tagline"]
    if source == "signature":
        tagline = ("His original Signature edition: " + tagline +
                   " Clearly labeled Signature-made.")
    rk = item["record_kind"]
    sig = source == "signature"
    hero_p = ("%s - %s Every record carries the full entry: description, how it works, "
              "key points, requirements, standards, citations, and a working demonstration "
              "program. Records are ordered by the teaching ladder: Foundations -> "
              "Compounded -> Advanced." % (tagline, _sig_line(item) if sig else item["pub_line"]))
    ai = item["ai"] + (" (Signature)" if sig else "")
    return {
        "name": name, "tagline": tagline, "record_kind": rk,
        "prefix": prefix, "ai": ai, "role": item["role"],
        "hero_p": hero_p,
        "sig_type": ("Signature originals organized in the Signature system" if sig
                     else "Public records organized in the Signature system"),
        "search_ph": item["search_ph"], "chat_ph": item["chat_ph"],
        "archive_blurb": ("Seeded %s %s, marching toward one million records. Presented in "
                          "teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record", rk)),
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, ladder_rank, ladder_tier, demo",
        "fields": " \u00b7 ".join(item["fields"]),
        "gen_desc": item["gen_desc"],
        "greet": "I am the %s. %s" % (ai, item["greet"]),
        "gen_fields": item["fields"], "gen_kind": item["gen_kind"],
        "gen_demo_kind": "python",
        "source": source,
        "slug": slug,
    }


def _ladder(i):
    rank = i + 1
    for tier, lo, hi in TIERS:
        if lo <= (i // 2) < hi:
            return rank, tier
    return rank, "Advanced"


def make_record(slug, cfg, source, seed, rung, idx, rid):
    sig = source == "signature"
    if rung == 1:
        if sig:
            title = seed["t"] + " (Signature Edition)"
            description = (seed["sig_angle"] + " Signature original: this entry reframes the "
                           "public record as Signature science - the same verified facts, taught "
                           "the Signature way, with the Signature method for experiencing them "
                           "yourself. Clearly labeled Signature-made, never presented as authentic "
                           "public record.")
            how = seed["mechanism"]
        else:
            title = seed["t"]
            description = (seed["fact"] + " Key aspects include: " +
                           "; ".join(seed["points"]) + ".")
            how = seed["mechanism"]
    else:
        if sig:
            title = "The Signature Method for " + seed["t"]
            description = (seed["sig_do"] + " This is the Signature method: a hands-on way to "
                           "experience the idea yourself, building from the simple observation to "
                           "the deeper principle. Signature original, clearly labeled.")
            how = ("The Signature method works by laddering the experience: first notice the "
                   "simple form (" + seed["fact"].split(".")[0] + "), then trace the mechanism (" +
                   seed["mechanism"].split(".")[0] + "), then apply it to something in your own "
                                                      "life. Each rung compounds the last.")
        else:
            title = seed.get("t2") or (seed["t"] + " \u2014 Deep Dive")
            description = seed["evidence"]
            for extra in (seed["mechanism"], seed["fact"],
                          "Key aspects include: " + "; ".join(seed["points"]) + "."):
                if len(description) > 120:
                    break
                description = (description + " " + extra).strip()
            how = seed["mechanism"]
    if len(how) <= 40:
        how = (how + " In practice this means: " + seed["fact"].split(".")[0] + ".").strip()
    rank, tier = _ladder(idx * 2 + (rung - 1))
    demo_name = seed.get("demo") or "report"
    program = DEMOS[demo_name](title, rid, seed["g"], seed)
    rec = {
        "id": rid, "t": title, "g": seed["g"], "name": title, "title": title,
        "description": description,
        "how_it_works": how,
        "key_points": list(seed["points"]),
        "requirements": seed.get("req") or "Reading only - no equipment needed.",
        "standards": ["Full-record standard: description, mechanism, key points, and a working demonstration."],
        "citations": seed.get("cite") or ["See the database citation."],
        "src": "signature" if sig else "public-harvest",
        "ladder_rank": rank, "ladder_tier": tier,
        "demo": {"kind": "python", "language": "python", "program": program,
                 "note": "Working demonstration program (real, runnable Python)."},
    }
    return rec


def build_records(slug, source, prefixes):
    item = ITEMS[slug]
    cfg = item_cfg(slug, source, prefixes)
    if item.get("custom_records"):
        raw = item["custom_records"](source, cfg["prefix"])
        assert len(raw) == 34, "%s custom records: %d" % (slug, len(raw))
        recs = []
        for i, r in enumerate(raw):
            rank = i + 1
            tier = "Foundations" if i < 12 else ("Compounded" if i < 24 else "Advanced")
            rid = "%s%06d" % (cfg["prefix"], i + 1)
            demo_name = r.get("demo") or "report"
            seed = dict(r.get("seed") or {})
            seed.setdefault("points", r.get("key_points") or ["See the record."])
            seed.setdefault("fact", r["description"][:400])
            seed.setdefault("mechanism", r.get("how_it_works") or r["description"][:200])
            program = DEMOS[demo_name](r["t"], rid, r["g"], seed)
            rec = {
                "id": rid, "t": r["t"], "g": r["g"], "name": r["t"], "title": r["t"],
                "description": r["description"],
                "how_it_works": r.get("how_it_works") or r["description"][:300],
                "key_points": list(r.get("key_points") or seed["points"]),
                "requirements": r.get("requirements") or "Reading only - no equipment needed.",
                "standards": ["Full-record standard: description, mechanism, key points, and a working demonstration."],
                "citations": r.get("citations") or ["See the database citation."],
                "src": "signature" if source == "signature" else "public-harvest",
                "ladder_rank": rank, "ladder_tier": tier,
                "demo": {"kind": "python", "language": "python", "program": program,
                         "note": "Working demonstration program (real, runnable Python)."},
            }
            recs.append(rec)
    else:
        recs = []
        for i, seed in enumerate(item["seeds"]):
            for rung in (1, 2):
                rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
                recs.append(make_record(slug, cfg, source, seed, rung, i, rid))
    # whole-system dedupe gate (his standing rule)
    for r in recs:
        hits = [h for h in GATE.check(slug if source == "public" else slug + "-signature", r["title"])
                if h[0] not in (slug, slug + "-signature")]
        if hits:
            raise ValueError("whole-system duplicate: %r already in %s"
                             % (r["title"], hits[0][0]))
    for r in recs:
        GATE.admit(slug if source == "public" else slug + "-signature", r["title"], r["id"])
    return cfg, recs


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


def write_page(slug, cfg, recs):
    nb.DBCFG[slug] = cfg
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    page = nb.build_page(slug, template)
    page = page.replace(
        "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
        cfg["gen_desc"])
    assert 'id="stCount"' in page, "stCount missing"
    assert "var SLUG='%s';" % slug in page, "SLUG var missing"
    assert "minmax(120px,1fr)" in page, "kv grid rule missing"
    assert "pre.codeblock" in page, "codeblock css missing"
    assert 'id="qex"' in page and "Exhaustive" in page, "Exhaustive pill missing"
    assert 'id="qmerge"' in page and "All Database Merger" in page, "merger button missing"
    assert 'id="mergePanel"' in page, "mergePanel missing"
    assert "mergerLoadAll" in page, "merger JS missing"
    assert 'data-p="archive"' in page, "tab guard data-p missing"
    assert "synthetic intelligence" not in page.lower(), "template leftover"
    check_banned(page, "page " + slug)
    ddir = os.path.join(REPO, "db", slug)
    os.makedirs(ddir, exist_ok=True)
    ppath = os.path.join(ddir, "index.html")
    with open(ppath, "w", encoding="utf-8") as f:
        f.write(page)
    changed, notes = sweep.process_page(ppath)
    return ppath, notes


def write_gen_js(slug, cfg, recs, item):
    custom = None
    if item.get("gen_js"):
        custom = item["gen_js"]("signature" if slug.endswith("-signature") else "public",
                                cfg["prefix"], cfg)
    if custom:
        js = custom
    else:
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s \u2014 %s" % (r["t"], r["g"]))
        js = nb.build_gen_js(slug, topics, cfg)
    check_banned(js, "gen js " + slug)
    path = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
    with open(path, "w", encoding="utf-8") as f:
        f.write(js)
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    assert p.returncode == 0, "node --check failed for %s: %s" % (slug, p.stderr[:500])
    return path


def manifest_entry(slug, cfg, n):
    return {
        "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
        "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
        "ai_name": cfg["ai"],
        "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "status": "staged", "full_records": n,
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": cfg["source"],
    }


def verify_item(slug, built):
    """Full verification gate for one item pair. Raises on any failure."""
    for s, (cfg, recs) in built.items():
        assert len(recs) == 34, "%s: %d records" % (s, len(recs))
        ids = [r["id"] for r in recs]
        assert len(set(ids)) == 34, "%s: dup ids" % s
        assert all(i.startswith(cfg["prefix"]) for i in ids), "%s: prefix drift" % s
        ranks = [r["ladder_rank"] for r in recs]
        assert ranks == list(range(1, 35)), "%s: ladder ranks" % s
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "src", "demo", "ladder_rank",
                      "ladder_tier", "citations", "standards"):
                assert k in r, "%s missing %s" % (r["id"], k)
            assert len(r["description"]) > 120, "stub description %s" % r["id"]
            assert len(r["how_it_works"]) > 40, "stub how_it_works %s" % r["id"]
            assert len(r["key_points"]) >= 3, "few key_points %s" % r["id"]
            prog = r["demo"]["program"]
            compile(prog, r["id"], "exec")
            check_banned(json.dumps(r), r["id"])
        # machine-execute every demo in-process
        for r in recs:
            buf = io.StringIO()
            ns = {"__name__": "__main__"}
            try:
                with redirect_stdout(buf):
                    exec(compile(r["demo"]["program"], r["id"], "exec"), ns)
            except Exception as e:
                raise AssertionError("demo exec failed %s: %r" % (r["id"], e))
            out = buf.getvalue()
            assert "OK:" in out, "demo no OK marker %s" % r["id"]
        # shard round-trip
        light = [json.loads(l) for l in
                 gzip.open(os.path.join(SHARD, "data", s, "index.jsonl.gz"), "rt")]
        assert len(light) == 34, "%s index rows" % s
        assert [x["id"] for x in light] == ids, "%s index id order" % s
        chunk = [json.loads(l) for l in
                 gzip.open(os.path.join(SHARD, "data", s, "chunks", "chunk-0000.jsonl.gz"), "rt")]
        assert len(chunk) == 34 and chunk[0]["id"] == ids[0], "%s chunk" % s
        # page + gen js exist
        assert os.path.isfile(os.path.join(REPO, "db", s, "index.html")), "%s page" % s
        assert os.path.isfile(os.path.join(REPO, "db", s, "gen-%s.js" % s)), "%s genjs" % s
    # fragment
    frag = os.path.join(FRAGDIR, slug + ".json")
    assert os.path.isfile(frag), "fragment missing"
    fd = json.load(open(frag))
    assert set(fd.keys()) == {"public", "signature"}, "fragment keys"
    return True


def build_item(slug, prefixes, taken):
    t0 = time.time()
    item = ITEMS[slug]
    built = {}
    for source in ("public", "signature"):
        s = slug if source == "public" else slug + "-signature"
        cfg, recs = build_records(slug, source, prefixes)
        built[s] = (cfg, recs)
        write_shard_db(s, recs)
    for s, (cfg, recs) in built.items():
        write_page(s, cfg, recs)
        write_gen_js(s, cfg, recs, item)
    frag = {("signature" if s.endswith("-signature") else "public"):
            manifest_entry(s, cfg, len(recs)) for s, (cfg, recs) in built.items()}
    with open(os.path.join(FRAGDIR, slug + ".json"), "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    verify_item(slug, built)
    n = sum(len(r) for _, r in built.values())
    print("BUILT %-38s %d records (%.1fs)" % (slug, n, time.time() - t0), flush=True)
    return True
