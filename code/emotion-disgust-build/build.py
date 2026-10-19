#!/usr/bin/env python3
"""Build the Disgust Emotion databases for JAH Databases
(Manon's 2026-10-17 16:15 emotion-series order, batch 1).

Verified 2026-10-17: RAW pre-check over the full manifest (2,442
databases) plus every shard index file in jah-databases-data-1: prefixes
JAH-EMDI- (public) and JAH-EMDIS- (signature) return zero exact hits; the
68 planned titles (34 + 34 Signature Edition) pass the whole-system dedupe
gate with zero collisions. No other emotion-* slugs exist in the manifest,
so this is the first database in the emotion series.

So this build creates two NEW databases, 34 ladder-ordered records each:

  emotion-disgust            - The Disgust Emotion Database
                               (public-harvest: real, fact-checked emotion
                               psychology - what disgust is, where it sits
                               in the emotion family, first-person
                               simulation, body signals, facial expression,
                               triggers, behavior, healthy expression,
                               recognizing it in others, related emotions
                               and mixes, full behavioral simulation;
                               standard references Darwin 1872; Rozin and
                               Fallon 1987; Rozin, Haidt and McCauley 1999;
                               Ekman 1999; Haidt, McCauley and Rozin 1994;
                               Miller 1997; Chapman et al. 2009; Tybur et
                               al. 2013)
  emotion-disgust-signature  - The Disgust Emotion Signature Database
                               (his original Signature Emotion Method: the
                               Signature system reads disgust as the first
                               and most honest boundary signal - the body's
                               original NO, the purity compass, the guardian
                               of the gates; src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex.

Descriptive and educational ONLY - never diagnoses real people, never
labels any real person with an emotional state, never offers therapeutic
advice beyond general, safe, everyday guidance.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
It writes only db/emotion-disgust[-signature]/, the shard data dirs, and
the merger fragment at
~/workspace/hidden_files/missing-builds/fragments/emotion-disgust.json.

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/emotion-disgust.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_emotion_disgust import ENTRIES, SIG_TAIL
from demos_emotion_disgust import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Emotion "
                "Method: the Signature system reads disgust as the first "
                "and most honest boundary signal, the body original NO, the "
                "purity compass, the guardian of the gates. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked emotion psychology: "
                "what disgust is, where it sits in the emotion family, "
                "first-person simulation, body signals, facial expression, "
                "triggers, behavior, healthy expression, recognizing it in "
                "others, related emotions and mixes, and full behavioral "
                "simulation - descriptive and educational only, never "
                "diagnosing any real person.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what disgust is, the emotion family, intensity, myths, "
              "first-person simulation, the arc, low vs high intensity, "
              "disgust mixed with anger, a day in the life) -> Compounded "
              "(body signals, posture, sleep appetite and energy, bodily "
              "differences, the face, expression intensity, hiding and "
              "faking, drawing guide, classic triggers, personal triggers, "
              "surprise triggers, chain reactions, behavior, speech, "
              "decisions, escalation) -> Advanced (healthy expression, "
              "unhealthy expression, everyday practices, reading others, "
              "supportive responses, what not to do, neighbors, mixes, "
              "full behavioral simulation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search disgust definition, emotion family, intensity, body signals, facial expression, triggers, behavior, healthy expression, reading others, mixes, simulation...",
        "chat_ph": "Ask about disgust...",
        "archive_blurb": ("Seeded %s disgust emotion records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Description \u00b7 Inner Experience \u00b7 Body Signals \u00b7 Facial Expression \u00b7 Triggers \u00b7 Behavior \u00b7 Healthy Expression \u00b7 Recognizing It in Others \u00b7 Related Emotions and Simulation - each field opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled disgust emotion studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about disgust - what it is, the emotion family, intensity, first-person experience, body signals, the face, triggers, behavior, healthy expression, reading it in others, related emotions and mixes, and full behavioral simulation." % ai,
        "gen_fields": ["Description", "Inner Experience", "Body Signals",
                       "Facial Expression", "Triggers", "Behavior",
                       "Healthy Expression", "Recognizing It in Others",
                       "Related Emotions and Simulation"],
        "gen_kind": "emotion-record", "gen_demo_kind": "emotion-demo",
        "source": source,
    }

CIT_PUB = ("Disgust emotion psychology (standard references: Darwin C. The "
           "Expression of the Emotions in Man and Animals. John Murray; "
           "1872; Rozin P, Fallon AE. A perspective on disgust. "
           "Psychological Review. 1987;94(1):23-41; Rozin P, Haidt J, "
           "McCauley CR. Disgust. In: Lewis M, Haviland-Jones JM, eds. "
           "Handbook of Emotions. 2nd ed. Guilford Press; 2000:637-653; "
           "Ekman P. Basic emotions. In: Dalgleish T, Power M, eds. "
           "Handbook of Cognition and Emotion. Wiley; 1999:45-60; Haidt J, "
           "McCauley CR, Rozin P. Individual differences in sensitivity to "
           "disgust. Personality and Individual Differences. "
           "1994;16(5):701-713; Miller WI. The Anatomy of Disgust. Harvard "
           "University Press; 1997; Chapman HA et al. In bad taste: "
           "Evidence for the oral origins of moral disgust. Science. "
           "2009;323(5918):1222-1226; Tybur JM et al. Disgust: Evolved "
           "function and structure. Psychological Review. "
           "2013;120(1):65-84). Descriptive and educational only.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Emotion "
                     "Method - the Signature system reads disgust as the "
                     "first and most honest boundary signal, the body "
                     "original NO, the purity compass, the guardian of the "
                     "gates - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["emotion-disgust"] = _cfg(
    "emotion-disgust", "The Disgust Emotion Database",
    "Understand disgust completely: what it is, how it feels from the "
    "inside, what it does to the body and face, what triggers it, how it "
    "shows in behavior, how to express it well, how to recognize it in "
    "others, and how it blends with other emotions - real, fact-checked "
    "emotion psychology, taught progressively along the ladder, "
    "descriptive and educational only.",
    "emotion record", "JAH-EMDI-", "JAH Disgust Emotion Archivist",
    "disgust emotion archivist - describing and simulating the disgust "
    "emotion across description, inner experience, body signals, facial "
    "expression, triggers, behavior, healthy expression, recognizing it in "
    "others, and related emotions and mixes; teaching progressively along "
    "the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, history, "
    "how-to - using only archive data from this system; descriptive and "
    "educational only, never diagnosing any real person",
    CIT_PUB, "public")
DBCFG["emotion-disgust-signature"] = _cfg(
    "emotion-disgust-signature", "The Disgust Emotion Signature Database",
    "His original Signature Emotion Method applied to disgust: the "
    "Signature system reads disgust as the first and most honest boundary "
    "signal - the body original NO, the purity compass, the guardian of "
    "the gates. The full ladder from what disgust is through inner "
    "experience, body, face, triggers, and behavior, to healthy "
    "expression, reading others, and full behavioral simulation, reframed "
    "as Signature science. Clearly labeled Signature-made, never presented "
    "as authentic public record.",
    "emotion record", "JAH-EMDIS-", "JAH Disgust Emotion Archivist (Signature)",
    "disgust emotion archivist - Signature editions: his original Signature "
    "Emotion Method reading disgust as the first and most honest boundary "
    "signal, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "using only archive data from this system; descriptive and educational "
    "only, never diagnosing any real person",
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


def js_hygiene(page_paths, gen_paths):
    """node --check every inline page script (excluding ld+json) and gen js."""
    checked = 0
    for pp in page_paths:
        html = open(pp, encoding="utf-8").read()
        for i, m in enumerate(re.finditer(
                r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                html, flags=re.S)):
            body = m.group(1).strip()
            if not body:
                continue
            with tempfile.NamedTemporaryFile("w", suffix=".js",
                                             delete=False) as tf:
                tf.write(body)
                tp = tf.name
            p = subprocess.run(["node", "--check", tp],
                               capture_output=True, text=True)
            os.unlink(tp)
            assert p.returncode == 0, \
                "node --check failed %s block %d: %s" % (pp, i, p.stderr[-600:])
            checked += 1
    for gp in gen_paths:
        p = subprocess.run(["node", "--check", gp],
                           capture_output=True, text=True)
        assert p.returncode == 0, \
            "node --check failed %s: %s" % (gp, p.stderr[-600:])
        checked += 1
    print("js hygiene: %d script blocks node --check clean" % checked,
          flush=True)


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
    for slug in ("emotion-disgust", "emotion-disgust-signature"):
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
        # apostrophe-free cfg strings (JS hygiene)
        for k in ("ai", "role", "greet", "search_ph"):
            assert "'" not in cfg[k], "apostrophe in cfg %s for %s" % (k, slug)
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
    page_paths, gen_paths = [], []
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
        page_paths.append(ppath)
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
        gen_paths.append(gpath)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    js_hygiene(page_paths, gen_paths)

    # merger fragment (the merger handles manifest/api.json/index.html/README)
    frag = {
        "public": base.manifest_entry("emotion-disgust", len(built["emotion-disgust"])),
        "signature": base.manifest_entry("emotion-disgust-signature",
                                         len(built["emotion-disgust-signature"])),
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("DONE: 68 records, 68 demos OK, pages + shards + fragment written. "
          "Manifest/api/index/README left untouched for the merger. No commit, no push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
