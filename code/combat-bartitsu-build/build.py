#!/usr/bin/env python3
"""Build the Bartitsu Combat databases for JAH Databases
(Manon's combat orders 2026-10-17, combat batch 3).

Dedupe gate pre-run 2026-10-17 over all 68 titles (34 public + 34
" (Signature Edition)") vs the WHOLE system: zero collisions.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-bartitsu              - Bartitsu Combat Database
                                 (public-harvest: real, fact-checked
                                 Victorian martial-arts knowledge - Edward
                                 William Barton-Wright's Bartitsu (London,
                                 circa 1898-1902): English pugilism, French
                                 savate, Japanese jujutsu (Yukio Tani), and
                                 the Vigny cane method - every record a
                                 technique with step-by-step body mechanics)
  combat-bartitsu-signature    - Bartitsu Combat Signature Database
                                 (his original Signature Combat Method: the
                                 cane the Signature line drawn through
                                 space, the grip the oath, the guard the
                                 boundary of the self, every cut a decision
                                 carried to completion; src signature,
                                 titles suffixed " (Signature Edition)",
                                 never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBBA- (public) and JAH-CBBAS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Civilian historical martial art only. Screening: nothing hate-adjacent,
profane, or inappropriate; no religious talk; nothing on neutralizing or
defeating military or defense-grade systems.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_bartitsu.py). Every demo prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker; the build machine-executes all 68 demos before delivery.

Never the words "bat belt" anywhere. No website references. No Facebook.

Concurrency: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes - a merger handles those. It writes only:
  db/combat-bartitsu/ + db/combat-bartitsu-signature/ (index.html + gen-*.js)
  code/combat-bartitsu-build/ (this pipeline)
  <shard>/data/combat-bartitsu[-signature]/ (index.jsonl.gz + chunks)
  ~/workspace/hidden_files/missing-builds/fragments/combat-bartitsu.json
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-bartitsu.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_bartitsu import ENTRIES, SIG_TAIL
from demos_bartitsu import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat Method: "
                "the cane the Signature line drawn through space, the grip "
                "the oath, the guard the boundary of the self, every cut a "
                "decision carried to completion. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Victorian martial-arts "
                "knowledge: Edward William Barton-Wright's Bartitsu (London, "
                "circa 1898-1902), blending English pugilism, French savate, "
                "Japanese jujutsu as taught by Yukio Tani, and the Vigny "
                "cane-fighting method - every record a technique with "
                "step-by-step body mechanics, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what Bartitsu is, the guard stance, footwork, the Vigny cane "
              "grip and portes, ukemi falling safety, the straight blow, "
              "the savate front kick, cane guards tierce and quarte, "
              "distance and timing, basic cane parries) -> Compounded (the "
              "Vigny overhead cut, the moulinet figure-of-eight, o goshi hip "
              "throw, the hook punch, the savate low kick, the cane thrust, "
              "kotegaeshi wrist lock, the chasse side kick, uppercut and "
              "body blow, the cane hook disarm, hip throw with cane assist, "
              "combination striking, seoi nage shoulder throw, balayage foot "
              "sweep) -> Advanced (juji gatame armlock, knife defense, the "
              "flying mare throw, counter-punching and the riposte, multiple "
              "opponent awareness, the two-handed cane trap, hadaka jime "
              "choke and defense, randori sparring, the grand combination, "
              "teaching Bartitsu).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Bartitsu, cane fighting, Vigny, savate, pugilism, jujutsu, throws, locks, stance, footwork, ukemi, parries, moulinet, kotegaeshi, randori...",
        "chat_ph": "Ask about Bartitsu techniques...",
        "archive_blurb": ("Seeded %s Bartitsu combat technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Bartitsu technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Bartitsu - from what the art is through the guard stance, footwork, cane grip, ukemi, punches, kicks, guards, distance, and parries, through cuts, moulinets, hip throws, hooks, thrusts, locks, side kicks, disarms, combinations, shoulder throws, and sweeps, to armlocks, knife defense, the flying mare, counters, multiple opponents, cane traps, chokes, randori, the grand combination, and teaching the art." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "bartitsu-study", "gen_demo_kind": "bartitsu-demo",
        "source": source,
    }

CIT_PUB = ("Bartitsu and Victorian martial arts (standard references: "
           "Barton-Wright EW. The New Art of Self Defence. Pearson's "
           "Magazine; 1899; Barton-Wright EW. Self Defence with a "
           "Walking-Stick. Pearson's Magazine; 1901; Vigny P. The Art of "
           "Self-Defence on Foot with the Cane and the Umbrella. Health & "
           "Strength; 1904; Charlemont J. La Boxe Francaise: Traite "
           "Theorique et Pratique. Paris; 1878; Kano J. Kodokan Judo. "
           "Kodansha International; 1986; Lang TH. The Walking Stick Method "
           "of Self Defence. Athletic Publications; 1923; Wolf T, ed. The "
           "Bartitsu Compendium. Vol 1. Lulu Press; 2005; Marquess of "
           "Queensberry Rules. London; 1867).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Combat "
                     "Method - the cane the Signature line drawn through "
                     "space, the grip the oath, the guard the boundary of "
                     "the self - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["combat-bartitsu"] = _cfg(
    "combat-bartitsu", "Bartitsu Combat Database",
    "Victorian Bartitsu self-defense: cane fighting, savate, pugilism, and "
    "jujutsu combined - 34 ladder-ordered techniques, each with step-by-step "
    "body mechanics, from stance and footwork through cuts, throws, and "
    "locks to sparring and teaching the art.",
    "combat technique record", "JAH-CBBA-", "JAH Bartitsu Combat Archivist",
    "bartitsu combat archivist - teaching Victorian Bartitsu self-defense: "
    "cane fighting, savate, pugilism, and jujutsu combined, every technique "
    "with step-by-step body mechanics; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, math, "
    "how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-bartitsu-signature"] = _cfg(
    "combat-bartitsu-signature", "Bartitsu Combat Signature Database",
    "His original Signature Combat Method: the cane the Signature line drawn "
    "through space, the grip the oath, the guard the boundary of the self, "
    "every cut a decision carried to completion. The full ladder from what "
    "Bartitsu is through stance, footwork, cane, striking, throws, and "
    "locks to sparring, the grand combination, and teaching, reframed as "
    "Signature science. Clearly labeled Signature-made, never presented as "
    "authentic public record.",
    "combat technique record", "JAH-CBBAS-", "JAH Bartitsu Combat Archivist (Signature)",
    "bartitsu combat archivist - Signature editions: his original Signature "
    "Combat Method, the cane the Signature line drawn through space and the "
    "grip the oath, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
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


def _extract_scripts(page):
    scripts = []
    for m in re.finditer(r"<script(?![^>]*\ssrc=)(?![^>]*ld\+json)[^>]*>(.*?)</script>", page, re.S):
        body = m.group(1).strip()
        if body:
            scripts.append(body)
    return scripts


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
    for slug in ("combat-bartitsu", "combat-bartitsu-signature"):
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
        assert "bartitsu" in page.lower(), "field content missing in %s" % slug
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
        # JS hygiene: node --check on extracted page scripts and gen js
        scripts = _extract_scripts(page)
        assert scripts, "no inline scripts found in %s" % slug
        import tempfile
        for i, body in enumerate(scripts):
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                tf.write(body)
                tf_path = tf.name
            p = subprocess.run(["node", "--check", tf_path],
                               capture_output=True, text=True, timeout=60)
            os.unlink(tf_path)
            assert p.returncode == 0, "node --check failed page script %d in %s: %s" % (i, slug, p.stderr[-500:])
        p = subprocess.run(["node", "--check", os.path.join(ddir, "gen-%s.js" % slug)],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "node --check failed gen js %s: %s" % (slug, p.stderr[-500:])
        # apostrophe-free role/ai/greet/search strings
        for k in ("ai", "role", "greet", "search_ph", "chat_ph"):
            assert "'" not in DBCFG[slug][k], "apostrophe in %s cfg %s" % (slug, k)
        print("page:  db/%s/index.html + gen-%s.js [%s] [node OK x%d]" % (
            slug, slug, ", ".join(notes), len(scripts)), flush=True)

    # Fragment for the merger (manifest/api/index.html/README/AI_ACCESS untouched here).
    fragment = {"public": {}, "signature": {}}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        sig = slug.endswith("-signature")
        key = "signature" if sig else "public"
        base_slug = "combat-bartitsu"
        fragment[key] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": "%s/data/%s/index.jsonl.gz" % (SHARD_BASE, slug),
            "record_count": len(recs),
            "status": "live",
            "full_records": len(recs),
            "index": "%s/data/%s/index.jsonl.gz" % (SHARD_BASE, slug),
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
            "source": "signature" if sig else "public-harvest",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=2)
    print("fragment: %s" % FRAGMENT, flush=True)
    print("DONE: %d records across %d databases. Merger verifies; do NOT claim live." % (total, len(built)))
    print("NEXT (merger): restamp counts, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
