#!/usr/bin/env python3
"""Build the Muay Thai Combat databases for JAH Databases
(combat batch 1, 2026-10-17).

Scope verified 2026-10-17 before authoring: RAW check over the full manifest
plus every shard index title in jah-databases-data-1: zero 'combat-muay*'
slugs/names; zero Muay Thai combat technique catalog databases of this kind.
Dedupe gate check of all 68 planned titles (34 public + 34 Signature) vs the
whole exact index: zero collisions, zero refusals. ID prefixes JAH-CBMT- and
JAH-CBMTS- verified free in the manifest id_prefix values and every shard
index file (zero hits).

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-muay-thai              - The Muay Thai Combat Database
                                  (public-harvest: real, fact-checked Muay
                                  Thai technique knowledge - the art of eight
                                  limbs: punches (mat), elbows (sok), knees
                                  (khao), kicks (tae, thip), clinch work
                                  (chap kho), sweeps and dumps (tad kha,
                                  thum), and conditioning methods - every
                                  record carrying the Thai name with
                                  translation, step-by-step body mechanics,
                                  key points, requirements, standards, and
                                  citations; standard references Delp C.
                                  Muay Thai Basics 2004; Delp C. Muay Thai:
                                  Advanced Thai Kickboxing Techniques 2006;
                                  Kraitus P, Kraitus P. Muay Thai: The Most
                                  Distinguished Art of Fighting 1988; IFMA
                                  rules; WMC rules)
  combat-muay-thai-signature    - The Muay Thai Combat Signature Database
                                  (his original Signature Eight-Limb Method:
                                  every limb a covenant of mechanics, the
                                  stance the oath of the feet, the guard
                                  the walls of the temple, the clinch the
                                  handshake of warriors; src signature,
                                  titles suffixed " (Signature Edition)",
                                  never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBMT- (public) and JAH-CBMTS- (signature), verified free
in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_muay_thai.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before commit.

Civilian martial-arts sport instruction only. Nothing on neutralizing or
defeating military or defense-grade systems. Never the words "bat belt"
anywhere. No website references. No Facebook.

CONCURRENCY: this script never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles manifest/api/pages wiring.
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
from entries_combat_muay_thai import ENTRIES, SIG_TAIL
from demos_combat_muay_thai import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Eight-Limb "
                "Method: every limb a covenant of mechanics, the stance the "
                "oath of the feet, the guard the walls of the temple, the "
                "clinch the handshake of warriors. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Muay Thai technique "
                "knowledge: the art of eight limbs - punches (mat), elbows "
                "(sok), knees (khao), kicks (tae, thip), clinch work (chap "
                "kho), sweeps and dumps (tad kha, thum), and conditioning "
                "methods - every record carrying the Thai name with "
                "translation, step-by-step body mechanics, key points, "
                "requirements, standards, and citations, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(fighting stance, footwork, high guard, jab, parry and slip, "
              "shadowboxing, cross, roundhouse kick, teep, checking kicks, "
              "heavy bag training, shin and core conditioning) -> Compounded "
              "(hook, uppercut, horizontal elbow, straight knee, upward and "
              "diagonal elbows, curved knee, clinch entry and inside "
              "position, low cut kick, switch kick, clinch control and "
              "pummeling, catching kicks and dumps, defensive shell and "
              "counters) -> Advanced (spinning elbow, flying knee, spinning "
              "heel kick, elbow-range pocket fighting, clinch throws, "
              "sweeps, counter-fighting timing, combination systems, "
              "ringcraft, full fight camp conditioning).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stance, footwork, guard, jab, cross, hook, uppercut, elbow, knee, roundhouse, teep, low kick, switch kick, clinch, sweeps, throws, ringcraft, fight camp...",
        "chat_ph": "Ask about Muay Thai technique...",
        "archive_blurb": ("Seeded %s Muay Thai combat technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Muay Thai technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Muay Thai - from stance, footwork, guard, jab, parry, shadowboxing, cross, roundhouse, teep, checking, bag work, and conditioning, through hooks, uppercuts, elbows, knees, clinch entry and control, low and switch kicks, catches, dumps, and counters, to spinning techniques, flying knee, throws, sweeps, counter-timing, combinations, ringcraft, and the full fight camp." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "muay-thai-study", "gen_demo_kind": "muay-thai-demo",
        "source": source,
    }

CIT_PUB = ("Muay Thai technique (standard references: Delp C. Muay Thai "
           "Basics: Introductory Thai Boxing Techniques. North Atlantic "
           "Books; 2004; Delp C. Muay Thai: Advanced Thai Kickboxing "
           "Techniques. Blue Snake Books; 2006; Kraitus P, Kraitus P. Muay "
           "Thai: The Most Distinguished Art of Fighting. Soma Publishing; "
           "1988; International Federation of Muaythai Associations (IFMA) "
           "Rules of Muaythai Competition; World Muaythai Council (WMC) "
           "Muaythai Rules and Regulations).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Eight-Limb Method - every limb a covenant of "
                     "mechanics, the stance the oath of the feet - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["combat-muay-thai"] = _cfg(
    "combat-muay-thai", "The Muay Thai Combat Database",
    "The art of eight limbs, taught step by step: real, fact-checked Muay "
    "Thai technique knowledge - punches, elbows, knees, kicks, clinch work, "
    "sweeps and dumps, and conditioning methods - every record carrying the "
    "Thai name with translation and full body mechanics, taught "
    "progressively along the ladder.",
    "combat technique record", "JAH-CBMT-", "JAH Muay Thai Combat Archivist",
    "muay thai combat archivist - teaching the art of eight limbs: punches, "
    "elbows, knees, kicks, clinch work, sweeps and dumps, and conditioning "
    "methods, with Thai names, translations, and step-by-step body "
    "mechanics; teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-muay-thai-signature"] = _cfg(
    "combat-muay-thai-signature", "The Muay Thai Combat Signature Database",
    "His original Signature Eight-Limb Method: every limb a covenant of "
    "mechanics, the stance the oath of the feet, the guard the walls of the "
    "temple, the clinch the handshake of warriors. The full ladder from "
    "stance and footwork through punches, elbows, knees, kicks, and clinch, "
    "to spinning techniques, throws, sweeps, ringcraft, and the fight camp, "
    "reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "combat technique record", "JAH-CBMTS-", "JAH Muay Thai Combat Archivist (Signature)",
    "muay thai combat archivist - Signature editions: his original Signature "
    "Eight-Limb Method, every limb a covenant of mechanics and the clinch "
    "the handshake of warriors, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, math, "
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
    for slug in ("combat-muay-thai", "combat-muay-thai-signature"):
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
        assert "muay thai" in page.lower(), "field content missing in %s" % slug
        assert "public-synthetic-intelligence" not in page, "template leftover in %s" % slug
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
        assert "universal-build" not in page, "slug leftover in %s" % slug
        assert "facebook" not in page.lower()
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
        assert "synthetic intelligence" not in gen_js.lower(), "template leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # NOTE: manifest.json / api.json are owned by the merger - never touched here.
    print("built %d databases, %d records; manifest/api left for the merger" % (len(built), total))
    print("NEXT (merger): run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
