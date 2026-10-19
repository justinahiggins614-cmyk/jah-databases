#!/usr/bin/env python3
"""Build the Love Emotion databases for JAH Databases (Manon's 2026-10-17
16:15 order, emotion series batch 1).

Creates two NEW databases, 34 ladder-ordered records each:

  emotion-love              - The Love Emotion Database
                              (public-harvest: real, fact-checked
                              psychology of love - Sternberg, Lee, Bowlby,
                              Fisher, Hatfield and Rapson, Ekman, Plutchik,
                              Lazarus, Gottman, Fredrickson, Fromm, Tennov,
                              Buss, Zajonc, Aron et al.)
  emotion-love-signature    - The Love Emotion Signature Database
                              (his original Signature interpretation of
                              the same ladder: love as the system's home
                              frequency; src signature, titles suffixed
                              " (Signature Edition)", clearly labeled
                              Signature-made, never presented as authentic
                              public record)

Descriptive and educational ONLY: the database describes and simulates the
emotion; it never diagnoses real people and never labels any real person
with an emotional state. Warm and wholesome throughout; nothing
hate-adjacent, profane, inappropriate, or religious.

34-record ladder per the shared emotion spec: what love is (1-4) ->
first-person simulation (5-9) -> body signals (10-13) -> facial
expression (14-17) -> triggers (18-21) -> behavior (22-25) -> healthy
expression (26-28) -> recognizing in others (29-31) -> related emotions,
mixes, full simulation (32-34). ladder_rank 1-10 non-decreasing; tiers
foundations -> compounded -> advanced.

ID prefixes: JAH-EMLO- (public) and JAH-EMLOS- (signature), verified free
in the manifest id_prefix values (2,442 databases, zero hits) and in every
shard index file of jah-databases-data-1 (zero hits) 2026-10-17.

Dedupe: all 68 titles checked against the whole system via dedupe_gate
before authoring - zero collisions, zero refusals.

Demos: 34 emotion-scenario simulator programs (scenario arc, mix blender,
recognition trainer), each machine-executed in both editions (68 runs),
real computed values, tight-bounds asserts (never float exact-equality),
OK marker required.

This builder does NOT touch data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md, and does NOT git commit or push - the
merger handles those. It writes: db/emotion-love[/-signature]/index.html
+ gen-*.js, the shard data dirs, code/emotion-love-build sources, and the
merger fragment JSON.

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
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_emotion_love import ENTRIES, SIG_TAIL
from demos_emotion_love import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation "
                "of the psychology of love: love as the system home frequency, "
                "the feeling that marks something as worth keeping, "
                "protecting, and building around. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked psychology of love: "
                "what love is, how it feels from the inside, body signals, "
                "facial expression, triggers, behavior, healthy expression, "
                "recognizing it in others, related emotions and mixes, and a "
                "full behavioral simulation - descriptive and educational "
                "only, never diagnosing real people.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what love is, first-person simulation) -> Compounded (body "
              "signals, facial expression, triggers) -> Advanced (behavior, "
              "healthy expression, recognizing it in others, related "
              "emotions and mixes, full simulation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search love definition, emotion family, intensity, myths, first-person feeling, body signals, facial expression, triggers, behavior, healthy expression, recognizing love, related emotions, mixes, simulation...",
        "chat_ph": "Ask about the emotion of love...",
        "archive_blurb": ("Seeded %s love emotion records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled love emotion studies. Seeded archive records are the authoritative entries.",
        "greet": ("I am the %s. Ask me about love - what it is, how it feels, body signals, "
                  "facial expression, triggers, behavior, healthy expression, recognizing it in "
                  "others, related emotions and mixes, and full behavioral simulation. "
                  "Descriptive and educational only: I describe and simulate the emotion and never "
                  "diagnose real people." % ai),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "love-emotion-study", "gen_demo_kind": "love-emotion-demo",
        "source": source,
    }

CIT_PUB = ("Psychology of love (standard references: Sternberg R.J. A "
           "triangular theory of love. Psychological Review. 1986;93(2):"
           "119-135; Lee J.A. The Colours of Love. Toronto: New Press; "
           "1973; Bowlby J. Attachment and Loss. New York: Basic Books; "
           "1969-1980; Fisher H.E., Aron A., Brown L.L. Romantic love: a "
           "mammalian brain system for mate choice. Philosophical "
           "Transactions of the Royal Society B. 2006;361(1476):2173-2186; "
           "Hatfield E., Rapson R.L. Love, Sex, and Intimacy. New York: "
           "HarperCollins; 1993; Ekman P. An argument for basic emotions. "
           "Cognition and Emotion. 1992;6(3-4):169-200; Plutchik R. Emotion: "
           "A Psychoevolutionary Synthesis. New York: Harper & Row; 1980; "
           "Lazarus R.S. Emotion and Adaptation. New York: Oxford University "
           "Press; 1991; Gottman J.M. The Seven Principles for Making "
           "Marriage Work. New York: Crown; 1999; Fredrickson B.L. The role "
           "of positive emotions in positive psychology. American "
           "Psychologist. 2001;56(3):218-226; Fromm E. The Art of Loving. "
           "New York: Harper & Row; 1956; Tennov D. Love and Limerence. New "
           "York: Stein and Day; 1979; Aron A., Aron E.N. Love and the "
           "Expansion of Self. New York: Hemisphere; 1986).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "interpretation of the psychology of love - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["emotion-love"] = _cfg(
    "emotion-love", "The Love Emotion Database",
    "Understand love completely: what it is, how it feels from the inside, "
    "body signals, facial expression, triggers, behavior, healthy "
    "expression, recognizing it in others, related emotions and mixes, and "
    "a full behavioral simulation. Real, fact-checked psychology, taught "
    "progressively along the ladder - descriptive and educational only.",
    "emotion record", "JAH-EMLO-", "JAH Love Emotion Archivist",
    "love emotion archivist - describing and simulating the emotion of love: "
    "what it is, how it feels, body signals, facial expression, triggers, "
    "behavior, healthy expression, recognizing it in others, related "
    "emotions and mixes, and full behavioral simulation; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; descriptive and educational only, never diagnosing real "
    "people; answers from many angles - definition, example, analogy, "
    "application, history, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["emotion-love-signature"] = _cfg(
    "emotion-love-signature", "The Love Emotion Signature Database",
    "His original Signature interpretation of the psychology of love: the "
    "same 34-record ladder - what love is, how it feels, body signals, "
    "face, triggers, behavior, healthy expression, recognizing it, related "
    "emotions and mixes, full simulation - reframed through the Signature "
    "lens as the system home frequency. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "emotion record", "JAH-EMLOS-", "JAH Love Emotion Archivist (Signature)",
    "love emotion archivist - Signature editions: his original Signature "
    "interpretation of the psychology of love, love as the system home "
    "frequency, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; descriptive and "
    "educational only, never diagnosing real people; answers from many "
    "angles using only archive data from this system",
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


def _extract_js(page):
    """Extract inline <script> (non-JSON) bodies for node --check."""
    scripts = []
    for m in re.finditer(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                         page, flags=re.S | re.I):
        body = m.group(1).strip()
        if body:
            scripts.append(body)
    return scripts


def js_hygiene(paths):
    bad = 0
    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        bodies = _extract_js(content) if path.endswith(".html") else [content]
        for i, body in enumerate(bodies):
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                tf.write(body)
                tmp = tf.name
            p = subprocess.run(["node", "--check", tmp], capture_output=True,
                               text=True, timeout=60)
            os.unlink(tmp)
            if p.returncode != 0:
                bad += 1
                print("  JS CHECK FAILED %s block %d: %s" % (path, i, p.stderr[-500:]),
                      flush=True)
    assert bad == 0, "js hygiene failed"
    print("js hygiene: node --check clean on %d files" % len(paths), flush=True)


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
    for slug in ("emotion-love", "emotion-love-signature"):
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
            assert "diagnos" not in blob or "never diagnos" in blob, \
                "diagnostic language in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-28s %d records" % (slug, n), flush=True)

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
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    js_hygiene([os.path.join(REPO, "db", s, "index.html") for s in built] +
               [os.path.join(REPO, "db", s, "gen-%s.js" % s) for s in built])

    frag = {
        "public": {
            "slug": "emotion-love",
            "name": "The Love Emotion Database",
            "tagline": DBCFG["emotion-love"]["tagline"],
            "record_kind": "emotion record",
            "id_prefix": "JAH-EMLO-",
            "ai_name": "JAH Love Emotion Archivist",
            "local_index": SHARD_BASE + "/data/emotion-love/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/emotion-love/index.jsonl.gz",
            "chunk_pattern": "data/emotion-love/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "emotion-love-signature",
            "name": "The Love Emotion Signature Database",
            "tagline": DBCFG["emotion-love-signature"]["tagline"],
            "record_kind": "emotion record",
            "id_prefix": "JAH-EMLOS-",
            "ai_name": "JAH Love Emotion Archivist (Signature)",
            "local_index": SHARD_BASE + "/data/emotion-love-signature/index.jsonl.gz",
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": SHARD_BASE + "/data/emotion-love-signature/index.jsonl.gz",
            "chunk_pattern": "data/emotion-love-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(FRAGDIR, exist_ok=True)
    frag_path = os.path.join(FRAGDIR, "emotion-love.json")
    with open(frag_path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
    print("fragment: %s" % frag_path, flush=True)
    print("DONE: %d databases, %d records. Merger owns manifest/api/restamp/commit." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
