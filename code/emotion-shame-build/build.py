#!/usr/bin/env python3
"""Build the Shame Emotion databases for JAH Databases
(Manon's 2026-10-17 16:15 order, emotion series batch 1).

Descriptive and educational ONLY - describes and simulates shame; never
diagnoses real people, never labels any real person, never offers
therapeutic advice beyond general safe everyday guidance.

So this build creates two NEW databases, 34 ladder-ordered records each:

  emotion-shame                - The Shame Emotion Database
                                 (public-harvest: real, fact-checked
                                 psychology of shame - Darwin, Ekman,
                                 Tangney, Lewis, Izard, Lazarus, Gross,
                                 Scherer, Scheff, Nathanson, APA Dictionary;
                                 src public-harvest)
  emotion-shame-signature      - The Shame Emotion Signature Database
                                 (his original Signature lens: shame as
                                 the mirror of the true self, the honor
                                 and mastery; src signature, titles
                                 suffixed " (Signature Edition)", clearly
                                 labeled Signature-made, never presented
                                 as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-34,
non-decreasing; tiers foundations/compounded/advanced); the shard index is
written in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-EMSH- (public) and JAH-EMSHS- (signature), verified free
in the manifest id_prefix values (2,442 databases, zero hits) and in all
jah-databases-data-1 shard index files (zero 'JAH-EMSH' substring hits),
2026-10-17.

Every demo is an emotion-scenario simulator: real, runnable, stdlib-only
Python performing the actual scenario computation for its record. All are
machine-executed by this build before writing: each prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker (see demos_emotion_shame.py).

CONCURRENCY: this builder NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md and NEVER runs git commit or
git push. A merger handles those. It writes ONLY: db/emotion-shame/ +
db/emotion-shame-signature/ (index.html + gen-*.js), the shard dirs under
~/workspace/jah-databases-data-1/data/, and the fragment JSON for the
merger at ~/workspace/hidden_files/missing-builds/fragments/.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
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
FRAGMENTS = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_emotion_shame import ENTRIES, SIG_TAIL
from demos_emotion_shame import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature lens: shame "
                "as the soul's pressure forge, the honest alarm of a "
                "violated boundary; every facet framed as signal, fuel, "
                "and mastery - never as a diagnosis, never labeling any "
                "real person. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked psychology of shame: "
                "what shame is, how it feels from the inside, body "
                "signals, facial expression, triggers, behavior, healthy "
                "expression, recognizing it in others, related emotions "
                "and mixes, and full behavioral simulation - descriptive "
                "and educational only, never diagnosing any real person.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what shame is, the emotion family, the three volumes, "
              "myths, first-person simulation, the time course, low "
              "versus high intensity, the frustration blend, a day with "
              "shame) -> Compounded (body signals, posture and movement, "
              "sleep appetite and energy, how bodies differ, the face of "
              "shame, the face across intensities, hiding and faking, "
              "expression gallery notes, the classic triggers) -> "
              "Advanced (personal triggers, surprise triggers, chain "
              "reactions, angry actions, angry speech, shame and "
              "judgment, escalation, healthy expression, unhealthy "
              "expression, everyday practices, reading others, supportive "
              "responses, mistakes to avoid, the shame neighborhood, "
              "shame blends, full behavioral simulation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search shame definition, intensity, body signals, facial expression, triggers, behavior, healthy expression, reading shame, blends, simulation...",
        "chat_ph": "Ask about shame...",
        "archive_blurb": ("Seeded %s shame emotion records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced. "
                          "Descriptive and educational only - never diagnosing any real person."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled shame emotion studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about shame - what it is, how it feels, body signals, facial expression, triggers, behavior, healthy expression, reading it in others, related emotions and blends, and full behavioral simulation. I describe and simulate only; I never diagnose any real person." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "shame-emotion-study", "gen_demo_kind": "shame-emotion-demo",
        "source": source,
    }

DBCFG = {}
DBCFG["emotion-shame"] = _cfg(
    "emotion-shame", "The Shame Emotion Database",
    "Describe and simulate shame: what it is, how it feels from the inside, "
    "body signals, facial expression, triggers, behavior, healthy "
    "expression, recognizing it in others, related emotions and mixes, and "
    "full behavioral simulation - real, fact-checked psychology, taught "
    "progressively along the ladder. Descriptive and educational only.",
    "emotion record", "JAH-EMSH-", "JAH Shame Emotion Archivist",
    "shame emotion archivist - describing and simulating shame across what "
    "it is, how it feels, body signals, facial expression, triggers, "
    "behavior, healthy expression, recognizing it in others, related "
    "emotions and blends, and full behavioral simulation; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; descriptive and educational only, never diagnosing any real "
    "person; answers from many angles - definition, example, analogy, "
    "application, history, how-to - using only archive data from this system",
    "public")
DBCFG["emotion-shame-signature"] = _cfg(
    "emotion-shame-signature", "The Shame Emotion Signature Database",
    "His original Signature lens on shame: the soul's pressure forge, the "
    "honest alarm of a violated boundary - every facet framed as signal, "
    "fuel, and mastery, from what shame is through the full behavioral "
    "simulation. Clearly labeled Signature-made, never presented as "
    "authentic public record, never diagnosing any real person.",
    "emotion record", "JAH-EMSHS-", "JAH Shame Emotion Archivist (Signature)",
    "shame emotion archivist - Signature editions: his original Signature "
    "lens, shame as the pressure forge of the soul - signal, fuel, and mastery - "
    "clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations "
    "through compounded to advanced; descriptive and educational only, "
    "never diagnosing any real person; answers from many angles - "
    "definition, example, analogy, application, history, how-to - using "
    "only archive data from this system",
    "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def preflight_dedupe():
    """Whole-system title check BEFORE authoring records: all 68 titles."""
    refused = []
    for slug in ("emotion-shame", "emotion-shame-signature"):
        sig = slug.endswith("-signature")
        for e in ENTRIES:
            title = e["name"] + " (Signature Edition)" if sig else e["name"]
            hits = [h for h in base.GATE.check(slug, title) if h[0] != slug]
            if hits:
                refused.append((title, hits))
    if refused:
        for title, hits in refused:
            print("REFUSED: %r already in %s" % (title, hits), flush=True)
        raise SystemExit("dedupe preflight refused %d titles" % len(refused))
    print("dedupe preflight: 68 titles checked vs whole system, zero collisions", flush=True)


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
                       "note": "Working demonstration program (real, runnable Python) - emotion-scenario simulator."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    pub = {
        "slug": "emotion-shame",
        "name": "The Shame Emotion Database",
        "tagline": DBCFG["emotion-shame"]["tagline"],
        "record_kind": "emotion record",
        "id_prefix": "JAH-EMSH-",
        "ai_name": "JAH Shame Emotion Archivist",
        "local_index": SHARD_BASE + "/data/emotion-shame/index.jsonl.gz",
        "record_count": len(built["emotion-shame"]),
        "status": "live",
        "full_records": len(built["emotion-shame"]),
        "index": SHARD_BASE + "/data/emotion-shame/index.jsonl.gz",
        "chunk_pattern": "data/emotion-shame/chunks/chunk-NNNN.jsonl.gz",
        "source": "public-harvest",
    }
    sig = {
        "slug": "emotion-shame-signature",
        "name": "The Shame Emotion Signature Database",
        "tagline": DBCFG["emotion-shame-signature"]["tagline"],
        "record_kind": "emotion record",
        "id_prefix": "JAH-EMSHS-",
        "ai_name": "JAH Shame Emotion Archivist (Signature)",
        "local_index": SHARD_BASE + "/data/emotion-shame-signature/index.jsonl.gz",
        "record_count": len(built["emotion-shame-signature"]),
        "status": "live",
        "full_records": len(built["emotion-shame-signature"]),
        "index": SHARD_BASE + "/data/emotion-shame-signature/index.jsonl.gz",
        "chunk_pattern": "data/emotion-shame-signature/chunks/chunk-NNNN.jsonl.gz",
        "source": "signature",
    }
    os.makedirs(FRAGMENTS, exist_ok=True)
    fpath = os.path.join(FRAGMENTS, "emotion-shame.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump({"public": pub, "signature": sig}, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath, flush=True)
    return fpath


def node_check_js(path):
    """node --check every <script> block except ld+json (JSON, not JS)."""
    with open(path, encoding="utf-8") as f:
        html = f.read()
    blocks = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                        html, flags=re.S)
    assert blocks, "no script blocks found in %s" % path
    import tempfile
    for i, b in enumerate(blocks):
        if not b.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
            tf.write(b)
            tpath = tf.name
        p = subprocess.run(["node", "--check", tpath],
                           capture_output=True, text=True, timeout=60)
        os.unlink(tpath)
        assert p.returncode == 0, "node --check failed block %d in %s: %s" % (i, path, p.stderr[:500])
    # gen js files
    ddir = os.path.dirname(path)
    for fn in sorted(os.listdir(ddir)):
        if fn.startswith("gen-") and fn.endswith(".js"):
            gp = os.path.join(ddir, fn)
            p = subprocess.run(["node", "--check", gp], capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "node --check failed %s: %s" % (gp, p.stderr[:500])
    print("node --check clean: %s (+gen js)" % path, flush=True)


def main():
    if not os.path.exists("/home/hatch/workspace/hidden_files/db-writer-free.marker"):
        raise SystemExit("db-writer-free.marker absent - STOPPING")
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

    preflight_dedupe()

    built = {}
    for slug in ("emotion-shame", "emotion-shame-signature"):
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
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
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
        print("shard: %-32s %d records" % (slug, n), flush=True)

    # machine-execute all 68 demos
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    # cross-check: demo OK-line names match entry titles
    for slug, recs in built.items():
        sig = slug.endswith("-signature")
        for r in recs:
            p = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                               capture_output=True, text=True, timeout=60)
            ok_line = [l for l in p.stdout.splitlines() if l.startswith("OK:")][0]
            assert r["title"] in ok_line or r["name"] in ok_line, \
                "demo/title mismatch in %s" % r["id"]
    print("cross-check: all demo OK lines match entry titles", flush=True)

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
        # apostrophe-free JS strings: role/ai_name/greet/search
        for key in ("role", "ai", "greet", "search_ph"):
            assert "'" not in DBCFG[slug][key], "apostrophe in %s.%s" % (slug, key)
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
        assert "shame" in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        node_check_js(ppath)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    fpath = write_fragment(built)
    print("DONE: %d databases, %d records. manifest/api/index.html untouched; no git run." % (len(built), total))
    print("fragment: %s" % fpath)
    print("NEXT (merger): merge fragment, run code/restamp_counts.py, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
