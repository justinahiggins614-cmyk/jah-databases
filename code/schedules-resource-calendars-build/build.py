#!/usr/bin/env python3
"""Build the Schedules and Resource Calendars databases for JAH Databases
(missing-115, Wave 1 - operational data, Manon's #1 priority).

Item 50 of ~/workspace/hidden_files/catalog-missing-categories-115.txt:
appointments, equipment availability, personnel shifts, facilities, and
maintenance windows - scheduling algorithms, shift-rotation rules, constraint
satisfaction, calendar data models, recurrence rules, time-zone handling, and
resource conflict resolution.

Verified 2026-10-17 (missing-115 Wave 1): RAW SWEEP over the full manifest
(2,390 databases) PLUS every shard index in jah-databases-data-1: zero
'schedules-resource-calendars*' slugs/names; zero title collisions on the 34
record titles. ID prefixes JAH-SCH- (public) and JAH-SCHS- (signature)
verified free in the manifest id_prefix values and in every shard index
file (zero hits). Dedupe gate run over all 68 titles before authoring:
zero collisions, zero refusals.

So this build creates two NEW databases, 34 ladder-ordered records each:

  schedules-resource-calendars            - The Schedules and Resource
                                            Calendars Database
                                            (public-harvest: real,
                                            fact-checked scheduling science;
                                            standard references RFC 5545
                                            iCalendar, RFC 5546 iTIP,
                                            RFC 4791 CalDAV, RFC 6352
                                            CardDAV, RFC 5905 NTP, ISO
                                            8601:2019, the IANA time zone
                                            database, Pinedo Scheduling 6th
                                            ed 2022, Garey and Johnson 1979,
                                            Kelley and Walker 1959, Malcolm
                                            et al 1959, Kuhn 1955, Munkres
                                            1957, Little 1961, Kleinrock
                                            1975, Lamport 1978, Graham et al
                                            1979, de Werra 1985, Moubray
                                            1997, ISO 55000:2024, NIOSH
                                            shiftwork guidance, Czeisler et
                                            al 1982, Gantt 1913, Goldratt
                                            The Goal, PMBOK Guide 7th ed,
                                            ITIL 4, Liu and Layland 1973)
  schedules-resource-calendars-signature  - The Schedules and Resource
                                            Calendars Signature Database
                                            (his original Signature
                                            Scheduling Method: every slot a
                                            covenant of time, the calendar
                                            the ledger of kept promises;
                                            src signature, titles suffixed
                                            " (Signature Edition)", never
                                            presented as authentic public
                                            record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes. A merger handles those. Outputs are only the allowed new untracked
paths: db/schedules-resource-calendars[/-signature]/ (index.html +
gen-*.js), shard data under jah-databases-data-1, and the merger fragment.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian operational scope only.
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/schedules-resource-calendars.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_schedules_resource_calendars import ENTRIES, SIG_TAIL
from demos_schedules_resource_calendars import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Scheduling "
                "Method: every slot a covenant of time, the calendar the "
                "ledger of kept promises, rotation the rhythm, conflict the "
                "broken oath, the maintenance window the honored rest. "
                "Clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked scheduling science: "
                "appointments, equipment availability, personnel shifts, "
                "facilities, and maintenance windows; calendar data models, "
                "recurrence rules, time-zone handling, scheduling algorithms, "
                "shift-rotation rules, constraint satisfaction, and resource "
                "conflict resolution - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a schedule is, calendar data models, time duration and "
              "intervals, recurrence rules, time zones, appointments, "
              "personnel shifts, equipment availability, facilities, "
              "maintenance windows, iCalendar RFC 5545) -> Compounded "
              "(conflict detection, constraint satisfaction, shift-rotation "
              "rules, scheduling algorithms, resource allocation, queueing "
              "theory, buffers, multi-resource scheduling, synchronization, "
              "preventive maintenance, downtime SLAs, stochastic models) -> "
              "Advanced (linear programming, timetabling, job-shop, "
              "real-time deadlines, distributed consensus, fairness, MRP, "
              "predictive maintenance, system architecture, audit, the "
              "operating picture).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search appointments, shifts, rotations, equipment, rooms, maintenance windows, RRULE, time zones, iCalendar, conflicts, constraints, Hungarian, queueing, MRP...",
        "chat_ph": "Ask about schedules and resource calendars...",
        "archive_blurb": ("Seeded %s schedule and calendar records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled scheduling studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about schedules and resource calendars - from what a schedule is through data models, intervals, recurrence, time zones, appointments, shifts, equipment, facilities, maintenance windows, and iCalendar, through conflict detection, constraints, rotation rules, algorithms, allocation, queueing, buffers, multi-resource bundles, sync, preventive maintenance, SLAs, and stochastic models, to linear programming, timetabling, job shops, real-time deadlines, distributed consensus, fairness, MRP, predictive maintenance, architecture, audit, and the operating picture." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "scheduling-study", "gen_demo_kind": "scheduling-demo",
        "source": source,
    }

CIT_PUB = ("Scheduling science (standard references: Desruisseaux B (Ed.). "
           "RFC 5545. Internet Calendaring and Scheduling Core Object "
           "Specification (iCalendar); September 2009; Daboo C. RFC 5546. "
           "iTIP; 2009; Daboo C, Desruisseaux B, Dusseault L. RFC 4791. "
           "CalDAV; 2007; Daboo C. RFC 6352. CardDAV; 2011; Mills D et al. "
           "RFC 5905. NTP version 4; 2010; ISO 8601:2019; IANA Time Zone "
           "Database; Pinedo ML. Scheduling: Theory, Algorithms, and "
           "Systems. 6th ed. Springer; 2022; Garey MR, Johnson DS. Computers "
           "and Intractability. Freeman; 1979; Kelley JE Jr, Walker MR. "
           "Critical-path planning and scheduling; 1959; Malcolm DG et al. "
           "PERT. Operations Research; 1959; Kuhn HW. The Hungarian method; "
           "1955; Munkres J. The assignment problem; 1957; Little JDC. "
           "L = lambda W; 1961; Kleinrock L. Queueing Systems Vol. 1; 1975; "
           "Lamport L. Time, clocks, and the ordering of events; 1978; "
           "Graham RL et al. Scheduling notation survey; 1979; de Werra D. "
           "Timetabling; 1985; Moubray J. Reliability-centered Maintenance. "
           "2nd ed.; 1997; ISO 55000:2024; NIOSH. Plain Language About "
           "Shiftwork; 1997; Czeisler CA et al. Science; 1982; Gantt HL. "
           "Work, Wages, and Profits; 1913; Goldratt EM. The Goal; 2004; "
           "PMBOK Guide 7th ed.; 2021; ITIL 4; 2019; Liu CL, Layland JW. "
           "Scheduling algorithms for multiprogramming; 1973).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Scheduling Method - every slot a covenant of time, "
                     "the calendar the ledger of kept promises - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["schedules-resource-calendars"] = _cfg(
    "schedules-resource-calendars", "The Schedules and Resource Calendars Database",
    "Appointments, equipment, shifts, facilities, and maintenance windows: "
    "real, fact-checked scheduling science - calendar data models, "
    "recurrence rules, time-zone handling, scheduling algorithms, "
    "shift-rotation rules, constraint satisfaction, and resource conflict "
    "resolution - taught progressively along the ladder.",
    "schedule and calendar record", "JAH-SCH-", "JAH Schedules and Resource Calendars Archivist",
    "schedules and resource calendars archivist - appointments, equipment "
    "availability, personnel shifts, facilities, and maintenance windows; "
    "scheduling algorithms, shift-rotation rules, constraint satisfaction, "
    "calendar data models, recurrence rules, time-zone handling, and "
    "resource conflict resolution; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["schedules-resource-calendars-signature"] = _cfg(
    "schedules-resource-calendars-signature", "The Schedules and Resource Calendars Signature Database",
    "His original Signature Scheduling Method: every slot a covenant of "
    "time, the calendar the ledger of kept promises, rotation the rhythm, "
    "conflict the broken oath, the maintenance window the honored rest. "
    "The full ladder from what a schedule is through data models, "
    "recurrence, time zones, appointments, shifts, equipment, facilities, "
    "and maintenance, through conflict detection, constraints, algorithms, "
    "and rotations, to optimization, fairness, MRP, and the operating "
    "picture, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "schedule and calendar record", "JAH-SCHS-", "JAH Schedules and Resource Calendars Archivist (Signature)",
    "schedules and resource calendars archivist - Signature editions: his "
    "original Signature Scheduling Method, every slot a covenant of time "
    "and the calendar the ledger of kept promises, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this "
    "system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    frag = {}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        sig = slug.endswith("-signature")
        key = "signature" if sig else "public"
        frag[key] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(recs),
            "status": "live",
            "full_records": len(recs),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if sig else "public-harvest",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)


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

    built = {}
    for slug in ("schedules-resource-calendars", "schedules-resource-calendars-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
        assert "universal-build" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)
    print("built %d databases, %d records; manifest/api merge left to the merger." % (len(built), total))
    print("NO git commit/push performed (merger owns that).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
