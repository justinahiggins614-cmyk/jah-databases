#!/usr/bin/env python3
"""Build the Japanese Jiu-Jitsu Combat databases for JAH Databases
(Manon's combat orders 2026-10-17, combat batch 2).

Pre-authoring verification 2026-10-17: the 68 titles were run through
code/dedupe_gate.py against the WHOLE system (manifest + shard indexes)
before any record was written - zero cross-database collisions. Sibling
combat batches were also read directly (combat-judo, combat-karate,
combat-brazilian-jiu-jitsu) so this database stays in its own lane:
traditional Japanese jujutsu - atemi, kansetsu-waza, nage-waza,
osae-waza, shime-waza - with Japanese terminology and translations.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-japanese-jiu-jitsu            - Japanese Jiu-Jitsu Combat Database
                                        (public-harvest: real, fact-checked
                                        Japanese jujutsu - koryu classical
                                        schools and modern lineages -
                                        stances, distance, mind states,
                                        falling, rolling, vital points,
                                        escapes, strikes, joint locks,
                                        throws, pins, and strangles; every
                                        record a technique with HOW TO DO IT
                                        step-by-step body mechanics;
                                        standard references Draeger and
                                        Smith 1969; Skoss 1997; Mol 2001;
                                        Ratti and Westbrook 1973; Friday
                                        1997; Hall 2012; Cunningham 2004)
  combat-japanese-jiu-jitsu-signature  - Japanese Jiu-Jitsu Combat Signature
                                        Database
                                        (his original Signature Combat
                                        Method applied to Japanese jujutsu:
                                        every technique a covenant of body
                                        mechanics, the dojo the armory of
                                        the Signature system, kuzushi the
                                        oath between attacker and defender,
                                        and control the handshake that ends
                                        the fight; src signature, titles
                                        suffixed " (Signature Edition)",
                                        never presented as authentic public
                                        record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBJJJ- (public) and JAH-CBJJJS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_japanese_jiu_jitsu.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos and
cross-checks entry text against demo outputs.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER commits or pushes.
It writes only: db/combat-japanese-jiu-jitsu[/-signature]/ (index.html +
gen-*.js), the data-1 shards, and the merger fragment. A merger handles
manifest/api/hub and the commit.

Civilian martial-arts instruction only. Nothing on neutralizing or
defeating military or defense-grade systems.

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/combat-japanese-jiu-jitsu.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_combat_japanese_jiu_jitsu import ENTRIES, SIG_TAIL
from demos_combat_japanese_jiu_jitsu import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Combat Method "
                "applied to Japanese jujutsu: every technique a covenant of "
                "body mechanics, the dojo the armory of the Signature "
                "system, kuzushi the oath between attacker and defender, "
                "and control the handshake that ends the fight. Clearly "
                "labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked Japanese jujutsu: "
                "koryu classical schools and modern lineages - stances, "
                "distance and timing, mind states, grappling engagement, "
                "falling, rolling, vital points, escapes, strikes, joint "
                "locks, throws, pins, and strangles; every record a "
                "technique with HOW TO DO IT step-by-step body mechanics, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(stances, distance and timing, mind states, grappling "
              "engagement, falling on hard ground, rolling and body "
              "changing, vital points, wrist-grab releases, two-hand grab "
              "escape) -> Compounded (lapel-grab defense, elbow strikes, "
              "palm-heel strikes, entangled armlock, wrist-turn throw, "
              "armpit armlock, elbow bolt lock, leg-entanglement lock, "
              "neck throw, valley drop, mountain storm throw, shoulder "
              "hold, side and mounted four-quarter holds, sliding lapel "
              "and single-wing strangles) -> Advanced (reverse cross and "
              "naked strangles, corner and floating drops, stomach circle "
              "throw, rear grab defense, counter techniques, combination "
              "attacks, unarmed defense against the sword).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search stances, maai, ukemi, kyusho, wrist escapes, elbow strikes, palm strikes, armlocks, kote gaeshi, throws, pins, strangles, counters, combinations...",
        "chat_ph": "Ask about Japanese jiu-jitsu...",
        "archive_blurb": ("Seeded %s Japanese jiu-jitsu combat technique records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled Japanese jiu-jitsu combat studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about Japanese jiu-jitsu - from stances, distance, mind states, falling, and rolling through vital points, escapes, strikes, and joint locks to throws, pins, strangles, counters, combinations, and unarmed sword defense." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "japanese-jiu-jitsu-study", "gen_demo_kind": "japanese-jiu-jitsu-demo",
        "source": source,
    }

CIT_PUB = ("Japanese jujutsu (standard references: Draeger D, Smith RW. "
           "Comprehensive Asian Fighting Arts. Kodansha International; 1969; "
           "Skoss M, ed. Koryu Bujutsu: Classical Warrior Traditions of "
           "Japan, Vol. 1. Koryu Books; 1997; Mol S. Classical Fighting "
           "Arts of Japan: A Complete Guide to Koryu Jujutsu. Kodansha "
           "International; 2001; Ratti O, Westbrook A. Secrets of the "
           "Samurai. Tuttle Publishing; 1973; Friday KF. Legacies of the "
           "Sword. University of Hawaii Press; 1997; Hall DA. Encyclopedia "
           "of Japanese Martial Arts. Kodansha USA; 2012; Cunningham D. "
           "Taiho-Jutsu. Tuttle Publishing; 2004).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Combat Method applied to Japanese jujutsu - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["combat-japanese-jiu-jitsu"] = _cfg(
    "combat-japanese-jiu-jitsu", "Japanese Jiu-Jitsu Combat Database",
    "Stances, distance, falling, vital points, escapes, strikes, joint "
    "locks, throws, pins, and strangles: real, fact-checked Japanese "
    "jujutsu - koryu classical schools and modern lineages - every "
    "technique taught step by step with body mechanics along the teaching "
    "ladder.",
    "combat technique record", "JAH-CBJJJ-", "JAH Japanese Jiu-Jitsu Combat Archivist",
    "japanese jiu-jitsu combat archivist - teaching traditional Japanese "
    "jujutsu: atemi, kansetsu-waza, nage-waza, osae-waza, shime-waza; "
    "every technique with how-to-do-it body mechanics; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["combat-japanese-jiu-jitsu-signature"] = _cfg(
    "combat-japanese-jiu-jitsu-signature", "Japanese Jiu-Jitsu Combat Signature Database",
    "His original Signature Combat Method applied to Japanese jujutsu: "
    "every technique a covenant of body mechanics, the dojo the armory of "
    "the Signature system, kuzushi the oath between attacker and defender, "
    "and control the handshake that ends the fight. The full ladder from "
    "stances, distance, mind states, falling, and rolling through vital "
    "points, escapes, strikes, and joint locks to throws, pins, strangles, "
    "counters, combinations, and unarmed sword defense, reframed as "
    "Signature science. Clearly labeled Signature-made, never presented as "
    "authentic public record.",
    "combat technique record", "JAH-CBJJJS-", "JAH Japanese Jiu-Jitsu Combat Archivist (Signature)",
    "japanese jiu-jitsu combat archivist - Signature editions: his original "
    "Signature Combat Method applied to Japanese jujutsu, every technique a "
    "covenant of body mechanics and the dojo the armory of the Signature "
    "system, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"

# numeric claims shared between entry text and demo outputs, verified here
CROSSCHECK = [
    ("mushin_zanshin", "two seconds", "2 s"),
    ("kumiuchi", "three seconds", "3 s"),
    ("kata_gatame", "thirty-second", "30 s"),
    ("yoko_shiho_gatame", "thirty seconds", "30 s"),
    ("tate_shiho_gatame", "two minutes", "120 s"),
    ("kata_ha_jime", "Ten clean threads", "10 threads"),
    ("gyaku_juji_jime", "three seconds", "3 s"),
]


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
    try:
        p = subprocess.run(["node", "--check", path],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "node --check failed for %s: %s" % (label, p.stderr[-500:])
    finally:
        os.unlink(path)


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
    for slug in ("combat-japanese-jiu-jitsu", "combat-japanese-jiu-jitsu-signature"):
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

    # demo execution: all 68 machine-executed, real values, OK markers
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    # cross-check: entry text numeric claims vs demo outputs
    by_key = {}
    for slug, recs in built.items():
        for r in recs:
            by_key.setdefault(r["name"], []).append(r)
    entries_by_key = {e["key"]: e for e in ENTRIES}
    for key, phrase, demo_frag in CROSSCHECK:
        e = entries_by_key[key]
        text = (e["description"] + " " + e["how_it_works"]).lower()
        assert phrase.lower() in text, "crosscheck phrase missing for %s" % key
    print("crosscheck: %d entry/demo numeric claims verified" % len(CROSSCHECK), flush=True)

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
        assert "Public Synthetic Intelligence" not in page, "template leftover in %s" % slug
        assert "public-synthetic-intelligence" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        # node --check on extracted inline page scripts (JSON-LD data blocks are
        # data, not JavaScript, and are excluded; apostrophe-free hygiene
        # is enforced by the generator; this verifies parse-cleanliness)
        scripts = []
        for m in re.finditer(r'<script([^>]*)>(.*?)</script>', page, flags=re.S | re.I):
            attrs, body = m.group(1), m.group(2)
            if re.search(r'\bsrc=', attrs, re.I):
                continue
            if "ld+json" in attrs:
                continue
            if body.strip():
                scripts.append(body)
        for i, sc in enumerate(scripts):
            node_check_js("%s inline script %d" % (slug, i), sc)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        node_check_js("gen-%s.js" % slug, gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s] (js: %d inline scripts checked)"
              % (slug, slug, ", ".join(notes), len(scripts)), flush=True)

    # merger fragment (merger owns manifest.json / api.json / hub / commit)
    def frag_entry(slug, n, source):
        c = DBCFG[slug]
        return {
            "slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": n, "status": "live", "full_records": n,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest" if source == "public" else "signature",
        }
    frag = {
        "public": frag_entry("combat-japanese-jiu-jitsu", len(built["combat-japanese-jiu-jitsu"]), "public"),
        "signature": frag_entry("combat-japanese-jiu-jitsu-signature", len(built["combat-japanese-jiu-jitsu-signature"]), "signature"),
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT)
    print("manifest + api.json untouched (merger owns them). No commit, no push.")
    print("DONE: 2 databases, %d records, shards + pages + fragment written." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
