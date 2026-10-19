#!/usr/bin/env python3
"""Build the Unsolved Botany databases for JAH Databases
(Manon 2026-10-17 16:15 orders, Unsolved Problems Solved series).

Verified 2026-10-17: prefixes JAH-USBO- / JAH-USBOS- verified free in manifest
id_prefix values AND in every shard record ID in jah-databases-data-1 (zero
hits); zero title collisions for all 68 planned titles (dedupe gate, whole
system); no unsolved-botany slugs in manifest.

Two NEW databases, 34 ladder-ordered records each:

  unsolved-botany              - The Unsolved Botany Database
                                 (public-harvest: 34 real, fact-checked
                                 famous unsolved plant problems -
                                 problem, background, why_it_matters, plus
                                 a short pointer to the Signature solution
                                 approach)
  unsolved-botany-signature    - The Unsolved Botany Signature Database
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

Ladder: rank 1 (most approachable: autumn leaf color) -> 34 (most compounded:
plant consciousness); tiers foundations / compounded / advanced.

Page structure and pipeline replicate code/unsolved-astronomy-build/
exactly (nb.build_page, sweep, gen js, shard writer, demo machine-execution).

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
It writes only: db/unsolved-botany[/-signature]/, the shard data dirs,
and the merger fragment. The merger handles manifest/api/restamp.

No website references. No Facebook.
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
    sig_line = ("Signature originals - the same 34 famous unsolved botany "
                "problems worked through the Signature lens: every record "
                "carries the full Signature-generated proposed solution, "
                "opening with the exact honesty label, laying out assumptions, "
                "reasoning path, proposed mechanism, confirm and refute "
                "conditions, and what it does not claim. Clearly labeled "
                "Signature-made, never presented as established science or "
                "authentic public record.")
    pub_line = ("Public records - 34 real, fact-checked famous unsolved "
                "botany problems: the problem as the world knows it, its "
                "history and current state, why solving it matters, and a "
                "short pointer to the Signature solution approach, organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (autumn "
              "leaf color, the Venus flytrap count, phototropism, seed dormancy, "
              "florigen, carnivorous plants, plant warning signals, vernalization, "
              "bristlecone longevity, the wood wide web debate, plant cognition) "
              "-> Compounded (the ascent of sap, hormone crosstalk, plant immunity, "
              "the root microbiome, mycorrhizal functions, drought genetics, C4 "
              "convergence, photorespiration, nitrogen fixation for cereals, "
              "photoprotection, epigenetic memory, plant electrical signaling) "
              "-> Advanced (the field efficiency gap, Rubisco engineering, crop "
              "yield ceilings, C4 rice, the longevity genome, the origin of land "
              "plants, endosymbiosis mechanics, synthetic chloroplasts, the "
              "complete mechanics of photosynthesis optimization, the de novo "
              "photosynthetic organism, plant consciousness).")
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
        "search_ph": "Search photosynthesis, Rubisco, mycorrhizae, C4, photorespiration, florigen, vernalization, carnivory, yield ceilings...",
        "chat_ph": "Ask about unsolved botany problems...",
        "archive_blurb": ("Seeded %s unsolved botany records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, problem, background, why_it_matters, "
                   "signature_solution, src, ladder_rank, ladder_tier, citations, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved botany studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about unsolved botany - from autumn leaf color, the Venus flytrap count, phototropism, seed dormancy, florigen, carnivorous plants, plant warning signals, vernalization, bristlecone longevity, the wood wide web debate, and plant cognition, through the ascent of sap, hormone crosstalk, plant immunity, the root microbiome, mycorrhizal functions, drought genetics, C4 convergence, photorespiration, nitrogen fixation for cereals, photoprotection, epigenetic memory, and plant electrical signaling, to the field efficiency gap, Rubisco engineering, crop yield ceilings, C4 rice, the longevity genome, the origin of land plants, endosymbiosis mechanics, synthetic chloroplasts, the complete mechanics of photosynthesis optimization, the de novo photosynthetic organism, and plant consciousness." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-botany-study", "gen_demo_kind": "unsolved-botany-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["unsolved-botany"] = _cfg(
    "unsolved-botany", "The Unsolved Botany Database",
    "Thirty-four famous unsolved problems of botany - real, fact-checked, "
    "from autumn leaf color to plant consciousness - each with its history, "
    "its stakes, and a pointer to the Signature solution approach, taught "
    "progressively along the ladder.",
    "unsolved problem record", "JAH-USBO-", "JAH Unsolved Botany Archivist",
    "unsolved botany archivist - the famous open problems of plant science, "
    "fact-checked and taught progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math - using only archive data "
    "from this system; when asked whether a problem is solved, answers "
    "honestly that it is open in established science",
    "public")
DBCFG["unsolved-botany-signature"] = _cfg(
    "unsolved-botany-signature", "The Unsolved Botany Signature Database",
    "The same 34 famous unsolved botany problems worked through the "
    "Signature lens: full Signature-generated proposed solutions, each "
    "opening with the exact honesty label, with assumptions, reasoning, "
    "confirm and refute conditions, and what is not claimed. Clearly labeled "
    "Signature-made, never presented as established science.",
    "unsolved problem record", "JAH-USBOS-", "JAH Unsolved Botany Archivist (Signature)",
    "unsolved botany archivist - Signature editions: the 34 famous open "
    "problems of plant science worked through the Signature lens, every proposed "
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
    for slug in ("unsolved-botany", "unsolved-botany-signature"):
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
        assert "facebook" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        p = subprocess.run(["node", "--check", gpath], capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "node --check failed %s: %s" % (gpath, p.stderr[-500:])
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # Merger fragment (the merger owns manifest.json / api.json / restamp).
    def frag_entry(slug, n, source):
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
        "public": frag_entry("unsolved-botany", len(built["unsolved-botany"]),
                             "public-harvest"),
        "signature": frag_entry("unsolved-botany-signature",
                                len(built["unsolved-botany-signature"]),
                                "signature"),
    }
    fpath = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-botany.json"
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath)
    print("NEXT (merger): manifest + api.json entries, restamp_counts.py, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
