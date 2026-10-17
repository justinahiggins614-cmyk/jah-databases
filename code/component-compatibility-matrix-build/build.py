#!/usr/bin/env python3
"""Build the Component Compatibility Matrix databases for JAH Databases
(Build-210 #3, top-20 priority).

Verified 2026-10-17 (Build-210 top-20 #3): RAW SWEEP over the full manifest
(2,388 databases) PLUS every shard index title in jah-databases-data-1:
zero 'component-compatibility*' slugs/names; zero 'component compatibility
matrix' title collisions. The one keyword near-hit, 'component-parts-catalog'
(JAH-CPTC-), is a parts CATALOG - it catalogs what each part is, its
properties and uses; it does not JUDGE pairings. This database is the
distinct capability the paste names: compatibility matrices that declare
whether parts, modules, materials, and interfaces WORK TOGETHER - interface
compatibility (voltage levels, logic families, protocols, connectors,
mechanical fit), material compatibility (galvanic, thermal, chemical),
module interoperability rules, and how to verify a pairing. The paste's rule
was applied by name/purpose/record schema/capabilities: judging pairings is
a distinct capability - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  component-compatibility-matrix           - The Component Compatibility
                                             Matrix Database (public-harvest:
                                             real, fact-checked compatibility
                                             engineering - every record a full
                                             compatibility-matrix entry with
                                             verdict rules, the numbers behind
                                             them, and verification
                                             procedures; standard references
                                             Horowitz and Hill The Art of
                                             Electronics 3rd ed 2015; JEDEC
                                             JESD8C LVCMOS; NXP UM10204 I2C;
                                             ISO 11898 CAN; IEEE 802.3
                                             Ethernet; IPC J-STD-001; IPC-2221;
                                             IPC-2152; IEC 60664-1; IEC
                                             61000-4-2; MIL-STD-889 galvanic;
                                             MIL-HDBK-217F; ISO 286 fits;
                                             IEC 60529 IP codes; JEDEC JESD79;
                                             ASME B1.1; ISO 898; Machinery's
                                             Handbook 31st ed 2020)
  component-compatibility-matrix-signature - The Component Compatibility
                                             Matrix Signature Database
                                             (his original Signature Handshake
                                             Method: every pairing a covenant,
                                             the matrix the ledger where
                                             handshakes are recorded,
                                             compatibility the honor kept
                                             between works; src signature,
                                             titles suffixed " (Signature
                                             Edition)", never presented as
                                             authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CPCM- (public) and JAH-CPCMS- (signature), verified free
in the manifest and in every shard index (zero hits; JAH-CPCT- belongs to the
Component and Parts Catalog database, a different capability entirely, so the
CPCM form was chosen to avoid substring confusion).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_component_compatibility_matrix.py). Every demo prints its
real computed values, asserts tight bounds (never float exact-equality), and
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
from entries_component_compatibility_matrix import ENTRIES, SIG_TAIL
from demos_component_compatibility_matrix import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Handshake Method: "
                "every pairing a covenant, the matrix the ledger where "
                "handshakes are recorded, and compatibility the honor kept "
                "between works. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked compatibility engineering: "
                "interface compatibility (voltage levels, logic families, "
                "protocols, connectors, mechanical fit), material compatibility "
                "(galvanic, thermal, chemical), module interoperability (power, "
                "grounding, RF, firmware, memory, sensors, motors, networks), "
                "and system-level practice (EMC, timing, derating, substitution, "
                "integration, verification, obsolescence) - every record "
                "carrying verdict rules, the numbers behind them, and "
                "verification procedures, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what compatibility means, reading and writing the matrix, the "
              "five dimensions, voltage levels, logic families, current and "
              "power, connector fit, protocols UART SPI I2C CAN USB Ethernet, "
              "impedance, tolerance and fits, reading two datasheets, material "
              "basics) -> Compounded (galvanic corrosion, thermal expansion, "
              "chemical and environmental, soldering and joining, power supply "
              "interoperability, grounding and shielding, battery chemistries, "
              "RF modules, firmware and API versions, memory and storage, "
              "displays and cameras, sensors, motors and drivers, network "
              "stacks) -> Advanced (EMC between modules, timing closure, "
              "derating and reliability, substitution matrices, system "
              "integration, verification testing, obsolescence, building your "
              "own matrix).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search voltage levels, logic families, I2C, CAN, galvanic corrosion, thermal expansion, EMC, timing, derating, substitution, connectors, grounding, batteries, RF modules...",
        "chat_ph": "Ask about component compatibility...",
        "archive_blurb": ("Seeded %s compatibility matrix records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled compatibility matrix studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about component compatibility - from what compatibility means through voltage levels, logic families, protocols, impedance, tolerance, and materials, through galvanic, thermal, joining, power, grounding, batteries, RF, firmware, memory, displays, sensors, motors, and networks, to EMC, timing, derating, substitution, integration, verification, and obsolescence." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "compatibility-matrix-study", "gen_demo_kind": "compatibility-matrix-demo",
        "source": source,
    }

CIT_PUB = ("Compatibility engineering (standard references: Horowitz P, "
           "Hill W. The Art of Electronics. 3rd ed. Cambridge University "
           "Press; 2015; Oberg E et al. Machinery's Handbook. 31st ed. "
           "Industrial Press; 2020; JEDEC JESD8C.01 LVCMOS; NXP UM10204 I2C; "
           "ISO 11898-1:2015 CAN; IEEE Std 802.3-2022 Ethernet; IPC J-STD-001H; "
           "IPC-2221B; IPC-2152; IEC 60664-1:2020; IEC 61000-4-2:2008; "
           "MIL-STD-889D dissimilar metals; MIL-HDBK-217F Notice 2 reliability "
           "prediction; ISO 286-1:2010 fits; IEC 60529:2013 IP codes; JEDEC "
           "JESD79-5A DDR5; ASME B1.1-2019 threads; ISO 898-1:2013 fasteners; "
           "IEC 60068-2 environmental testing; JEDEC JESD22-A114F ESD; "
           "MIL-STD-202H test methods).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Handshake "
                     "Method - every pairing a covenant, the matrix the ledger "
                     "where handshakes are recorded - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["component-compatibility-matrix"] = _cfg(
    "component-compatibility-matrix", "The Component Compatibility Matrix Database",
    "Judge whether parts, modules, materials, and interfaces work together: real, "
    "fact-checked compatibility engineering across interface compatibility, material "
    "compatibility, module interoperability, and system-level practice - every record "
    "carrying verdict rules, the numbers behind them, and verification procedures, "
    "taught progressively along the ladder.",
    "compatibility matrix record", "JAH-CPCM-", "JAH Component Compatibility Matrix Archivist",
    "component compatibility matrix archivist - judging whether parts, modules, "
    "materials, and interfaces work together across interface compatibility, material "
    "compatibility, module interoperability, and system-level practice; teaching "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["component-compatibility-matrix-signature"] = _cfg(
    "component-compatibility-matrix-signature", "The Component Compatibility Matrix Signature Database",
    "His original Signature Handshake Method: every pairing a covenant, the matrix the "
    "ledger where handshakes are recorded, compatibility the honor kept between works. "
    "The full ladder from what compatibility means through voltage levels, protocols, "
    "materials, and modules, to EMC, timing, derating, substitution, integration, "
    "verification, and obsolescence, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "compatibility matrix record", "JAH-CPCMS-", "JAH Component Compatibility Matrix Archivist (Signature)",
    "component compatibility matrix archivist - Signature editions: his original "
    "Signature Handshake Method, every pairing a covenant and the matrix the ledger "
    "where handshakes are recorded, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only "
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
    for slug in ("component-compatibility-matrix", "component-compatibility-matrix-signature"):
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
        assert "universal-build-specifications" not in page, "Build-210 #1 slug leftover in %s" % slug
        assert "component-parts-catalog" not in page, "Build-210 #2 slug leftover in %s" % slug
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
        assert "universal-build-specifications" not in gen_js, "Build-210 #1 slug leftover in gen js %s" % slug
        assert "component-parts-catalog" not in gen_js, "Build-210 #2 slug leftover in gen js %s" % slug
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
