#!/usr/bin/env python3
"""Build the Spanish to English databases for JAH Databases
(language orders #10-11, roster rank 2).

Roster rank 2: language-spanish. Slug verified free in the manifest
(2,410 databases) and in all 812 shard index files. 68 titles (34
public + 34 Signature Edition) run through code/dedupe_gate.py against
the whole system before authoring: zero refusals.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-spanish             - The Spanish to English Database
                                 (public-harvest: real, fact-checked Spanish
                                 linguistics - every record carrying Spanish
                                 content with English translation and example
                                 sentences, taught progressively along the
                                 teaching ladder from overview to mastery
                                 review; standard references the Real
                                 Academia Espanola Diccionario de la lengua
                                 espanola 23rd ed. 2014, the Nueva gramatica
                                 de la lengua espanola 2009, the Ortografia
                                 de la lengua espanola 2010, the Instituto
                                 Cervantes El espanol en el mundo yearbook
                                 2023, Ethnologue 28th ed. 2025, and Nebrija
                                 1492)
  language-spanish-signature   - The Spanish to English Signature Database
                                 (his original Signature Word Method: every
                                 word a signed instrument of meaning,
                                 grammar the covenant binding words into
                                 truth, the learner's tongue the seal;
                                 src signature, titles suffixed " (Signature
                                 Edition)", clearly labeled Signature-made,
                                 never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LSPA- (public) and JAH-LSPAS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits
across all 812 index files).

Linguistic cores: all hand-authored 2026-10-17, machine-verified by the
demos (see demos_language_spanish.py): conjugation drills, stress-rule
checkers, gender classifiers, number-to-word converters, sentence-order
checkers, register classifiers, and vocabulary quizzes. Every demo prints
its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker; the build machine-executes
all 68 demos.

Screened: no hate-adjacent, profane, or inappropriate content; no
religious talk; nothing on neutralizing/defeating military or
defense-grade systems.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those.

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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_spanish import ENTRIES, SIG_TAIL
from demos_language_spanish import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Word Method: "
                "every word a signed instrument of meaning, grammar the "
                "covenant binding words into truth, the learners tongue "
                "the seal. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("Public records - real, fact-checked Spanish linguistics: "
                "about 485 million native speakers and about 600 million "
                "total speakers of this Indo-European Romance language "
                "(ISO es/spa), official in 20 countries - every record "
                "carrying Spanish content with English translation and "
                "example sentences, taught progressively along the ladder.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system and alphabet, "
              "pronunciation and phonology, core nouns, core verbs, "
              "adjectives and adverbs, pronouns, numbers and time, "
              "greetings and everyday phrases, grammar essentials) -> "
              "Compounded (home and family, food and cooking, travel and "
              "directions, work and school, health and body, emotions and "
              "feelings, nature and weather, shopping and money, friendship "
              "and social life, technology and communication, verb tenses "
              "in sentences, questions and answers, commands and requests, "
              "descriptions of people and places) -> Advanced (three "
              "ten-sentence stories in present, past, and future, idioms "
              "and proverbs, formal and polite registers, compound and "
              "complex sentences, three twenty-line bilingual "
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
        "search_ph": "Search alphabet, pronunciation, nouns, verbs, adjectives, pronouns, numbers, greetings, grammar, tenses, idioms, conversations...",
        "chat_ph": "Ask about Spanish...",
        "archive_blurb": ("Seeded %s Spanish to English records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Spanish language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Spanish - from the alphabet, sounds, nouns, verbs, adjectives, pronouns, numbers, greetings, and grammar, through everyday sentences for home, food, travel, work, health, emotions, nature, shopping, friendship, and technology, to verb tenses, questions, commands, stories, idioms, registers, complex sentences, and conversations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "spanish-language-study", "gen_demo_kind": "spanish-language-demo",
        "source": source,
    }

CIT_PUB = ("Spanish linguistics (standard references: Real Academia "
           "Espanola. Diccionario de la lengua espanola. 23rd ed. Madrid: "
           "Espasa; 2014; Real Academia Espanola y Asociacion de Academias "
           "de la Lengua Espanola. Nueva gramatica de la lengua espanola. "
           "Madrid: Espasa; 2009; Ortografia de la lengua espanola. "
           "Madrid: Espasa; 2010; Instituto Cervantes. El espanol en el "
           "mundo: Anuario del Instituto Cervantes. Madrid; 2023; "
           "Ethnologue: Languages of the World. 28th ed. Dallas: SIL "
           "International; 2025; Nebrija A de. Gramatica sobre la lengua "
           "castellana. Salamanca; 1492).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Word "
                     "Method - every word a signed instrument of meaning, "
                     "grammar the covenant binding words into truth - "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-spanish"] = _cfg(
    "language-spanish", "The Spanish to English Database",
    "Learn Spanish from the alphabet to fluent conversation: real, "
    "fact-checked Spanish linguistics - every record carrying Spanish "
    "content with English translation and example sentences, taught "
    "progressively along the ladder from overview to mastery review.",
    "language learning record", "JAH-LSPA-", "JAH Spanish to English Archivist",
    "spanish to english archivist - teaching Spanish from the alphabet "
    "through sounds, words, and grammar to fluent sentences and "
    "conversation; answers from many angles - definition, example, "
    "analogy, application, history, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["language-spanish-signature"] = _cfg(
    "language-spanish-signature", "The Spanish to English Signature Database",
    "His original Signature Word Method: every word a signed instrument "
    "of meaning, grammar the covenant binding words into truth, the "
    "learners tongue the seal. The full ladder from alphabet and sounds "
    "through words and sentences to stories, idioms, and conversation, "
    "reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "language learning record", "JAH-LSPAS-", "JAH Spanish to English Archivist (Signature)",
    "spanish to english archivist - Signature editions: his original "
    "Signature Word Method, every word a signed instrument of meaning "
    "and grammar the covenant binding words into truth, clearly labeled "
    "Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, how-to - using only archive "
    "data from this system",
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


def node_check_js(label, code):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False,
                                     encoding="utf-8") as f:
        f.write(code)
        path = f.name
    try:
        p = subprocess.run(["node", "--check", path],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "node --check failed for %s: %s" % (label, p.stderr[-600:])
    finally:
        os.unlink(path)


def check_page_scripts(slug, page):
    # check every inline classic script (skip ld+json and external src)
    n = 0
    for m in re.finditer(r'<script(?![^>]*src=)(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                         page, re.S | re.I):
        body = m.group(1).strip()
        if body:
            node_check_js("%s inline script #%d" % (slug, n), body)
            n += 1
    print("  node --check: %d inline page scripts clean" % n, flush=True)
    assert n > 0, "no inline scripts found in %s" % slug


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
    for slug in ("language-spanish", "language-spanish-signature"):
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
        check_page_scripts(slug, page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        node_check_js("gen-%s.js" % slug, gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    print("records built: %d databases, %d records (34 + 34)" % (len(built), total))
    print("NOTE: manifest.json / api.json untouched (merger owns them). No commit, no push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
