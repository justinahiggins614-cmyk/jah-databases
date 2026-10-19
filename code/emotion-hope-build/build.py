#!/usr/bin/env python3
"""Build the Hope Emotion databases for JAH Databases
(Manon's 16:15 orders, emotion series).

Creates two NEW databases, 34 ladder-ordered records each:

  emotion-hope            - The Hope Emotion Database
                            (public-harvest: real, fact-checked psychology of
                            hope - definition, family placement, intensity,
                            first-person simulation, body signals, facial
                            expression, triggers, behavior, healthy
                            expression, recognition in others, related
                            emotions and mixes, full behavioral simulation;
                            descriptive/educational only - never diagnosing
                            real people; standard references Snyder hope
                            theory 2002; Snyder et al. 1991; Lazarus 1999;
                            Averill, Catlin and Chon 1990; Fredrickson
                            2004; Ekman and Friesen FACS 1978; Plutchik
                            1980; Russell circumplex 1980; Lazarus 1991;
                            Frijda 1986; Scherer 2005; Barrett 2017; Darwin
                            1872; APA Dictionary of Psychology)
  emotion-hope-signature  - The Hope Emotion Signature Database
                            (his original Signature Hope Method: hope as the
                            forward signal of the system - the blueprint kept
                            on the bench, the lamp lit ahead of the build;
                            agency the drive gear, pathways the rails, vision
                            the headlamp; src signature, titles suffixed
                            " (Signature Edition)", never presented as
                            authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

ID prefixes: JAH-EMHO- (public) and JAH-EMHOS- (signature), verified free
in the manifest (zero EMHO hits across all id_prefix values) and zero hits
across all record IDs in the jah-databases-data-1 shards.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_emotion_hope.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos. Demo outputs
cross-checked against entry text during authoring.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. This script writes only: db/emotion-hope[/-signature]/
(index.html + gen-*.js), the shard dirs under jah-databases-data-1, and the
merger fragment.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Descriptive/educational only - never diagnosing real
people.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/emotion-hope.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_emotion_hope import ENTRIES, SIG_TAIL
from demos_emotion_hope import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature Hope Method: "
                "hope as the forward signal of the system - the blueprint "
                "kept on the bench, the lamp lit ahead of the build; agency "
                "the drive gear, pathways the rails, vision the headlamp. "
                "Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked psychology of the "
                "emotion of hope: what hope is, where it sits in the emotion "
                "family, mild to intense volumes, first-person simulation, "
                "body signals, the face of hope, triggers, how it shows in "
                "behavior, healthy expression, recognizing it in others, "
                "related emotions and mixes, and a full behavioral "
                "simulation - descriptive and educational only, never "
                "diagnosing real people - organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what hope is, the emotion family, intensity volumes, myths, "
              "first-person simulation, time course, low vs high hope, the "
              "hope-optimism blend, a day with hope) -> Compounded (body "
              "signals, posture and movement, sleep appetite and energy, "
              "individual differences, the face of hope, the face across "
              "intensity, hiding and faking, drawing hope, classic triggers, "
              "personal triggers, surprise triggers, chain reactions, "
              "actions, speech, decisions, behavior under intensity) -> "
              "Advanced (healthy expression, costs of mishandling, everyday "
              "practices, reading hope in others, supportive responses, "
              "mistakes to avoid, related emotions, hope blends, the full "
              "simulation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search hope definition, emotion family, intensity volumes, first-person feeling, body signals, face of hope, lifted gaze, triggers, behavior, healthy expression, reading hope in others, emotion mixes, hope blends, full simulation...",
        "chat_ph": "Ask about the emotion of hope...",
        "archive_blurb": ("Seeded %s hope emotion records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "What the Emotion Is \u00b7 How It Feels \u00b7 Body Signals \u00b7 Facial Expression \u00b7 Triggers \u00b7 How It Shows in Behavior \u00b7 Expressing It Healthily \u00b7 Recognizing It in Others \u00b7 Related Emotions and Mixes - each section opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled hope emotion studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the emotion of hope - what it is, where it sits in the emotion family, its volumes from mild to intense, what it feels like from the inside, body signals, the face of hope, triggers, behavior, healthy expression, reading it in others, related emotions and mixes, and the full behavioral simulation." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "hope-emotion-study", "gen_demo_kind": "hope-emotion-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["emotion-hope"] = _cfg(
    "emotion-hope", "The Hope Emotion Database",
    "Describe and simulate the emotion of hope: what it is, how it feels "
    "from the inside, body signals, the face of hope, triggers, behavior, "
    "healthy expression, reading it in others, related emotions and mixes, "
    "and a full behavioral simulation - real, fact-checked psychology "
    "taught progressively along the ladder, descriptive and educational "
    "only, never diagnosing real people.",
    "emotion record", "JAH-EMHO-", "JAH Hope Emotion Archivist",
    "hope emotion archivist - describing and simulating the emotion of hope "
    "across definition, family placement, intensity, first-person feeling, "
    "body signals, facial expression, triggers, behavior, healthy "
    "expression, recognition in others, related emotions and mixes, and "
    "full behavioral simulation; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, science, "
    "how-to - using only archive data from this system",
    "public")
DBCFG["emotion-hope-signature"] = _cfg(
    "emotion-hope-signature", "The Hope Emotion Signature Database",
    "His original Signature Hope Method: hope as the forward signal of the "
    "system - the blueprint kept on the bench, the lamp lit ahead of the "
    "build; agency the drive gear, pathways the rails, vision the "
    "headlamp. The full ladder from what hope is through feeling, body, "
    "face, triggers, and behavior, to healthy expression, recognition, "
    "mixes, and the full simulation, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public "
    "record.",
    "emotion record", "JAH-EMHOS-", "JAH Hope Emotion Archivist (Signature)",
    "hope emotion archivist - Signature editions: his original Signature "
    "Hope Method, hope as the forward signal of the system, agency the "
    "drive gear, pathways the rails, vision the headlamp, clearly labeled "
    "Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, science, how-to - using only "
    "archive data from this system",
    "signature")

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


def js_check(path):
    """node --check every <script> block except application/ld+json."""
    src = open(path, encoding="utf-8").read()
    blocks = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                        src, flags=re.S | re.I)
    assert blocks, "no script blocks found in %s" % path
    import tempfile
    for i, b in enumerate(blocks):
        if not b.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
            tf.write(b)
            tpath = tf.name
        try:
            p = subprocess.run(["node", "--check", tpath],
                               capture_output=True, text=True, timeout=60)
        finally:
            os.unlink(tpath)
        assert p.returncode == 0, "JS syntax fail %s block %d: %s" % (path, i, p.stderr[-500:])
    return len([b for b in blocks if b.strip()])


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
    for slug in ("emotion-hope", "emotion-hope-signature"):
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
        assert "component" not in page.lower() or "emotion" in page.lower(), \
            "field leftover in %s" % slug
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
        assert "synthetic intelligence" not in gen_js.lower(), "template leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        nblocks = js_check(ppath)
        p = subprocess.run(["node", "--check", gpath],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "gen js syntax fail %s: %s" % (slug, p.stderr[-500:])
        print("page:  db/%s/index.html + gen-%s.js [%s] js-blocks=%d node-clean"
              % (slug, slug, ", ".join(notes), nblocks), flush=True)

    # merger fragment (the merger owns manifest/api/index/README wiring)
    frag = {}
    for slug in ("emotion-hope", "emotion-hope-signature"):
        cfg = DBCFG[slug]
        key = "signature" if slug.endswith("-signature") else "public"
        frag[key] = {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": cfg["source"],
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("done: 68 records, 68 demos OK, pages + shards + fragment written; "
          "manifest/api/index/README untouched for the merger.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
