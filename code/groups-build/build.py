#!/usr/bin/env python3
"""PHASE I — Groups of every kind: 14 categories x (public + signature) = 28 DBs.

- Builds 28 new group databases from ENTRIES (no covering DBs exist; nothing filed).
- Each entry seeds both a public-harvest record and a Signature-edition record.
- Whole-system dedupe via code/dedupe_gate.py. Canon page/chunk/index pattern.
- No website references, no Facebook, no banned phrases. Neutral/scholarly tone.
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

sys.path.insert(0, os.path.join(REPO, "code", "dbtype-build"))
spec_db = importlib.util.spec_from_file_location(
    "dbtype_build", os.path.join(REPO, "code", "dbtype-build", "build.py"))
dbt = importlib.util.module_from_spec(spec_db)
spec_db.loader.exec_module(dbt)
build_record = dbt.build_record
check_record = dbt.check_record
DEMOS = dbt.DEMOS
write_gz_jsonl = dbt.write_gz_jsonl

sys.path.insert(0, HERE)
_spec_e = importlib.util.spec_from_file_location(
    "groups_entries", os.path.join(HERE, "entries.py"))
_mod_e = importlib.util.module_from_spec(_spec_e)
_spec_e.loader.exec_module(_mod_e)
ENTRIES = _mod_e.ENTRIES

# (cat, slug, name, tagline, record_kind, prefix, ai, role, citation)
CATS = [
    ("social", "social-groups", "The Social Groups Database",
     "Civic and service clubs, fellowship circles, and social organizations: how groups gather, serve, and endure.",
     "social group record", "JAH-SOG-", "JAH Social Groups Archivist",
     "social groups archivist — service clubs and fellowship organizations",
     "Organizational studies (public organizational records)."),
    ("prof", "professional-associations", "The Professional Associations Database",
     "Professional bodies and trade associations: standards, certification, advocacy, and the professions they organize.",
     "professional association record", "JAH-PAF-", "JAH Professional Associations Archivist",
     "professional associations archivist — standards and certification bodies",
     "Organizational studies (public organizational records)."),
    ("hobby", "hobby-clubs", "The Hobby Clubs Database",
     "Hobby and enthusiast clubs: radio, railroads, orchids, astronomy, crafts, and the joy of shared obsession.",
     "hobby club record", "JAH-HBC-", "JAH Hobby Clubs Archivist",
     "hobby clubs archivist — enthusiast and collector organizations",
     "Organizational studies (public organizational records)."),
    ("relig", "religious-congregations", "The Religious Congregations Database",
     "Congregations and worshipping communities across traditions, described scholarly: structure, practice, and governance.",
     "religious congregation record", "JAH-RLC-", "JAH Religious Congregations Archivist",
     "religious congregations archivist — scholarly congregational studies",
     "Religious studies (scholarly congregational literature)."),
    ("sports", "sports-teams", "The Sports Teams Database",
     "Sports clubs and franchises: rosters, stadiums, championships, and how teams are built and run.",
     "sports team record", "JAH-SPT-", "JAH Sports Teams Archivist",
     "sports teams archivist — clubs, franchises, and team organization",
     "Sports studies (public team records)."),
    ("acad", "academic-cohorts", "The Academic Cohorts Database",
     "Scholarship cohorts, graduating classes, and academic honor groups: how cohorts form and what they become.",
     "academic cohort record", "JAH-ACC-", "JAH Academic Cohorts Archivist",
     "academic cohorts archivist — scholarship and class cohorts",
     "Educational studies (public cohort records)."),
    ("online", "online-communities", "The Online Communities Database",
     "Digital communities: forums, wikis, open-source collectives, and the norms that govern them.",
     "online community record", "JAH-ONC-", "JAH Online Communities Archivist",
     "online communities archivist — digital collective governance",
     "Community studies (public community records)."),
    ("support", "support-groups", "The Support Groups Database",
     "Mutual-aid and support fellowships: recovery, grief, caregiving, and peer-led healing.",
     "support group record", "JAH-SPG-", "JAH Support Groups Archivist",
     "support groups archivist — mutual-aid and recovery fellowships",
     "Support studies (public organizational records)."),
    ("polit", "political-organizations", "The Political Organizations Database",
     "Parties, committees, think tanks, and civic bodies — described factually and neutrally, never endorsed or attacked.",
     "political organization record", "JAH-PLG-", "JAH Political Organizations Archivist",
     "political organizations archivist — neutral civic documentation",
     "Civic studies (public organizational records; described neutrally)."),
    ("volun", "volunteer-orgs", "The Volunteer Organizations Database",
     "Volunteer service organizations: disaster relief, mentoring, building, and the logistics of goodwill.",
     "volunteer organization record", "JAH-VLO-", "JAH Volunteer Organizations Archivist",
     "volunteer organizations archivist — service and relief organizations",
     "Volunteer studies (public organizational records)."),
    ("union", "unions-guilds", "The Labor Unions and Trade Guilds Database",
     "Labor unions and trade guilds: bargaining, contracts, strikes, and the craft traditions behind them.",
     "union and guild record", "JAH-UUG-", "JAH Unions and Guilds Archivist",
     "unions and guilds archivist — labor and craft organizations",
     "Labor studies (public organizational records)."),
    ("frat", "fraternal-societies", "The Fraternal Societies Database",
     "Fraternal orders and Greek-letter societies: ritual, charity, and brotherhood and sisterhood traditions.",
     "fraternal society record", "JAH-FRT-", "JAH Fraternal Societies Archivist",
     "fraternal societies archivist — fraternal orders and Greek-letter organizations",
     "Fraternal studies (public organizational records)."),
    ("neigh", "neighborhood-associations", "The Neighborhood Associations Database",
     "Block-level and neighborhood bodies: HOAs, watch programs, garden associations, and tenant groups.",
     "neighborhood association record", "JAH-NBA-", "JAH Neighborhood Associations Archivist",
     "neighborhood associations archivist — community-level organizations",
     "Community studies (public organizational records)."),
    ("advoc", "advocacy-groups", "The Advocacy Groups Database",
     "Advocacy and cause organizations across the spectrum — described factually and neutrally.",
     "advocacy group record", "JAH-ADG-", "JAH Advocacy Groups Archivist",
     "advocacy groups archivist — neutral cause-organization documentation",
     "Advocacy studies (public organizational records; described neutrally)."),
]

SIG_PREFIX = {"social": "JAH-SOGG-", "prof": "JAH-PAFG-", "hobby": "JAH-HBCG-",
              "relig": "JAH-RLCG-", "sports": "JAH-SPTG-", "acad": "JAH-ACCG-",
              "online": "JAH-ONCG-", "support": "JAH-SPGG-", "polit": "JAH-PLGG-",
              "volun": "JAH-VLOG-", "union": "JAH-UUGG-", "frat": "JAH-FRTG-",
              "neigh": "JAH-NBAG-", "advoc": "JAH-ADGG-"}


def _cfg(cat, slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig = source == "signature"
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s — %s Every record carries the full entry: description, how it works, "
                   "key points, requirements, standards, citations, and a working demonstration program."
                   % (tagline,
                      "Signature originals — original Signature group-organization designs."
                      if sig else
                      "Public records — real-world groups documented factually.")),
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else "Public records organized in the Signature system"),
        "search_ph": "Search %s..." % record_kind,
        "chat_ph": "Ask about %s..." % record_kind,
        "archive_blurb": "Seeded %s %s, marching toward one million records." % (
            "Signature-original" if sig else "public-record", record_kind),
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "group-kind catalog",
        "gen_desc": ("Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries."),
        "greet": "I am the %s. Ask me about %s." % (ai, record_kind),
        "gen_fields": ["group-kind catalog"], "gen_kind": slug,
        "gen_demo_kind": "python", "source": source,
    }


DBCFG = {}
CIT = {}
for (cat, slug, name, tagline, rk, prefix, ai, role, citation) in CATS:
    DBCFG[slug] = _cfg(cat, slug, name, tagline, rk, prefix, ai, role, citation, "public")
    CIT[slug] = citation
    sslug = slug + "-signature"
    DBCFG[sslug] = _cfg(cat, sslug, name.replace(" Database", " Signature Database"),
                        tagline, rk, SIG_PREFIX[cat], ai + " (Signature)",
                        role + " — Signature editions", citation, "signature")
    CIT[sslug] = citation + " Signature editions are original Signature group-organization designs."


def build_new_records():
    built = {}
    for (cat, slug, _n, _t, _rk, _p, _a, _r, _c) in CATS:
        for ver in ("public", "signature"):
            s = slug if ver == "public" else slug + "-signature"
            cfg = DBCFG[s]
            src = "signature" if ver == "signature" else "public-harvest"
            recs = []
            for (key, ecat, title, desc, points, req, standards, citations,
                 demo_kind, target) in ENTRIES:
                if ecat != cat or target:
                    continue
                ftitle = title + " (Signature Edition)" if ver == "signature" else title
                if [h for h in GATE.check(s, ftitle) if h[0] != s]:
                    print("  gate refused (cross-db dupe): %s" % ftitle, flush=True)
                    continue
                rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
                rec = build_record(title, title, key, desc, points, req, standards,
                                   CIT[s], src, demo_kind, rid)
                check_record(rec)
                GATE.admit(s, ftitle, rid)
                recs.append(rec)
            assert recs, "empty db " + s
            built[s] = recs
    return built


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
    for e in entries:
        if e["slug"] not in have:
            data["databases"].append(e)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")


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

    assert len(ENTRIES) == 98, "expected 98 entries, got %d" % len(ENTRIES)

    # ---- step 1: build seed records
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

    # ---- step 2: execute one demo per archetype used
    markers = {"report": "INFO = {", "stats": "statistics.median",
               "text": "most_common(5)", "pipeline": "def clean(rec)"}
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

    # ---- step 3: pages + generators
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
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s — %s" % (r["t"], r["g"]))
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
