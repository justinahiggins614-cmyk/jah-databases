#!/usr/bin/env python3
"""Build the Unsolved Psychology databases for JAH Databases
(Manon 2026-10-17 16:15 Unsolved Problems Solved series, batch 1).

Verified 2026-10-17: ID prefixes JAH-USPS- (public) / JAH-USPSS-
(signature) return zero hits in the manifest id_prefix values AND in
all 872 shard index files of jah-databases-data-1 (raw zgrep sweep).
Slug unsolved-psychology is new (only unsolved-mysteries exists, a
different database).

So this build creates two NEW databases, 34 ladder-ordered records each:

  unsolved-psychology              - The Unsolved Psychology Database
                                     (public-harvest: 34 real,
                                     fact-checked unsolved problems of
                                     psychology, ladder-ordered by
                                     problem accessibility, rank 1-34)
  unsolved-psychology-signature    - The Unsolved Psychology Signature
                                     Database
                                     (the same 34 problems through the
                                     Signature lens: titles suffixed
                                     " (Signature Edition)", src
                                     signature, the full Signature-
                                     generated proposed solution
                                     approach per record, clearly
                                     labeled Signature-made, never
                                     presented as authentic public
                                     record)

Every record carries: id, t, g, name, title, problem, background,
why_it_matters, signature_solution, src, ladder_rank, ladder_tier,
demo. The signature_solution OPENS WITH THE EXACT LABEL
"Signature-generated proposed solution — not established science".
The public half carries a short pointer to the signature companion
record; the signature half carries the full treatment. Honesty rule:
no claim of proof, no implied peer acceptance, no speculation
presented as settled. Descriptive and educational only.

Pipeline: dedupe pre-pass on all 68 titles vs the WHOLE system ->
build records -> validate (incl. label-opener and confirm/refute
cross-checks) -> write shard DBs (index.jsonl.gz + chunk-0000.jsonl.gz)
-> machine-execute all 68 demos -> build db pages + gen js (swept) ->
node --check hygiene -> write merger fragment.

This builder NEVER touches data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md and NEVER commits or pushes. A merger
handles registration.

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-psychology.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_psychology import (
    ENTRIES, LABEL, public_solution, signature_solution, expected_net)
from demos_unsolved_psychology import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature reading of "
                "psychology's open problems: every unsolved problem a "
                "locked door in the mind, the Signature method the key "
                "cut from first principles. Clearly labeled "
                "Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - 34 real, fact-checked unsolved problems "
                "of psychology: dream function, yawning, laughter, tears, "
                "deja vu, sleep function, the placebo effect, the nature "
                "of emotion, forgetting, motivation, bias persistence, "
                "language acquisition, creativity, linguistic relativity, "
                "stress and trauma, moral judgment, altruism, attention, "
                "the binding problem, the self, decision timing, memory "
                "consolidation, nature and nurture, the full picture of "
                "intelligence, the Flynn effect, the replication crisis, "
                "the unconscious, the causes of depression, the causes of "
                "schizophrenia, measuring consciousness, the hard "
                "problem, other minds, matter and experience, and the "
                "full architecture of mind.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(ranks 1-12: dreams, yawning, laughter, tears, deja vu, "
              "sleep, placebo, emotion, forgetting, motivation, bias, "
              "language acquisition) -> Compounded (ranks 13-24: "
              "creativity, linguistic relativity, stress and trauma, "
              "moral judgment, altruism, attention, the binding problem, "
              "the self, decision timing, memory consolidation, nature "
              "and nurture, intelligence in full) -> Advanced (ranks "
              "25-34: the Flynn effect, the replication crisis, the "
              "unconscious, depression, schizophrenia, measuring "
              "consciousness, the hard problem, other minds, matter and "
              "experience, the full architecture of mind).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: the problem, "
                  "its background, why it matters, and the Signature-"
                  "generated proposed solution approach, plus a working "
                  "solution-explorer demonstration program.%s"
                  % (tagline, sig_line if source == "signature" else pub_line,
                     ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": ("Search dreams, yawning, laughter, tears, deja vu, sleep, "
                      "placebo, emotion, forgetting, motivation, bias, language, "
                      "creativity, trauma, morals, altruism, attention, binding, "
                      "self, free will, memory, intelligence, Flynn effect, "
                      "replication, unconscious, depression, schizophrenia, "
                      "consciousness..."),
        "chat_ph": "Ask about psychology's open problems...",
        "archive_blurb": ("Seeded 34 %s unsolved-psychology records, marching "
                          "toward one million records. Presented in teaching-"
                          "ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature"
                             else "public-record")),
        "schema": ("id, t, g, name, title, problem, background, "
                   "why_it_matters, signature_solution, src, ladder_rank, "
                   "ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": ("Generate clearly-labeled unsolved-psychology studies. "
                     "Seeded archive records are the authoritative entries. "
                     "Solutions are Signature-generated proposals, never "
                     "established science."),
        "greet": ("I am the %s. Ask me about the open problems of psychology, "
                  "from why we dream through memory, emotion, motivation, "
                  "language, intelligence, and mental health science to "
                  "consciousness itself. I teach step by step, simple first, "
                  "and I always mark proposed solutions as proposals." % ai),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-psychology-study",
        "gen_demo_kind": "unsolved-psychology-demo",
        "source": source,
    }

CIT_PUB = ("Unsolved problems of psychology (standard references: Freud S. "
           "The Interpretation of Dreams. 1900; James W. The Principles of "
           "Psychology. 1890; Ebbinghaus H. Memory. 1885; Spearman C. 1904; "
           "Maslow AH. 1943; Chomsky N. 1959; Schachter S, Singer JE. 1962; "
           "Tversky A, Kahneman D. 1974; Hobson JA, McCarley RW. 1977; "
           "Treisman A. 1980; Libet B. 1983; Gardner H. 1983; Chalmers DJ. "
           "1995; Haidt J. 2001; Barrett LF. 2017; Open Science Collaboration. "
           "2015; Moncrieff J et al. 2022).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "reading - every open problem a locked door in the "
                     "mind, the Signature method the key cut from first "
                     "principles - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["unsolved-psychology"] = _cfg(
    "unsolved-psychology", "The Unsolved Psychology Database",
    "The great open questions of psychology - dream function, the binding "
    "problem, free will, memory, intelligence, the replication crisis, "
    "consciousness - 34 real, fact-checked unsolved problems, each with "
    "the Signature system's proposed solution approach, clearly labeled "
    "as proposal, never established science.",
    "unsolved problem record", "JAH-USPS-",
    "JAH Unsolved Psychology Archivist",
    "unsolved psychology archivist - the open problems of psychology from "
    "dreams and sleep through memory, emotion, motivation, language, "
    "intelligence, and mental health science to consciousness; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from "
    "this system; marks every proposed solution as Signature-generated, "
    "never established science",
    CIT_PUB, "public")
DBCFG["unsolved-psychology-signature"] = _cfg(
    "unsolved-psychology-signature",
    "The Unsolved Psychology Signature Database",
    "His original Signature reading of psychology's open problems: the "
    "same 34 unsolved problems seen through the Signature lens, each with "
    "a full proposed solution approach - assumptions, reasoning path, "
    "confirm and refute lines. Clearly labeled Signature-made, never "
    "presented as authentic public record, never established science.",
    "unsolved problem record", "JAH-USPSS-",
    "JAH Unsolved Psychology Archivist (Signature)",
    "unsolved psychology archivist - Signature editions: his original "
    "Signature reading of the open problems, every problem a locked door "
    "in the mind and the Signature method the key cut from first "
    "principles, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"
assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)


def _tier_for(rank):
    return ("foundations" if rank <= 12 else
            "compounded" if rank <= 24 else "advanced")


def prepass_dedupe():
    """Check all 68 titles vs the WHOLE system BEFORE authoring records."""
    titles = []
    for e in ENTRIES:
        titles.append(("unsolved-psychology", e["name"]))
        titles.append(("unsolved-psychology-signature",
                       e["name"] + " (Signature Edition)"))
    refused = []
    for slug, title in titles:
        hits = [h for h in base.GATE.check(slug, title) if h[0] != slug]
        if hits:
            refused.append((title, hits))
    print("dedupe pre-pass: %d titles checked, %d cross-db collisions"
          % (len(titles), len(refused)), flush=True)
    for title, hits in refused:
        print("  REFUSED: %r already in %s"
              % (title, ", ".join("%s:%s" % (s, i) for s, i in hits)),
              flush=True)
    return refused


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
        companion = "JAH-USPSS-%06d" % (len(recs) + 1)
        sol = signature_solution(e) if sig else public_solution(companion)
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name,
            "title": title,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": sol,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, title, rid, e["group"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": ("Solution-explorer walkthrough: five steps, "
                                "adjustable assumptions, confirm/refute "
                                "panels, computed verdict. Working "
                                "demonstration program (real, runnable "
                                "Python).")}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def validate(built):
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        sig = slug.endswith("-signature")
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), \
            "prefix drift in %s" % slug
        assert len(recs) == 34, \
            "expected 34 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "problem",
                      "background", "why_it_matters", "signature_solution",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog, "missing demo in %s" % r["id"]
            assert len(r["problem"]) > 60, "stub problem in %s" % r["id"]
            assert len(r["background"]) > 300, "stub background in %s" % r["id"]
            assert len(r["why_it_matters"]) > 100, \
                "stub why_it_matters in %s" % r["id"]
            assert len(r["signature_solution"]) > 200, \
                "stub solution in %s" % r["id"]
            assert r["signature_solution"].startswith(LABEL), \
                "label opener missing in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, \
                "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] == _tier_for(r["ladder_rank"]), \
                "tier/rank mismatch in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded",
                                        "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            key = r["demo"]["program"].split("KEY = ")[1].split("\n")[0]
            e = next(x for x in ENTRIES if repr(x["key"]) == key)
            # cross-check: every confirm/refute label must appear in the
            # signature solution text (signature half carries the full
            # treatment; public half carries only the pointer), and the
            # demo prints the same items as the entry.
            for label, _text, _w in e["confirm"] + e["refute"]:
                assert label in prog, \
                    "panel label %r not in demo of %s" % (label, r["id"])
                if sig:
                    assert label.lower() in r["signature_solution"].lower(), \
                        "panel label %r not in solution text of %s" % (label,
                                                                       r["id"])
            assert e["problem"] in prog, \
                "demo problem text drift in %s" % r["id"]
            if sig:
                assert "(signature edition)" in r["title"].lower(), \
                    "sig title missing suffix"
                assert r["src"] == "signature"
                assert "what it does not claim" in r["signature_solution"].lower(), \
                    "sig solution missing scope limit in %s" % r["id"]
            else:
                assert r["src"] == "public-harvest"
                assert "JAH-USPSS-" in r["signature_solution"], \
                    "public pointer missing companion id in %s" % r["id"]
    print("validation: all record checks passed", flush=True)


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = ("/home/hatch/workspace/goals/database-quality-audit/"
                  "hidden_files/patches/sweep-db-pages.py")
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    refused = prepass_dedupe()
    assert not refused, "dedupe pre-pass found collisions; refusing to build"

    built = {}
    for slug in ("unsolved-psychology", "unsolved-psychology-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    validate(built)

    total = 0
    for slug, recs in built.items():
        n = base.write_shard_db(slug, recs)
        total += n
        print("shard: %-38s %d records" % (slug, n), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, \
                "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            assert "CONFIRM panel" in p.stdout and "REFUTE panel" in p.stdout, \
                "demo missing panels %s" % r["id"]
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
        assert "pill-ex" in page and "qmerge" in page, \
            "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), \
            "template leftover in %s" % slug
        assert "universal build" not in page.lower(), \
            "field leftover in %s" % slug
        assert "universal-build" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), \
            "banned phrase in page %s" % slug
        for s in (DBCFG[slug]["role"], DBCFG[slug]["ai"],
                  DBCFG[slug]["greet"], DBCFG[slug]["search_ph"]):
            assert "'" not in s, "apostrophe in JS string: %r" % s[:40]
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
        assert "facebook" not in gen_js.lower() and \
            "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), \
            "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        # node --check hygiene on extracted page scripts (excluding
        # ld+json blocks, which are JSON not JS) and on gen-*.js
        scripts = re.findall(
            r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
            page, flags=re.S)
        with tempfile.TemporaryDirectory() as td:
            for i, s in enumerate(scripts):
                if not s.strip():
                    continue
                sp = os.path.join(td, "page-%d.js" % i)
                with open(sp, "w", encoding="utf-8") as f:
                    f.write(s)
                p = subprocess.run(["node", "--check", sp],
                                   capture_output=True, text=True,
                                   timeout=60)
                assert p.returncode == 0, \
                    "node --check failed page script %d: %s" % (i, p.stderr[-500:])
            p = subprocess.run(["node", "--check", gpath],
                               capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, \
                "node --check failed gen js: %s" % p.stderr[-500:]
        print("page:  db/%s/index.html + gen-%s.js [%s] (node clean)"
              % (slug, slug, ", ".join(notes)), flush=True)

    frag = {
        "public": {
            "slug": "unsolved-psychology",
            "name": "The Unsolved Psychology Database",
            "tagline": DBCFG["unsolved-psychology"]["tagline"],
            "record_kind": "unsolved problem record",
            "id_prefix": "JAH-USPS-",
            "ai_name": "JAH Unsolved Psychology Archivist",
            "local_index": (SHARD_BASE +
                            "/data/unsolved-psychology/index.jsonl.gz"),
            "record_count": 34, "status": "live", "full_records": 34,
            "index": (SHARD_BASE +
                      "/data/unsolved-psychology/index.jsonl.gz"),
            "chunk_pattern": "data/unsolved-psychology/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "unsolved-psychology-signature",
            "name": "The Unsolved Psychology Signature Database",
            "tagline": DBCFG["unsolved-psychology-signature"]["tagline"],
            "record_kind": "unsolved problem record",
            "id_prefix": "JAH-USPSS-",
            "ai_name": "JAH Unsolved Psychology Archivist (Signature)",
            "local_index": (SHARD_BASE +
                            "/data/unsolved-psychology-signature/index.jsonl.gz"),
            "record_count": 34, "status": "live", "full_records": 34,
            "index": (SHARD_BASE +
                      "/data/unsolved-psychology-signature/index.jsonl.gz"),
            "chunk_pattern": ("data/unsolved-psychology-signature/chunks/"
                              "chunk-NNNN.jsonl.gz"),
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("DONE: 2 databases, %d records. Merger: register manifest/api, "
          "restamp counts." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
