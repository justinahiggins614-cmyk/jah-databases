#!/usr/bin/env python3
"""Build the Taekwondo Combat databases for JAH Databases
(combat batch 1, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,390 databases)
PLUS every shard index title in jah-databases-data-1: zero
'combat-taekwondo*' slugs/names; zero combat/taekwondo/martial-arts slug
hits of any kind. No existing database covers Korean taekwondo technique
instruction, so BUILD NEW is the verdict.

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-taekwondo              - The Taekwondo Combat Database
                                  (public-harvest: real, fact-checked Korean
                                  taekwondo - WT and ITF - with real Korean
                                  technique names and translations, real
                                  poomsae and tul names, every record carrying
                                  how to do it step by step, key points,
                                  requirements, standards, and citations)
  combat-taekwondo-signature    - The Taekwondo Combat Signature Database
                                  (his original Signature Combat Method:
                                  every technique a covenant of balance,
                                  every kick a signature written in the air,
                                  the form the handwriting of the spirit;
                                  src signature, titles suffixed
                                  " (Signature Edition)", never presented as
                                  authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBTKD- (public) and JAH-CBTKDS- (signature), verified free
in the manifest and in every shard index (zero hits; no substring ambiguity
with any existing prefix).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_taekwondo.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes. A merger handles those. It only writes:
  db/combat-taekwondo[-signature]/index.html + gen-*.js
  <shard-data-1>/data/combat-taekwondo[-signature]/{index.jsonl.gz,chunks/}
  ~/workspace/hidden_files/missing-builds/fragments/combat-taekwondo.json

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian martial-arts instruction only: nothing on neutralizing or defeating
military or defense-grade systems.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-taekwondo.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_taekwondo import ENTRIES, SIG_TAIL
from demos_combat_taekwondo import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat Method: "
                "every technique a covenant of balance, every kick a "
                "signature written in the air, the form the handwriting of "
                "the spirit. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked Korean taekwondo (WT "
                "and ITF): stances, hand techniques, the full kicking "
                "arsenal, poomsae and tul forms, sparring principles - "
                "every record carrying how to do it step by step, key "
                "points, requirements, standards, and citations, organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what taekwondo is, attention and bow, ready stance, front "
              "stance, back stance, horse stance, breathing and ki hap, "
              "straight punch, knife-hand, the three basic blocks, front "
              "kick) -> Compounded (roundhouse kick, side kick, back kick, "
              "axe kick, push kick, crescent kicks, hook kick, footwork, "
              "kick combinations, taegeuk poomsae, Chon-Ji tul, sparring "
              "fundamentals) -> Advanced (tornado kick, spinning hook kick, "
              "jumping kicks, double and multiple kicks, Koryo poomsae, "
              "Dan-Gun tul, counter techniques, match strategy, "
              "self-defense, breaking, the mastery path).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stances, punches, blocks, front kick, roundhouse, side kick, back kick, axe kick, poomsae, tul, sparring, breaking, combinations...",
        "chat_ph": "Ask about taekwondo technique...",
        "archive_blurb": ("Seeded %s taekwondo combat records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled taekwondo combat studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about taekwondo - from stances, bowing, breathing, punches, knife-hand, and blocks, through the full kicking arsenal and footwork, to poomsae, tul, sparring, counters, strategy, self-defense, breaking, and the mastery path." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "taekwondo-combat-study", "gen_demo_kind": "taekwondo-combat",
        "source": source,
    }

CIT_PUB = ("Taekwondo technique (standard references: Choi Hong Hi. "
           "Encyclopedia of Taekwon-Do. 15 vols. 5th ed. International "
           "Taekwon-Do Federation; 1999; Kukkiwon. Taekwondo Textbook. "
           "Seoul: Kukkiwon; 2013; World Taekwondo. Competition Rules and "
           "Interpretation, in force; World Taekwondo. Poomsae Competition "
           "Rules, in force; ITF Tournament Rules).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Combat "
                     "Method - every technique a covenant of balance, every "
                     "kick a signature written in the air - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["combat-taekwondo"] = _cfg(
    "combat-taekwondo", "The Taekwondo Combat Database",
    "Korean taekwondo, taught step by step: stances, hand techniques, the "
    "full kicking arsenal, poomsae and tul forms, sparring principles - "
    "real fact-checked technique with real Korean names and translations, "
    "every record carrying how to do it, key points, requirements, "
    "standards, and citations, ladder-ordered from basic stances to "
    "advanced forms.",
    "combat technique record", "JAH-CBTKD-", "JAH Taekwondo Combat Archivist",
    "taekwondo combat archivist - Korean taekwondo technique (WT and ITF): "
    "stances, hand techniques, the kicking arsenal, poomsae and tul forms, "
    "sparring principles; every record teaches how to do it step by step; "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["combat-taekwondo-signature"] = _cfg(
    "combat-taekwondo-signature", "The Taekwondo Combat Signature Database",
    "His original Signature Combat Method: every technique a covenant of "
    "balance, every kick a signature written in the air, the form the "
    "handwriting of the spirit. The full ladder from what taekwondo is "
    "through stances, hand techniques, and the kicking arsenal, to poomsae, "
    "tul, sparring, counters, strategy, self-defense, breaking, and the "
    "mastery path, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "combat technique record", "JAH-CBTKDS-", "JAH Taekwondo Combat Archivist (Signature)",
    "taekwondo combat archivist - Signature editions: his original "
    "Signature Combat Method, every technique a covenant of balance and "
    "every kick a signature written in the air, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this "
    "system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def preflight_dedupe():
    """Check all 68 titles against the WHOLE system before authoring."""
    refusals = []
    for slug in ("combat-taekwondo", "combat-taekwondo-signature"):
        sig = slug.endswith("-signature")
        for e in ENTRIES:
            title = e["name"] + " (Signature Edition)" if sig else e["name"]
            hits = [h for h in base.GATE.check(slug, title) if h[0] != slug]
            if hits:
                refusals.append((slug, title, hits))
    if refusals:
        for slug, title, hits in refusals:
            print("REFUSED (whole-system dupe): [%s] %r already in %s"
                  % (slug, title, ", ".join("%s:%s" % (s, i) for s, i in hits)),
                  flush=True)
        raise SystemExit("dedupe preflight failed: %d title collisions" % len(refusals))
    print("dedupe preflight: 68 titles checked vs whole system, zero collisions",
          flush=True)


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


def node_check(path):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    assert p.returncode == 0, "node --check failed for %s: %s" % (path, p.stderr[-500:])
    print("node --check clean: %s" % path, flush=True)


def main():
    if not os.path.exists("/home/hatch/workspace/hidden_files/db-writer-free.marker"):
        raise SystemExit("db-writer-free.marker absent - STOP")
    preflight_dedupe()

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
    for slug in ("combat-taekwondo", "combat-taekwondo-signature"):
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
            assert "military" not in blob and "defense-grade" not in blob, \
                "excluded topic in %s" % r["id"]
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
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)
        # node --check the gen JS and every inline page script
        node_check(gpath)
        scripts = re.findall(r"<script(?![^>]*src=)(?![^>]*ld\+json)[^>]*>(.*?)</script>",
                             page, flags=re.S | re.I)
        for i, body in enumerate(scripts):
            if body.strip():
                tmp = "/tmp/tkd-page-%s-%d.js" % (slug, i)
                with open(tmp, "w", encoding="utf-8") as f:
                    f.write(body)
                node_check(tmp)
                os.remove(tmp)

    fragment = {
        "public": {
            "slug": "combat-taekwondo",
            "name": "The Taekwondo Combat Database",
            "tagline": DBCFG["combat-taekwondo"]["tagline"],
            "record_kind": "combat technique record",
            "id_prefix": "JAH-CBTKD-",
            "ai_name": "JAH Taekwondo Combat Archivist",
            "local_index": SHARD_BASE + "/data/combat-taekwondo/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/combat-taekwondo/index.jsonl.gz",
            "chunk_pattern": "data/combat-taekwondo/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "combat-taekwondo-signature",
            "name": "The Taekwondo Combat Signature Database",
            "tagline": DBCFG["combat-taekwondo-signature"]["tagline"],
            "record_kind": "combat technique record",
            "id_prefix": "JAH-CBTKDS-",
            "ai_name": "JAH Taekwondo Combat Archivist (Signature)",
            "local_index": SHARD_BASE + "/data/combat-taekwondo-signature/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/combat-taekwondo-signature/index.jsonl.gz",
            "chunk_pattern": "data/combat-taekwondo-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(fragment, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("DONE: 2 databases, %d records. Manifest/api/merge left to the merger." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
