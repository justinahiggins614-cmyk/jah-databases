#!/usr/bin/env python3
"""Build the 10 batch-7 language database pairs for JAH Databases (2026-10-17).

Replaces the prior worker's empty batch: 10 languages x (public + signature),
34 ladder-ordered records each = 680 records total.

  language-somali / -signature        JAH-LSOM-  / JAH-LSOMS-
  language-greek / -signature         JAH-LELL-  / JAH-LELLS-
  language-kazakh / -signature        JAH-LKAZ-  / JAH-LKAZS-
  language-hungarian / -signature     JAH-LHUN-  / JAH-LHUNS-
  language-zulu / -signature          JAH-LZUL-  / JAH-LZULS-
  language-shona / -signature         JAH-LSNA-  / JAH-LSNAS-
  language-czech / -signature         JAH-LCES-  / JAH-LCESS-
  language-swedish / -signature       JAH-LSWE-  / JAH-LSWES-
  language-belarusian / -signature    JAH-LBEL-  / JAH-LBELS-
  language-haitian-creole / -signature JAH-LHAT- / JAH-LHATS-

ID prefixes verified free: zero exact/substring hits across all 2,758
manifest id_prefix values (checked 2026-10-17 before authoring).

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/<slug>/index.html + gen-<slug>.js
  shard repo: data/<slug>/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
  build dir : code/language-batch7-build/
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/language-<x>.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes. No website references.
No Facebook.
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
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
import framework

LANG_MODULES = [
    ("somali", "lang_somali"),
    ("greek", "lang_greek"),
    ("kazakh", "lang_kazakh"),
    ("hungarian", "lang_hungarian"),
    ("zulu", "lang_zulu"),
    ("shona", "lang_shona"),
    ("czech", "lang_czech"),
    ("swedish", "lang_swedish"),
    ("belarusian", "lang_belarusian"),
    ("haitian-creole", "lang_haitian_creole"),
]

# ------------------------------------------------------------------ config

def _cfg(L, source):
    lang = L["lang"]
    sig = source == "signature"
    sig_line = ("Signature originals - his original Signature %s Method: %s Clearly "
                "labeled Signature-made, never presented as authentic public record."
                % (lang, L["sig_lens"]))
    pub_line = ("Public records - real, fact-checked %s language teaching: the language "
                "overview, the %s writing system, pronunciation and phonology, core nouns "
                "verbs adjectives and adverbs with sentences, pronouns, numbers and time, "
                "greetings, grammar essentials, themed sentence sets for daily life, verb "
                "tenses, questions and answers, commands and requests, descriptions, "
                "stories, idioms, formal and polite registers, complex sentences, "
                "conversations, and a mastery review - every record carrying %s content "
                "with romanization plus English translation plus example sentences."
                % (lang, L["facts"]["script"], lang))
    ladder = (" Records are ordered by the teaching ladder: Foundations (language overview, "
              "writing system, pronunciation and phonology, core nouns, core verbs, "
              "adjectives and adverbs, pronouns, numbers and time, greetings, grammar "
              "essentials) -> Compounded (home and family, food and cooking, travel and "
              "directions, work and school, health and body, emotions and feelings, nature "
              "and weather, shopping and money, friendship and social life, technology and "
              "communication, verb tenses in sentences) -> Advanced (questions and answers, "
              "commands and requests, descriptions, three stories, idioms and proverbs, "
              "formal and polite registers, compound and complex sentences, three "
              "conversations, mastery review and full reference).")
    ai = L["ai"] + (" (Signature)" if sig else "")
    return {
        "name": "The %s Language %sDatabase" % (lang, "Signature " if sig else ""),
        "tagline": L["tagline_sig"] if sig else L["tagline_pub"],
        "record_kind": "language learning record",
        "prefix": L["prefix_sig"] if sig else L["prefix_pub"],
        "ai": ai,
        "role": (L["role"] + " - Signature editions: clearly labeled Signature-made, never "
                 "presented as authentic public record" if sig else L["role"]),
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (L["tagline_sig"] if sig else L["tagline_pub"],
                                  sig_line if sig else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else
                     "Public records organized in the Signature system"),
        "search_ph": L["search_ph"],
        "chat_ph": L["chat_ph"],
        "archive_blurb": ("Seeded %s %s language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record", lang)),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": L["gen_desc"],
        "greet": ("I am the %s. %s" % (ai, L["greet"].split(". ", 1)[1])
                  if L["greet"].startswith("I am the") else L["greet"]),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": L["gen_kind"], "gen_demo_kind": L["gen_demo_kind"],
        "source": source,
    }


def build_records(L, slug, source):
    cfg = _cfg(L, source)
    sig = source == "signature"
    sig_tail = "Signature original - " + L["sig_lens"]
    entries = framework.build_entries(L)
    assert set(framework.DEMOS) >= {e["demo_key"] for e in entries}, "demo map misses entries"
    ordered = sorted(enumerate(entries), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + L["sig_lens"] + " "
                           + e["description"])
            how = L["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [sig_tail]
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
        demo_fn = framework.DEMOS[e["demo_key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["demo_data"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs, cfg


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


def gate_records(slug, recs, cfg):
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
        if slug.endswith("-signature"):
            assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
            assert r["src"] == "signature"
        else:
            assert r["src"] == "public-harvest"


def run_demos(recs):
    for r in recs:
        prog = r["demo"]["program"]
        p = subprocess.run([sys.executable, "-c", prog],
                           capture_output=True, text=True, timeout=180)
        assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
        assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]


def write_pages(slug, recs, cfg, template, sweep):
    page = None
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = {slug: cfg}
    page = nb.build_page(slug, template)
    page = page.replace(
        "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
        cfg["gen_desc"])
    assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
    assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
    assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
    assert "dataset.p" in page, "tab-handler guard missing"
    assert "facebook" not in page.lower()
    assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
    ddir = os.path.join(REPO, "db", slug)
    os.makedirs(ddir, exist_ok=True)
    ppath = os.path.join(ddir, "index.html")
    with open(ppath, "w", encoding="utf-8") as f:
        f.write(page)
    changed, notes = sweep.process_page(ppath)
    topics = {}
    for r in recs:
        topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
    gen_js = nb.build_gen_js(slug, topics, cfg)
    assert "facebook" not in gen_js.lower()
    gen_path = os.path.join(ddir, "gen-%s.js" % slug)
    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gen_js)
    scripts = _extract_scripts(page)
    assert scripts, "no inline scripts found in %s" % slug
    for i, body in enumerate(scripts):
        chk = "/tmp/batch7_check_%s_%d.js" % (slug.replace("-", "_"), i)
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


def write_fragment(key, L, pub_cfg, sig_cfg):
    slug = "language-" + key
    sig_slug = slug + "-signature"
    fragment = {
        "public": {
            "slug": slug,
            "name": pub_cfg["name"],
            "tagline": pub_cfg["tagline"],
            "record_kind": "language learning record",
            "id_prefix": L["prefix_pub"],
            "ai_name": pub_cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": sig_slug,
            "name": sig_cfg["name"],
            "tagline": sig_cfg["tagline"],
            "record_kind": "language learning record",
            "id_prefix": L["prefix_sig"],
            "ai_name": sig_cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + sig_slug + "/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/" + sig_slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + sig_slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(FRAGDIR, exist_ok=True)
    fpath = os.path.join(FRAGDIR, slug + ".json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath, flush=True)


def main():
    only = sys.argv[1:] or None
    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    total_dbs = 0
    total_recs = 0
    for key, modname in LANG_MODULES:
        if only and key not in only:
            continue
        mod = importlib.import_module(modname)
        L = mod.LANG
        slug = "language-" + key
        sig_slug = slug + "-signature"
        print("=== %s ===" % slug, flush=True)
        recs_pub, cfg_pub = build_records(L, slug, "public")
        recs_sig, cfg_sig = build_records(L, sig_slug, "signature")
        for s, recs, cfg in ((slug, recs_pub, cfg_pub), (sig_slug, recs_sig, cfg_sig)):
            gate_records(s, recs, cfg)
        run_demos(recs_pub)
        run_demos(recs_sig)
        print("demo execution: all 68 demos ran OK", flush=True)
        for s, recs, cfg in ((slug, recs_pub, cfg_pub), (sig_slug, recs_sig, cfg_sig)):
            n = base.write_shard_db(s, recs)
            print("shard: %-38s %d records" % (s, n), flush=True)
        for s, recs, cfg in ((slug, recs_pub, cfg_pub), (sig_slug, recs_sig, cfg_sig)):
            write_pages(s, recs, cfg, template, sweep)
        write_fragment(key, L, cfg_pub, cfg_sig)
        total_dbs += 2
        total_recs += len(recs_pub) + len(recs_sig)
    print("DONE: %d databases, %d records. Merger handles manifest/api/restamp/commit."
          % (total_dbs, total_recs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
