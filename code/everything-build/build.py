#!/usr/bin/env python3
"""PHASE D — "Everything" subject databases (20).

Builds one comprehensive subject archive per major subject, each seeded with
12 full records (8 public fact-checked + 4 Signature editions) across the
subject's branches as browse groups. Whole-system dedupe via
code/dedupe_gate.py. Canon page/chunk/index pattern from code/dbtype-build
(template page, gzipped index + chunks in jah-databases-data-1, unique ID
prefixes, manifest/api.json entries). No website references, no Facebook,
no banned phrases.
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
from entries_a import ENTRIES_A
from entries_b import ENTRIES_B
from entries_c import ENTRIES_C
from entries_d import ENTRIES_D

# (slug, name, tagline, record_kind, prefix, ai_name, demo_key)
SUBJECTS = [
    ("everything-mathematics", "The Everything Mathematics Database",
     "The complete mathematics archive: foundations, algebra, geometry, calculus, probability, and number theory — plus Signature editions.",
     "mathematics record", "JAH-EVM-", "JAH Everything Mathematics Archivist", "math"),
    ("everything-physics", "The Everything Physics Database",
     "The complete physics archive: mechanics, electromagnetism, thermodynamics, relativity, quantum physics, and fluids — plus Signature editions.",
     "physics record", "JAH-EVP-", "JAH Everything Physics Archivist", "physics"),
    ("everything-chemistry", "The Everything Chemistry Database",
     "The complete chemistry archive: general, organic, physical chemistry, and biochemistry — plus Signature editions.",
     "chemistry record", "JAH-EVC-", "JAH Everything Chemistry Archivist", "chem"),
    ("everything-biology", "The Everything Biology Database",
     "The complete biology archive: cells, genetics, evolution, ecology, human biology, microbiology, and botany — plus Signature editions.",
     "biology record", "JAH-EVB-", "JAH Everything Biology Archivist", "bio"),
    ("everything-computer-science", "The Everything Computer Science Database",
     "The complete computer science archive: foundations, algorithms, theory, systems, and security — plus Signature editions.",
     "computer science record", "JAH-EVCS-", "JAH Everything Computer Science Archivist", "cs"),
    ("everything-engineering", "The Everything Engineering Database",
     "The complete engineering archive: mechanical, electrical, civil, and design practice — plus Signature editions.",
     "engineering record", "JAH-EVE-", "JAH Everything Engineering Archivist", "eng"),
    ("everything-medicine-health", "The Everything Medicine and Health Database",
     "The complete medicine and health archive: anatomy, physiology, clinical knowledge, wellness, and public health — plus Signature editions.",
     "medicine and health record", "JAH-EVMH-", "JAH Everything Medicine and Health Archivist", "med"),
    ("everything-earth-science", "The Everything Earth Science Database",
     "The complete earth science archive: geology, meteorology, hydrology, oceanography, and hazards — plus Signature editions.",
     "earth science record", "JAH-EVES-", "JAH Everything Earth Science Archivist", "earth"),
    ("everything-astronomy-space", "The Everything Astronomy and Space Database",
     "The complete astronomy and space archive: solar system, stars, cosmology, observation, and spaceflight — plus Signature editions.",
     "astronomy and space record", "JAH-EVAS-", "JAH Everything Astronomy and Space Archivist", "astro"),
    ("everything-economics-finance", "The Everything Economics and Finance Database",
     "The complete economics and finance archive: micro, macro, personal finance, investing, banking, and trade — plus Signature editions.",
     "economics and finance record", "JAH-EVEF-", "JAH Everything Economics and Finance Archivist", "econ"),
    ("everything-psychology", "The Everything Psychology Database",
     "The complete psychology archive: cognitive, developmental, social, personality, clinical, behavioral, and biological — plus Signature editions.",
     "psychology record", "JAH-EVPS-", "JAH Everything Psychology Archivist", "psych"),
    ("everything-history", "The Everything History Database",
     "The complete history archive: ancient, medieval, early modern, modern, and contemporary eras — plus Signature editions.",
     "history record", "JAH-EVH-", "JAH Everything History Archivist", "hist"),
    ("everything-geography", "The Everything Geography Database",
     "The complete geography archive: physical and human geography, cartography, and biogeography — plus Signature editions.",
     "geography record", "JAH-EVG-", "JAH Everything Geography Archivist", "geo"),
    ("everything-law", "The Everything Law Database",
     "The complete law archive: public, criminal, civil law, and legal practice — plus Signature editions. Educational reference.",
     "law record", "JAH-EVL-", "JAH Everything Law Archivist", "law"),
    ("everything-philosophy", "The Everything Philosophy Database",
     "The complete philosophy archive: logic, ethics, metaphysics, epistemology, and value theory — plus Signature editions. Scholarly throughout.",
     "philosophy record", "JAH-EVPH-", "JAH Everything Philosophy Archivist", "phil"),
    ("everything-linguistics-language", "The Everything Linguistics and Language Database",
     "The complete linguistics archive: phonetics, phonology, morphology, syntax, semantics, acquisition, and sociolinguistics — plus Signature editions.",
     "linguistics record", "JAH-EVLL-", "JAH Everything Linguistics and Language Archivist", "ling"),
    ("everything-art-music", "The Everything Art and Music Database",
     "The complete art and music archive: visual art fundamentals, art history, music theory, and music history — plus Signature editions.",
     "art and music record", "JAH-EVAM-", "JAH Everything Art and Music Archivist", "artmusic"),
    ("everything-education", "The Everything Education Database",
     "The complete education archive: learning science, teaching, literacy, and educational technology — plus Signature editions.",
     "education record", "JAH-EVED-", "JAH Everything Education Archivist", "edu"),
    ("everything-agriculture-food", "The Everything Agriculture and Food Database",
     "The complete agriculture and food archive: agronomy, livestock, crop protection, food science, and farm business — plus Signature editions.",
     "agriculture and food record", "JAH-EVAF-", "JAH Everything Agriculture and Food Archivist", "agri"),
    ("everything-energy", "The Everything Energy Database",
     "The complete energy archive: fundamentals, sources, renewables, the grid, and efficiency — plus Signature editions.",
     "energy record", "JAH-EVEN-", "JAH Everything Energy Archivist", "energy"),
]


def _cfg(slug, name, tagline, record_kind, prefix, ai, demo_key):
    role = "everything %s archivist — comprehensive subject archive" % record_kind.replace(" record", "")
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
        "archive_blurb": "Seeded with 12 full %s across the subject's branches, marching toward one million records." % record_kind,
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "subject archive",
        "gen_desc": "Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about %s." % (ai, record_kind),
        "gen_fields": [],  # filled per-DB from record groups
        "gen_kind": slug, "gen_demo_kind": "python", "source": "public+signature",
    }


DBCFG = {s[0]: _cfg(*s) for s in SUBJECTS}

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
    assert "facebook" not in blob, "facebook ref in %s" % rec["id"]
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

    all_entries = ENTRIES_A + ENTRIES_B + ENTRIES_C + ENTRIES_D
    assert len(all_entries) == 240, "expected 240 entries, got %d" % len(all_entries)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    built = {}
    skipped = []
    for si, (slug, _n, _t, _rk, prefix, _ai, demo_key) in enumerate(SUBJECTS):
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
    markers = {"math": "solve_quadratic(", "physics": "projectile_range(",
               "chem": "molar_mass(", "bio": "gc_content(", "cs": "quicksort(",
               "eng": "cantilever_deflection(", "med": "bmi(",
               "earth": "haversine_km(", "astro": "orbital_period_days(",
               "econ": "compound(", "psych": "statistics.stdev(",
               "hist": "span_years(", "geo": "population_density(",
               "law": "add_business_days(", "phil": "def entails(",
               "ling": "flesch_kincaid_grade(", "artmusic": "major_scale(",
               "edu": "weighted_grade(", "agri": "yield_estimate(",
               "energy": "electricity_cost("}
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
    added_m = update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [api_entry(s, len(built[s])) for s in built]
    added_a = update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest: +%d, api.json: +%d, records: %d, gate-skipped: %d"
          % (added_m, added_a, total, len(skipped)))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
