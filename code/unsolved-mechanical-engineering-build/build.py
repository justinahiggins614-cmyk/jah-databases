#!/usr/bin/env python3
"""Build the Unsolved Mechanical Engineering databases for JAH Databases
(Manon 2026-10-17 16:15 orders, Unsolved Problems Solved series).

Whole-system dedupe: titles checked against the full manifest via
DedupeGate before writing; ID prefixes JAH-USMC- / JAH-USMCS- verified
with zero hits across all manifest id_prefix values and every record ID
in the data-1 shards.

Two NEW databases, 34 ladder-ordered records each:

  unsolved-mechanical-engineering            - The Unsolved Mechanical
      Engineering Database (public-harvest: real, fact-checked famous
      unsolved mechanical engineering problems - turbulence control,
      friction and wear prediction, metamaterial manufacturing at scale,
      soft robotics control, energy-harvesting efficiency limits)
  unsolved-mechanical-engineering-signature  - The Unsolved Mechanical
      Engineering Signature Database (his original Signature Engineering
      Method: full Signature-generated proposed solutions, honesty-labeled,
      src signature, titles suffixed " (Signature Edition)")

34 records each, teaching ladder 1-34 (approachable/compounded/advanced);
the shard index is written in ladder order so pages present simple ->
compounded -> complex.

Every signature solution opens with the exact label
"Signature-generated proposed solution - not established science" and
never claims proof or peer acceptance.

Standing exclusions honored: civilian problems only (nothing on
neutralizing or defeating military or defense-grade systems), no
religious talk, nothing hate-adjacent or profane. No website references.
No Facebook.

Numerical cores: hand-specified 2026-10-17, machine-verified by the
demos (see demos_unsolved_mechanical_engineering.py). Every demo is a
solution-explorer walkthrough: adjustable assumptions, real computed
values, tight-bounds asserts, an explicit CONFIRM / REFUTE panel, and
the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or
pushes - the merger handles those. It only writes db/unsolved-mechanical-
engineering*/ pages, the shard data dirs, its own code dir, and the
handoff fragment.
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = ("/home/hatch/workspace/hidden_files/missing-builds/fragments/"
            "unsolved-mechanical-engineering.json")
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_mechanical_engineering import ENTRIES, SIG_TAIL, SIG_LABEL
from demos_unsolved_mechanical_engineering import DEMOS

OWN_SLUGS = ("unsolved-mechanical-engineering",
             "unsolved-mechanical-engineering-signature")

LADDER_TXT = (" Records are ordered by the teaching ladder: Approachable "
              "(bearing life, heat-exchanger fouling, gear contact fatigue, "
              "bolted-joint loosening, vibration energy harvesting, "
              "3D-printed parts, machine noise and vibration, small-scale "
              "turbomachinery, corrosion under insulation, friction and "
              "wear, cavitation erosion, thermal packaging) -> Compounded "
              "(turbulence closure, laminar-turbulent transition, drag "
              "reduction, nanoscale contact, galling, multiphase flow, "
              "flutter, thermoacoustic instability, metamaterial "
              "manufacturing, soft robot control, microrobot swimming, "
              "topology optimization) -> Advanced (compliant mechanism "
              "fatigue, random-load fatigue, creep-fatigue, superlubricity, "
              "active turbulence control, scramjet combustion, hypersonic "
              "transition, Navier-Stokes regularity, chaotic mixing "
              "control, megastructure tethers).")


def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig_line = ("Signature originals - his original Signature Engineering "
                "Method applied to the same 34 famous unsolved mechanical "
                "engineering problems: full Signature-generated proposed "
                "solution approaches with stated assumptions, reasoning "
                "paths, proposed mechanisms, confirm-or-kill evidence, and "
                "what each approach does NOT claim. Clearly labeled "
                "Signature-made, never presented as established science or "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked famous unsolved "
                "mechanical engineering problems across turbulence "
                "control, friction and wear, metamaterial manufacturing, "
                "soft robotics, and energy harvesting: turbulence drag "
                "reduction, the closure problem, friction and wear "
                "prediction, metamaterials at scale, soft robot control, "
                "energy-harvesting limits, and 28 more - every record "
                "carrying the problem statement, its history, why it "
                "matters, and a short pointer to the Signature proposed "
                "solution. Civilian problems only.")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s - %s Every record carries the full entry: problem, "
                   "background, why it matters, the Signature proposed "
                   "solution, citations, and a working solution-explorer "
                   "demonstration program with confirm and refute panels.%s"
                   % (tagline, sig_line if source == "signature" else pub_line,
                      LADDER_TXT)),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": ("Search turbulence control, drag reduction, friction, "
                      "wear, bearings, gears, metamaterials, soft robotics, "
                      "energy harvesting, cavitation, flutter, Navier-Stokes..."),
        "chat_ph": "Ask about unsolved mechanical engineering problems...",
        "archive_blurb": ("Seeded %s unsolved mechanical engineering records, "
                          "marching toward one million records. Presented in "
                          "teaching-ladder order: approachable, compounded, "
                          "advanced."
                          % ("Signature-original" if source == "signature"
                             else "public-record")),
        "schema": ("id, t, g, name, title, problem, background, "
                   "why_it_matters, signature_solution, src, ladder_rank, "
                   "ladder_tier, demo, citations"),
        "fields": ("Friction and Wear \u00b7 Turbulence and Fluids "
                   "\u00b7 Manufacturing and Metamaterials \u00b7 Soft "
                   "Robotics and Control \u00b7 Energy Harvesting and Thermal "
                   "- each field opens on demand and loads only what you open"),
        "gen_desc": ("Generate clearly-labeled unsolved mechanical "
                     "engineering studies. Seeded archive records are the "
                     "authoritative entries."),
        "greet": ("I am the %s. Ask me about the famous open problems of "
                  "mechanical engineering - from bearings, gears, and "
                  "friction through turbulence, drag reduction, and "
                  "metamaterials, to soft robots, energy harvesting, and "
                  "the Navier-Stokes regularity question. Every problem "
                  "here is OPEN in established science; the Signature "
                  "approaches are proposed paths, labeled as such, never "
                  "settled science." % ai),
        "gen_fields": ["Friction and Wear", "Turbulence and Fluids",
                       "Manufacturing and Metamaterials",
                       "Soft Robotics and Control",
                       "Energy Harvesting and Thermal"],
        "gen_kind": "unsolved-mechanical-engineering-study",
        "gen_demo_kind": "unsolved-mechanical-engineering-demo",
        "source": source,
    }


DBCFG = {}
DBCFG["unsolved-mechanical-engineering"] = _cfg(
    "unsolved-mechanical-engineering",
    "The Unsolved Mechanical Engineering Database",
    "The famous unsolved problems of mechanical engineering, fact-checked: "
    "turbulence control, friction and wear prediction, metamaterial "
    "manufacturing at scale, soft robotics control, energy-harvesting "
    "efficiency limits, and 29 more - every record carrying the problem, "
    "its history, why it matters, and a pointer to the Signature proposed "
    "solution.",
    "unsolved problem record", "JAH-USMC-",
    "JAH Unsolved Mechanical Engineering Archivist",
    "unsolved mechanical engineering archivist - the famous open problems "
    "of mechanical engineering across turbulence and fluids, friction and "
    "wear, manufacturing and metamaterials, soft robotics and control, and "
    "energy harvesting and thermal, and the Signature proposed solution "
    "approaches; teaches progressively along the ladder from approachable "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system; answers honestly that each problem is "
    "OPEN in established science and the Signature approach is a proposed "
    "path, labeled as such",
    "public")
DBCFG["unsolved-mechanical-engineering-signature"] = _cfg(
    "unsolved-mechanical-engineering-signature",
    "The Unsolved Mechanical Engineering Signature Database",
    "His original Signature Engineering Method applied to the 34 famous "
    "unsolved mechanical engineering problems: full Signature-generated "
    "proposed solutions - assumptions, reasoning paths, proposed "
    "mechanisms, confirm-or-kill evidence, and what each approach does not "
    "claim. Clearly labeled Signature-made, never presented as established "
    "science.",
    "unsolved problem record", "JAH-USMCS-",
    "JAH Unsolved Mechanical Engineering Archivist (Signature)",
    "unsolved mechanical engineering archivist - Signature editions: his "
    "original Signature Engineering Method applied to the famous open "
    "problems of mechanical engineering, clearly labeled Signature-made "
    "and never presented as established science or authentic public "
    "record; teaches progressively along the ladder from approachable "
    "through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def compose_signature_solution(e):
    s = e["sig"]
    parts = [
        SIG_LABEL,
        "Step one, stated assumptions: " + s["assumptions"],
        "Step two, the reasoning path: " + s["reasoning"],
        "Step three, the proposed mechanism: " + s["mechanism"],
        ("Step four, what would confirm or kill it: CONFIRM - " +
         s["confirm"] + " KILL - " + s["kill"]),
        ("What this approach does NOT claim: " + s["notclaim"]),
    ]
    return " ".join(parts)


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        hits = [h for h in base.GATE.check(slug, title) if h[0] not in OWN_SLUGS]
        if hits:
            print("  gate refused (cross-db dupe): %s -> %s" % (title, hits),
                  flush=True)
            continue
        n = len(recs) + 1
        rid = "%s%06d" % (cfg["prefix"], n)
        sig_rid = "JAH-USMCS-%06d" % n
        if sig:
            solution = compose_signature_solution(e)
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            solution = (SIG_LABEL + " " + e["sig_pointer"] + " The full "
                        "Signature-generated treatment lives in record " +
                        sig_rid + " of the Unsolved Mechanical Engineering "
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
                       "note": "Solution-explorer walkthrough: adjustable "
                               "assumptions, computed numbers, confirm/refute "
                               "panels (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    frag = {}
    for slug in OWN_SLUGS:
        cfg = DBCFG[slug]
        source = "signature" if slug.endswith("-signature") else "public-harvest"
        frag["public" if source == "public-harvest" else "signature"] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
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
    nb.SHARD_BASE = SHARD_BASE

    sweep_path = ("/home/hatch/workspace/goals/database-quality-audit/"
                  "hidden_files/patches/sweep-db-pages.py")
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in OWN_SLUGS:
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), \
            "prefix drift in %s" % slug
        assert len(recs) == 34, \
            "expected 34 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "problem",
                      "background", "why_it_matters", "signature_solution",
                      "src", "ladder_rank", "ladder_tier", "demo",
                      "citations"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["background"]) > 200, "stub in %s" % r["id"]
            assert (len(r["problem"]) > 100
                    and len(r["why_it_matters"]) > 100), \
                "thin field in %s" % r["id"]
            assert r["signature_solution"].startswith(SIG_LABEL), \
                "honesty label missing in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, \
                "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("approachable", "compounded",
                                        "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "'" not in r["t"], "apostrophe in title %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), \
                    "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-44s %d records" % (slug, n), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, \
                "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            assert "CONFIRM:" in p.stdout and "REFUTE:" in p.stdout, \
                "demo missing confirm/refute panel %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded "
            "archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, \
            "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), \
            "template leftover in %s" % slug
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
        assert "synthetic intelligence" not in gen_js.lower(), \
            "template leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        chk = subprocess.run(["node", "--check", gpath],
                             capture_output=True, text=True)
        assert chk.returncode == 0, \
            "node --check failed for %s: %s" % (gpath, chk.stderr)
        print("page:  db/%s/index.html + gen-%s.js [%s]" %
              (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)
    # NOTE: data/manifest.json, api.json, index.html, README.md,
    # docs/AI_ACCESS.md are owned by the merger - this build intentionally
    # does not touch them, and never git commits or pushes.
    print("records: %d public + %d signature = %d total" %
          (len(built[OWN_SLUGS[0]]), len(built[OWN_SLUGS[1]]), total))
    print("NEXT (merger): register manifest/api entries, run "
          "restamp_counts.py, commit + push.")
    return 0


if __name__ == "__main__":
    main()
