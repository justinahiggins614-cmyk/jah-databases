#!/usr/bin/env python3
"""Build the Price and Profit Tracking databases for JAH Databases
(Manon's orders 2026-10-17 15:32 EDT, #1-2).

Manon's order: "Profit and price marking database so each thing has a price
in a time (time for reference over time)" - "so AI knows what things are
worth, or if make something new it'll have a ballpark."

So this build creates two NEW databases, 34 ladder-ordered records each:

  price-profit-tracking            - The Price and Profit Tracking Database
                                     (public-harvest: real, fact-checked
                                     price and profit data - price anatomy,
                                     nominal vs real, supply and demand, cost
                                     types, markup vs margin, the CPI,
                                     reading price tags, break-even, profit
                                     layers, real series for gold (LBMA), oil
                                     (EIA/FRED), housing (Census/NAR),
                                     equities (S&P 500), inflation
                                     adjustment, depreciation methods,
                                     appreciation/CAGR, comparables, cost
                                     approach, income/DCF, elasticity,
                                     margins by industry, unit economics,
                                     price-index construction, time-series
                                     tools, purchasing-power lifetime,
                                     Fermi ballparks, analogous estimation,
                                     market multiples, inventory valuation,
                                     price forecasting, profit attribution,
                                     hurdle rate, pricing psychology, and
                                     the complete price record capstone)
  price-profit-tracking-signature  - The Price and Profit Tracking Signature Database
                                     (his original Signature Valuation
                                     Method: every price a covenant between
                                     maker and buyer sealed in time, profit
                                     the honest wage of value delivered, the
                                     price record the ledger line of that
                                     covenant; src signature, titles
                                     suffixed " (Signature Edition)", never
                                     presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-PFT- (public) and JAH-PFTS- (signature), verified free in
the manifest id_prefix values (zero hits) and in every shard index file of
jah-databases-data-1 (zero hits on the '"id":"JAH-PFT' prefix).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_price_profit_tracking.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

This build does NOT touch data/manifest.json, api.json, index.html,
README.md, or docs/AI_ACCESS.md, and does NOT commit or push - the merger
handles those. It writes only: db/price-profit-tracking[/-signature]/
(index.html + gen-*.js), and the shard data dirs.

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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_price_profit_tracking import ENTRIES, SIG_TAIL
from demos_price_profit_tracking import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Valuation "
                "Method: every price a covenant between maker and buyer "
                "sealed in time, profit the honest wage of value delivered, "
                "and the price record the ledger line of that covenant. "
                "Clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked price and profit data: "
                "price anatomy, nominal versus real value, supply and "
                "demand, cost types, markup versus margin, the Consumer "
                "Price Index, reading price tags, break-even analysis, the "
                "layers of profit, real historical series for gold (LBMA), "
                "oil (EIA/FRED), housing (Census/NAR), and equities (S&P "
                "500), inflation adjustment, depreciation methods, "
                "appreciation and CAGR, the comparables, cost, and income "
                "valuation approaches, price elasticity, profit margins by "
                "industry, unit economics, price-index construction, "
                "time-series tools, purchasing-power math, Fermi ballpark "
                "estimation, analogous estimation, market multiples, "
                "inventory valuation, price forecasting, profit "
                "attribution, hurdle rates, pricing psychology, and the "
                "complete time-stamped price record - organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a price is, nominal versus real, supply and demand, "
              "cost types, markup versus margin, the CPI, reading a price "
              "tag, break-even, gross operating and net profit) -> "
              "Compounded (gold prices across a century, oil prices since "
              "1970, American home prices 1975 to 2024, the S&P 500 as a "
              "price series, inflation adjustment, depreciation methods, "
              "appreciation and CAGR, the comparables approach, the cost "
              "approach, discounted cash flow, price elasticity, profit "
              "margins by industry, unit economics) -> Advanced (building "
              "a price index, time-series tools, a lifetime of purchasing "
              "power, Fermi ballpark estimation, analogous estimation, "
              "market multiples, inventory valuation, price forecasting, "
              "profit attribution, cost of capital and the hurdle rate, "
              "pricing psychology, the complete price record).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search price anatomy, CPI, inflation, gold, oil, housing, S&P 500, depreciation, CAGR, DCF, comparables, multiples, margins, break-even, elasticity, forecasting...",
        "chat_ph": "Ask about prices and profits...",
        "archive_blurb": ("Seeded %s price and profit tracking records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled price and profit studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about prices and profits - from what a price is through nominal versus real value, supply and demand, costs, markup and margin, the CPI, price tags, break-even, and the layers of profit, through gold, oil, housing, and equity price series, inflation adjustment, depreciation, CAGR, the three valuation approaches, elasticity, industry margins, and unit economics, to price indexes, time-series tools, ballpark estimation, multiples, inventory valuation, forecasting, attribution, hurdle rates, pricing psychology, and the complete price record." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "price-profit-study", "gen_demo_kind": "price-profit-demo",
        "source": source,
    }

CIT_PUB = ("Price and profit tracking (standard references: U.S. Bureau of "
           "Labor Statistics Consumer Price Index CPI-U; LBMA gold annual "
           "averages via National Mining Association; U.S. Energy "
           "Information Administration crude prices and FRED DCOILWTICO; "
           "U.S. Census Bureau new-home price medians; National Association "
           "of Realtors existing-home medians; S&P 500 historical closes; "
           "U.S. Department of Labor minimum-wage history; USPAP and IVS "
           "valuation approaches; U.S. GAAP ASC 330/360; Brealey Myers Allen "
           "corporate finance; Tversky and Kahneman anchoring 1974; "
           "Hyndman and Athanasopoulos forecasting).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Valuation Method - every price a covenant between "
                     "maker and buyer sealed in time, profit the honest "
                     "wage of value delivered - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["price-profit-tracking"] = _cfg(
    "price-profit-tracking", "The Price and Profit Tracking Database",
    "Know what things are worth across time: real, fact-checked price and "
    "profit records - price anatomy, time-series tracking of gold, oil, "
    "housing, and equities, inflation adjustment, depreciation and "
    "appreciation, the three valuation approaches, ballpark-estimation "
    "heuristics for new things, and profit margins by category - taught "
    "progressively along the ladder.",
    "price and profit record", "JAH-PFT-", "JAH Price and Profit Tracking Archivist",
    "price and profit tracking archivist - knowing what things are worth "
    "across time through price anatomy, real historical series, inflation "
    "adjustment, depreciation and appreciation, the three valuation "
    "approaches, ballpark estimation for new things, and profit margins by "
    "category; teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["price-profit-tracking-signature"] = _cfg(
    "price-profit-tracking-signature", "The Price and Profit Tracking Signature Database",
    "His original Signature Valuation Method: every price a covenant "
    "between maker and buyer sealed in time, profit the honest wage of "
    "value delivered, the price record the ledger line of that covenant. "
    "The full ladder from price anatomy through real series, valuation "
    "approaches, and ballpark heuristics to the complete price record, "
    "reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "price and profit record", "JAH-PFTS-", "JAH Price and Profit Tracking Archivist (Signature)",
    "price and profit tracking archivist - Signature editions: his original "
    "Signature Valuation Method, every price a covenant sealed in time and "
    "profit the honest wage of value delivered, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this "
    "system",
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
    for slug in ("price-profit-tracking", "price-profit-tracking-signature"):
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

    print("wrote %d records across %d databases; manifest/api/restamp left to the merger." % (total, len(built)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
