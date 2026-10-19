#!/usr/bin/env python3
"""Build The Hindi to English Database (language-hindi) and its Signature
edition (language-hindi-signature) for JAH Databases.

Manon language orders #10-11 (2026-10-17), roster rank 4. Follows the
shared per-language template (language-template.md) EXACTLY: 34
ladder-ordered records each (overview, Devanagari writing system,
phonology, core vocabulary with sentences, grammar essentials, themed
sentence sets, tenses, stories, idioms, register, complex sentences,
dialogues, mastery review). ladder_rank 1-10 non-decreasing,
ladder_tier foundations -> compounded -> advanced.

Public edition: real, fact-checked Hindi teaching (Devanagari +
transliteration + English + example sentences in every record).
Signature edition: the same ladder through the Signature lens, titles
suffixed " (Signature Edition)", src='signature', clearly labeled
Signature-made, never presented as authentic public record.

ID prefixes: JAH-LHIN- (public) and JAH-LHINS- (signature), verified
2026-10-17: zero hits in manifest id_prefix values AND in all 811
shard index files of jah-databases-data-1. Slug 'language-hindi' also
verified free in both. Dedupe pre-check (code/dedupe_gate.py) over the
whole system: zero collisions across all 68 titles.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or
pushes. A merger handles those. It only creates:
  db/language-hindi/ + db/language-hindi-signature/ (index.html + gen-*.js)
  code/language-hindi-build/ (this file, entries, demos)
  <data-1>/data/language-hindi[-signature]/ (index.jsonl.gz + chunks/)
  workspace/hidden_files/missing-builds/fragments/language-hindi.json

Numerical cores: all hand-authored 2026-10-17, machine-verified by the
demos (see demos_language_hindi.py). Every demo prints real computed
values, asserts tight bounds (never float exact-equality), and ends
with the OK marker; the build machine-executes all 68 demos and
cross-checks sampled Devanagari tokens from each demo against the
record text.

Screened 2026-10-17: nothing hate-adjacent, profane, or inappropriate;
no religious talk; nothing on neutralizing/defeating military or
defense-grade systems. Never the words "bat belt" anywhere. No website
references. No Facebook.
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
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAG = "/home/hatch/workspace/hidden_files/missing-builds/fragments/language-hindi.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_hindi import ENTRIES, SIG_TAIL
from demos_language_hindi import DEMOS

DEVA_RE = re.compile(r'[\u0900-\u097F]{2,}')

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature language method: "
                "the same real Hindi re-taught as his own language instrument, "
                "every lesson framed through the Signature lens. Clearly labeled "
                "Signature-made, never presented as an outside authority text.")
    pub_line = ("Public records - real, fact-checked Hindi teaching: every record "
                "carries Hindi in Devanagari plus transliteration plus English "
                "translation plus example sentences, from the language overview "
                "through the Devanagari writing system, pronunciation and "
                "phonology, core nouns verbs adjectives and adverbs, pronouns, "
                "numbers and time, greetings, and grammar essentials, through "
                "themed sentence sets for home, food, travel, work, health, "
                "emotions, nature, shopping, social life, and technology, to verb "
                "tenses, questions and answers, commands, descriptions, stories, "
                "idioms, formal registers, complex sentences, dialogues, and the "
                "full mastery review - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, Devanagari writing system, pronunciation and "
              "phonology, core nouns, core verbs, adjectives and adverbs, "
              "pronouns, numbers and time, greetings, grammar essentials) -> "
              "Compounded (themed sentence sets: home and family, food and "
              "cooking, travel and directions, work and school, health and body, "
              "emotions and feelings, nature and weather, shopping and money, "
              "friendship and social life, technology and communication) -> "
              "Advanced (verb tenses, questions and answers, commands and "
              "requests, descriptions, three stories, idioms and proverbs, "
              "formal and polite registers, compound and complex sentences, "
              "three dialogues, mastery review and full reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Hindi words, Devanagari script, pronunciation, verbs, nouns, grammar, tenses, idioms, stories, dialogues, phrases...",
        "chat_ph": "Ask about Hindi words, grammar, sentences...",
        "archive_blurb": ("Seeded %s Hindi to English records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder, ladder_rank, ladder_tier, record_kind, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Hindi language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Hindi - the Devanagari script, pronunciation, vocabulary, verbs, grammar, tenses, idioms, stories, dialogues, and everyday phrases - from first words to full conversation." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "hindi-lesson", "gen_demo_kind": "hindi-demo",
        "source": source,
    }

CIT_PUB = ("Hindi language references (standard references: McGregor, R. S. "
           "The Oxford Hindi-English Dictionary. Oxford University Press; 1993; "
           "Snell, Rupert & Weightman, Simon. Teach Yourself Hindi. Hodder & "
           "Stoughton; 2003; Shapiro, Michael C. Hindi. In: Cardona, George & "
           "Jain, Dhanesh (eds.) The Indo-Aryan Languages. Routledge; 2003; "
           "Ohala, Manjari. Hindi. In: Handbook of the International Phonetic "
           "Association. Cambridge University Press; 1999; ISO 639-1:2002 code "
           "hi; ISO 639-3:2007 code hin; Unicode Standard, Devanagari block "
           "U+0900-U+097F; ISO 15919:2001 transliteration).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature language "
                     "method - the same real Hindi re-taught through the "
                     "Signature lens, clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-hindi"] = _cfg(
    "language-hindi", "The Hindi to English Database",
    "Learn Hindi from first sounds to full conversation: real, fact-checked "
    "Hindi teaching with Devanagari script, transliteration, English "
    "translation, and example sentences in every record - overview, writing "
    "system, pronunciation, core vocabulary, grammar, themed sentence sets, "
    "tenses, stories, idioms, dialogues, and a full mastery review, taught "
    "progressively along the ladder.",
    "language learning record", "JAH-LHIN-", "JAH Hindi to English Archivist",
    "hindi to english archivist - teaching Hindi from first sounds to full "
    "conversation: Devanagari script, pronunciation and phonology, core "
    "vocabulary with sentences, grammar essentials, themed sentence sets, verb "
    "tenses, stories, idioms, registers, complex sentences, dialogues, and the "
    "mastery review; teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["language-hindi-signature"] = _cfg(
    "language-hindi-signature", "The Hindi to English Signature Database",
    "His original Signature language method: the same real Hindi re-taught as "
    "his own language instrument - every lesson framed through the Signature "
    "lens, from first sounds through the Devanagari script, vocabulary, "
    "grammar, and themed sentences, to tenses, stories, idioms, dialogues, and "
    "full mastery. Clearly labeled Signature-made, never presented as an "
    "outside authority text.",
    "language learning record", "JAH-LHINS-", "JAH Hindi to English Archivist (Signature)",
    "hindi to english archivist - Signature editions: his original Signature "
    "language method, the same real Hindi re-taught as his own language "
    "instrument through the Signature lens, clearly labeled Signature-made and "
    "never presented as an outside authority text; teaches progressively "
    "along the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, history, "
    "how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"

# JS hygiene: these strings land in page JS - apostrophe-free
for _c in DBCFG.values():
    for _k in ("ai", "role", "greet", "search_ph", "chat_ph"):
        assert "'" not in _c[_k], "apostrophe in %s" % _k


def _cross_check(rec, prog):
    toks = DEVA_RE.findall(prog)
    seen, sample = set(), []
    for t in toks:
        if t not in seen:
            seen.add(t)
            sample.append(t)
        if len(sample) == 6:
            break
    blob = rec["description"] + " " + rec["how_it_works"]
    for t in sample:
        assert t in blob, "demo token %r not in entry text for %s" % (t, rec["id"])
    return len(sample)


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        hits = [h for h in base.GATE.check(slug, title) if h[0] != slug]
        assert not hits, "dedupe refused (cross-db dupe): %s -> %s" % (title, hits)
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
            "ladder": e["ladder"],
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
            "record_kind": "language-lesson",
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
    for slug in ("language-hindi", "language-hindi-signature"):
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
                      "src", "ladder", "ladder_rank", "ladder_tier", "record_kind", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            assert r["record_kind"] == "language-lesson"
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

    checked = 0
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            checked += _cross_check(r, prog)
    print("demo execution: all %d demos ran OK; cross-checked %d Devanagari tokens vs entry text"
          % (total, checked), flush=True)

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

    # node --check on all page scripts and gen files
    for slug in built:
        ddir = os.path.join(REPO, "db", slug)
        for fn in ("index.html", "gen-%s.js" % slug):
            p = os.path.join(ddir, fn)
            with open(p, encoding="utf-8") as f:
                html = f.read()
            scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S) if fn.endswith(".html") else [html]
            for i, js in enumerate(scripts):
                if not js.strip():
                    continue
                tmp = "/tmp/langhin-check-%s-%d.js" % (slug.replace("/", "_"), i)
                with open(tmp, "w", encoding="utf-8") as f:
                    f.write(js)
                r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
                assert r.returncode == 0, "node --check failed %s#%d: %s" % (fn, i, r.stderr[-500:])
        print("node --check clean: db/%s" % slug, flush=True)

    # fragment for the merger
    frag = {
        "public": {
            "slug": "language-hindi", "name": "The Hindi to English Database",
            "tagline": DBCFG["language-hindi"]["tagline"],
            "record_kind": "language learning record", "id_prefix": "JAH-LHIN-",
            "ai_name": "JAH Hindi to English Archivist",
            "local_index": "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/language-hindi/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/language-hindi/index.jsonl.gz",
            "chunk_pattern": "data/language-hindi/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "language-hindi-signature", "name": "The Hindi to English Signature Database",
            "tagline": DBCFG["language-hindi-signature"]["tagline"],
            "record_kind": "language learning record", "id_prefix": "JAH-LHINS-",
            "ai_name": "JAH Hindi to English Archivist (Signature)",
            "local_index": "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/language-hindi-signature/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/language-hindi-signature/index.jsonl.gz",
            "chunk_pattern": "data/language-hindi-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAG), exist_ok=True)
    with open(FRAG, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAG, flush=True)

    print("DONE: %d records across %d databases. Manifest/api/index/README/docs untouched - merger handles." % (total, len(built)))
    print("Do NOT commit or push - merger handles.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
