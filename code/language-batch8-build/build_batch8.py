#!/usr/bin/env python3
"""Build the batch-8 language database pairs (Manon's language project,
ranks 71-80): ilocano, bulgarian, quechua, mongolian, danish, slovak,
finnish, hebrew, norwegian, croatian.

Usage: build_batch8.py [lang ...]   (default: all 10)

For each language this creates two NEW databases, 34 ladder-ordered
records each:

  language-<lang>              - The <Lang> Language Database
                                 (public-harvest: real, fact-checked language
                                 teaching - overview, writing system,
                                 pronunciation and phonology, core vocabulary
                                 with sentences, pronouns, numbers and time,
                                 greetings, grammar essentials, themed
                                 sentence sets for daily life, verb tenses,
                                 questions and answers, commands, descriptions,
                                 stories, idioms, formal and polite registers,
                                 complex sentences, conversations, and a
                                 mastery review; every record carries the
                                 language plus romanization plus English)
  language-<lang>-signature    - The <Lang> Language Signature Database
                                 (his original Signature <Lang> Method;
                                 src signature, titles suffixed
                                 " (Signature Edition)", never presented as
                                 authentic public record)

34 records each, ladder-ordered 1-34 (foundations 1-10 / compounded 11-21 /
advanced 22-34); the shard index is written in ladder order so pages present
simple -> compounded -> complex.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it, asserts tight bounds (never float
exact-equality), prints the real computed values, and ends with the OK
marker. This build machine-executes all demos (680 for the full batch).

Dedupe gate: every record checked against the whole system before writing
(zero duplicates). Content gates: nothing hate-adjacent/profane/
inappropriate, no religious framing; known false-positive classes screened
with context, legitimate language terms never stripped.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/language-<lang>/index.html + gen-language-<lang>.js
              db/language-<lang>-signature/index.html + gen-...js
  shard repo: data/language-<lang>/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/language-<lang>-signature/... (same)
  build dir : code/language-batch8-build/{build_batch8.py, engine.py,
              d_<lang>.py, fix_scandinavian.py}
              code/language-<lang>-build/build.py (thin per-pair wrappers)
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/
              language-<lang>.json

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
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
import engine
from engine import DEMOS

DATA_MODS = ["d_ilocano", "d_bulgarian", "d_quechua", "d_mongolian",
             "d_danish", "d_slovak", "d_finnish", "d_hebrew",
             "d_norwegian", "d_croatian"]


def _cfg(L, source):
    n = L["name"]
    sig = source == "signature"
    sig_line = ("Signature originals - " + L["sig_method"] +
                " Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked %s language teaching: "
                "the language overview, the writing system, pronunciation "
                "and phonology, core nouns verbs adjectives and adverbs with "
                "sentences, pronouns, numbers and time, greetings, grammar "
                "essentials, themed sentence sets for daily life, verb "
                "tenses, questions and answers, commands and requests, "
                "descriptions, stories, idioms, formal and polite registers, "
                "complex sentences, conversations, and a mastery review - "
                "every record carrying %s content plus romanization plus "
                "English translation plus example sentences." % (n, n))
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
    ai = "JAH %s Language Archivist" % n + (" (Signature)" if sig else "")
    return {
        "name": "The %s Language %sDatabase" % (n, "Signature " if sig else ""),
        "tagline": L["tagline"],
        "record_kind": "language learning record",
        "prefix": L["sig_prefix"] if sig else L["prefix"],
        "ai": ai,
        "role": L["role"] + (" - Signature editions" if sig else ""),
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (L["tagline"], sig_line if sig else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else
                     "Public records organized in the Signature system"),
        "search_ph": L["search_ph"],
        "chat_ph": L["chat_ph"],
        "archive_blurb": ("Seeded %s %s language records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record", n)),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled %s language studies. Seeded archive records are the authoritative entries." % n,
        "greet": L["greet"] + (" (Signature editions.)" if sig else ""),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "language-%s-study" % L["slug"].split("-", 1)[1],
        "gen_demo_kind": "language-%s-demo" % L["slug"].split("-", 1)[1],
        "source": source,
    }


def build_records(L, entries, source):
    sig = source == "signature"
    slug = L["slug"] + ("-signature" if sig else "")
    cfg = _cfg(L, source)
    sig_tail = ("Signature original - " + L["sig_method"] +
                " Clearly labeled Signature-made, never presented as "
                "authentic public record.")
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
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
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


def build_language(L):
    n = L["name"]
    entries = engine.build_entries(L)
    assert len(entries) == 34
    built = {}
    for source in ("public", "signature"):
        slug = L["slug"] + ("-signature" if source == "signature" else "")
        built[slug] = (build_records(L, entries, source), _cfg(L, source))

    total = 0
    for slug, (recs, cfg) in built.items():
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
        total += len(recs)
        w = base.write_shard_db(slug, recs)
        assert w == 34
        print("shard: %-38s %d records" % (slug, w), flush=True)

    for slug, (recs, cfg) in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK for %s" % (total, n), flush=True)

    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, (recs, cfg) in built.items():
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
        gen_js = nb.build_gen_js(slug, topics, cfg)
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        scripts = _extract_scripts(page)
        assert scripts, "no inline scripts found in %s" % slug
        for i, body in enumerate(scripts):
            chk = "/tmp/batch8_check_%s_%d.js" % (slug.replace("-", "_"), i)
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

    pub_cfg = built[L["slug"]][1]
    sig_cfg = built[L["slug"] + "-signature"][1]
    fragment = {
        "public": {
            "slug": L["slug"],
            "name": pub_cfg["name"],
            "tagline": pub_cfg["tagline"],
            "record_kind": "language learning record",
            "id_prefix": pub_cfg["prefix"],
            "ai_name": pub_cfg["ai"],
            "local_index": SHARD_BASE + "/data/%s/index.jsonl.gz" % L["slug"],
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/%s/index.jsonl.gz" % L["slug"],
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % L["slug"],
            "source": "public-harvest",
        },
        "signature": {
            "slug": L["slug"] + "-signature",
            "name": sig_cfg["name"],
            "tagline": sig_cfg["tagline"],
            "record_kind": "language learning record",
            "id_prefix": sig_cfg["prefix"],
            "ai_name": sig_cfg["ai"],
            "local_index": SHARD_BASE + "/data/%s-signature/index.jsonl.gz" % L["slug"],
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/%s-signature/index.jsonl.gz" % L["slug"],
            "chunk_pattern": "data/%s-signature/chunks/chunk-NNNN.jsonl.gz" % L["slug"],
            "source": "signature",
        },
    }
    os.makedirs(FRAGDIR, exist_ok=True)
    fpath = os.path.join(FRAGDIR, "%s.json" % L["slug"])
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath, flush=True)

    # thin per-pair wrapper in code/language-<lang>-build/
    pairdir = os.path.join(REPO, "code", "%s-build" % L["slug"])
    os.makedirs(pairdir, exist_ok=True)
    wpath = os.path.join(pairdir, "build.py")
    with open(wpath, "w", encoding="utf-8") as f:
        f.write('#!/usr/bin/env python3\n'
                '"""Build the %s language database pair (ranks 71-80, batch 8).\n'
                'Thin wrapper - the shared engine lives in\n'
                'code/language-batch8-build/. Run: python3 build.py\n'
                'NEVER touches data/manifest.json or api.json. NEVER commits.\n'
                '"""\n'
                'import os\n'
                'import sys\n'
                'sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/language-batch8-build")\n'
                'import build_batch8\n'
                '\n'
                'if __name__ == "__main__":\n'
                '    sys.exit(build_batch8.main(["%s"]))\n'
                % (n, L["slug"].split("-", 1)[1]))
    print("wrapper: %s" % wpath, flush=True)
    print("DONE %s: 2 databases, %d records." % (n, total), flush=True)
    return total


def main(langs=None):
    mods = {}
    for mname in DATA_MODS:
        mod = __import__(mname)
        mods[mod.LANG["slug"].split("-", 1)[1]] = mod.LANG
    if langs:
        want = [a.replace("language-", "") for a in langs]
        unknown = [w for w in want if w not in mods]
        assert not unknown, "unknown languages: %s" % unknown
        order = want
    else:
        order = [mname[2:] for mname in DATA_MODS]
    grand = 0
    for key in order:
        grand += build_language(mods[key])
    print("BATCH DONE: %d languages, %d databases, %d records. "
          "Merger handles manifest/api/restamp/commit." % (len(order), len(order) * 2, grand))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
