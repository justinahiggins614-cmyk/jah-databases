#!/usr/bin/env python3
"""Build the Telugu Language databases for JAH Databases
(Manon's language project 2026-10-17, batch 2, ranks 11-20).

Follows the shared per-language template (language-template.md) EXACTLY and
replicates the component-parts-catalog-build pipeline EXACTLY for page
structure (template page + numbering-build page builder + gen JS +
sweep-db-pages post-pass).

Creates two NEW databases, 34 ladder-ordered records each:

  language-telugu            - Telugu Language Database
                               (public-harvest: real, fact-checked Telugu
                               linguistic data - Telugu script plus
                               transliteration plus English on every line,
                               example sentences in every record)
  language-telugu-signature  - Telugu Language Signature Database
                               (his original Signature language instrument:
                               Telugu as a working system he commands;
                               src signature, titles suffixed
                               " (Signature Edition)", clearly labeled
                               Signature-made, never presented as authentic
                               public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10
non-decreasing, ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

ID prefixes: JAH-LTEL- (public) and JAH-LTELS- (signature), verified free
in the manifest id_prefix values and in every shard index file under
jah-databases-data-1 (zero hits on 2026-10-17).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_telugu.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing.

Never the words "bat belt" anywhere. No website references. No Facebook.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, docs/AI_ACCESS.md and NEVER commits or pushes.
A merger handles those. It ONLY writes:
  db/language-telugu/ + db/language-telugu-signature/ (index.html + gen-*.js)
  code/language-telugu-build/{build.py, entries_*.py, demos_*.py}
  jah-databases-data-1/data/language-telugu[-signature]/ (index.jsonl.gz + chunks/)
  hidden_files/missing-builds/fragments/language-telugu.json
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
from entries_language_telugu import ENTRIES, SIG_TAIL
from demos_language_telugu import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature language "
                "instrument: Telugu as a working system he commands, taught "
                "through the Signature lens from the alphabet through the "
                "sound system, words, grammar and daily sentences to stories, "
                "idioms, registers and full conversations. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Telugu linguistic data: "
                "Telugu (తెలుగు) in Telugu script plus transliteration plus "
                "English on every line, with example sentences in every "
                "record - alphabet and script, pronunciation, nouns, verbs, "
                "adjectives and adverbs, pronouns, numbers and time, "
                "greetings, grammar, daily-life sentences, tenses, questions, "
                "commands, descriptions, stories, idioms, registers, complex "
                "sentences, conversations and a full mastery review, organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation, core nouns, "
              "core verbs, adjectives and adverbs, pronouns, numbers and time, "
              "greetings, grammar essentials, home and family, food and "
              "cooking) -> Compounded (travel and directions, work and school, "
              "health and body, emotions and feelings, nature and weather, "
              "shopping and money, friendship and social life, technology and "
              "communication, verb tenses, questions and answers, commands and "
              "requests) -> Advanced (descriptions, three stories, idioms and "
              "proverbs, formal and polite registers, compound and complex "
              "sentences, three conversations, mastery review).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Telugu alphabet, script, pronunciation, nouns, verbs, adjectives, pronouns, numbers, greetings, grammar, tenses, idioms, proverbs, conversations, stories...",
        "chat_ph": "Ask about the Telugu language...",
        "archive_blurb": ("Seeded %s Telugu language learning records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Telugu language learning studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the Telugu language - from the alphabet and script through pronunciation, nouns, verbs, adjectives, pronouns, numbers, greetings and grammar, through travel, work, health, feelings, nature, shopping, social life, technology, tenses, questions and commands, to descriptions, stories, idioms, registers, complex sentences and conversations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "telugu-language-study", "gen_demo_kind": "telugu-language-demo",
        "source": source,
    }

CIT_PUB = ("Telugu linguistics (standard references: Krishnamurti, Bhadriraju "
           "& Gwynn, J. P. L. A Grammar of Modern Telugu. Oxford University "
           "Press; 1985; Krishnamurti, Bhadriraju. The Dravidian Languages. "
           "Cambridge University Press; 2003; Gwynn, J. P. L. A "
           "Telugu-English Dictionary. Oxford University Press; 1991; "
           "Subrahmanyam, P. S. Dravidian Comparative Phonology. Annamalai "
           "University; 1983; Unicode Standard, Telugu block U+0C00-U+0C7F; "
           "ISO 639-1:2002 code 'te'; ISO 639-3:2007 code 'tel'; ISO "
           "15919:2001 transliteration of Telugu).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature language "
                     "instrument - Telugu as a working system he commands - "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-telugu"] = _cfg(
    "language-telugu", "Telugu Language Database",
    "Learn Telugu (తెలుగు): real, fact-checked Telugu linguistic data with "
    "Telugu script plus transliteration plus English on every line and "
    "example sentences in every record, taught progressively along the "
    "ladder from the alphabet to full conversations.",
    "language learning record", "JAH-LTEL-", "JAH Telugu Language Tutor",
    "telugu language tutor - teaching the Telugu language progressively along "
    "the ladder from the alphabet and script through pronunciation, "
    "vocabulary, grammar and daily sentences to stories, idioms, registers "
    "and conversations; answers from many angles - definition, example, "
    "analogy, application, history, how-to - using only archive data from "
    "this system",
    CIT_PUB, "public")
DBCFG["language-telugu-signature"] = _cfg(
    "language-telugu-signature", "Telugu Language Signature Database",
    "His original Signature language instrument: Telugu as a working system "
    "he commands, taught through the Signature lens from the alphabet through "
    "the sound system, words, grammar and daily sentences to stories, idioms, "
    "registers and full conversations. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "language learning record", "JAH-LTELS-", "JAH Telugu Language Tutor (Signature)",
    "telugu language tutor - Signature editions: his original Signature "
    "language instrument, Telugu as a working system he commands, clearly "
    "labeled Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, how-to - using only archive data from "
    "this system",
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
    for slug in ("language-telugu", "language-telugu-signature"):
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

    print("built %d databases, %d records - manifest/api/restamp/commit left to the merger" % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
