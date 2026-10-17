#!/usr/bin/env python3
"""Build the Judo Combat databases for JAH Databases (combat batch 1).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,390 databases)
PLUS every shard index title in jah-databases-data-1 (812 index files):
zero 'combat-judo' slugs/names; zero 'judo' / 'karate' / 'martial' /
'combat' / 'kung' databases of any kind - no near-hits at all. ID prefixes
JAH-CBJ- and JAH-CBJS- verified free in the manifest id_prefix values and
in every shard index file (zero hits). The 68 titles were run through the
whole-system dedupe gate before authoring: zero collisions.

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-judo             - The Judo Combat Database
                            (public-harvest: real, fact-checked Kodokan judo -
                            ukemi, nage-waza by family, katame-waza, randori
                            principles - every record with Japanese
                            terminology, step-by-step body mechanics, and
                            citations)
  combat-judo-signature   - The Judo Combat Signature Database
                            (his original Signature Way of the Gentle Path;
                            src signature, titles suffixed " (Signature
                            Edition)", never presented as authentic public
                            record)

34 records each, ladder_rank 1-10 non-decreasing, tiers
foundations -> compounded -> advanced; shard index written in ladder order.

Pipeline replicates code/component-parts-catalog-build/build.py exactly for
page structure: build_page + build_gen_js from numbering-build, sweep pass,
Exhaustive pill + merger button + tab guard carried over from the template.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes. The merger owns those. This script writes only:
  db/combat-judo/ + db/combat-judo-signature/ (index.html + gen-*.js)
  jah-databases-data-1/data/combat-judo[-signature]/ (index.jsonl.gz + chunks)
  ~/workspace/hidden_files/missing-builds/fragments/combat-judo.json

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_judo.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian martial-arts instruction only.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-judo.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_judo import ENTRIES, SIG_TAIL
from demos_combat_judo import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature Way of the "
                "Gentle Path: seiryoku zenyo, maximum efficiency, as the "
                "Signature law of perfect economy; jita kyoei, mutual "
                "welfare, as the covenant between training partners; "
                "kuzushi as reading the opponent's signature before it is "
                "written. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("Public records - real, fact-checked Kodokan judo: ukemi "
                "breakfalls, nage-waza throws by family (te-waza hand "
                "techniques, koshi-waza hip techniques, ashi-waza foot "
                "techniques, sutemi-waza sacrifice techniques), katame-waza "
                "(osaekomi-waza pins, shime-waza chokes, kansetsu-waza "
                "armlocks), and randori principles - every record carrying "
                "the Japanese terminology with translations, step-by-step "
                "body mechanics, key points, safety requirements, "
                "standards, and citations, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(reigi etiquette, shisei posture, mae/koho/yoko/zenpo-kaiten "
              "ukemi, kuzushi eight directions, tai sabaki, ayumi/tsugi "
              "ashi footwork, kumikata gripping) -> Compounded (de ashi "
              "harai, o soto gari, o goshi, seoi nage, o uchi gari, ko uchi "
              "gari, hiza guruma, tai otoshi, kesa gatame, harai goshi, "
              "uchi mata, tomoe nage, kami shiho gatame, yoko shiho gatame, "
              "nami juji jime, hadaka jime, juji gatame) -> Advanced "
              "(renraku waza combinations, kaeshi waza counters, tate shiho "
              "gatame, okuri eri jime, sumi gaeshi, ude garami, randori "
              "free practice).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search ukemi, kuzushi, tai sabaki, footwork, kumikata, seoi nage, o goshi, uchi mata, tomoe nage, kesa gatame, juji gatame, hadaka jime, renraku waza, kaeshi waza, randori...",
        "chat_ph": "Ask about judo techniques...",
        "archive_blurb": ("Seeded %s judo combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Nage Waza \u00b7 Katame Waza \u00b7 Advanced Study - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled judo technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about judo - from ukemi breakfalls, posture, balance breaking, body movement, footwork, and gripping, through the throwing families te-waza, koshi-waza, ashi-waza, and sutemi-waza, through pins, chokes, and armlocks, to combinations, counters, and randori." % ai,
        "gen_fields": ["Foundations", "Nage Waza", "Katame Waza", "Advanced Study"],
        "gen_kind": "judo-technique-study", "gen_demo_kind": "judo-technique-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["combat-judo"] = _cfg(
    "combat-judo", "Judo Combat Database",
    "Kodokan judo from the ground up: ukemi breakfalls, the throwing "
    "families, pins, chokes, armlocks, and randori principles - every "
    "technique with real Japanese terminology and step-by-step body "
    "mechanics, taught along the ladder from foundations to advanced.",
    "combat technique record", "JAH-CBJ-", "JAH Judo Combat Archivist",
    "judo combat archivist - teaching Kodokan judo from ukemi through "
    "nage-waza and katame-waza to randori principles; step-by-step body "
    "mechanics for every technique; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    "public")
DBCFG["combat-judo-signature"] = _cfg(
    "combat-judo-signature", "Judo Combat Signature Database",
    "His original Signature Way of the Gentle Path: the full judo ladder - "
    "ukemi, nage-waza, katame-waza, randori - reframed as Signature "
    "science, where maximum efficiency is the law and every technique is "
    "signed, not forced. Clearly labeled Signature-made, never presented "
    "as authentic public record.",
    "combat technique record", "JAH-CBJS-", "JAH Judo Combat Archivist (Signature)",
    "judo combat archivist - Signature editions: his original Signature Way "
    "of the Gentle Path, maximum efficiency as the Signature law of perfect "
    "economy and mutual welfare as the covenant between training partners, "
    "clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    "signature")

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
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            refused.append(title)
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
    return recs, refused


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
    for slug in ("combat-judo", "combat-judo-signature"):
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
        assert "judo" in page.lower(), "field content missing in %s" % slug
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

    # JS hygiene: node --check on extracted inline page scripts + gen-*.js
    for slug in built:
        ddir = os.path.join(REPO, "db", slug)
        page = open(os.path.join(ddir, "index.html"), encoding="utf-8").read()
        scripts = re.findall(r"<script>(.*?)</script>", page, re.S)
        assert scripts, "no inline scripts found in %s" % slug
        for i, body in enumerate(scripts):
            tmp = "/tmp/cj_jscheck_%s_%d.js" % (slug.replace("-", "_"), i)
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(body)
            p = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
            assert p.returncode == 0, "node --check failed page script %d of %s: %s" % (i, slug, p.stderr[:500])
        gp = os.path.join(ddir, "gen-%s.js" % slug)
        p = subprocess.run(["node", "--check", gp], capture_output=True, text=True)
        assert p.returncode == 0, "node --check failed %s: %s" % (gp, p.stderr[:500])
        print("js hygiene: %s page scripts + gen js node-clean" % slug, flush=True)

    # Fragment for the merger (merger owns manifest.json / api.json / restamp).
    def frag(slug, source):
        cfg = DBCFG[slug]
        url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        return {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": url,
            "record_count": len(built[slug]),
            "status": "live",
            "full_records": len(built[slug]),
            "index": url,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": source,
        }
    fragment = {
        "public": frag("combat-judo", "public-harvest"),
        "signature": frag("combat-judo-signature", "signature"),
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("gate refusals during build: %d" % len(all_refused), flush=True)
    for t in all_refused:
        print("  refused: %s" % t, flush=True)
    print("DONE: %d records across 2 databases; merger verifies live." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
