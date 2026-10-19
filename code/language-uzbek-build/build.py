#!/usr/bin/env python3
"""Build the Uzbek Language databases for JAH Databases (language
project batch 5, ranks 41-50, 2026-10-17).

Dedupe gate: 'uzbek' zero hits across the full manifest; 'JAH-LUZB-'/
'JAH-LUZBS-' zero hits in all shard index files of jah-databases-data-1;
zero collisions on any of the 68 record titles, checked with
code/dedupe_gate.py BEFORE authoring. ID prefixes verified free: zero hits
in manifest id_prefix values (exact and substring) and zero hits in shard
record IDs.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-uzbek              - The Uzbek to English Database
  language-uzbek-signature    - The Uzbek to English Signature Database

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34); the shard index is written in ladder
order so pages present simple -> compounded -> complex.

Demos: real, runnable, stdlib-only Python; the build machine-executes all
68 demos; every demo prints real computed values and ends with the OK
marker.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/language-uzbek/index.html + gen-language-uzbek.js
              db/language-uzbek-signature/index.html + gen-language-uzbek-signature.js
  shard repo: data/language-uzbek/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/language-uzbek-signature/... (same)
  build dir : code/language-uzbek-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/language-uzbek.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Never the words "bat belt" anywhere. No website references. No Facebook.
Property of Justin Addam Higgins (JAH).
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/language-uzbek.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from langdata_uzbek import DATA
from entries_language_uzbek import ENTRIES, SIG_TAIL
from demos_language_uzbek import DEMOS

DISPLAY = "Uzbek"
ALPHABET_DESC = "the Latin alphabet"
SCRIPT_PHRASE = "Latin script"
LATIN = True


def _carry():
    if LATIN:
        return ("every record carrying %s plus English translation plus example sentences"
                % DISPLAY)
    return ("every record carrying %s in %s plus romanization plus English translation "
            "plus example sentences" % (DISPLAY, SCRIPT_PHRASE))


def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original %s: %s, the whole language "
                "taught as Signature science. Clearly labeled Signature-made, never "
                "presented as authentic public record."
                % (DATA["method"], DATA["method_note"]))
    pub_line = ("Public records - real, fact-checked %s language teaching: the language "
                "overview, %s writing system, pronunciation and phonology, core nouns "
                "verbs adjectives and adverbs with sentences, pronouns, numbers and time, "
                "greetings, grammar essentials, themed sentence sets for daily life, verb "
                "tenses, questions and answers, commands and requests, descriptions, "
                "stories, idioms, formal and polite registers, complex sentences, "
                "conversations, and a mastery review - %s."
                % (DISPLAY, ALPHABET_DESC, _carry()))
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation and phonology, core "
              "nouns, core verbs, adjectives and adverbs, pronouns, numbers and time, "
              "greetings, grammar essentials) -> Compounded (home and family, food and "
              "cooking, travel and directions, work and school, health and body, emotions "
              "and feelings, nature and weather, shopping and money, friendship and "
              "social life, technology and communication, verb tenses in sentences) -> "
              "Advanced (questions and answers, commands and requests, descriptions, "
              "three stories, idioms and proverbs, formal and polite registers, compound "
              "and complex sentences, three conversations, mastery review and full "
              "reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Uzbek letters, words, verbs, tenses, phrases, grammar, dialogues...",
        "chat_ph": "Ask about Uzbek...",
        "archive_blurb": ("Seeded %s Uzbek language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Uzbek language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Uzbek - from the Latin alphabet and sounds through core words, grammar, and everyday sentences to stories, idioms, and conversations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "uzbek-study", "gen_demo_kind": "uzbek-demo",
        "source": source,
    }


def _role(ai):
    return ("Uzbek language archivist - teaching Uzbek from the Latin alphabet "
            "and sounds through core vocabulary, grammar, and everyday sentences to stories, "
            "idioms, registers, and conversations; teaching progressively along the ladder from "
            "foundations through compounded to advanced; answers from many angles - definition, "
            "example, pronunciation, usage, grammar, culture - using only archive data from "
            "this system")


CITATION = 'Uzbek language teaching (standard references: Bodrogligeti A. Modern Literary Uzbek: A Manual for Intensive Elementary, Intermediate and Advanced Courses. Lincom Europa; 2003; Boeschoten H. Uzbek. In: Johanson L, Csató E, editors. The Turkic Languages. Routledge; 1998; ISO 639-1 uz and ISO 639-3 uzb; standard pedagogical sources for vocabulary, usage, and phraseology).'

DBCFG = {}
DBCFG["language-uzbek"] = _cfg(
    "language-uzbek", "The Uzbek to English Database",
    "Learn Uzbek from the ground up: the language overview, the Latin alphabet, "
    "pronunciation and phonology, core vocabulary with sentences, grammar essentials, and "
    "themed sentence sets for daily life - every record carrying Uzbek plus English translation plus example sentences, taught progressively along the ladder.",
    "language learning record", "JAH-LUZB-", "JAH Uzbek Language Archivist",
    _role("JAH Uzbek Language Archivist"),
    CITATION, "public")
DBCFG["language-uzbek-signature"] = _cfg(
    "language-uzbek-signature", "The Uzbek to English Signature Database",
    "His original Signature Uzbek Method: every suffix a caravan seal, every sentence a road well traveled - the full ladder from the language overview "
    "through the script, sounds, words, and grammar, through daily-life sentences, to "
    "stories, idioms, registers, and conversations, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public record.",
    "language learning record", "JAH-LUZBS-", "JAH Uzbek Language Archivist (Signature)",
    "Uzbek language archivist - Signature editions: his original Signature Uzbek Method, every suffix a caravan seal, every sentence a road well traveled, "
    "clearly labeled Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to advanced; answers "
    "from many angles using only archive data from this system",
    CITATION, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["demo_key"] for e in ENTRIES}, "demo map misses entries"


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
        demo_fn = DEMOS[e["demo_key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["demo_data"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def _extract_scripts(page):
    scripts = []
    for m in re.finditer(r'<script([^>]*)>(.*?)</script>', page, re.S):
        attrs, body = m.group(1), m.group(2).strip()
        if re.search(r'\bsrc=', attrs):
            continue
        tm = re.search(r'type="([^"]+)"', attrs)
        if tm and tm.group(1) not in ("text/javascript", "application/javascript"):
            continue
        if body:
            scripts.append(body)
    return scripts


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
    for slug in ("language-uzbek", "language-uzbek-signature"):
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
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
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
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        scripts = _extract_scripts(page)
        assert scripts, "no inline scripts found in %s" % slug
        for i, body in enumerate(scripts):
            chk = "/tmp/languzbek_check_%d.js" % i
            with open(chk, "w", encoding="utf-8") as f:
                f.write(body)
            p = subprocess.run(["node", "--check", chk],
                               capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "page script %d failed node --check in %s: %s" % (i, slug, p.stderr[-500:])
        p = subprocess.run(["node", "--check", gen_path],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "gen js failed node --check in %s: %s" % (slug, p.stderr[-500:])
        print("page:  db/%s/index.html + gen-%s.js [%s] (js checked: %d page scripts + gen)"
              % (slug, slug, ", ".join(notes), len(scripts)), flush=True)

    fragment = {
        "public": {
            "slug": "language-uzbek",
            "name": "The Uzbek to English Database",
            "tagline": DBCFG["language-uzbek"]["tagline"],
            "record_kind": "language learning record",
            "id_prefix": "JAH-LUZB-",
            "ai_name": "JAH Uzbek Language Archivist",
            "local_index": SHARD_BASE + "/data/language-uzbek/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/language-uzbek/index.jsonl.gz",
            "chunk_pattern": "data/language-uzbek/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "language-uzbek-signature",
            "name": "The Uzbek to English Signature Database",
            "tagline": DBCFG["language-uzbek-signature"]["tagline"],
            "record_kind": "language learning record",
            "id_prefix": "JAH-LUZBS-",
            "ai_name": "JAH Uzbek Language Archivist (Signature)",
            "local_index": SHARD_BASE + "/data/language-uzbek-signature/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/language-uzbek-signature/index.jsonl.gz",
            "chunk_pattern": "data/language-uzbek-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("DONE: %d databases, %d records. Merger handles manifest/api/restamp/commit." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
