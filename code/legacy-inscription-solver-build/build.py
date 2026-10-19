#!/usr/bin/env python3
"""Build the Legacy Inscription Solver databases for JAH Databases
(Manon's 2026-10-17 17:55 order: "Solve legacy inscription database").

Verified 2026-10-17: zero 'legacy-inscription-solver' slugs in manifest;
ID prefixes JAH-LIS- and JAH-LISS- verified free across ALL manifest
id_prefix values AND every record ID in jah-databases-data-1/data (zero
hits). Whole-system dedupe gate: inscription/decipher overlap checked -
impossible-scripts (file utilities), manuscripts-public (document
transcription archive), linguistics (JAH-LIN-) are all distinct scopes.
The 68 titles run through the whole-system dedupe gate before authoring:
zero collisions.

This build creates two NEW databases, 34 ladder-ordered records each:

  legacy-inscription-solver            - The Legacy Inscription Solver
                                         Database (public: 34 real
                                         documented decipherment records -
                                         fact-checked - from the Rosetta
                                         Stone to the still-undeciphered)
  legacy-inscription-solver-signature  - The Legacy Inscription Solver
                                         Signature Database (signature:
                                         the Signature system's proposed
                                         readings for the same 34
                                         inscriptions - ALWAYS labeled
                                         "Signature-generated proposed
                                         reading - not established
                                         scholarship", never presented as
                                         real decipherment)

34 records each, ladder_rank 1-34, tiers foundations -> compounded ->
advanced; shard index written in ladder order.

Pipeline replicates code/unsolved-logic-build/build.py exactly for page
structure: build_page + build_gen_js from numbering-build, sweep pass,
Exhaustive pill + merger button + tab guard carried over from the template.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes. The merger owns those. This script writes only:
  db/legacy-inscription-solver/ + db/legacy-inscription-solver-signature/
    (index.html + gen-*.js)
  jah-databases-data-1/data/legacy-inscription-solver[-signature]/
    (index.jsonl.gz + chunks)
  ~/workspace/hidden_files/missing-builds/fragments/legacy-inscription-solver.json

Demos: every record ships a decipherment walkthrough - a real, runnable,
stdlib-only Python program with sign frequency analysis, anchor check,
step-by-step method/proposal path, adjustable assumptions, and
confirm/refute panels. Machine-executed by this build: each prints real
computed values, asserts tight bounds, and ends with the OK marker.

No website references. No Facebook. Screened content.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/legacy-inscription-solver.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_legacy_inscription_solver import ENTRIES, SIG_LABEL, SIG_TAIL
from demos_legacy_inscription_solver import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature proposed readings - the Signature system "
                "proposed reading for each of the 34 inscriptions, every "
                "one opened with the exact label 'Signature-generated "
                "proposed reading - not established scholarship', laid out "
                "step by step with assumptions, reasoning path, confirming "
                "and refuting evidence, and what it does NOT claim. Clearly "
                "labeled Signature work, never presented as real "
                "decipherment.")
    pub_line = ("Public records - 34 real documented decipherment records, "
                "fact-checked: Egyptian hieroglyphs, Linear B, cuneiform, "
                "Mayan glyphs, Brahmi, Ugaritic, and the methods that "
                "cracked them, plus honest documentation of the "
                "still-undeciphered scripts. Every record carries readings, "
                "translations, the decipherment method, and a pointer to "
                "the Signature edition's proposed reading.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the Rosetta Stone, Egyptian hieroglyphs, Demotic, Linear B, "
              "Behistun, cuneiform, Old Persian, Hittite, Mayan glyphs, "
              "Brahmi, Ugaritic, oracle bone script) -> Compounded (Luwian "
              "hieroglyphs, Etruscan, Meroitic, Carian, Iberian, Linear "
              "Elamite, Epi-Olmec, Zapotec, Khitan, Tangut) -> Advanced "
              "(Linear A, Indus script, Cretan hieroglyphs, Proto-Elamite, "
              "Rongorongo, Phaistos Disc, Byblos syllabary, Cypro-Minoan, "
              "Voynich manuscript, Rohonc Codex, Vinca-Turdas symbols, "
              "Cascajal Block).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record is the full file: problem, background, "
                  "readings, translations, the decipherment method, and a working "
                  "decipherment-walkthrough demonstration program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature proposed readings organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Rosetta Stone, hieroglyphs, Linear B, cuneiform, Mayan glyphs, Brahmi, Ugaritic, Linear A, Indus script, Rongorongo, Phaistos Disc, Voynich...",
        "chat_ph": "Ask about deciphering ancient inscriptions...",
        "archive_blurb": ("Seeded %s inscription-solver records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature proposed-reading" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, script, status, problem, background, "
                   "why_it_matters, readings, translations, decipherment_method, "
                   "signature_solution, description, how_it_works, key_points, "
                   "requirements, standards, citations, src, ladder_rank, "
                   "ladder_tier, demo"),
        "fields": "Deciphered Scripts \u00b7 Partially Deciphered Scripts \u00b7 Undeciphered Scripts - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled inscription-solver studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about deciphering ancient inscriptions - from the Rosetta Stone and Linear B through cuneiform, Mayan glyphs, Brahmi, and Ugaritic, to Linear A, the Indus script, Rongorongo, and the Voynich manuscript." % ai,
        "gen_fields": ["Deciphered Scripts", "Partially Deciphered Scripts",
                       "Undeciphered Scripts"],
        "gen_kind": "inscription-solution-study", "gen_demo_kind": "inscription-solver-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["legacy-inscription-solver"] = _cfg(
    "legacy-inscription-solver", "The Legacy Inscription Solver Database",
    "Solving legacy inscriptions: real documented decipherment knowledge - "
    "Egyptian hieroglyphs, Linear B, cuneiform, Mayan glyphs, Brahmi, "
    "Ugaritic and more - readings, translations, and the methods that "
    "cracked them, fact-checked, taught along the ladder from the great "
    "decipherments to the still-undeciphered.",
    "inscription solution record", "JAH-LIS-", "JAH Legacy Inscription Solver",
    "legacy inscription solver - teaching real documented decipherment "
    "knowledge from the Rosetta Stone through Linear B, cuneiform, Mayan "
    "glyphs, Brahmi, and Ugaritic to the still-undeciphered scripts; "
    "readings and translations fact-checked, methods fully laid out; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, method - using only archive "
    "data from this system",
    "public")
DBCFG["legacy-inscription-solver-signature"] = _cfg(
    "legacy-inscription-solver-signature",
    "The Legacy Inscription Solver Signature Database",
    "The Signature system proposed readings for legacy and undeciphered "
    "inscriptions - Linear A, the Indus script, Rongorongo, Proto-Elamite, "
    "the Phaistos Disc and more - every reading opened with the exact "
    "label Signature-generated proposed reading - not established "
    "scholarship, laid out step by step with assumptions, reasoning, "
    "confirming and refuting evidence, and honest limits. Clearly labeled "
    "Signature work, never presented as real decipherment.",
    "inscription solution record", "JAH-LISS-",
    "JAH Legacy Inscription Solver (Signature)",
    "legacy inscription solver - Signature editions: the Signature system "
    "proposed readings for the 34 inscriptions, each opened with the exact "
    "honesty label Signature-generated proposed reading - not established "
    "scholarship, and honest about what is not claimed; teaches "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles using only archive data from "
    "this system",
    "signature")

base.DBCFG = DBCFG

assert len(ENTRIES) == 34, "need exactly 34 entries"
assert len(DEMOS) == 34, "demo map misses entries"


def _sig_solution_text(e):
    parts = [SIG_LABEL]
    parts.append("Assumptions:")
    parts.extend("  " + a for a in e["assumptions"])
    parts.append("Proposed-reading path:")
    parts.extend("  " + s for s in e["steps"])
    parts.append("What would confirm it:")
    parts.extend("  [+] " + c for c in e["confirm"])
    parts.append("What would refute it:")
    parts.extend("  [-] " + r for r in e["refute"])
    parts.append("What it does NOT claim:")
    parts.extend("  [x] " + n for n in e["not_claims"])
    return "\n".join(parts)


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    refused = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            refused.append(title)
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            signature_solution = _sig_solution_text(e)
            description = (SIG_LABEL + " " + e["problem"] + " " +
                           e["why_it_matters"])
            how = e["background"] + "\n\n" + signature_solution
            key_points = list(e["steps"])
            requirements = list(e["assumptions"])
            standards = [
                SIG_LABEL,
                "Proposed reading only - claims no real decipherment and no scholarly acceptance.",
                "Honesty rule: where the answer is 'we do not know', the record says so.",
            ]
            citations = list(e["citations"]) + [SIG_TAIL]
            src = "signature"
        else:
            signature_solution = (SIG_LABEL + " See the Signature edition (" +
                                  title + " (Signature Edition)) for the full "
                                  "proposed-reading treatment. " + e["sig_pointer"])
            description = e["problem"] + " " + e["why_it_matters"]
            how = (e["background"] + "\n\nDocumented decipherment method: " +
                   e["method"])
            key_points = list(e["readings"])
            requirements = [
                "No prerequisites - each record states its inscription plainly.",
                "Each record is self-contained: problem, background, readings, and method.",
            ]
            standards = [
                "Decipherment status documented as of 2026.",
                "Readings and translations fact-checked against the epigraphic literature.",
                "Undeciphered entries mark all proposals as unproven.",
            ]
            citations = list(e["citations"])
            src = "public-harvest"
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "script": e["script"], "status": e["status"],
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "readings": list(e["readings"]),
            "translations": list(e["translations"]),
            "decipherment_method": e["method"],
            "signature_solution": signature_solution,
            "description": description,
            "how_it_works": how,
            "key_points": key_points,
            "requirements": requirements,
            "standards": standards,
            "citations": citations,
            "src": src,
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        pub_fn, sig_fn = DEMOS[e["key"]]
        demo_fn = sig_fn if sig else pub_fn
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          key_points, "; ".join(requirements), sig)
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Decipherment walkthrough (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    assert ranks == list(range(1, 35)), "ladder ranks must be 1..34 for %s" % slug
    return recs, refused


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
    all_refused = []
    for slug in ("legacy-inscription-solver", "legacy-inscription-solver-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        recs, refused = build_records(slug, source)
        built[slug] = recs
        all_refused.extend(refused)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "script", "status",
                      "problem", "background", "why_it_matters", "readings",
                      "translations", "decipherment_method",
                      "signature_solution", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            assert len(r["background"].split(". ")) >= 3, "background too thin in %s" % r["id"]
            assert len(r["readings"]) >= 3, "readings too thin in %s" % r["id"]
            assert len(r["translations"]) >= 2, "translations too thin in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
                assert SIG_LABEL.lower() in r["signature_solution"].lower(), \
                    "sig label missing in %s" % r["id"]
                assert SIG_LABEL.lower() in r["description"].lower(), \
                    "sig label missing in description %s" % r["id"]
                assert SIG_LABEL.lower() in r["how_it_works"].lower(), \
                    "sig label missing in how_it_works %s" % r["id"]
            else:
                assert r["src"] == "public-harvest"
                assert SIG_LABEL.lower() in r["signature_solution"].lower(), \
                    "sig pointer label missing in %s" % r["id"]
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
        assert "facebook" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # JS hygiene: node --check on extracted inline page scripts + gen-*.js
    for slug in built:
        ddir = os.path.join(REPO, "db", slug)
        page = open(os.path.join(ddir, "index.html"), encoding="utf-8").read()
        scripts = re.findall(r"<script>(.*?)</script>", page, re.S)
        assert scripts, "no inline scripts found in %s" % slug
        for i, body in enumerate(scripts):
            tmp = "/tmp/lis_jscheck_%s_%d.js" % (slug.replace("-", "_"), i)
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(body)
            p = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
            assert p.returncode == 0, "node --check failed page script %d of %s: %s" % (i, slug, p.stderr[:500])
        gp = os.path.join(ddir, "gen-%s.js" % slug)
        p = subprocess.run(["node", "--check", gp], capture_output=True, text=True)
        assert p.returncode == 0, "node --check failed %s: %s" % (gp, p.stderr[:500])
        print("js hygiene: %s page scripts + gen js node-clean" % slug, flush=True)

    # gen-js demos: execute generate() in node, validate, and run each demo program
    for slug in built:
        gp = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
        node_src = (
            "var gen=require(%s);\n"
            "var out=[];\n"
            "for(var s=1;s<=3;s++){var r=gen.generate(s,{});"
            "var v=gen.validate(r);"
            "if(!v.ok)throw new Error('gen validate failed seed '+s);\n"
            "out.push(r.demo.program);}\n"
            "console.log(JSON.stringify(out));\n" % json.dumps(gp))
        p = subprocess.run(["node", "-e", node_src], capture_output=True, text=True)
        assert p.returncode == 0, "gen-js execute failed %s: %s" % (slug, p.stderr[:500])
        programs = json.loads(p.stdout)
        assert len(programs) == 3, "gen-js produced no demos for %s" % slug
        for prog in programs:
            q = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=60)
            assert q.returncode == 0, "gen demo failed %s: %s" % (slug, q.stderr[-400:])
        print("gen-js demos: %s 3/3 executed OK" % slug, flush=True)

    # Fragment for the merger (merger owns manifest.json / api.json / restamp).
    def frag(slug, source):
        cfg = DBCFG[slug]
        url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        return {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": url,
            "record_count": len(built[slug]),
            "status": "live",
            "full_records": len(built[slug]),
            "index": url,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": source,
        }
    fragment = {
        "public": frag("legacy-inscription-solver", "public-harvest"),
        "signature": frag("legacy-inscription-solver-signature", "signature"),
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("gate refusals during build: %d" % len(all_refused), flush=True)
    for t in all_refused:
        print("  refused: %s" % t, flush=True)
    print("DONE: %d records across 2 databases; merger verifies live." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
