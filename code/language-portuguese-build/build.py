#!/usr/bin/env python3
"""Build the Portuguese to English databases for JAH Databases
(Manon's language orders #10-11, 2026-10-17, roster rank 7).

Roster-verified free slug. Whole-system dedupe gate checked all 68 titles
before authoring: zero refusals.

Two databases, 34 ladder-ordered records each:

  language-portuguese            - The Portuguese to English Database
                                   (public-harvest: real, fact-checked
                                   Portuguese language teaching - every record
                                   carrying Portuguese content with English
                                   translation and example sentences;
                                   ISO 639-1 pt / 639-3 por; Indo-European >
                                   Italic > Romance; ~236M native speakers;
                                   1990 Acordo Ortografico; Nova Gramatica do
                                   Portugues Contemporaneo (Cunha e Cintra);
                                   Dicionario Houaiss; Instituto Camoes
                                   Referencial)
  language-portuguese-signature  - The Portuguese to English Signature Database
                                   (his original Signature Language Method:
                                   every word a covenant between sound and
                                   meaning, every sentence a signed contract
                                   of understanding, the learner's voice the
                                   seal; src signature, titles suffixed
                                   " (Signature Edition)", never presented
                                   as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced, ladder 1-34); the shard index
is written in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LPOR- (public) and JAH-LPORS- (signature), verified free
in the manifest id_prefix values and in every shard index file
(jah-databases-data-1): zero hits for both.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_portuguese.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. It only writes:
  db/language-portuguese/ + db/language-portuguese-signature/
    (index.html + gen-*.js each)
  code/language-portuguese-build/  (this build, entries, demos)
  <shard>/data/language-portuguese/ + -signature/
    (index.jsonl.gz + chunks/chunk-0000.jsonl.gz)
  ~/workspace/hidden_files/missing-builds/fragments/language-portuguese.json

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/language-portuguese.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_portuguese import ENTRIES, SIG_TAIL
from demos_language_portuguese import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Language Method: "
                "every word a covenant between sound and meaning, every "
                "sentence a signed contract of understanding, the learner's "
                "voice the seal. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Portuguese language "
                "teaching: every record carries Portuguese content with "
                "English translation and example sentences - overview, "
                "writing system, pronunciation, core nouns, core verbs, "
                "adjectives and adverbs, pronouns, numbers and time, "
                "greetings, grammar essentials, themed sentence sets (home, "
                "food, travel, work, health, emotions, nature, shopping, "
                "friendship, technology), verb tenses, questions and answers, "
                "commands, descriptions, stories, idioms, registers, complex "
                "sentences, conversations, and a full mastery reference - "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation and "
              "phonology, core nouns, core verbs, adjectives and adverbs, "
              "pronouns, numbers and time, greetings and everyday phrases, "
              "grammar essentials) -> Compounded (home and family, food and "
              "cooking, travel and directions, work and school, health and "
              "body, emotions and feelings, nature and weather, shopping and "
              "money, friendship and social life, technology and "
              "communication, verb tenses in sentences, questions and "
              "answers, commands and requests, descriptions of people and "
              "places) -> Advanced (three stories, idioms and proverbs, "
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
        "search_ph": "Search Portuguese words, verbs, grammar, phrases, stories, idioms, conversations, pronunciation, numbers...",
        "chat_ph": "Ask about Portuguese...",
        "archive_blurb": ("Seeded %s Portuguese language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, ladder, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Portuguese language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Portuguese - from the alphabet, sounds, nouns, verbs, adjectives, pronouns, numbers, and greetings, through home, food, travel, work, health, emotions, nature, shopping, friendship, and technology sentences, to verb tenses, questions, commands, descriptions, stories, idioms, registers, complex sentences, conversations, and the full mastery reference." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "portuguese-language-study", "gen_demo_kind": "portuguese-language-demo",
        "source": source,
    }

CIT_PUB = ("Portuguese language (standard references: Acordo Ortografico da "
           "Lingua Portuguesa, 1990; Cunha C, Cintra L F L. Nova Gramatica do "
           "Portugues Contemporaneo. LEXIKON Editora Digital; 2013; Mateus M "
           "H M et al. Gramatica da Lingua Portuguesa. 7th ed. Caminho; 2006; "
           "Houaiss A. Dicionario Houaiss da Lingua Portuguesa; Instituto "
           "Camoes. Referencial Camoes Portugues Lingua Estrangeira. Lisbon; "
           "2017; ISO 639-1:1988 (pt); ISO 639-2:1998 (por)).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Language "
                     "Method - every word a covenant between sound and "
                     "meaning, clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-portuguese"] = _cfg(
    "language-portuguese", "The Portuguese to English Database",
    "Learn Portuguese step by step: real, fact-checked Portuguese teaching - "
    "every record carrying Portuguese content with English translation and "
    "example sentences, from the alphabet and sounds through core vocabulary "
    "and grammar to stories, idioms, and full conversations, taught "
    "progressively along the ladder.",
    "language learning record", "JAH-LPOR-", "JAH Portuguese to English Archivist",
    "portuguese to english archivist - teaching Portuguese through the "
    "teaching ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["language-portuguese-signature"] = _cfg(
    "language-portuguese-signature", "The Portuguese to English Signature Database",
    "His original Signature Language Method: every word a covenant between "
    "sound and meaning, every sentence a signed contract of understanding, "
    "the learner's voice the seal. The full ladder from the alphabet through "
    "core vocabulary and grammar to stories, idioms, and conversations, "
    "reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "language learning record", "JAH-LPORS-", "JAH Portuguese to English Archivist (Signature)",
    "portuguese to english archivist - Signature editions: his original "
    "Signature Language Method, every word a covenant between sound and "
    "meaning, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
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
    for pos, (_, e) in enumerate(ordered, start=1):
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
            "ladder": pos,
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


def node_check(path):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True, timeout=60)
    assert p.returncode == 0, "node --check failed for %s: %s" % (path, p.stderr[-500:])
    return True


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

    # ---- whole-system dedupe pre-check on all 68 titles (before authoring)
    refused = []
    for e in ENTRIES:
        for slug, title in (("language-portuguese", e["name"]),
                            ("language-portuguese-signature", e["name"] + " (Signature Edition)")):
            hits = [h for h in base.GATE.check(slug, title)]
            if hits:
                refused.append((title, hits))
    print("dedupe pre-check: 68 titles vs whole system, refusals: %d" % len(refused), flush=True)
    for t, h in refused:
        print("  REFUSED %s -> %s" % (t, h), flush=True)
    assert not refused, "dedupe refusals must be zero"

    built = {}
    for slug in ("language-portuguese", "language-portuguese-signature"):
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
                      "src", "ladder_rank", "ladder_tier", "ladder", "demo"):
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

    # ---- machine-execute all 68 demos
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    # ---- pages + generator JS
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
        # node --check extracted inline page scripts
        with open(ppath, encoding="utf-8") as f:
            psrc = f.read()
        scripts = [b for b in re.findall(r"<script(?![^>]*src=)(?![^>]*ld\+json)[^>]*>(.*?)</script>", psrc, re.S)]
        for si, body in enumerate(scripts):
            if body.strip():
                sp = "/tmp/lpor-page-%s-%d.js" % (slug, si)
                with open(sp, "w", encoding="utf-8") as f:
                    f.write(body)
                node_check(sp)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        node_check(gpath)
        # apostrophe-free hygiene on role/ai_name/greet/search strings
        for k in ("ai", "role", "greet", "search_ph", "chat_ph"):
            assert "'" not in DBCFG[slug][k], "apostrophe in %s.%s" % (slug, k)
        print("page:  db/%s/index.html + gen-%s.js [%s] node --check clean" % (slug, slug, ", ".join(notes)), flush=True)

    # ---- fragment for the merger
    def frag_entry(slug, ai_name, source):
        cfg = DBCFG[slug]
        return {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": ai_name,
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": source,
        }
    fragment = {
        "public": frag_entry("language-portuguese", "JAH Portuguese to English Archivist", "public-harvest"),
        "signature": frag_entry("language-portuguese-signature",
                                "JAH Portuguese to English Archivist (Signature)", "signature"),
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("databases built: 2, records: %d (34 public + 34 signature)" % total)
    print("NOTE: manifest/api/index.html/README/docs untouched - merger handles those. Do NOT claim live.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
