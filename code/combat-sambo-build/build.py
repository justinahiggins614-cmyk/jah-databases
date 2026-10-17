#!/usr/bin/env python3
"""Build the Sambo Combat databases for JAH Databases
(Manon combat orders 2026-10-17, combat batch 2).

Two NEW databases, 34 ladder-ordered records each:

  combat-sambo               - The Sambo Combat Database
                               (public-harvest: real, fact-checked martial-arts
                               knowledge - Russian sambo, sport and combat
                               sambo: throws, leg locks, ground control, and
                               the strikes of combat sambo; every record a
                               technique carrying HOW TO DO IT step-by-step
                               body mechanics, ladder-ordered from
                               fundamentals to advanced; civilian training
                               scope only)
  combat-sambo-signature     - The Sambo Combat Signature Database
                               (his original Signature Sambo Method: the same
                               ladder through the Signature lens, every
                               technique reframed as Signature science; src
                               signature, titles suffixed " (Signature
                               Edition)", never presented as authentic public
                               record)

34 records each, teaching ladder ranks 1-10 non-decreasing:
foundations -> compounded -> advanced.

ID prefixes: JAH-CBSAM- (public) and JAH-CBSAMS- (signature), verified free
in data/manifest.json id_prefix values and in all 819 shard index files in
jah-databases-data-1 (zero hits, 2026-10-17).

Pre-authoring dedupe sweep (2026-10-17): all 68 titles (34 public + 34
" (Signature Edition)") checked against the whole-system exact gate
(data/dedupe/exact) - zero collisions.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_sambo.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes. A merger handles those. It only writes db/combat-sambo*/,
the shard data dirs, and this build directory.

Civilian training scope only. No hate-adjacent, profane, or inappropriate
content; no religious talk. Nothing on neutralizing or defeating military
or defense-grade systems (standing exclusion).

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
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_sambo import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Sambo Method: "
                "the same ladder through the Signature lens, every technique "
                "reframed as Signature science. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked martial-arts knowledge: "
                "Russian sambo, sport and combat sambo - throws (o soto "
                "gari, seoi nage, harai goshi, uchi mata, ura nage), leg "
                "locks (Achilles lock, knee bar, toe hold), ground control "
                "(kesa gatame, mount, back control), and the strikes of "
                "combat sambo - every record a technique carrying HOW TO DO "
                "IT step-by-step body mechanics, organized in the Signature "
                "system; civilian training scope only.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(stance and base, breakfalls, jacket grips, footwork, "
              "kuzushi, tie-up and clinch entry, posture and frame, hip "
              "escape, bridging, rules and scoring) -> Compounded (o soto "
              "gari, de ashi harai, ko uchi gari, seoi nage, harai goshi, "
              "uchi mata, morote gari, sprawl, kesa gatame, mount, back "
              "control and the rear choke) -> Advanced (armbar, kimura, "
              "Achilles lock, knee bar, toe hold, throwing combinations, "
              "counter throwing, striking entries, clinch striking, kick "
              "defense, ground striking defense, ura nage, fight strategy).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search sambo stance, breakfalls, grips, kuzushi, o soto gari, seoi nage, harai goshi, uchi mata, leg locks, Achilles lock, knee bar, kesa gatame, mount, armbar, kimura, combat sambo striking, scoring...",
        "chat_ph": "Ask about sambo techniques...",
        "archive_blurb": ("Seeded %s sambo combat technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled sambo technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about sambo - from stance, breakfalls, grips, footwork, and kuzushi through o soto gari, seoi nage, harai goshi, uchi mata, and the leg locks to combat sambo striking and fight strategy." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "sambo-technique-study", "gen_demo_kind": "sambo-technique-demo",
        "source": source,
    }

CIT_PUB = ("Sambo technique (standard references: FIAS Official Sambo "
           "Rules. Lausanne; 2024; FIAS Official Combat Sambo Rules. "
           "Lausanne; 2024; Chumakov EM. 100 Lessons of Sambo. Fizkultura "
           "i sport; Moscow; 1977; Kharlampiev AA. Sambo foundational "
           "manuals; 1930s-1940s; Jacques B, Anderson S. The Sambo "
           "Encyclopedia. Black Belt Communications; 2016; Kano J. Kodokan "
           "Judo. Kodansha; 1986).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Sambo "
                     "Method - the same ladder through the Signature lens, "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["combat-sambo"] = _cfg(
    "combat-sambo", "The Sambo Combat Database",
    "Sambo Combat Database: Russian sambo throws, leg locks, ground control, "
    "and combat sambo strikes - every technique with HOW TO DO IT "
    "step-by-step body mechanics, ladder-ordered from fundamentals to "
    "advanced; civilian training scope only.",
    "combat technique record", "JAH-CBSAM-", "JAH Sambo Combat Archivist",
    "sambo combat archivist - Russian sambo throws, leg locks, ground "
    "control, and combat sambo strikes, every technique taught with "
    "step-by-step body mechanics along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["combat-sambo-signature"] = _cfg(
    "combat-sambo-signature", "The Sambo Combat Signature Database",
    "His original Signature Sambo Method: the full sambo ladder - stance, "
    "breakfalls, grips, kuzushi, the great throws, the leg locks, ground "
    "control, and combat sambo striking - reframed through the Signature "
    "lens. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "combat technique record", "JAH-CBSAMS-", "JAH Sambo Combat Archivist (Signature)",
    "sambo combat archivist - Signature editions: his original Signature "
    "Sambo Method, the same ladder through the Signature lens, clearly "
    "labeled Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

import demos_combat_sambo as _dmod
DEMOS = {n[len("demo_cbsam_"):]: getattr(_dmod, n)
         for n in dir(_dmod) if n.startswith("demo_cbsam_")}
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
    for slug in ("combat-sambo", "combat-sambo-signature"):
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

    # CONCURRENCY: manifest.json, api.json, index.html, README.md, docs/AI_ACCESS.md
    # are owned by the merger - this build does not touch them and never commits.
    print("manifest/api/index/README/docs: SKIPPED (merger-owned)")
    print("wrote: db/combat-sambo/index.html, db/combat-sambo/gen-combat-sambo.js")
    print("wrote: db/combat-sambo-signature/index.html, db/combat-sambo-signature/gen-combat-sambo-signature.js")
    print("shards: data-1/data/combat-sambo[/-signature]/{index.jsonl.gz,chunks/chunk-0000.jsonl.gz}")
    print("NEXT: merger runs restamp, commit, push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
