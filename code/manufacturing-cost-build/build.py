#!/usr/bin/env python3
"""Build the Manufacturing Cost databases for JAH Databases
(2026-10-17 15:32 EDT order #3).

Verified 2026-10-17 (order #3): RAW SWEEP over the full manifest
(2,390 databases) PLUS every shard index title in jah-databases-data-1
(795 index files, 1,130,741 index lines): zero 'manufacturing-cost*' slugs;
zero title collisions across all 68 planned titles (dedupe gate pre-check:
68/68 clean). The nearest neighbors - 'manufacturing-engineers',
'manufacturing-fabrication-control' (JAH-MFC-), 'public-manufacturing-
engineers', 'manufacturing-robotics-data-types-signature' - are
engineering-process archives, none a cost-to-make vs sell-price costing
database. The paste's rule was applied by name/purpose/record schema/
capabilities: cost accounting of manufacture (BOM costing, labor costing,
overhead allocation, tooling amortization, economies of scale, should-cost
analysis, margin math from unit cost through wholesale to retail, make-vs-
buy costing) is a distinct capability - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  manufacturing-cost             - The Manufacturing Cost Database
                                   (public-harvest: real, fact-checked cost
                                   accounting - the same things the price
                                   database tracks, cost-to-make vs sell
                                   price; standard references Horngren Datar
                                   Rajan Cost Accounting 16th ed 2018;
                                   Cooper and Kaplan HBR 1988; Boothroyd
                                   Dewhurst Knight Product Design for
                                   Manufacture and Assembly 3rd ed 2011;
                                   Wright 1936; Juran Quality Handbook 5th
                                   ed 1999; APICS Dictionary 17th ed 2022;
                                   BLS Employer Costs for Employee
                                   Compensation; US Census Annual Survey of
                                   Manufactures; USITC Harmonized Tariff
                                   Schedule; and the other landmarks cited
                                   per record)
  manufacturing-cost-signature   - The Manufacturing Cost Signature Database
                                   (his original Signature Cost Method:
                                   every unit cost a sworn accounting, the
                                   BOM a covenant of parts, margin the honor
                                   earned between maker and buyer, scale the
                                   discipline that turns cents into
                                   abundance; src signature, titles suffixed
                                   " (Signature Edition)", never presented
                                   as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-MFG- (public) and JAH-MFGS- (signature), verified free in
the manifest id_prefix values and in every shard index (zero hits; the taken
JAH-MFC- belongs to the unrelated manufacturing-fabrication-control
database, so the MFG form was chosen instead).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_manufacturing_cost.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

NOTE: this build never touches data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md - a merger handles those. It never commits.

Never the words "bat belt" anywhere. No website references. No Facebook.
No military or defense-grade content of any kind.
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
from entries_manufacturing_cost import ENTRIES, SIG_TAIL
from demos_manufacturing_cost import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Cost Method: "
                "every unit cost a sworn accounting, the BOM a covenant of "
                "parts, margin the honor earned between maker and buyer, "
                "and scale the discipline that turns cents into abundance. "
                "Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked cost accounting of "
                "manufacture: the cost to make the same things the price "
                "database tracks, set against their sell price - BOM "
                "costing, labor costing, overhead allocation, tooling "
                "amortization, economies of scale, should-cost analysis, "
                "and margin math from unit cost through wholesale to "
                "retail, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a manufacturing cost is, the bill of materials, direct "
              "material costing, direct labor costing, what overhead is, "
              "the standard cost stack, cost of goods sold vs unit cost, "
              "landed cost, reading a supplier quotation, make vs buy the "
              "first question) -> Compounded (multilevel BOM rollups, labor "
              "standards and time studies, machine-hour overhead rates, "
              "tooling and NRE amortization, injection molding cost "
              "anatomy, machining cost anatomy, electronics assembly "
              "costing, yield scrap and rework costing, economies of "
              "scale, activity-based costing, should-cost analysis, target "
              "costing and design-to-cost) -> Advanced (margin math unit "
              "cost vs wholesale vs retail, contribution margin and "
              "break-even, make vs buy total cost of ownership, parametric "
              "cost estimation, cost of poor quality, lifecycle costing, "
              "transfer pricing between plants, design-for-manufacturing "
              "cost decisions, supply-chain disruption costing, "
              "environmental and compliance cost, the 20-cent lesson on "
              "cost differentiation at scale, cost audit).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search BOM costing, material cost, labor rates, overhead allocation, tooling amortization, molding, machining, electronics assembly, yield, scale, ABC, should-cost, target cost, margin math, break-even, make vs buy, lifecycle, cost audit...",
        "chat_ph": "Ask about manufacturing cost...",
        "archive_blurb": ("Seeded %s manufacturing cost records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled manufacturing cost studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about manufacturing cost - from what a manufacturing cost is through the BOM, materials, labor, overhead, the cost stack, landed cost, quotations, and make vs buy, through rollups, time studies, machine rates, tooling, molding, machining, electronics, yield, scale, ABC, should-cost, and target costing, to margin math, break-even, total cost of ownership, parametric estimation, quality cost, lifecycle, transfer pricing, DFM, disruption, compliance, the 20-cent lesson, and cost audits." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "manufacturing-cost-study", "gen_demo_kind": "manufacturing-cost-demo",
        "source": source,
    }

CIT_PUB = ("Manufacturing cost accounting (standard references: Horngren "
           "CT, Datar SM, Rajan MV. Cost Accounting: A Managerial Emphasis. "
           "16th ed. Pearson; 2018; Cooper R, Kaplan RS. Measure Costs "
           "Right: Make the Right Decisions. Harvard Business Review; "
           "1988; Boothroyd G, Dewhurst P, Knight WA. Product Design for "
           "Manufacture and Assembly. 3rd ed. CRC Press; 2011; Wright TP. "
           "Factors Affecting the Cost of Airplanes. Journal of the "
           "Aeronautical Sciences; 1936; Juran JM, Godfrey AB. Juran's "
           "Quality Handbook. 5th ed. McGraw-Hill; 1999; APICS Dictionary. "
           "17th ed. ASCM; 2022; U.S. Bureau of Labor Statistics. Employer "
           "Costs for Employee Compensation; U.S. Census Bureau. Annual "
           "Survey of Manufactures; U.S. International Trade Commission. "
           "Harmonized Tariff Schedule of the United States).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Cost "
                     "Method - every unit cost a sworn accounting, the BOM "
                     "a covenant of parts, margin the honor earned between "
                     "maker and buyer - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["manufacturing-cost"] = _cfg(
    "manufacturing-cost", "The Manufacturing Cost Database",
    "What things cost to make vs what they sell for: real, fact-checked "
    "cost accounting of manufacture - BOM costing, labor costing, overhead "
    "allocation, tooling amortization, economies of scale, should-cost "
    "analysis, and margin math from unit cost through wholesale to retail - "
    "taught progressively along the ladder.",
    "manufacturing cost record", "JAH-MFG-", "JAH Manufacturing Cost Archivist",
    "manufacturing cost archivist - costing what things take to make and "
    "how that cost becomes a price: BOM costing, labor costing, overhead "
    "allocation, tooling amortization, economies of scale, should-cost "
    "analysis, and margin math from unit cost through wholesale to retail; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["manufacturing-cost-signature"] = _cfg(
    "manufacturing-cost-signature", "The Manufacturing Cost Signature Database",
    "His original Signature Cost Method: every unit cost a sworn "
    "accounting, the BOM a covenant of parts, margin the honor earned "
    "between maker and buyer, scale the discipline that turns cents into "
    "abundance. The full ladder from what a manufacturing cost is through "
    "the BOM, labor, overhead, tooling, and scale, to margin math, "
    "break-even, lifecycle, and the 20-cent lesson, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "manufacturing cost record", "JAH-MFGS-", "JAH Manufacturing Cost Archivist (Signature)",
    "manufacturing cost archivist - Signature editions: his original "
    "Signature Cost Method, every unit cost a sworn accounting and the BOM "
    "a covenant of parts, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
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
    for slug in ("manufacturing-cost", "manufacturing-cost-signature"):
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

    # manifest + api.json + restamp + commit are the MERGER's job - never touched here.
    print("manifest/api: SKIPPED (merger handles manifest.json, api.json, restamp, commit)")
    print("built 2 databases, %d records total; shards + pages written, nothing committed" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
