#!/usr/bin/env python3
"""Build the Incident and Outage Records databases for JAH Databases
(missing-115 #55, Wave 1: operational data).

Verified 2026-10-17 (Wave 1): dedupe_gate over the full system (all 68
planned titles, 34 public + 34 Signature Edition): zero collisions. ID
prefixes JAH-INC- (public) and JAH-INCS- (signature) verified free in the
manifest id_prefix values AND in all 790 shard index files (zero hits).
Slugs incident-outage-records / -signature verified free. BUILD NEW.

Creates two NEW databases, 34 ladder-ordered records each:
  incident-outage-records            - The Incident and Outage Records Database
  incident-outage-records-signature  - The Incident and Outage Records Signature Database

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md and NEVER commits or pushes.
It writes only: db/<slug>/index.html + gen-<slug>.js, the shard data dir,
and code/incident-outage-records-build/*. The merger handles the rest.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_incident_outage_records import ENTRIES, SIG_TAIL
from demos_incident_outage_records import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Incident "
                "Method: every outage a wound in the Signature system and "
                "every incident record a battle report - the timeline the "
                "scar, the postmortem the testimony, the error budget the "
                "oath of uptime. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked incident management "
                "and site reliability engineering: the incident lifecycle, "
                "MTTR and MTBF, availability and the nines, fault "
                "timelines, blast radius mapping, impact assessment, "
                "detection and alerting, on-call and escalation, incident "
                "communication, incident command, triage, mitigation, "
                "restoration and rollback, the Five Whys, fault trees, "
                "blameless postmortems, status pages, paging, incident "
                "bridges, SRE and error budgets, chaos engineering, "
                "observability, incident metrics, DORA benchmarks, game "
                "days, review boards, and real case studies (Dyn 2016, "
                "Fastly 2021, AWS 2021) - organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what an incident is, what an outage is, the incident "
              "lifecycle, MTTR, MTBF, availability and the nines, fault "
              "timelines, blast radius, impact assessment, detection and "
              "alerting, on-call and escalation, incident communication) "
              "-> Compounded (incident command, triage and severity, "
              "mitigation before resolution, restoration and rollback, "
              "the Five Whys, fishbone diagrams and fault trees, blameless "
              "postmortems, the postmortem template, remediation action "
              "items, status page operations, paging and alert routing, "
              "the incident bridge) -> Advanced (SRE and error budgets, "
              "chaos engineering, observability, incident metrics "
              "dashboards, DORA benchmarks, game days, incident review "
              "boards, and the Dyn, Fastly, and AWS case studies).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search incidents, outages, MTTR, MTBF, nines, timelines, blast radius, postmortems, error budgets, chaos engineering, DORA, status pages, paging, case studies...",
        "chat_ph": "Ask about incidents and outages...",
        "archive_blurb": ("Seeded %s incident and outage records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled incident and outage studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about incidents and outages - from what an incident is through the lifecycle, MTTR, MTBF, the nines, timelines, blast radius, impact, detection, on-call, and communication, through command, triage, mitigation, restoration, root-cause analysis, postmortems, status pages, paging, and bridges, to error budgets, chaos engineering, observability, metrics, DORA, game days, review boards, and the great outage case studies." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "incident-outage-study", "gen_demo_kind": "incident-outage-demo",
        "source": source,
    }

CIT_PUB = ("Incident management and site reliability engineering (standard "
           "references: Beyer B et al. Site Reliability Engineering: How "
           "Google Runs Production Systems. O'Reilly; 2016; Beyer B et al. "
           "The Site Reliability Workbook. O'Reilly; 2018; Cichonski P et "
           "al. NIST SP 800-61 Rev. 2: Computer Security Incident Handling "
           "Guide; 2012; ISO/IEC 27035-1:2016; Axelos. ITIL Foundation: "
           "ITIL 4 Edition; 2019; Forsgren N, Humble J, Kim G. Accelerate. "
           "IT Revolution; 2018; Allspaw J. Blameless PostMortems and a "
           "Just Culture. Etsy; 2012; FEMA National Incident Management "
           "System (ICS); Basiri A et al. Chaos Engineering. IEEE "
           "Software; 2016; PagerDuty State of On-Call Report; Atlassian "
           "Incident Communication Handbook; OpenTelemetry documentation "
           "(CNCF); Dyn statement on the 10/21/2016 DDoS attack; Fastly "
           "Summary of June 8 outage; 2021; Amazon Web Services. Summary "
           "of the AWS Service Event in the Northern Virginia (US-EAST-1) "
           "Region; 2021).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Incident Method - every outage a wound in the "
                     "Signature system, every record a battle report - "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["incident-outage-records"] = _cfg(
    "incident-outage-records", "The Incident and Outage Records Database",
    "Fault timelines, affected systems, impact, restoration, and root-cause "
    "analysis: real, fact-checked incident management and site reliability "
    "engineering - from what an incident is through command, triage, "
    "mitigation, and blameless postmortems, to error budgets, chaos "
    "engineering, DORA benchmarks, and the great outage case studies - "
    "taught progressively along the ladder.",
    "incident and outage record", "JAH-INC-", "JAH Incident and Outage Records Archivist",
    "incident and outage records archivist - fault timelines, affected "
    "systems, impact, restoration, and root-cause analysis across incident "
    "command, postmortems, blameless review, MTTR/MTBF measurement, "
    "status-page operations, and escalation and paging; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["incident-outage-records-signature"] = _cfg(
    "incident-outage-records-signature", "The Incident and Outage Records Signature Database",
    "His original Signature Incident Method: every outage a wound in the "
    "Signature system and every incident record a battle report - the "
    "timeline the scar, the postmortem the testimony, the error budget the "
    "oath of uptime. The full ladder from what an incident is through the "
    "lifecycle, MTTR, MTBF, the nines, command, triage, mitigation, and "
    "postmortems, to error budgets, chaos engineering, DORA, and the "
    "great outage case studies, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "incident and outage record", "JAH-INCS-", "JAH Incident and Outage Records Archivist (Signature)",
    "incident and outage records archivist - Signature editions: his "
    "original Signature Incident Method, every outage a wound in the "
    "Signature system and every record a battle report, clearly labeled "
    "Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
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
    for slug in ("incident-outage-records", "incident-outage-records-signature"):
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

    # NOTE: manifest.json, api.json, index.html, README.md, docs/AI_ACCESS.md
    # are owned by the merger. This build stops here by design.
    print("records built: %d databases, %d records total" % (len(built), total))
    print("NEXT (merger): manifest + api.json entries, restamp, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
