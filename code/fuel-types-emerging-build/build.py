#!/usr/bin/env python3
"""Build The Emerging Fuel Types Database (fuel track 2 of 3, 2026-10-17).

Manon's 2026-10-17 17:55 order: "New types of fuel databases" - track 2:
NEW/EMERGING fuel types. Track 1 (established) and track 3 (speculated)
are sibling builds; this build keeps its records strictly to emerging
fuels: e-fuels/synthetic electrofuels, green hydrogen, green ammonia,
sustainable aviation fuel, algae biofuels, renewable diesel (HVO),
biomethane, dimethyl ether, formic acid carriers, LOHC, solid-oxide fuel
cell fuels, iron-air/metal energy carriers, advanced cellulosic ethanol,
pyrolysis bio-oils, waste-to-fuel pathways.

So this build creates two NEW databases, 34 ladder-ordered records each:

  fuel-types-emerging            - The Emerging Fuel Types Database
                                   (public-harvest: real, fact-checked
                                   emerging-fuel knowledge - status, TRL,
                                   production routes, honest maturity
                                   framing; pilot-stage technology is never
                                   presented as deployed; standard
                                   references: IEA, IRENA, U.S. DOE, NREL,
                                   ASTM, ISO, ICAO CORSIA, plus the
                                   landmarks cited per record)
  fuel-types-emerging-signature  - The Emerging Fuel Types Signature Database
                                   (his original Signature fuel designs and
                                   pathway analyses: Signature
                                   re-engineerings of each emerging
                                   pathway - optimized reactor concepts,
                                   Signature efficiency analyses, original
                                   deployment designs; src signature,
                                   titles suffixed " (Signature Edition)",
                                   never presented as authentic public
                                   record)

34 records each, ladder_rank 1-34 (foundations 1-12 / compounded 13-23 /
advanced 24-34); the shard index is written in ladder order so pages
present simple -> compounded -> complex.

Dedupe 2026-10-17: all 68 titles checked against the WHOLE system via
code/dedupe_gate.py before authoring: zero collisions, zero refusals.
ID prefixes JAH-FUE- / JAH-FUES- verified free in the manifest
id_prefix values and in every data-1 shard index record ID (zero hits);
fuel-types-emerging slugs absent from the manifest and from data-1.
Distinct from track 1 (fuel-types) and track 3 (fuel-types-speculated)
by title and subject.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_fuel_emerging.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker naming the record; the build machine-executes all 68 demos.

Screened: nothing hate-adjacent, profane, or inappropriate; no religious
talk. Nothing on neutralizing or defeating military or defense-grade
systems. No website references. No Facebook.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
It writes only db/fuel-types-emerging[-signature]/,
code/fuel-types-emerging-build/, and the data-1 shard dirs. A merger
handles the manifest; the fragment is written by this build's final step.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

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
from entries_fuel_emerging import ENTRIES, SIG_TAIL
from demos_fuel_emerging import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature fuel designs "
                "and pathway analyses: Signature re-engineerings of each "
                "emerging pathway - optimized reactor concepts, Signature "
                "efficiency analyses, and original deployment designs. "
                "Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked emerging-fuel "
                "knowledge: green hydrogen, green ammonia, e-methanol, "
                "power-to-liquid e-fuels, synthetic methane, sustainable "
                "aviation fuel (HEFA, alcohol-to-jet, Fischer-Tropsch), "
                "renewable diesel, cellulosic ethanol, biomethane, bio-LNG, "
                "algae and seaweed biofuels, pyrolysis bio-oils, HTL "
                "bio-crude, waste gasification, used cooking oil fuels, "
                "plastic pyrolysis, bio-butanol, marine biofuels, "
                "methanol-to-gasoline, dimethyl ether, formic acid "
                "carriers, LOHC, ammonia cracking and combustion, "
                "solid-oxide fuel cell fuels, iron powder combustion, "
                "co-electrolysis e-kerosene, microbial electrosynthesis, "
                "solar thermochemical fuels, and artificial photosynthesis - "
                "with status, technology readiness, production routes, and "
                "honest maturity framing, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(green hydrogen, green ammonia, e-methanol, power-to-liquid "
              "e-fuels, synthetic methane, SAF via HEFA, SAF via "
              "alcohol-to-jet, SAF via Fischer-Tropsch, renewable diesel, "
              "cellulosic ethanol, biomethane, bio-LNG) -> Compounded "
              "(algae biofuels, seaweed biofuels, fast pyrolysis bio-oils, "
              "catalytic pyrolysis oils, HTL bio-crude, waste gasification, "
              "used cooking oil fuels, plastic pyrolysis, bio-butanol, "
              "marine biofuels, methanol-to-gasoline) -> Advanced (dimethyl "
              "ether, formic acid carriers, LOHC, ammonia cracking, "
              "ammonia combustion, solid-oxide fuel cell fuels, iron powder "
              "combustion, co-electrolysis e-kerosene, microbial "
              "electrosynthesis, solar thermochemical fuels, artificial "
              "photosynthesis).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search green hydrogen, ammonia, e-methanol, e-fuels, SAF, HEFA, renewable diesel, biomethane, algae, pyrolysis, DME, LOHC, fuel cells...",
        "chat_ph": "Ask about emerging fuels...",
        "archive_blurb": ("Seeded %s emerging-fuel records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled emerging-fuel studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about emerging fuels - from green hydrogen, green ammonia, e-methanol, power-to-liquid e-fuels, and synthetic methane, through HEFA, alcohol-to-jet, and Fischer-Tropsch SAF, renewable diesel, cellulosic ethanol, biomethane, and bio-LNG, to algae and seaweed biofuels, pyrolysis oils, HTL bio-crude, waste gasification, DME, formic acid carriers, LOHC, ammonia cracking and combustion, solid-oxide fuel cells, iron powder combustion, co-electrolysis e-kerosene, microbial electrosynthesis, solar thermochemical fuels, and artificial photosynthesis." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "emerging-fuel-study", "gen_demo_kind": "emerging-fuel-demo",
        "source": source,
    }

CIT_PUB = ("Emerging fuel pathways (standard references: International "
           "Energy Agency. Global Hydrogen Review 2024; Energy Technology "
           "Perspectives 2024; International Renewable Energy Agency. "
           "Green Hydrogen Cost Reduction; Innovation Outlook: Renewable "
           "Ammonia; U.S. Department of Energy. Hydrogen Shot; Bioenergy "
           "Technologies Office Multi-Year Program Plan; National Renewable "
           "Energy Laboratory techno-economic analyses; ASTM D7566 "
           "aviation turbine fuel with synthesized hydrocarbons; ASTM D975 "
           "diesel fuel; EN 15940 paraffinic diesel; ISO 14687 hydrogen "
           "fuel quality; ISO 15403 natural gas vehicle fuel; ICAO CORSIA "
           "eligible fuels life-cycle methodology). Pilot-stage "
           "technologies are identified as such and never presented as "
           "deployed.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature fuel "
                     "designs and pathway analyses - Signature "
                     "re-engineerings with optimized reactor concepts, "
                     "Signature efficiency analyses, and original "
                     "deployment designs - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["fuel-types-emerging"] = _cfg(
    "fuel-types-emerging", "The Emerging Fuel Types Database",
    "New and emerging fuel types: green hydrogen, green ammonia, "
    "e-methanol, power-to-liquid e-fuels, synthetic methane, sustainable "
    "aviation fuel, renewable diesel, cellulosic ethanol, biomethane, "
    "bio-LNG, algae and seaweed biofuels, pyrolysis bio-oils, HTL "
    "bio-crude, waste-to-fuel pathways, dimethyl ether, formic acid "
    "carriers, LOHC, ammonia cracking and combustion, solid-oxide fuel "
    "cell fuels, iron powder combustion, co-electrolysis e-kerosene, "
    "microbial electrosynthesis, solar thermochemical fuels, and "
    "artificial photosynthesis - real documented pathways with honest "
    "maturity framing, ladder-ordered from foundations to the research "
    "frontier.",
    "emerging fuel record", "JAH-FUE-", "JAH Emerging Fuels Archivist",
    "emerging fuels archivist - teaching new fuel pathways step by step: "
    "status, technology readiness, production routes, energy balances, and "
    "honest maturity framing; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_PUB, "public")
DBCFG["fuel-types-emerging-signature"] = _cfg(
    "fuel-types-emerging-signature", "The Emerging Fuel Types Signature Database",
    "His original Signature fuel designs and pathway analyses: Signature "
    "re-engineerings of every emerging fuel pathway - optimized reactor "
    "concepts, Signature efficiency analyses, and original deployment "
    "designs for green hydrogen, e-fuels, SAF, biofuels, hydrogen "
    "carriers, and frontier conversion concepts. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "emerging fuel record", "JAH-FUES-", "JAH Emerging Fuels Archivist (Signature)",
    "emerging fuels archivist - Signature editions: his original "
    "Signature fuel designs and pathway analyses, Signature "
    "re-engineerings with optimized reactor concepts and efficiency "
    "analyses, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
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


def node_check(path, label):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    assert p.returncode == 0, "node --check failed for %s: %s" % (label, p.stderr[-500:])


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
    for slug in ("fuel-types-emerging", "fuel-types-emerging-signature"):
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
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
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

    # cross-check entry text vs demo outputs: demo OK markers must name the record
    for slug, recs in built.items():
        for r in recs:
            p = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                               capture_output=True, text=True, timeout=60)
            ok_line = [l for l in p.stdout.splitlines() if l.startswith("OK:")]
            assert ok_line and r["name"] in ok_line[0], \
                "demo/text mismatch in %s: %s" % (r["id"], ok_line)

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
        assert "facebook" not in gen_js.lower()
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        # JS hygiene: node --check the gen file and every inline page script
        node_check(gpath, "gen-%s.js" % slug)
        scripts = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>",
                             page, re.S | re.I)
        with open(ppath, "r", encoding="utf-8") as f:
            swept_page = f.read()
        scripts = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>",
                             swept_page, re.S | re.I)
        # drop non-JS script blocks (JSON-LD etc.): keep typeless or JS-typed only
        typed = re.findall(r"<script(?![^>]*\bsrc=)([^>]*)>",
                           swept_page, re.S | re.I)
        js_scripts = []
        for attrs, body in zip(typed, scripts):
            m = re.search(r'\btype\s*=\s*["\']([^"\']+)["\']', attrs, re.I)
            if m and "json" in m.group(1).lower():
                continue
            if m and not any(k in m.group(1).lower()
                             for k in ("javascript", "ecmascript", "module")):
                continue
            js_scripts.append(body)
        scripts = js_scripts
        for i, body in enumerate(scripts):
            if not body.strip():
                continue
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                tf.write(body)
                tpath = tf.name
            try:
                node_check(tpath, "%s inline script %d" % (slug, i))
            finally:
                os.unlink(tpath)
        print("page:  db/%s/index.html + gen-%s.js [%s] [js: %d inline scripts node-clean]"
              % (slug, slug, ", ".join(notes), len(scripts)), flush=True)

    # NOTE (concurrency): manifest.json and api.json are owned by the merger.
    # This build does not touch them. Fragment for the merger:
    for slug, recs in built.items():
        print("fragment-ready: %-38s %d records" % (slug, len(recs)), flush=True)
    print("NEXT: merger runs restamp + commit. This build committed nothing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
