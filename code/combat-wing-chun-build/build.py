#!/usr/bin/env python3
"""Build the Wing Chun Combat databases for JAH Databases (combat batch 3).

Pre-authoring whole-system dedupe: code/combat-wing-chun-build/dedupe_sweep.py
ran the 68 titles against the DedupeGate exact store plus a RAW sweep of
every shard index title in jah-databases-data-1 plus the main-repo data dir:
zero collisions (see build log).

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-wing-chun              - Wing Chun Combat Database (public-harvest:
                                  real, fact-checked Wing Chun martial-arts
                                  knowledge - centerline theory, stances,
                                  hand techniques, footwork, the three
                                  empty-hand forms, chi sao, the wooden
                                  dummy, the traditional weapons - every
                                  record a technique with step-by-step body
                                  mechanics; standard references Chu,
                                  Ritchie and Wu, Complete Wing Chun
                                  (Tuttle, 1998); Belonoha, The Wing Chun
                                  Compendium vols 1-2 (2009, 2013); Yip
                                  Chun, 116 Wing Tsun Dummy Techniques
                                  (1981); Leung Ting, Wing Tsun Kuen (1981);
                                  Yimm Lee, Wing Chun Kung Fu (1972))
  combat-wing-chun-signature    - Wing Chun Combat Signature Database
                                  (his original Signature Combat Method: the
                                  centerline as the Signature line, every
                                  technique a covenant of structure, the
                                  dummy the iron training partner, chi sao
                                  the listening bridge; src signature,
                                  titles suffixed " (Signature Edition)",
                                  never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBWC- (public) and JAH-CBWCS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_wing_chun.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. A merger handles registration. It ONLY writes db/combat-wing-chun*/
pages, the shard data dirs, and the missing-builds fragment.

Civilian traditional-art scope only. Nothing on neutralizing military or
defense-grade systems. No website references. No Facebook.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-wing-chun.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_wing_chun import ENTRIES, SIG_TAIL
from demos_combat_wing_chun import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat "
                "Method applied to Wing Chun: the centerline as the "
                "Signature line every technique is measured from, each "
                "technique a covenant of structure, the wooden dummy the "
                "iron training partner, chi sao the listening bridge, and "
                "forward pressure the oath. Clearly labeled "
                "Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked Wing Chun martial-arts "
                "knowledge: centerline theory, stances, hand techniques, "
                "footwork, the three empty-hand forms, chi sao sticking "
                "hands, the wooden dummy form, and the traditional weapons "
                "- every record a technique with step-by-step body "
                "mechanics for how to do it, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(centerline theory, the basic stance, the guard, the "
              "vertical punch, chain punching, Tan Sau, Bong Sau, Fook Sau, "
              "Pak Sau, advancing and retreating, turning the stance, the "
              "first form Siu Nim Tau) -> Compounded (Lap Sau, Jut Sau, "
              "Kwan Sau, Gaun Sau, Huen Sau, Gan Sau, Biu Sau, the second "
              "form Chum Kiu, kicks, single-hand sticking, double-hand "
              "rolling, the Lop Sao attack-defense cycle) -> Advanced (the "
              "wooden dummy form, dummy footwork and angles, the third "
              "form Biu Jee, sticky legs, the eight-cut knives, the "
              "six-and-a-half-point pole, simultaneous attack and defense, "
              "free sparring, free sticking hands, the self-defense "
              "application framework).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search centerline, Tan Sau, Bong Sau, Fook Sau, Pak Sau, chain punching, chi sao, wooden dummy, Biu Jee, footwork, forms, knives, pole...",
        "chat_ph": "Ask about Wing Chun techniques...",
        "archive_blurb": ("Seeded %s Wing Chun technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Wing Chun technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Wing Chun - from centerline theory, the stance, the guard, the vertical punch, chain punching, Tan Sau, Bong Sau, Fook Sau, and Pak Sau, through footwork, the three forms, Lap Sau, Jut Sau, Kwan Sau, Gaun Sau, Huen Sau, Gan Sau, Biu Sau, kicks, and the chi sao drills, to the wooden dummy, Biu Jee, sticky legs, the knives, the pole, simultaneous attack and defense, sparring, and the self-defense framework." % ai,
        "gen_fields": ["Foundations", "Hand Techniques", "Footwork", "Forms", "Chi Sao", "Wooden Dummy", "Weapons"],
        "gen_kind": "wing-chun-study", "gen_demo_kind": "wing-chun-demo",
        "source": source,
    }

CIT_PUB = ("Wing Chun martial-arts knowledge (standard references: Chu R, "
           "Ritchie R, Wu Y. Complete Wing Chun: The Definitive Guide to "
           "Wing Chun's History and Traditions. Tuttle Publishing; 1998; "
           "Belonoha W. The Wing Chun Compendium, Volumes 1 and 2. Blue "
           "Snake Books; 2009, 2013; Yip Chun. 116 Wing Tsun Dummy "
           "Techniques. Hong Kong; 1981; Leung Ting. Wing Tsun Kuen. Hong "
           "Kong; 1981; Yimm Lee J. Wing Chun Kung Fu. Ohara Publications; "
           "1972).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Combat "
                     "Method - the centerline as the Signature line, every "
                     "technique a covenant of structure - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["combat-wing-chun"] = _cfg(
    "combat-wing-chun", "Wing Chun Combat Database",
    "Wing Chun from the ground up: centerline theory, stances, hand "
    "techniques, footwork, the three empty-hand forms, chi sao sticking "
    "hands, the wooden dummy form, and the traditional weapons - every "
    "technique taught step by step with real body mechanics, ladder-ordered "
    "from foundations to advanced.",
    "combat technique record", "JAH-CBWC-", "JAH Wing Chun Combat Archivist",
    "Wing Chun combat archivist - centerline theory, stances, hand "
    "techniques, footwork, the three forms, chi sao, the wooden dummy, and "
    "the traditional weapons; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-wing-chun-signature"] = _cfg(
    "combat-wing-chun-signature", "Wing Chun Combat Signature Database",
    "His original Signature Combat Method applied to Wing Chun: the "
    "centerline as the Signature line, every technique a covenant of "
    "structure, the wooden dummy the iron training partner, chi sao the "
    "listening bridge. The full ladder from centerline theory through "
    "stances, hand techniques, footwork, forms, and chi sao, to the dummy, "
    "the weapons, and free practice, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public "
    "record.",
    "combat technique record", "JAH-CBWCS-", "JAH Wing Chun Combat Archivist (Signature)",
    "Wing Chun combat archivist - Signature editions: his original "
    "Signature Combat Method, the centerline as the Signature line and "
    "every technique a covenant of structure, clearly labeled "
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


def write_fragment(built):
    frag = {}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        is_sig = slug.endswith("-signature")
        frag["signature" if is_sig else "public"] = {
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
            "source": "signature" if is_sig else "public-harvest",
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
    for slug in ("combat-wing-chun", "combat-wing-chun-signature"):
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
            assert "'" not in cfg["ai"] and "'" not in cfg["role"] \
                and "'" not in cfg["greet"] and "'" not in cfg["search_ph"], \
                "apostrophe in JS-embedded string for %s" % slug
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
        assert "public-synthetic-intelligence" not in page, "slug leftover in %s" % slug
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

    write_fragment(built)
    print("manifest/api.json: NOT touched (merger registers these databases).")
    print("BUILD COMPLETE: 2 databases, %d records. No commit, no push (merger handles)." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
