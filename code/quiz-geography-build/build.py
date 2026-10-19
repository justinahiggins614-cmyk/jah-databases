#!/usr/bin/env python3
"""Build the Geography Quiz databases for JAH Databases
(Manon 16:15 orders 2026-10-17: test then quiz databases, answers at bottom).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,447 databases):
zero 'quiz-geography' slugs; zero 'geography quiz' names. All 68 titles
(34 public + 34 signature) gate-checked against the whole-system dedupe
exact index before authoring: zero collisions, zero refusals. ID prefixes
JAH-QZGE- / JAH-QZGES- verified free in manifest id_prefix values and in
every shard index file.

Two NEW databases, 34 ladder-ordered records each. Every record is one
complete ten-question geography quiz with the full answer key printed AT
THE BOTTOM of the record (his explicit requirement):

  quiz-geography            - The Geography Quiz Database
                              (public-harvest: real, fact-checked geography
                              quiz questions - continents, oceans, capitals,
                              mountains, rivers, deserts, islands, lakes,
                              volcanoes, climate, maps, time zones, borders,
                              landmarks)
  quiz-geography-signature  - The Geography Quiz Signature Database
                              (his original Signature Quiz Method: every
                              quiz a proving of the lands, every question a
                              landmark on the trail, every answer a sealed
                              stamp, the answer key the unsealing at the
                              bottom; src signature, titles suffixed
                              " (Signature Edition)", never presented as
                              authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical cores: every demo is a real quiz runner - it loads the same ten
questions and answers the record carries, simulates a scored run, asserts
the exact score, prints the answer key, and ends with the OK marker.
Demos and record text are generated from the same qa lists, so entry text
and demo outputs cannot drift apart. The build machine-executes all 68
demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. It only writes: db/quiz-geography[-signature]/
(index.html + gen-*.js), the shard data dir, and the merger fragment.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/quiz-geography.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_quiz_geography import ENTRIES, SIG_TAIL
from demos_quiz_geography import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Quiz Method: "
                "every quiz a proving of the lands, every question a "
                "landmark on the trail, every answer a sealed stamp, and the "
                "answer key the unsealing at the bottom. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked geography quiz questions: "
                "continents and oceans, world capitals, maps and compass "
                "directions, mountains and ranges, great rivers, deserts and "
                "rainforests, islands, lakes, volcanoes and earthquakes, "
                "climate zones, latitude longitude and time zones, polar "
                "regions, landmarks, rivers of the Americas Africa Asia and "
                "Europe, ocean currents, caves and canyons, borders and "
                "enclaves, world records, cities and population, map "
                "projections, plate tectonics, waterfalls, Central Asia, "
                "island nations, and the grand challenge - every record one "
                "complete ten-question quiz with the answers at the bottom, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(continents and oceans, world capitals, maps and compass "
              "directions, mountains, great rivers, deserts and rainforests, "
              "islands, lakes, US states, Europe, Asia) -> Compounded "
              "(Africa, South America, volcanoes and earthquakes, climate "
              "zones, latitude longitude and time zones, polar regions, "
              "landmarks, rivers of the Americas, rivers of Africa and Asia, "
              "ocean currents, caves and canyons) -> Advanced (borders and "
              "enclaves, highest deepest longest, cities and population, "
              "European rivers, map projections, plate tectonics, waterfalls, "
              "Central Asia and the Caucasus, Middle East, island nations, "
              "border trivia, the grand challenge).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how the quiz works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search continents, oceans, capitals, mountains, rivers, deserts, islands, lakes, volcanoes, climate, maps, time zones, borders, landmarks, quizzes...",
        "chat_ph": "Ask about geography quizzes...",
        "archive_blurb": ("Seeded %s geography quiz records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled geography quiz studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about geography quizzes - continents, oceans, capitals, mountains, rivers, deserts, islands, lakes, volcanoes, climate, maps, time zones, borders, and landmarks, from easy starters to the grand challenge." % ai,
        "gen_fields": ["Climate and Earth", "Countries and Capitals", "Landforms and Mountains",
                       "Maps and Navigation", "Places and Records", "Rivers and Water"],
        "gen_kind": "geography-quiz", "gen_demo_kind": "geography-quiz-demo",
        "source": source,
    }

CIT_PUB = ("Geography quiz questions (standard references: Central "
           "Intelligence Agency. The World Factbook; updated 2026; National "
           "Geographic Society. National Geographic Atlas of the World. 11th "
           "ed; 2019; Encyclopaedia Britannica geography reference articles; "
           "U.S. Geological Survey geographic names and earthquake hazards "
           "data; United Nations Statistics Division demographic and "
           "geographic data; Guinness World Records natural world records; "
           "National Oceanic and Atmospheric Administration ocean and "
           "climate data).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Quiz "
                     "Method - every quiz a proving of the lands, every "
                     "question a landmark on the trail, every answer a sealed "
                     "stamp, the answer key the unsealing at the bottom - "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["quiz-geography"] = _cfg(
    "quiz-geography", "The Geography Quiz Database",
    "Test yourself with complete geography quizzes: ten fact-checked questions on countries, "
    "capitals, landforms, rivers, and maps in every record, with the full answer key at the "
    "bottom. Taught along the ladder from easy starters to the grand challenge.",
    "quiz record", "JAH-QZGE-", "JAH Geography Quizmaster",
    "geography quizmaster - running complete ten-question geography quizzes with the answers "
    "at the bottom, from foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, math, how-to - using only archive "
    "data from this system",
    CIT_PUB, "public")
DBCFG["quiz-geography-signature"] = _cfg(
    "quiz-geography-signature", "The Geography Quiz Signature Database",
    "His original Signature Quiz Method: every quiz a proving of the lands, every question a "
    "landmark on the trail, every answer a sealed stamp, and the answer key the unsealing at "
    "the bottom. The full ladder from continents and capitals through rivers, mountains, "
    "climate, and borders to the grand challenge, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "quiz record", "JAH-QZGES-", "JAH Geography Quizmaster (Signature)",
    "geography quizmaster - Signature editions: his original Signature Quiz Method, every "
    "quiz a proving of the lands and every answer a sealed stamp, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches progressively "
    "along the ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def render_quiz(e):
    lines = []
    lines.append("HOW THIS QUIZ WORKS")
    lines.append("Read each question and write down your answer before moving on. "
                 "Each correct answer is worth ten points, and a perfect round is one hundred points. "
                 "Do not peek at the bottom of the record until you have answered all ten questions.")
    lines.append("")
    lines.append("QUESTIONS")
    for i, (q, a) in enumerate(e["qa"], start=1):
        lines.append("%d. %s" % (i, q))
    lines.append("")
    lines.append("ANSWERS - CHECK YOUR WORK AT THE BOTTOM")
    lines.append("The full answer key is below. Count ten points for every match.")
    for i, (q, a) in enumerate(e["qa"], start=1):
        lines.append("%d. %s" % (i, a))
    return "\n".join(lines)


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
            how = e["sig_lens"] + " " + render_quiz(e)
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = render_quiz(e)
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
                          e["key_points"], "; ".join(e["requirements"]), e["qa"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python): a quiz runner that scores a simulated run and reveals the answer key."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    frag = {
        "public": {
            "slug": "quiz-geography",
            "name": "The Geography Quiz Database",
            "tagline": DBCFG["quiz-geography"]["tagline"],
            "record_kind": "quiz record",
            "id_prefix": "JAH-QZGE-",
            "ai_name": "JAH Geography Quizmaster",
            "local_index": SHARD_BASE + "/data/quiz-geography/index.jsonl.gz",
            "record_count": len(built["quiz-geography"]),
            "status": "live",
            "full_records": len(built["quiz-geography"]),
            "index": SHARD_BASE + "/data/quiz-geography/index.jsonl.gz",
            "chunk_pattern": "data/quiz-geography/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "quiz-geography-signature",
            "name": "The Geography Quiz Signature Database",
            "tagline": DBCFG["quiz-geography-signature"]["tagline"],
            "record_kind": "quiz record",
            "id_prefix": "JAH-QZGES-",
            "ai_name": "JAH Geography Quizmaster (Signature)",
            "local_index": SHARD_BASE + "/data/quiz-geography-signature/index.jsonl.gz",
            "record_count": len(built["quiz-geography-signature"]),
            "status": "live",
            "full_records": len(built["quiz-geography-signature"]),
            "index": SHARD_BASE + "/data/quiz-geography-signature/index.jsonl.gz",
            "chunk_pattern": "data/quiz-geography-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, ensure_ascii=False, indent=2)
    print("fragment: %s" % FRAGMENT, flush=True)


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
    for slug in ("quiz-geography", "quiz-geography-signature"):
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
            assert "ANSWERS - CHECK YOUR WORK AT THE BOTTOM" in r["how_it_works"], \
                "answer key missing in %s" % r["id"]
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

    write_fragment(built)
    print("NOTE: manifest.json / api.json / commit / push are the merger's job - not touched.")
    print("NEXT: merger runs python3 code/restamp_counts.py, then commits + pushes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
