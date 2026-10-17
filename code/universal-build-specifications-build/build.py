#!/usr/bin/env python3
"""Build the Universal Build Specifications databases for JAH Databases
(Build-210 #1, top-20 priority).

Verified 2026-10-17 (Build-210 top-20 #1): NO database covers converting a
request into a complete structured build specification - objectives,
deliverables, functional and non-functional requirements, constraints,
assumptions and dependencies, acceptance criteria, verification plans -
across software, hardware, devices, and systems. The paste's rule was
applied by name/purpose/record schema/capabilities; the one keyword hit
(lego-satellite) is unrelated.

Manifest search (2,384 databases): zero 'universal-build*' slugs/names;
zero 'build-spec' slugs/names; no db/universal-build* dirs. Whole-system
exact-title sweep over the manifest PLUS all shard index 't' keys: zero
collisions for all 34 planned titles x2 editions (68 variants). NOTE: the
persisted dedupe gate dir (data/dedupe/exact) is stale for the newest
fields, so the raw manifest+shard sweep was the authoritative preflight.

So this build creates two NEW databases, 34 ladder-ordered records each:

  universal-build-specifications           - The Universal Build Specifications Database
                                             (public-harvest: real, fact-checked
                                             requirements and systems engineering;
                                             standard references INCOSE Systems
                                             Engineering Handbook 4th ed 2015;
                                             ISO/IEC/IEEE 29148:2018 Requirements
                                             Engineering; ISO/IEC/IEEE 15288:2015
                                             Life Cycle Processes; Wiegers and
                                             Beatty Software Requirements 3rd ed
                                             2013; Robertson and Robertson
                                             Mastering the Requirements Process 3rd
                                             ed 2012; NASA Systems Engineering
                                             Handbook SP-2016-6105 Rev 2 2016;
                                             PMBOK Guide 7th ed 2021; landmark
                                             standards and papers as cited per
                                             record)
  universal-build-specifications-signature - The Universal Build Specifications
                                             Signature Database
                                             (his original Signature Build Method:
                                             every request is a commission and every
                                             specification a build contract - the
                                             objective as the destination,
                                             deliverables as the promised cargo,
                                             requirements as the load-bearing beams,
                                             acceptance as the final inspection
                                             stamp; src signature, titles suffixed
                                             " (Signature Edition)", never
                                             presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-UBS- (public) and JAH-UBSS- (signature), verified free in
the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_universal_build_specifications.py). Every demo prints its
real computed values, asserts tight bounds (never float exact-equality),
and ends with the OK marker; the build machine-executes all 68 demos
before commit.

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
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_universal_build_specifications import ENTRIES, SIG_TAIL
from demos_universal_build_specifications import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Build Method: "
                "every request is a commission and every specification a build "
                "contract - the objective as the destination, deliverables as "
                "the promised cargo, requirements as the load-bearing beams, "
                "and acceptance as the final inspection stamp. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked requirements and systems "
                "engineering: the full ladder from what a build specification "
                "is through the request-to-specification pipeline, the anatomy "
                "of a complete spec, objectives, deliverables, functional and "
                "non-functional requirements, constraints, assumptions and "
                "dependencies, acceptance criteria, and verification plans, "
                "through stakeholder mapping, scope control, traceability, "
                "risk registers, interface specifications, software specs, "
                "hardware specs, embedded specs, integration specs, safety and "
                "regulatory compliance, versioning, cost estimation, and "
                "prototypes and phase gates, to model-based systems "
                "engineering, specification standards, AI-assisted generation "
                "and review, machine learning system specs, cyber-physical "
                "system specs, contracts and statements of work, executable "
                "specifications and digital twins, FMEA and FTA, formal "
                "reviews and inspections, and the handoff from specification "
                "to manufacture, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what "
              "a build specification is, the request-to-specification "
              "pipeline, anatomy of a complete spec, objectives, "
              "deliverables, functional requirements, non-functional "
              "requirements, constraints, assumptions and dependencies, "
              "acceptance criteria, verification plans) -> Compounded "
              "(stakeholder mapping and elicitation, scope control, "
              "traceability matrices, risk registers, interface "
              "specifications, software build specs, hardware build specs, "
              "embedded build specs, systems integration specs, safety and "
              "regulatory compliance, versioning and baselines, cost "
              "estimation, prototypes and phase gates) -> Advanced "
              "(model-based systems engineering, specification standards, "
              "AI-assisted generation and review, machine learning system "
              "specs, cyber-physical system specs, contracts and statements "
              "of work, executable specifications and digital twins, FMEA "
              "and FTA, formal reviews and inspections, specification to "
              "manufacture handoff).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search objectives, deliverables, requirements, constraints, acceptance criteria, verification, traceability, FMEA, IEEE 29148, interfaces, tolerance stack-up, SOW...",
        "chat_ph": "Ask about build specifications...",
        "archive_blurb": ("Seeded %s universal build specification records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled build specification studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about build specifications - from what a spec is through the request pipeline, objectives, deliverables, requirements, constraints, acceptance, and verification, through stakeholders, scope, traceability, risks, interfaces, software, hardware, embedded, integration, safety, versioning, cost, and prototypes, to MBSE, standards, AI-assisted review, ML and cyber-physical specs, contracts, executable specs, FMEA, inspections, and the manufacturing handoff." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "build-specification-study", "gen_demo_kind": "build-specification-demo",
        "source": source,
    }

CIT_PUB = ("Build specifications (standard references: INCOSE "
           "INCOSE-TP-2003-002-04 Systems Engineering Handbook 4th ed 2015; "
           "ISO/IEC/IEEE 29148:2018 Requirements Engineering; ISO/IEC/IEEE "
           "15288:2015 System Life Cycle Processes; Wiegers and Beatty "
           "Software Requirements 3rd ed 2013; Robertson and Robertson "
           "Mastering the Requirements Process 3rd ed 2012; NASA "
           "SP-2016-6105 Rev 2 Systems Engineering Handbook 2016; PMI PMBOK "
           "Guide 7th ed 2021; IEEE 830-1998; Hull Jackson and Dick "
           "Requirements Engineering 3rd ed 2011; Sommerville Software "
           "Engineering 10th ed 2016; Ulrich and Eppinger Product Design and "
           "Development 7th ed 2019; Boehm Software Engineering Economics "
           "1981; McConnell Software Estimation 2006; CMMI for Development "
           "v2.0 2018; ISO/IEC 25010:2011; ISO 9001:2015; SAE J1739-2021 "
           "FMEA; IEC 61025:2006 FTA; ISO 26262:2018; IEC 61508:2010; RTCA "
           "DO-178C 2011; OMG SysML v1.6 2019; INCOSE-TP-2010-006-03 Guide "
           "for Writing Requirements; MIL-STD-882E 2012; Fagan IBM Systems "
           "Journal 1976 inspections; Gilb and Graham Software Inspection "
           "1993).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Build "
                     "Method - every request a commission, every specification "
                     "a build contract - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["universal-build-specifications"] = _cfg(
    "universal-build-specifications", "The Universal Build Specifications Database",
    "Real, fact-checked requirements and systems engineering: how to turn any "
    "request into a complete, structured build specification - objectives, "
    "deliverables, functional and non-functional requirements, constraints, "
    "assumptions and dependencies, acceptance criteria, and verification plans - "
    "across software, hardware, devices, and systems, taught progressively "
    "along the ladder.",
    "universal build specification record", "JAH-UBS-", "JAH Universal Build Specifications Archivist",
    "universal build specifications archivist - requirements engineering: turning "
    "requests into complete structured build specifications (objectives, "
    "deliverables, functional and non-functional requirements, constraints, "
    "assumptions and dependencies, acceptance criteria, verification plans) "
    "across software, hardware, devices, and systems; teaching progressively "
    "along the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["universal-build-specifications-signature"] = _cfg(
    "universal-build-specifications-signature", "The Universal Build Specifications Signature Database",
    "His original Signature Build Method: every request is a commission and "
    "every specification a build contract - the objective as the destination, "
    "deliverables as the promised cargo, requirements as the load-bearing "
    "beams, acceptance as the final inspection stamp. The full ladder from "
    "what a spec is through the pipeline, objectives, deliverables, and "
    "requirements, through stakeholders, scope, traceability, and interfaces, "
    "to MBSE, standards, executable specs, FMEA, inspections, and the "
    "manufacturing handoff, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "universal build specification record", "JAH-UBSS-", "JAH Universal Build Specifications Archivist (Signature)",
    "universal build specifications archivist - Signature editions: his original "
    "Signature Build Method, every request a commission and every specification "
    "a build contract, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using "
    "only archive data from this system",
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
    for slug in ("universal-build-specifications", "universal-build-specifications-signature"):
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
        assert "nephrology" not in page.lower(), "field leftover in %s" % slug
        assert "kidney" not in page.lower(), "field leftover in %s" % slug
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
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    entries_m = [base.manifest_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [base.api_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
