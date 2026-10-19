#!/usr/bin/env python3
"""Build the German Language databases for JAH Databases
(language project 2026-10-17, batch 2, roster rank 11).

Roster: language-german (rank 11) / language-german-signature (rank 12).
Slug verified free in manifest and db/ tree. ID prefixes JAH-LDEU- /
JAH-LDEUS- verified zero hits in manifest id_prefix values AND in every
shard index file. 68 titles run through code/dedupe_gate.py against the
whole system before authoring: zero refusals.

Creates two NEW databases, 34 ladder-ordered records each:

  language-german             - German Language Database
                                (public-harvest: real, fact-checked German
                                linguistics - every record carrying German
                                content with English translation and example
                                sentences, taught progressively along the
                                teaching ladder from overview to mastery
                                review)
  language-german-signature   - German Language Signature Database
                                (his original Signature Word Method:
                                every word a signed instrument of meaning,
                                grammar the covenant binding words into
                                truth, the learner's tongue the seal;
                                src signature, titles suffixed " (Signature
                                Edition)", never presented as authentic
                                public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical/linguistic cores: all hand-authored 2026-10-17, machine-verified
by the demos (see demos_language_german.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. Only writes: db/language-german/,
db/language-german-signature/, shard dirs under jah-databases-data-1,
and the merger fragment.

Screened: no hate-adjacent, profane, or inappropriate content; no
religious talk; nothing on neutralizing/defeating military or
defense-grade systems.

Never the words "bat belt" anywhere. No website references. No Facebook.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/language-german.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_german import ENTRIES, SIG_TAIL
from demos_language_german import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Word Method: "
                "every word a signed instrument of meaning, grammar the "
                "covenant that binds words into truth, and the learner's "
                "tongue the seal. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked German linguistics: "
                "Deutsch, the West Germanic language of Germany, Austria, "
                "Switzerland, Liechtenstein, Luxembourg, and Belgium - "
                "every record carrying German content with English "
                "translation and example sentences, taught progressively "
                "along the teaching ladder, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system and alphabet, "
              "pronunciation and phonology, core nouns, core verbs, "
              "adjectives and adverbs, pronouns, numbers and time, "
              "greetings and everyday phrases, grammar essentials) -> "
              "Compounded (home and family, food and cooking, travel and "
              "directions, work and school, health and body, emotions and "
              "feelings, nature and weather, shopping and money, friendship "
              "and social life, technology and communication) -> Advanced "
              "(verb tenses in sentences, questions and answers, commands "
              "and requests, descriptions, three stories, idioms and "
              "proverbs, formal and polite registers, compound and complex "
              "sentences, three conversations, mastery review and full "
              "reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: German "
                  "content with English translation, description, how it "
                  "works, key points, requirements, standards, citations, "
                  "and a working demonstration program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search German alphabet, pronunciation, nouns, verbs, adjectives, pronouns, numbers, greetings, grammar, tenses, idioms, proverbs, dialogues...",
        "chat_ph": "Ask about German...",
        "archive_blurb": ("Seeded %s German language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled German language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about German - from the alphabet and pronunciation through nouns, verbs, adjectives, pronouns, numbers, greetings, and grammar essentials, through home, food, travel, work, health, emotions, nature, shopping, friendship, and technology, to tenses, questions, commands, idioms, registers, complex sentences, and full conversations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "language-lesson", "gen_demo_kind": "language-demo",
        "source": source,
    }

CIT_PUB = ("German linguistics (standard references: Dudenredaktion. "
           "Duden: Die deutsche Rechtschreibung. 28. Aufl. Berlin: "
           "Dudenverlag; 2020; Rat fuer deutsche Rechtschreibung; Grimm J, "
           "Grimm W. Deutsches Woerterbuch. Leipzig: Hirzel; 1854-1961; "
           "Eberhard DM, Simons GF, Fennig CD, eds. Ethnologue: Languages "
           "of the World. 28th ed. Dallas: SIL International; 2025; "
           "Durrell M. Hammer's German Grammar and Usage. 6th ed. London: "
           "Routledge; 2017; Goethe-Institut; Council of Europe CEFR).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Word "
                     "Method - every word a signed instrument of meaning, "
                     "grammar the covenant binding words into truth - "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-german"] = _cfg(
    "language-german", "German Language Database",
    "Learn German from the ground up: real, fact-checked German "
    "linguistics - Deutsch, the West Germanic language of Germany, "
    "Austria, Switzerland, Liechtenstein, Luxembourg, and Belgium - "
    "every record carrying German content with English translation and "
    "example sentences, taught progressively from alphabet to mastery "
    "review along the teaching ladder.",
    "language learning record", "JAH-LDEU-", "JAH German Language Tutor",
    "german language tutor - teaching German from the alphabet and "
    "pronunciation through core vocabulary and grammar essentials, "
    "through everyday life domains, to tenses, idioms, registers, complex "
    "sentences, and full conversations; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["language-german-signature"] = _cfg(
    "language-german-signature", "German Language Signature Database",
    "His original Signature Word Method applied to German: every word a "
    "signed instrument of meaning, grammar the covenant binding words "
    "into truth, the learner's tongue the seal. The full ladder from "
    "alphabet and pronunciation through core vocabulary and grammar to "
    "tenses, idioms, registers, and conversations, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "language learning record", "JAH-LDEUS-", "JAH German Language Tutor (Signature)",
    "german language tutor - Signature editions: his original Signature "
    "Word Method applied to German, every word a signed instrument of "
    "meaning and grammar the covenant binding words into truth, clearly "
    "labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, how-to - using "
    "only archive data from this system",
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


def _node_check(path):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True, timeout=60)
    assert p.returncode == 0, "node --check failed for %s: %s" % (path, p.stderr[-500:])


def _check_page_scripts(page_path):
    with open(page_path, "r", encoding="utf-8") as f:
        html = f.read()
    tags = re.findall(r"<script([^>]*)>(.*?)</script>", html, flags=re.S | re.I)
    blocks = []
    for attrs, body in tags:
        if re.search(r"\bsrc\s*=", attrs, re.I):
            continue
        m = re.search(r'\btype\s*=\s*["\']([^"\']+)["\']', attrs, re.I)
        if m and m.group(1).lower() not in ("text/javascript", "application/javascript", "module"):
            continue  # e.g. application/ld+json is JSON, not JS
        blocks.append(body)
    assert blocks, "no inline JS scripts found in %s" % page_path
    for i, b in enumerate(blocks):
        if not b.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
            tf.write(b)
            tp = tf.name
        try:
            _node_check(tp)
        finally:
            os.unlink(tp)
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

    # hygiene: apostrophe-free role/ai_name/greet/search strings
    for slug, cfg in DBCFG.items():
        for field in ("role", "ai", "greet", "search_ph"):
            assert "'" not in cfg[field], "apostrophe in %s.%s" % (slug, field)

    built = {}
    for slug in ("language-german", "language-german-signature"):
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
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        _node_check(gen_path)
        nscripts = _check_page_scripts(ppath)
        print("page:  db/%s/index.html + gen-%s.js [%s] (scripts checked: %d)"
              % (slug, slug, ", ".join(notes), nscripts), flush=True)

    # merger fragment
    tagline_pub = DBCFG["language-german"]["tagline"]
    tagline_sig = DBCFG["language-german-signature"]["tagline"]
    fragment = {
        "public": {
            "slug": "language-german",
            "name": "German Language Database",
            "tagline": tagline_pub,
            "record_kind": "language learning record",
            "id_prefix": "JAH-LDEU-",
            "ai_name": "JAH German Language Tutor",
            "local_index": SHARD_BASE + "/data/language-german/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/language-german/index.jsonl.gz",
            "chunk_pattern": "data/language-german/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "language-german-signature",
            "name": "German Language Signature Database",
            "tagline": tagline_sig,
            "record_kind": "language learning record",
            "id_prefix": "JAH-LDEUS-",
            "ai_name": "JAH German Language Tutor (Signature)",
            "local_index": SHARD_BASE + "/data/language-german-signature/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/language-german-signature/index.jsonl.gz",
            "chunk_pattern": "data/language-german-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("built %d records across 2 databases; manifest/api untouched (merger handles)." % total)
    print("NEXT: merger verifies, runs restamp_counts.py, commits + pushes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
