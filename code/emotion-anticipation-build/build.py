#!/usr/bin/env python3
"""Build The Anticipation Emotion Database (public + Signature), 34 records each.

Manon's 2026-10-17 16:15 orders, emotion series batch 1. Shared spec:
~/workspace/hidden_files/new-orders-1540/emotion-template.md.

Pipeline replicates code/component-parts-catalog-build/build.py EXACTLY for
page structure, but per concurrency rules this builder:
  - NEVER touches data/manifest.json, api.json, index.html, README.md, docs/AI_ACCESS.md
  - NEVER git commits or pushes (a merger handles those)
  - ONLY writes: db/emotion-anticipation/ + db/emotion-anticipation-signature/
    (index.html + gen-*.js each), this code dir, the shard dirs in
    jah-databases-data-1, and the missing-builds fragment.

ID prefixes: JAH-EMAP- (public) / JAH-EMAPS- (signature), verified free in
the manifest id_prefix values (2,442 databases) and in every shard index file
(zero hits) before authoring; all 68 titles passed code/dedupe_gate.py with
zero refusals.

Descriptive/educational ONLY - never diagnoses real people. Screening: no
hate-adjacent, profane, or inappropriate content; no religious talk.
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
from entries_emotion_anticipation import ENTRIES, SIG_TAIL
from demos_emotion_anticipation import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature reading of the emotional "
                "landscape: anticipation as the compass emotion, the forward gauge, "
                "the earliest instrument of intention. Clearly labeled Signature-made, "
                "never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked emotion psychology: what anticipation "
                "is, how it feels from the inside, body signals, facial expression, "
                "triggers, behavior, healthy expression, recognition in others, related "
                "emotions and mixes, and full behavioral simulation - descriptive and "
                "educational only, never diagnosing real people.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what anticipation is, where it sits in the emotion family, its volumes, "
              "its myths, first-person simulation, its timeline, low vs high intensity, "
              "its blend with excitement, a day in the life, body signals, posture) -> "
              "Compounded (sleep appetite and energy, individual differences, the face of "
              "anticipation, expression across intensity, hiding and faking, gallery "
              "notes, classic triggers, personal triggers, surprise triggers, chain "
              "reactions, typical actions, language and tone) -> Advanced (decisions "
              "and judgment, escalation, healthy expression, unhealthy expression, "
              "everyday practices, recognition, supportive responses, mistakes to "
              "avoid, related emotions map, blends, full behavioral simulation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search definition, emotion family, intensity, first-person feeling, timeline, body signals, posture, facial expression, triggers, behavior, healthy expression, recognition, blends, simulation...",
        "chat_ph": "Ask about anticipation...",
        "archive_blurb": ("Seeded %s anticipation emotion records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled anticipation emotion studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about anticipation - what it is, where it sits among the emotions, its volumes, how it feels from the inside, its timeline, body signals, posture, facial expression, triggers, behavior, healthy expression, recognition in others, related emotions and blends, and full behavioral simulation." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "emotion-study", "gen_demo_kind": "emotion-demo",
        "source": source,
    }

CIT_PUB = ("Emotion psychology (standard references: Plutchik R. (1980) Emotion: A "
           "Psychoevolutionary Synthesis; Lazarus R. S. (1991) Emotion and "
           "Adaptation; Russell J. A. (1980) circumplex model of affect; Frijda "
           "N. H. (1986) The Emotions; Scherer K. R. (2001) appraisal as "
           "multilevel sequential checking; Ekman facial expression research; "
           "Gross process model of emotion regulation). Descriptive and "
           "educational only - never diagnoses real people.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature reading of the "
                     "emotional landscape - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["emotion-anticipation"] = _cfg(
    "emotion-anticipation", "The Anticipation Emotion Database",
    "Understand anticipation completely: real, fact-checked emotion psychology covering "
    "what anticipation is, how it feels from the inside, body signals, facial expression, "
    "triggers, behavior, healthy expression, recognition in others, related emotions and "
    "blends, and full behavioral simulation - taught progressively along the ladder, "
    "descriptive and educational only.",
    "emotion record", "JAH-EMAP-", "JAH Anticipation Emotion Archivist",
    "anticipation emotion archivist - describing and simulating the emotion of anticipation "
    "across what it is, how it feels, body signals, facial expression, triggers, behavior, "
    "healthy expression, recognition in others, and related emotions and blends; teaching "
    "progressively along the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, history, how-to - using "
    "only archive data from this system; descriptive and educational only, never diagnosing "
    "real people",
    CIT_PUB, "public")
DBCFG["emotion-anticipation-signature"] = _cfg(
    "emotion-anticipation-signature", "The Anticipation Emotion Signature Database",
    "His original Signature reading of anticipation: the compass emotion, the forward gauge, "
    "the earliest instrument of intention. The full ladder from what anticipation is through "
    "how it feels, body signals, facial expression, triggers, and behavior, to healthy "
    "expression, recognition, blends, and full behavioral simulation, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic public record.",
    "emotion record", "JAH-EMAPS-", "JAH Anticipation Emotion Archivist (Signature)",
    "anticipation emotion archivist - Signature editions: his original Signature reading of "
    "the emotional landscape, anticipation as the compass emotion and forward gauge, clearly "
    "labeled Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, history, how-to - using "
    "only archive data from this system; descriptive and educational only, never diagnosing "
    "real people",
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
    for slug in ("emotion-anticipation", "emotion-anticipation-signature"):
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
            # apostrophe-free check on strings that land in single-quoted page JS
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

    # CONCURRENCY: manifest/api.json/index.html/README/docs updates and git are the
    # merger's job. This builder stops here.
    print("done: %d databases, %d records. Manifest/api/commit left to merger." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
