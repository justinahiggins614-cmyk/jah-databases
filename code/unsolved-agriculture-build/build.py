#!/usr/bin/env python3
"""Build the Unsolved Agriculture databases for JAH Databases
(Manon 2026-10-17 16:15 orders - Unsolved Problems Solved series).

Two NEW databases, 34 ladder-ordered records each:

  unsolved-agriculture              - The Unsolved Agriculture Database
                                      (public-harvest: 34 real, fact-checked
                                      unsolved agricultural problems - feeding
                                      10 billion sustainably, nitrogen-use
                                      efficiency, drought-proof staple crops,
                                      soil microbiome management, closing the
                                      yield gap without new land, phosphorus,
                                      soil erosion, irrigation water,
                                      post-harvest loss, pesticide resistance,
                                      livestock methane, pollinators, and the
                                      rest - each carrying problem,
                                      background, why-it-matters, and a short
                                      pointer to the Signature proposed
                                      solution)
  unsolved-agriculture-signature    - The Unsolved Agriculture Signature
                                      Database
                                      (his original Signature proposed
                                      solution approaches to the same 34
                                      problems; src signature, titles suffixed
                                      " (Signature Edition)"; every
                                      signature_solution opens with the EXACT
                                      label "Signature-generated proposed
                                      solution \u2014 not established science";
                                      never claiming proof or peer acceptance;
                                      never presented as authentic public
                                      record)

34 records each, ladder-ordered by problem accessibility (ladder_rank 1-34,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-USAG- (public) and JAH-USAGS- (signature), verified free
2026-10-17: zero hits in manifest id_prefix values AND in all record IDs of
jah-databases-data-1.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_agriculture.py). Every demo is a
solution-explorer walkthrough: interactive steps, adjustable assumptions,
real computed values, tight-bounds asserts (never float exact-equality),
a confirm/refute panel, and the OK marker; the build machine-executes all
68 demos.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. It writes only: db/unsolved-agriculture[-signature]/
(index.html + gen-*.js), the shard data dirs, and the fragment file.
A merger handles manifest/api/restamp/commit.

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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/unsolved-agriculture.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_unsolved_agriculture import ENTRIES, SIG_TAIL, SIG_LABEL
from demos_unsolved_agriculture import DEMOS

# ---------------------------------------------------------------- DB config

FOUND_LIST = ("feeding 10 billion sustainably, closing the yield gap without "
              "new land, nitrogen-use efficiency, peak phosphorus, "
              "drought-proof staples, soil erosion, irrigation water, "
              "post-harvest loss, pesticide resistance, livestock methane, "
              "pollinator decline")
COMP_LIST = ("nitrogen-fixing cereals, C4 rice, soil microbiome management, "
             "heat sterility at flowering, salinity intrusion, groundwater "
             "depletion, the narrow genetic base, mycotoxins under warming, "
             "land competition, nitrous oxide, the precision-ag digital "
             "divide, seed systems for smallholders")
ADV_LIST = ("apomixis, perennial grains, re-domesticating orphan crops, "
            "synthetic symbiosis, crop wild relatives, multi-stress stacking, "
            "the rhizosphere signaling code, regenerative agriculture at "
            "scale, controlled-environment staples, One Health at the farm "
            "gate, the ultimate yield ceiling")


def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original proposed solution "
                "approaches to each of the 34 unsolved agricultural "
                "problems: every signature_solution opens with the "
                "exact label 'Signature-generated proposed solution "
                "\u2014 not established science', lays out assumptions, "
                "reasoning path, proposed mechanism, what would confirm "
                "or kill it, and what it does not claim. Clearly labeled "
                "Signature-made, never presented as established science "
                "or authentic public record.")
    pub_line = ("Public records - 34 real, fact-checked unsolved "
                "agricultural problems: feeding 10 billion sustainably, "
                "nitrogen-use efficiency, drought-proof staple crops, "
                "soil microbiome management, closing the yield gap without "
                "new land, phosphorus, soil erosion, irrigation water, "
                "post-harvest loss, pesticide resistance, livestock "
                "methane, pollinators, nitrogen-fixing cereals, C4 rice, "
                "heat sterility, salinity, groundwater, the genetic base, "
                "mycotoxins, land competition, nitrous oxide, the digital "
                "divide, seed systems, apomixis, perennial grains, orphan "
                "crops, synthetic symbiosis, crop wild relatives, "
                "multi-stress stacking, the rhizosphere code, regenerative "
                "scale, controlled-environment staples, One Health, and "
                "the yield ceiling - each carrying the problem, its "
                "background, why it matters, and a short pointer to the "
                "Signature proposed solution, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(%s) -> Compounded (%s) -> Advanced (%s)."
              % (FOUND_LIST, COMP_LIST, ADV_LIST))
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s - %s Every record carries the full entry: problem, background, "
                  "why it matters, the Signature proposed solution, key points, "
                  "requirements, standards, citations, and a working solution-explorer "
                  "walkthrough program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder)),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": ("Search feeding 10 billion, nitrogen efficiency, drought crops, "
                       "soil microbiome, yield gap, phosphorus, erosion, irrigation, "
                       "methane, pollinators, C4 rice, apomixis, perennials..."),
        "chat_ph": "Ask about unsolved agriculture problems...",
        "archive_blurb": ("Seeded %s unsolved agriculture problem records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, signature_solution, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved agriculture studies. Seeded archive records are the authoritative entries.",
        "greet": ("I am the %s. Ask me about unsolved agriculture - from feeding 10 billion and the yield gap "
                  "through nitrogen, water, soil, pests, and livestock, to nitrogen-fixing cereals, C4 rice, "
                  "apomixis, perennial grains, and the ultimate yield ceiling." % ai),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-agriculture-study", "gen_demo_kind": "unsolved-agriculture-demo",
        "source": source,
    }

CIT_PUB = ("Agriculture (standard references: FAO. The State of Food and "
           "Agriculture. Rome (annual); FAO. The State of Food Security and "
           "Nutrition in the World. Rome (annual); Erisman JW et al. Nature "
           "Geoscience; 2008; Mueller ND et al. Nature; 2012; Gleeson T et "
           "al. Nature; 2012; Klein AM et al. Proc. R. Soc. B; 2007; "
           "Gerber PJ et al. FAO; 2013; Montgomery DR. PNAS; 2007; Cordell "
           "D et al. Global Environmental Change; 2009).")
CIT_SIG = CIT_PUB + (" Signature editions carry his original proposed "
                     "solution approaches - clearly labeled "
                     "Signature-generated proposed solutions, never "
                     "presented as established science.")

DBCFG = {}
DBCFG["unsolved-agriculture"] = _cfg(
    "unsolved-agriculture", "The Unsolved Agriculture Database",
    "The famous unsolved problems of agriculture - feeding 10 billion "
    "sustainably, nitrogen-use efficiency, drought-proof staple crops, "
    "soil microbiome management, closing the yield gap without new land, "
    "phosphorus, erosion, water, waste, resistance, methane, pollinators, "
    "and the rest - each stated honestly as an open problem with its "
    "background, why it matters, and a pointer to the Signature proposed "
    "solution. Taught progressively along the ladder.",
    "unsolved problem record", "JAH-USAG-", "JAH Unsolved Agriculture Archivist",
    "unsolved agriculture archivist - the famous open problems of "
    "agriculture, stated honestly with background and why-it-matters, "
    "teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system; answers the is-this-solved question honestly: the problem is "
    "open in established science and the Signature approach is a proposed "
    "path, labeled as such",
    CIT_PUB, "public")
DBCFG["unsolved-agriculture-signature"] = _cfg(
    "unsolved-agriculture-signature", "The Unsolved Agriculture Signature Database",
    "His original proposed solution approaches to the 34 unsolved "
    "agricultural problems - every solution opening with the exact label "
    "'Signature-generated proposed solution \u2014 not established science', "
    "with assumptions, reasoning path, proposed mechanism, confirm-or-kill "
    "evidence, and what it does not claim. Clearly labeled Signature-made, "
    "never presented as established science.",
    "unsolved problem record", "JAH-USAGS-", "JAH Unsolved Agriculture Archivist (Signature)",
    "unsolved agriculture archivist - Signature editions: his original "
    "proposed solution approaches to each unsolved problem, every one "
    "opening with the exact honesty label, "
    "clearly labeled Signature-made and never "
    "presented as established science or authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles using only archive data from this "
    "system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {"explorer"}, "demo map must carry the explorer factory"
assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)


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
            description = ("Signature original proposed solution. " +
                           e["sig_full"])
            how = ("Background: " + e["background"] + " Why it matters: " +
                   e["why_it_matters"])
            citations = list(e["citations"]) + [SIG_TAIL]
            sigsol = e["sig_full"]
        else:
            description = ("Problem: " + e["problem"] + " " + e["sig_pointer"])
            how = ("Background: " + e["background"] + " Why it matters: " +
                   e["why_it_matters"])
            citations = list(e["citations"])
            sigsol = (SIG_LABEL + " The public half of this record carries "
                      "only a short pointer. The full proposed solution "
                      "approach - assumptions, reasoning path, proposed "
                      "mechanism, what would confirm or kill it, and what it "
                      "does not claim - is developed in the Signature "
                      "edition of this record, 'The Unsolved Agriculture "
                      "Signature Database'.")
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
            "signature_solution": sigsol,
        }
        demo_fn = DEMOS["explorer"]
        program = demo_fn(base._hdr, name if not sig else title, rid,
                          e["group"], e["key_points"],
                          "; ".join(e["requirements"]), e["demo"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Solution-explorer walkthrough (real, runnable Python): "
                               "interactive steps, adjustable assumptions, real computed "
                               "values, and a confirm/refute panel."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment(built):
    frag = {}
    for slug in ("unsolved-agriculture", "unsolved-agriculture-signature"):
        cfg = DBCFG[slug]
        sig = slug.endswith("-signature")
        key = "signature" if sig else "public"
        frag[key] = {
            "ai_name": cfg["ai"],
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
            "full_records": 34,
            "id_prefix": cfg["prefix"],
            "index": "%s/data/%s/index.jsonl.gz" % (SHARD_BASE, slug),
            "local_index": "%s/data/%s/index.jsonl.gz" % (SHARD_BASE, slug),
            "name": cfg["name"],
            "record_count": 34,
            "record_kind": "unsolved problem record",
            "slug": slug,
            "source": "signature" if sig else "public-harvest",
            "status": "live",
            "tagline": cfg["tagline"],
        }
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
    for slug in ("unsolved-agriculture", "unsolved-agriculture-signature"):
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
                      "src", "ladder_rank", "ladder_tier", "signature_solution",
                      "demo"):
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
            assert SIG_LABEL.lower() in r["signature_solution"].lower(), \
                "honesty label missing in %s" % r["id"]
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
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment(built)

    # Manifest/api.json/restamp/commit are the merger's job - we stop here.
    print("records: %d total (34 public + 34 signature)" % total)
    print("NEXT (merger): manifest + api.json entries, restamp_counts.py, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
