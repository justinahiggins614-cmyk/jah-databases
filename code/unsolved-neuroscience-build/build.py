#!/usr/bin/env python3
"""Build the Unsolved Neuroscience databases for JAH Databases
(Manon 2026-10-17 16:15 orders, Unsolved Problems Solved series batch 1).

Creates two NEW databases, 34 ladder-ordered records each:

  unsolved-neuroscience            - The Unsolved Neuroscience Database
                                     (public-harvest: 34 real, famous
                                     unsolved neuroscience problems,
                                     fact-checked - dreaming, attention,
                                     forgetting, consolidation, deja vu,
                                     prediction-error learning, pain, body
                                     ownership, few-shot learning, spatial
                                     representation, working memory, sensory
                                     cancellation, sleep, the neural code,
                                     binding, the engram, plasticity rules,
                                     decision, emotion, language,
                                     creativity, lifelong learning,
                                     anesthesia, volition, NCC, brain
                                     aging, BCI limits, self-repair,
                                     receptor-to-experience, psychosis
                                     circuits, whole-brain mapping, the
                                     self, the hard problem, a complete
                                     theory - every record carrying
                                     problem, background, why-it-matters,
                                     and a short pointer to the Signature
                                     proposed solution)
  unsolved-neuroscience-signature  - The Unsolved Neuroscience Signature
                                     Database
                                     (his original Signature Neuroscience
                                     Method: the same 34 problems through
                                     the Signature lens of prediction,
                                     precision, and generative modeling,
                                     each carrying the full proposed
                                     solution treatment, always opening
                                     with the exact honesty label and
                                     never presented as established
                                     science; src signature, titles
                                     suffixed " (Signature Edition)")

ID prefixes: JAH-USNS- (public) and JAH-USNSS- (signature), verified free
in the manifest id_prefix values (2442 databases, zero hits) and in all
871 shard index files in jah-databases-data-1 (zero hits).

Honesty rule: every signature_solution opens with the exact label
"Signature-generated proposed solution - not established science";
never claims proof, never implies peer acceptance, never presents
speculation as settled. Descriptive and educational only: no diagnosing
real people, no medical claims.

Demos: solution-explorer walkthroughs, machine-executed, all OK - real
computed values with tight-bounds asserts, never float exact-equality.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or
pushes. A merger handles registration.

Never the words "bat belt" anywhere. No website references. No Facebook.
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
from entries_unsolved_neuroscience import ENTRIES as EA, POINTER
from entries_unsolved_neuroscience_b import ENTRIES_B
from entries_unsolved_neuroscience_c import ENTRIES_C, SIG_TAIL
from demos_unsolved_neuroscience import DEMOS

ENTRIES = EA + ENTRIES_B + ENTRIES_C
LABEL = "Signature-generated proposed solution \u2014 not established science."

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    pub_line = ("Public records - 34 real, famous unsolved neuroscience "
                "problems, fact-checked: dreaming, attention, forgetting, "
                "memory consolidation, deja vu, prediction-error learning, "
                "pain, body ownership, few-shot learning, spatial "
                "representation, working memory limits, sensory "
                "cancellation, the full function of sleep, the neural "
                "code, the binding problem, the physical basis of memory, "
                "the rules of neuroplasticity, decision-making, emotion, "
                "language comprehension, creativity, lifelong learning, "
                "anesthesia and consciousness, volition, the neural "
                "correlates of consciousness, brain aging, brain-computer "
                "interface limits, neural self-repair, the receptor-to-"
                "experience gap, the circuit basis of psychosis, whole-"
                "brain mapping, the neural basis of the self, the hard "
                "problem of consciousness, and a complete computational "
                "theory of the brain. Every record carries the problem, "
                "its background, why it matters, and a pointer to the "
                "Signature proposed solution.")
    sig_line = ("Signature originals - his original Signature Neuroscience "
                "Method: the same 34 unsolved problems approached through "
                "the Signature lens of prediction, precision, and "
                "generative modeling. Every record carries the full "
                "proposed solution treatment - assumptions, reasoning "
                "path, proposed mechanism, what would confirm or refute "
                "it, and what it does not claim - always opening with the "
                "exact honesty label, never presented as established "
                "science.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(dreaming, attention, forgetting, consolidation, deja vu, "
              "prediction-error learning, pain, body ownership, few-shot "
              "learning, spatial maps, working memory, sensory "
              "cancellation) -> Compounded (sleep, the neural code, "
              "binding, the engram, plasticity rules, decision, emotion, "
              "language, creativity, lifelong learning, anesthesia, "
              "volition) -> Advanced (NCC, brain aging, BCI limits, "
              "self-repair, receptor-to-experience, psychosis circuits, "
              "whole-brain mapping, the self, the hard problem, a complete "
              "theory).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: problem, background, why it matters, signature solution, key points, requirements, standards, citations, and a working solution-explorer demonstration program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search dreaming, attention, forgetting, memory, sleep, neural code, binding, plasticity, consciousness, hard problem, BCI, engram...",
        "chat_ph": "Ask about unsolved neuroscience...",
        "archive_blurb": ("Seeded %s unsolved-neuroscience records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, problem, background, why_it_matters, signature_solution, "
                   "key_points, requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved-neuroscience studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the great unsolved problems of neuroscience, from why we dream and how attention works through the neural code, the binding problem, and the rules of plasticity, to the neural correlates of consciousness, the hard problem, and the search for a complete theory of the brain. Public records state each problem as the field knows it; Signature editions develop the proposed solution path, always labeled as proposed, never as settled science." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-neuroscience-study", "gen_demo_kind": "unsolved-neuroscience-demo",
        "source": source,
    }

ROLE_PUB = ("unsolved neuroscience archivist - the great open problems of the brain, from dreaming "
            "and attention through memory, sleep, the neural code, binding, plasticity, and decision, "
            "to consciousness, the hard problem, and a complete theory; teaching progressively along "
            "the ladder from foundations through compounded to advanced; answers from many angles - "
            "definition, example, analogy, application, history, math, how-to - using only archive "
            "data from this system")
ROLE_SIG = ("unsolved neuroscience archivist - Signature editions: his original Signature Neuroscience "
            "Method on the same 34 open problems, every proposed solution opening with the exact honesty "
            "label and never presented as established science; teaches progressively along the ladder; "
            "answers from many angles using only archive data from this system")

DBCFG = {}
DBCFG["unsolved-neuroscience"] = _cfg(
    "unsolved-neuroscience", "The Unsolved Neuroscience Database",
    "Thirty-four of the great unsolved problems of neuroscience, stated as the field knows them: "
    "from why we dream and what attention is, through memory, sleep, the neural code, and the rules "
    "of plasticity, to the neural correlates of consciousness, the hard problem, and the search for "
    "a complete computational theory of the brain. Taught progressively along the ladder.",
    "unsolved problem record", "JAH-USNS-", "JAH Unsolved Neuroscience Archivist",
    ROLE_PUB, "public")
DBCFG["unsolved-neuroscience-signature"] = _cfg(
    "unsolved-neuroscience-signature", "The Unsolved Neuroscience Signature Database",
    "The same 34 unsolved problems through his original Signature Neuroscience Method: prediction, "
    "precision, and generative modeling. Every record develops the full proposed solution approach - "
    "assumptions, reasoning path, proposed mechanism, what would confirm or refute it, and what it "
    "does not claim - always opening with the exact honesty label, never presented as established science.",
    "unsolved problem record", "JAH-USNSS-", "JAH Unsolved Neuroscience Archivist (Signature)",
    ROLE_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"
assert len(ENTRIES) == 34, "expected 34 entries"


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
                           + e["problem"])
            how = e["sig_lens"] + " " + e["background"]
            citations = list(e["citations"]) + [SIG_TAIL]
            signature_solution = e["signature_solution_full"]
        else:
            description = e["problem"]
            how = e["background"]
            citations = list(e["citations"])
            signature_solution = POINTER
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": signature_solution,
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

    # ---- dedupe pre-gate: all 68 titles vs the whole system before authoring
    print("dedupe pre-gate: 68 titles vs whole system", flush=True)
    refusals = []
    for slug in ("unsolved-neuroscience", "unsolved-neuroscience-signature"):
        sig = slug.endswith("-signature")
        for e in ENTRIES:
            title = e["name"] + (" (Signature Edition)" if sig else "")
            hits = [h for h in base.GATE.check(slug, title) if h[0] != slug]
            if hits:
                refusals.append((title, hits))
    if refusals:
        for t, h in refusals:
            print("REFUSED: %s -> %s" % (t, h), flush=True)
        raise SystemExit("dedupe pre-gate refused %d titles" % len(refusals))
    print("dedupe pre-gate: zero collisions across 68 titles", flush=True)

    built = {}
    for slug in ("unsolved-neuroscience", "unsolved-neuroscience-signature"):
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
            for k in ("id", "t", "g", "name", "title", "problem", "background",
                      "why_it_matters", "signature_solution", "description",
                      "how_it_works", "key_points", "requirements",
                      "standards", "citations", "src", "ladder_rank",
                      "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert len(r["problem"]) > 200 and len(r["background"]) > 200, \
                "thin problem/background in %s" % r["id"]
            assert len(r["why_it_matters"]) > 100, "thin why_it_matters in %s" % r["id"]
            assert r["signature_solution"].startswith(LABEL), \
                "honesty label missing in %s" % r["id"]
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
                assert len(r["signature_solution"]) > 1500, "thin sig solution in %s" % r["id"]
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # ---- machine-execute all 68 demos
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    # ---- pages (template replication); no manifest/api writes, no commit
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
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        # node --check on extracted page scripts (exclude ld+json) and gen js
        scripts = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                             page, flags=re.S)
        with open(ppath, "r", encoding="utf-8") as f:
            live = f.read()
        live_scripts = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                                  live, flags=re.S)
        for i, s in enumerate(live_scripts):
            if not s.strip():
                continue
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                tf.write(s)
                tp = tf.name
            q = subprocess.run(["node", "--check", tp], capture_output=True, text=True)
            os.unlink(tp)
            assert q.returncode == 0, "node --check failed on page script %d in %s: %s" % (i, slug, q.stderr[:500])
        q = subprocess.run(["node", "--check", gpath], capture_output=True, text=True)
        assert q.returncode == 0, "node --check failed on %s: %s" % (gpath, q.stderr[:500])
        print("page:  db/%s/index.html + gen-%s.js [%s] node --check clean" % (slug, slug, ", ".join(notes)), flush=True)

    # ---- fragment for the merger
    def frag(slug, source):
        c = DBCFG[slug]
        base_url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        ai = c["ai"]
        return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
                "record_kind": c["record_kind"], "id_prefix": c["prefix"],
                "ai_name": ai, "local_index": base_url, "record_count": 34,
                "status": "live", "full_records": 34, "index": base_url,
                "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
                "source": source}
    fragment = {"public": frag("unsolved-neuroscience", "public-harvest"),
                "signature": frag("unsolved-neuroscience-signature", "signature")}
    fpath = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-neuroscience.json"
    os.makedirs(os.path.dirname(fpath), exist_ok=True)
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath, flush=True)
    print("DONE: 68 records, 68 demos OK, pages + shards written. manifest/api untouched; no commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
