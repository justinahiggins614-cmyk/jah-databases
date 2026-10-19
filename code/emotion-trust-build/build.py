#!/usr/bin/env python3
"""Build the Trust Emotion databases for JAH Databases
(Manon 2026-10-17 16:15 order, emotion series batch 1).

Creates two NEW databases, 34 ladder-ordered records each:

  emotion-trust              - The Trust Emotion Database
                               (public-harvest: real, fact-checked psychology
                               of trust - Erikson, Rotter, Deutsch,
                               Mayer-Davis-Schoorman, Rempel-Holmes-Zanna,
                               McAllister, Bowlby, Ekman, Plutchik, Gottman,
                               Simpson, Kramer, and the trust-game literature;
                               descriptive/educational only, never diagnosing
                               real people)
  emotion-trust-signature    - The Trust Emotion Signature Database
                               (his original Signature Trust Science: trust
                               as a sworn covenant, the kept word as the
                               stamped seal, the trust ledger; src signature,
                               titles suffixed " (Signature Edition)", never
                               presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10
non-decreasing, ladder_tier foundations/compounded/advanced); the shard
index is written in ladder order so pages present simple -> compounded ->
complex. Record spec follows the shared emotion-template.md: what trust IS
(1-4) -> first-person simulation (5-9) -> body signals (10-13) -> facial
expression (14-17) -> triggers (18-21) -> behavior (22-25) -> healthy
expression (26-28) -> recognizing it in others (29-31) -> related emotions,
mixes, and full behavioral simulation (32-34).

ID prefixes: JAH-EMTR- (public) and JAH-EMTRS- (signature), verified free
in the manifest id_prefix values, in every shard index file, and unique
across the 28-emotion roster (planner brief:
~/workspace/hidden_files/new-orders-1540/emotion-roster.json).

Demos: 34 emotion-scenario simulators (demos_emotion_trust.py), each a
situation + intensity curve simulated scene by scene with computed body
signals, facial-expression metrics, and a record-specific computed block.
All 68 executions (34 x 2 editions) are machine-run by this build: each
prints real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
It writes only: db/emotion-trust[/-signature]/, code/emotion-trust-build/,
the shard data dirs, and the merger fragment. A merger handles the rest.

Never the words "bat belt" anywhere. No website references. No Facebook.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/emotion-trust.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_emotion_trust import ENTRIES, SIG_TAIL
from demos_emotion_trust import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Trust Science: "
                "trust as a sworn covenant between people, the kept word as "
                "the stamped seal, every promise an entry in the trust "
                "ledger. Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked psychology of trust: "
                "what trust is, how it feels from the inside, its body "
                "signals and facial expression, its triggers, how it shows "
                "in behavior, how to express it healthily, how to recognize "
                "it in others, its blends with other emotions, and full "
                "behavioral simulation - organized in the Signature system. "
                "Descriptive and educational only; never diagnosing real "
                "people.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what trust is - definition, emotion family, intensity "
              "volumes, myths; how trust feels - first-person passage, arc "
              "over time, low vs high intensity, the affection blend, a day "
              "in the life) -> Compounded (body signals - heart breath muscle "
              "energy, posture, sleep appetite energy, individual "
              "differences; facial expression - the face of trust, intensity "
              "scaling, hidden and faked expressions, artist and actor "
              "notes; triggers - classic, personal, surprise, chain "
              "reactions; behavior - actions, speech, decisions, full "
              "intensity) -> Advanced (healthy expression - expressing well, "
              "the two unhealthy extremes, everyday practices; recognizing "
              "trust - reading signs, supportive responses, mistakes to "
              "avoid; mixes and simulation - related emotions, four blends, "
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
        "search_ph": "Search trust definition, first-person trust, trust arc, body signals of trust, face of trust, trust triggers, trusting behavior, healthy trust, recognizing trust, trust and affection, trust mixes, trust simulation...",
        "chat_ph": "Ask about trust...",
        "archive_blurb": ("Seeded %s trust emotion records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "What trust is \u00b7 How trust feels \u00b7 Body signals \u00b7 Facial expression \u00b7 Triggers \u00b7 Trust in behavior \u00b7 Healthy expression \u00b7 Recognizing trust \u00b7 Mixes and simulation - each opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled trust emotion studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about trust - what it is, how it feels from the inside, its arc over time, its body signals and facial expression, its triggers, how it shows in behavior, how to express it healthily, how to recognize it in others, its blends with other emotions, and full behavioral simulation." % ai,
        "gen_fields": ["what trust is", "how trust feels", "body signals",
                       "facial expression", "triggers", "trust in behavior",
                       "healthy expression", "recognizing trust",
                       "mixes and simulation"],
        "gen_kind": "trust-emotion-study", "gen_demo_kind": "trust-emotion-demo",
        "source": source,
    }

CIT_PUB = ("Psychology of trust (standard references: Erikson EH. Childhood "
           "and Society. Norton; 1950; Rotter JB. J Pers. 1967;35:651-665; "
           "Deutsch M. J Confl Resolut. 1958;2:265-279; Mayer RC, Davis JH, "
           "Schoorman FD. Acad Manage Rev. 1995;20:709-734; Rempel JK, Holmes "
           "JG, Zanna MP. J Pers Soc Psychol. 1985;49:95-112; McAllister DJ. "
           "Acad Manage J. 1995;38:24-59; Rousseau DM et al. Acad Manage Rev. "
           "1998;23:393-404; Bowlby J. Attachment and Loss. Basic Books; "
           "1969; Ekman P. Emotions Revealed. Times Books; 2003; Plutchik R. "
           "The Emotions. Univ Press of America; 1991; Gottman JM. The "
           "Science of Trust. Norton; 2011; Simpson JA. Curr Dir Psychol "
           "Sci. 2007;16:264-268; Kramer RM. Annu Rev Psychol. 1999;50:569-"
           "598; Meyerson D, Weick KE, Kramer RM. In: Trust in Organizations. "
           "Sage; 1996; Berg J, Dickhaut J, McCabe K. Games Econ Behav. "
           "1995;10:122-142; Kosfeld M et al. Nature. 2005;435:673-676; "
           "Luhmann N. Trust and Power. Wiley; 1979). Descriptive and "
           "educational only.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Trust "
                     "Science - trust as a sworn covenant, the kept word as "
                     "the stamped seal - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["emotion-trust"] = _cfg(
    "emotion-trust", "The Trust Emotion Database",
    "What trust IS, from cautious openness to deep reliance: describe it, "
    "feel it from the inside, read it in the body and the face, learn its "
    "triggers, watch it in behavior, express it healthily, recognize it in "
    "others, blend it with other emotions, and simulate it scene by scene - "
    "34 ladder-ordered records, descriptive and educational.",
    "emotion record", "JAH-EMTR-", "JAH Trust Emotion Archivist",
    "trust emotion archivist - describing and simulating the emotion of trust "
    "from plain definition through first-person feeling, body signals, "
    "facial expression, triggers, behavior, healthy expression, recognition "
    "in others, and emotion blends to full behavioral simulation; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["emotion-trust-signature"] = _cfg(
    "emotion-trust-signature", "The Trust Emotion Signature Database",
    "His original Signature Trust Science: trust as a sworn covenant between "
    "people, the kept word as the stamped seal, every promise an entry in "
    "the trust ledger. The full ladder from what trust is through how it "
    "feels, body and face, triggers, behavior, healthy expression, and "
    "recognition, to blends and full simulation, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "emotion record", "JAH-EMTRS-", "JAH Trust Emotion Archivist (Signature)",
    "trust emotion archivist - Signature editions: his original Signature "
    "Trust Science, trust as a sworn covenant and the kept word as the "
    "stamped seal, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, how-to - using only "
    "archive data from this system",
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


def write_fragment(built):
    frag = {}
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        pub = not slug.endswith("-signature")
        frag["public" if pub else "signature"] = {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(recs), "status": "live",
            "full_records": len(recs),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": cfg["source"] if pub else "signature",
        }
    # public-harvest source label per canon
    frag["public"]["source"] = "public-harvest"
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)


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
    for slug in ("emotion-trust", "emotion-trust-signature"):
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

    # JS hygiene: node --check on extracted page scripts (excluding ld+json)
    # and on gen-*.js files.
    import re as _re, tempfile
    for slug in built:
        ppath = os.path.join(REPO, "db", slug, "index.html")
        html = open(ppath, encoding="utf-8").read()
        blocks = _re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                             html, flags=_re.S)
        assert blocks, "no scripts found in %s" % slug
        for bi, blk in enumerate(blocks):
            if not blk.strip():
                continue
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                tf.write(blk)
                tfp = tf.name
            p = subprocess.run(["node", "--check", tfp], capture_output=True, text=True)
            assert p.returncode == 0, "node --check failed page %s block %d: %s" % (slug, bi, p.stderr[-500:])
            os.unlink(tfp)
        gp = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
        p = subprocess.run(["node", "--check", gp], capture_output=True, text=True)
        assert p.returncode == 0, "node --check failed %s: %s" % (gp, p.stderr[-500:])
    print("js hygiene: node --check clean on page scripts and gen-*.js", flush=True)

    # cross-check: demo outputs reference entry content (scenario keywords
    # drawn from each record's key points / group vocabulary)
    for slug, recs in built.items():
        for r in recs:
            out = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                                 capture_output=True, text=True, timeout=60).stdout.lower()
            assert "scenario" in out and "intensity" in out, "demo output thin in %s" % r["id"]
    print("cross-check: demo outputs carry scenario + intensity for all %d records" % total, flush=True)

    write_fragment(built)
    print("DONE: 2 databases, %d records. Manifest/api/index.html/README untouched for the merger." % total)
    print("Do NOT claim live - the merger verifies.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
