#!/usr/bin/env python3
"""Build the Lethwei Combat databases for JAH Databases
(Manon's combat orders 2026-10-17, combat batch 1).

Terminology fact-checked 2026-10-17 against Wikipedia 'Lethwei'
(Gowl Tite = headbutt, Let Thee = punching, Tel Daung = elbow, Kan = kicking,
Doo = knee; KO-or-draw traditional rules with one two-minute injury timeout
per corner; tape-and-gauze wraps; five 3-minute rounds; thaing umbrella;
banshay shadowboxing; naban controlled sparring; kyar ba nyein circle
training; Lekkha Moun and Lethwei Yay traditional gestures), lethwei.net,
lethwei.com, fightersvault.com, dojoandring.com, mmafullcontact.com.

Creates two NEW databases, 34 ladder-ordered records each:

  combat-lethwei              - The Lethwei Combat Database
                                (public-harvest: real, fact-checked Burmese
                                bareknuckle lethwei - punches, kicks, elbows,
                                knees, headbutts, clinch and traditional
                                rules - every record a technique with HOW TO
                                DO IT step-by-step body mechanics,
                                ladder-ordered from stance to advanced
                                traditional bouts; civilian training scope)
  combat-lethwei-signature    - The Lethwei Combat Signature Database
                                (his original Signature combat method: the
                                nine limbs as nine covenants, the fighter's
                                mark in every strike; src signature, titles
                                suffixed " (Signature Edition)", clearly
                                labeled Signature-made, never presented as
                                authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBLETH- (public) and JAH-CBLETHS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_lethwei.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos before writing pages.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. Only db/combat-lethwei*/, code/combat-lethwei-build,
the shard data dirs, and the fragment file are written.

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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_lethwei import ENTRIES, SIG_TAIL
from demos_combat_lethwei import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature combat "
                "method: the nine limbs as nine covenants, the fighter's "
                "mark in every strike, the stance the first covenant and "
                "the knockout the final signature. Clearly labeled "
                "Signature-made, never presented as authentic public "
                "record.")
    pub_line = ("Public records - real, fact-checked Burmese bareknuckle "
                "lethwei: punches (Let Thee), kicks (Kan), elbows (Tel "
                "Daung), knees (Doo), headbutts (Gowl Tite), the clinch, "
                "sweeps and throws, and the traditional KO-or-draw rules - "
                "every record a technique with HOW TO DO IT step-by-step "
                "body mechanics, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(the fighting stance, footwork, hand wrapping, the jab and "
              "cross, the guard and shell, the low kick, the foot thrust, "
              "banshay shadowboxing, conditioning the body, the "
              "traditional Lethwei Yay opening) -> Compounded (hooks and "
              "uppercuts, the elbow, the spinning backfist, entering the "
              "clinch, the straight knee, the spear and jumping knee, the "
              "roundhouse kick, sweeps and throws, the headbutt, the "
              "spinning elbow, the axe and hook kick, nine-limb "
              "combinations, defending the clinch, counter-striking, "
              "cutting off the ring, naban controlled sparring) -> "
              "Advanced (the clinch game, traditional bout rules, setting "
              "up the Gowl Tite, reading rhythm with feints and timing, "
              "knuckle and shin hardening, the five-round fight plan, the "
              "full traditional bout from Yay to knockout).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stances, footwork, hand wraps, jabs, crosses, hooks, uppercuts, elbows, knees, kicks, headbutts, clinch, sweeps, throws, banshay, naban, Lethwei Yay, knockout rules, fight plans...",
        "chat_ph": "Ask about Lethwei techniques...",
        "archive_blurb": ("Seeded %s Lethwei combat technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Lethwei combat technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Lethwei - from the stance, footwork, hand wrapping, jabs, crosses, the guard, low kicks, the foot thrust, banshay, conditioning, and the Lethwei Yay, through hooks, uppercuts, elbows, the spinning backfist, the clinch, knees, the roundhouse, sweeps, the headbutt, combinations, counters, ring cutting, and naban, to the clinch game, traditional rules, headbutt setups, rhythm and feints, hardening, the five-round plan, and the full traditional bout." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "lethwei-combat-study", "gen_demo_kind": "lethwei-combat-demo",
        "source": source,
    }

CIT_PUB = ("Lethwei technique and rules (standard references: Wikipedia, "
           "\"Lethwei\" - Gowl Tite headbutt, Let Thee punching, Tel Daung "
           "elbow, Kan kicking, Doo knee; traditional KO-or-draw rules with "
           "one two-minute injury timeout per corner; tape-and-gauze hand "
           "wraps; five three-minute rounds; thaing umbrella arts; banshay "
           "shadowboxing; naban controlled sparring; Lekkha Moun and "
           "Lethwei Yay traditional gestures; accessed 2026-10-17; "
           "lethwei.net, \"Knockout\" - the knockout-only rule; lethwei.com "
           "- the nine weapons; fightersvault.com, \"Lethwei Explained\" - "
           "techniques and rules; dojoandring.com - 1952 Kyar Ba Nyein "
           "modernization and 2016 World Lethwei Championship; "
           "mmafullcontact.com - banshay, naban, and kyar ba nyein "
           "training methods).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature combat "
                     "method - the nine limbs as nine covenants - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["combat-lethwei"] = _cfg(
    "combat-lethwei", "The Lethwei Combat Database",
    "Burmese bareknuckle lethwei, the art of nine limbs: real, fact-checked "
    "technique records - punches, kicks, elbows, knees, headbutts, the "
    "clinch, and traditional KO-or-draw rules - each record a technique "
    "with HOW TO DO IT step-by-step body mechanics, taught progressively "
    "along the ladder from stance to advanced traditional bouts.",
    "combat technique record", "JAH-CBLETH-", "JAH Lethwei Combat Archivist",
    "lethwei combat archivist - Burmese bareknuckle technique: the nine "
    "limbs, the clinch, and traditional rules; teaching progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["combat-lethwei-signature"] = _cfg(
    "combat-lethwei-signature", "The Lethwei Combat Signature Database",
    "His original Signature combat method: the nine limbs as nine "
    "covenants, the fighter's mark in every strike, the stance the first "
    "covenant and the knockout the final signature. The full ladder from "
    "stance and footwork through the nine weapons and the clinch to the "
    "traditional bout, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "combat technique record", "JAH-CBLETHS-", "JAH Lethwei Combat Archivist (Signature)",
    "lethwei combat archivist - Signature editions: his original Signature "
    "combat method, the nine limbs as nine covenants, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from "
    "this system",
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
    for slug in ("combat-lethwei", "combat-lethwei-signature"):
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
        assert "lethwei" in page.lower(), "field content missing in page %s" % slug
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

    # CONCURRENCY: manifest/api.json/index.html/README/AI_ACCESS and git are
    # owned by the merger. This builder stops here.
    print("manifest + api.json: SKIPPED (merger-owned)")
    print("git commit/push: SKIPPED (merger-owned)")
    print("DONE: %d databases, %d records. NEXT: merger runs restamp + commit." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
