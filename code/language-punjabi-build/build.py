#!/usr/bin/env python3
"""Build the Punjabi to English databases for JAH Databases
(Manon's language orders #10-11, 2026-10-17, roster rank 9).

Verified 2026-10-17: RAW SWEEP over the full manifest PLUS every shard
index title in jah-databases-data-1 PLUS the main-repo data dir:
zero 'language-punjabi*' slugs/names; zero 'punjabi' title collisions
across all 68 candidate titles (checked via code/dedupe_gate.py against
the whole-system exact-title gate before authoring). ID prefixes
JAH-LPAN- (public) and JAH-LPANS- (signature): zero hits in manifest
id_prefix values and zero hits in all shard index files.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-punjabi               - The Punjabi to English Database
                                   (public-harvest: real, fact-checked
                                   Punjabi teaching - Gurmukhi script,
                                   phonology and tone, core vocabulary
                                   with sentences, grammar, themed
                                   sentence sets, verb tenses, questions,
                                   commands, descriptions, stories,
                                   idioms, registers, complex sentences,
                                   dialogues, and the full mastery
                                   reference; standard references
                                   Bhatia 1993, Shackle 2003, Gill &
                                   Gleason 1969, the Unicode Gurmukhi
                                   block)
  language-punjabi-signature     - The Punjabi to English Signature
                                   Database
                                   (his original Signature Language
                                   Method: every tone a signature stroke,
                                   every postposition a handshake, every
                                   dialect a witness, the whole ladder
                                   reframed as Signature science;
                                   src signature, titles suffixed
                                   " (Signature Edition)", never
                                   presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_punjabi.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this builder NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or
pushes. A merger handles those. This build writes only: db/language-
punjabi[-signature]/ (index.html + gen-*.js), the data-1 shard dirs,
and the merger fragment.

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/language-punjabi.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_punjabi import ENTRIES, SIG_TAIL
from demos_language_punjabi import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Language "
                "Method: every tone a signature stroke, every postposition a "
                "handshake after the noun, every dialect a witness to the "
                "same original draft, the whole ladder from script through "
                "conversation reframed as Signature science. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Punjabi teaching: the "
                "Gurmukhi script and its thirty-five letters, pronunciation "
                "phonology and the three tones, core nouns verbs adjectives "
                "adverbs pronouns numbers and time with example sentences, "
                "grammar essentials, twenty-sentence sets for home family "
                "food travel work school health emotions nature shopping "
                "friendship and technology, verb tenses, questions and "
                "answers, commands and requests, descriptions, three "
                "stories, idioms and proverbs, formal registers, complex "
                "sentences, three dialogues, and the full mastery review - "
                "every record carrying Punjabi in Gurmukhi plus plain "
                "transliteration plus English, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, Gurmukhi writing system, pronunciation "
              "and phonology, core nouns, core verbs, adjectives and "
              "adverbs, pronouns, numbers and time, greetings and everyday "
              "phrases) -> Compounded (grammar essentials, home and family "
              "sentences, food and cooking sentences, travel and directions "
              "sentences, work and school sentences, health and body "
              "sentences, emotions and feelings sentences, nature and "
              "weather sentences, shopping and money sentences, friendship "
              "and social life sentences, technology and communication "
              "sentences) -> Advanced (verb tenses in sentences, questions "
              "and answers, commands and requests, descriptions of people "
              "and places, three short stories, idioms and proverbs, "
              "formal and polite registers, compound and complex sentences, "
              "three conversations, mastery review and full reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Gurmukhi letters, tones, nouns, verbs, adjectives, pronouns, numbers, greetings, grammar, tenses, stories, idioms, dialogues, mastery review...",
        "chat_ph": "Ask about learning Punjabi...",
        "archive_blurb": ("Seeded %s Punjabi language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Punjabi language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about learning Punjabi - from the Gurmukhi script and the three tones through core words and grammar, to sentences for daily life, tenses, stories, idioms, and real dialogues." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "punjabi-language-study", "gen_demo_kind": "punjabi-language-demo",
        "source": source,
    }

CIT_PUB = ("Punjabi linguistics (standard references: Bhatia, Tej K. "
           "Punjabi: A Cognitive-Descriptive Grammar. Routledge; 1993; "
           "Shackle, Christopher. Punjabi. In The Indo-Aryan Languages, "
           "edited by George Cardona and Dhanesh Jain, Routledge; 2003; "
           "Gill, Harjit Singh and Gleason, Henry A. A Reference Grammar "
           "of Punjabi; 1969; The Unicode Standard - Gurmukhi block "
           "U+0A00-U+0A7F; Ethnologue: Punjabi, ISO 639-3 pan).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Language Method - every tone a signature stroke, "
                     "every postposition a handshake - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["language-punjabi"] = _cfg(
    "language-punjabi", "The Punjabi to English Database",
    "Learn Punjabi from the ground up: Gurmukhi script, sounds and tones, "
    "core words with sentences, grammar, themed sentence sets, verb tenses, "
    "stories, idioms, and full dialogues - every record in Punjabi with "
    "transliteration and English, taught step by step along the ladder.",
    "language learning record", "JAH-LPAN-", "JAH Punjabi to English Archivist",
    "punjabi to english archivist - teaching the Punjabi language from the "
    "Gurmukhi script and the three tones through core vocabulary with "
    "sentences and grammar essentials, through themed sentence sets for "
    "daily life, to tenses, stories, idioms, registers, and real dialogues; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, how-to - using only archive data from "
    "this system",
    CIT_PUB, "public")
DBCFG["language-punjabi-signature"] = _cfg(
    "language-punjabi-signature", "The Punjabi to English Signature Database",
    "His original Signature Language Method for Punjabi: every tone a "
    "signature stroke, every postposition a handshake, every dialect a "
    "witness - the full ladder from Gurmukhi script through core words, "
    "grammar, daily-life sentences, tenses, stories, idioms, and dialogues, "
    "reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "language learning record", "JAH-LPANS-", "JAH Punjabi to English Archivist (Signature)",
    "punjabi to english archivist - Signature editions: his original "
    "Signature Language Method for Punjabi, every tone a signature stroke "
    "and every postposition a handshake, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, how-to - using only archive data from this system",
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


def node_check_page_scripts(ppath):
    """Extract inline JavaScript page scripts and run node --check on each.
    Skips non-JS script blocks such as application/ld+json."""
    html = open(ppath, encoding="utf-8").read()
    found = re.findall(r'<script([^>]*)>(.*?)</script>', html, flags=re.S | re.I)
    blocks = [b for attrs, b in found
              if "src=" not in attrs.lower()
              and "ld+json" not in attrs.lower()]
    assert blocks, "no inline scripts found in %s" % ppath
    for i, b in enumerate(blocks):
        if not b.strip():
            continue
        tmp = "/tmp/pan_script_%d.js" % i
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(b)
        p = subprocess.run(["node", "--check", tmp],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "node --check failed block %d: %s" % (i, p.stderr[:500])
    return len([b for b in blocks if b.strip()])


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
    for slug in ("language-punjabi", "language-punjabi-signature"):
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
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        # JS hygiene: node --check on the gen file and every inline page script
        pg = subprocess.run(["node", "--check", gpath],
                            capture_output=True, text=True, timeout=60)
        assert pg.returncode == 0, "node --check failed gen js: %s" % pg.stderr[:500]
        nblocks = node_check_page_scripts(ppath)
        print("page:  db/%s/index.html + gen-%s.js [%s] node: gen OK, %d script blocks OK"
              % (slug, slug, ", ".join(notes), nblocks), flush=True)

    # Merger fragment (the merger owns manifest.json / api.json / counts).
    frag = {"public": {}, "signature": {}}
    for slug, key in (("language-punjabi", "public"),
                      ("language-punjabi-signature", "signature")):
        cfg = DBCFG[slug]
        n = len(built[slug])
        is_sig = key == "signature"
        frag[key] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": n,
            "status": "live",
            "full_records": n,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest" if key == "public" else "signature",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT)
    print("NOTE: manifest.json / api.json untouched - merger handles those.")
    print("NEXT: merger runs python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
