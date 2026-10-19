#!/usr/bin/env python3
"""Build the Persian Language databases for JAH Databases
(Language project 2026-10-17, batch 2: roster ranks 11-20 - this builder
owns rank 20, Persian).

Verified 2026-10-17: RAW SWEEP over the full manifest (id_prefix values)
PLUS every shard index in jah-databases-data-1: zero hits for JAH-LFAS-
or JAH-LFASS-. Dedupe pre-check on all 68 candidate titles vs the whole
system: zero collisions, zero refusals.

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-persian              - Persian Language Database
                                  (public-harvest: real, fact-checked
                                  Persian linguistic data - farsi, an
                                  Indo-European language of the Iranian
                                  branch; every record carries Persian
                                  script + transliteration + English;
                                  standard references Lazard A Grammar of
                                  Contemporary Persian 1992; Windfuhr
                                  Persian Grammar 1979; Thackston An
                                  Introduction to Persian 4th ed 2009;
                                  Mahootian Persian 1997; Beeman Language,
                                  Status, and Power in Iran 1986;
                                  Ethnologue 27th ed 2024; Academy of
                                  Persian Language and Literature
                                  orthography; Dehkhoda dictionary)
  language-persian-signature    - Persian Language Signature Database
                                  (his original Signature Language Method:
                                  every language a covenant of meaning,
                                  every word a signed seal of its people,
                                  the ladder the oath between learner and
                                  tongue; src signature, titles suffixed
                                  " (Signature Edition)", never presented
                                  as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LFAS- (public) and JAH-LFASS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_language_persian.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), prints an
ENTRY-CHECK marker that this build verifies verbatim against the entry
text, and ends with the OK marker; the build machine-executes all 68 demos.

SCOPE: this builder writes ONLY db/language-persian[/-signature],
code/language-persian-build, the data-1 shards, and the fragment file.
It NEVER touches data/manifest.json, api.json, index.html, README.md, or
docs/AI_ACCESS.md, and NEVER commits or pushes - the merger handles those.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk anywhere in these records.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/language-persian.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_persian import ENTRIES, SIG_TAIL
from demos_language_persian import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Language "
                "Method: every language a covenant of meaning, every word a "
                "signed seal of its people, the ladder the oath between "
                "learner and tongue. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Persian language "
                "teaching: farsi, an Indo-European language of the Iranian "
                "branch, written right to left in the Perso-Arabic script - "
                "every record carrying Persian script, transliteration, and "
                "English translation with example sentences, organized in "
                "the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation, core nouns, "
              "core verbs, adjectives and adverbs, pronouns, numbers and "
              "time, greetings, grammar essentials) -> Compounded (home and "
              "family, food and cooking, travel and directions, work and "
              "school, health and body, emotions, nature and weather, "
              "shopping and money, friendship and social life, technology, "
              "verb tenses, questions and answers, commands and requests, "
              "descriptions) -> Advanced (three short stories, idioms and "
              "proverbs, formal and polite registers, complex sentences, "
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
        "search_ph": "Search Persian alphabet, pronunciation, nouns, verbs, adjectives, pronouns, numbers, greetings, grammar, tenses, idioms, proverbs, conversations...",
        "chat_ph": "Ask about Persian language...",
        "archive_blurb": ("Seeded %s Persian language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Persian language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Persian - from the alphabet, sounds, and script through nouns, verbs, adjectives, pronouns, numbers, greetings, and grammar, to tenses, questions, commands, descriptions, stories, idioms, registers, and conversations." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "persian-lesson", "gen_demo_kind": "persian-demo",
        "source": source,
    }

CIT_PUB = ("Persian linguistics (standard references: Lazard G. A Grammar "
           "of Contemporary Persian. Mazda Publishers; 1992; Windfuhr G L. "
           "Persian Grammar: History and State of its Study. Mouton de "
           "Gruyter; 1979; Thackston W M. An Introduction to Persian. 4th "
           "ed. IBEX Publishers; 2009; Mahootian S. Persian. Routledge; "
           "1997; Beeman W O. Language, Status, and Power in Iran. Indiana "
           "University Press; 1986; Ethnologue: Languages of the World. 27th "
           "ed. SIL International; 2024; Academy of Persian Language and "
           "Literature (Farhangestan). Dastur-e xatt-e farsi - official "
           "Persian orthography; Dehkhoda A A. Loghatname-ye Dehkhoda. "
           "University of Tehran Press; ISO 639-1:1988 (fa), ISO "
           "639-3:2007 (fas)).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Language Method - every language a covenant of "
                     "meaning, every word a signed seal of its people - "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-persian"] = _cfg(
    "language-persian", "Persian Language Database",
    "Learn Persian (farsi): real, fact-checked Persian language teaching - "
    "34 ladder-ordered records from the alphabet, sounds, and script through "
    "core vocabulary, grammar, and verb tenses to stories, idioms, registers, "
    "and conversations. Every record carries Persian script, "
    "transliteration, and English with example sentences.",
    "language learning record", "JAH-LFAS-", "JAH Persian Language Tutor",
    "persian language tutor - teaching Persian from the alphabet, sounds, "
    "and script through core vocabulary, grammar, and verb tenses to "
    "stories, idioms, registers, and conversations; answers from many "
    "angles - definition, example, pronunciation, usage, grammar, culture - "
    "using only archive data from this system",
    CIT_PUB, "public-harvest")
DBCFG["language-persian-signature"] = _cfg(
    "language-persian-signature", "Persian Language Signature Database",
    "His original Signature Language Method: every language a covenant of "
    "meaning, every word a signed seal of its people, the ladder the oath "
    "between learner and tongue. The full Persian ladder - alphabet, sounds, "
    "words, grammar, tenses, stories, idioms, registers, conversations - "
    "reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "language learning record", "JAH-LFASS-",
    "JAH Persian Language Tutor (Signature)",
    "persian language tutor - Signature editions: his original Signature "
    "Language Method, every language a covenant of meaning and every word "
    "a signed seal of its people, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, pronunciation, usage, grammar, "
    "culture - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"

# JS hygiene: apostrophe-free ai/role/greet/search strings
for _slug, _c in DBCFG.items():
    for _k in ("ai", "role", "greet", "search_ph"):
        assert "'" not in _c[_k], "apostrophe in %s.%s" % (_slug, _k)


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


def cross_check(slug, recs):
    """Verify every demo's ENTRY-CHECK marker verbatim against its entry text."""
    n = 0
    for r in recs:
        e = next(e for e in ENTRIES if e["name"] == r["name"])
        text = (e["description"] + "\n" + e["how_it_works"] + "\n"
                + "\n".join(e["key_points"]))
        prog = r["demo"]["program"]
        m = re.search(r'ENTRY-CHECK: ([^"\n]*)', prog)
        assert m, "no ENTRY-CHECK marker in %s" % r["id"]
        chk = m.group(1)
        assert chk in text, "ENTRY-CHECK mismatch in %s: %r" % (r["id"], chk)
        n += 1
    print("cross-check: %d/%d ENTRY-CHECK markers verified verbatim vs entry text (%s)"
          % (n, len(recs), slug), flush=True)


def write_fragment(built):
    pub_i = ("%s/data/language-persian/index.jsonl.gz" % SHARD_BASE)
    sig_i = ("%s/data/language-persian-signature/index.jsonl.gz" % SHARD_BASE)
    frag = {
        "public": {
            "slug": "language-persian",
            "name": "Persian Language Database",
            "tagline": DBCFG["language-persian"]["tagline"],
            "record_kind": "language learning record",
            "id_prefix": "JAH-LFAS-",
            "ai_name": "JAH Persian Language Tutor",
            "local_index": pub_i,
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": pub_i,
            "chunk_pattern": "data/language-persian/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "language-persian-signature",
            "name": "Persian Language Signature Database",
            "tagline": DBCFG["language-persian-signature"]["tagline"],
            "record_kind": "language learning record",
            "id_prefix": "JAH-LFASS-",
            "ai_name": "JAH Persian Language Tutor (Signature)",
            "local_index": sig_i,
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": sig_i,
            "chunk_pattern": "data/language-persian-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, ensure_ascii=False, indent=2)
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
    for slug in ("language-persian", "language-persian-signature"):
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
        n = nb.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            assert "ENTRY-CHECK:" in p.stdout, "demo no ENTRY-CHECK %s" % r["id"]
        cross_check(slug, recs)
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
        assert "mergePanel" in page, "merge panel missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
        assert "universal-build" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        assert DBCFG[slug]["name"] in page, "db name missing in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            tier = {"foundations": "Foundations", "compounded": "Compounded",
                    "advanced": "Advanced"}[r["ladder_tier"]]
            topics.setdefault(tier, []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "template leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)

    # NOTE (concurrency rule): manifest.json, api.json, index.html, README.md,
    # docs/AI_ACCESS.md are owned by the merger. This build does NOT touch
    # them and does NOT commit or push.
    print("merger entries (for the merger only - not written by this build):")
    for slug in built:
        print("  " + json.dumps(nb.manifest_entry(slug, len(built[slug])), ensure_ascii=False))
    print("NEXT: merger runs restamp, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
