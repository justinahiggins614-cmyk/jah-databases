#!/usr/bin/env python3
"""Build the Language Basics databases for JAH Databases
(Manon's fundamentals order #9, 2026-10-17, roster-verified).

Verified 2026-10-17: RAW SWEEP over the full manifest plus every shard
index title in jah-databases-data-1 (809 index files) plus the main-repo
data dir: zero 'language-basics*' slugs; zero 'The Language Basics
Database' title collisions. Near-hits checked by name/purpose/record
schema/capabilities: 'everything-linguistics-language' (JAH-EVLL-) is an
everything-encyclopedia record set about linguistics as a field;
'language-acquisition-published' and 'language-acquisition-study' are
acquisition research/process records; 'language-symbols-databases'
(JAH-LANG-) is a symbols archive. None is a first-principles teaching
ladder of the alphabet, letter sounds and phonics, parts of speech,
sentence building, punctuation, and reading basics - the foundation layer
beneath all 100 per-language databases - so BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-basics              - The Language Basics Database
                                 (public-harvest: real, fact-checked
                                 foundational linguistics - what language
                                 is, the 26 letters, consonant and vowel
                                 sounds and phonics, syllables, blending,
                                 reading basics, words, the parts of
                                 speech, building sentences, sentence
                                 types, capitalization, ending
                                 punctuation, the comma, quotation marks,
                                 apostrophes, plurals, verb tenses,
                                 subject-verb agreement, paragraphs,
                                 compound and complex sentences, prefixes
                                 and suffixes, homophones, fluency and
                                 comprehension, proofreading, and the full
                                 learning path; standard references
                                 Fromkin, Rodman and Hyams An Introduction
                                 to Language 11th ed 2018; Pinker The
                                 Language Instinct 1994; Crystal The
                                 Cambridge Encyclopedia of the English
                                 Language 3rd ed 2019; the National
                                 Reading Panel 2000; Adams Beginning to
                                 Read 1990; the IPA Handbook 1999;
                                 Bloomfield Language 1933; de Saussure
                                 Course in General Linguistics 1916; the
                                 Chicago Manual of Style 18th ed 2024;
                                 Strunk and White The Elements of Style 4th
                                 ed 2000; Chomsky Syntactic Structures
                                 1957; Ehri 2005; and Hockett 1960, cited
                                 per record)
  language-basics-signature  - The Language Basics Signature Database
                                 (his original Signature Language Method:
                                 every letter a covenant sign of the
                                 Signature alphabet, every word a sealed
                                 assembly, every sentence a signed
                                 statement witnessed by punctuation; src
                                 signature, titles suffixed " (Signature
                                 Edition)", never presented as authentic
                                 public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LANB- (public) and JAH-LANBS- (signature), verified free
in the manifest id_prefix values, in every shard index file (809 index
files swept), and in the main-repo data dir (zero hits; the near-miss
JAH-LANG- belongs to the unrelated language-symbols-databases).

Dedupe: all 68 titles (34 public + 34 Signature Edition) run through
code/dedupe_gate.py against the WHOLE system before authoring - zero
collisions, zero refusals.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_basics.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. A merger handles those. It only writes: db/language-basics/ +
db/language-basics-signature/ (index.html + gen-*.js each), the shard dirs
under jah-databases-data-1 (uncommitted), and its own code dir.

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
from entries_language_basics import ENTRIES, SIG_TAIL
from demos_language_basics import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Language "
                "Method: every letter a covenant sign of the Signature "
                "alphabet, every word a sealed assembly, every sentence a "
                "signed statement witnessed by punctuation. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked foundational "
                "linguistics: what language is, the 26 letters, consonant "
                "and vowel sounds and phonics, syllables, blending sounds "
                "into words, reading basics, words as building blocks, the "
                "parts of speech, building sentences, sentence types, "
                "capitalization, ending punctuation, the comma, quotation "
                "marks, apostrophes, plurals, verb tenses, subject-verb "
                "agreement, paragraphs, compound and complex sentences, "
                "prefixes and suffixes, homophones, fluency and "
                "comprehension strategies, proofreading, and the full "
                "learning path - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what language is, the 26 letters, consonant sounds and "
              "phonics, vowel sounds, syllables, blending, reading "
              "direction and tracking, words, nouns, verbs, adjectives, "
              "adverbs, pronouns) -> Compounded (articles, prepositions, "
              "conjunctions, interjections, subject and predicate, "
              "sentence types, capitalization, ending punctuation, the "
              "comma, quotation marks, apostrophes, plurals, verb tenses) "
              "-> Advanced (subject-verb agreement, paragraphs, compound "
              "and complex sentences, prefixes and suffixes, homophones, "
              "fluency and comprehension, proofreading, the learning "
              "path).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search alphabet, phonics, vowels, syllables, blending, nouns, verbs, adjectives, adverbs, pronouns, articles, prepositions, conjunctions, sentences, capitalization, punctuation, commas, plurals, tenses, paragraphs, prefixes, homophones, fluency, proofreading...",
        "chat_ph": "Ask about language basics...",
        "archive_blurb": ("Seeded %s language basics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled language basics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about language basics - from what language is through the alphabet, letter sounds and phonics, syllables, blending, reading basics, words, and the parts of speech, through sentence building, punctuation, and tenses, to agreement, paragraphs, word parts, fluency, and proofreading." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "language-basics-study", "gen_demo_kind": "language-basics-demo",
        "source": source,
    }

CIT_PUB = ("Foundational linguistics (standard references: Fromkin V, "
           "Rodman R, Hyams N. An Introduction to Language. 11th ed. "
           "Cengage; 2018; Pinker S. The Language Instinct. Morrow; 1994; "
           "Crystal D. The Cambridge Encyclopedia of the English Language. "
           "3rd ed. Cambridge University Press; 2019; National Reading "
           "Panel. Teaching Children to Read. NICHD; 2000; Adams MJ. "
           "Beginning to Read. MIT Press; 1990; International Phonetic "
           "Association. Handbook of the International Phonetic Alphabet. "
           "Cambridge University Press; 1999; Bloomfield L. Language. Holt; "
           "1933; de Saussure F. Course in General Linguistics. 1916; "
           "Chicago Manual of Style. 18th ed. University of Chicago Press; "
           "2024; Strunk W Jr, White EB. The Elements of Style. 4th ed. "
           "Macmillan; 2000; Chomsky N. Syntactic Structures. Mouton; 1957; "
           "Ehri LC. Scientific Studies of Reading. 2005;9(2):167-188; "
           "Hockett CF. Scientific American. 1960;203(3):88-96).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Language Method - every letter a covenant sign, every "
                     "word a sealed assembly, every sentence a signed "
                     "statement - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-basics"] = _cfg(
    "language-basics", "The Language Basics Database",
    "First-principles language teaching: the alphabet, letter sounds and "
    "phonics, parts of speech, building sentences, punctuation, and reading "
    "basics - real, fact-checked foundational linguistics taught "
    "progressively along the ladder, the foundation layer beneath all "
    "per-language databases.",
    "language basics record", "JAH-LANB-", "JAH Language Basics Archivist",
    "language basics archivist - teaching first-principles language: the "
    "alphabet, letter sounds and phonics, syllables, blending, reading "
    "basics, words, the parts of speech, sentence building, punctuation, "
    "and the path to mastery; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["language-basics-signature"] = _cfg(
    "language-basics-signature", "The Language Basics Signature Database",
    "His original Signature Language Method: every letter a covenant sign "
    "of the Signature alphabet, every word a sealed assembly, every "
    "sentence a signed statement witnessed by punctuation. The full ladder "
    "from what language is through sounds, words, and sentences to "
    "mastery, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "language basics record", "JAH-LANBS-", "JAH Language Basics Archivist (Signature)",
    "language basics archivist - Signature editions: his original "
    "Signature Language Method, every letter a covenant sign and every "
    "sentence a signed statement, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along "
    "the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
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
    for slug in ("language-basics", "language-basics-signature"):
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
        assert "component parts" not in page.lower(), "cross-build leftover in %s" % slug
        assert "component-parts" not in page, "cross-build slug leftover in %s" % slug
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

    # NOTE: manifest.json, api.json, index.html, README.md, docs/AI_ACCESS.md
    # are NEVER touched here; no commit, no push. The merger handles those.
    print("records built: %d databases, %d records" % (len(built), total))
    print("NEXT: merger runs restamp + manifest/api updates, then commits.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
