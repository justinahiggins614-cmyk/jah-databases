#!/usr/bin/env python3
"""Build the Catalan Language database pair for JAH Databases (batch 9).

Dedupe gate: 'catalan' zero hits across the full manifest; 'JAH-LCAT-' /
'JAH-LCATS-' verified free: zero hits in manifest id_prefix values and zero
hits in shard record IDs (checked with code/dedupe_gate.py BEFORE
authoring).

Two NEW databases, 34 ladder-ordered records each:
  language-catalan            - The Catalan Language Database (public-harvest)
  language-catalan-signature  - The Catalan Language Signature Database
                                (signature)

34 records each, ladder-ordered 1-34 (foundations 1-10 / compounded 11-21 /
advanced 22-34).

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/language-catalan/index.html + gen-language-catalan.js
              db/language-catalan-signature/index.html + gen-...js
  shard repo: data/language-catalan/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/language-catalan-signature/... (same)
  build dir : code/language-catalan-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/language-catalan.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/language-catalan.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_catalan import ENTRIES, SIG_TAIL, LANG
from demos_language_catalan import DEMOS
sys.path.insert(0, os.path.join(REPO, "code", "lang-batch9-common"))
import langkit

# ---------------------------------------------------------------- DB config

SIG_FLAVOR = "every letter a sworn sign of the Catalan lands, every verb a living action, every proverb a covenant of the ancestors"
PUB_DETAIL = "the language overview, the Latin writing system, pronunciation and phonology, core nouns verbs adjectives and adverbs with sentences, pronouns, numbers and time, greetings, grammar essentials, themed sentence sets for daily life, verb tenses, questions and answers, commands and requests, descriptions, stories, idioms, formal and polite registers, complex sentences, conversations, and a mastery review"
SCRIPT_PHRASE = "the Latin alphabet with ç, ny, and l·l"
SCRIPT_SHORT = "Latin script plus English translation"
ROLE_DETAIL = "teaching Catalan from the alphabet and sounds through core vocabulary, grammar, and everyday sentences to stories, idioms, registers, and conversations"

def _cfg(slug, name, tagline, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature Catalan "
                "Method: " + SIG_FLAVOR + ", the whole language taught as "
                "Signature science. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Catalan language "
                "teaching: " + PUB_DETAIL + " - every record carrying "
                "Catalan content in " + SCRIPT_SHORT + " plus example "
                "sentences.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation and "
              "phonology, core nouns, core verbs, adjectives and adverbs, "
              "pronouns, numbers and time, greetings, grammar essentials) "
              "-> Compounded (home and family, food and cooking, travel "
              "and directions, work and school, health and body, emotions "
              "and feelings, nature and weather, shopping and money, "
              "friendship and social life, technology and communication, "
              "verb tenses in sentences) -> Advanced (questions and "
              "answers, commands and requests, descriptions, three "
              "stories, idioms and proverbs, formal and polite registers, "
              "compound and complex sentences, three conversations, "
              "mastery review and full reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": "language learning record",
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Catalan letters, words, verbs, tenses, phrases, grammar, dialogues...",
        "chat_ph": "Ask about Catalan...",
        "archive_blurb": ("Seeded %s Catalan language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Catalan language studies. Seeded archive records are the authoritative entries.",
        "greet": ("I am the %s. Ask me about Catalan - from " + SCRIPT_PHRASE + " and sounds through core words, grammar, and everyday sentences to stories, idioms, and conversations.") % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "catalan-study", "gen_demo_kind": "catalan-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["language-catalan"] = _cfg(
    "language-catalan", "The Catalan Language Database",
    "Learn Catalan from the ground up: the language overview, " + SCRIPT_PHRASE + ", "
    "pronunciation and phonology, core vocabulary with sentences, grammar essentials, "
    "and themed sentence sets for daily life - every record carrying Catalan in "
    + SCRIPT_SHORT + " plus example sentences, taught progressively along the ladder.",
    "JAH-LCAT-", "JAH Catalan Language Archivist",
    "Catalan language archivist - " + ROLE_DETAIL + "; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, "
    "pronunciation, usage, grammar, culture - using only archive data from "
    "this system",
    "public")
DBCFG["language-catalan-signature"] = _cfg(
    "language-catalan-signature", "The Catalan Language Signature Database",
    "His original Signature Catalan Method: " + SIG_FLAVOR + " - the full ladder from the language "
    "overview through the script, sounds, words, and grammar, through "
    "daily-life sentences, to stories, idioms, registers, and conversations, "
    "reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "JAH-LCATS-", "JAH Catalan Language Archivist (Signature)",
    "Catalan language archivist - Signature editions: his original "
    "Signature Catalan Method, " + SIG_FLAVOR + ", clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles using only archive data from this "
    "system",
    "signature")

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
    """Return list of inline <script> (non-src, JS only) bodies for node --check."""
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
    for slug in ("language-catalan", "language-catalan-signature"):
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
        # content screen: report hits for manual context review
        hits = langkit.screen_records(recs)
        if hits:
            print("  content-screen hits in %s:" % slug, flush=True)
            for rid, field, term, snip in hits:
                print("    %s [%s] term=%r ctx=...%s..." % (rid, field, term, snip), flush=True)
            raise SystemExit("content screen flagged terms - review required in %s" % slug)
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
        # JS hygiene: node --check on extracted page scripts and gen-*.js
        scripts = _extract_scripts(page)
        assert scripts, "no inline scripts found in %s" % slug
        for i, body in enumerate(scripts):
            with open("/tmp/langcatalan_check_%d.js" % i, "w", encoding="utf-8") as f:
                f.write(body)
            p = subprocess.run(["node", "--check", "/tmp/langcatalan_check_%d.js" % i],
                               capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "page script %d failed node --check in %s: %s" % (i, slug, p.stderr[-500:])
        p = subprocess.run(["node", "--check", gen_path],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "gen js failed node --check in %s: %s" % (slug, p.stderr[-500:])
        print("page:  db/%s/index.html + gen-%s.js [%s] (js checked: %d page scripts + gen)"
              % (slug, slug, ", ".join(notes), len(scripts)), flush=True)

    fragment = {
        "public": {
            "slug": "language-catalan",
            "name": "The Catalan Language Database",
            "tagline": DBCFG["language-catalan"]["tagline"],
            "record_kind": "language learning record",
            "id_prefix": "JAH-LCAT-",
            "ai_name": "JAH Catalan Language Archivist",
            "local_index": SHARD_BASE + "/data/language-catalan/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/language-catalan/index.jsonl.gz",
            "chunk_pattern": "data/language-catalan/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "language-catalan-signature",
            "name": "The Catalan Language Signature Database",
            "tagline": DBCFG["language-catalan-signature"]["tagline"],
            "record_kind": "language learning record",
            "id_prefix": "JAH-LCATS-",
            "ai_name": "JAH Catalan Language Archivist (Signature)",
            "local_index": SHARD_BASE + "/data/language-catalan-signature/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/language-catalan-signature/index.jsonl.gz",
            "chunk_pattern": "data/language-catalan-signature/chunks/chunk-NNNN.jsonl.gz",
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
