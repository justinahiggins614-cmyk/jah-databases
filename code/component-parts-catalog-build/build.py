#!/usr/bin/env python3
"""Build the Component and Parts Catalog databases for JAH Databases
(Build-210 #2, top-20 priority).

Verified 2026-10-17 (Build-210 top-20 #2): RAW SWEEP over the full manifest
(2,386 databases) PLUS every shard index title in jah-databases-data-1
(785 index files, 1,130,401 index lines) PLUS the main-repo data dir:
zero 'component-parts*' slugs/names; zero 'component and parts catalog'
or 'component-parts' title collisions. The one keyword near-hit, the
'components' database (JAH-CPT), is an encyclopedia-style multi-aspect
archive (overview/detailed/examples/faq/history/applications per topic),
NOT a parts catalog - it has no per-part engineering properties,
compatibility notes, selection criteria, or cross-references. The other
near-hit, 'software-components' (JAH-CMP-), covers software only. The
paste's rule was applied by name/purpose/record schema/capabilities: a
searchable catalog of real parts with properties, specifications,
compatibility, and uses is a distinct capability - BUILD NEW is the
verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  component-parts-catalog            - The Component and Parts Catalog Database
                                       (public-harvest: real, fact-checked
                                       component and parts engineering -
                                       electronic components, mechanical
                                       parts, materials stock, modules and
                                       subassemblies - every record carrying
                                       properties, specifications, selection
                                       criteria, typical uses, and
                                       compatibility notes; standard
                                       references Horowitz and Hill The Art
                                       of Electronics 3rd ed 2015;
                                       Machinery's Handbook 31st ed 2020;
                                       IEC 60062 marking codes; IEC 60115
                                       resistors; IEC 60384 capacitors;
                                       MIL-STD-202; IPC-A-610; IPC-2221;
                                       ASME B1.1 threads; ISO 898 fasteners;
                                       ISO 281 bearing life; AGMA 2001 gears;
                                       IEC 61000 EMC; MIL-HDBK-217F
                                       reliability; SAE AS5553 counterfeit
                                       avoidance; and the other landmarks
                                       cited per record)
  component-parts-catalog-signature  - The Component and Parts Catalog
                                       Signature Database
                                       (his original Signature Parts Method:
                                       every component a covenant of
                                       properties, the catalog the armory of
                                       the Signature system, selection the
                                       oath between builder and part,
                                       compatibility the handshake, derating
                                       the honor margin; src signature,
                                       titles suffixed " (Signature
                                       Edition)", never presented as
                                       authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CPTC- (public) and JAH-CPTCS- (signature), verified free
in the manifest and in every shard index (zero hits; JAH-CPCT- belongs to
the unrelated Captain Planet CO2 Token Trackers database, so the CPTC form
was chosen to avoid even substring ambiguity).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_component_parts_catalog.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
commit.

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
from entries_component_parts_catalog import ENTRIES, SIG_TAIL
from demos_component_parts_catalog import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Parts Method: "
                "every component a covenant of properties, the catalog the "
                "armory of the Signature system, selection the oath between "
                "builder and part, compatibility the handshake, and derating "
                "the honor margin. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked component and parts "
                "engineering: electronic components (resistors, capacitors, "
                "inductors, diodes, transistors, ICs, sensors, "
                "optoelectronics, relays), mechanical parts (fasteners, "
                "bearings, gears, belts), wire and cable, materials stock, "
                "and modules and subassemblies - every record carrying "
                "properties, specifications, selection criteria, typical "
                "uses, and compatibility notes, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a component or part is, reading a datasheet, units "
              "tolerances and ratings, passive components, mechanical "
              "parts, wire cable and connectors, markings and "
              "identification, materials stock, series and parallel rules, "
              "what compatibility means, selection criteria, standards "
              "bodies and part numbering) -> Compounded (resistors, "
              "capacitors, inductors and transformers, diodes, transistors, "
              "integrated circuits and logic families, sensors, "
              "optoelectronics, fasteners and threads, bearings and "
              "bushings, gears belts and power transmission, relays "
              "contactors and switches) -> Advanced (derating and design "
              "margins, tolerance stack-up, thermal management, EMI and EMC "
              "compatibility, reliability MTBF and failure rates, "
              "counterfeit detection, obsolescence management, sourcing the "
              "BOM and the supply chain, cross-references and substitution, "
              "modules and subassemblies build vs buy).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search resistors, capacitors, inductors, diodes, transistors, ICs, sensors, fasteners, bearings, gears, relays, datasheets, derating, BOM, cross-references...",
        "chat_ph": "Ask about components and parts...",
        "archive_blurb": ("Seeded %s component and parts catalog records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled component and parts studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about components and parts - from what a part is through datasheets, tolerances, passives, mechanical parts, wire and connectors, markings, stock, and selection, through resistors, capacitors, inductors, diodes, transistors, ICs, sensors, optoelectronics, fasteners, bearings, gears, and relays, to derating, stack-up, thermal, EMC, reliability, counterfeit detection, obsolescence, sourcing, cross-references, and build vs buy." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "component-parts-study", "gen_demo_kind": "component-parts-demo",
        "source": source,
    }

CIT_PUB = ("Component and parts engineering (standard references: Horowitz P, "
           "Hill W. The Art of Electronics. 3rd ed. Cambridge University "
           "Press; 2015; Oberg E et al. Machinery's Handbook. 31st ed. "
           "Industrial Press; 2020; IEC 60062:2016 marking codes; IEC "
           "60115-1:2020 fixed resistors; IEC 60384-1:2016 fixed capacitors; "
           "MIL-STD-202H electronic parts test methods; IPC-A-610H; IPC-2221B; "
           "IPC J-STD-001H; ASME B1.1-2019 unified threads; ISO 68-1:1998 "
           "metric threads; ISO 898-1:2013 fastener grades; ISO 281:2007 "
           "bearing life; ANSI/AGMA 2001-D04 gears; IEC 61000-4 EMC; "
           "MIL-HDBK-217F Notice 2 reliability prediction; SAE AS5553B "
           "counterfeit avoidance; JEDEC JESD47 qualification; IEC 60664-1 "
           "insulation coordination; EIA-198 ceramic capacitors; IEC 60068-2 "
           "environmental testing).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Parts "
                     "Method - every component a covenant of properties, the "
                     "catalog the armory of the Signature system - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["component-parts-catalog"] = _cfg(
    "component-parts-catalog", "The Component and Parts Catalog Database",
    "Find components, their properties, compatibility, and uses: real, "
    "fact-checked component and parts engineering across electronic "
    "components, mechanical parts, materials stock, and modules and "
    "subassemblies - every record carrying properties, specifications, "
    "selection criteria, typical uses, and compatibility notes, taught "
    "progressively along the ladder.",
    "component parts catalog record", "JAH-CPTC-", "JAH Component and Parts Catalog Archivist",
    "component and parts catalog archivist - finding components, their "
    "properties, compatibility, and uses across electronic components, "
    "mechanical parts, materials stock, and modules and subassemblies; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["component-parts-catalog-signature"] = _cfg(
    "component-parts-catalog-signature", "The Component and Parts Catalog Signature Database",
    "His original Signature Parts Method: every component a covenant of "
    "properties, the catalog the armory of the Signature system, selection "
    "the oath between builder and part, compatibility the handshake, "
    "derating the honor margin. The full ladder from what a part is through "
    "datasheets, tolerances, passives, mechanical parts, and selection, "
    "through the deep component families, to derating, thermal, EMC, "
    "reliability, sourcing, and build vs buy, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "component parts catalog record", "JAH-CPTCS-", "JAH Component and Parts Catalog Archivist (Signature)",
    "component and parts catalog archivist - Signature editions: his original "
    "Signature Parts Method, every component a covenant of properties and "
    "the catalog the armory of the Signature system, clearly labeled "
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
    for slug in ("component-parts-catalog", "component-parts-catalog-signature"):
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

    entries_m = [base.manifest_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [base.api_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
