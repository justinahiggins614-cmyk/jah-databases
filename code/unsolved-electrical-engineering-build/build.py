#!/usr/bin/env python3
"""Build the Unsolved Electrical Engineering databases for JAH Databases
(Manon 2026-10-17 16:15 orders, Unsolved Problems Solved series).

Verified 2026-10-17: ID prefixes JAH-USEE- (public) and JAH-USEES-
(signature) have ZERO hits across data/manifest.json id_prefix values AND
across all record IDs in ~/workspace/jah-databases-data-1/data/. Slugs
unsolved-electrical-engineering / -signature have zero manifest hits. The
whole-system exact-title dedupe gate runs at build time over all 68 titles.

So this build creates two NEW databases, 34 ladder-ordered records each:

  unsolved-electrical-engineering            - The Unsolved Electrical
                                              Engineering Database
                                              (public-harvest: real,
                                              fact-checked famous unsolved
                                              electrical-engineering
                                              problems - wireless power at
                                              distance, grid stability with
                                              100% renewables, terahertz
                                              electronics, beyond-silicon
                                              computing, quantum
                                              interconnects, and 29 more -
                                              civilian only)
  unsolved-electrical-engineering-signature  - The Unsolved Electrical
                                              Engineering Signature
                                              Database
                                              (his original Signature
                                              Engineering Method: full
                                              Signature-generated proposed
                                              solutions, honesty-labeled,
                                              src signature, titles suffixed
                                              " (Signature Edition)")

34 records each, ordered by the teaching ladder (ladder_rank 1-34,
ladder_tier approachable/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Standing exclusion honored: nothing on neutralizing or defeating military
or defense-grade systems - every problem is civilian. No religious talk.
Nothing hate-adjacent, profane, or inappropriate.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_electrical_engineering.py). Every demo is a
solution-explorer walkthrough: adjustable assumptions, real computed
values, tight-bounds asserts (never float exact-equality), an explicit
CONFIRM / REFUTE panel, and the OK marker; the build machine-executes all
68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes - the merger handles those. It only writes db/unsolved-electrical-
engineering*/ pages, the shard data dirs, its own code dir, and the
handoff fragment.

No website references. No Facebook.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-electrical-engineering.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_electrical_engineering import ENTRIES, SIG_TAIL, SIG_LABEL
from demos_unsolved_electrical_engineering import DEMOS

OWN_SLUGS = ("unsolved-electrical-engineering",
             "unsolved-electrical-engineering-signature")

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Engineering "
                "Method applied to the same 34 famous unsolved electrical "
                "engineering problems: full Signature-generated proposed "
                "solution approaches with stated assumptions, reasoning "
                "paths, proposed mechanisms, confirm-or-kill evidence, and "
                "what each approach does NOT claim. Clearly labeled "
                "Signature-made, never presented as established science or "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked famous unsolved "
                "electrical engineering problems across power systems, "
                "computing hardware, wireless and RF, devices and "
                "materials, and quantum electronics: wireless power at "
                "distance, grid stability with 100 percent renewables, "
                "terahertz electronics at room temperature, beyond-silicon "
                "transistors, quantum interconnects, and 29 more - every "
                "record carrying the problem statement, its history, why "
                "it matters, and a short pointer to the Signature "
                "proposed solution. Civilian problems only.")
    ladder = (" Records are ordered by the teaching ladder: Approachable "
              "(wireless power transfer, 100-percent-renewable grid "
              "stability, room-temperature terahertz, beyond-silicon "
              "transistors, quantum interconnects, universal memory, chip "
              "thermal wall, ambient energy harvesting, EMI coexistence, "
              "ultra-fast charging, solid-state transformers, "
              "superconducting cables) -> Compounded (silicon photonics, "
              "spintronic logic, neuromorphic chips, single-molecule "
              "electronics, cryogenic logic, dynamic wireless charging, "
              "EMP hardening, HVDC breakers, wide-bandgap cost, motor "
              "power density, solid-state lidar, implant wireless power) "
              "-> Advanced (terahertz links, SMES economics, backscatter "
              "networks, noninvasive BCIs, picosecond power delivery, "
              "self-healing grids, reversible logic, antenna size limit, "
              "room-temperature photon detectors, million-qubit wiring).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: problem, background, why it matters, "
                  "the Signature proposed solution, citations, and a working solution-explorer "
                  "demonstration program with confirm and refute panels.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search wireless power, grid stability, terahertz, beyond-silicon, quantum interconnects, universal memory, photonics, spintronics, HVDC, antennas, lidar, SMES...",
        "chat_ph": "Ask about unsolved electrical engineering problems...",
        "archive_blurb": ("Seeded %s unsolved electrical engineering records, marching toward one million records. "
                          "Presented in teaching-ladder order: approachable, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, problem, background, why_it_matters, signature_solution, "
                   "src, ladder_rank, ladder_tier, demo, citations"),
        "fields": "Power Systems \u00b7 Computing Hardware \u00b7 Wireless & RF \u00b7 Devices & Materials \u00b7 Quantum Electronics - each field opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved electrical engineering studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the famous open problems of electrical engineering - from wireless power and grid stability through terahertz electronics, beyond-silicon transistors, and quantum interconnects, to superconducting cables, HVDC breakers, and million-qubit wiring. Every problem here is OPEN in established science; the Signature approaches are proposed paths, labeled as such, never settled science." % ai,
        "gen_fields": ["Power Systems", "Computing Hardware", "Wireless & RF", "Devices & Materials", "Quantum Electronics"],
        "gen_kind": "unsolved-electrical-engineering-study", "gen_demo_kind": "unsolved-electrical-engineering-demo",
        "source": source,
    }

CIT_PUB = ("Unsolved electrical engineering problems (standard references: "
           "IEEE Transactions and Proceedings papers cited per record; U.S. "
           "DOE grid modernization and energy storage programs; NERC "
           "reliability standards including TPL-007 and IEEE 1547/2800; "
           "the IRDS roadmap 2023; ITU-R propagation models; and the "
           "other landmarks cited per record).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Engineering Method - proposed solution approaches, "
                     "honesty-labeled, clearly labeled Signature-made.")

DBCFG = {}
DBCFG["unsolved-electrical-engineering"] = _cfg(
    "unsolved-electrical-engineering", "The Unsolved Electrical Engineering Database",
    "The famous unsolved problems of electrical engineering, fact-checked: "
    "wireless power at distance, grid stability with 100 percent "
    "renewables, terahertz electronics at room temperature, beyond-silicon "
    "transistors, quantum interconnects, and 29 more - every record "
    "carrying the problem, its history, why it matters, and a pointer to "
    "the Signature proposed solution.",
    "unsolved problem record", "JAH-USEE-", "JAH Unsolved Electrical Engineering Archivist",
    "unsolved electrical engineering archivist - the famous open problems "
    "of electrical engineering across power systems, computing hardware, "
    "wireless and RF, devices and materials, and quantum electronics, and "
    "the Signature proposed solution approaches; teaches progressively "
    "along the ladder from approachable through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system; "
    "answers honestly that each problem is OPEN in established science "
    "and the Signature approach is a proposed path, labeled as such",
    CIT_PUB, "public")
DBCFG["unsolved-electrical-engineering-signature"] = _cfg(
    "unsolved-electrical-engineering-signature", "The Unsolved Electrical Engineering Signature Database",
    "His original Signature Engineering Method applied to the 34 famous "
    "unsolved electrical engineering problems: full Signature-generated "
    "proposed solutions - assumptions, reasoning paths, proposed "
    "mechanisms, confirm-or-kill evidence, and what each approach does "
    "not claim. Clearly labeled Signature-made, never presented as "
    "established science.",
    "unsolved problem record", "JAH-USEES-", "JAH Unsolved Electrical Engineering Archivist (Signature)",
    "unsolved electrical engineering archivist - Signature editions: his "
    "original Signature Engineering Method applied to the famous open "
    "problems of electrical engineering, clearly labeled Signature-made "
    "and never presented as established science or authentic public "
    "record; teaches progressively along the ladder from approachable "
    "through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
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
        if [h for h in base.GATE.check(slug, title) if h[0] not in OWN_SLUGS]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        sig_rid = "JAH-USEES-%06d" % (len(recs) + 1)
        if sig:
            solution = SIG_LABEL + " " + e["signature_solution"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            solution = (SIG_LABEL + " " + e["sig_pointer"] + " The full "
                        "Signature-generated treatment lives in record " +
                        sig_rid + " of the Unsolved Electrical Engineering "
                        "Signature Database.")
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": solution,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
            "citations": citations,
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, title, rid, e["group"], e)
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Solution-explorer walkthrough: adjustable assumptions, computed numbers, confirm/refute panels (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    frag = {}
    for slug in ("unsolved-electrical-engineering",
                 "unsolved-electrical-engineering-signature"):
        cfg = DBCFG[slug]
        source = "signature" if slug.endswith("-signature") else "public-harvest"
        ai = cfg["ai"]
        frag["public" if source == "public-harvest" else "signature"] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": ai,
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(built[slug]),
            "status": "live",
            "full_records": len(built[slug]),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": source,
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
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
    for slug in ("unsolved-electrical-engineering",
                 "unsolved-electrical-engineering-signature"):
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
                      "why_it_matters", "signature_solution", "src",
                      "ladder_rank", "ladder_tier", "demo", "citations"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["background"]) > 200, "stub in %s" % r["id"]
            assert len(r["problem"]) > 100 and len(r["why_it_matters"]) > 100, \
                "thin field in %s" % r["id"]
            assert r["signature_solution"].startswith(SIG_LABEL), \
                "honesty label missing in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("approachable", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "'" not in r["t"], "apostrophe in title %s" % r["id"]
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
            assert "CONFIRM:" in p.stdout and "REFUTE:" in p.stdout, \
                "demo missing confirm/refute panel %s" % r["id"]
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
        assert "facebook" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "template leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)
    # NOTE: manifest.json, api.json, index.html, README.md, docs/AI_ACCESS.md
    # are owned by the merger - this build intentionally does not touch them,
    # and never git commits or pushes.
    print("records: %d public + %d signature = %d total" %
          (len(built["unsolved-electrical-engineering"]),
           len(built["unsolved-electrical-engineering-signature"]), total))
    print("NEXT (merger): register manifest/api entries, run restamp_counts.py, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
