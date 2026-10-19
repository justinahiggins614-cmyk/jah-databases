#!/usr/bin/env python3
"""Build the Unsolved Economics databases for JAH Databases
(Manon's 16:15 orders, Unsolved Problems Solved series, batch 1).

Two NEW databases, 34 ladder-ordered records each:

  unsolved-economics            - The Unsolved Economics Database (public-harvest:
                                  the field's real famous unsolved problems -
                                  business cycle's full cause, equity premium
                                  puzzle, crisis prediction, optimal taxation,
                                  behavioral foundations, inequality dynamics,
                                  and 28 more - every record carrying problem,
                                  background, why_it_matters, and a
                                  signature_solution pointer)
  unsolved-economics-signature  - The Unsolved Economics Signature Database
                                  (the SAME 34 problems through the Signature
                                  lens; titles suffixed " (Signature Edition)",
                                  src signature, clearly labeled
                                  Signature-made, never presented as authentic
                                  public record or established science)

Every signature_solution OPENS WITH THE EXACT LABEL:
"Signature-generated proposed solution -- not established science."
Honesty rule enforced: never claims proof, never implies peer acceptance,
never presents speculation as settled.

ID prefixes: JAH-USEC- (public) and JAH-USECS- (signature), verified free in
the manifest id_prefix values (zero hits) and in every shard index file of
jah-databases-data-1 (zero hits) before authoring. All 68 titles dedupe-gated
against the whole system before authoring: zero collisions.

Ladder: 34 unique ranks 1-34 (foundations 1-11, compounded 12-23, advanced
24-34); the shard index is written in ladder order so pages present simple
-> compounded -> complex.

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_unsolved_economics.py). Every demo is a solution-explorer
walkthrough: steps through the Signature approach, adjustable assumption
knobs, computed values, CONFIRM/REFUTE panels, tight-bounds asserts (never
float exact-equality), OK marker. The build machine-executes all 68 demos.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes. A merger handles registration. Outputs only:
  db/unsolved-economics/ + db/unsolved-economics-signature/ (index.html + gen-*.js)
  code/unsolved-economics-build/{build.py, entries_*.py, demos_*.py}
  jah-databases-data-1/data/unsolved-economics[-signature]/ (index.jsonl.gz + chunks/)
  hidden_files/missing-builds/fragments/unsolved-economics.json

Never the words "bat belt" anywhere. No website references. No Facebook.
Human-readable sentences and paragraphs throughout.
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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_economics import ENTRIES, SIG_TAIL, SIG_LABEL
from demos_unsolved_economics import DEMOS, DEMOS_SIG

# ---------------------------------------------------------------- DB config

def _cfg(name, tagline, record_kind, prefix, ai, role, citation, source):
    pub_line = ("Public records - the field's real famous unsolved problems, "
                "fact-checked: the full cause of the business cycle, the equity "
                "premium puzzle, stock market participation, home bias, the "
                "productivity slowdown, the flattened Phillips curve, worker "
                "immobility, the happiness paradox, bubbles, Feldstein-Horioka, "
                "crisis prediction, the forward premium, exchange-rate disconnect, "
                "the Lucas paradox, current-account dark matter, productivity "
                "dispersion, the labor share decline, minimum-wage effects, top "
                "inequality dynamics, the gender wage gap, deficits, fiscal "
                "multipliers, optimal taxation, behavioral foundations, the social "
                "cost of carbon, the zero lower bound, r-star, AI and labor, "
                "patent length, corruption, platform monopoly, demographics and "
                "saving, and expectations formation - every record carrying the "
                "problem, its background, why it matters, and a labeled pointer "
                "to the Signature proposal, organized in the Signature system.")
    sig_line = ("Signature originals - the same 34 famous problems read through "
                "the Signature lens, each with the Signature system's proposed "
                "solution approach: assumptions, reasoning path, proposed "
                "mechanism, what would confirm or kill it, and what it does NOT "
                "claim. Every solution opens with the exact label "
                "'Signature-generated proposed solution - not established "
                "science.' Clearly labeled Signature-made, never presented as "
                "established science or authentic public record.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the growth question, the business cycle, the equity premium, "
              "participation, home bias, the productivity slowdown, the Phillips "
              "curve, worker immobility, happiness, bubbles, Feldstein-Horioka) "
              "-> Compounded (crisis prediction, the forward premium, exchange "
              "rates, the Lucas paradox, dark matter, productivity dispersion, "
              "the labor share, minimum wages, top inequality, the gender gap, "
              "deficits, multipliers) -> Advanced (optimal taxation, behavioral "
              "foundations, the social cost of carbon, the zero lower bound, "
              "r-star, AI and labor, patent length, corruption, platform "
              "monopoly, demographics, expectations formation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: problem, background, "
                  "why it matters, the labeled Signature proposal, how the phenomenon "
                  "works, key points, what solving it requires, standards, citations, "
                  "and a working solution-explorer demonstration program.%s"
                  % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": ("Search equity premium puzzle, business cycle, financial crises, "
                      "optimal taxation, behavioral economics, inequality, Phillips curve, "
                      "exchange rates, r-star, expectations..."),
        "chat_ph": "Ask about the unsolved problems of economics...",
        "archive_blurb": ("Seeded %s unsolved-problem records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, problem, background, why_it_matters, "
                   "signature_solution, description, how_it_works, key_points, "
                   "requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": ("Generate clearly-labeled unsolved-economics studies. Seeded archive "
                     "records are the authoritative entries; Signature proposals are labeled "
                     "proposals, never established science."),
        "greet": "I am the %s. Ask me about the great unsolved problems of economics - from growth and business cycles through asset pricing, labor, money, and international economics, to taxation, behavior, climate, and expectations - and I will teach them progressively along the ladder, simple first, then compounded, then most complex." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-economics-study", "gen_demo_kind": "unsolved-economics-demo",
        "source": source,
    }

CIT_PUB = ("Unsolved problems of economics (standard references: Samuelson PA. "
           "Economics. McGraw-Hill; 1948; Keynes JM. The General Theory of "
           "Employment, Interest and Money. Macmillan; 1936; Friedman M. A Theory "
           "of the Consumption Function. Princeton University Press; 1957; Solow "
           "RM. A Contribution to the Theory of Economic Growth. Quarterly "
           "Journal of Economics; 1956; Mankiw NG. Principles of Economics. 9th "
           "ed. Cengage; 2021; Piketty T. Capital in the Twenty-First Century. "
           "Harvard University Press; 2014; Shiller RJ. Irrational Exuberance. "
           "3rd ed. Princeton University Press; 2015; Kahneman D. Thinking, Fast "
           "and Slow. Farrar, Straus and Giroux; 2011; Stiglitz JE. The Price of "
           "Inequality. W. W. Norton; 2012; Acemoglu D, Robinson JA. Why Nations "
           "Fail. Crown Business; 2012; plus the per-record landmarks cited in "
           "each entry).")
CIT_SIG = CIT_PUB + (" Signature editions carry the Signature system's proposed "
                     "solution approaches, each opening with the exact label "
                     "'Signature-generated proposed solution - not established "
                     "science,' clearly labeled Signature-made.")

DBCFG = {}
DBCFG["unsolved-economics"] = _cfg(
    "The Unsolved Economics Database",
    "Famous unsolved problems of economics, fact-checked: growth, business "
    "cycles, asset pricing puzzles, labor, money, international economics, "
    "policy, behavior, climate, and expectations - each with its history, its "
    "stakes, and a labeled pointer to the Signature proposal, taught "
    "progressively along the ladder.",
    "unsolved problem record", "JAH-USEC-", "JAH Unsolved Economics Archivist",
    "unsolved economics archivist - the great open problems of the field, fact-checked "
    "and taught progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this "
    "system; when asked whether a problem is solved, answers honestly that it is "
    "open in established science and the Signature approach is a labeled proposal",
    CIT_PUB, "public")
DBCFG["unsolved-economics-signature"] = _cfg(
    "The Unsolved Economics Signature Database",
    "The same 34 famous problems through the Signature lens: the Signature "
    "system's proposed solution approaches - assumptions, reasoning paths, "
    "proposed mechanisms, what would confirm or kill each, and what each does "
    "NOT claim - every one opening with the exact label "
    "'Signature-generated proposed solution - not established science.' "
    "Clearly labeled Signature-made, never presented as established science "
    "or authentic public record.",
    "unsolved problem record", "JAH-USECS-", "JAH Unsolved Economics Archivist (Signature)",
    "unsolved economics archivist - Signature editions: the same 34 famous "
    "problems through the Signature lens, each with a proposed solution approach "
    "opening with the exact label Signature-generated proposed solution - not "
    "established science; clearly labeled Signature-made and never presented as "
    "established science or authentic public record; teaches progressively along "
    "the ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"
assert set(DEMOS_SIG) == {e["key"] for e in ENTRIES}, "sig demo map misses entries"


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
                           + e["description"] + " " + e["problem"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
            sigsol = e["sig_full"]
        else:
            description = e["description"] + " " + e["problem"]
            how = e["how_it_works"]
            citations = list(e["citations"])
            sigsol = e["sig_pointer"]
        assert sigsol.startswith(SIG_LABEL), "label missing in %s" % title
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": sigsol,
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
        demo_fn = (DEMOS_SIG if sig else DEMOS)[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": ("Working solution-explorer demonstration program "
                                "(real, runnable Python).")}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    assert ranks == list(range(1, 35)), "ladder ranks must be 1-34 for %s" % slug
    return recs


def js_hygiene_check(paths):
    """node --check every extracted page <script> (minus ld+json) and gen-*.js."""
    for p in paths:
        with open(p, "r", encoding="utf-8") as f:
            html = f.read()
        blocks = re.findall(
            r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
            html, flags=re.S)
        for i, b in enumerate(blocks):
            if not b.strip():
                continue
            tmp = "/tmp/use_jscheck_%d.js" % i
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(b)
            r = subprocess.run(["node", "--check", tmp], capture_output=True,
                               text=True, timeout=60)
            assert r.returncode == 0, "JS syntax fail %s block %d: %s" % (
                p, i, r.stderr[-500:])
        print("  js-hygiene OK: %s (%d script blocks)" % (p, len(blocks)), flush=True)


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
    for slug in ("unsolved-economics", "unsolved-economics-signature"):
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
                      "how_it_works", "key_points", "requirements", "standards",
                      "citations", "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert len(r["background"]) > 400, "thin background in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            assert r["signature_solution"].startswith(SIG_LABEL), \
                "label missing in %s" % r["id"]
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
            assert "CONFIRM panel:" in p.stdout and "REFUTE panel:" in p.stdout, \
                "demo missing confirm/refute panels %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    gen_paths = []
    page_paths = []
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
            tier = {"foundations": "Foundations", "compounded": "Compounded",
                    "advanced": "Advanced"}[r["ladder_tier"]]
            topics.setdefault(tier, []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        page_paths.append(ppath)
        gen_paths.append(gpath)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    js_hygiene_check(page_paths)
    for gpath in gen_paths:
        r = subprocess.run(["node", "--check", gpath], capture_output=True,
                           text=True, timeout=60)
        assert r.returncode == 0, "JS syntax fail %s: %s" % (gpath, r.stderr[-500:])
        print("  js-hygiene OK: %s" % gpath, flush=True)

    # NOTE: manifest.json / api.json / index.html / README / docs are the merger's
    # job. This build deliberately does NOT touch them.
    print("manifest/api untouched (merger's job); shard + pages written.", flush=True)

    frag = {
        "public": {
            "slug": "unsolved-economics",
            "name": "The Unsolved Economics Database",
            "tagline": DBCFG["unsolved-economics"]["tagline"],
            "record_kind": "unsolved problem record",
            "id_prefix": "JAH-USEC-",
            "ai_name": "JAH Unsolved Economics Archivist",
            "local_index": SHARD_BASE + "/data/unsolved-economics/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/unsolved-economics/index.jsonl.gz",
            "chunk_pattern": "data/unsolved-economics/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "unsolved-economics-signature",
            "name": "The Unsolved Economics Signature Database",
            "tagline": DBCFG["unsolved-economics-signature"]["tagline"],
            "record_kind": "unsolved problem record",
            "id_prefix": "JAH-USECS-",
            "ai_name": "JAH Unsolved Economics Archivist (Signature)",
            "local_index": SHARD_BASE + "/data/unsolved-economics-signature/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/unsolved-economics-signature/index.jsonl.gz",
            "chunk_pattern": "data/unsolved-economics-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    frag_path = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-economics.json"
    os.makedirs(os.path.dirname(frag_path), exist_ok=True)
    with open(frag_path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % frag_path, flush=True)
    print("NEXT: merger verifies and registers (manifest/api/restamp/commit).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
