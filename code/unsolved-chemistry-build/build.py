#!/usr/bin/env python3
"""Build the Unsolved Chemistry databases for JAH Databases
(Manon 16:15 orders, Unsolved Problems Solved series, batch 1).

34 famous unsolved chemistry problems, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex):

  unsolved-chemistry             - The Unsolved Chemistry Database
                                   (public-harvest: real, fact-checked
                                   unsolved problems - every record carrying
                                   problem, background, why_it_matters, and
                                   a signature_solution pointer; src
                                   public-harvest)
  unsolved-chemistry-signature   - The Unsolved Chemistry Signature Database
                                   (his original Signature solution
                                   approaches: every record carries the full
                                   step-by-step treatment opening with the
                                   EXACT label "Signature-generated proposed
                                   solution - not established science";
                                   titles suffixed " (Signature Edition)";
                                   src signature; never presented as
                                   authentic public record)

ID prefixes: JAH-USCH- (public) and JAH-USCHS- (signature), verified free
2026-10-17 in the manifest id_prefix values and across all shard index
files (zero hits).

Demos: all 68 are solution-explorer walkthroughs with confirm/refute
panels (see demos_unsolved_chemistry.py) - real computed values, tight
bounds asserts (never float exact-equality), machine-executed below.

Honesty rule: never claim proof, never imply peer acceptance, never
present speculation as settled.

Never the words "bat belt" anywhere. No website references. No Facebook.
No manifest/api.json/index.html/README/AI_ACCESS writes and no git
operations - a merger handles those.
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
FRAG = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-chemistry.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_chemistry import ENTRIES, SIG_TAIL, LABEL
from demos_unsolved_chemistry import DEMOS

# ---------------------------------------------------------------- DB config
# NOTE: role / ai_name / greet / search strings are apostrophe-free (JS hygiene).


def _cfg(name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature solution "
                "approaches to famous unsolved chemistry problems: every "
                "record walks the proposed solution step by step with "
                "adjustable assumptions and a confirm-or-refute panel, "
                "opening with the exact label Signature-generated proposed "
                "solution - not established science. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked unsolved chemistry "
                "problems: water anomalies, the glass transition, protein "
                "folding, homochirality, enzyme catalysis, photosynthesis, "
                "batteries, corrosion, catalysis design, superconductivity, "
                "and more - every record carrying the problem, its "
                "background, why it matters, and a pointer to the "
                "Signature solution approach, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Approachable "
              "(everyday mysteries anyone can grasp - freezing water, "
              "strange water, smell, protein folding, enzymes, the "
              "hydrophobic effect, handedness of life, origin of life, "
              "photosynthesis, glass, proton hopping, water surfaces) -> "
              "Deep (crystal nucleation, crystal prediction, batteries, "
              "corrosion, forever chemicals, nitrogen fixation, CO2 to "
              "fuel, hydrogen storage, active sites, catalyst design, "
              "isotope separation) -> Frontier (molecular machines, "
              "organic electronics, molecular computing, chemical space, "
              "open-shell modeling, interstellar chemistry, metallic "
              "hydrogen, high-temperature superconductivity, inverse "
              "materials design, superheavy elements, artificial enzymes).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: problem, background, "
                  "why it matters, the Signature solution approach, key points, "
                  "citations, and a working solution-explorer demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search unsolved problems, water anomalies, glass transition, protein folding, homochirality, enzymes, photosynthesis, batteries, corrosion, catalysis, superconductivity...",
        "chat_ph": "Ask about unsolved chemistry problems...",
        "archive_blurb": ("Seeded %s unsolved chemistry records, marching toward one million records. "
                          "Presented in teaching-ladder order: approachable, deep, frontier."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, problem, background, why_it_matters, "
                   "signature_solution, key_points, src, ladder_rank, ladder_tier, demo"),
        "fields": "Approachable \u00b7 Deep \u00b7 Frontier - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved-chemistry studies. Seeded archive records are the authoritative entries.",
        "greet": ("I am the %s. Ask me about unsolved chemistry - from freezing water, strange water, smell, "
                  "protein folding, enzymes, the hydrophobic effect, the handedness of life, the origin of life, "
                  "photosynthesis, glass, proton hopping, and water surfaces, through crystal nucleation, batteries, "
                  "corrosion, forever chemicals, nitrogen fixation, CO2 to fuel, hydrogen storage, active sites, "
                  "catalyst design, and isotope separation, to molecular machines, organic electronics, molecular "
                  "computing, chemical space, open-shell modeling, interstellar chemistry, metallic hydrogen, "
                  "high-temperature superconductivity, inverse materials design, superheavy elements, and artificial "
                  "enzymes." % ai),
        "gen_fields": ["Approachable", "Deep", "Frontier"],
        "gen_kind": "unsolved-chemistry-study", "gen_demo_kind": "unsolved-chemistry-demo",
        "source": source,
    }


CIT_PUB = ("Unsolved problems in chemistry (standard references: Atkins P, "
           "de Paula J. Physical Chemistry. 11th ed. Oxford University "
           "Press; 2018; Clayden J, Greeves N, Warren S. Organic Chemistry. "
           "2nd ed. Oxford University Press; 2012; Housecroft CE, Sharpe AG. "
           "Inorganic Chemistry. 5th ed. Pearson; 2018; plus the landmark "
           "papers and reviews cited per record).")
CIT_SIG = CIT_PUB + (" Signature editions carry his original Signature "
                     "solution approaches - proposed paths, labeled as "
                     "such, never presented as established science.")

DBCFG = {}
DBCFG["unsolved-chemistry"] = _cfg(
    "The Unsolved Chemistry Database",
    "Famous unsolved chemistry problems, fact-checked: water anomalies, the "
    "glass transition, protein folding, homochirality, enzyme catalysis, "
    "photosynthesis, batteries, corrosion, catalysis, superconductivity, "
    "and more - every record carrying the problem, its background, why it "
    "matters, and a pointer to the Signature solution approach.",
    "unsolved problem record", "JAH-USCH-", "JAH Unsolved Chemistry Archivist",
    "unsolved chemistry archivist - the famous open problems of chemistry, "
    "fact-checked: problem, background, why it matters, and the Signature "
    "solution pointer; teaching progressively along the ladder from "
    "approachable through deep to frontier; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    "public")
DBCFG["unsolved-chemistry-signature"] = _cfg(
    "The Unsolved Chemistry Signature Database",
    "His original Signature solution approaches to famous unsolved "
    "chemistry problems: every record walks a proposed solution step by "
    "step - assumptions, reasoning path, proposed mechanism, what would "
    "confirm or kill it - opening with the exact label Signature-generated "
    "proposed solution - not established science. Clearly labeled "
    "Signature-made, never presented as established science.",
    "unsolved problem record", "JAH-USCHS-", "JAH Unsolved Chemistry Archivist (Signature)",
    "unsolved chemistry archivist - Signature editions: his original "
    "proposed solution approaches to famous unsolved chemistry problems, "
    "each labeled Signature-generated proposed solution - not established "
    "science, never presented as established science; teaches progressively "
    "along the ladder from approachable through deep to frontier; answers "
    "from many angles using only archive data from this system",
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
        if sig:
            solution = e["sig_full"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            solution = e["sig_pointer"]
            citations = list(e["citations"])
        assert solution.startswith(LABEL), "honesty label missing in %s" % title
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": solution,
            "key_points": list(e["key_points"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, title, rid, e["group"],
                          e["key_points"], solution[:200])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Solution-explorer walkthrough: working demonstration program (real, runnable Python)."}
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
    for slug in ("unsolved-chemistry", "unsolved-chemistry-signature"):
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
                      "why_it_matters", "signature_solution", "key_points",
                      "citations", "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["background"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("approachable", "deep", "frontier"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            assert r["signature_solution"].startswith(LABEL), "label drift in %s" % r["id"]
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
        assert "synthetic intelligence" not in gen_js.lower(), "template leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # JS hygiene: node --check on extracted page scripts and gen-*.js (skip ld+json)
    import re as _re
    for slug in built:
        ppath = os.path.join(REPO, "db", slug, "index.html")
        src = open(ppath, encoding="utf-8").read()
        scripts = _re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                              src, flags=_re.S)
        for i, body in enumerate(scripts):
            if not body.strip():
                continue
            sp = "/tmp/uc_script_%s_%d.js" % (slug.replace("-", "_"), i)
            open(sp, "w", encoding="utf-8").write(body)
            p = subprocess.run(["node", "--check", sp], capture_output=True, text=True)
            assert p.returncode == 0, "node --check failed %s script %d: %s" % (slug, i, p.stderr[-500:])
        gp = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
        p = subprocess.run(["node", "--check", gp], capture_output=True, text=True)
        assert p.returncode == 0, "node --check failed gen js %s: %s" % (slug, p.stderr[-500:])
    print("JS hygiene: node --check clean on page scripts + gen-*.js", flush=True)

    # fragment for the merger
    def frag_entry(slug, source):
        cfg = DBCFG[slug]
        tag = ("Signature-labeled proposed solutions to famous unsolved chemistry "
               "problems - step-by-step solution explorers with confirm-or-refute panels."
               if source == "signature" else
               "Famous unsolved chemistry problems, fact-checked - problem, background, "
               "why it matters, and a pointer to the Signature solution approach.")
        ai = cfg["ai"]
        return {
            "slug": slug,
            "name": cfg["name"],
            "tagline": tag,
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": ai,
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if source == "signature" else "public-harvest",
        }

    frag = {"public": frag_entry("unsolved-chemistry", "public"),
            "signature": frag_entry("unsolved-chemistry-signature", "signature")}
    os.makedirs(os.path.dirname(FRAG), exist_ok=True)
    with open(FRAG, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAG, flush=True)
    print("DONE: %d records built (no manifest/api writes, no git - merger handles those)." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
