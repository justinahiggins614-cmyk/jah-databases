#!/usr/bin/env python3
"""PHASE E — "Everything <entity>" databases (20).

Builds one comprehensive entity archive per major organization/institution/
system, each seeded with 12 full records (8 public fact-checked + 4 Signature
editions) across the entity's branches as browse groups. Whole-system dedupe
via code/dedupe_gate.py. Canon page/chunk/index pattern from code/dbtype-build
(template page, gzipped index + chunks in jah-databases-data-1, unique ID
prefixes, manifest/api.json entries). No website references, no Facebook as a
source, no banned phrases.

Content-safety note: the historical company name "Facebook" appears in
everything-meta record titles/descriptions as fact-checked public history
(the company was Facebook, Inc. until October 2021). The standing rule bars
referencing the user's personal Facebook and citing Facebook as a source —
both remain enforced (no facebook.com URLs anywhere, no Facebook citations).
Historical intel agencies (KGB/CIA/FBI/MI6) are verified public history only:
scholarly tone, no tradecraft how-tos, no glorification.
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
from demos import DEMOS
from entries_e1 import ENTRIES_E1
from entries_e2 import ENTRIES_E2
from entries_e3 import ENTRIES_E3
from entries_e4 import ENTRIES_E4

# (slug, name, tagline, record_kind, prefix, ai_name, demo_key)
ENTITIES = [
    ("everything-apple", "The Everything Apple Database",
     "The complete Apple Inc. archive: founding history, landmark products, software and services, retail, and public filings — fact-checked public records plus Signature editions.",
     "apple record", "JAH-EVAP-", "JAH Everything Apple Archivist", "compare"),
    ("everything-nasa", "The Everything NASA Database",
     "The complete NASA archive: programs, landmark missions, field centers, astronauts, and science results — fact-checked public records plus Signature editions.",
     "nasa record", "JAH-EVNA-", "JAH Everything NASA Archivist", "orbit"),
    ("everything-kgb", "The Everything KGB Database",
     "The historical KGB archive: origins, Cold War history, declassified records, and legacy — verified public history in a scholarly tone, plus Signature editions.",
     "kgb history record", "JAH-EVKG-", "JAH Everything KGB Historian", "timeline"),
    ("everything-university", "The Everything University Database",
     "The complete university-system archive: major institutions, admissions, curricula, research, and campus life — per-institution public records plus Signature editions.",
     "university record", "JAH-EVUNI-", "JAH Everything University Archivist", "admissions"),
    ("everything-free-market", "The Everything Free Market Database",
     "The complete free-market archive: mechanisms, history, participants, and data — fact-checked public records plus Signature editions.",
     "free market record", "JAH-EVFM-", "JAH Everything Free Market Archivist", "equilibrium"),
    ("everything-esa", "The Everything ESA Database",
     "The complete European Space Agency archive: the agency, launchers, science missions, and exploration — fact-checked public records plus Signature editions.",
     "esa record", "JAH-EVESA-", "JAH Everything ESA Archivist", "orbit"),
    ("everything-spacex", "The Everything SpaceX Database",
     "The complete SpaceX archive: the company, launch vehicles, spacecraft, and constellations — fact-checked public records plus Signature editions.",
     "spacex record", "JAH-EVSX-", "JAH Everything SpaceX Archivist", "launch"),
    ("everything-roscosmos", "The Everything Roscosmos Database",
     "The complete Roscosmos archive: the agency, launchers, stations, and exploration — fact-checked public records plus Signature editions.",
     "roscosmos record", "JAH-EVRO-", "JAH Everything Roscosmos Archivist", "timeline"),
    ("everything-microsoft", "The Everything Microsoft Database",
     "The complete Microsoft archive: the company, software, cloud and gaming, and history — fact-checked public records plus Signature editions.",
     "microsoft record", "JAH-EVMS-", "JAH Everything Microsoft Archivist", "compare"),
    ("everything-google", "The Everything Google Database",
     "The complete Google archive: the company, search, products, and history — fact-checked public records plus Signature editions.",
     "google record", "JAH-EVGO-", "JAH Everything Google Archivist", "stats"),
    ("everything-meta", "The Everything Meta Database",
     "The complete Meta archive: the company, social platforms, hardware, and history — fact-checked public records plus Signature editions.",
     "meta record", "JAH-EVME-", "JAH Everything Meta Archivist", "stats"),
    ("everything-amazon", "The Everything Amazon Database",
     "The complete Amazon archive: the company, retail, cloud, and devices — fact-checked public records plus Signature editions.",
     "amazon record", "JAH-EVAMZ-", "JAH Everything Amazon Archivist", "growth"),
    ("everything-ibm", "The Everything IBM Database",
     "The complete IBM archive: the company, hardware, software, and history — fact-checked public records plus Signature editions.",
     "ibm record", "JAH-EVIBM-", "JAH Everything IBM Archivist", "timeline"),
    ("everything-cia", "The Everything CIA Database",
     "The historical CIA archive: origins, Cold War history, declassified records, and oversight — verified public history in a scholarly tone, plus Signature editions.",
     "cia history record", "JAH-EVCIA-", "JAH Everything CIA Historian", "archive"),
    ("everything-fbi", "The Everything FBI Database",
     "The historical FBI archive: origins, history, major investigations, and oversight — verified public history in a scholarly tone, plus Signature editions.",
     "fbi history record", "JAH-EVFBI-", "JAH Everything FBI Historian", "archive"),
    ("everything-mi6", "The Everything MI6 Database",
     "The historical MI6 archive: origins, history, declassified records, and legacy — verified public history in a scholarly tone, plus Signature editions.",
     "mi6 history record", "JAH-EVMI6-", "JAH Everything MI6 Historian", "timeline"),
    ("everything-united-nations", "The Everything United Nations Database",
     "The complete United Nations archive: the organization, principal organs, agencies, and history — fact-checked public records plus Signature editions.",
     "united nations record", "JAH-EVNAT-", "JAH Everything UN Archivist", "stats"),
    ("everything-who", "The Everything WHO Database",
     "The complete World Health Organization archive: the organization, programs, history, and global health work — fact-checked public records plus Signature editions.",
     "who record", "JAH-EVWHO-", "JAH Everything WHO Archivist", "growth"),
    ("everything-world-bank", "The Everything World Bank Database",
     "The complete World Bank archive: the organization, history, lending, and development work — fact-checked public records plus Signature editions.",
     "world bank record", "JAH-EVWB-", "JAH Everything World Bank Archivist", "rate"),
    ("everything-central-banks", "The Everything Central Banks Database",
     "The complete central-banking archive: the system, major institutions, policy tools, and history — fact-checked public records plus Signature editions.",
     "central bank record", "JAH-EVCB-", "JAH Everything Central Banks Archivist", "rate"),
]


def _cfg(slug, name, tagline, record_kind, prefix, ai, demo_key):
    role = "everything %s archivist — comprehensive entity archive" % record_kind.replace(" record", "")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s Every record carries the full entry: description, how it works, "
                   "key points, requirements, standards, citations, and a working demonstration program. "
                   "Public records carry fact-checked established knowledge; Signature editions carry "
                   "original Signature treatments." % tagline),
        "sig_type": "Public records and Signature originals organized in the Signature system",
        "search_ph": "Search %s..." % record_kind,
        "chat_ph": "Ask about %s..." % record_kind,
        "archive_blurb": "Seeded with 12 full %s across the entity's branches, marching toward one million records." % record_kind,
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "entity archive",
        "gen_desc": "Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about %s." % (ai, record_kind),
        "gen_fields": [],  # filled per-DB from record groups
        "gen_kind": slug, "gen_demo_kind": "python", "source": "public+signature",
    }


DBCFG = {s[0]: _cfg(*s) for s in ENTITIES}

# ============================================================ record assembly

def how_it_works_pub(name, desc, points):
    return ("In real-world study and practice, %s works as follows. %s The key ideas are: %s"
            % (name, desc, " ".join("%s." % p for p in points)))


def how_it_works_sig(name, desc, points):
    return ("The Signature edition of %s is an original Signature design: it specifies the record model, "
            "the working geometry, and the behavior as a complete, buildable design in the Signature system. "
            "%s The Signature design principles are: %s"
            % (name, desc, " ".join("%s." % p for p in points)))


def build_record(title, name, group, desc, points, req, standards, citations,
                 src, demo_kind, rid):
    if src == "signature":
        ftitle = title + " (Signature Edition)"
        description = ("Signature original: " + desc)
        hiw = how_it_works_sig(name, desc, points)
    else:
        ftitle = title
        description = desc
        hiw = how_it_works_pub(name, desc, points)
    rec = {
        "id": rid, "t": ftitle, "g": group, "name": name, "title": ftitle,
        "description": description, "how_it_works": hiw,
        "key_points": list(points), "requirements": req,
        "standards": list(standards), "citations": citations,
        "src": src,
    }
    prog = DEMOS[demo_kind](name, rid, group, points, req)
    rec["demo"] = {"kind": "python", "language": "python",
                   "program": prog,
                   "note": "Working demonstration program (real, runnable Python)."}
    return rec


def check_record(rec):
    for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
              "key_points", "requirements", "standards", "src", "demo"):
        assert k in rec, "missing %s in %s" % (k, rec["id"])
    assert len(rec["description"]) > 60, "stub in %s" % rec["id"]
    prog = rec["demo"]["program"]
    assert prog
    compile(prog, rec["id"], "exec")
    blob = json.dumps(rec).lower()
    # Standing rule, enforced precisely: no Facebook as a source, no facebook.com
    # links, no reference to the user's personal Facebook. The historical company
    # name "Facebook" in everything-meta record titles/descriptions is
    # fact-checked public history (the company was Facebook, Inc. until Oct 2021)
    # and is permitted there.
    assert "facebook.com" not in blob, "facebook URL in %s" % rec["id"]
    assert "facebook" not in rec["citations"].lower(), "facebook citation in %s" % rec["id"]
    assert "bat belt" not in blob, "banned phrase in %s" % rec["id"]


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
    return len(recs)


def update_json_list(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    have = {d["slug"] for d in data["databases"]}
    added = 0
    for e in entries:
        if e["slug"] not in have:
            data["databases"].append(e)
            added += 1
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")
    return added


def manifest_entry(slug, n):
    c = DBCFG[slug]
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": n, "status": "live", "full_records": n,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": c["source"]}


def api_entry(slug, n):
    c = DBCFG[slug]
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "record_count": n, "status": "live",
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"}


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    all_entries = ENTRIES_E1 + ENTRIES_E2 + ENTRIES_E3 + ENTRIES_E4
    assert len(all_entries) == 240, "expected 240 entries, got %d" % len(all_entries)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    # prefix collision check against the live manifest
    import json as _json
    man = _json.load(open(os.path.join(REPO, "data", "manifest.json")))
    used_pfx = {d.get("id_prefix", "") for d in man["databases"]} - {""}
    for slug, _n, _t, _rk, prefix, _ai, _dk in ENTITIES:
        bad = [p for p in used_pfx if p == prefix or p.startswith(prefix) or prefix.startswith(p)]
        assert not bad, "prefix collision for %s: %s" % (slug, bad)

    built = {}
    skipped = []
    for si, (slug, _n, _t, _rk, prefix, _ai, demo_key) in enumerate(ENTITIES):
        chunk = all_entries[si * 12:(si + 1) * 12]
        assert len(chunk) == 12, "short chunk for %s" % slug
        recs = []
        groups = []
        for (key, group, title, desc, points, req, standards, citations,
             dkind, src) in chunk:
            assert dkind == demo_key, "demo drift in %s: %s != %s" % (slug, dkind, demo_key)
            ftitle = title + " (Signature Edition)" if src == "signature" else title
            hits = [h for h in GATE.check(slug, ftitle) if h[0] != slug]
            if hits:
                skipped.append((slug, ftitle, hits))
                print("  gate refused (cross-db dupe): %s [%s]" % (ftitle, hits[0][0]), flush=True)
                continue
            rid = "%s%06d" % (prefix, len(recs) + 1)
            rec = build_record(title, title, group, desc, points, req, standards,
                               citations, src, dkind, rid)
            check_record(rec)
            GATE.admit(slug, ftitle, rid)
            recs.append(rec)
            if group not in groups:
                groups.append(group)
        assert recs, "empty db " + slug
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(prefix) for i in ids), "prefix drift in %s" % slug
        n_pub = sum(1 for r in recs if r["src"] == "public-harvest")
        n_sig = sum(1 for r in recs if r["src"] == "signature")
        print("built: %-36s %d records (%d public, %d signature)" % (slug, len(recs), n_pub, n_sig), flush=True)
        built[slug] = recs
        DBCFG[slug]["gen_fields"] = groups

    # ---- execute one demo per archetype
    markers = {"compare": "def compare_items(",
               "orbit": "def orbital_period_days(",
               "timeline": "def build_timeline(",
               "admissions": "def admission_model(",
               "equilibrium": "def market_equilibrium(",
               "launch": "def launch_cadence(",
               "stats": "def compute_stats(",
               "growth": "def compound_growth(",
               "archive": "def search_archive(",
               "rate": "def effective_rate("}
    done = set()
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            for k, m in markers.items():
                if k not in done and m in prog:
                    done.add(k)
                    p = subprocess.run([sys.executable, "-c", prog],
                                       capture_output=True, text=True, timeout=60)
                    assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
                    assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
                    print("demo ok: %-10s %s" % (k, r["id"]), flush=True)
    assert len(done) == len(markers), "not all archetypes executed: %s" % (set(markers) - done)
    print("demo execution: %d archetypes ran OK" % len(done), flush=True)

    # ---- shard data
    total = 0
    for slug, recs in built.items():
        n = write_shard_db(slug, recs)
        total += n
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # ---- pages + generators
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook.com" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
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
        assert "facebook.com" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ",".join(notes)), flush=True)

    entries_m = [manifest_entry(s, len(built[s])) for s in built]
    added_m = update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [api_entry(s, len(built[s])) for s in built]
    added_a = update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest: +%d, api.json: +%d, records: %d, gate-skipped: %d"
          % (added_m, added_a, total, len(skipped)))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
