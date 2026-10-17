#!/usr/bin/env python3
"""Build the Kickboxing Combat databases for JAH Databases (combat orders
2026-10-17, combat batch 1).

Dedupe verified 2026-10-17: raw sweep over the full manifest (2,094 id
prefixes) plus every shard index in jah-databases-data-1: zero
'combat-kickboxing' slugs, zero kickboxing databases of any kind, zero
title collisions on all 68 titles (34 public + 34 ' (Signature Edition)'
variants) through code/dedupe_gate.py against the whole exact-title
index - zero refusals. ID prefixes JAH-CBKBX- (public) and JAH-CBKBXS-
(signature) verified zero hits in manifest id_prefix values and in every
shard index file.

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-kickboxing            - The Kickboxing Combat Database
                                 (public-harvest: real, fact-checked
                                 kickboxing across the American, K-1, and
                                 Dutch rule sets - punches, kicks, knee
                                 strikes, combinations, and defense - each
                                 record a technique with how to do it
                                 taught step by step, ordered along the
                                 teaching ladder from stance to advanced
                                 combinations)
  combat-kickboxing-signature  - The Kickboxing Combat Signature Database
                                 (his original Signature Combat Method:
                                 every technique an oath of body
                                 mechanics, the stance the covenant
                                 ground, each strike the signature stroke
                                 written by the body, defense the honor
                                 guard, conditioning the sworn
                                 preparation; src signature, titles
                                 suffixed " (Signature Edition)", clearly
                                 labeled Signature-made, never presented
                                 as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_kickboxing.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Screening: civilian martial-arts instruction only - nothing
hate-adjacent, profane, or inappropriate; no religious talk; nothing on
neutralizing or defeating military or defense-grade systems.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never runs git commit
or git push - a merger handles those. It writes only db/combat-kickboxing*/
pages, code/combat-kickboxing-build/*, the data-1 shard dirs, and the
missing-builds fragment.

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
FRAGMENTS = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_kickboxing import ENTRIES, SIG_TAIL
from demos_combat_kickboxing import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat "
                "Method: every technique an oath of body mechanics, the "
                "stance the covenant ground, each strike the signature "
                "stroke written by the body, defense the honor guard, and "
                "conditioning the sworn preparation. Clearly labeled "
                "Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked kickboxing across the "
                "American, K-1, and Dutch rule sets: punches, kicks, knee "
                "strikes, combinations, and defense - each record a "
                "technique with how to do it taught step by step in plain "
                "sentences, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the stance, the guard, footwork, the jab, the cross, hooks, "
              "the uppercut, the low kick, the roundhouse kick to the body) "
              "-> Compounded (the teep, the front snap kick, the knee "
              "strike, the one-two, the jab-cross-hook, blocking and "
              "parrying, slip weave and roll, checking kicks, catching "
              "kicks and sweeps, inside and outside leg kicks, clinch "
              "entry and pummeling, counter-punching) -> Advanced "
              "(Dutch-style combinations, the switch kick, the spinning "
              "back kick, the flying knee, shin and body conditioning, "
              "feints and setups, ring cutting and angles, advanced "
              "defense, sparring strategy and round management, southpaw "
              "versus orthodox planning, ruleset mastery, fight camp "
              "design).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stance, guard, footwork, jab, cross, hook, uppercut, low kick, roundhouse, teep, knee, combinations, checks, clinch, counters, Dutch style, feints, rulesets, fight camp...",
        "chat_ph": "Ask about kickboxing technique...",
        "archive_blurb": ("Seeded %s kickboxing combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled kickboxing combat studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about kickboxing - from stance, guard, and footwork through every punch, kick, and knee, through combinations, defense, and the clinch, to Dutch-style striking, feints, ring craft, rulesets, and fight camp design." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "kickboxing-combat-study", "gen_demo_kind": "kickboxing-combat-demo",
        "source": source,
    }

CIT_PUB = ("Kickboxing technique and rules (standard references: Dempsey J. "
           "Championship Fighting: Explosive Punching and Aggressive "
           "Defense. 1950; Hatmaker M. Boxing Mastery. Tracks Publishing; "
           "2004; Rooney M. Training for Warriors. HarperCollins; 2008; "
           "Bompa T, Haff GG. Periodization: Theory and Methodology of "
           "Training. 5th ed. Human Kinetics; 2009; World Association of "
           "Kickboxing Organizations (WAKO) official rules; International "
           "Sport Karate Association (ISKA) official rules; K-1 World "
           "Grand Prix official rules).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Combat "
                     "Method - every technique an oath of body mechanics, "
                     "the stance the covenant ground, each strike the "
                     "signature stroke written by the body - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["combat-kickboxing"] = _cfg(
    "combat-kickboxing", "The Kickboxing Combat Database",
    "Kickboxing across the American, K-1, and Dutch rule sets: punches, "
    "kicks, knee strikes, combinations, and defense - each record a "
    "technique with how to do it taught step by step in plain sentences, "
    "ladder-ordered from stance to advanced combinations.",
    "combat technique record", "JAH-CBKBX-", "JAH Kickboxing Combat Archivist",
    "kickboxing combat archivist - punches, kicks, knee strikes, "
    "combinations, and defense across the American, K-1, and Dutch rule "
    "sets; teaching progressively along the ladder from stance through "
    "compounded technique to advanced combinations; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-kickboxing-signature"] = _cfg(
    "combat-kickboxing-signature", "The Kickboxing Combat Signature Database",
    "His original Signature Combat Method: every technique an oath of body "
    "mechanics, the stance the covenant ground, each strike the signature "
    "stroke written by the body, defense the honor guard, conditioning the "
    "sworn preparation. The full ladder from stance through punches, kicks, "
    "knees, combinations, and defense to Dutch-style striking, feints, ring "
    "craft, rulesets, and fight camp design, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public "
    "record.",
    "combat technique record", "JAH-CBKBXS-", "JAH Kickboxing Combat Archivist (Signature)",
    "kickboxing combat archivist - Signature editions: his original "
    "Signature Combat Method, every technique an oath of body mechanics "
    "and the stance the covenant ground, clearly labeled Signature-made "
    "and never presented as authentic public record; teaches progressively "
    "along the ladder from stance through compounded technique to advanced "
    "combinations; answers from many angles - definition, example, analogy, "
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


def write_fragment(built):
    os.makedirs(FRAGMENTS, exist_ok=True)
    frag = {}
    for slug, recs in built.items():
        sig = slug.endswith("-signature")
        cfg = DBCFG[slug]
        key = "signature" if sig else "public"
        frag[key] = {
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
            "source": "signature" if sig else "public-harvest",
        }
    path = os.path.join(FRAGMENTS, "combat-kickboxing.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % path, flush=True)
    return path


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
    for slug in ("combat-kickboxing", "combat-kickboxing-signature"):
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
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)
    # NOTE: manifest.json / api.json / index.html / README / docs/AI_ACCESS
    # are owned by the merger - this builder never touches them, and never
    # runs git commit or git push.
    print("built %d databases, %d records total - ready for merger" % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
