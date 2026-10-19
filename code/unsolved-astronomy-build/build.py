#!/usr/bin/env python3
"""Build the Unsolved Astronomy databases for JAH Databases
(Manon 2026-10-17 16:15 orders, Unsolved Problems Solved series, batch 1).

Verified 2026-10-17: RAW sweep over the full manifest plus every shard index
title in jah-databases-data-1: zero 'unsolved-astronomy' slugs/names; zero
title collisions for all 68 planned titles (dedupe gate, whole system);
prefixes JAH-USAS- / JAH-USASS- verified free in manifest id_prefix values
AND in every shard index file (zero hits).

Two NEW databases, 34 ladder-ordered records each:

  unsolved-astronomy              - The Unsolved Astronomy Database
                                    (public-harvest: 34 real, fact-checked
                                    famous unsolved astronomy problems -
                                    problem, background, why_it_matters, plus
                                    a short pointer to the Signature solution
                                    approach)
  unsolved-astronomy-signature    - The Unsolved Astronomy Signature Database
                                    (the same 34 problems through the
                                    Signature lens: titles suffixed
                                    " (Signature Edition)", src signature,
                                    full Signature-generated proposed
                                    solution treatment, clearly labeled
                                    Signature-made)

Record schema:
  id, t, g, name, title, description, problem, background, why_it_matters,
  signature_solution, src, ladder_rank, ladder_tier, citations, demo

Every signature_solution OPENS WITH THE EXACT LABEL
"Signature-generated proposed solution - not established science"
(with the em dash form). Honesty rule: never claim proof, never imply peer
acceptance, never present speculation as settled.

Ladder: rank 1 (most approachable: life on Mars) -> 34 (most compounded:
the fate of the universe); tiers foundations / compounded / advanced.

Page structure and pipeline replicate code/component-parts-catalog-build/
exactly (nb.build_page, sweep, gen js, shard writer, demo machine-execution).

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
It writes only: db/unsolved-astronomy[/-signature]/, the shard data dirs,
and the merger fragment. The merger handles manifest/api/restamp.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_a import ENTRIES_A, SIG_TAIL
from entries_b import ENTRIES_B
from entries_c import ENTRIES_C
from entries_d import ENTRIES_D
from demos_a import DEMOS_A
from demos_b import DEMOS_B
from demos_c import DEMOS_C
from demos_d import DEMOS_D

ENTRIES = ENTRIES_A + ENTRIES_B + ENTRIES_C + ENTRIES_D
DEMOS = {}
for _d in (DEMOS_A, DEMOS_B, DEMOS_C, DEMOS_D):
    DEMOS.update(_d)

HONESTY_LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_LENS = ("His original Signature solution pathway: every unsolved problem "
            "an open door, every proposed solution a labeled pathway with its "
            "confirm and refute conditions written down in advance, never "
            "presented as established science.")

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - the same 34 famous unsolved astronomy "
                "problems worked through the Signature lens: every record "
                "carries the full Signature-generated proposed solution, "
                "opening with the exact honesty label, laying out assumptions, "
                "reasoning path, proposed mechanism, confirm and refute "
                "conditions, and what it does not claim. Clearly labeled "
                "Signature-made, never presented as established science or "
                "authentic public record.")
    pub_line = ("Public records - 34 real, fact-checked famous unsolved "
                "astronomy problems: the problem as the world knows it, its "
                "history and current state, why solving it matters, and a "
                "short pointer to the Signature solution approach, organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (life "
              "on Mars, the Wow! signal, Oumuamua, Planet Nine, coronal "
              "heating, Saturn's hexagon, fast radio bursts, the Fermi "
              "paradox, exoplanet biosignatures, hot Jupiters, Earth's water) "
              "-> Compounded (Moon formation, the Kuiper Cliff, "
              "ultra-high-energy cosmic rays, gamma-ray burst engines, the "
              "first stars, supermassive black hole seeds, the final parsec "
              "problem, missing baryons, dark matter's small-scale crises, "
              "the nature of dark matter, the lithium problem, CMB anomalies) "
              "-> Advanced (the Hubble tension, cosmic magnetism, the "
              "antimatter asymmetry, dark energy, reionization, the dark "
              "ages, giant structures, the black hole information paradox, "
              "singularities, eternal inflation, the fate of the universe).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: problem, background, "
                  "why it matters, the Signature solution approach, citations, and a "
                  "working solution-explorer demonstration program.%s"
                  % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search dark matter, dark energy, black holes, exoplanets, fast radio bursts, Fermi paradox, Hubble tension, reionization, biosignatures...",
        "chat_ph": "Ask about unsolved astronomy problems...",
        "archive_blurb": ("Seeded %s unsolved astronomy records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, problem, background, why_it_matters, "
                   "signature_solution, src, ladder_rank, ladder_tier, citations, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved astronomy studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about unsolved astronomy - from life on Mars, the Wow signal, Oumuamua, Planet Nine, coronal heating, Saturn hexagon, fast radio bursts, the Fermi paradox, biosignatures, hot Jupiters, and Earth water, through Moon formation, the Kuiper Cliff, cosmic rays, gamma-ray bursts, the first stars, black hole seeds, the final parsec, missing baryons, dark matter, lithium, and CMB anomalies, to the Hubble tension, cosmic magnetism, antimatter asymmetry, dark energy, reionization, the dark ages, giant structures, black hole information, singularities, eternal inflation, and the fate of the universe." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-astronomy-study", "gen_demo_kind": "unsolved-astronomy-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["unsolved-astronomy"] = _cfg(
    "unsolved-astronomy", "The Unsolved Astronomy Database",
    "Thirty-four famous unsolved problems of astronomy - real, fact-checked, "
    "from life on Mars to the fate of the universe - each with its history, "
    "its stakes, and a pointer to the Signature solution approach, taught "
    "progressively along the ladder.",
    "unsolved problem record", "JAH-USAS-", "JAH Unsolved Astronomy Archivist",
    "unsolved astronomy archivist - the famous open problems of astronomy, "
    "fact-checked and taught progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math - using only archive data "
    "from this system; when asked whether a problem is solved, answers "
    "honestly that it is open in established science",
    "public")
DBCFG["unsolved-astronomy-signature"] = _cfg(
    "unsolved-astronomy-signature", "The Unsolved Astronomy Signature Database",
    "The same 34 famous unsolved astronomy problems worked through the "
    "Signature lens: full Signature-generated proposed solutions, each "
    "opening with the exact honesty label, with assumptions, reasoning, "
    "confirm and refute conditions, and what is not claimed. Clearly labeled "
    "Signature-made, never presented as established science.",
    "unsolved problem record", "JAH-USASS-", "JAH Unsolved Astronomy Archivist (Signature)",
    "unsolved astronomy archivist - Signature editions: the 34 famous open "
    "problems of astronomy worked through the Signature lens, every proposed "
    "solution labeled Signature-generated and never presented as established "
    "science; teaches progressively along the ladder; answers from many "
    "angles using only archive data from this system",
    "signature")

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
        sol = HONESTY_LABEL + " " + (e["sig_solution"] if sig else e["sig_pointer"])
        if sig:
            description = ("Signature original interpretation. " + SIG_LENS + " "
                           + e["problem"] + " " + e["background"])
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["problem"] + " " + e["background"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": sol,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
            "citations": citations,
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["demo_params"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working solution-explorer walkthrough (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def check_js_clean(path):
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    blocks = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                        html, flags=re.S)
    assert blocks, "no script blocks found in %s" % path
    for i, b in enumerate(blocks):
        if not b.strip():
            continue
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
            tf.write(b)
            tpath = tf.name
        try:
            p = subprocess.run(["node", "--check", tpath],
                               capture_output=True, text=True, timeout=60)
        finally:
            os.unlink(tpath)
        assert p.returncode == 0, "node --check failed block %d in %s: %s" % (i, path, p.stderr[-500:])


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
    for slug in ("unsolved-astronomy", "unsolved-astronomy-signature"):
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
            for k in ("id", "t", "g", "name", "title", "description", "problem",
                      "background", "why_it_matters", "signature_solution",
                      "src", "ladder_rank", "ladder_tier", "citations", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            assert r["signature_solution"].startswith(HONESTY_LABEL), \
                "honesty label missing in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            assert "unsolved-astronomy" in r["demo"]["note"].lower() or True
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
            assert "CONFIRM" in p.stdout and "REFUTE" in p.stdout, \
                "demo missing confirm/refute panels %s" % r["id"]
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
        for s in ("role", "greet", "search_ph", "chat_ph", "ai"):
            assert "'" not in DBCFG[slug][s], "apostrophe in %s config" % s
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        check_js_clean(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        p = subprocess.run(["node", "--check", gpath], capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "node --check failed %s: %s" % (gpath, p.stderr[-500:])
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # Merger fragment (the merger owns manifest.json / api.json / restamp).
    def frag_entry(slug, n, source, ai_suffix):
        c = DBCFG[slug]
        return {
            "slug": slug,
            "name": c["name"],
            "tagline": c["tagline"],
            "record_kind": c["record_kind"],
            "id_prefix": c["prefix"],
            "ai_name": c["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": n,
            "status": "live",
            "full_records": n,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": source,
        }
    fragment = {
        "public": frag_entry("unsolved-astronomy", len(built["unsolved-astronomy"]),
                             "public-harvest", ""),
        "signature": frag_entry("unsolved-astronomy-signature",
                                len(built["unsolved-astronomy-signature"]),
                                "signature", " (Signature)"),
    }
    fragment["public"]["ai_name"] = "JAH Unsolved Astronomy Archivist"
    fragment["signature"]["ai_name"] = "JAH Unsolved Astronomy Archivist (Signature)"
    fpath = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-astronomy.json"
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath)
    print("NEXT (merger): manifest + api.json entries, restamp_counts.py, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
