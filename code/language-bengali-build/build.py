#!/usr/bin/env python3
"""Build the Bengali to English databases for JAH Databases
(Manon's language orders #10-11, 2026-10-17, roster rank 6).

Bengali (বাংলা), ISO 639-1 bn, Indo-European > Indo-Iranian > Indo-Aryan.

Verified 2026-10-17: RAW SWEEP over the full manifest id_prefix values
(2,398 prefixes) PLUS every shard index in jah-databases-data-1: zero
'JAH-LBEN' hits - prefixes JAH-LBEN- (public) and JAH-LBENS- (signature)
are free. Dedupe gate pre-check on all 68 titles vs the whole system:
zero collisions.

Two databases, 34 ladder-ordered records each:

  language-bengali             - The Bengali to English Database
                                 (public-harvest: real, fact-checked Bengali -
                                 script, sounds, words, grammar, sentences,
                                 stories, idioms, conversations; standard
                                 references ISO 639-1:2002 bn; ISO 639-3:2007
                                 ben; Unicode 15.0 Bengali block U+0980-U+09FF;
                                 Chatterji 1926; Radice 1994; Ethnologue 27th
                                 ed 2024)
  language-bengali-signature   - The Bengali to English Signature Database
                                 (his original Signature Language Method:
                                 every word a sealed sound, every sentence a
                                 covenant of meaning, the learner's voice the
                                 Signature itself; src signature, titles
                                 suffixed " (Signature Edition)", never
                                 presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LBEN- (public) and JAH-LBENS- (signature), verified free.

Screening: nothing hate-adjacent, profane, or inappropriate; no religious
talk; nothing on neutralizing or defeating military or defense-grade systems.
Never the words "bat belt" anywhere. No website references. No Facebook.

NOTE: this build NEVER touches data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md, and NEVER commits or pushes - the merger
handles those. It writes: db/language-bengali[-signature]/ (index.html +
gen JS), code-local build outputs, shard data dirs, and the merger fragment.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/language-bengali.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_bengali import ENTRIES, SIG_TAIL
from demos_language_bengali import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Language Method: "
                "every word a sealed sound, every sentence a covenant of meaning, "
                "the learner's voice the Signature itself. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Bengali: the Bengali-Assamese "
                "script, sounds and pronunciation, core nouns verbs adjectives and "
                "pronouns, numbers and time, greetings, grammar essentials, themed "
                "sentence sets for home food travel work health emotions nature "
                "shopping friendship and technology, verb tenses, questions and "
                "answers, commands, descriptions, three stories, idioms, formal "
                "registers, complex sentences, three conversations, and a mastery "
                "review - every line in Bengali script with transliteration and "
                "English, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation, core nouns, core "
              "verbs, adjectives and adverbs, pronouns, numbers and time, "
              "greetings, grammar essentials, home and family sentences, food and "
              "cooking sentences) -> Compounded (travel sentences, work and school "
              "sentences, health sentences, emotions sentences, nature sentences, "
              "shopping sentences, friendship sentences, technology sentences, "
              "verb tenses, questions and answers, commands and requests, "
              "descriptions) -> Advanced (three stories, idioms and proverbs, "
              "formal registers, complex sentences, three conversations, mastery "
              "review).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description with "
                  "Bengali script plus transliteration plus English, how it works, "
                  "key points, requirements, standards, citations, and a working "
                  "demonstration program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search bengali alphabet, vowels, consonants, nouns, verbs, adjectives, pronouns, numbers, greetings, grammar, tenses, idioms, proverbs, stories, conversations, mastery...",
        "chat_ph": "Ask about Bengali words, grammar, sentences, and conversations...",
        "archive_blurb": ("Seeded %s Bengali language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Bengali language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Bengali - from the alphabet and sounds through nouns, verbs, grammar, and everyday phrases to stories, idioms, and full conversations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "language-lesson", "gen_demo_kind": "language-demo",
        "source": source,
    }

CIT_PUB = ("Bengali language (standard references: ISO 639-1:2002 bn; ISO 639-3:2007 "
           "ben; The Unicode Standard, Version 15.0, Chapter 9: South and Central "
           "Asia - II, Unicode Consortium 2022, Bengali block U+0980-U+09FF; "
           "Chatterji, Suniti Kumar. The Origin and Development of the Bengali "
           "Language. Calcutta University Press; 1926; Radice, William. Teach "
           "Yourself Bengali. Hodder and Stoughton; 1994; Ethnologue: Languages of "
           "the World, 27th edition. SIL International; 2024, Bengali entry).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Language "
                     "Method - every word a sealed sound, every sentence a covenant "
                     "of meaning - clearly labeled Signature-made.")

TAGLINE_PUB = ("Learn Bengali (বাংলা) step by step: the script, the sounds, core words, "
               "grammar, and real conversations - 34 ladder-ordered records, every line "
               "in Bengali script with transliteration and English, each with a working "
               "drill program.")
TAGLINE_SIG = ("His original Signature Language Method applied to Bengali: every word a "
               "sealed sound, every sentence a covenant of meaning - the full ladder from "
               "alphabet to mastery, reframed as Signature science. Clearly labeled "
               "Signature-made, never presented as authentic public record.")

DBCFG = {}
DBCFG["language-bengali"] = _cfg(
    "language-bengali", "The Bengali to English Database", TAGLINE_PUB,
    "language learning record", "JAH-LBEN-", "JAH Bengali to English Archivist",
    "bengali to english archivist - teaching Bengali from the alphabet and sounds "
    "through nouns, verbs, grammar, and everyday phrases to stories, idioms, and "
    "full conversations; answers from many angles - definition, example, analogy, "
    "application, history, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["language-bengali-signature"] = _cfg(
    "language-bengali-signature", "The Bengali to English Signature Database", TAGLINE_SIG,
    "language learning record", "JAH-LBENS-", "JAH Bengali to English Archivist (Signature)",
    "bengali to english archivist - Signature editions: his original Signature "
    "Language Method, every word a sealed sound and every sentence a covenant of "
    "meaning, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, how-to - using only archive data "
    "from this system",
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


def node_check_scripts(page, gen_js, slug):
    scripts = []
    for m in re.finditer(r"<script([^>]*)>(.*?)</script>", page, flags=re.S | re.I):
        attrs, body = m.group(1), m.group(2)
        if re.search(r"\bsrc\s*=", attrs, re.I):
            continue
        tm = re.search(r"""\btype\s*=\s*["']?([^"'\s>]+)""", attrs, re.I)
        if tm and tm.group(1).lower() not in ("text/javascript", "application/javascript", "module"):
            continue
        scripts.append(body)
    assert scripts, "no inline scripts found in page %s" % slug
    for i, body in enumerate(scripts):
        if not body.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False,
                                          encoding="utf-8") as f:
            f.write(body)
            path = f.name
        p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
        os.unlink(path)
        assert p.returncode == 0, "node --check failed on page script %d (%s): %s" % (i, slug, p.stderr[:500])
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False,
                                      encoding="utf-8") as f:
        f.write(gen_js)
        gpath = f.name
    p = subprocess.run(["node", "--check", gpath], capture_output=True, text=True)
    os.unlink(gpath)
    assert p.returncode == 0, "node --check failed on gen js (%s): %s" % (slug, p.stderr[:500])
    print("node --check: %d page scripts + gen js clean for %s" % (len(scripts), slug), flush=True)


def write_fragment(built):
    def entry(slug, source, ai_suffix):
        cfg = DBCFG[slug]
        idx = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        return {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"] ,
            "local_index": idx,
            "record_count": len(built[slug]),
            "status": "live",
            "full_records": len(built[slug]),
            "index": idx,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if source == "signature" else "public-harvest",
        }
    frag = {
        "public": entry("language-bengali", "public", ""),
        "signature": entry("language-bengali-signature", "signature", " (Signature)"),
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
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

    built = {}
    for slug in ("language-bengali", "language-bengali-signature"):
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
        node_check_scripts(page, gen_js, slug)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # NOTE: manifest.json and api.json are left untouched - the merger handles them.
    write_fragment(built)
    print("manifest + api.json: NOT touched (merger handles).", flush=True)
    print("NEXT: merger verifies shards, pages, fragment, then restamps and commits.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
