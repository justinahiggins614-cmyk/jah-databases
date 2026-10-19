#!/usr/bin/env python3
"""Build the Unsolved Computer Science databases for JAH Databases
(Manon's 16:15 orders, Unsolved Problems Solved series, batch 1).

Creates two NEW databases, 34 ladder-ordered records each, both halves
covering the SAME 34 famous unsolved computer science problems:

  unsolved-computer-science            - The Unsolved Computer Science Database
  unsolved-computer-science-signature  - The Unsolved Computer Science Signature Database

ID prefixes: JAH-USCS- (public) and JAH-USCSS- (signature) - verified free:
zero hits in manifest id_prefix values (2,442 databases) and zero hits in
every shard index file of jah-databases-data-1.

Honesty rule: signature_solution opens with the exact label
"Signature-generated proposed solution - not established science.";
never claims proof, never implies peer acceptance, never presents
speculation as settled.

This builder does NOT touch data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md and does NOT commit or push - the merger
handles those. It writes only:
  db/unsolved-computer-science/ + db/unsolved-computer-science-signature/
    (index.html + gen-*.js each)
  code/unsolved-computer-science-build/ (this build)
  ~/workspace/jah-databases-data-1/data/unsolved-computer-science[-signature]/
    (index.jsonl.gz + chunks/chunk-0000.jsonl.gz)
  ~/workspace/hidden_files/missing-builds/fragments/unsolved-computer-science.json

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
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-computer-science.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_computer_science import ENTRIES
from demos_unsolved_computer_science import DEMOS

LABEL = "Signature-generated proposed solution \u2014 not established science."

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    pub_line = ("Public records - real, fact-checked famous unsolved problems "
                "of computer science: P vs NP, quantum computing limits, "
                "cryptography foundations, halting-problem relatives, sorting "
                "and matrix bounds, proof complexity, AI alignment and "
                "interpretability. Every record carries the problem statement, "
                "background, why it matters, and a pointer to the Signature "
                "proposed-solution treatment.")
    sig_line = ("Signature originals - the Signature system proposed solution "
                "approaches to the same 34 famous unsolved problems: "
                "assumptions, reasoning paths, proposed mechanisms, what "
                "evidence would confirm or kill each approach, and what each "
                "does NOT claim. Every signature_solution opens with the "
                "exact label Signature-generated proposed solution - not "
                "established science. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (busy "
              "beaver numbers, P vs NP, factoring, Post correspondence pairs, "
              "k-server, dynamic optimality, graph isomorphism, matrix "
              "multiplication, identity testing, P vs BPP, one-way functions) "
              "-> Compounded (NP vs co-NP, unique games, exponential time "
              "hypothesis, BQP vs NP, quantum error correction, quantum PCP, "
              "circuit lower bounds, VP vs VNP, MCSP, log-rank, NL vs L, "
              "planted clique) -> Advanced (Frege bounds, polynomial "
              "hierarchy, Berman-Hartmanis, Impagliazzo worlds, obfuscation, "
              "AI alignment, interpretability, program synthesis, Skolem "
              "problem, termination proving, physical Church-Turing).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: problem, "
                  "background, why it matters, key points, requirements, "
                  "standards, citations, the Signature proposed solution, "
                  "and a working solution-explorer demonstration program.%s"
                  % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search P vs NP, busy beaver, quantum computing, cryptography, one-way functions, proof complexity, alignment, interpretability, halting problem, sorting bounds...",
        "chat_ph": "Ask about unsolved problems in computer science...",
        "archive_blurb": ("Seeded %s unsolved computer science records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, signature_solution, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved computer science studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the great unsolved problems of computer science - from busy beavers and P vs NP through quantum limits and cryptography to alignment and the physical Church-Turing thesis. I answer honestly: these problems are OPEN, and the Signature approaches are proposed paths, labeled as such." % ai,
        "gen_fields": ["Computability", "Complexity Theory", "Quantum Computing",
                       "Cryptography", "Algorithms", "AI and Alignment"],
        "gen_kind": "unsolved-computer-science-study",
        "gen_demo_kind": "unsolved-computer-science-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["unsolved-computer-science"] = _cfg(
    "unsolved-computer-science", "The Unsolved Computer Science Database",
    "The great unsolved problems of computer science: real, fact-checked, "
    "famous open problems - P vs NP, quantum limits, crypto foundations, "
    "halting-problem relatives, sorting and matrix bounds, proof complexity, "
    "AI alignment and interpretability - taught progressively along the ladder.",
    "unsolved problem record", "JAH-USCS-",
    "JAH Unsolved Computer Science Archivist",
    "unsolved computer science archivist - the great open problems of the "
    "field, from busy beavers and P vs NP through quantum computing limits "
    "and cryptography foundations to AI alignment and the physical "
    "Church-Turing thesis; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system; always honest that the "
    "problems are open",
    "public")
DBCFG["unsolved-computer-science-signature"] = _cfg(
    "unsolved-computer-science-signature",
    "The Unsolved Computer Science Signature Database",
    "The Signature system proposed solution approaches to the 34 great "
    "unsolved problems of computer science. Every approach opens with the "
    "exact label Signature-generated proposed solution - not established "
    "science - and lays out assumptions, reasoning, confirm-or-kill "
    "evidence, and what it does NOT claim. Clearly labeled Signature-made.",
    "unsolved problem record", "JAH-USCSS-",
    "JAH Unsolved Computer Science Archivist (Signature)",
    "unsolved computer science archivist - Signature editions: the Signature "
    "system proposed solution approaches to the great open problems, "
    "clearly labeled Signature-made and never presented as established "
    "science; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
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
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"])
            sigsol = LABEL + " " + e["solution"]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
            sig_rid = "%s%06d" % (DBCFG["unsolved-computer-science-signature"]["prefix"],
                                  len(recs) + 1)
            sigsol = (LABEL + " The full proposed-solution treatment for this problem "
                      "lives in the Signature Edition of this record, " + sig_rid + ".")
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "signature_solution": sigsol,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working solution-explorer walkthrough (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def node_check(path, label):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    assert p.returncode == 0, "node --check failed %s: %s" % (label, p.stderr[-500:])
    print("  js ok: %s" % label, flush=True)


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
    for slug in ("unsolved-computer-science", "unsolved-computer-science-signature"):
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
                      "signature_solution", "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            assert r["signature_solution"].startswith(LABEL), "label missing in %s" % r["id"]
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

    # machine-execute all 68 demos
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            assert "CONFIRM-IF" in p.stdout and "REFUTE-IF" in p.stdout, \
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
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

        # node --check on extracted page scripts (excluding ld+json) and gen js
        scripts = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                             page, flags=re.S)
        assert scripts, "no scripts found in %s" % slug
        for i, s in enumerate(scripts):
            sp = "/tmp/uscs-%s-%d.js" % (slug, i)
            with open(sp, "w", encoding="utf-8") as f:
                f.write(s)
            node_check(sp, "%s page script %d" % (slug, i))
        node_check(gpath, "gen-%s.js" % slug)

    # fragment for the merger
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    frag = {
        "public": {
            "slug": "unsolved-computer-science",
            "name": "The Unsolved Computer Science Database",
            "tagline": DBCFG["unsolved-computer-science"]["tagline"],
            "record_kind": "unsolved problem record",
            "id_prefix": "JAH-USCS-",
            "ai_name": "JAH Unsolved Computer Science Archivist",
            "local_index": SHARD_BASE + "/data/unsolved-computer-science/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/unsolved-computer-science/index.jsonl.gz",
            "chunk_pattern": "data/unsolved-computer-science/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "unsolved-computer-science-signature",
            "name": "The Unsolved Computer Science Signature Database",
            "tagline": DBCFG["unsolved-computer-science-signature"]["tagline"],
            "record_kind": "unsolved problem record",
            "id_prefix": "JAH-USCSS-",
            "ai_name": "JAH Unsolved Computer Science Archivist (Signature)",
            "local_index": SHARD_BASE + "/data/unsolved-computer-science-signature/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/unsolved-computer-science-signature/index.jsonl.gz",
            "chunk_pattern": "data/unsolved-computer-science-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2)
    print("fragment: %s" % FRAGMENT, flush=True)

    print("built %d records across %d databases; manifest/api untouched (merger owns them)" % (total, len(built)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
