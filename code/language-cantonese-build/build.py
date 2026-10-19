#!/usr/bin/env python3
"""Build the Cantonese Language databases for JAH Databases
(language orders, roster rank 15).

Verified 2026-10-17: RAW SWEEP over the full manifest PLUS every shard
index title in jah-databases-data-1 (830 index files) for the slug
'language-cantonese', the name 'Cantonese Language Database', and the id
prefixes JAH-LYUE- / JAH-LYUES-: zero hits, all free. The 68 planned
titles (34 public + 34 Signature Edition) were run through
code/dedupe_gate.py against the WHOLE system before authoring: zero
refusals, zero collisions.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-cantonese            - The Cantonese Language Database
                                   (public-harvest: real, fact-checked
                                   Cantonese linguistics - every record
                                   carrying Chinese characters, Jyutping
                                   romanization, and English translation
                                   with example sentences, taught
                                   progressively along the teaching ladder
                                   from overview to mastery review; standard
                                   references Matthews and Yip Cantonese: A
                                   Comprehensive Grammar 2nd ed. 2011;
                                   Bauer and Benedict Modern Cantonese
                                   Phonology 1997; the Linguistic Society of
                                   Hong Kong Jyutping scheme 1993; and
                                   Ethnologue 28th ed. 2025)
  language-cantonese-signature  - The Cantonese Language Signature Database
                                   (his original Signature Word Method:
                                   every word a signed instrument of
                                   meaning, grammar the covenant binding
                                   words into truth, the learner's tongue
                                   the seal; src signature, titles suffixed
                                   " (Signature Edition)", clearly labeled
                                   Signature-made, never presented as
                                   authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LYUE- (public) and JAH-LYUES- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits
across all 830 index files).

Linguistic cores: all hand-authored 2026-10-17, machine-verified by the
demos (see demos_language_cantonese.py): tone drills, Jyutping syllable
inventory checks, number-to-Cantonese converters, aspect-particle quizzes,
question-word classifiers, register sorters, vocabulary and idiom quizzes,
and conversation analytics. Every demo prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker; the build machine-executes all 68 demos.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md and never commits or pushes.
It writes only: db/language-cantonese/ + db/language-cantonese-signature/
(index.html + gen-*.js), the jah-databases-data-1 shards, and the code
files. A merger handles manifest/api/counts.

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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_cantonese import ENTRIES, SIG_TAIL
from demos_language_cantonese import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Word Method: "
                "every word a signed instrument of meaning, grammar the "
                "covenant that binds words into truth, and the learner's "
                "tongue the seal. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Cantonese linguistics: "
                "the 粵語 language of Hong Kong, Macao, Guangdong, and the "
                "worldwide Cantonese diaspora - every record carrying "
                "Chinese characters, Jyutping romanization, and English "
                "translation with example sentences, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation and tones, "
              "core nouns, core verbs, adjectives and adverbs, pronouns, "
              "numbers and time, greetings and everyday phrases, grammar "
              "essentials) -> Compounded (home and family, food and cooking, "
              "travel and directions, work and school, health and body, "
              "emotions and feelings, nature and weather, shopping and "
              "money, friendship and social life, technology and "
              "communication, verb aspects in sentences) -> Advanced "
              "(questions and answers, commands and requests, descriptions, "
              "three graded stories, idioms and proverbs, formal and polite "
              "registers, compound and complex sentences, three "
              "conversations, mastery review and full reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Cantonese tones, Jyutping, nouns, verbs, adjectives, pronouns, numbers, greetings, grammar, idioms, proverbs, conversations...",
        "chat_ph": "Ask about Cantonese...",
        "archive_blurb": ("Seeded %s Cantonese language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Cantonese language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Cantonese - from the six tones and Jyutping through nouns, verbs, adjectives, pronouns, numbers, greetings, and grammar essentials, through home, food, travel, work, health, emotions, nature, shopping, social life, technology, and verb aspects, to questions, commands, descriptions, stories, idioms, registers, complex sentences, conversations, and the full mastery review." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "language-lesson", "gen_demo_kind": "language-demo",
        "source": source,
    }

CITATION = ("Cantonese linguistics (standard references: Matthews S, Yip V. "
            "Cantonese: A Comprehensive Grammar. 2nd ed. Routledge; 2011; "
            "Bauer RS, Benedict PK. Modern Cantonese Phonology. Mouton de "
            "Gruyter; 1997; Linguistic Society of Hong Kong. The Jyutping "
            "Scheme; 1993; Eberhard DM et al., eds. Ethnologue: Languages "
            "of the World. 28th ed. SIL International; 2025).")

DBCFG = {}
DBCFG["language-cantonese"] = _cfg(
    "language-cantonese", "The Cantonese Language Database",
    "Learn Cantonese: real, fact-checked 粵語 linguistics - every record "
    "carrying Chinese characters, Jyutping romanization, and English "
    "translation with example sentences, taught progressively along the "
    "ladder from tones and sounds through words and grammar to stories, "
    "idioms, and conversations.",
    "language learning record", "JAH-LYUE-", "JAH Cantonese Language Tutor",
    "cantonese language tutor - teaching Cantonese from the six tones and "
    "Jyutping through nouns, verbs, adjectives, pronouns, numbers, "
    "greetings, and grammar essentials, through themed sentence sets and "
    "verb aspects, to questions, commands, descriptions, stories, idioms, "
    "registers, complex sentences, conversations, and mastery review; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, how-to - using only archive data from "
    "this system",
    CITATION, "public")
DBCFG["language-cantonese-signature"] = _cfg(
    "language-cantonese-signature", "The Cantonese Language Signature Database",
    "His original Signature Word Method applied to Cantonese: every word a "
    "signed instrument of meaning, grammar the covenant binding words into "
    "truth, the learners tongue the seal. The full ladder from tones and "
    "Jyutping through words and grammar to stories, idioms, and "
    "conversations, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "language learning record", "JAH-LYUES-", "JAH Cantonese Language Tutor (Signature)",
    "cantonese language tutor - Signature editions: his original Signature "
    "Word Method, every word a signed instrument of meaning and grammar the "
    "covenant binding words into truth, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively along "
    "the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, history, "
    "how-to - using only archive data from this system",
    CITATION + (" Signature editions are his original Signature Word Method "
                "- every word a signed instrument of meaning - clearly "
                "labeled Signature-made."), "signature")

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
    for slug in ("language-cantonese", "language-cantonese-signature"):
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

    # CONCURRENCY: manifest.json / api.json / counts are the merger's job.
    # This builder stops here: shards + pages + gen JS are written.
    print("manifest + api.json: SKIPPED by builder (merger handles via fragment).")
    print("fragment: write ~/workspace/hidden_files/missing-builds/fragments/language-cantonese.json")
    print("built %d databases, %d records total - ready for merger" % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
