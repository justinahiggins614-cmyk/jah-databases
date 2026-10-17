#!/usr/bin/env python3
"""Build the JAH Signature Number Line databases (Manon order #13,
2026-10-17 15:32 EDT).

Pipeline replicates code/component-parts-catalog-build/build.py EXCEPT:
never touches data/manifest.json, api.json, index.html, README.md, or
docs/AI_ACCESS.md, and never commits or pushes - a merger handles those.
Instead this build writes the merger fragment at
~/workspace/hidden_files/missing-builds/fragments/jah-number-line.json.

Verified 2026-10-17 (order #13): RAW SWEEP over the full manifest (2,390
databases): zero 'jah-number-line*' slugs/names; zero 'number line' /
'numberline' hits in any name, slug, or tagline. The one keyword near-hit,
the Natural Language Processing pair (JAH-NLP-PUB / JAH-NLP-SIG), is about
language AI, not the mathematical number line. The paste's rule was applied
by name/purpose/record schema/capabilities: a ladder-ordered archive of
number-line records is a distinct capability - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  jah-number-line               - The JAH Signature Number Line Database
                                  (public-harvest: real, fact-checked
                                  mathematics of the number line)
  jah-number-line-signature     - The JAH Signature Number Line Signature
                                  Database
                                  (his original Signature Number Line
                                  Method; src signature, titles suffixed
                                  " (Signature Edition)", never presented
                                  as authentic public record)

ID prefixes: JAH-NLN- (public) and JAH-NLNS- (signature), verified free in
the manifest id_prefix values and in every shard index file (zero hits;
JAH-NLP-PUB / JAH-NLP-SIG belong to the unrelated Natural Language
Processing databases).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_jah_number_line.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before the fragment
is written.

Never the words "bat belt" anywhere. No website references. No Facebook.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/jah-number-line.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_jah_number_line import ENTRIES, SIG_TAIL
from demos_jah_number_line import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Number Line "
                "Method: the line as a sworn order of values, every "
                "position a value sealed at its post, zero the signet of "
                "the origin, order the covenant of less and greater, the "
                "arrow the oath that the order continues. Clearly labeled "
                "Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked mathematics of the "
                "number line: counting numbers, zero, negatives, integers, "
                "ordering, addition and subtraction as steps, fractions, "
                "decimals, rational numbers, absolute value, intervals, "
                "inequalities, midpoints, multiplication and division as "
                "scaling, square roots, the coordinate axis, estimation, "
                "irrational numbers, the completeness of the reals, "
                "interval arithmetic, the Cartesian plane, measurement, "
                "limits, functions, infinite intervals, and continuity - "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the counting line, zero and the origin, negatives, "
              "integers, ordering, addition, subtraction, halves and "
              "quarters, opposites, the ruler, reading and marking "
              "points) -> Compounded (fractions, decimals, rational "
              "numbers, absolute value, intervals, inequalities, "
              "midpoints, multiplication, division, square roots, the "
              "coordinate axis, benchmarks) -> Advanced (irrationals, "
              "completeness of the reals, interval notation, interval "
              "arithmetic, absolute value inequalities, the Cartesian "
              "plane, measurement, limits, functions, infinite intervals, "
              "continuity).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search counting numbers, zero, negatives, integers, ordering, addition, subtraction, fractions, decimals, absolute value, intervals, inequalities, square roots, irrationals, real numbers, limits, functions...",
        "chat_ph": "Ask about the number line...",
        "archive_blurb": ("Seeded 34 %s number line records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled number line studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the number line - from counting numbers, zero, negatives, and integers through fractions, decimals, absolute value, intervals, and inequalities, to irrationals, the real line, limits, and functions." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "number-line-study", "gen_demo_kind": "number-line-demo",
        "source": source,
    }

CIT_PUB = ("Number line mathematics (standard references: Euclid. Elements. "
           "Book VII; c. 300 BCE; Dedekind R. Stetigkeit und irrationale "
           "Zahlen; 1872; Common Core State Standards for Mathematics; "
           "2010; National Council of Teachers of Mathematics. Principles "
           "to Actions; 2014; ISO 80000-2:2019 mathematical signs and "
           "symbols; Rudin W. Principles of Mathematical Analysis. 3rd ed; "
           "1976; Apostol TM. Calculus, Vol. 1. 2nd ed; 1967; Stewart J. "
           "Calculus. 8th ed; 2016; Devlin K. The Language of Mathematics; "
           "2000).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Number "
                     "Line Method - the line as a sworn order of values, "
                     "every position sealed at its post - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["jah-number-line"] = _cfg(
    "jah-number-line", "The JAH Signature Number Line Database",
    "The number line, taught whole: real, fact-checked mathematics of "
    "counting numbers, zero, negatives, integers, fractions, decimals, "
    "rational and real numbers, absolute value, intervals, inequalities, "
    "square roots, coordinate mapping, limits, and functions - every "
    "record carrying description, how it works, key points, requirements, "
    "standards, citations, and a working demonstration program, taught "
    "progressively along the ladder.",
    "number line record", "JAH-NLN-", "JAH Signature Number Line Archivist",
    "number line archivist - counting numbers, zero, negatives, integers, "
    "fractions, decimals, rational numbers, absolute value, intervals, "
    "inequalities, square roots, coordinate mapping, limits, and functions; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["jah-number-line-signature"] = _cfg(
    "jah-number-line-signature", "The JAH Signature Number Line Signature Database",
    "His original Signature Number Line Method: the line as a sworn order "
    "of values - every position a value sealed at its post, zero the "
    "signet of the origin, order the covenant of less and greater, the "
    "arrow the oath that the order continues. The full ladder from "
    "counting and zero through fractions, absolute value, intervals, and "
    "inequalities, to irrationals, the complete real line, limits, "
    "functions, and continuity, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "number line record", "JAH-NLNS-", "JAH Signature Number Line Archivist (Signature)",
    "number line archivist - Signature editions: his original Signature "
    "Number Line Method, the line as a sworn order of values with every "
    "position sealed at its post, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
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
    for slug in ("jah-number-line", "jah-number-line-signature"):
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
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # Merger fragment (manifest/api.json updates belong to the merger).
    def frag_entry(slug, source):
        c = DBCFG[slug]
        return {
            "slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(built[slug]), "status": "live",
            "full_records": len(built[slug]),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if source == "signature" else "public-harvest",
        }
    fragment = {
        "public": frag_entry("jah-number-line", "public"),
        "signature": frag_entry("jah-number-line-signature", "signature"),
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("records: %d total (%d public + %d signature)" %
          (total, len(built["jah-number-line"]), len(built["jah-number-line-signature"])))
    print("NEXT: merger verifies, then restamp + commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
