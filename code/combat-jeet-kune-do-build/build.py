#!/usr/bin/env python3
"""Build the Jeet Kune Do Combat databases for JAH Databases
(combat batch 2, 2026-10-17).

Two NEW databases, 34 ladder-ordered records each:

  combat-jeet-kune-do              - The Jeet Kune Do Combat Database
                                      (public-harvest: real, fact-checked
                                      jeet kune do knowledge - Bruce Lee's
                                      way of the intercepting fist:
                                      bai-jong stance, push-step footwork,
                                      the straight lead, the five ways of
                                      attack, pak/lop/jut sao trapping,
                                      stop hits and stop kicks, broken
                                      rhythm, economy of motion; standard
                                      references Lee Tao of Jeet Kune Do
                                      1975, Bruce Lee's Fighting Method
                                      Complete Edition 2008, Inosanto Jeet
                                      Kune Do: The Art and Philosophy of
                                      Bruce Lee 1980, Little The Warrior
                                      Within 1996)
  combat-jeet-kune-do-signature    - The Jeet Kune Do Combat Signature
                                      Database
                                      (his original Signature combat method:
                                      every technique a covenant of body and
                                      breath, the stance the oath of the
                                      ground, the intercepting fist the
                                      signature of the reader of motion;
                                      src signature, titles suffixed
                                      " (Signature Edition)", never
                                      presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBJKD- (public) and JAH-CBJKDS- (signature), verified free
in the manifest id_prefix values and zero hits in every shard index file.

Dedupe: all 68 titles run through the whole-system dedupe gate before
authoring - zero refusals, zero collisions.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_jeet_kune_do.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Screening: civilian martial-arts instruction only. Nothing on neutralizing
or defeating military or defense-grade systems - the standing exclusion
holds.

CONCURRENCY: this builder does NOT touch data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and does NOT git commit or
push. A merger handles those. Outputs: db/<slug>/{index.html,gen-<slug>.js}
x2, shard data dirs x2, and the fragment file (written by the caller).

Never the words "bat belt" anywhere. No website references. No Facebook.
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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_jeet_kune_do import ENTRIES, SIG_TAIL
from demos_combat_jeet_kune_do import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature combat method: "
                "every technique a covenant of body and breath, the stance "
                "the oath of the ground, the intercepting fist the signature "
                "of the reader of motion, trapping the handshake that never "
                "lets go. Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked jeet kune do knowledge: "
                "Bruce Lee's way of the intercepting fist - the bai-jong "
                "on-guard stance, push-step footwork, the straight lead, the "
                "five ways of attack, pak sao / lop sao / jut sao trapping, "
                "stop hits and stop kicks, broken rhythm and economy of "
                "motion - every technique taught as a full record with "
                "step-by-step body mechanics, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (the "
              "bai-jong stance, advance and retreat footwork, the guard with "
              "parry and cover, the straight lead, the cross, the lead hook, "
              "the uppercut, lateral footwork, the first trapping touch, the "
              "slip and the duck) -> Compounded (the five ways of attack: "
              "single direct attack, attack by combination, progressive "
              "indirect attack, hand immobilization attack, attack by "
              "drawing; pak sao, lop sao, jut sao; the lead side kick, the "
              "hook kick, the low lead kick; the stop hit, the stop kick, "
              "broken rhythm) -> Advanced (economy of motion, the time hit, "
              "trapping flow drills, the stop-thrust, the low line stop, "
              "attack on preparation, cadence traps, centerline theory, "
              "simultaneous parry and hit, the sparring synthesis).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search bai-jong, straight lead, five ways of attack, pak sao, lop sao, trapping, stop hit, stop kick, broken rhythm, centerline, interception...",
        "chat_ph": "Ask about jeet kune do...",
        "archive_blurb": ("Seeded %s jeet kune do combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled jeet kune do studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about jeet kune do - from the bai-jong stance, footwork, guard, straight lead, cross, hook, and uppercut, through the five ways of attack, pak sao, lop sao, jut sao, the kicks, stop hits, stop kicks, and broken rhythm, to economy of motion, time hits, flow drills, the stop-thrust, attack on preparation, centerline theory, and the sparring synthesis." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "jeet-kune-do-study", "gen_demo_kind": "jeet-kune-do-demo",
        "source": source,
    }

CIT_PUB = ("Jeet kune do (standard references: Lee B. Tao of Jeet Kune Do. "
           "Santa Clarita: Ohara Publications; 1975; Lee B. Bruce Lee's "
           "Fighting Method: The Complete Edition. Valencia: Black Belt "
           "Communications; 2008; Inosanto D. Jeet Kune Do: The Art and "
           "Philosophy of Bruce Lee. Los Angeles: Know Now Publishing; 1980; "
           "Little J, ed. The Warrior Within: The Philosophies of Bruce Lee. "
           "Chicago: Contemporary Books; 1996).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature combat "
                     "method - every technique a covenant of body and breath, "
                     "the intercepting fist the signature of the reader of "
                     "motion - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["combat-jeet-kune-do"] = _cfg(
    "combat-jeet-kune-do", "The Jeet Kune Do Combat Database",
    "Bruce Lee's way of the intercepting fist: real, fact-checked jeet kune "
    "do - the bai-jong stance, footwork, the straight lead, the five ways of "
    "attack, trapping, stop hits and stop kicks, broken rhythm and economy "
    "of motion - every technique taught as a full record with step-by-step "
    "body mechanics, progressively along the ladder.",
    "combat technique record", "JAH-CBJKD-", "JAH Jeet Kune Do Combat Archivist",
    "jeet kune do combat archivist - teaching the way of the "
    "intercepting fist: stance, footwork, hand and foot weapons, the five "
    "ways of attack, trapping, and interception timing; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this "
    "system",
    CIT_PUB, "public")
DBCFG["combat-jeet-kune-do-signature"] = _cfg(
    "combat-jeet-kune-do-signature", "The Jeet Kune Do Combat Signature Database",
    "His original Signature combat method: every technique a covenant of "
    "body and breath, the stance the oath of the ground, the intercepting "
    "fist the signature of the reader of motion, trapping the handshake that "
    "never lets go. The full ladder from bai-jong through the five ways of "
    "attack and trapping to interception mastery, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "combat technique record", "JAH-CBJKDS-", "JAH Jeet Kune Do Combat Archivist (Signature)",
    "jeet kune do combat archivist - Signature editions: his original "
    "Signature combat method, every technique a covenant of body and breath "
    "and the intercepting fist the signature of the reader of motion, "
    "clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
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


def node_check_js(label, code):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(code)
        path = f.name
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    os.unlink(path)
    assert p.returncode == 0, "node --check failed for %s: %s" % (label, p.stderr[-800:])


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
    for slug in ("combat-jeet-kune-do", "combat-jeet-kune-do-signature"):
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
        assert "jeet-kune-do" in page or "jeet kune do" in page.lower()
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        for m in re.finditer(r"<script(?![^>]*src=)(?![^>]*ld\+json)[^>]*>(.*?)</script>", page, re.S):
            node_check_js("%s inline script" % slug, m.group(1))
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
        node_check_js("gen-%s.js" % slug, gen_js)
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s] (node --check clean)" % (slug, slug, ", ".join(notes)), flush=True)

    print("built 2 databases, %d records; manifest/api/index/README left for the merger" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
