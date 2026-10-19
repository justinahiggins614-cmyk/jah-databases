#!/usr/bin/env python3
"""Build The Unsolved Nursing Database (unsolved-nursing) and its Signature half (unsolved-nursing-signature).

Unsolved Problems Solved series, batch 3 (2026-10-17 orders).

34 famous unsolved nursing problems, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems (JAH-USNU-).
Signature half: the SAME 34 problems through the Signature lens
(JAH-USNUS-), titles suffixed " (Signature Edition)", src signature,
clearly labeled Signature-made.

ID prefixes verified free: zero hits in manifest id_prefix values AND in
all shard index files (jah-databases-data-1), exact + substring.

Honesty rule (round8 repair pattern): every record's how_it_works OPENS with
the exact label "Signature-generated proposed solution \u2014 not established
science." (em-dash U+2014). Assembly order:
  signature half = LABEL + " " + sig_lens + " " + why + " " + solution_body
  public half    = LABEL + " " + why + " " + pointer
Gate asserts startswith on BOTH halves (68/68) and zero hyphenated-label
leftovers. Never claims proof, never implies peer acceptance, never presents
speculation as settled; medical/adjacent proposals are labeled speculation,
never advice, no dosages, no cure claims.

Demos: data-driven solution-explorer walkthroughs with real computed ratios,
tight-bounds asserts, confirm/refute panels, machine-executed.

CONCURRENCY: this script never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md; never commits or pushes.
A merger handles registration. It only writes:
  db/unsolved-nursing/ + db/unsolved-nursing-signature/ (index.html, gen-*.js)
  shard data dirs under ~/workspace/jah-databases-data-1/data/
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
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_nursing import ENTRIES, LABEL, SIG_TAIL
from demos_unsolved_nursing import build_demos

DEMOS = build_demos(ENTRIES)

HYPHEN_LABEL = "Signature-generated proposed solution - not established science."

# entries must never carry the hyphenated (wrong-dash) label anywhere
for _e in ENTRIES:
    _blob = json.dumps(_e, ensure_ascii=False)
    assert HYPHEN_LABEL not in _blob, "hyphen label in entry " + _e.get("key", "?")
    assert _blob.count(LABEL) <= 1, "label duplicated in entry " + _e.get("key", "?")

# demo_data sanity: ratio must sit strictly inside bounds, b nonzero
for _e in ENTRIES:
    _dd = _e.get("demo_data") or {}
    _av = _dd["a"][1]; _bv = _dd["b"][1]; _lo, _hi = _dd["bounds"]
    assert _bv != 0, "demo b=0 in " + _e["key"]
    _r = _av / _bv
    assert _lo < _r < _hi, "demo ratio out of bounds in %s: %r not in (%r,%r)" % (_e["key"], _r, _lo, _hi)

# ---------------------------------------------------------------- DB config

def _tier_listing():
    tiers = [("foundations", "Foundations"), ("compounded", "Compounded"), ("advanced", "Advanced")]
    parts = []
    for tkey, tname in tiers:
        names = [e["name"] for e in sorted(ENTRIES, key=lambda x: x["ladder_rank"]) if e["ladder_tier"] == tkey]
        parts.append("%s (%s)" % (tname, ", ".join(names)))
    return " -> ".join(parts)


def _cfg(name, tagline, record_kind, prefix, ai, role, source, greet):
    pub = source == "public"
    hero_line = ("Public records - thirty-four of nursing's greatest unsolved "
                 "problems, each fact-checked: the problem as the world knows "
                 "it, its history, why it matters, and a pointer to the "
                 "Signature system's labeled proposed solution. Organized in "
                 "the Signature system.")
    sig_line = ("Signature originals - the same thirty-four unsolved problems "
                "through the Signature lens: each record carries the full "
                "Signature-generated proposed solution approach - assumptions, "
                "reasoning path, proposed mechanism, what would confirm or "
                "kill it, and what it does not claim. Clearly labeled "
                "Signature-made proposals, never established science, never "
                "presented as authentic public record.")
    ladder = " Records are ordered by the teaching ladder: %s." % _tier_listing()
    ai_bit = ai.replace(" (Signature)", "")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: problem, "
                  "background, why it matters, the Signature-generated "
                  "proposed solution (labeled as a proposal, never established "
                  "science), how nursing researchers study it, key points, requirements, "
                  "standards, citations, and a working solution-explorer "
                  "demonstration program.%s" % (tagline, sig_line if not pub else hero_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if not pub else
                     "Public records organized in the Signature system"),
        "search_ph": "Search failure to rescue, alarm fatigue, pressure injury, nurse burnout, staffing ratios, handoffs...",
        "chat_ph": "Ask about unsolved nursing...",
        "archive_blurb": ("Seeded %s unsolved-nursing records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if not pub else "public-record")),
        "schema": ("id, t, g, name, title, problem, background, why_it_matters, "
                   "signature_solution, description, how_it_works, key_points, "
                   "requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved-nursing studies. Seeded archive records are the authoritative entries.",
        "greet": greet,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-nursing-study", "gen_demo_kind": "unsolved-nursing-solution-explorer",
        "source": source,
    }

CIT_PUB = "Unsolved problems in nursing science (standard references: Agency for Healthcare Research and Quality; American Nurses Association; Cochrane systematic reviews; landmark studies cited per record)."
CIT_SIG = CIT_PUB + (" Signature editions carry the Signature system's "
                     "proposed solution approaches - labeled proposals, never "
                     "established science.")

DBCFG = {}
DBCFG["unsolved-nursing"] = _cfg(
    "The Unsolved Nursing Database",
    "Thirty-four of nursing science's greatest unsolved problems - predicting patient deterioration, pressure injury prevention, alarm fatigue, nurse burnout, failure to rescue - each a fact-checked public record, each explored through a labeled Signature-generated proposed solution, taught in ladder order from the approachable to the profound.",
    "unsolved problem record", "JAH-USNU-", "JAH Unsolved Nursing Archivist",
    "unsolved nursing archivist - the famous open problems of nursing, what "
    "is known about each, why each matters, and the Signature system labeled "
    "proposed solution approaches; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math - using only "
    "archive data from this system",
    "public", "I am the JAH Unsolved Nursing Archivist. Ask me about the great unsolved problems of nursing science - from patient deterioration, pressure injuries, and alarm fatigue through burnout, staffing, and rescue - each with what is known, why it matters, and the Signature system's labeled proposed solution approach.")
DBCFG["unsolved-nursing-signature"] = _cfg(
    "The Unsolved Nursing Signature Database",
    "The same thirty-four unsolved problems through the Signature lens: every record carries the full Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established science, never clinical advice.",
    "unsolved problem record", "JAH-USNUS-", "JAH Unsolved Nursing Archivist (Signature)",
    "unsolved nursing archivist - Signature editions: the Signature system "
    "proposed solution approaches to the famous unsolved problems, clearly "
    "labeled Signature-made proposals and never established science; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math - using only archive data from this system",
    "signature",
    ("I am the JAH Unsolved Nursing Archivist (Signature). Ask me about the Signature system's "
     "proposed solution approaches to the great unsolved problems of nursing - each a clearly labeled "
     "proposal, never established science."))

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    sig_prefix = DBCFG["unsolved-nursing-signature"]["prefix"]
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
            # round8 assembly: LABEL opens how_it_works
            how = LABEL + " " + e["sig_lens"] + " " + e["why_it_matters"] + " " + e["sig_full"]
            citations = list(e["citations"]) + [SIG_TAIL]
            sigsol = LABEL + " " + e["sig_full"]
        else:
            description = e["description"]
            how = (LABEL + " " + e["why_it_matters"] + " The Signature system's proposed approach "
                   "to this problem is explored in full in the companion Signature Edition record "
                   "(%s%06d), which lays out assumptions, reasoning path, a proposed "
                   "mechanism, what would confirm or kill it, and what it does not "
                   "claim. " % (sig_prefix, len(recs) + 1)
                   + e["sig_pointer"])
            citations = list(e["citations"])
            sigsol = (LABEL + " The Signature system's proposed approach to this problem is "
                      "explored in full in the companion Signature Edition record "
                      "(%s%06d), which lays out assumptions, reasoning path, a proposed "
                      "mechanism, what would confirm or kill it, and what it does not "
                      "claim. " % (sig_prefix, len(recs) + 1)
                      + e["sig_pointer"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": sigsol,
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
                       "note": "Working solution-explorer demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def node_check_js(path):
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    blocks = []
    for m in re.finditer(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                         html, re.S | re.I):
        body = m.group(1).strip()
        if body:
            blocks.append(body)
    for i, body in enumerate(blocks):
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
            tf.write(body)
            tf.flush()
            p = subprocess.run(["node", "--check", tf.name],
                               capture_output=True, text=True, timeout=60)
        os.unlink(tf.name)
        assert p.returncode == 0, "node --check failed on %s block %d: %s" % (path, i, p.stderr[:500])
    return len(blocks)


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
    for slug in ("unsolved-nursing", "unsolved-nursing-signature"):
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
            for k in ("id", "t", "g", "name", "title", "problem", "background",
                      "why_it_matters", "signature_solution", "description",
                      "how_it_works", "key_points", "requirements", "standards",
                      "citations", "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            # LABEL GATE (round8): how_it_works OPENS with the exact em-dash label, both halves
            assert r["how_it_works"].startswith(LABEL), "honesty label not at record open in %s" % r["id"]
            assert r["signature_solution"].startswith(LABEL), "label missing in signature_solution %s" % r["id"]
            assert HYPHEN_LABEL not in r["how_it_works"], "hyphen label leftover in %s" % r["id"]
            assert HYPHEN_LABEL not in r["signature_solution"], "hyphen label leftover in sigsol %s" % r["id"]
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
        print("shard: %-38s %d records" % (slug, n), flush=True)

    label_ok = sum(1 for recs in built.values() for r in recs
                   if r["how_it_works"].startswith(LABEL))
    assert label_ok == 68, "label gate: %d/68 open with label" % label_ok
    print("label gate: %d/68 records open with exact label; 0 hyphen leftovers" % label_ok, flush=True)

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
        assert "unsolved" in page.lower()
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["ladder_tier"].capitalize(), []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        nblocks = node_check_js(ppath)
        p = subprocess.run(["node", "--check", gpath], capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "node --check failed on %s: %s" % (gpath, p.stderr[:500])
        print("page:  db/%s/index.html + gen-%s.js [%s] js-blocks=%d node-clean"
              % (slug, slug, ", ".join(notes), nblocks), flush=True)

    # NOTE: manifest.json / api.json / index.html / README / docs are owned by
    # the merger - this build deliberately does not touch them.
    print("built 2 databases, %d records. fragment + registration left to merger." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
