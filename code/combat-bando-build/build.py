#!/usr/bin/env python3
"""Build the Bando Combat databases for JAH Databases
(Manon's combat orders 2026-10-17, combat batch 3).

Terminology fact-checked 2026-10-17 against Wikipedia 'Bando' (nine ABA
animal systems - bull, boar, cobra, viper, python, panther, tiger,
scorpion, eagle; aka = empty-handed forms/kata; basics taught as stances
and footholds for months; black belt requires aka, stick weapons, bladed
weapons, sparring, and a fitness test with minimum five years training;
belts white, green, brown, black; Maung Gyi taught Hanthawaddy bando in
Washington DC from the early 1960s; 9x9 technique-principle matrix),
the encyclopedia entries (boar = furious powerful rushes, cobra =
lightning fast strikes to vital targets, python = wraps and crushes;
strategies emulated, not mimicry; free fighting/middle style similar to
tournament karate; related arts lethwei bareknuckle striking and naban
Burmese wrestling), and the seven thaing systems (bando empty-hand
combat, banshay weapons, lethwei, naban grappling, shan thaing
soft/internal, khut thaing pressure point techniques, arweththa mental
discipline).

Creates two NEW databases, 34 ladder-ordered records each:

  combat-bando              - The Bando Combat Database
                              (public-harvest: real, fact-checked Burmese
                              bando - the hand-to-hand complement to the
                              thaing weapon arts - each record a technique
                              with HOW TO DO IT step-by-step body
                              mechanics, ladder-ordered from basics to
                              advanced; civilian traditional-art scope)
  combat-bando-signature    - The Bando Combat Signature Database
                              (his original Signature combat method: the
                              empty hand as the signature itself, every
                              technique a covenant of balance, the nine
                              animal strategies as nine covenants; src
                              signature, titles suffixed " (Signature
                              Edition)", clearly labeled Signature-made,
                              never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBBD- (public) and JAH-CBBDS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_bando.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing
pages.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. Only db/combat-bando*/, code/combat-bando-build,
the shard data dirs, and the fragment file are written.

Never the words "bat belt" anywhere. No website references. No Facebook.

SCREENING: civilian traditional-art instruction only - nothing
hate-adjacent, profane, or inappropriate; no religious talk; nothing on
neutralizing or defeating military or defense-grade systems.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

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
from entries_combat_bando import ENTRIES, SIG_TAIL
from demos_combat_bando import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature combat "
                "method: the empty hand as the signature itself, every "
                "technique a covenant of balance, the nine animal "
                "strategies as nine covenants, the stance the first "
                "covenant and mastery the final signature. Clearly "
                "labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked Burmese bando, the "
                "hand-to-hand complement to the thaing weapon arts: "
                "stances and footholds, the core strikes, kicking, "
                "parries and guards, breakfalls, aka empty-hand forms, "
                "the nine animal systems (bull, boar, cobra, viper, "
                "python, panther, tiger, scorpion, eagle), naban "
                "grappling, khut thaing pressure-point study, "
                "combinations, counters, and the 9x9 technique-principle "
                "matrix - every record a technique with HOW TO DO IT "
                "step-by-step body mechanics, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what bando means, the ready stance and footholds, "
              "stepping, the straight punch, the backfist and hammer "
              "strike, the open-hand chop and palm heel, the elbow "
              "strike, the parry and forearm guard, the knee strike, the "
              "front kick, the bando low kick, the breakfall) -> "
              "Compounded (the first aka, tiger raking strikes, boar "
              "rushing entry, eagle hooking and grasping, cobra "
              "lightning hand strikes, viper sinuous evasion, python "
              "wraps and crushes, panther sweep, bull charging power, "
              "scorpion deceptive strikes, naban standing clinch "
              "control, naban hip throw) -> Advanced (naban ground "
              "holds and pins, khut thaing pressure-point study, "
              "combination chains, counter-attack timing, positioning "
              "against multiple attackers, close-quarter elbow and "
              "knee chains, the sweep-to-throw chain, the advanced aka, "
              "controlled sparring, the 9x9 matrix).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stances, footholds, stepping, straight punches, backfists, hammer strikes, chops, palm heels, elbows, parries, knees, front kicks, low kicks, breakfalls, aka forms, tiger, boar, eagle, cobra, viper, python, panther, bull, scorpion, naban, clinch, hip throws, pins, khut thaing, combinations, counters, sweeps, sparring, 9x9 matrix...",
        "chat_ph": "Ask about bando techniques...",
        "archive_blurb": ("Seeded %s bando combat technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled bando combat technique studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about bando - from what the empty hand means, the ready stance and footholds, stepping, the straight punch, the backfist and hammer strike, the open-hand chop and palm heel, the elbow, the parry and guard, the knee, the front kick, the low kick, and the breakfall, through the first aka, the tiger, boar, eagle, cobra, viper, python, panther, bull, and scorpion systems, naban clinch and hip throw, to ground pins, khut thaing study, combinations, counters, multiple-attacker positioning, close-quarter chains, the sweep-to-throw chain, the advanced aka, controlled sparring, and the 9x9 matrix." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "bando-combat-study", "gen_demo_kind": "bando-combat-demo",
        "source": source,
    }

CIT_PUB = ("Bando technique and tradition (standard references: Maung Gyi. "
           "Bando: Philosophy, Principles and Practice. Xlibris; 2000; "
           "Wikipedia, \"Bando\" - nine ABA animal systems (bull, boar, "
           "cobra, viper, python, panther, tiger, scorpion, eagle), aka "
           "empty-handed forms, stances and footholds as the preliminary "
           "stage, black belt requirements and minimum five years, belts "
           "white green brown black, Maung Gyi Hanthawaddy style taught "
           "in Washington DC from the early 1960s, 9x9 "
           "technique-principle matrix; accessed 2026-10-17; American "
           "Bando Association - the nine animal systems, aka forms, "
           "naban grappling; Myanmar Thaing Federation - the seven "
           "thaing systems: bando, banshay, lethwei, naban, shan thaing, "
           "khut thaing, arweththa; Hay JG. The Biomechanics of Sports "
           "Techniques. 4th ed. Prentice-Hall; 1993 - striking and "
           "kicking mechanics).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature combat "
                     "method - the empty hand as the signature itself, "
                     "every technique a covenant of balance - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["combat-bando"] = _cfg(
    "combat-bando", "The Bando Combat Database",
    "Burmese bando, the empty-hand complement to the thaing weapon arts: "
    "real, fact-checked technique records - stances, strikes, kicks, "
    "defenses, aka forms, the nine animal systems, naban grappling, and "
    "the 9x9 matrix - each record a technique with HOW TO DO IT "
    "step-by-step body mechanics, taught progressively along the ladder "
    "from basics to advanced.",
    "combat technique record", "JAH-CBBD-", "JAH Bando Combat Archivist",
    "bando combat archivist - Burmese empty-hand technique: stances, "
    "strikes, kicks, defenses, aka forms, the nine animal systems, naban "
    "grappling, and the 9x9 technique-principle matrix; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive "
    "data from this system",
    CIT_PUB, "public")
DBCFG["combat-bando-signature"] = _cfg(
    "combat-bando-signature", "The Bando Combat Signature Database",
    "His original Signature combat method: the empty hand as the "
    "signature itself, every technique a covenant of balance, the nine "
    "animal strategies as nine covenants, the stance the first covenant "
    "and mastery the final signature. The full ladder from what bando "
    "means through strikes, kicks, forms, the animal systems, and naban "
    "grappling to the 9x9 matrix, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public "
    "record.",
    "combat technique record", "JAH-CBBDS-", "JAH Bando Combat Archivist (Signature)",
    "bando combat archivist - Signature editions: his original Signature "
    "combat method, the empty hand as the signature itself and every "
    "technique a covenant of balance, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, "
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


def node_check(path, label):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    assert p.returncode == 0, "node --check failed %s (%s): %s" % (label, path, p.stderr[-500:])
    return True


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
    for slug in ("combat-bando", "combat-bando-signature"):
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
        assert "bando" in page.lower(), "field content missing in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        # node --check on extracted inline page scripts (skip JSON-LD data blocks)
        scripts = []
        for m in re.finditer(r"<script([^>]*)>(.*?)</script>", page, re.S | re.I):
            attrs, body = m.group(1), m.group(2)
            if "src=" in attrs.lower():
                continue
            tm = re.search(r'type\s*=\s*["\']([^"\']+)', attrs, re.I)
            if tm and "javascript" not in tm.group(1).lower() and "ecmascript" not in tm.group(1).lower() and "module" not in tm.group(1).lower():
                continue
            scripts.append(body)
        checked = 0
        for i, body in enumerate(scripts):
            if body.strip():
                with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                    tf.write(body)
                    tfp = tf.name
                node_check(tfp, "%s inline script %d" % (slug, i))
                os.unlink(tfp)
                checked += 1
        print("page scripts node --check: %d inline scripts clean [%s]" % (checked, slug), flush=True)
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
        node_check(gpath, "gen-%s.js" % slug)
        print("page:  db/%s/index.html + gen-%s.js node --check clean [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # fragment for the merger (metadata only - merger owns manifest/api)
    os.makedirs(FRAGMENTS, exist_ok=True)
    frag = {}
    for key, slug in (("public", "combat-bando"), ("signature", "combat-bando-signature")):
        cfg = DBCFG[slug]
        idx_url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        frag[key] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": idx_url,
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": idx_url,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest" if key == "public" else "signature",
        }
    fpath = os.path.join(FRAGMENTS, "combat-bando.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath, flush=True)

    # CONCURRENCY: manifest/api.json/index.html/README/AI_ACCESS and git are
    # owned by the merger. This builder stops here.
    print("manifest + api.json: SKIPPED (merger-owned)")
    print("git commit/push: SKIPPED (merger-owned)")
    print("DONE: %d databases, %d records. NEXT: merger runs restamp + commit." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
