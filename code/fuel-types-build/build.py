#!/usr/bin/env python3
"""Build The Fuel Types Database for JAH Databases
(Manon's order 2026-10-17 17:55 EDT, track 1 of 3: ESTABLISHED fuel types).

34 ladder-ordered records (rank 1-34, simple fuels -> complex systems):
what a fuel is, wood, charcoal, coal basics, coal grades, coke, peat,
kerosene, heating oil No. 2, fuel oil grades, natural gas, propane,
gasoline/octane, diesel/cetane, ethanol blends, E85, biodiesel, biodiesel
blends, methanol, avgas, jet fuel, LNG, CNG, hydrogen production (SMR),
hydrogen use, natural uranium, enriched uranium, nuclear fuel cycle,
naphtha, the refinery, blending/additives, bunker fuel, storage/safety,
energy-density framework.

Dedupe: 2026-10-17 - all 68 titles checked against the whole system via
code/dedupe_gate.py (manifest 2,602 databases + global exact shards):
zero collisions, zero refusals. Sibling tracks (emerging, speculated)
are built by sibling workers; this builder's titles are established-only.

Two NEW databases, 34 ladder-ordered records each:

  fuel-types                 - The Fuel Types Database
                               (public-harvest: real, fact-checked fuel
                               knowledge - properties, production, uses,
                               handling/safety, energy density)
  fuel-types-signature       - The Fuel Types Signature Database
                               (his original Signature fuel-system
                               designs, optimization frameworks, and
                               comparative analyses; src signature,
                               titles suffixed " (Signature Edition)",
                               never presented as authentic public
                               record)

ID prefixes: JAH-FUEL- (public) and JAH-FUELS- (signature), verified
free in the manifest id_prefix values and with zero hits in every
shard index file (grep over data-1 and main data dirs, 2026-10-17).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_fuel_types.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends
with the OK marker; the build machine-executes all 68 demos.

Concurrency: this builder writes ONLY its own new untracked paths -
db/fuel-types/, db/fuel-types-signature/, code/fuel-types-build/,
the data-1 shard dirs (data/fuel-types/, data/fuel-types-signature/),
and the fragment file. It never touches data/manifest.json, api.json,
index.html, README.md, docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those.

No website references. No Facebook. Screened per the canon.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/fuel-types.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_fuel_types import ENTRIES, SIG_TAIL
from demos_fuel_types import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, greet, source):
    sig_line = ("Signature originals - his original Signature fuel-system "
                "designs, optimization frameworks, and comparative analyses "
                "for every established fuel, from the Signature fuel "
                "taxonomy and Energy Ledger through the Signature blend "
                "optimizer to the Signature fuel selection framework. "
                "Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked fuel knowledge: "
                "properties, production, uses, handling and safety, and "
                "energy density for every established fuel type - organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a fuel is, wood, charcoal, coal basics, coal grades, "
              "coke, peat, kerosene, heating oil No. 2, fuel oil grades, "
              "natural gas, propane) -> Compounded (gasoline and octane, "
              "diesel and cetane, ethanol blends, E85, biodiesel, biodiesel "
              "blends, methanol, aviation gasoline, jet fuel, LNG, CNG, "
              "hydrogen production, hydrogen use) -> Advanced (natural "
              "uranium, enriched uranium, the nuclear fuel cycle, naphtha "
              "streams, the refinery, blending and additives, bunker fuel, "
              "storage and safety systems, the energy-density framework).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role, "greet": greet,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search gasoline, diesel, octane, cetane, coal, natural gas, propane, ethanol, biodiesel, jet fuel, hydrogen, uranium, refinery, bunker fuel...",
        "chat_ph": "Ask about established fuel types...",
        "archive_blurb": ("Seeded %s fuel-type records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled fuel-type studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "fuel-types-study", "gen_demo_kind": "fuel-types-demo",
        "source": source,
    }

ROLE_PUB = ("Fuel archivist - established fuel types taught progressively along the ladder "
  "from what a fuel is through wood, charcoal, coal, petroleum distillates, and gaseous fuels, "
  "through gasoline, diesel, biofuels, methanol, aviation fuels, LNG, CNG, and hydrogen, "
  "to uranium, refining systems, bunker fuel, safety systems, and the energy-density framework; "
  "answers from many angles - definition, example, analogy, application, history, math, how-to - "
  "using only archive data from this system")
GREET_PUB = ("I am the JAH Fuel Types Archivist. Ask me about established fuels - from wood and coal "
  "through gasoline, diesel, natural gas, propane, biofuels, jet fuel, hydrogen, and uranium, "
  "to refineries, bunker fuel, storage safety, and energy-density comparisons.")
ROLE_SIG = ("Fuel archivist - Signature editions: his original Signature fuel-system designs, "
  "optimization frameworks, and comparative analyses for every established fuel, clearly labeled "
  "Signature-made and never presented as authentic public record; teaches progressively along the ladder "
  "from foundations through compounded to advanced; answers from many angles - definition, example, "
  "analogy, application, history, math, how-to - using only archive data from this system")
GREET_SIG = ("I am the JAH Fuel Types Archivist (Signature). Ask me about his original Signature "
  "fuel-system designs and optimization frameworks - from the Signature fuel taxonomy through blend "
  "optimization to the Signature fuel selection framework. Clearly labeled Signature-made.")

DBCFG = {}
DBCFG["fuel-types"] = _cfg(
    "fuel-types", "The Fuel Types Database",
    "Established fuel types: the real, fact-checked properties, production, uses, handling and "
    "safety, and energy density of every established fuel - from wood, coal, and kerosene through "
    "gasoline, diesel, natural gas, biofuels, jet fuel, and hydrogen to uranium and the refinery "
    "systems that make them - taught progressively along the ladder.",
    "fuel type record", "JAH-FUEL-", "JAH Fuel Types Archivist",
    ROLE_PUB, GREET_PUB, "public")
DBCFG["fuel-types-signature"] = _cfg(
    "fuel-types-signature", "The Fuel Types Signature Database",
    "His original Signature fuel-system designs, optimization frameworks, and comparative analyses "
    "for every established fuel: the Signature fuel taxonomy, the Signature Energy Ledger, blend "
    "optimization, and the Signature fuel selection framework. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "fuel type record", "JAH-FUELS-", "JAH Fuel Types Archivist (Signature)",
    ROLE_SIG, GREET_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"

TIER_LABEL = {"foundations": "Foundations", "compounded": "Compounded", "advanced": "Advanced"}


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
    frag = {"public": {}, "signature": {}}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        side = "signature" if slug.endswith("-signature") else "public"
        frag[side] = {
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
            "source": "signature" if side == "signature" else "public-harvest",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
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
    for slug in ("fuel-types", "fuel-types-signature"):
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
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # ladder ranks must be exactly 1..34 in order
    for slug, recs in built.items():
        ranks = [r["ladder_rank"] for r in recs]
        assert ranks == list(range(1, 35)), "ladder not 1-34 in %s" % slug

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
        gen_marker = ("Generate structural synthetic intelligence studies. "
                      "Seeded archive records are the authoritative entries.")
        if gen_marker in page:
            page = page.replace(gen_marker, DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "fuel-types" in page or "fuel_types" in page or "Fuel Types" in page
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            tier = TIER_LABEL[r["ladder_tier"]]
            topics.setdefault(tier, []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower()
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)
    print("records: %d public + %d signature = %d total" %
          (len(built["fuel-types"]),
           len(built["fuel-types-signature"]), total))
    print("NOTE: manifest.json / api.json / restamp left to the merger; no commit, no push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
