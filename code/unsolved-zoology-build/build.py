#!/usr/bin/env python3
"""Build the Unsolved Zoology databases for JAH Databases
(Manon's 16:15 orders, Unsolved Problems Solved series).

Verified 2026-10-17: zero 'unsolved-zoology' slugs in the manifest;
zero JAH-USZO- hits in the manifest id_prefix values AND across all
shard index files in jah-databases-data-1. DedupeGate check over all 68
titles vs the whole system: zero collisions (pre-authoring check).

So this build creates two NEW databases, 34 ladder-ordered records each:

  unsolved-zoology              - The Unsolved Zoology Database
                                  (public-harvest: 34 famous unsolved
                                  zoology problems, real and
                                  fact-checked - giraffe necks, zebra
                                  stripes, animal sleep, pigeon homing,
                                  monarch migration, salmon homing, whale
                                  strandings, lemming cycles, desert ant
                                  navigation, electroreception, no wheels
                                  in nature, cephalopod camouflage,
                                  consciousness markers, animal language,
                                  eusociality, maintenance of sex, insect
                                  flight, bat echolocation, regeneration,
                                  vertebrate jaw, aging, parasite
                                  manipulation, tool use, migration
                                  clocks, Cambrian explosion,
                                  multicellular origin, bilateral
                                  symmetry, animal root, extinction
                                  selectivity, bird flight, negligible
                                  senescence, predictable evolution,
                                  consciousness evolution, last common
                                  ancestor - each with problem,
                                  background, why-it-matters, and a short
                                  pointer to the Signature approach)
  unsolved-zoology-signature    - The Unsolved Zoology Signature Database
                                  (his original Signature solution method:
                                  the same 34 problems through the
                                  Signature lens, each carrying the full
                                  Signature-generated proposed solution -
                                  always labeled, never presented as
                                  established science; src signature,
                                  titles suffixed " (Signature Edition)")

34 records each, ladder-ordered by problem accessibility (ladder_rank 1-34,
tiers foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-USZO- (public) and JAH-USZOS- (signature), verified free
in the manifest and in every shard index.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_zoology.py). Every demo is a
solution-explorer walkthrough: it prints its real computed values,
asserts tight bounds (never float exact-equality), prints CONFIRM/REFUTE
panels, and ends with the OK marker; the build machine-executes all 68
demos.

Honesty rule: signature solutions open with the exact label
"Signature-generated proposed solution — not established science" and never
claim proof, peer acceptance, or settled status.

Never the words "bat belt" anywhere. No website references. No Facebook.

This build does NOT touch data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md, and does NOT git commit or push - a
merger handles registration. It writes the fragment file for the merger.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-zoology.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_zoology import ENTRIES, SIG_TAIL, LABEL
from demos_unsolved_zoology import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature solution method: the same 34 famous "
                "unsolved zoology problems approached as a covenant between the known and the "
                "unknown, each carrying the full Signature-generated proposed solution with its "
                "assumptions declared, its confirm and refute conditions stated, and its limits honestly "
                "marked. Clearly labeled Signature-made, never presented as established science or "
                "authentic public record.")
    pub_line = ("Public records - 34 famous unsolved zoology problems, real and fact-checked: giraffe "
                "necks, zebra stripes, why animals sleep, pigeon homing, monarch migration, salmon "
                "homing, whale strandings, lemming cycles, desert ant navigation, electroreception, "
                "why there are no wheels in nature, cephalopod camouflage, consciousness markers, "
                "animal language, eusociality, the maintenance of sex, insect flight, bat echolocation, "
                "regeneration, the vertebrate jaw, aging, parasite manipulation, tool use, migration "
                "clocks, the Cambrian explosion, the multicellular origin, bilateral symmetry, the "
                "animal root, extinction selectivity, bird flight, negligible senescence, predictable "
                "evolution, the evolution of consciousness, and the last common ancestor of animals - "
                "every record carrying the problem statement, background, why it matters, key points, "
                "requirements, standards, citations, and a working solution-explorer demonstration, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(giraffe necks, zebra stripes, animal sleep, pigeon homing, monarch migration, salmon "
              "homing, whale strandings, lemming cycles, desert ant navigation, electroreception, "
              "no wheels in nature, cephalopod camouflage) -> "
              "Compounded (consciousness markers, animal language, eusociality, maintenance of sex, "
              "insect flight, bat echolocation, regeneration, vertebrate jaw, aging, parasite "
              "manipulation, tool use, migration clocks) -> "
              "Advanced (Cambrian explosion, multicellular origin, bilateral symmetry, animal root, "
              "extinction selectivity, bird flight, negligible senescence, predictable evolution, "
              "consciousness evolution, last common ancestor).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: problem, background, why it matters, "
                  "key points, requirements, standards, citations, and a working solution-explorer "
                  "demonstration program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search giraffe necks, zebra stripes, eusociality, maintenance of sex, consciousness, migration, Cambrian explosion, animal navigation...",
        "chat_ph": "Ask about unsolved problems in zoology...",
        "archive_blurb": ("Seeded %s unsolved zoology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved zoology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the great unsolved problems of zoology - from giraffe necks, zebra stripes, and animal sleep through migration navigation, eusociality, and the maintenance of sex, to the Cambrian explosion, the animal root, and the evolution of consciousness." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-zoology-study", "gen_demo_kind": "unsolved-zoology-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["unsolved-zoology"] = _cfg(
    "unsolved-zoology", "The Unsolved Zoology Database",
    "Thirty-four famous unsolved zoology problems, from giraffe necks to the last common ancestor "
    "of animals: real, fact-checked, each with its full story and a clearly labeled Signature "
    "proposed solution.",
    "unsolved problem record", "JAH-USZO-", "JAH Unsolved Zoology Archivist",
    "unsolved zoology archivist - the great open problems of zoology, from giraffe necks, zebra "
    "stripes, and animal sleep through pigeon homing, monarch migration, salmon homing, whale "
    "strandings, desert ant navigation, and cephalopod camouflage, to consciousness markers, "
    "animal language, eusociality, the maintenance of sex, insect and bird flight, regeneration, "
    "aging, the Cambrian explosion, the animal root, and the evolution of consciousness; teaching "
    "progressively along the ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, math - using only archive "
    "data from this system",
    "public")
DBCFG["unsolved-zoology-signature"] = _cfg(
    "unsolved-zoology-signature", "The Unsolved Zoology Signature Database",
    "His original Signature solution method applied to all 34 famous unsolved zoology problems: "
    "Signature-generated proposed solutions with assumptions declared, confirm and refute conditions "
    "stated, and limits honestly marked. Clearly labeled Signature-made, never established science.",
    "unsolved problem record", "JAH-USZOS-", "JAH Unsolved Zoology Archivist (Signature)",
    "unsolved zoology archivist - Signature editions: his original Signature solution method applied "
    "to the 34 famous unsolved zoology problems, each carrying the full Signature-generated proposed "
    "solution, clearly labeled Signature-made and never presented as established science; teaches "
    "progressively along the ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math - using only archive data from "
    "this system",
    "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"
assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)


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
        problem = e["problem"]
        background = e["background"]
        why = e["why_it_matters"]
        if sig:
            assert e["sig_solution"].startswith(LABEL), "sig solution must open with exact label: %s" % name
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + problem + " " + background)
            sol_body = e["sig_solution"][len(LABEL):].lstrip()
            how = (LABEL + " " + e["sig_lens"] + " " + why + " " + sol_body)
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = problem + " " + background
            how = LABEL + " " + why + " " + e["pointer"]
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
                       "note": "Solution-explorer walkthrough (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def node_check(path):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True, timeout=60)
    assert p.returncode == 0, "node --check failed for %s: %s" % (path, p.stderr[-500:])
    return True


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
    for slug in ("unsolved-zoology", "unsolved-zoology-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        assert [r["ladder_rank"] for r in recs] == list(range(1, 35)), "ladder ranks must be 1-34 in %s" % slug
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
                assert r["how_it_works"].startswith(LABEL), "honesty label not at record open in %s" % r["id"]
            else:
                assert r["src"] == "public-harvest"
                assert r["how_it_works"].startswith(LABEL), "honesty label not at record open in %s" % r["id"]
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=300)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            assert "CONFIRM IF:" in p.stdout and "REFUTE IF:" in p.stdout, \
                "demo missing confirm/refute panel %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    gen_paths = []
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
        # node --check on extracted page scripts (exclude ld+json blocks: JSON, not JS)
        scripts = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                             page, flags=re.S)
        for i, body in enumerate(scripts):
            if body.strip():
                tmp = "/tmp/uszl_pagescript_%s_%d.js" % (slug.replace("-", "_"), i)
                with open(tmp, "w", encoding="utf-8") as f:
                    f.write(body)
                node_check(tmp)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        node_check(gpath)
        gen_paths.append(gpath)
        # apostrophe hygiene on role/ai_name/greet/search strings (JS uses
        # single-quoted literals, so embedded values must be apostrophe-free)
        for k in ("role", "ai", "greet", "search_ph", "chat_ph", "gen_desc"):
            assert "'" not in DBCFG[slug][k], "apostrophe in cfg %s for %s" % (k, slug)
        for r in recs:
            assert "'" not in r["t"], "apostrophe in title %s" % r["id"]
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # fragment for the merger (manifest/api/hub/README/docs handled by merger)
    def frag_entry(slug):
        c = DBCFG[slug]
        idx = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        return {
            "slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": idx, "record_count": 34,
            "status": "live", "full_records": 34, "index": idx,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest" if not slug.endswith("-signature") else "signature",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump({"public": frag_entry("unsolved-zoology"),
                   "signature": frag_entry("unsolved-zoology-signature")},
                  f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT)
    print("NOTE: manifest/api/hub/README/docs NOT touched - merger handles registration. No commit/push done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
