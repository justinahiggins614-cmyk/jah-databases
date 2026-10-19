#!/usr/bin/env python3
"""Build The Surprise Emotion Database (emotion-surprise / -signature).

Manon's 2026-10-17 16:15 order, emotion series batch 1: one database per
emotion - the archive must be able to describe or simulate emotions and
human behavior. Shared 34-record spec from
~/workspace/hidden_files/new-orders-1540/emotion-template.md: what the
emotion IS -> first-person simulation -> body signals -> facial expression ->
triggers -> behavior -> healthy expression -> recognizing it in others ->
related emotions and mixes -> full behavioral simulation.
DESCRIPTIVE/EDUCATIONAL ONLY - never diagnoses real people.

Pipeline replicates code/component-parts-catalog-build/build.py exactly for
page structure and pipeline, EXCEPT this builder never touches
data/manifest.json, api.json, index.html, README.md, or docs/AI_ACCESS.md,
and never git commits or pushes - a merger handles those. This builder ONLY
creates: db/emotion-surprise/ + db/emotion-surprise-signature/ (index.html +
gen-*.js each); the shard dirs under ~/workspace/jah-databases-data-1/data/;
and the fragment ~/workspace/hidden_files/missing-builds/fragments/emotion-surprise.json.

Public edition: real, fact-checked psychology knowledge about surprise
(Ekman, Plutchik, Scherer, Lazarus, Russell, Panksepp, LeDoux, Sokolov).
Signature edition: the same ladder through the Signature lens - surprise as
the mind's Signal Bell; src 'signature', titles suffixed ' (Signature
Edition)', clearly labeled Signature-made, never presented as authentic
public record.

ID prefixes JAH-EMSU- / JAH-EMSUS- verified free 2026-10-17: zero hits in
manifest id_prefix values (2,442 databases) and zero hits across all 857
shard index files in jah-databases-data-1, plus zero 'emotion-surprise'
slug hits anywhere. All 68 titles pre-checked against the whole-system
exact dedupe index: zero cross-database collisions.

Every demo is an emotion-scenario simulator: real, runnable, stdlib-only
Python, machine-executed here. Each prints real computed values, asserts
tight bounds (never float exact-equality), cross-checks its output against
its entry's text, and ends with the OK marker.

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/emotion-surprise.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_emotion_surprise import ENTRIES, SIG_TAIL
from demos_emotion_surprise import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature lens on the "
                "human emotional system: surprise read as the mind's Signal "
                "Bell, the early-warning instrument that turns novelty into "
                "data; the body its alarm panel, the face its beacon, and "
                "the healthy response the Signature habit of letting the "
                "bell ring, reading the message, and choosing the next move "
                "on purpose. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("Public records - real, fact-checked psychology of surprise: "
                "what surprise is, how it feels from the inside, body "
                "signals, the facial expression, triggers, behavior, "
                "healthy expression, recognizing it in others, related "
                "emotions and mixes, and full behavioral simulation - "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what surprise is, where it sits in the emotion family, its "
              "volumes, myths, the first-person passage, its time course, "
              "low vs high intensity, the fear blend, a day in the life, "
              "body signals, posture and movement) -> Compounded (sleep "
              "appetite and energy, bodily differences, the face of "
              "surprise, the expression at intensities, hiding and faking, "
              "the artist's notes, classic triggers, personal triggers, odd "
              "triggers, chain reactions, surprised behavior, surprised "
              "speech, surprise and judgment) -> Advanced (escalation, "
              "healthy expression, unhealthy expression, everyday "
              "practices, reading surprise in others, supportive responses, "
              "what not to do, the emotion map, the four blends, the full "
              "simulation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it unfolds, "
                  "key points, reading notes, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search surprise, startle, facial expression, triggers, body signals, blends, delight, alarm...",
        "chat_ph": "Ask about surprise...",
        "archive_blurb": ("Seeded %s surprise emotion records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled surprise emotion studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about surprise - what it is, how it feels, body signals, the face, triggers, behavior, healthy expression, reading it in others, blends, and full behavioral simulation." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "emotion-surprise-study", "gen_demo_kind": "emotion-surprise-demo",
        "source": source,
    }

CIT_PUB = ("Psychology of emotion (standard references: Ekman P. An argument "
           "for basic emotions. Cognition and Emotion 1992; Ekman P, Friesen "
           "WV. Facial Action Coding System. Consulting Psychologists Press; "
           "1978; Plutchik R. Emotion: A Psychoevolutionary Synthesis. Harper "
           "and Row; 1980; Lazarus RS. Emotion and Adaptation. Oxford "
           "University Press; 1991; Scherer KR. Appraisal considered as a "
           "process of multilevel sequential checking. Oxford University "
           "Press; 2001; Russell JA. A circumplex model of affect. JPSP 1980; "
           "Panksepp J. Affective Neuroscience. Oxford University Press; "
           "1998; Sokolov EN. The orienting reflex. Ann Rev Physiol 1963; "
           "Schachter S, Singer JE. Cognitive, social, and physiological "
           "determinants of emotional state. Psych Rev 1962; Barrett LF. How "
           "Emotions Are Made. Houghton Mifflin Harcourt; 2017; LeDoux JE. "
           "The Emotional Brain. Simon and Schuster; 1996; Gross JJ. Emotion "
           "regulation. Psychophysiology 2002).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature lens on "
                     "the human emotional system - surprise as the mind's "
                     "Signal Bell - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["emotion-surprise"] = _cfg(
    "emotion-surprise", "The Surprise Emotion Database",
    "Surprise, the mind's signal bell: what it is, how it feels from the "
    "inside, body signals, the facial expression, triggers, behavior, "
    "healthy expression, recognizing it in others, related emotions and "
    "mixes, and full behavioral simulation - descriptive and educational, "
    "taught progressively along the ladder.",
    "emotion record", "JAH-EMSU-", "JAH Surprise Emotion Archivist",
    "surprise emotion archivist - describing and simulating the surprise "
    "emotion and human behavior: what surprise is, how it feels, body "
    "signals, facial expression, triggers, behavior, healthy expression, "
    "recognition in others, mixes, and full simulation; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, how-it-unfolds - using only archive data from "
    "this system; descriptive and educational only, never diagnosing anyone",
    CIT_PUB, "public")
DBCFG["emotion-surprise-signature"] = _cfg(
    "emotion-surprise-signature", "The Surprise Emotion Signature Database",
    "His original Signature lens on surprise: the mind's Signal Bell, the "
    "early-warning instrument that turns novelty into data - the body its "
    "alarm panel, the face its beacon. The full ladder from what surprise "
    "is through how it feels, body signals, expression, triggers, and "
    "behavior, to healthy expression, recognition, mixes, and the full "
    "simulation, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "emotion record", "JAH-EMSUS-", "JAH Surprise Emotion Archivist (Signature)",
    "surprise emotion archivist - Signature editions: his original "
    "Signature lens on the human emotional system, surprise as the Signal Bell "
    "of the mind, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; descriptive and "
    "educational only, never diagnosing anyone",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"

# demo output must echo a key term from its entry's text (cross-check)
XCHECK = {
    "def1": ["mismatch"], "family": ["delight", "alarm"],
    "volumes": ["volume", "moderate"], "myths": ["myth"],
    "firstperson": ["bright blank"], "timecourse": ["aftershock"],
    "lowhigh": ["whisper"], "mixfear": ["fear"], "dayinlife": ["landing"],
    "body": ["gasp"], "posture": ["crouch", "discharge"], "sleep": ["threshold"],
    "differences": ["instrument"], "face": ["brow"], "intensityface": ["flicker"],
    "hidefake": ["leak"], "artist": ["brows"], "classictriggers": ["break"],
    "personaltriggers": ["network"], "oddtriggers": ["confidence"],
    "chains": ["cascade"], "behaviors": ["freeze"], "speech": ["gasp"],
    "judgment": ["tilt"], "escalation": ["stage"], "healthyexpr": ["permission"],
    "unhealthy": ["books"], "practices": ["instrument"], "reading": ["channels"],
    "support": ["steadiness"], "nottodo": ["instrument"], "emomap": ["map"],
    "blends": ["landing"], "fullsim": ["trigger"],
}


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


def js_hygiene(ddir, slug):
    """node --check on extracted page scripts (excluding ld+json) and gen-*.js."""
    ppath = os.path.join(ddir, "index.html")
    with open(ppath, "r", encoding="utf-8") as f:
        page = f.read()
    blocks = []
    for m in re.finditer(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                         page, re.S):
        body = m.group(1).strip()
        if body:
            blocks.append(body)
    assert blocks, "no script blocks found in %s" % ppath
    tmpd = tempfile.mkdtemp(prefix="emsu-js-")
    checked = 0
    for i, body in enumerate(blocks):
        p = os.path.join(tmpd, "page-%d.js" % i)
        with open(p, "w", encoding="utf-8") as f:
            f.write(body)
        r = subprocess.run(["node", "--check", p], capture_output=True, text=True)
        assert r.returncode == 0, "node --check failed on page script %d: %s" % (i, r.stderr[:500])
        checked += 1
    gen = os.path.join(ddir, "gen-%s.js" % slug)
    r = subprocess.run(["node", "--check", gen], capture_output=True, text=True)
    assert r.returncode == 0, "node --check failed on %s: %s" % (gen, r.stderr[:500])
    checked += 1
    print("js hygiene: node --check clean on %d page scripts + gen-%s.js" % (len(blocks), slug),
          flush=True)
    return checked


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

    # apostrophe-free JS-embedded strings
    for slug, c in DBCFG.items():
        for k in ("ai", "role", "greet", "search_ph"):
            assert "'" not in c[k], "apostrophe in %s.%s" % (slug, k)

    built = {}
    for slug in ("emotion-surprise", "emotion-surprise-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    demo_outputs = {}
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

    # machine-execute all demos + cross-check entry text vs demo outputs
    for slug, recs in built.items():
        key_of = {r["id"]: None for r in recs}
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            demo_outputs[(slug, r["id"])] = p.stdout
    print("demo execution: all %d demos ran OK" % total, flush=True)

    for slug, recs in built.items():
        for r in recs:
            key = [e["key"] for e in ENTRIES if e["name"] == r["name"]][0]
            out = demo_outputs[(slug, r["id"])]
            blob = (r["description"] + " " + r["how_it_works"]).lower()
            for term in XCHECK[key]:
                assert term in out.lower(), "demo output missing %r (%s)" % (term, r["id"])
                assert term in blob, "entry text missing %r (%s)" % (term, r["id"])
    print("cross-check: demo outputs echo entry text for all %d records" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        if "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries." in page:
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
        assert "Emotion Database" in page or "emotion" in page.lower()
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
        js_hygiene(ddir, slug)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # fragment for the merger (manifest/api/index/README/docs handled by merger)
    frag = {
        "public": {
            "slug": "emotion-surprise",
            "name": "The Surprise Emotion Database",
            "tagline": DBCFG["emotion-surprise"]["tagline"],
            "record_kind": "emotion record",
            "id_prefix": "JAH-EMSU-",
            "ai_name": "JAH Surprise Emotion Archivist",
            "local_index": SHARD_BASE + "/data/emotion-surprise/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/emotion-surprise/index.jsonl.gz",
            "chunk_pattern": "data/emotion-surprise/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "emotion-surprise-signature",
            "name": "The Surprise Emotion Signature Database",
            "tagline": DBCFG["emotion-surprise-signature"]["tagline"],
            "record_kind": "emotion record",
            "id_prefix": "JAH-EMSUS-",
            "ai_name": "JAH Surprise Emotion Archivist (Signature)",
            "local_index": SHARD_BASE + "/data/emotion-surprise-signature/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/emotion-surprise-signature/index.jsonl.gz",
            "chunk_pattern": "data/emotion-surprise-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("NOTE: manifest.json / api.json / hub files untouched - merger handles those. No commit, no push.")
    print("NEXT: merger runs restamp + commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
