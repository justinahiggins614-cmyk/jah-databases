#!/usr/bin/env python3
"""Build the Sumo Combat databases for JAH Databases (combat batch 2).

Verified 2026-10-17: RAW SWEEP over the full manifest plus every shard
index title in jah-databases-data-1 plus the main-repo data dir: zero
'combat-sumo*' slugs/names; zero title collisions for all 68 titles
(34 public + 34 " (Signature Edition)") through the whole-system dedupe
gate BEFORE authoring: zero refusals. Existing combat/martial-arts
databases cover karate forms, green-beret material, and self-defense
knowledge; none teaches Japanese sumo fundamentals, shiko training, or
the 82 kimarite winning techniques with step-by-step body mechanics, so
BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-sumo                  - The Sumo Combat Database
                                 (public-harvest: real, fact-checked Japanese
                                 sumo: shiko and basic training, stance and
                                 footwork, and the 82 kimarite winning
                                 techniques - pushes, throws, leg trips -
                                 each record carrying step-by-step body
                                 mechanics; standard references: the Nihon
                                 Sumo Kyokai official kimarite list, dohyo
                                 dimensions and bout rules, stable training
                                 practices)
  combat-sumo-signature        - The Sumo Combat Signature Database
                                 (his original Signature Sumo Method: the
                                 dohyo the field of work, the tachiai the
                                 oath of engagement, each kimarite a signed
                                 technique of balance taken and balance
                                 kept; src signature, titles suffixed
                                 " (Signature Edition)", never presented as
                                 authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBSUM- (public) and JAH-CBSUMS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_sumo.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md and never commits or pushes.
It only writes: db/combat-sumo[/-signature]/ (index.html + gen-*.js),
the shard data dirs, and the fragment file. The merger handles the rest.

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
from entries_combat_sumo import ENTRIES, SIG_TAIL
from demos_combat_sumo import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Sumo Method: "
                "the dohyo the field of work, the tachiai the oath of "
                "engagement, each kimarite a signed technique of balance "
                "taken and balance kept. Clearly labeled Signature-made, "
                "never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Japanese sumo: shiko "
                "and basic training, the kamae stance and suri-ashi "
                "footwork, teppo striking, butsukari impact work, the "
                "yotsu belt grips, and the 82 kimarite winning techniques "
                "- pushes, thrusts, throws, and leg trips - every record "
                "carrying step-by-step body mechanics, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the kamae stance, shiko leg stomps, suri-ashi sliding "
              "footwork, teppo striking post, matawari splits, the tachiai "
              "charge, butsukari impact training, the hidari-yotsu and "
              "migi-yotsu belt grips) -> Compounded (oshi-dashi, "
              "oshi-taoshi, tsuki-dashi, tsuki-taoshi, okuri-dashi, "
              "okuri-taoshi, hatakikomi, hiki-otoshi, sukuinage, "
              "uwate-nage, shitate-nage, kote-nage, kubi-nage, sotogake) "
              "-> Advanced (uchigake, kirikaeshi, watashikomi, yori-kiri, "
              "yori-taoshi, uwatedashi-nage, shitatedashi-nage, katasukashi, "
              "utchari, tsuri-otoshi, kawazugake, izori).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search shiko, kamae, suri-ashi, teppo, tachiai, yotsu, oshi-dashi, tsuki-dashi, uwate-nage, shitate-nage, sotogake, yori-kiri, utchari, kimarite...",
        "chat_ph": "Ask about sumo...",
        "archive_blurb": ("Seeded %s sumo combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled sumo technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about sumo - from the kamae stance, shiko stomps, suri-ashi footwork, teppo striking, matawari splits, the tachiai charge, butsukari impact work, and the yotsu belt grips, through the pushing and thrusting kimarite, the slap and pull counters, the great belt throws, and the leg trips, to the advanced force-outs, edge reversals, lifts, and special techniques." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "sumo-study", "gen_demo_kind": "sumo-demo",
        "source": source,
    }

CIT_PUB = ("Japanese sumo (standard references: Nihon Sumo Kyokai (Japan "
           "Sumo Association) official 82 kimarite list - kihonwaza, "
           "nagewaza, kakewaza, hineriwaza, soritewaza, tokushuwaza; dohyo "
           "dimensions and bout rules - 4.55 m ring, tawara straw bales; "
           "stable training practices - asageiko, shiko, teppo, "
           "butsukari-geiko, moshiai-geiko; sumo history from the Kojiki "
           "chronicles (712 CE) through the Edo period to the modern "
           "honbasho tournament system).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Sumo "
                     "Method - the dohyo the field of work, the tachiai the "
                     "oath of engagement, each kimarite a signed technique "
                     "of balance taken and balance kept - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["combat-sumo"] = _cfg(
    "combat-sumo", "The Sumo Combat Database",
    "Japanese sumo, taught step by step: shiko and basic training, the "
    "stance, footwork, and belt grips, and the 82 kimarite winning "
    "techniques - pushes, thrusts, throws, and leg trips - every record a "
    "full technique with how to do it, in body-mechanic detail, ordered "
    "along the teaching ladder from foundations to the advanced "
    "specials.",
    "combat technique record", "JAH-CBSUM-", "JAH Sumo Combat Archivist",
    "sumo combat archivist - teaching Japanese sumo from the kamae stance "
    "through shiko, suri-ashi, teppo, matawari, tachiai, butsukari, and "
    "the yotsu grips, through the pushing, thrusting, slap, pull, throw, "
    "and leg-trip kimarite, to the advanced force-outs, edge reversals, "
    "lifts, and special techniques; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-sumo-signature"] = _cfg(
    "combat-sumo-signature", "The Sumo Combat Signature Database",
    "His original Signature Sumo Method: the dohyo the field of work, the "
    "tachiai the oath of engagement, each kimarite a signed technique of "
    "balance taken and balance kept. The full ladder from stance and "
    "shiko through the pushing and thrusting kimarite, the counters, "
    "throws, and leg trips, to the advanced force-outs, reversals, lifts, "
    "and specials, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "combat technique record", "JAH-CBSUMS-", "JAH Sumo Combat Archivist (Signature)",
    "sumo combat archivist - Signature editions: his original Signature "
    "Sumo Method, the dohyo the field of work and each kimarite a signed "
    "technique of balance taken and balance kept, clearly labeled "
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
    for slug in ("combat-sumo", "combat-sumo-signature"):
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
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    print("manifest/api/index updates SKIPPED (merger-owned).")
    print("NEXT: merger runs restamp_counts.py, then commits + pushes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
