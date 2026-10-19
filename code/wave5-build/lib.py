#!/usr/bin/env python3
"""Shared build core for the 1000 fun/social list, WAVE 5 (subagent a3996ec4).

49 items (mystery x29, civilization-space x20) -> 98 databases (public +
Signature pair each), 34 ladder-ordered full records each = 3,332 records.

Mirrors the merged pair structure (db/language-pashto/): pages rendered with
code/numbering-build's build_page from the public-synthetic-intelligence
template, swept with the quality-audit sweep script, generators via
build_gen_js (custom hand-authored JS for the 4 GENERATOR-class items), shard
data as data/<slug>/index.jsonl.gz (light) + chunks/chunk-0000.jsonl.gz
(full records), and coordinator-merge fragments in
~/workspace/hidden_files/missing-builds/fragments/<slug>.json (status staged).

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Content gates: nothing hate-adjacent/profane/inappropriate; no religious
framing; paranormal/cryptid content separates evidence from speculation and
is clearly labeled; fictional scenarios are clearly fictional, never
presented as real-world claims. No website references. No Facebook.
Property of Justin Addam Higgins (JAH).
"""
import gzip
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import time
from contextlib import redirect_stdout

REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"
OWNER = "Justin Addam Higgins (JAH)"
WAVE = "wave5-mystery-civspace"

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
nb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(nb)

_sspec = importlib.util.spec_from_file_location(
    "sweep", "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py")
sweep = importlib.util.module_from_spec(_sspec)
_sspec.loader.exec_module(sweep)

GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

BLOCKLIST = [
    "nigger", "faggot", "kike", "spic", "chink", "raghead", "tranny",
    "fuck", "shit", "bitch", "whore", "slut", "porn", "xxx",
    "kill all", "exterminate", "master race", "racial purity",
    "jesus christ", "bible", "quran", "koran", "torah", "talmud",
    "salvation", "eternal damnation", "holy war", "jihad",
    "bat belt", "facebook",
]


def _block_pattern():
    parts = []
    for term in BLOCKLIST:
        if " " in term:
            parts.append(re.escape(term))
        else:
            parts.append(r"\b" + re.escape(term) + r"\b")
    return re.compile("|".join(parts), re.IGNORECASE)


BLOCK_RE = _block_pattern()


def check_banned(blob, where):
    m = BLOCK_RE.search(blob or "")
    assert not m, "content gate hit %r in %s" % (m.group(0)[:40], where)


TIERS = [("Foundations", 0, 6), ("Compounded", 6, 12), ("Advanced", 12, 17)]


def _ladder(i):
    rank = i + 1
    for tier, lo, hi in TIERS:
        if lo <= (i // 2) < hi:
            return rank, tier
    return rank, "Advanced"


# ---------------------------------------------------------------- prefixes
def load_existing_prefixes():
    m = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    out = set()
    for e in m["databases"]:
        p = e.get("id_prefix")
        if p:
            out.add(p)
    return out


def initialism(name, n=3):
    words = re.findall(r"[A-Za-z]+", name)
    stop = {"the", "of", "a", "an", "and", "vs", "s", "to", "for", "in", "on",
            "from", "with", "by", "is", "it", "as", "at", "or", "de", "la"}
    letters = "".join(w[0].upper() for w in words
                      if w.lower() not in stop and len(w) > 1)
    return (letters[:n] or "X").ljust(min(n, 3), "X")[:n]


def alloc_prefix(family_letter, name, taken):
    """Collision-free prefix: exact + substring both ways vs manifest and
    everything taken in this run. Signature edition gets an S before the dash.
    Falls back to longer initialisms when the 3-letter code collides."""
def _codes_for(name):
    """Candidate code strings, shortest first: initialisms, then 2-letter
    word fragments (dodges substring clashes like 'JAH-CHP' vs 'JAH-CHPD-')."""
    words = [w for w in re.findall(r"[A-Za-z]+", name)
             if w.lower() not in {"the", "of", "a", "an", "and", "vs", "s",
                                  "to", "for", "in", "on", "from", "with",
                                  "by", "is", "it", "as", "at", "or", "de",
                                  "la"} and len(w) > 1]
    codes = []
    for n in (3, 4, 5, 6):
        c = initialism(name, n)
        if c not in codes:
            codes.append(c)
    frag = "".join(w[:2].upper() for w in words)[:8]
    if frag and frag not in codes:
        codes.append(frag)
    return codes


def alloc_prefix(family_letter, name, taken):
    """Collision-free prefix: exact + substring both ways vs manifest and
    everything taken in this run. Signature edition gets an S before the dash."""
    for code in _codes_for(name):
        i = 0
        while True:
            cand = "JAH-%s%s%s-" % (family_letter, code, "" if i == 0 else str(i))
            clash = any(cand == p or cand in p or p in cand for p in taken)
            if not clash:
                sig = cand[:-1] + "S-"
                clash = any(sig == p or sig in p or p in sig for p in taken)
                if not clash:
                    taken.add(cand)
                    taken.add(sig)
                    return cand, sig
            i += 1
            if i >= 50:
                break  # try the next code
    raise AssertionError("prefix allocation failed for %s" % name)


# ---------------------------------------------------------------- item registry
ITEMS = {}
ORDER = []


def S(key, t, g, fact, mechanism, evidence, sig_angle, sig_do, points, **kw):
    d = dict(key=key, t=t, g=g, fact=fact, mechanism=mechanism,
             evidence=evidence, sig_angle=sig_angle, sig_do=sig_do,
             points=points)
    d.update(kw)
    return d


def register(item):
    assert item["slug"] not in ITEMS, "duplicate item %s" % item["slug"]
    assert item.get("record_kind"), "item %s missing record_kind" % item["slug"]
    assert item.get("citation"), "item %s missing citation" % item["slug"]
    assert item.get("pub_line"), "item %s missing pub_line" % item["slug"]
    assert item.get("ai"), "item %s missing ai" % item["slug"]
    if item.get("custom_records") is None:
        assert len(item["seeds"]) == 17, \
            "item %s has %d seeds, need 17" % (item["slug"], len(item["seeds"]))
        keys = [s["key"] for s in item["seeds"]]
        assert len(set(keys)) == 17, "dup seed keys in %s" % item["slug"]
        for s in item["seeds"]:
            for f in ("t", "g", "fact", "mechanism", "evidence", "sig_angle",
                      "sig_do", "points"):
                assert s.get(f), "seed %s missing %s" % (s.get("key"), f)
            assert 3 <= len(s["points"]) <= 6, "seed %s points" % s["key"]
            s.setdefault("cite", [item["citation"]])
            s.setdefault("req", item.get("req_default") or
                         "Reading only - no equipment needed.")
            s.setdefault("demo", item.get("demo_default") or "report")
    ITEMS[item["slug"]] = item


def finalize_registry():
    seen = {}
    for slug, item in ITEMS.items():
        if item.get("custom_records") is None:
            for s in item["seeds"]:
                assert s["key"] not in seen, \
                    "seed key %r reused in %s and %s" % (s["key"], seen.get(s["key"]), slug)
                seen[s["key"]] = slug
    picks = [s for s in ITEMS if ITEMS[s].get("first_pick")]
    rest = [s for s in ITEMS if not ITEMS[s].get("first_pick")]
    ORDER[:] = picks + rest
    return len(ITEMS), len(seen)


# ---------------------------------------------------------------- item cfg
def _sig_line():
    return ("Signature originals - his original Signature treatment of every entry: "
            "each record reframed with the Signature method for experiencing and "
            "applying it yourself, clearly labeled Signature-made, never presented "
            "as authentic public record.")


def _base_slug(slug):
    return slug[:-len("-signature")] if slug.endswith("-signature") else slug


def item_cfg(slug, source, prefixes):
    item = ITEMS[_base_slug(slug)]
    pub_prefix, sig_prefix = prefixes
    prefix = sig_prefix if source == "signature" else pub_prefix
    sig = source == "signature"
    base = item["name"]
    if base.endswith(" Database"):
        base = base[:-len(" Database")]
    name = base + (" Signature Database" if sig else " Database")
    tagline = item["tagline"]
    if sig:
        tagline = ("His original Signature edition: " + tagline +
                   " Clearly labeled Signature-made.")
    rk = item["record_kind"]
    hero_p = ("%s - %s Every record carries the full entry: description, how it works, "
              "key points, requirements, standards, citations, and a working demonstration "
              "program. Records are ordered by the teaching ladder: Foundations -> "
              "Compounded -> Advanced." % (tagline, _sig_line() if sig else item["pub_line"]))
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


# ---------------------------------------------------------------- records
def make_record(slug, cfg, source, seed, rung, idx, rid, DEMOS):
    sig = source == "signature"
    if rung == 1:
        if sig:
            title = seed["t"] + " (Signature Edition)"
            description = (seed["sig_angle"] + " Signature original: this entry reframes the "
                           "record the Signature way, with the Signature method for experiencing "
                           "it yourself. Clearly labeled Signature-made, never presented as "
                           "authentic public record.")
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
            # deep-dive descriptions pair the evidence with the mechanism's
            # lead sentence so the record stays a full, self-contained entry
            mech_first = seed["mechanism"].split(".")[0].strip()
            if len(description) <= 140 and mech_first and \
                    mech_first not in description:
                description = description.rstrip() + " " + mech_first + "."
            how = seed["mechanism"]
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


def build_records(slug, source, prefixes, DEMOS):
    from gen_custom import GEN_CUSTOM
    item = ITEMS[_base_slug(slug)]
    cfg = item_cfg(slug, source, prefixes)
    sig = source == "signature"
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
                "citations": r.get("citations") or [item["citation"]],
                "src": "signature" if sig else "public-harvest",
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
                recs.append(make_record(slug, cfg, source, seed, rung, i, rid, DEMOS))
    # whole-system dedupe gate (his standing rule)
    own = (slug, slug + "-signature") if not slug.endswith("-signature") \
        else (slug[:-len("-signature")], slug)
    eslug = slug if source == "public" else slug + "-signature"
    for r in recs:
        hits = [h for h in GATE.check(eslug, r["title"]) if h[0] not in own]
        if hits:
            raise ValueError("whole-system duplicate: %r already in %s"
                             % (r["title"], hits[0][0]))
    for r in recs:
        GATE.admit(eslug, r["title"], r["id"])
    return cfg, recs


# ---------------------------------------------------------------- writers
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
    assert "structural synthetic intelligence studies" not in page, \
        "gen_desc replacement missed"
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
    from gen_custom import GEN_CUSTOM
    custom = None
    base_slug = slug[:-len("-signature")] if slug.endswith("-signature") else slug
    if base_slug in GEN_CUSTOM:
        custom = GEN_CUSTOM[base_slug]["js"](
            "signature" if slug.endswith("-signature") else "public",
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
    # live generate+validate smoke test through node
    node_test = (
        "const g=require(%s);"
        "let n=0;"
        "for(const s of [7,42,3001]){"
        "  const r=g.generate(s,{});"
        "  const v=g.validate(r);"
        "  if(!v.ok) throw new Error('validate failed '+JSON.stringify(v.errors));"
        "  if(!r.demo||!r.demo.program) throw new Error('no demo');"
        "  n++;}"
        "console.log('GEN_OK '+n);"
    ) % json.dumps(path)
    p = subprocess.run(["node", "-e", node_test], capture_output=True, text=True)
    assert p.returncode == 0 and "GEN_OK 3" in p.stdout, \
        "gen smoke failed %s: %s" % (slug, p.stderr[:300])
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
        assert os.path.isfile(os.path.join(REPO, "db", s, "index.html")), "%s page" % s
        assert os.path.isfile(os.path.join(REPO, "db", s, "gen-%s.js" % s)), "%s genjs" % s
    frag = os.path.join(FRAGDIR, slug + ".json")
    assert os.path.isfile(frag), "fragment missing"
    fd = json.load(open(frag))
    assert set(fd.keys()) == {"public", "signature"}, "fragment keys"
    for ed in ("public", "signature"):
        assert fd[ed]["status"] == "staged", "fragment not staged"
    return True


def build_item(slug, prefixes, taken):
    from demos import DEMOS
    t0 = time.time()
    built = {}
    for source in ("public", "signature"):
        s = slug if source == "public" else slug + "-signature"
        cfg, recs = build_records(s, source, prefixes, DEMOS)
        built[s] = (cfg, recs)
        write_shard_db(s, recs)
    for s, (cfg, recs) in built.items():
        write_page(s, cfg, recs)
        write_gen_js(s, cfg, recs, ITEMS[slug])
    frag = {("signature" if s.endswith("-signature") else "public"):
            manifest_entry(s, cfg, len(recs)) for s, (cfg, recs) in built.items()}
    with open(os.path.join(FRAGDIR, slug + ".json"), "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    verify_item(slug, built)
    n = sum(len(r) for _, r in built.values())
    print("BUILT %-38s %d records (%.1fs)" % (slug, n, time.time() - t0), flush=True)
