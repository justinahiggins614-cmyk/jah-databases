#!/usr/bin/env python3
"""Build The Japanese to English Database (Manon's language order #10,
roster rank 10).

Two NEW databases, 34 ladder-ordered records each, per the shared
per-language template (overview, writing systems, phonology, core
vocabulary with sentences, grammar essentials, themed sentence sets,
tenses, questions, commands, descriptions, stories, idioms, registers,
complex sentences, conversations, mastery review):

  language-japanese              - The Japanese to English Database
                                   (public-harvest: real, fact-checked
                                   Japanese - kana, kanji, romaji, and
                                   English on every line; every record a
                                   full lesson with example sentences)
  language-japanese-signature    - The Japanese to English Signature Database
                                   (his original Signature Language
                                   Method: every kana a sworn sound-seal,
                                   every kanji a meaning-covenant, every
                                   particle a bridge-oath; src signature,
                                   titles suffixed " (Signature Edition)",
                                   never presented as authentic public
                                   record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LJPN- (public) and JAH-LJPNS- (signature), verified free
in the manifest and in every shard index (zero hits), 2026-10-17.
Dedupe gate: all 68 titles checked against the whole system before
authoring - zero collisions.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_japanese.py). Every demo prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker; the build machine-executes all 68 demos before finishing.

Pipeline replicates code/component-parts-catalog-build/build.py for page
structure. Concurrency rules for this shared clone: this build NEVER
touches data/manifest.json, api.json, index.html, README.md, or
docs/AI_ACCESS.md, and NEVER runs git commit or git push - the merger
handles those. It only creates db/language-japanese*/ pages, the shard
data dirs, and the missing-builds fragment.

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
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "code", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_japanese import ENTRIES, SIG_TAIL
from demos_japanese import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Language Method: "
                "every kana a sworn sound-seal, every kanji a meaning-covenant, "
                "every particle a bridge-oath between speaker and listener, "
                "and every conversation a completed circuit of understanding. "
                "Clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked Japanese: the language "
                "overview, the three writing scripts, pronunciation and pitch "
                "accent, core nouns verbs adjectives and adverbs, pronouns, "
                "numbers and time, greetings, grammar essentials, themed "
                "sentence sets for daily life, verb tenses, questions and "
                "answers, commands and requests, descriptions, stories, "
                "idioms and proverbs, formal and polite registers, complex "
                "sentences, full conversations, and a mastery review - every "
                "record carrying real Japanese with kana, kanji, romaji, and "
                "English translations plus example sentences, organized in "
                "the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation, core nouns, "
              "core verbs, adjectives and adverbs, pronouns, numbers and "
              "time, greetings, grammar essentials) -> Compounded (home and "
              "family, food and cooking, travel and directions, work and "
              "school, health and body, emotions and feelings, nature and "
              "weather, shopping and money, friendship and social life, "
              "technology and communication) -> Advanced (verb tenses, "
              "questions and answers, commands and requests, descriptions, "
              "three short stories, idioms and proverbs, formal and polite "
              "registers, complex sentences, three conversations, mastery "
              "review).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search kana, hiragana, katakana, kanji, romaji, verbs, particles, greetings, numbers, idioms, keigo, conversations...",
        "chat_ph": "Ask about Japanese words, grammar, and sentences...",
        "archive_blurb": ("Seeded %s Japanese language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Japanese language lessons. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Japanese - from the first sounds and kana through core words, particles, and grammar, to daily sentences, stories, idioms, polite registers, and full conversations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "language-lesson", "gen_demo_kind": "language-lesson-demo",
        "source": source,
    }

CIT_PUB = ("Japanese linguistics (standard references: Shibatani M. The "
           "Languages of Japan. Cambridge University Press; 1990; Tsujimura "
           "N. An Introduction to Japanese Linguistics. 4th ed. Wiley-"
           "Blackwell; 2023; Martin SE. A Reference Grammar of Japanese. "
           "University of Hawaii Press; 1975; Kuno S. The Structure of the "
           "Japanese Language. MIT Press; 1973; Vance TJ. An Introduction "
           "to Japanese Phonology. SUNY Press; 1987; Agency for Cultural "
           "Affairs, Japan. List of Joyo Kanji (2010); Japan Foundation. "
           "Japanese Language Proficiency Test Official Practice Materials, "
           "N5; ISO 639-1: ja; ISO 639-3: jpn).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Language Method - every kana a sworn sound-seal, every "
                     "kanji a meaning-covenant, every particle a bridge-oath "
                     "- clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-japanese"] = _cfg(
    "language-japanese", "The Japanese to English Database",
    "Learn Japanese step by step: real Japanese with kana, kanji, romaji, "
    "and English on every line - from the first sounds and scripts through "
    "core words and grammar to daily sentences, stories, idioms, polite "
    "registers, and full conversations, taught progressively along the "
    "ladder.",
    "language learning record", "JAH-LJPN-", "JAH Japanese to English Archivist",
    "japanese to english archivist - teaching real Japanese from the first "
    "sounds and kana through core words, particles, and grammar, to daily "
    "sentences, stories, idioms, polite registers, and full conversations; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, how-to - using only archive data from "
    "this system",
    CIT_PUB, "public")
DBCFG["language-japanese-signature"] = _cfg(
    "language-japanese-signature", "The Japanese to English Signature Database",
    "His original Signature Language Method: every kana a sworn sound-seal, "
    "every kanji a meaning-covenant, every particle a bridge-oath between "
    "speaker and listener, and every conversation a completed circuit of "
    "understanding. The full ladder from the first sounds through core "
    "words, daily sentences, stories, and idioms to full conversations, "
    "reframed as Signature teaching. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "language learning record", "JAH-LJPNS-", "JAH Japanese to English Archivist (Signature)",
    "japanese to english archivist - Signature editions: his original "
    "Signature Language Method, every kana a sworn sound-seal and every "
    "particle a bridge-oath, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "how-to - using only archive data from this system",
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
            "ladder": len(recs) + 1,
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


def node_check(path, label):
    p = subprocess.run(["node", "--check", path],
                       capture_output=True, text=True, timeout=60)
    assert p.returncode == 0, "node --check failed %s: %s" % (label, p.stderr[-500:])
    print("  node --check OK: %s" % label, flush=True)


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
    for slug in ("language-japanese", "language-japanese-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        assert [r["ladder"] for r in recs] == list(range(1, 35)), "ladder ordinals broken"
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder", "ladder_rank", "ladder_tier", "demo"):
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
        # JS hygiene: node --check the gen file and every inline page script
        node_check(gpath, "gen-%s.js" % slug)
        scripts = re.findall(r"<script>(.*?)</script>", page, flags=re.S)
        for i, body in enumerate(scripts):
            tmp = "/tmp/jpn_script_%s_%d.js" % (slug.replace("-", "_"), i)
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(body)
            node_check(tmp, "%s inline script %d" % (slug, i))
            os.remove(tmp)
        # apostrophe-free JS string literals for role/ai/greet/search
        for key in ("ai", "role", "greet", "search_ph", "chat_ph"):
            assert "'" not in DBCFG[slug][key], "apostrophe in %s (%s)" % (key, slug)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # missing-builds fragment for the merger
    os.makedirs(FRAGDIR, exist_ok=True)
    frag = {"public": {
                "slug": "language-japanese",
                "name": "The Japanese to English Database",
                "tagline": DBCFG["language-japanese"]["tagline"],
                "record_kind": "language learning record",
                "id_prefix": "JAH-LJPN-",
                "ai_name": "JAH Japanese to English Archivist",
                "local_index": SHARD_BASE + "/data/language-japanese/index.jsonl.gz",
                "record_count": 34, "status": "live", "full_records": 34,
                "index": SHARD_BASE + "/data/language-japanese/index.jsonl.gz",
                "chunk_pattern": "data/language-japanese/chunks/chunk-NNNN.jsonl.gz",
                "source": "public-harvest"},
            "signature": {
                "slug": "language-japanese-signature",
                "name": "The Japanese to English Signature Database",
                "tagline": DBCFG["language-japanese-signature"]["tagline"],
                "record_kind": "language learning record",
                "id_prefix": "JAH-LJPNS-",
                "ai_name": "JAH Japanese to English Archivist (Signature)",
                "local_index": SHARD_BASE + "/data/language-japanese-signature/index.jsonl.gz",
                "record_count": 34, "status": "live", "full_records": 34,
                "index": SHARD_BASE + "/data/language-japanese-signature/index.jsonl.gz",
                "chunk_pattern": "data/language-japanese-signature/chunks/chunk-NNNN.jsonl.gz",
                "source": "signature"}}
    fpath = os.path.join(FRAGDIR, "language-japanese.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath, flush=True)

    print("done: %d databases, %d records. manifest/api.json untouched (merger handles)." % (len(built), total))
    print("NEXT: merger runs restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
