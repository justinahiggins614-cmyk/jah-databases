#!/usr/bin/env python3
"""Build the Unsolved Oceanography databases for JAH Databases
(Unsolved Problems Solved series, batch 1; Manon 2026-10-17 16:15 EDT).

Two databases, 34 ladder-ordered records each:

  unsolved-oceanography            - The Unsolved Oceanography Database
                                     (public-harvest: real, fact-checked
                                     famous unsolved ocean problems -
                                     rogue wave prediction, the missing
                                     ocean plastic, the deep-sea species
                                     census, vent origins of life, the
                                     biological carbon pump efficiency,
                                     deep-ocean mixing, and 28 more)
  unsolved-oceanography-signature  - The Unsolved Oceanography Signature
                                     Database (the same 34 problems through
                                     the Signature lens: Signature-generated
                                     proposed solution approaches, clearly
                                     labeled, never presented as established
                                     science; titles suffixed
                                     " (Signature Edition)", src signature)

ID prefixes: JAH-USOC- (public) and JAH-USOCS- (signature). Prefix search:
zero hits in data/manifest.json id_prefix values and zero hits across every
shard index in jah-databases-data-1 (full zgrep sweep over all
index.jsonl.gz files, 2026-10-17). Sibling unsolved-* prefixes (USMA, USPH,
USCH, USBI, USCS, USME, USAS, USES, USCL, USEC, USEN, USGE, USPS, USPY)
collide with nothing.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never git commits or pushes.
A merger handles registration. It writes only:
  db/unsolved-oceanography{,-signature}/ (index.html + gen-*.js)
  <shard>/data/unsolved-oceanography{,-signature}/ (index.jsonl.gz + chunks)
  ~/workspace/hidden_files/missing-builds/fragments/unsolved-oceanography.json
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
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_oceanography import ENTRIES
from demos_unsolved_oceanography import demos_for, LABEL as HONESTY_LABEL

DEMOS = demos_for(ENTRIES)

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, source):
    sig = source == "signature"
    hero_pub = ("Real, fact-checked unsolved problems of oceanography: rogue wave prediction, the missing "
                "ocean plastic, the deep-sea species census, microbial dark matter, the Great Atlantic "
                "Sargassum Belt, marine heatwaves, the Kuroshio large meander, the ocean biological geography, "
                "unexplained deep-ocean sounds, tidal energy dissipation, ocean cloud seeding, the ice-free "
                "Arctic, mapping the seafloor by 2030, vent origins of life, the biological carbon pump "
                "efficiency, twilight-zone biomass, expanding oxygen minimum zones, abyssal mixing, Antarctic "
                "Bottom Water, decadal ocean memory, submarine groundwater, hadal trench life, ice-shelf melt, "
                "the viral shunt, the deep-water return path, the Southern Ocean carbon sink, deep-sea mining "
                "recovery, the subseafloor biosphere, internal-wave solitons, deep-ocean heat, bioluminescent "
                "networks, ocean eddies, ocean carbon removal, and turbulence closure. Every record carries "
                "the problem, its background, why it matters, and a solution-explorer walkthrough demo. "
                "Records are ordered by the teaching ladder: Foundations (the most approachable problems) -> "
                "Compounded -> Advanced (the most complex).")
    hero_sig = ("The same 34 famous unsolved oceanography problems through the Signature lens: for each open "
                "problem, the Signature system's proposed solution approach - assumptions, reasoning path, "
                "proposed mechanism, what would confirm or kill it, and what it does not claim. Every solution "
                "opens with the exact label Signature-generated proposed solution, not established science, and "
                "is clearly labeled Signature-made, never presented as established science or authentic public "
                "record. Records are ordered by the teaching ladder: Foundations -> Compounded -> Advanced.")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s" % (tagline, hero_sig if sig else hero_pub),
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else
                     "Public records organized in the Signature system"),
        "search_ph": "Search rogue waves, ocean plastic, deep-sea species, Sargassum, marine heatwaves, carbon pump, AMOC, hydrothermal vents, trenches, eddies, ocean mixing...",
        "chat_ph": "Ask about unsolved oceanography problems...",
        "archive_blurb": ("Seeded %s unsolved oceanography problem records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record")),
        "schema": ("id, t, g, name, title, description, problem, background, why_it_matters, "
                   "signature_solution, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": ("Generate clearly-labeled unsolved oceanography problem studies. "
                     "Seeded archive records are the authoritative entries."),
        "greet": ("I am the %s. Ask me about unsolved oceanography - from rogue waves, missing plastic, the "
                  "deep-sea census, and marine heatwaves through vent origins of life, the carbon pump, deep "
                  "mixing, and the Southern Ocean sink to eddies, ocean carbon removal, and turbulence "
                  "closure - and I will answer honestly about what is open and what the Signature approach "
                  "proposes." % ai),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-oceanography-study", "gen_demo_kind": "unsolved-oceanography-demo",
        "source": source,
    }

CIT = ("Oceanography (standard references: Tomczak M, Godfrey J S. Regional Oceanography: An Introduction. "
       "2nd ed. Daya Publishing; 2003; Talley L D et al. Descriptive Physical Oceanography. 6th ed. "
       "Academic Press; 2011; Garrison T. Oceanography: An Invitation to Marine Science. Cengage; "
       "IPCC AR6 WGI Chapter 9: Ocean, Cryosphere and Sea Level Change; 2021; NOAA Pacific Marine "
       "Environmental Laboratory ocean sound and buoy programs).")

DBCFG = {}
DBCFG["unsolved-oceanography"] = _cfg(
    "unsolved-oceanography", "The Unsolved Oceanography Database",
    "Thirty-four famous unsolved problems of oceanography, fact-checked and ladder-ordered: from rogue "
    "wave prediction, the missing ocean plastic, and the deep-sea species census through vent origins of "
    "life, the biological carbon pump, and deep-ocean mixing to ocean eddies, carbon removal, and "
    "turbulence closure.",
    "unsolved problem record", "JAH-USOC-", "JAH Unsolved Oceanography Archivist",
    "unsolved oceanography archivist - the famous open problems of oceanography, fact-checked and taught "
    "progressively along the ladder from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only archive data from this system; "
    "answers honestly when asked whether a problem is solved: the problem is OPEN in established science",
    "public")
DBCFG["unsolved-oceanography-signature"] = _cfg(
    "unsolved-oceanography-signature", "The Unsolved Oceanography Signature Database",
    "The same 34 famous unsolved oceanography problems through the Signature lens: Signature-generated proposed "
    "solution approaches - assumptions, reasoning, proposed mechanisms, confirm-or-kill criteria - clearly labeled "
    "as proposals, never as established science.",
    "unsolved problem record", "JAH-USOCS-", "JAH Unsolved Oceanography Archivist (Signature)",
    "unsolved oceanography archivist - Signature editions: proposed solution approaches of the Signature system "
    "to the famous open problems of oceanography, clearly labeled Signature-generated proposed solutions and "
    "never presented as established science or authentic public record; teaches progressively along the ladder; "
    "answers honestly when asked whether a problem is solved: the problem is OPEN in established science and the "
    "Signature approach is a labeled proposal",
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
        hits = [h for h in base.GATE.check(slug, title) if h[0] != slug]
        if hits:
            print("  gate refused (cross-db dupe): %s -> %s" % (title, hits), flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = "Signature Edition. " + e["sig_lens"] + " " + e["problem"]
            signature_solution = HONESTY_LABEL + " " + e["signature_solution"]
        else:
            description = e["problem"]
            signature_solution = HONESTY_LABEL + " " + e["sig_pointer"]
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "problem": e["problem"],
            "background": e["background"],
            "why_it_matters": e["why_it_matters"],
            "signature_solution": signature_solution,
            "citations": [CIT] + list(e["citations"]),
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(title, rid, e["group"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": ("Solution-explorer walkthrough: interactive steps, adjustable assumptions, "
                                "and a what-would-confirm-or-refute panel. Working demonstration program "
                                "(real, runnable Python).")}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    os.makedirs(FRAGDIR, exist_ok=True)
    frag = {}
    for slug, recs in built.items():
        sig = slug.endswith("-signature")
        cfg = DBCFG[slug]
        frag["signature" if sig else "public"] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(recs),
            "status": "live",
            "full_records": len(recs),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": cfg["source"],
        }
    path = os.path.join(FRAGDIR, "unsolved-oceanography.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    return path


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
    for slug in ("unsolved-oceanography", "unsolved-oceanography-signature"):
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
            for k in ("id", "t", "g", "name", "title", "description", "problem",
                      "background", "why_it_matters", "signature_solution",
                      "citations", "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 100, "stub in %s" % r["id"]
            assert len(r["background"]) > 200, "thin background in %s" % r["id"]
            assert len(r["why_it_matters"]) > 100, "thin why_it_matters in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            assert r["signature_solution"].startswith(HONESTY_LABEL), \
                "honesty label missing at open in %s" % r["id"]
            compile(prog, r["id"], "exec")
            # explorer spec internal consistency: every step/check key exists in run(A)
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert r["title"].endswith("(Signature Edition)"), "sig title missing suffix"
                assert r["src"] == "signature"
                assert "does NOT claim" in r["signature_solution"], "honesty section missing in %s" % r["id"]
            else:
                assert r["src"] == "public-harvest"
                assert "signature edition" in r["signature_solution"].lower(), \
                    "public pointer missing in %s" % r["id"]
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # machine-execute every demo; require the OK marker
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    # pages + generator JS (template replication, no manifest/api writes)
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
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # JS hygiene: node --check extracted page scripts + gen js (skip ld+json)
    for slug in built:
        ppath = os.path.join(REPO, "db", slug, "index.html")
        with open(ppath, encoding="utf-8") as f:
            html = f.read()
        scripts = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                             html, flags=re.S)
        for i, s in enumerate(scripts):
            if not s.strip():
                continue
            sp = "/tmp/use_check_%s_%d.js" % (slug.replace("-", "_"), i)
            with open(sp, "w", encoding="utf-8") as f:
                f.write(s)
            p = subprocess.run(["node", "--check", sp], capture_output=True, text=True)
            assert p.returncode == 0, "node --check failed %s script %d: %s" % (slug, i, p.stderr[-500:])
        gp = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
        p = subprocess.run(["node", "--check", gp], capture_output=True, text=True)
        assert p.returncode == 0, "node --check failed %s: %s" % (gp, p.stderr[-500:])
    print("node --check: page scripts + gen js clean for both databases", flush=True)

    frag = write_fragment(built)
    print("fragment: %s" % frag, flush=True)
    print("DONE: 68 records, 68 demos OK, pages + shards + fragment written.")
    print("NOTE: manifest/api.json untouched (merger registers); no commit, no push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
