#!/usr/bin/env python3
"""Build the Customer Relationship and Service History databases for JAH Databases
(missing-115 program, Wave 1 - operational data, Manon's #1 priority).

Item 52 of the 115-category audit: requests, communications, product
history, support cases, service outcomes - CRM data models, ticket
lifecycles, escalation matrices, CSAT/NPS measurement, support analytics,
customer journey records, retention analysis.

Dedupe pre-check 2026-10-17: all 34 titles plus all 34 " (Signature
Edition)" variants run through code/dedupe_gate.py against the whole
system (exact index) BEFORE authoring - zero collisions, zero refusals.

ID prefixes: JAH-CRM- (public) and JAH-CRMS- (signature), verified free
in the manifest (2,390 prefixes: zero exact hits, zero substring hits)
and in every shard index file of jah-databases-data-1 (zero "JAH-CRM
id hits across all index.jsonl.gz files).

So this build creates two NEW databases, 34 ladder-ordered records each:

  customer-relationship-service-history            - The Customer
      Relationship and Service History Database (public-harvest: real,
      fact-checked CRM and service-management practice; standard
      references Reichheld The Ultimate Question 2.0 2011; ITIL 4
      Foundation 2019; Buttle and Maklan CRM 4th ed 2019; Dixon The
      Effortless Experience 2013; Peppers and Rogers 3rd ed 2016;
      Zeithaml Services Marketing 7th ed 2017; Heskett The Service
      Profit Chain 1997; Johnston Service Operations Management 4th ed
      2012; Fitzsimmons Service Management 9th ed 2019; ISO 10002:2018;
      ISO 10004:2018; ISO/IEC 20000-1:2018; COPC CX Standard; and the
      other landmarks cited per record)
  customer-relationship-service-history-signature  - The Customer
      Relationship and Service History Signature Database (his original
      Signature Service Covenant: every customer a covenant partner,
      every request a sworn matter, every ticket a kept promise,
      resolution the honor kept, and the archive the memory of every
      oath; src signature, titles suffixed " (Signature Edition)",
      never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_customer_relationship_service_history.py). Every demo
prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker; the build machine-executes
all 68 demos.

MERGER NOTE: this build does NOT touch data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and does NOT git commit or
push. It writes only its own new untracked paths plus the merger
fragment at
~/workspace/hidden_files/missing-builds/fragments/customer-relationship-service-history.json.

Civilian operational scope only: nothing on neutralizing or defeating
military or defense-grade systems. Never the words "bat belt" anywhere.
No website references. No Facebook.
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
FRAGMENT = ("/home/hatch/workspace/hidden_files/missing-builds/fragments/"
            "customer-relationship-service-history.json")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_customer_relationship_service_history import ENTRIES, SIG_TAIL
from demos_customer_relationship_service_history import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Service "
                "Covenant: every customer a covenant partner, every "
                "request a sworn matter, every ticket a kept promise, "
                "resolution the honor kept, and the archive the memory of "
                "every oath. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked customer "
                "relationship and service management: the customer "
                "record, the service vocabulary, ticket anatomy and "
                "lifecycles, communication channels, SLAs, "
                "prioritization, service desks, product history, CRM "
                "data models, escalation matrices, core metrics, "
                "knowledge bases and self-service, journey mapping, "
                "CSAT, NPS, CES, support analytics, retention and "
                "churn, segmentation, complaint recovery, major "
                "incidents, workforce management, quality assurance, "
                "root cause analysis, voice of the customer, lifetime "
                "value, predictive churn, omnichannel routing, service "
                "catalogs, continual improvement, CRM architecture, and "
                "service economics - every record carrying description, "
                "how it works, key points, requirements, standards, "
                "citations, and a working demonstration program, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a customer relationship is, the customer record, "
              "the service vocabulary, ticket anatomy, ticket lifecycle, "
              "channels and touchpoints, SLAs, prioritization, service "
              "desk tiers, product history) -> Compounded (CRM data "
              "models, escalation matrices, core metrics, knowledge "
              "bases and self-service, journey mapping, CSAT, NPS, CES, "
              "support analytics, retention and churn, segmentation, "
              "complaint recovery, major incidents) -> Advanced "
              "(workforce management, quality assurance, root cause "
              "analysis, voice of the customer, lifetime value, "
              "predictive churn, omnichannel routing, service catalog, "
              "continual improvement, CRM architecture, service "
              "economics).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search customer records, tickets, SLAs, escalation, CSAT, NPS, CES, churn, retention, RFM, journey maps, knowledge bases, workforce management, root cause, lifetime value...",
        "chat_ph": "Ask about customer relationships and service history...",
        "archive_blurb": ("Seeded %s customer relationship and service history records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled customer relationship and service studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about customer relationships and service history - from what a relationship is through customer records, the service vocabulary, tickets and lifecycles, channels, SLAs, prioritization, service desks, and product history, through CRM models, escalation, core metrics, knowledge bases, journey mapping, CSAT, NPS, CES, analytics, retention, segmentation, recovery, and major incidents, to workforce management, quality assurance, root cause analysis, voice of the customer, lifetime value, predictive churn, omnichannel routing, service catalogs, continual improvement, CRM architecture, and service economics." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "customer-relationship-study", "gen_demo_kind": "customer-relationship-demo",
        "source": source,
    }

CIT_PUB = ("Customer relationship and service management (standard "
           "references: Reichheld FF. The Ultimate Question 2.0. Harvard "
           "Business Review Press; 2011; AXELOS. ITIL Foundation: ITIL 4 "
           "Edition. TSO; 2019; Buttle F, Maklan S. Customer Relationship "
           "Management: Concepts and Technologies. 4th ed. Routledge; "
           "2019; Dixon M, Toman N, DeLisi R. The Effortless Experience. "
           "Portfolio; 2013; Peppers D, Rogers M. Managing Customer "
           "Experience and Relationships. 3rd ed. Wiley; 2016; Zeithaml "
           "VA, Bitner MJ, Gremler DD. Services Marketing. 7th ed. "
           "McGraw-Hill; 2017; Heskett JL, Sasser WE, Schlesinger LA. The "
           "Service Profit Chain. Free Press; 1997; Johnston R, Clark G. "
           "Service Operations Management. 4th ed. Pearson; 2012; "
           "Fitzsimmons JA, Fitzsimmons MJ, Bordoloi SK. Service "
           "Management. 9th ed. McGraw-Hill; 2019; ISO 10002:2018; ISO "
           "10004:2018; ISO/IEC 20000-1:2018; COPC Customer Experience "
           "(CX) Standard Release 7.0; 2021).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Service Covenant - every customer a covenant "
                     "partner, every request a sworn matter, every ticket "
                     "a kept promise - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["customer-relationship-service-history"] = _cfg(
    "customer-relationship-service-history",
    "The Customer Relationship and Service History Database",
    "Requests, communications, product history, support cases, and "
    "service outcomes: real, fact-checked CRM and service-management "
    "practice across the customer record, tickets, SLAs, escalation, "
    "CSAT, NPS, CES, analytics, retention, and the economics of "
    "service, taught progressively along the ladder.",
    "customer relationship and service record", "JAH-CRM-",
    "JAH Customer Relationship and Service History Archivist",
    "customer relationship and service history archivist - keeping the "
    "complete record of requests, communications, product history, "
    "support cases, and service outcomes; teaching CRM data models, "
    "ticket lifecycles, escalation matrices, CSAT and NPS measurement, "
    "support analytics, customer journey records, and retention "
    "analysis progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["customer-relationship-service-history-signature"] = _cfg(
    "customer-relationship-service-history-signature",
    "The Customer Relationship and Service History Signature Database",
    "His original Signature Service Covenant: every customer a "
    "covenant partner, every request a sworn matter, every ticket a "
    "kept promise, resolution the honor kept, and the archive the "
    "memory of every oath. The full ladder from what a relationship "
    "is through records, tickets, channels, SLAs, and service desks, "
    "through CRM models, escalation, metrics, journeys, and "
    "measurement, to workforce management, quality, prediction, and "
    "service economics, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "customer relationship and service record", "JAH-CRMS-",
    "JAH Customer Relationship and Service History Archivist (Signature)",
    "customer relationship and service history archivist - Signature "
    "editions: his original Signature Service Covenant, every customer "
    "a covenant partner and every ticket a kept promise, clearly "
    "labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to "
    "- using only archive data from this system",
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
        is_sig = slug.endswith("-signature")
        key = "signature" if is_sig else "public"
        idx = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        frag[key] = {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"], "local_index": idx,
            "record_count": len(recs), "status": "live",
            "full_records": len(recs), "index": idx,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if is_sig else "public-harvest",
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
    for slug in ("customer-relationship-service-history",
                 "customer-relationship-service-history-signature"):
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
    print("done: %d databases, %d records. manifest/api.json untouched for the merger; no commit." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
