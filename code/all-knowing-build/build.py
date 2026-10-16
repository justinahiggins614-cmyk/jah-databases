#!/usr/bin/env python3
"""PHASE N — All-Knowing Databases: the master omniscient index.

ONE database indexing and cross-referencing every database in the JAH
Databases network (every database, its scope, record counts, key records),
plus its Signature edition carrying the original Signature
knowledge-organization framework.

Regen (keeps the index in sync with the manifest — deterministic, idempotent):
    cd ~/workspace/jah-databases
    python3 code/all-knowing-build/build.py
    python3 code/restamp_counts.py

Every database in data/manifest.json becomes exactly one record per
edition, in manifest order, with sequential IDs (JAH-AK-%06d /
JAH-AKS-%06d). Re-running regenerates everything from the current
manifest: new databases appear as new records, record counts refresh.

Canon: template page + gzipped index chunks in jah-databases-data-1,
unique ID prefixes, manifest/api.json upserts, whole-system dedupe gate
(code/dedupe_gate.py), .kv grids minmax(120px,1fr) via the shared
template, dedupe/xdb script tags + generator handlers via
sweep-db-pages.py. No website references, no Facebook, no banned phrases.
"""
import gzip
import importlib.util
import json
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
N_KEY = 6  # sampled key-record titles per index entry
# Banned strings (build canon: no Facebook references, no banned phrases).
# Key-record titles containing them are skipped during sampling.
BANNED = ("facebook", "bat belt")

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from themes import theme_of, THEMES, FALLBACK

PUBLIC_SLUG = "all-knowing-databases"
SIG_SLUG = "all-knowing-databases-signature"
PUBLIC_PREFIX = "JAH-AK-"
SIG_PREFIX = "JAH-AKS-"

# ============================================================ index sampling
# Key records: the first N_KEY titles of each database's own light index.
# Best effort — unresolved/empty indexes yield an empty key_records list,
# never a build failure.

def resolve_index(entry):
    for u in (entry.get("local_index") or "", entry.get("index") or ""):
        if not u:
            continue
        uu = u.replace("/data/data/", "/data/")
        if uu.startswith(SHARD_BASE + "/"):
            rel = uu[len(SHARD_BASE) + 1:]
            p = os.path.join(SHARD, rel)
            if os.path.exists(p):
                return p
        elif not uu.startswith("http"):
            p = os.path.join(REPO, uu)
            if os.path.exists(p):
                return p
    return None


def sample_titles(path, n):
    out = []
    try:
        with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                if not isinstance(r, dict):
                    continue
                t = r.get("t") or r.get("title") or ""
                if t:
                    tl = str(t).lower()
                    if any(b in tl for b in BANNED):
                        continue
                    out.append({"id": str(r.get("id", "")), "t": str(t)[:140]})
                if len(out) >= n:
                    break
    except Exception:
        return []
    return out


# ============================================================ demos
# Every demo is real, runnable, stdlib-only Python with an "OK:" marker.
# The public demo exercises master-index mechanics (slug map, theme map,
# inverted keyword index, lookups). The Signature demo exercises the
# original Signature knowledge-organization framework (deterministic theme
# taxonomy, classification, coverage).

def _hdr(title, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (title, rid, group))

STOP = {"the", "a", "an", "of", "and", "database", "databases", "in",
        "for", "to", "with", "on", "its", "by", "from"}


def _qword(name, slug):
    toks = [w for w in re.findall(r"[a-z0-9]+", name.lower())
            if w not in STOP and len(w) >= 3]
    if toks:
        return toks[0]
    toks = [w for w in slug.split("-") if w not in ("public", "signature")]
    return toks[0] if toks else "data"


# Fixed sample slice shared by every demo: flagship databases, resolved
# against the live manifest at build time (deterministic).
SAMPLE_SLUGS = ["equations", "patents", "specs", "words", "wiki", "ai-models"]


def demo_lookup(title, rid, group, slug, name, count, kind, theme, samples):
    rows = [{"slug": slug, "name": name, "theme": theme,
             "records": count, "kind": kind}]
    rows += [{"slug": s, "name": n, "theme": t, "records": c, "kind": k}
             for (s, n, t, c, k) in samples]
    qword = _qword(name, slug)
    prog = _hdr(title, rid, group) + '''\
"""Master-index lookup demo: builds a slug map, a theme map, and an inverted
keyword index over a sample slice of the network, then runs a slug lookup,
a theme browse, a full-text search, and a kind cross-reference."""
import re

INDEX = %s

STOP = %s

def tokenize(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP]

def build(rows):
    by_slug = {r["slug"]: r for r in rows}
    by_theme = {}
    inv = {}
    for r in rows:
        by_theme.setdefault(r["theme"], []).append(r["slug"])
        for w in set(tokenize(r["name"] + " " + r["kind"])):
            inv.setdefault(w, []).append(r["slug"])
    return by_slug, by_theme, inv

def main():
    rows = INDEX
    by_slug, by_theme, inv = build(rows)
    print("sampled network slice: %%d databases" %% len(rows))
    hit = by_slug[%s]
    print("slug lookup: %%s -> %%s (%%d %%s)" %% (
        hit["slug"], hit["name"], hit["records"], hit["kind"]))
    assert hit["records"] == %d, "record count mismatch"
    members = by_theme[%s]
    print("theme %%s: %%d databases in slice" %% (%s, len(members)))
    assert %s in members, "theme map missing own slug"
    q = %s
    res = sorted({s for w in tokenize(q) for s in inv.get(w, [])})
    print("search '%%s': %%d hit(s)" %% (q, len(res)))
    assert %s in res, "full-text search missed own slug"
    fam = sorted(r["slug"] for r in rows if r["kind"] == %s)
    print("kind cross-reference %%s: %%d database(s)" %% (%s, len(fam)))
    assert %s in fam, "kind cross-reference missed own slug"
    print("OK: %%s queried the master index four ways" %% %s)

if __name__ == "__main__":
    main()
''' % (json.dumps(rows, ensure_ascii=False), json.dumps(sorted(STOP)),
       json.dumps(slug), count, json.dumps(theme), json.dumps(theme),
       json.dumps(slug), json.dumps(qword), json.dumps(slug),
       json.dumps(kind), json.dumps(kind), json.dumps(slug),
       json.dumps(title))
    return prog


def demo_sigorg(title, rid, group, slug, name, theme, theme_kws, extra_themes,
                samples):
    theme_names = [t for t, _ in THEMES] + [FALLBACK]
    tax = {theme: sorted(theme_kws)}
    for t, kws in extra_themes:
        if t != theme:
            tax[t] = sorted(kws)[:8]
    # order the excerpt like the real taxonomy so first-match agrees
    order = {t: i for i, t in enumerate(theme_names)}
    tax = {t: tax[t] for t in sorted(tax, key=lambda t: order.get(t, 999))}
    rows = [{"slug": slug, "theme": theme}]
    rows += [{"slug": s, "theme": t} for (s, t) in samples]
    prog = _hdr(title, rid, group) + '''\
"""Signature knowledge-organization demo: the deterministic theme taxonomy
maps each database slug to exactly one browse theme. The demo classifies
this record with the framework, lists its theme members, verifies taxonomy
coverage over the slice, and checks determinism."""
import json

THEMES = %s
TAXONOMY = %s
INDEX = %s

def classify(slug):
    toks = set(slug.split("-"))
    for theme, kws in TAXONOMY.items():
        if toks & set(kws):
            return theme
    return %s

def main():
    print("taxonomy themes: %%d" %% len(THEMES))
    got = classify(%s)
    print("classify(%%s) -> '%%s'" %% (%s, got))
    assert got == %s, "framework mis-mapped its own record"
    members = [r["slug"] for r in INDEX if r["theme"] == %s]
    print("theme %%s members in slice: %%d" %% (%s, len(members)))
    assert %s in members, "theme member list missing own slug"
    uncovered = [r["slug"] for r in INDEX if r["theme"] not in THEMES]
    print("taxonomy coverage: %%d/%%d slice entries" %% (
        len(INDEX) - len(uncovered), len(INDEX)))
    assert not uncovered, "theme outside the taxonomy"
    assert classify(%s) == got, "classification not deterministic"
    print("OK: %%s organized by the Signature framework" %% %s)

if __name__ == "__main__":
    main()
''' % (json.dumps(theme_names, ensure_ascii=False),
       json.dumps(tax, ensure_ascii=False),
       json.dumps(rows, ensure_ascii=False),
       json.dumps(FALLBACK), json.dumps(slug), json.dumps(slug),
       json.dumps(theme), json.dumps(theme), json.dumps(theme),
       json.dumps(slug), json.dumps(slug),
       json.dumps(title))
    return prog

# ============================================================ record assembly

def _src_label(entry):
    s = (entry.get("source") or "").strip().lower()
    if "signature" in s:
        return "a Signature-original database"
    if "public" in s:
        return "a public-records database"
    if s.startswith("jah-") or s.startswith("signature-") or s.startswith("cyber-"):
        return "a network-source database"
    return "a JAH Databases archive"


def build_record_pub(entry, title, theme, key_recs, rid):
    name = entry["name"]
    slug = entry["slug"]
    n = entry.get("record_count", 0)
    kind = entry.get("record_kind") or "database record"
    tagline = entry.get("tagline") or ""
    ai = entry.get("ai_name") or "the database's archive AI"
    idx = entry.get("index") or entry.get("local_index") or ""
    desc = ("The %s is a JAH Database holding %s %s records, organized in "
            "the Signature system. %s This master-index entry cross-references "
            "the database: its scope, live index location, record count, AI "
            "archivist, and generator — with %d sampled key-record titles "
            "below." % (name, f"{n:,}", kind, tagline, len(key_recs)))
    scope = ("Scope: the full %s archive of %s (%s) — %s records in the '%s' "
             "browse theme, %s. This index entry covers the database as a "
             "whole: what it holds, how its records are stored and addressed, "
             "and how to query it." % (kind, name, slug, f"{n:,}", theme,
                                       _src_label(entry)))
    chunk_dir = "data/%s/chunks/" % slug
    hiw = ("As the master index, this entry works as a pointer plus a "
           "summary. The live record index lives at %s as a gzipped JSONL "
           "light-row file (id, t, g per record); full records live in "
           "100-record gzipped chunks under %s. A client reads the light "
           "index to search titles, then fetches only the chunk holding a "
           "hit. The seeded key records below are the first titles of the "
           "live index, so this entry is useful even offline. Re-running the "
           "all-knowing build regenerates this entry deterministically from "
           "the manifest." % (idx, chunk_dir))
    points = [
        "Database slug: %s" % slug,
        "Records indexed: %s %s" % (f"{n:,}", kind),
        "Browse theme: %s (Signature knowledge-organization taxonomy)" % theme,
        "AI archivist: %s" % ai,
        "Generator: jahdb-%s-1.0 (boundless generator)" % slug,
        "Live index: %s" % idx,
        "Key records sampled: %d (titles below)" % len(key_recs),
    ]
    req = ("Python 3 standard library to run the embedded demonstration; a "
           "JSON reader for the gzipped chunks; network access for live "
           "index fetches (optional — the seeded key records work offline).")
    standards = [
        "Light rows carry id, t, g only; full records live in 100-record "
        "gzipped JSONL chunks.",
        "Record IDs are sequential within this edition (%s%06d-style) in "
        "manifest order — deterministic across rebuilds." % (PUBLIC_PREFIX, 1),
        "Titles are whole-system dedupe-gated before write "
        "(code/dedupe_gate.py).",
        "Every record carries a runnable stdlib demonstration program.",
    ]
    citations = [
        "JAH Databases manifest — data/manifest.json (registry source for "
        "this index).",
        "JAH Databases API — api.json (public index endpoint).",
    ]
    return {
        "id": rid, "t": title, "g": theme, "name": name, "title": title,
        "description": desc, "scope": scope, "how_it_works": hiw,
        "key_points": points, "requirements": req, "standards": standards,
        "citations": citations, "key_records": key_recs, "src": "public-harvest",
        "indexed_slug": slug, "indexed_records": n,
    }


def build_record_sig(entry, title, theme, key_recs, rid, theme_kws):
    name = entry["name"]
    slug = entry["slug"]
    n = entry.get("record_count", 0)
    kind = entry.get("record_kind") or "database record"
    tagline = entry.get("tagline") or ""
    ai = entry.get("ai_name") or "the database's archive AI"
    idx = entry.get("index") or entry.get("local_index") or ""
    desc = ("Signature original knowledge organization: the %s placed in the "
            "Signature framework — theme '%s', %s %s records, cross-referenced "
            "to the network. %s Designed in the Signature system as an "
            "original knowledge-organization record." % (name, theme, f"{n:,}",
                                                        kind, tagline))
    scope = ("Scope: the Signature-edition master-index record for %s (%s) — "
             "the same %s %s records as the public index entry, organized "
             "under the original Signature knowledge-organization framework: "
             "deterministic theme taxonomy, stable browse groups, and "
             "cross-theme references." % (name, slug, f"{n:,}", kind))
    hiw = ("The Signature framework works in three deterministic steps. "
           "First, every database slug maps to exactly one browse theme "
           "through the ordered theme taxonomy (%d themes; first keyword "
           "match wins; stable across rebuilds). Second, each theme becomes "
           "a browse group on the archive page, so the whole network is "
           "navigable by subject. Third, the live index at %s stays the "
           "source of truth for records — this entry never duplicates it, it "
           "organizes it. The embedded demonstration classifies this very "
           "record with the framework to prove the mapping." % (len(THEMES), idx))
    points = [
        "Database slug: %s" % slug,
        "Records indexed: %s %s" % (f"{n:,}", kind),
        "Signature theme: %s" % theme,
        "Framework: %d-theme deterministic taxonomy, ordered first-match" % len(THEMES),
        "AI archivist: %s" % ai,
        "Generator: jahdb-%s-1.0 (boundless generator)" % (slug + "-signature"),
        "Live index: %s" % idx,
        "Key records sampled: %d (titles below)" % len(key_recs),
    ]
    req = ("Python 3 standard library to run the embedded demonstration; a "
           "JSON reader for the gzipped chunks; network access for live "
           "index fetches (optional — the seeded key records work offline).")
    standards = [
        "Light rows carry id, t, g only; full records live in 100-record "
        "gzipped JSONL chunks.",
        "Record IDs are sequential within this edition (%s%06d-style) in "
        "manifest order — deterministic across rebuilds." % (SIG_PREFIX, 1),
        "Theme mapping is a pure function of the database slug — the same "
        "manifest always yields the same browse groups.",
        "Titles are whole-system dedupe-gated before write "
        "(code/dedupe_gate.py).",
    ]
    citations = [
        "JAH Databases manifest — data/manifest.json (registry source for "
        "this index).",
        "Signature knowledge-organization framework — original Signature "
        "design, defined by this database (code/all-knowing-build/themes.py).",
    ]
    return {
        "id": rid, "t": title, "g": theme, "name": name, "title": title,
        "description": desc, "scope": scope, "how_it_works": hiw,
        "key_points": points, "requirements": req, "standards": standards,
        "citations": citations, "key_records": key_recs, "src": "signature",
        "indexed_slug": slug, "indexed_records": n,
    }


def check_record(rec):
    for k in ("id", "t", "g", "name", "title", "description", "scope",
              "how_it_works", "key_points", "requirements", "standards",
              "src", "demo", "key_records"):
        assert k in rec, "missing %s in %s" % (k, rec["id"])
    assert len(rec["description"]) > 60, "stub in %s" % rec["id"]
    assert len(rec["scope"]) > 40, "stub scope in %s" % rec["id"]
    assert isinstance(rec["key_records"], list)
    prog = rec["demo"]["program"]
    assert prog
    compile(prog, rec["id"], "exec")
    blob = json.dumps(rec).lower()
    assert "facebook" not in blob, "facebook ref in %s" % rec["id"]
    assert "bat belt" not in blob, "banned phrase in %s" % rec["id"]


# ============================================================ shard writing

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
        write_gz_jsonl(
            os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
            recs[ci:ci + 100])
    return len(recs)


# ============================================================ page config

def _dbcfg(slug, name, tagline, record_kind, prefix, ai, role, hero_p,
           sig_type, source):
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role, "hero_p": hero_p,
        "sig_type": sig_type,
        "search_ph": "Search the master index of all databases...",
        "chat_ph": "Ask about any database in the network...",
        "archive_blurb": ("The master index of the JAH Databases network — "
                          "every database cross-referenced, marching with the "
                          "network toward one million records."),
        "schema": ("id, t, g, name, title, description, scope, how_it_works, "
                   "key_points, requirements, standards, citations, "
                   "key_records, src, demo"),
        "fields": "knowledge-organization themes",
        "gen_desc": ("Generate clearly-labeled structural sample index "
                     "records. Seeded archive records are the authoritative "
                     "entries."),
        "greet": "I am the %s. Ask me about any database in the network." % ai,
        "gen_fields": [t for t, _ in THEMES] + [FALLBACK],
        "gen_kind": slug, "gen_demo_kind": "python", "source": source,
    }


DBCFG = {
    PUBLIC_SLUG: _dbcfg(
        PUBLIC_SLUG,
        "The All-Knowing Databases Database",
        "The master omniscient index of the JAH Databases network — every "
        "database, its scope, record counts, and key records, cross-referenced.",
        "database index record", PUBLIC_PREFIX,
        "JAH All-Knowing Archivist",
        "all-knowing archivist — master index of every database",
        "The master index of the entire network: every database, its scope, "
        "record counts, key records, AI archivist, and generator — "
        "cross-referenced and searchable in one place. Every record carries "
        "the full entry: description, scope, how it works, key points, "
        "requirements, standards, citations, sampled key records, and a "
        "working demonstration program.",
        "Public records organized in the Signature system", "public"),
    SIG_SLUG: _dbcfg(
        SIG_SLUG,
        "The All-Knowing Databases Signature Database",
        "The Signature knowledge-organization framework for the entire "
        "network — the master index as an original Signature design.",
        "database index record", SIG_PREFIX,
        "JAH All-Knowing Archivist (Signature)",
        "all-knowing archivist — Signature knowledge-organization framework",
        "The Signature edition of the master index: his original "
        "knowledge-organization framework applied to the entire network — "
        "deterministic theme taxonomy, stable browse groups, and "
        "cross-theme references. Every record carries the full entry: "
        "description, scope, how it works, key points, requirements, "
        "standards, citations, sampled key records, and a working "
        "demonstration program.",
        "Signature originals organized in the Signature system", "signature"),
}


def manifest_entry(slug, n):
    c = DBCFG[slug]
    url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": url,
            "record_count": n, "status": "live",
            "index": url,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": c["source"]}


def api_entry(slug, n):
    c = DBCFG[slug]
    url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "record_count": n,
            "status": "live", "index": url}


def upsert_json_list(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    idx = {d["slug"]: i for i, d in enumerate(data["databases"])}
    for e in entries:
        if e["slug"] in idx:
            data["databases"][idx[e["slug"]]] = e
        else:
            data["databases"].append(e)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")

# ============================================================ main

def main():
    manifest = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    api = json.load(open(os.path.join(REPO, "api.json")))
    dbs = manifest["databases"]
    m_idx = {d["slug"]: d for d in dbs}
    print("manifest databases: %d" % len(dbs), flush=True)

    # ---- collision checks (slugs + ID prefixes)
    for s in (PUBLIC_SLUG, SIG_SLUG):
        if s in m_idx and m_idx[s].get("id_prefix") not in (PUBLIC_PREFIX, SIG_PREFIX):
            raise SystemExit("slug collision: %s already exists" % s)
    taken = {d.get("id_prefix") for d in dbs} - {PUBLIC_PREFIX, SIG_PREFIX}
    assert PUBLIC_PREFIX not in taken, "prefix taken: " + PUBLIC_PREFIX
    assert SIG_PREFIX not in taken, "prefix taken: " + SIG_PREFIX
    print("collisions: none (slugs + prefixes clear)", flush=True)

    # ---- resolve sample slice for demos
    samples = []
    for s in SAMPLE_SLUGS:
        e = m_idx.get(s)
        if e:
            samples.append((s, e["name"], theme_of(e),
                            e.get("record_count", 0),
                            e.get("record_kind") or "database record"))
    sample_themes = []
    for (s, _n, t, _c, _k) in samples:
        if t not in sample_themes:
            sample_themes.append(t)

    # ---- derive records deterministically from the manifest
    # Duplicate database names are disambiguated with the slug so every
    # database still becomes exactly one record per edition.
    name_counts = Counter(d["name"] for d in dbs)

    def disp_title(d, sig=False):
        t = d["name"]
        if name_counts[d["name"]] > 1:
            t += " [%s]" % d["slug"]
        return t + " (Signature Edition)" if sig else t

    ndup = sum(1 for d in dbs if name_counts[d["name"]] > 1)
    if ndup:
        print("duplicate names disambiguated: %d" % ndup, flush=True)

    pub_recs, sig_recs = [], []
    skipped_gate = 0
    for i, d in enumerate(dbs):
        theme = theme_of(d)
        slug = d["slug"]
        ipath = resolve_index(d)
        key_recs = sample_titles(ipath, N_KEY) if ipath else []
        title_p, title_s = disp_title(d), disp_title(d, True)
        # dedupe gate (whole-system, before write)
        for ver, ttl in (("public", title_p), ("signature", title_s)):
            hits = [h for h in GATE.check(
                PUBLIC_SLUG if ver == "public" else SIG_SLUG, ttl)]
            if hits:
                skipped_gate += 1
                print("  gate refused: %s (%s)" % (ttl, hits[0][0]), flush=True)
                break
        else:
            rid_p = "%s%06d" % (PUBLIC_PREFIX, len(pub_recs) + 1)
            rec_p = build_record_pub(d, title_p, theme, key_recs, rid_p)
            rec_p["demo"] = {"kind": "python", "language": "python",
                             "program": demo_lookup(
                                 title_p, rid_p, theme, slug, d["name"],
                                 d.get("record_count", 0),
                                 d.get("record_kind") or "database record",
                                 theme, samples),
                             "note": "Working demonstration program (real, "
                                     "runnable Python). Master-index lookup "
                                     "over a sample slice of the network."}
            check_record(rec_p)
            GATE.admit(PUBLIC_SLUG, title_p, rid_p)
            pub_recs.append(rec_p)

            rid_s = "%s%06d" % (SIG_PREFIX, len(sig_recs) + 1)
            theme_kws = next(kws for t, kws in THEMES if t == theme) \
                if theme != FALLBACK else set()
            extra = [(t, kws) for t, kws in THEMES if t in sample_themes]
            rec_s = build_record_sig(d, title_s, theme, key_recs, rid_s,
                                     theme_kws)
            rec_s["demo"] = {"kind": "python", "language": "python",
                             "program": demo_sigorg(
                                 title_s, rid_s, theme, slug, d["name"],
                                 theme, theme_kws, extra,
                                 [(s, t) for (s, _n, t, _c, _k) in samples]),
                             "note": "Working demonstration program (real, "
                                     "runnable Python). Signature "
                                     "knowledge-organization framework demo."}
            check_record(rec_s)
            GATE.admit(SIG_SLUG, title_s, rid_s)
            sig_recs.append(rec_s)
        if (i + 1) % 500 == 0:
            print("  derived %d/%d" % (i + 1, len(dbs)), flush=True)
    print("records: public=%d signature=%d gate-skipped=%d"
          % (len(pub_recs), len(sig_recs), skipped_gate), flush=True)
    assert len(pub_recs) == len(sig_recs) == len(dbs) - skipped_gate

    # ---- write shard data (full rewrite — regen-safe)
    for slug, recs in ((PUBLIC_SLUG, pub_recs), (SIG_SLUG, sig_recs)):
        n = write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # ---- execute a sample of demos (first/middle/last per edition)
    for label, recs in (("public", pub_recs), ("signature", sig_recs)):
        picks = [0, len(recs) // 2, len(recs) - 1]
        for pi in picks:
            r = recs[pi]
            p = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                               capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            print("demo ok: %-9s %s" % (label, r["id"]), flush=True)

    # ---- pages + generators (template family + sweep)
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    sweep_path = ("/home/hatch/workspace/goals/database-quality-audit/"
                  "hidden_files/patches/sweep-db-pages.py")
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)
    for slug, recs in ((PUBLIC_SLUG, pub_recs), (SIG_SLUG, sig_recs)):
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive "
            "records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover"
        assert "bat belt" not in page.lower(), "banned phrase in page"
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s — %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]"
              % (slug, slug, ",".join(notes)), flush=True)

    # ---- manifest + api.json upserts
    upsert_json_list(os.path.join(REPO, "data", "manifest.json"),
                     [manifest_entry(PUBLIC_SLUG, len(pub_recs)),
                      manifest_entry(SIG_SLUG, len(sig_recs))])
    upsert_json_list(os.path.join(REPO, "api.json"),
                     [api_entry(PUBLIC_SLUG, len(pub_recs)),
                      api_entry(SIG_SLUG, len(sig_recs))])
    print("manifest + api.json: upserted 2 databases (%d + %d records)"
          % (len(pub_recs), len(sig_recs)))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
