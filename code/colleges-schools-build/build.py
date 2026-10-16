#!/usr/bin/env python3
"""PHASE J — education institutions databases.

Builds:
  everything-colleges        (50 per-institution records, JAH-EVCOL-)
  everything-public-schools  (48 district/school/program records, JAH-EVPBS-)

Canon: public records only, fact-checked from public sources. Record prose is
assembled ONLY from the structured fact dicts in entries_colleges.py /
entries_schools.py — no invented specifics. Enrollment figures are labeled
approximations from recent public reporting.

Pattern: template page + gzipped index/chunks in jah-databases-data-1, unique
ID prefixes collision-checked, manifest/api.json entries, whole-system dedupe
via code/dedupe_gate.py. .kv grids minmax(120px,1fr). No website references,
no Facebook, no banned phrases.
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
from entries_colleges import COLLEGES
from entries_schools import SCHOOLS

DBCFG = {
 "everything-colleges": {
  "name": "The Everything Colleges Database",
  "tagline": "The complete college archive: per-institution public records — history, campuses over time, publications, courses, admissions, and public data — fact-checked from public sources.",
  "record_kind": "college record", "prefix": "JAH-EVCOL-",
  "ai": "JAH Everything Colleges Archivist",
  "role": "everything colleges archivist — per-institution public records",
  "hero_p": ("The complete college archive: per-institution public records — history, campuses over time, "
             "publications, courses, admissions, and public data — fact-checked from public sources. "
             "Every record carries the full entry: description, campus history, key public facts, standards, "
             "citations, and a working demonstration program. Public records carry fact-checked established "
             "knowledge; figures are labeled approximations from recent public reporting."),
  "sig_type": "Public records organized in the Signature system",
  "search_ph": "Search colleges and universities...",
  "chat_ph": "Ask about colleges and universities...",
  "archive_blurb": "Seeded with 50 full per-institution college records across six world regions, marching toward one million records.",
  "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
  "fields": "institution archive",
  "gen_desc": "Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries.",
  "gen_fields": [],
  "gen_kind": "everything-colleges", "gen_demo_kind": "python", "source": "public",
  "greet": "I am the JAH Everything Colleges Archivist. Ask me about colleges and universities.",
 },
 "everything-public-schools": {
  "name": "The Everything Public Schools Database",
  "tagline": "The complete pre-college public-school archive: districts, historic high schools, magnet and specialized schools, and public programs — fact-checked public data with citations.",
  "record_kind": "public school record", "prefix": "JAH-EVPBS-",
  "ai": "JAH Everything Public Schools Archivist",
  "role": "everything public schools archivist — pre-college public records",
  "hero_p": ("The complete pre-college public-school archive: districts, historic high schools, magnet and "
             "specialized schools, and public programs — fact-checked public data with citations. "
             "Every record carries the full entry: description, public statistics, key public facts, standards, "
             "citations, and a working demonstration program. Figures are labeled approximations from recent "
             "public reporting."),
  "sig_type": "Public records organized in the Signature system",
  "search_ph": "Search public schools and districts...",
  "chat_ph": "Ask about public schools...",
  "archive_blurb": "Seeded with 48 full public-school records — major districts, historic high schools, magnet schools, and public programs — marching toward one million records.",
  "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
  "fields": "public-school archive",
  "gen_desc": "Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries.",
  "gen_fields": [],
  "gen_kind": "everything-public-schools", "gen_demo_kind": "python", "source": "public",
  "greet": "I am the JAH Everything Public Schools Archivist. Ask me about public schools.",
 },
}


def _year(s):
    m = re.match(r"(\d{3,4})", str(s))
    return int(m.group(1)) if m else 0


def _num(s):
    if not s:
        return None
    d = re.sub(r"[^\d]", "", str(s))
    return int(d) if d else None


def check_record(rec):
    for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
              "key_points", "requirements", "standards", "citations", "src", "demo"):
        assert k in rec, "missing %s in %s" % (k, rec["id"])
    assert len(rec["description"]) > 60, "stub in %s" % rec["id"]
    assert len(rec["how_it_works"]) > 60, "stub hiw in %s" % rec["id"]
    assert rec["src"] == "public-harvest", "src drift in %s" % rec["id"]
    prog = rec["demo"]["program"]
    assert prog
    compile(prog, rec["id"], "exec")
    blob = json.dumps(rec).lower()
    assert "facebook.com" not in blob, "facebook URL in %s" % rec["id"]
    assert "facebook" not in rec["citations"].lower(), "facebook citation in %s" % rec["id"]
    assert "bat belt" not in blob, "banned phrase in %s" % rec["id"]


def build_college(e, rid):
    title, name, group = e["title"], e["name"], e["group"]
    desc = "%s is a %s in %s, founded in %s." % (name, e["type_desc"], e["location"], e["founded"])
    if e.get("founded_note"):
        n = e["founded_note"]
        desc += " " + n[0].upper() + n[1:] + "."
    if e.get("enrollment"):
        desc += " Recent public reporting puts total enrollment at %s." % e["enrollment"]
    if e.get("programs"):
        desc += " Its schools and programs include %s." % "; ".join(e["programs"])
    if e.get("press"):
        desc += " Its publishing arm is %s." % e["press"]
    hiw = "Campuses over time. " + " ".join(e["campuses"])
    hiw += " Publications and press."
    if e.get("press"):
        hiw += " The university press is %s." % e["press"]
    if e.get("publications"):
        hiw += " Notable publications include %s." % "; ".join(e["publications"])
    hiw += " Programs and courses. %s offers %s." % (name, "; ".join(e["programs"]))
    hiw += " Admissions. %s" % e["admissions"]
    kp = ["Founded: %s." % e["founded"]]
    if e.get("enrollment"):
        kp.append("Enrollment: %s (recent public reporting; figures vary by year and source)." % e["enrollment"])
    kp.append("Location: %s." % e["location"])
    kp.append("Campus history: %d described campus sites, from the historic core to modern expansions." % len(e["campuses"]))
    if e.get("press"):
        kp.append("Press: %s." % e["press"])
    kp.extend(e["facts"])
    req = ("Admission and study requirements (public data): %s "
           "Prospective students should consult the institution's published admission requirements." % e["admissions"])
    rec = {"id": rid, "t": title, "g": group, "name": name, "title": title,
           "description": desc, "how_it_works": hiw, "key_points": kp,
           "requirements": req, "standards": [e["accreditation"], "ISO 8601 (dates)"],
           "citations": e["citations"], "src": "public-harvest"}
    rec["demo"] = {"kind": "python", "language": "python",
                   "program": DEMOS["profile"](name, rid, group, _year(e["founded"]),
                                               len(e["campuses"]), e["enrollment_num"]),
                   "note": "Working demonstration program (real, runnable Python)."}
    return rec


def build_school(e, rid):
    title, name, group, kind = e["title"], e["name"], e["group"], e["kind"]
    if kind == "program":
        desc = ("%s is a public education program in %s, established in %s. %s. "
                % (name, e["location"], e["established"], e["scope"]))
        desc += "Its components include %s." % "; ".join(e["programs"])
        hiw = ("Program history. %s was established in %s (%s). How it works. %s. "
               "Reach. %s."
               % (name, e["established"], e.get("established_note", ""), " ".join(e["programs"]), e["scope"]))
        kp = ["Established: %s." % e["established"], "Scope: %s." % e["scope"]]
        kp.extend(e["stats"])
        kp.extend(e["facts"])
        req = ("Participation requirements (public data): eligibility follows the program's published rules; "
               "consult the administering agency's public guidance.")
        standards = ["Federal program statute and regulation (public)", "NCES reporting definitions"]
        enroll, schools_n = None, None
    else:
        what = {"district": "public school district", "highschool": "public high school",
                "magnet": "public magnet school"}[kind]
        desc = "%s is a %s in %s, established in %s." % (name, what, e["location"], e["established"])
        if e.get("established_note"):
            n = e["established_note"]
            desc += " " + n[0].upper() + n[1:] + "."
        desc += " It serves %s." % e["grades"]
        if e.get("enrollment"):
            desc += " Recent public reporting puts enrollment at %s." % e["enrollment"]
        if e.get("schools_count"):
            desc += " The district operates %s." % e["schools_count"]
        if e.get("programs"):
            desc += " Programs include %s." % "; ".join(e["programs"])
        hiw = "Public record. " + " ".join(e["stats"]) + "."
        hiw += " Programs. %s offers %s." % (name, "; ".join(e["programs"]))
        hiw += " Public statistics. " + " ".join(e["stats"]) + "."
        kp = ["Established: %s." % e["established"], "Location: %s." % e["location"],
              "Grades: %s." % e["grades"]]
        if e.get("enrollment"):
            kp.append("Enrollment: %s (recent public reporting; figures vary by year and source)." % e["enrollment"])
        if e.get("schools_count"):
            kp.append("Schools: %s." % e["schools_count"])
        kp.extend(e["stats"])
        kp.extend(e["facts"])
        if kind == "district":
            req = ("Enrollment requirements (public data): public school enrollment is open to resident students; "
                   "attendance follows district zoning and state law. Consult the district's published enrollment guidance.")
        else:
            req = ("Admission requirements (public data): %s. Consult the school's published admission criteria."
                   % e["stats"][1] if len(e["stats"]) > 1 else "See published criteria.")
        standards = ["State academic standards (public)", "NCES Common Core of Data (reporting)"]
        enroll, schools_n = e.get("enrollment_num"), _num(e.get("schools_count"))
    rec = {"id": rid, "t": title, "g": group, "name": name, "title": title,
           "description": desc, "how_it_works": hiw, "key_points": kp,
           "requirements": req, "standards": standards,
           "citations": e["citations"], "src": "public-harvest"}
    rec["demo"] = {"kind": "python", "language": "python",
                   "program": DEMOS["stats"](name, rid, group, _year(e["established"]), enroll, schools_n),
                   "note": "Working demonstration program (real, runnable Python)."}
    return rec


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

    # ---- re-verify manifest at start
    man = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    print("manifest databases at start: %d" % len(man["databases"]), flush=True)
    used_slugs = {d["slug"] for d in man["databases"]}
    used_pfx = {d.get("id_prefix", "") for d in man["databases"]} - {""}
    for slug in DBCFG:
        assert slug not in used_slugs, "slug taken: " + slug
        pfx = DBCFG[slug]["prefix"]
        bad = [p for p in used_pfx if p == pfx or p.startswith(pfx) or pfx.startswith(p)]
        assert not bad, "prefix collision for %s: %s" % (slug, bad)
    print("slug + prefix checks OK", flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    plan = [("everything-colleges", COLLEGES, build_college),
            ("everything-public-schools", SCHOOLS, build_school)]
    built, skipped = {}, []
    for slug, entries, builder in plan:
        prefix = DBCFG[slug]["prefix"]
        recs, groups = [], []
        for e in entries:
            hits = [h for h in GATE.check(slug, e["title"]) if h[0] != slug]
            if hits:
                skipped.append((slug, e["title"], hits))
                print("  gate refused (cross-db dupe): %s [%s]" % (e["title"], hits[0][0]), flush=True)
                continue
            rid = "%s%06d" % (prefix, len(recs) + 1)
            rec = builder(e, rid)
            check_record(rec)
            GATE.admit(slug, e["title"], rid)
            recs.append(rec)
            if e["group"] not in groups:
                groups.append(e["group"])
        assert recs, "empty db " + slug
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(prefix) for i in ids), "prefix drift in %s" % slug
        n_pub = sum(1 for r in recs if r["src"] == "public-harvest")
        print("built: %-28s %d records (%d public)" % (slug, len(recs), n_pub), flush=True)
        built[slug] = recs
        DBCFG[slug]["gen_fields"] = groups

    # ---- execute one demo per archetype
    done = set()
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            key = "profile" if "def institution_age(" in prog else "stats"
            if key not in done:
                done.add(key)
                p = subprocess.run([sys.executable, "-c", prog],
                                   capture_output=True, text=True, timeout=60)
                assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
                assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
                print("demo ok: %-10s %s" % (key, r["id"]), flush=True)
    assert done == {"profile", "stats"}, "archetype missing: %s" % done

    # ---- shard data
    total = 0
    for slug, recs in built.items():
        n = write_shard_db(slug, recs)
        total += n
        print("shard: %-28s %d records" % (slug, n), flush=True)

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
          % (added_m, added_a, total, len(skipped)), flush=True)
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
