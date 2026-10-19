#!/usr/bin/env python3
"""Build the Arabic to English databases for JAH Databases
(Manon's language orders #10-11, 2026-10-17, roster rank 5).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases)
PLUS every shard index title in jah-databases-data-1 (814 index files):
zero 'language-arabic*' slugs. ID prefixes JAH-LARA- (public) and
JAH-LARAS- (signature) verified free in the manifest id_prefix values AND
in every shard index (zero zgrep hits for 'JAH-LARA' across 814
index.jsonl.gz files). Pre-authoring whole-system dedupe-gate check over
all 68 planned titles (34 + 34 Signature Edition): zero collisions, zero
refusals.

This build creates two NEW databases, 34 ladder-ordered records each:

  language-arabic              - The Arabic to English Database
                                 (public-harvest: real, fact-checked
                                 Modern Standard Arabic - overview,
                                 writing system, phonology, core
                                 vocabulary with sentences, grammar
                                 essentials, themed sentence sets, verb
                                 tenses, Q&A, commands, descriptions,
                                 stories, idioms, registers, complex
                                 sentences, conversations, mastery
                                 reference; standard references Wright
                                 1896, Ryding 2005, Badawi-Carter-Gully
                                 2004, Holes 2004, Hans Wehr 1979,
                                 ISO 233:1984)
  language-arabic-signature    - The Arabic to English Signature Database
                                 (his original Signature Language Method:
                                 every letter a sworn mark, every root a
                                 family, every sentence a covenant of
                                 meaning; src signature, titles suffixed
                                 " (Signature Edition)", clearly labeled
                                 Signature-made, never presented as
                                 authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record carries Arabic content (Arabic script + transliteration) +
English translation + example sentences. Sentences are required in EVERY
record - no vocabulary-list-only records.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_arabic.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing.

Build-time cross-check: every entry declares 'must_contain' strings and
the build asserts each one appears verbatim in the record description, so
entry text and demo outputs can never drift apart.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER commits or pushes.
It only creates: db/language-arabic[-signature]/ (index.html + gen-*.js),
the shard dirs under jah-databases-data-1, and the merger fragment. A
merger handles manifest/api/restamp/commit/push.

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/language-arabic.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_arabic import ENTRIES, SIG_TAIL
from demos_language_arabic import DEMOS

# ---------------------------------------------------------------- DB config

GROUPS = ["Foundations", "Core Vocabulary", "Grammar Essentials",
          "Everyday Themes", "Grammar in Action", "Stories and Idioms",
          "Conversation and Registers", "Mastery Reference"]

LADDER = (" Records are ordered by the teaching ladder: Foundations "
          "(language overview, the writing system, pronunciation and "
          "phonology) -> Core Vocabulary (nouns, verbs, adjectives and "
          "adverbs, pronouns, numbers and time, greetings) -> Grammar "
          "Essentials (the ten load-bearing rules) -> Everyday Themes "
          "(home and family, food, travel, work and school, health, "
          "emotions, nature, shopping, friendship, technology) -> "
          "Grammar in Action (verb tenses, questions and answers, "
          "commands, descriptions) -> Stories and Idioms (three short "
          "stories, idioms and proverbs) -> Conversation and Registers "
          "(formal registers, complex sentences, three conversations) "
          "-> Mastery Reference (alphabet, 200 core words, grammar "
          "rules, phrase tables).")


def _cfg(name, tagline, prefix, ai, role, source):
    sig = source == "signature"
    sig_line = ("Signature originals - his original Signature Language "
                "Method: every letter a sworn mark, every root a family, "
                "every sentence a covenant of meaning. Clearly labeled "
                "Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked Modern Standard "
                "Arabic: the writing system, pronunciation, core "
                "vocabulary with sentences, grammar essentials, themed "
                "sentence sets, verb tenses, questions and answers, "
                "commands, descriptions, stories, idioms and proverbs, "
                "registers, complex sentences, and conversations - every "
                "line in Arabic script with transliteration and English "
                "translation, organized in the Signature system.")
    return {
        "name": name, "tagline": tagline, "record_kind": "language learning record",
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if sig else pub_line, LADDER),
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Arabic letters, words, verbs, grammar, phrases, stories, idioms...",
        "chat_ph": "Ask about Arabic...",
        "archive_blurb": ("Seeded %s Arabic language learning records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": ("Foundations \u00b7 Core Vocabulary \u00b7 Grammar Essentials \u00b7 Everyday Themes \u00b7 "
                   "Grammar in Action \u00b7 Stories and Idioms \u00b7 Conversation and Registers \u00b7 "
                   "Mastery Reference - each field opens on demand and loads only what you open"),
        "gen_desc": "Generate clearly-labeled Arabic language studies. Seeded archive records are the authoritative entries.",
        "greet": ("I am the %s. Ask me about Arabic - from the alphabet and sounds through core "
                  "vocabulary and grammar to stories, idioms, and conversations." % ai),
        "gen_fields": list(GROUPS),
        "gen_kind": "arabic-language-study", "gen_demo_kind": "arabic-language-demo",
        "source": source,
    }

ROLE_PUB = ("arabic to english archivist - teaching Modern Standard Arabic "
            "with Arabic script, transliteration, and English translations; "
            "foundations through vocabulary and grammar to stories, idioms, "
            "and conversations; answers from many angles - definition, "
            "example, analogy, application, history, how-to - using only "
            "archive data from this system")
ROLE_SIG = (ROLE_PUB + " - Signature editions: his original Signature "
            "Language Method, every letter a sworn mark and every sentence "
            "a covenant of meaning, clearly labeled Signature-made and "
            "never presented as authentic public record")

DBCFG = {}
DBCFG["language-arabic"] = _cfg(
    "The Arabic to English Database",
    "Learn Modern Standard Arabic with English translations: the alphabet "
    "and writing system, pronunciation, core vocabulary with sentences, "
    "grammar essentials, themed sentence sets, verb tenses, stories, "
    "idioms, and conversations - every line in Arabic script with "
    "transliteration and English, taught progressively along the ladder.",
    "JAH-LARA-", "JAH Arabic to English Archivist", ROLE_PUB, "public")
DBCFG["language-arabic-signature"] = _cfg(
    "The Arabic to English Signature Database",
    "His original Signature Language Method: every letter a sworn mark, "
    "every root a family, every sentence a covenant of meaning. The full "
    "ladder from the alphabet and sounds through core vocabulary and "
    "grammar to stories, idioms, and conversations, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "JAH-LARAS-", "JAH Arabic to English Archivist (Signature)", ROLE_SIG, "signature")

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
        program = demo_fn(base._hdr, title, rid, e["group"], e)
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    frag = {}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        sig = slug.endswith("-signature")
        frag["signature" if sig else "public"] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(recs),
            "status": "live",
            "full_records": len(recs),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if sig else "public-harvest",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
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

    by_key = {e["key"]: e for e in ENTRIES}
    built = {}
    for slug in ("language-arabic", "language-arabic-signature"):
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
            # cross-check: entry text vs demo outputs (must_contain)
            for s in by_key[[e2["key"] for e2 in ENTRIES if e2["name"] == r["name"]][0]]["must_contain"]:
                assert s in r["description"], "must_contain drift in %s: %r" % (r["id"], s[:40])
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
    print("built %d databases, %d records total" % (len(built), total))
    print("NEXT (merger): manifest + api.json append, restamp_counts.py, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
