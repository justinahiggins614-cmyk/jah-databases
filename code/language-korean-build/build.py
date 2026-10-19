#!/usr/bin/env python3
"""Build the Korean Language databases for JAH Databases
(Manon language project, batch 2, ranks 11-20: Korean is rank 18 of the
100-language roster).

Verified 2026-10-17: roster slot language-korean / JAH-LKOR- (rank 18);
dedupe_gate.py pre-check over the whole system: zero collisions on all 68
titles (34 records x public + Signature editions); JAH-LKOR- and JAH-LKORS-
verified free in the manifest id_prefix values, in every shard index file,
and in the main-repo data dir.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-korean            - Korean Language Database
                               (public-harvest: real, fact-checked Korean
                               linguistic data - Hangul script, phonetics,
                               grammar core, 20 core phrases with
                               romanization, 8 conversation starters, 8
                               sample sentences with breakdowns; every
                               record carries Hangul + romanization +
                               English per the shared 34-record language
                               template; standard references ISO 639-1
                               (ko) / ISO 639-3 (kor); Revised
                               Romanization of Korean (2000); McCune-
                               Reischauer; Yale romanization;
                               Hunminjeongeum (1446); Unicode Hangul
                               syllables U+AC00-U+D7A3; TOPIK framework;
                               National Institute of Korean Language)
  language-korean-signature  - Korean Language Signature Database
                               (his original Signature Korean Method:
                               every sound a signature tone, every
                               syllable block a sealed mark, grammar the
                               covenant order of his system; src
                               signature, titles suffixed " (Signature
                               Edition)", never presented as authentic
                               public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

ID prefixes: JAH-LKOR- (public) and JAH-LKORS- (signature), verified free
(zero hits for JAH-LKOR and JAH-LKORS in manifest id_prefix values, all
shard index files, and the main-repo data dir).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_korean.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes - the merger handles those. It only writes db/language-korean[/-signature]/,
code/language-korean-build/, the shard data dirs, and the fragment file.

Never the words "bat belt" anywhere. No website references. No Facebook.
Nothing hate-adjacent, profane, or inappropriate; no religious talk.
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
FRAGMENTS = "/home/hatch/workspace/hidden_files/missing-builds/fragments"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_korean import ENTRIES, SIG_TAIL
from demos_language_korean import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Korean Method: "
                "every sound a signature tone, every syllable block a sealed "
                "mark, grammar the covenant order of his system, the full "
                "ladder from Hangul and pronunciation through words and "
                "grammar to stories and real conversations, reframed as "
                "Signature science. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Korean linguistic data: "
                "the Korean language (한국어, hangugeo), Hangul script, "
                "phonetics, grammar core, core vocabulary with sentences, "
                "numbers and time, greetings, verb tenses, idioms, registers, "
                "and full bilingual conversations - every record carrying "
                "Hangul plus romanization plus English, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, Hangul writing system, pronunciation and "
              "phonology, core nouns, core verbs, adjectives and adverbs, "
              "pronouns, numbers dates and time, greetings and everyday "
              "phrases, grammar essentials) -> Compounded (home and family, "
              "food and cooking, travel and directions, work and school, "
              "health and body, emotions and feelings, nature and weather, "
              "shopping and money, friendship and social life, technology "
              "and communication, verb tenses, questions and answers, "
              "commands and requests) -> Advanced (descriptions, three "
              "stories, idioms and proverbs, formal and polite registers, "
              "compound and complex sentences, three conversations, mastery "
              "review and full reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Hangul, pronunciation, nouns, verbs, adjectives, pronouns, numbers, greetings, grammar, tenses, idioms, conversations...",
        "chat_ph": "Ask about the Korean language...",
        "archive_blurb": ("Seeded %s Korean language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Korean language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Korean - from Hangul letters and sounds through words, grammar, and everyday phrases to stories and real conversations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "language-lesson", "gen_demo_kind": "language-demo",
        "source": source,
    }

CIT_PUB = ("Korean linguistics (standard references: ISO 639-1:2002 code "
           "ko; ISO 639-3:2007 code kor; Revised Romanization of Korean, "
           "Ministry of Culture and Tourism 2000; McCune G M, Reischauer "
           "E O. The Romanization of the Korean Language. 1939; Martin "
           "S E. Yale romanization; Hunminjeongeum, promulgated 1446 by "
           "King Sejong the Great; The Unicode Standard, Hangul Syllables "
           "U+AC00-U+D7A3; Test of Proficiency in Korean (TOPIK), National "
           "Institute of International Education; National Institute of "
           "Korean Language, Standard Korean Language Dictionary; Sohn "
           "H-M. The Korean Language. Cambridge University Press; 1999; "
           "Lee I, Ramsey S R. The Korean Language. SUNY Press; 2000).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Korean "
                     "Method - every sound a signature tone, every syllable "
                     "block a sealed mark - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-korean"] = _cfg(
    "language-korean", "Korean Language Database",
    "Learn Korean from the ground up: real, fact-checked Korean linguistic "
    "data - Hangul script, pronunciation, core vocabulary with sentences, "
    "grammar, verb tenses, idioms, registers, and full bilingual "
    "conversations. Every record carries Hangul plus romanization plus "
    "English, taught progressively along the ladder.",
    "language learning record", "JAH-LKOR-", "JAH Korean Language Tutor",
    "korean language tutor - teaching Korean from Hangul letters and "
    "sounds through words, grammar, and everyday phrases to stories and "
    "real conversations; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, how-to - using "
    "only archive data from this system",
    CIT_PUB, "public")
DBCFG["language-korean-signature"] = _cfg(
    "language-korean-signature", "Korean Language Signature Database",
    "His original Signature Korean Method: every sound a signature tone, "
    "every syllable block a sealed mark, grammar the covenant order of his "
    "system. The full ladder from Hangul and pronunciation through words "
    "and grammar to stories and real conversations, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "language learning record", "JAH-LKORS-", "JAH Korean Language Tutor (Signature)",
    "korean language tutor - Signature editions: his original Signature "
    "Korean Method, every sound a signature tone and every syllable block "
    "a sealed mark, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, how-to - using "
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


def write_fragment(built):
    frag = {}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        key = "signature" if slug.endswith("-signature") else "public"
        idx = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        frag[key] = {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"], "local_index": idx,
            "record_count": len(recs), "status": "live",
            "full_records": len(recs), "index": idx,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if key == "signature" else "public-harvest",
        }
    os.makedirs(FRAGMENTS, exist_ok=True)
    fpath = os.path.join(FRAGMENTS, "language-korean.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return fpath


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
    for slug in ("language-korean", "language-korean-signature"):
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
        assert "public-synthetic-intelligence" not in page, "slug leftover in %s" % slug
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
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    fpath = write_fragment(built)
    print("fragment: %s" % fpath, flush=True)
    print("built %d databases, %d records; manifest/api.json untouched (merger handles)" % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
