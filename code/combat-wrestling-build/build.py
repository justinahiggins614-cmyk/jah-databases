#!/usr/bin/env python3
"""Build the Wrestling Combat databases for JAH Databases (combat batch 2).

Verified 2026-10-17 (combat batch 2): RAW SWEEP over the full manifest
(2,410 databases) PLUS every shard index in jah-databases-data-1 PLUS the
main-repo data dir: zero 'combat-wrestling' slugs/names; zero wrestling
title collisions across all 68 titles (whole-system dedupe_gate check, 0
refusals). ID prefixes JAH-CBWR- (public) and JAH-CBWRS- (signature)
verified free in the manifest id_prefix values and in every shard index.

Two NEW databases, 34 ladder-ordered records each:

  combat-wrestling             - The Wrestling Combat Database
                                 (public-harvest: real, fact-checked
                                 freestyle and Greco-Roman wrestling
                                 technique - stance and motion, clinch ties,
                                 takedown defense and escapes, shots
                                 (single and double leg), clinch attacks,
                                 throws, par terre turns, reversals, and
                                 combination systems - every record a
                                 technique with step-by-step body
                                 mechanics; standard references United
                                 World Wrestling International Wrestling
                                 Rules; NCAA Wrestling Rules; Gable
                                 Coaching Wrestling Successfully 1999)
  combat-wrestling-signature   - The Wrestling Combat Signature Database
                                 (his original Signature Combat Method: the
                                 mat the proving ground, stance the oath,
                                 every technique a Signature discipline of
                                 leverage and will, the chain the creed;
                                 src signature, titles suffixed
                                 " (Signature Edition)", never presented as
                                 authentic public record)

34 records each, teaching ladder (ladder_rank 1-10, ladder_tier
foundations/compounded/advanced), shard index written in ladder order:
simple -> compounded -> complex.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md and never commits or pushes.
It writes only: db/combat-wrestling[/-signature]/ (index.html + gen JS),
the data-1 shard dirs, code/combat-wrestling-build/, and the merger
fragment at ~/workspace/hidden_files/missing-builds/fragments/
combat-wrestling.json. The merger handles manifest/api/counts/commit.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_wrestling.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian martial-arts instruction only.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-wrestling.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_wrestling import ENTRIES, SIG_TAIL
from demos_combat_wrestling import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat Method: "
                "the mat the proving ground, stance the oath, every "
                "technique a Signature discipline of leverage and will, "
                "the chain the creed. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked freestyle and "
                "Greco-Roman wrestling technique: stance and motion, clinch "
                "ties (collar tie, underhook, overhook, two-on-one), "
                "takedown defense and escapes (sprawl, whizzer, stand-up, "
                "par terre defense), shots (double leg, high single, ankle "
                "pick, low single), clinch attacks (arm drag, snap-down, "
                "front headlock, duck under), throws and turns (hip toss, "
                "headlock throw, gut wrench, leg lace, half nelson), "
                "reversals (switch, sit-out), Greco-Roman throws (suplex, "
                "lateral drop), and advanced combinations (fireman carry, "
                "cradle series, ankle lace, Peterson roll, chain wrestling) "
                "- every record a full technique with step-by-step body "
                "mechanics, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the stance, circling and motion footwork, the penetration "
              "step, the level change, the collar tie, the underhook, the "
              "overhook, the two-on-one, the sprawl, the whizzer, the "
              "stand-up escape, referee position and par terre defense) -> "
              "Compounded (the double leg, the high single, the ankle pick, "
              "the low single, the arm drag, the snap-down and go-behind, "
              "the front headlock, the duck under, the hip toss, the "
              "headlock throw, the gut wrench, the leg lace, the half "
              "nelson, the switch reversal) -> Advanced (the sit-out and "
              "turn-in, the suplex, the lateral drop, the fireman carry, "
              "the cradle series, the ankle lace turn, the Peterson roll, "
              "chain wrestling systems).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stance, motion, penetration step, level change, collar tie, underhook, overhook, Russian tie, sprawl, whizzer, stand-up, par terre, double leg, single leg, ankle pick, arm drag, snap down, headlock, duck under, hip toss, gut wrench, leg lace, half nelson, switch, sit-out, suplex, lateral drop, fireman carry, cradle, Peterson roll, chain wrestling...",
        "chat_ph": "Ask about wrestling technique...",
        "archive_blurb": ("Seeded %s wrestling combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled wrestling technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about wrestling technique - from the stance, circling, penetration step, and level change through the collar tie, underhook, overhook, and two-on-one, through the sprawl, whizzer, stand-up, and par terre defense, through the double leg, high single, ankle pick, low single, arm drag, snap-down, front headlock, and duck under, through the hip toss, headlock throw, gut wrench, leg lace, half nelson, and switch, to the sit-out, suplex, lateral drop, fireman carry, cradle series, ankle lace, Peterson roll, and chain wrestling systems." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "wrestling-technique-study", "gen_demo_kind": "wrestling-technique-demo",
        "source": source,
    }

CIT_PUB = ("Wrestling technique (standard references: United World "
           "Wrestling. International Wrestling Rules. Corsier-sur-Vevey: "
           "UWW; 2024 - freestyle and Greco-Roman scoring, par terre, "
           "passivity, falls; National Collegiate Athletic Association. "
           "NCAA Wrestling Rules Book. Indianapolis: NCAA; 2024-25 season; "
           "Gable D. Coaching Wrestling Successfully. Champaign: Human "
           "Kinetics; 1999).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Combat "
                     "Method - the mat the proving ground, stance the oath, "
                     "every technique a Signature discipline of leverage "
                     "and will - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["combat-wrestling"] = _cfg(
    "combat-wrestling", "The Wrestling Combat Database",
    "Freestyle and Greco-Roman wrestling technique, taught step by step: "
    "stance and motion, clinch ties, takedown defense and escapes, shots, "
    "clinch attacks, throws, par terre turns, reversals, and combination "
    "systems - every record a full technique with how-to body mechanics, "
    "ladder-ordered from stance to advanced throws.",
    "combat technique record", "JAH-CBWR-", "JAH Wrestling Combat Archivist",
    "wrestling combat archivist - teaching freestyle and Greco-Roman "
    "wrestling technique from stance and motion through clinch ties, "
    "takedown defense and escapes, shots, clinch attacks, throws, par "
    "terre turns, reversals, and combination systems; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive "
    "data from this system",
    CIT_PUB, "public")
DBCFG["combat-wrestling-signature"] = _cfg(
    "combat-wrestling-signature", "The Wrestling Combat Signature Database",
    "His original Signature Combat Method applied to wrestling: the mat "
    "the proving ground, stance the oath, every technique a Signature "
    "discipline of leverage and will, from stance through ties, takedowns, "
    "throws, turns, and reversals to the grand chain. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "combat technique record", "JAH-CBWRS-", "JAH Wrestling Combat Archivist (Signature)",
    "wrestling combat archivist - Signature editions: his original "
    "Signature Combat Method, the mat the proving ground and stance the "
    "oath, every technique a Signature discipline of leverage and will, "
    "clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
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
    for slug in ("combat-wrestling", "combat-wrestling-signature"):
        cfg = DBCFG[slug]
        sig = slug.endswith("-signature")
        key = "signature" if sig else "public"
        idx = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        frag[key] = {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"], "local_index": idx,
            "record_count": len(built[slug]), "status": "live",
            "full_records": len(built[slug]), "index": idx,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if sig else "public-harvest",
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
    for slug in ("combat-wrestling", "combat-wrestling-signature"):
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
    print("manifest + api.json: NOT touched (merger handles via fragment).")
    print("DONE: 2 databases, %d records. Merger verifies and ships." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
