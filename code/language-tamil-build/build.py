#!/usr/bin/env python3
"""Build the Tamil Language databases for JAH Databases
(Manon language project 2026-10-17, batch 2, ranks 11-20).

Roster rank 14: language-tamil. Slug verified free; ID prefixes JAH-LTAM-
(public) and JAH-LTAMS- (signature) verified zero hits in the manifest
id_prefix values AND in all shard index files. 68 titles run through
code/dedupe_gate.py against the WHOLE system before authoring: zero
refusals.

Creates two NEW databases, 34 ladder-ordered records each:

  language-tamil             - Tamil Language Database
                               (public-harvest: real, fact-checked Tamil
                               linguistics - தமிழ், Dravidian - every record
                               carrying Tamil script + transliteration +
                               English + example sentences, taught along
                               the teaching ladder)
  language-tamil-signature   - Tamil Language Signature Database
                               (his original Signature Word Method; src
                               signature, titles suffixed
                               " (Signature Edition)", clearly labeled
                               Signature-made, never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Linguistic cores: all hand-authored 2026-10-17, machine-verified by the
demos (see demos_language_tamil.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: never touches data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md. Never git commits or pushes. A merger
handles those. This build only creates: db/language-tamil[-signature]/
(index.html + gen-*.js), code/language-tamil-build/*, the shard data dirs,
and the merger fragment JSON.

Never the words "bat belt" anywhere. No website references. No Facebook.
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
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/language-tamil.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_language_tamil import ENTRIES, SIG_TAIL
from demos_language_tamil import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Word Method: "
                "every word a signed instrument of meaning, grammar the "
                "covenant binding words into truth, the learner's tongue "
                "the seal. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("Public records - real, fact-checked Tamil linguistics: "
                "தமிழ், a Dravidian language - every record carrying "
                "Tamil script with transliteration and English translation "
                "plus example sentences, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, script and writing system, pronunciation "
              "and phonology, core nouns, core verbs, adjectives and "
              "adverbs, pronouns, numbers and time, greetings and everyday "
              "phrases, grammar essentials) -> Compounded (home and family "
              "sentences, food and cooking sentences, travel and directions "
              "sentences, work and school sentences, health and body "
              "sentences, emotions and feelings sentences, nature and "
              "weather sentences, shopping and money sentences, friendship "
              "and social life sentences, technology and communication "
              "sentences, verb tenses in sentences, questions and answers, "
              "commands and requests, descriptions of people and places) -> "
              "Advanced (three story paragraphs, idioms and proverbs, "
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
        "search_ph": "Search Tamil script, pronunciation, nouns, verbs, grammar, numbers, greetings, tenses, idioms, proverbs, conversations...",
        "chat_ph": "Ask about the Tamil language...",
        "archive_blurb": ("Seeded %s Tamil language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Tamil language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the Tamil language - script, sounds, words, grammar, sentences, stories, idioms, and conversation." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "tamil-language-study", "gen_demo_kind": "tamil-language-demo",
        "source": source,
    }

CIT_PUB = ("Tamil linguistics (standard references: Tolkappiyar. "
           "Tolkappiyam; Thiruvalluvar. Thirukkural; Caldwell R. A "
           "Comparative Grammar of the Dravidian or South-Indian Family of "
           "Languages. London: Harrison; 1856; Pope GU. A Handbook of the "
           "Ordinary Dialect of the Tamil Language. 7th ed. Oxford: "
           "Clarendon Press; 1911; Lehmann T. A Grammar of Modern Tamil. "
           "Pondicherry: Pondicherry Institute of Linguistics and Culture; "
           "1989; Annamalai E, Steever SB. Modern Tamil. In Steever SB, "
           "ed. The Dravidian Languages. London: Routledge; 1998; "
           "Schiffman HF. A Reference Grammar of Spoken Tamil. Cambridge: "
           "Cambridge University Press; 1999; Eberhard DM et al, eds. "
           "Ethnologue: Languages of the World. 28th ed. Dallas: SIL "
           "International; 2025).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Word "
                     "Method - every word a signed instrument of meaning - "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-tamil"] = _cfg(
    "language-tamil", "Tamil Language Database",
    "Learn Tamil from first greeting to full conversation: real, "
    "fact-checked Tamil linguistics - தமிழ், a Dravidian language - every "
    "record carrying Tamil script with transliteration and English "
    "translation plus example sentences, taught progressively along the "
    "teaching ladder from overview to mastery review.",
    "language learning record", "JAH-LTAM-", "JAH Tamil Language Tutor",
    "Tamil language tutor - teaching Tamil from first greeting to full "
    "conversation: script, pronunciation, words, grammar, sentences, "
    "stories, idioms, and conversation; answers from many angles - "
    "definition, example, analogy, application, history, how-to - using "
    "only archive data from this system",
    CIT_PUB, "public")
DBCFG["language-tamil-signature"] = _cfg(
    "language-tamil-signature", "Tamil Language Signature Database",
    "His original Signature Word Method applied to Tamil: every word a "
    "signed instrument of meaning, grammar the covenant binding words "
    "into truth, the learner's tongue the seal. The full ladder from "
    "overview through script, sounds, words, and grammar, through themed "
    "sentences and tenses, to stories, idioms, and conversation, reframed "
    "as Signature science. Clearly labeled Signature-made, never presented "
    "as authentic public record.",
    "language learning record", "JAH-LTAMS-", "JAH Tamil Language Tutor (Signature)",
    "Tamil language tutor - Signature editions: his original Signature "
    "Word Method applied to Tamil, every word a signed instrument of "
    "meaning, clearly labeled Signature-made and never presented as "
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
        sig = slug.endswith("-signature")
        cfg = DBCFG[slug]
        url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        frag["signature" if sig else "public"] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": url,
            "record_count": len(recs),
            "status": "live",
            "full_records": len(recs),
            "index": url,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if sig else "public-harvest",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
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
    for slug in ("language-tamil", "language-tamil-signature"):
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
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)
    print("built 2 databases, %d records total; manifest/api untouched for the merger" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
