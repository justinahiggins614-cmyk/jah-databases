#!/usr/bin/env python3
"""Build the Speculated Fuel Types databases for JAH Databases
(Manon's 2026-10-17 17:55 EDT order - track 3 of 3: SPECULATED/THEORETICAL
fuel types).

Creates two NEW databases, 34 ladder-ordered records each:
  fuel-types-speculated            - The Speculated Fuel Types Database
                                     (src public-harvest: documents the
                                     SPECULATION ITSELF factually - who
                                     proposed it, the physics claims, why
                                     it is unproven)
  fuel-types-speculated-signature  - The Speculated Fuel Types Signature
                                     Database
                                     (src signature: his original
                                     Signature theoretical explorations;
                                     titles suffixed " (Signature Edition)")

CRITICAL LABELING: every record carries the exact label
"Signature-generated speculative concept - not established fact" in its
description (asserted for every record, both halves). Nothing is
presented as real, working, or validated technology.

ID prefixes: JAH-FUSPEC- (public) and JAH-FUSPECS- (signature). The
planner-suggested JAH-FUS- collides with manifest id_prefix JAH-FUS-REACT
(fusion-reactors), so the suffix was extended per the task. Both
prefixes verified zero hits across all 2,590 non-empty manifest
id_prefix values and all record IDs in jah-databases-data-1.

Dedupe pre-check 2026-10-17: all 68 titles (34 public + 34 Signature
Edition) checked against the whole-system dedupe gate before authoring -
68/68 admitted, zero refusals.

CONCURRENCY: this script NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. A merger handles those. It only creates new untracked paths.

Never the words "bat belt" anywhere. No website references. No Facebook.
Nothing on neutralizing/defeating military or defense-grade systems.
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
from entries_fuel_types_speculated import (
    ENTRIES, PUB_LABEL, PUB_DOC, SIG_LABEL, SIG_TAIL)
from demos_fuel_types_speculated import DEMOS

LABEL_A = "signature-generated speculative concept"
LABEL_B = "not established fact"

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature theoretical "
                "explorations of speculative fuel concepts: the speculation "
                "spectrum as a ladder of kept promises, the rocket equation "
                "as the covenant of momentum, each fuel read through "
                "Signature science. Clearly labeled Signature-made "
                "speculative concepts - not established fact, never "
                "presented as authentic public record or working technology.")
    pub_line = ("Public records - the SPECULATION ITSELF documented as "
                "fact: who proposed each concept, the physics claims made "
                "for it, and why it is unproven. Metallic hydrogen, "
                "antimatter catalysis and annihilation, fusion fuel cycles "
                "(D-T, D-D, D-He3, He3-He3, p-B11, muon-catalyzed), "
                "positronium, Bussard ramjets and variants, fusion ramjets, "
                "inertial-confinement pellets, magnetized target fusion, "
                "z-pinches, quark matter, strangelets, negative mass, "
                "zero-point schemes, Casimir cavities, black-hole power, "
                "kugelblitz holes, dark matter annihilation, false vacuum, "
                "warp-drive and wormhole requirements, exotic matter "
                "sourcing, white holes, cosmic strings, and the Kardashev "
                "fuel ladder. Nothing here is real, working, or validated "
                "technology.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the speculation spectrum, the rocket equation, D-T, D-D, "
              "D-He3, He3-He3, p-B11 and muon-catalyzed fusion fuels, "
              "metallic hydrogen, antimatter-catalyzed and pure antimatter "
              "fuel, positronium) -> Compounded (Bussard ramjet fuel, "
              "ram-augmented variants, fusion ramjets, inertial-confinement "
              "micro-fusion pellets, magnetized target fusion, z-pinch and "
              "dense plasma focus concepts, quark matter, strangelets, "
              "strange-matter conversion, negative-mass propellants, "
              "zero-point energy schemes, Casimir cavity energy) -> "
              "Advanced (Hawking-radiation black-hole power, kugelblitz "
              "black holes, dark matter annihilation, false-vacuum energy, "
              "warp-drive fuel requirements, wormhole exotic-matter "
              "requirements, exotic matter sourcing, white holes, cosmic "
              "strings, the Kardashev fuel ladder).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s Every record is labeled: Signature-generated speculative concept "
                  "- not established fact." % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search metallic hydrogen, antimatter, D-T fusion, He-3, Bussard ramjet, black-hole power, quark matter, zero-point energy, warp drive...",
        "chat_ph": "Ask about speculative fuel concepts...",
        "archive_blurb": ("Seeded 34 %s speculative fuel records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced. "
                          "Every record is labeled: Signature-generated speculative concept - not "
                          "established fact."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled speculative fuel studies. Seeded archive records are the authoritative entries. Every generated sample is labeled speculative - not established fact.",
        "greet": "I am the %s. Ask me about speculative fuel concepts - from the speculation spectrum and the rocket equation through D-T, D-D, D-He3, He3-He3, p-B11 and muon-catalyzed fusion, metallic hydrogen, antimatter catalysis and pure antimatter, positronium, Bussard ramjets and their variants, fusion ramjets, ICF pellets, magnetized target fusion, z-pinches, quark matter, strangelets, negative mass, zero-point schemes and Casimir cavities, to black-hole power, kugelblitz holes, dark matter annihilation, false vacuum, warp-drive and wormhole requirements, exotic matter sourcing, white holes, cosmic strings, and the Kardashev fuel ladder. I document speculation honestly: who proposed it, what is claimed, and why it is unproven - never presented as working technology." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "speculated-fuel-study", "gen_demo_kind": "speculated-fuel-demo",
        "source": source,
    }

FUS_CIT_PUB = ("Speculative fuel concepts (standard references: Tsiolkovsky "
               "KE. 1903; Lawson JD. Proc Phys Soc B 1957;70:6-10; Wigner E, "
               "Huntington HB. J Chem Phys 1935;3:764-770; Alvarez LW et al. "
               "Phys Rev 1957;105:1127-1128; Bussard RW. Astronautica Acta "
               "1960;6:179-194; Bond A et al. J Brit Interplanet Soc "
               "1978;31:S5-S7; Alcubierre M. Class Quantum Grav "
               "1994;11:L73-L77; Pfenning MJ, Ford LH. Class Quantum Grav "
               "1997;14:1743-1751; Witten E. Phys Rev D 1984;29:272-276; "
               "Bondi H. Rev Mod Phys 1957;29:423-428; Coleman S, De Luccia "
               "F. Phys Rev D 1980;21:3305-3315; Morris MS, Thorne KS. Am J "
               "Phys 1988;56:395-412; Casimir HBG. Proc K Ned Akad Wet "
               "1948;51:793-795; Hawking SW. Nature 1974;248:30-31; Forward "
               "RL. AFRPL TR-85-034; 1985; Crane L, Westmoreland S. "
               "arXiv:0908.1803; 2009; Kardashev NS. Soviet Astronomy "
               "1964;8:217-221; Abu-Shawareb H et al. Phys Rev Lett "
               "2024;132:065102; Deutsch M. Phys Rev 1951;82:455-456; "
               "Jungman G et al. Phys Rep 1996;267:195-373; Rostoker N et "
               "al. Science 1997;278:1419-1422; Visser M. Lorentzian "
               "Wormholes. AIP Press; 1995; Wittenberg LJ et al. Fusion "
               "Technology 1986;10:167-178; and the other landmarks cited "
               "per record). Every record labeled: Signature-generated "
               "speculative concept - not established fact.")
FUS_CIT_SIG = FUS_CIT_PUB + (" Signature editions are his original "
                             "Signature theoretical explorations - clearly "
                             "labeled Signature-made speculative concepts, "
                             "never presented as authentic public record or "
                             "working technology.")

DBCFG = {}
DBCFG["fuel-types-speculated"] = _cfg(
    "fuel-types-speculated", "The Speculated Fuel Types Database",
    "Speculative and theoretical fuel concepts - metallic hydrogen, "
    "antimatter, fusion fuel cycles, Bussard ramjets, black-hole power, "
    "quark matter, zero-point schemes, warp-drive requirements and more - "
    "documented as speculation: who proposed each concept, the physics "
    "claims, and why it is unproven. Nothing here is real, working, or "
    "validated technology.",
    "speculated fuel record", "JAH-FUSPEC-", "JAH Speculated Fuels Archivist",
    "speculated fuels archivist - speculative and theoretical fuel concepts "
    "documented as speculation: proposer, physics claims, and why unproven; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system; never presents speculation as working "
    "technology",
    FUS_CIT_PUB, "public")
DBCFG["fuel-types-speculated-signature"] = _cfg(
    "fuel-types-speculated-signature", "The Speculated Fuel Types Signature Database",
    "His original Signature theoretical explorations of speculative fuel "
    "concepts - the speculation spectrum as a ladder of kept promises, "
    "the rocket equation as the covenant of momentum, each fuel read "
    "through Signature science. Clearly labeled Signature-made "
    "speculative concepts - not established fact, never presented as "
    "authentic public record or working technology.",
    "speculated fuel record", "JAH-FUSPECS-", "JAH Speculated Fuels Archivist (Signature)",
    "speculated fuels archivist - Signature editions: his original "
    "Signature theoretical explorations of speculative fuel concepts, the "
    "speculation spectrum as a ladder of kept promises and the rocket "
    "equation as the covenant of momentum, clearly labeled Signature-made "
    "and never presented as authentic public record or working technology; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    FUS_CIT_SIG, "signature")

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
            description = (SIG_LABEL + e["sig_lens"] + " " + e["description"]
                           + " " + SIG_TAIL)
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"])
        else:
            description = PUB_LABEL + PUB_DOC + e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        # CRITICAL LABELING AUDIT: every record carries the exact label
        dl = description.lower()
        assert LABEL_A in dl and LABEL_B in dl, \
            "speculative label missing in %s" % rid
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
    for slug in ("fuel-types-speculated", "fuel-types-speculated-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        assert [r["ladder_rank"] for r in recs] == list(range(1, 35)), \
            "ladder must be 1-34 in order for %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            dl = r["description"].lower()
            assert LABEL_A in dl and LABEL_B in dl, "label missing in %s" % r["id"]
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
        cfg = DBCFG[slug]
        # apostrophe-free JS config strings (single-quoted JS literals)
        for k in ("name", "ai", "role", "record_kind"):
            assert "'" not in cfg[k], "apostrophe in JS config %s" % k
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            cfg["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "mergePanel" in page, "mergePanel missing"
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
        gen_js = nb.build_gen_js(slug, topics, cfg)
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        nc = subprocess.run(["node", "--check", gpath],
                            capture_output=True, text=True, timeout=60)
        assert nc.returncode == 0, "node --check failed %s: %s" % (gpath, nc.stderr[-500:])
        print("page:  db/%s/index.html + gen-%s.js [%s] node-check clean"
              % (slug, slug, ", ".join(notes)), flush=True)

    # NOTE: manifest.json / api.json updates are owned by the merger - not touched here.
    print("records built: %d databases, %d records" % (len(built), total))
    print("NEXT (merger): manifest + api.json entries, restamp, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
