#!/usr/bin/env python3
"""Build the Workflow and Case Records databases for JAH Databases
(missing-115 program, Wave 1 - operational data, Manon's #1 priority).

Verified 2026-10-17: RAW SWEEP over the full manifest plus every shard
index title in jah-databases-data-1 plus the main-repo data dir: zero
'workflow-case*' slugs/names; zero 'Workflow and Case Records' title
collisions; zero refusals from the whole-system dedupe gate over all 68
titles plus both database names. The two keyword near-hits, 'ai-workflows'
(AI agent/tool workflows) and 'project-workflow' (project scheduling and
phases), are distinct capabilities - neither carries workflow patterns,
state machines, BPMN, SLA tracking, escalation paths, case-management
lifecycles, or audit trails of status changes as its record schema. The
paste's rule was applied by name/purpose/record schema/capabilities:
workflow and case operational records are a distinct capability - BUILD NEW
is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  workflow-case-records              - The Workflow and Case Records Database
                                       (public-harvest: real, fact-checked
                                       operational workflow and case data -
                                       tasks, ownership, status transitions,
                                       deadlines, dependencies, outcomes;
                                       workflow patterns, state machines,
                                       BPMN 2.0, case-management lifecycles,
                                       SLA tracking, escalation paths,
                                       handoffs, audit trails; standard
                                       references van der Aalst et al.
                                       Workflow Patterns (MIT Press 2006);
                                       OMG BPMN 2.0; OMG CMMN 1.1; Dumas et
                                       al. Fundamentals of BPM 2nd ed 2018;
                                       Weske BPM 3rd ed 2019; WfMC Workflow
                                       Reference Model; PMBOK Guide 7th ed
                                       2021; ITIL 4 2019; Little 1961;
                                       Kelley and Walker CPM 1959; Swenson
                                       ACM 2010; Garcia-Molina and Salem
                                       Sagas 1987; and the other landmarks
                                       cited per record)
  workflow-case-records-signature    - The Workflow and Case Records Signature
                                       Database
                                       (his original Signature Operations
                                       Method: every task a sworn charge,
                                       every status a witnessed station,
                                       every handoff a sealed covenant, every
                                       audit trail an unbroken chain of
                                       testimony; src signature, titles
                                       suffixed " (Signature Edition)",
                                       never presented as authentic public
                                       record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-WFR- (public) and JAH-WFRS- (signature), verified free in
the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_workflow_case_records.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. It only creates the new untracked paths listed in
the task, plus the fragment JSON for the merger.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian operational scope only - nothing about neutralizing or defeating
military or defense-grade systems.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/workflow-case-records.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_workflow_case_records import ENTRIES, SIG_TAIL
from demos_workflow_case_records import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Operations "
                "Method: every task a sworn charge, every status a "
                "witnessed station, every handoff a sealed covenant, and "
                "every audit trail an unbroken chain of testimony. Clearly "
                "labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked operational workflow "
                "and case data: tasks, ownership, status transitions, "
                "deadlines, dependencies, and outcomes; workflow patterns, "
                "state machines, BPMN 2.0, case-management lifecycles, SLA "
                "tracking, escalation paths, handoffs, and audit trails of "
                "status changes, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a workflow is, tasks cases and processes, ownership "
              "and roles, status lifecycles, deadlines, handoffs, audit "
              "trails, outcomes versus outputs, a simple workflow "
              "walk-through) -> Compounded (state machines, basic workflow "
              "patterns, the four dependency types, advanced control-flow "
              "patterns, BPMN 2.0 notation, critical path math, SLA "
              "fundamentals, case management lifecycles, escalation paths, "
              "triage, queues and Little's law, multi-instance patterns, "
              "cancellation and compensation, handoff protocols) -> "
              "Advanced (BPMN execution semantics, orchestration versus "
              "choreography, sagas, deadlock detection, SLA breach "
              "prediction, hash-chained audit trails, cycle time and flow "
              "analytics, versioning running instances, dynamic escalation "
              "routing, workflow engines and durable execution, case "
              "records at scale).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search workflows, tasks, cases, status transitions, SLAs, escalations, BPMN, dependencies, handoffs, audit trails, sagas...",
        "chat_ph": "Ask about workflows and cases...",
        "archive_blurb": ("Seeded %s workflow and case records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled workflow and case studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about workflows and cases - from what a workflow is through tasks, cases, ownership, statuses, deadlines, handoffs, audit trails, and outcomes, through state machines, patterns, dependencies, BPMN, critical path, SLAs, case lifecycles, escalation, triage, queues, and handoff protocols, to execution semantics, sagas, deadlock detection, breach prediction, hash-chained trails, flow analytics, versioning, dynamic routing, durable engines, and records at scale." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "workflow-case-study", "gen_demo_kind": "workflow-case-demo",
        "source": source,
    }

CIT_PUB = ("Workflow and case operations (standard references: van der Aalst "
           "WMP et al. Workflow Patterns: The Definitive Guide. MIT Press; "
           "2006; Object Management Group. Business Process Model and "
           "Notation (BPMN), Version 2.0.2. OMG; 2013; Object Management "
           "Group. Case Management Model and Notation (CMMN), Version 1.1. "
           "OMG; 2016; Dumas M et al. Fundamentals of Business Process "
           "Management. 2nd ed. Springer; 2018; Weske M. Business Process "
           "Management. 3rd ed. Springer; 2019; Workflow Management "
           "Coalition. The Workflow Reference Model. WfMC-TC-1003; 1995; "
           "Project Management Institute. PMBOK Guide. 7th ed. PMI; 2021; "
           "AXELOS. ITIL Foundation: ITIL 4 Edition. TSO; 2019; Little JDC. "
           "A Proof for the Queuing Formula: L = lambda W. Operations "
           "Research. 1961; Kelley JE Jr, Walker MR. Critical-Path Planning "
           "and Scheduling. 1959; Swenson KD. Mastering the Unpredictable. "
           "Meghan-Kiffer Press; 2010; Garcia-Molina H, Salem K. Sagas. "
           "ACM SIGMOD; 1987).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Operations Method - every task a sworn charge, every "
                     "status a witnessed station, every handoff a sealed "
                     "covenant - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["workflow-case-records"] = _cfg(
    "workflow-case-records", "The Workflow and Case Records Database",
    "Tasks, ownership, status transitions, deadlines, dependencies, and "
    "outcomes: real, fact-checked operational workflow and case data - "
    "workflow patterns, state machines, BPMN 2.0, case-management "
    "lifecycles, SLA tracking, escalation paths, handoffs, and audit "
    "trails of status changes - taught progressively along the ladder.",
    "workflow and case record", "JAH-WFR-", "JAH Workflow and Case Records Archivist",
    "workflow and case records archivist - tasks, ownership, status "
    "transitions, deadlines, dependencies, and outcomes; workflow "
    "patterns, state machines, BPMN 2.0, case-management lifecycles, SLA "
    "tracking, escalation paths, handoffs, and audit trails of status "
    "changes; teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_PUB, "public")
DBCFG["workflow-case-records-signature"] = _cfg(
    "workflow-case-records-signature", "The Workflow and Case Records Signature Database",
    "His original Signature Operations Method: every task a sworn charge, "
    "every status a witnessed station, every handoff a sealed covenant, "
    "every audit trail an unbroken chain of testimony. The full ladder "
    "from what a workflow is through tasks, ownership, statuses, "
    "deadlines, handoffs, and audit trails, through state machines, "
    "patterns, dependencies, BPMN, SLAs, escalation, and triage, to "
    "execution semantics, sagas, breach prediction, durable engines, and "
    "records at scale, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "workflow and case record", "JAH-WFRS-", "JAH Workflow and Case Records Archivist (Signature)",
    "workflow and case records archivist - Signature editions: his "
    "original Signature Operations Method, every task a sworn charge and "
    "every handoff a sealed covenant, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from "
    "this system",
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
    for slug in ("workflow-case-records", "workflow-case-records-signature"):
        cfg = DBCFG[slug]
        sig = slug.endswith("-signature")
        key = "signature" if sig else "public"
        base_url = "%s/data/%s/index.jsonl.gz" % (SHARD_BASE, slug)
        frag[key] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": base_url,
            "record_count": len(built[slug]),
            "status": "live",
            "full_records": len(built[slug]),
            "index": base_url,
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
            "source": "signature" if sig else "public-harvest",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
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
    for slug in ("workflow-case-records", "workflow-case-records-signature"):
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
    # NOTE: manifest.json, api.json, index.html, README.md, docs/AI_ACCESS.md
    # are merger-owned - this build does not touch them, and does not commit
    # or push. The merger verifies and ships.
    print("done: %d databases, %d records. manifest/api/commit left to the merger." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
