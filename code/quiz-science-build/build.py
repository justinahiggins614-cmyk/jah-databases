#!/usr/bin/env python3
"""Build the Science Quiz databases for JAH Databases
(Manon's 2026-10-17 16:15 order: "Test then quiz databases with answers at
bottom").

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases)
plus every shard index title in jah-databases-data-1 plus the main-repo
data dir: zero quiz databases exist at all - no 'quiz*' slugs, no quiz
titles. Slug "quiz-science" is free. BUILD NEW is the verdict.

Two NEW databases, 34 ladder-ordered records each:

  quiz-science            - The Science Quiz Database
                            (public-harvest: real, fact-checked science
                            quizzes - physics, chemistry, biology, earth
                            science, astronomy; EVERY record is one complete
                            10-question quiz with the ANSWER KEY AT THE
                            BOTTOM of the record, per his explicit
                            requirement)
  quiz-science-signature  - The Science Quiz Signature Database
                            (his original Signature Quiz Method: every quiz
                            a proving ground of knowledge, the question a
                            challenge of the mind, the answer key at the
                            bottom the sealed judgment, mastery the covenant
                            stamp; src signature, titles suffixed
                            " (Signature Edition)", never presented as
                            authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-QZSC- (public) and JAH-QZSCS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits) on
2026-10-17.

Numerical cores: the demos are quiz runners with answer reveal and a
simulated graded attempt (see demos_quiz_science.py). Every demo prints its
real computed values, asserts tight bounds (never float exact-equality),
and ends with the OK marker; the build machine-executes all 68 demos and
cross-checks every answer against the demo output before writing.

Never the words "bat belt" anywhere. No website references. No Facebook.

NOTE: this build NEVER touches data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md, and never commits or pushes - a merger
handles those.
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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_quiz_science import ENTRIES, SIG_TAIL
from demos_quiz_science import DEMOS

# ---------------------------------------------------------------- DB config

SIG_LENS = {
    "Physics": ("Signature lens: physics is the proving ground of the moving "
                "world - every push a vow, every orbit a covenant kept. This "
                "quiz tests the same real physics through the Signature eye: "
                "measure truly, answer boldly, and let the answer key at the "
                "bottom seal the judgment."),
    "Chemistry": ("Signature lens: chemistry is the covenant of "
                  "transformation - matter bound by oath, changed by trial. "
                  "This quiz tests the same real chemistry through the "
                  "Signature eye: know the elements by name, follow the "
                  "changes honestly, and let the answer key at the bottom "
                  "seal the judgment."),
    "Biology": ("Signature lens: biology is the covenant of living things - "
                "every cell a promise kept, every ecosystem a trust. This "
                "quiz tests the same real biology through the Signature eye: "
                "observe truly, answer boldly, and let the answer key at the "
                "bottom seal the judgment."),
    "Earth Science": ("Signature lens: earth science is the covenant of the "
                      "world itself - rocks remembering, waters cycling, "
                      "skies turning on oath. This quiz tests the same real "
                      "earth science through the Signature eye: read the "
                      "planet honestly, and let the answer key at the bottom "
                      "seal the judgment."),
    "Astronomy": ("Signature lens: astronomy is the covenant of the cosmos - "
                  "stars keeping their ancient vows across the dark. This "
                  "quiz tests the same real astronomy through the Signature "
                  "eye: look up truly, answer boldly, and let the answer "
                  "key at the bottom seal the judgment."),
}


def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature Quiz Method: "
                "every quiz a proving ground of knowledge, the question a "
                "challenge of the mind, the answer key at the bottom the "
                "sealed judgment, and mastery the covenant stamp. Clearly "
                "labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked science quizzes across "
                "physics, chemistry, biology, earth science, and astronomy. "
                "Every record is one complete 10-question quiz with the "
                "answer key at the bottom of the record - answer all ten "
                "before checking - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(motion, matter, living things, day and night, forces, "
              "mixtures, plants, the solar system, simple machines, acids "
              "and bases, bones and muscles, rocks, light, the periodic "
              "table, ecosystems, weather) -> Compounded (Newton's first "
              "law, chemical reactions, cells, the Moon, energy, atoms, "
              "photosynthesis and respiration, electricity, bonding, plate "
              "tectonics) -> Advanced (waves, DNA, stars, gravity and "
              "Kepler, stoichiometry, climate systems, relativity, "
              "cosmology).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: the quiz, "
                  "how it works, key points, requirements, standards, "
                  "citations, and a working quiz-runner demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search motion, matter, magnets, planets, simple machines, acids, cells, energy, atoms, circuits, bonding, earthquakes, DNA, stars, gravity, relativity, cosmology...",
        "chat_ph": "Ask about science quizzes...",
        "archive_blurb": ("Seeded %s science quiz records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Physics \u00b7 Chemistry \u00b7 Biology \u00b7 Earth Science \u00b7 Astronomy - each field opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled science quiz studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about science quizzes - physics, chemistry, biology, earth science, and astronomy, from first steps in motion and matter through energy, atoms, cells, and plates, to waves, DNA, stars, relativity, and cosmology. Every quiz keeps its answer key at the bottom." % ai,
        "gen_fields": ["Physics", "Chemistry", "Biology", "Earth Science", "Astronomy"],
        "gen_kind": "science-quiz-study", "gen_demo_kind": "science-quiz-demo",
        "source": source,
    }

CIT_PUB = ("Science quiz content (standard references: OpenStax College "
           "Physics 2e, Chemistry 2e, Concepts of Biology, Astronomy 2e, Rice "
           "University; Tarbuck EJ et al. Earth Science. 15th ed. Pearson; "
           "2018; National Research Council. A Framework for K-12 Science "
           "Education. National Academies Press; 2012; Next Generation "
           "Science Standards, physical/life/earth and space science core "
           "ideas).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Quiz "
                     "Method - every quiz a proving ground of knowledge, "
                     "the question a challenge of the mind, the answer key "
                     "at the bottom the sealed judgment, mastery the "
                     "covenant stamp - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["quiz-science"] = _cfg(
    "quiz-science", "The Science Quiz Database",
    "Test yourself in real science: complete 10-question quizzes across "
    "physics, chemistry, biology, earth science, and astronomy - every quiz "
    "with the answer key at the bottom of the record, so you answer before "
    "you check. Fact-checked questions, ladder-ordered from first steps to "
    "relativity and cosmology.",
    "quiz record", "JAH-QZSC-", "JAH Science Quizmaster",
    "science quizmaster - running complete 10-question science quizzes "
    "across physics, chemistry, biology, earth science, and astronomy; the "
    "answer key always sits at the bottom of the record; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this "
    "system",
    "public")
DBCFG["quiz-science-signature"] = _cfg(
    "quiz-science-signature", "The Science Quiz Signature Database",
    "His original Signature Quiz Method: every quiz a proving ground of "
    "knowledge, the question a challenge of the mind, the answer key at the "
    "bottom the sealed judgment, mastery the covenant stamp. The full ladder "
    "from motion and matter through energy, atoms, cells, and plates, to "
    "waves, DNA, stars, relativity, and cosmology, reframed through the "
    "Signature lens. Clearly labeled Signature-made, never presented as "
    "authentic public record.",
    "quiz record", "JAH-QZSCS-", "JAH Science Quizmaster (Signature)",
    "science quizmaster - Signature editions: his original Signature Quiz "
    "Method, every quiz a proving ground of knowledge and the answer key at "
    "the bottom the sealed judgment, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    refusals = 0
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            refusals += 1
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        qs = e["questions"]
        assert len(qs) == 10, "quiz %s does not have 10 questions" % name
        qblock = "\n".join("%d. %s" % (i + 1, q) for i, (q, a) in enumerate(qs))
        ablock = "\n".join("%d. %s" % (i + 1, a) for i, (q, a) in enumerate(qs))
        how = ("Read each question and write your answers before looking "
               "below. Answer all 10 questions, then check them against the "
               "answer key at the bottom of this record.\n\n"
               "THE QUESTIONS\n%s\n\nANSWER KEY - AT THE BOTTOM\n%s"
               % (qblock, ablock))
        lens = SIG_LENS[e["group"]]
        if sig:
            description = ("Signature original interpretation. " + lens + " "
                           + e["description"])
            how = lens + " " + how
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
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
                       "note": "Working quiz-runner demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    print("dedupe gate: %d titles checked, %d refusals for %s"
          % (len(ordered), refusals, slug), flush=True)
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
    for slug in ("quiz-science", "quiz-science-signature"):
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
            assert "ANSWER KEY" in r["how_it_works"], "answer key missing in %s" % r["id"]
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
            answers = [line.split(". ", 1)[1] for line in r["how_it_works"].split("ANSWER KEY - AT THE BOTTOM", 1)[1].splitlines()
                       if line and line[0].isdigit()]
            assert len(answers) == 10, "answer key block broken in %s" % r["id"]
            # cross-check: every answer appears in the demo output
            for a in answers:
                assert a in p.stdout, "answer missing from demo output %s: %s" % (r["id"], a)
    print("demo execution + answer cross-check: all %d demos ran OK" % total, flush=True)

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

    print("pages + shards done for %d databases, %d records. "
          "manifest/api/index/README NOT touched - merger handles them." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
