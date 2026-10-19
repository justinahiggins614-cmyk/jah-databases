#!/usr/bin/env python3
"""Build the Jin Chinese Language databases for JAH Databases
(Language project 2026-10-17, batch 4).

Roster rank 34/100: Jin Chinese (晋语), ISO 639-3 cjy, Sino-Tibetan.
Slug verified free in the manifest; id prefixes JAH-LCJY- (public) and
JAH-LCJYS- (signature) verified zero-hit in the manifest id_prefix values
AND in every shard index file under jah-databases-data-1 (no JAH-LCJY*
prefix anywhere in the system).

So this build creates two NEW databases, 34 ladder-ordered records each:

  language-jin-chinese            - The Jin Chinese to English Database
                                    (public-harvest: real, fact-checked Jin
                                    Chinese linguistics - Taiyuan dialect
                                    of the Bingzhou group as the reference
                                    standard; the preserved entering tone,
                                    tones/romanization, phonology, core
                                    vocabulary, grammar, themed sentence
                                    sets, stories, idioms, registers,
                                    complex sentences, conversations,
                                    mastery reference; every record
                                    carrying Chinese characters +
                                    romanization + English; standard
                                    references Li Rong 1985, Language Atlas
                                    of China 1987/2012, Norman 1988, Hou &
                                    Shen 2002, Yan 2006, Kurpaska 2010,
                                    Ethnologue [cjy], ISCA 2024)
  language-jin-chinese-signature - The Jin Chinese to English Signature
                                    Database (his original Signature
                                    language work: the same 34-rung ladder
                                    read through the Signature lens - every
                                    record a signed covenant of meaning;
                                    src signature, titles suffixed
                                    " (Signature Edition)", never
                                    presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10
non-decreasing, ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

Romanization: practical pinyin-style teaching romanization with tone
numbers. Tone numbers map to the Taiyuan tone categories: 1 = 11 level
(yinping; old yangping merged in), 2 = 53 (shangsheng), 3 = 45 (qusheng),
4 = entering tone (short checked syllable ending in the glottal stop ʔ).
Citation tones per syllable; yin/yang ru split noted but not marked in the
teaching scheme. This is a teaching romanization defined in the entries.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_jin_chinese.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), prints CHECK:
lines cross-checked against the full entry text at build time, and ends
with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes -
a merger handles those. Manifest/api entries are printed (not written) for
the merger.

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
FRAGMENTS = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_jin_chinese import ENTRIES, SIG_TAIL
from demos_jin_chinese import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature language work: "
                "the full Jin ladder read through the Signature lens, every "
                "record a signed covenant of meaning, every entering tone a "
                "seal, every idiom a master seal of Shanxi identity. Clearly "
                "labeled Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked Jin Chinese linguistics: "
                "Taiyuan dialect of the Bingzhou group as the reference "
                "standard - the preserved entering tone, tones and "
                "romanization, phonology, core vocabulary, grammar, themed "
                "sentence sets, stories, idioms, registers, complex "
                "sentences, conversations, and a mastery reference - every "
                "record carrying Chinese characters, romanization, and "
                "English, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(language overview, writing system, pronunciation and "
              "phonology, core nouns, core verbs, adjectives and adverbs, "
              "pronouns, numbers and time, greetings and everyday phrases, "
              "grammar essentials) -> Compounded (home and family, food and "
              "cooking, travel and directions, work and school, health and "
              "body, emotions and feelings, nature and weather, shopping and "
              "money, friendship and social life, technology and "
              "communication) -> Advanced (verb tenses, questions and "
              "answers, commands and requests, descriptions, three stories, "
              "idioms and proverbs, formal and polite registers, compound "
              "and complex sentences, three conversations, mastery review "
              "and full reference).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Jin Chinese tones, pronunciation, nouns, verbs, grammar, numbers, greetings, phrases, idioms, conversations...",
        "chat_ph": "Ask about Jin Chinese...",
        "archive_blurb": ("Seeded %s Jin Chinese language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Jin Chinese language studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Jin Chinese - from tones and pronunciation through core words, grammar, numbers, greetings, and everyday topics, to stories, idioms, and full conversation." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "jin-chinese-study", "gen_demo_kind": "jin-chinese-demo",
        "source": source,
    }

CIT_PUB = ("Jin Chinese linguistics (standard references: Li Rong 李荣 1985, "
           "proposal of Jin as a separate top-level group; Language Atlas of "
           "China, 1st ed. 1987, 2nd ed. Chinese Academy of Social Sciences, "
           "Commercial Press, 2012 - 8 subgroups, 63.05 million speakers; "
           "Norman J. Chinese. Cambridge University Press; 1988; Hou Jingyi "
           "侯精一, Shen Ming 沈明. 现代汉语方言概论. Shanghai Education "
           "Press; 2002; Yan M.M. Introduction to Chinese Dialectology. "
           "LINCOM Europa; 2006; Kurpaska M. Chinese Language(s). de Gruyter; "
           "2010; Ethnologue: Jin Chinese [cjy], ISO 639-3:2007; Liao et al. "
           "Perception of the Merging Tones in Taiyuan Jin Chinese. ISCA "
           "Speech Prosody; 2024).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "language work - the Jin ladder read through the "
                     "Signature lens, clearly labeled Signature-made.")

DBCFG = {}
DBCFG["language-jin-chinese"] = _cfg(
    "language-jin-chinese", "The Jin Chinese to English Database",
    "Learn Jin Chinese (晋语): real, fact-checked Shanxi language teaching "
    "from first tones to full conversation - every record carrying Chinese "
    "characters, romanization, and English, taught along the ladder.",
    "language learning record", "JAH-LCJY-", "JAH Jin Chinese Language Tutor",
    "Jin Chinese language tutor - teaching Jin Chinese from first tones to full "
    "conversation with Chinese characters, romanization, and English on every "
    "line; answers from many angles - definition, example, analogy, "
    "application, history, sound, how-to - using only archive data from this "
    "system",
    CIT_PUB, "public")
DBCFG["language-jin-chinese-signature"] = _cfg(
    "language-jin-chinese-signature", "The Jin Chinese to English Signature Database",
    "His original Signature reading of Jin Chinese: the full 34-rung ladder "
    "from first tones to full conversation, reframed as signed covenants of "
    "meaning - every record a seal, every idiom a master seal of Shanxi "
    "identity. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "language learning record", "JAH-LCJYS-", "JAH Jin Chinese Language Tutor (Signature)",
    "Jin Chinese language tutor - Signature editions: his original Signature "
    "reading of Jin Chinese, every record a signed covenant of meaning, "
    "clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, sound, how-to - using only archive data "
    "from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    refused = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        hits = [h for h in base.GATE.check(slug, title) if h[0] != slug]
        if hits:
            refused.append((title, hits))
            print("  gate refused (cross-db dupe): %s -> %s" % (title, hits), flush=True)
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
    return recs, refused


def node_check_js(path):
    p = subprocess.run(["node", "--check", path],
                       capture_output=True, text=True, timeout=60)
    assert p.returncode == 0, "node --check failed on %s: %s" % (path, p.stderr[-500:])


def node_check_page_scripts(ppath, workdir):
    with open(ppath, "r", encoding="utf-8") as f:
        html = f.read()
    blocks = re.findall(r'<script(?![^>]*\bsrc=)(?![^>]*ld\+json)[^>]*>(.*?)</script>', html, re.S)
    n = 0
    for i, s in enumerate(blocks):
        if not s.strip():
            continue
        tmp = os.path.join(workdir, "page-script-%d.js" % i)
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(s)
        node_check_js(tmp)
        n += 1
    return n


def write_fragment(built):
    frag = {}
    for slug, recs in built.items():
        sig = slug.endswith("-signature")
        cfg = DBCFG[slug]
        frag["signature" if sig else "public"] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(recs),
            "status": "live",
            "full_records": len(recs),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if sig else "public-harvest",
        }
    os.makedirs(FRAGMENTS, exist_ok=True)
    fpath = os.path.join(FRAGMENTS, "language-jin-chinese.json")
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
    all_refused = []
    for slug in ("language-jin-chinese", "language-jin-chinese-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        recs, refused = build_records(slug, source)
        built[slug] = recs
        all_refused.extend(refused)

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

    # machine-execute ALL demos (68) + cross-check CHECK: words vs entry text
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            blob = json.dumps(r, ensure_ascii=False)
            for line in p.stdout.splitlines():
                if line.startswith("CHECK:"):
                    word = line[len("CHECK:"):]
                    assert word in blob, \
                        "demo/entry cross-check failed: %r not in %s" % (word, r["id"])
    print("demo execution: all %d demos ran OK; CHECK cross-checks passed" % total, flush=True)

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
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        nscripts = node_check_page_scripts(ppath, HERE)
        node_check_js(gpath)
        print("page:  db/%s/index.html + gen-%s.js [%s] node: %d page scripts + gen js clean"
              % (slug, slug, ", ".join(notes), nscripts), flush=True)

    fpath = write_fragment(built)
    print("fragment: %s" % fpath, flush=True)

    # merger handoff: manifest/api entries printed, NOT written (concurrency rule)
    for slug, recs in built.items():
        print("MERGE-ENTRY: %s" % json.dumps(base.manifest_entry(slug, len(recs)),
                                            ensure_ascii=False), flush=True)
    print("dedupe refusals: %d" % len(all_refused), flush=True)
    print("NEXT (merger): manifest + api.json + restamp + commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
