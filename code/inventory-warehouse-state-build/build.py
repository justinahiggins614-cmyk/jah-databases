#!/usr/bin/env python3
"""Build the Inventory and Warehouse State databases for JAH Databases
(missing-115 Wave 1, operational data - Manon's #1 priority).

Item 53 of the 115-category missing-database audit: supply, inventory, and
warehouse state - actual stock, reservations, lead times, movement, expiry,
and replenishment. Verified 2026-10-17 against the full manifest (2,390
databases) plus every shard index title in jah-databases-data-1 (792 index
files): zero 'inventory-warehouse*' slugs/names; zero title collisions on
the 68 planned titles (dedupe_gate whole-system check: 68 checked, 0
refusals). Keyword near-hits 'invisibility' (JAH-INVIS), 'inventors'
(JAH-INVENT), 'investing' (JAH-INVEST) are unrelated domains. The paste's
rule was applied by name/purpose/record schema/capabilities: a dedicated
inventory-and-warehouse-state database - SKU/location data models, stock
states, cycle counting, FIFO/LIFO/FEFO, ABC analysis, reorder-point math,
safety stock, warehouse layout and slotting, goods-receipt/putaway/pick/
pack records - is a distinct capability. BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  inventory-warehouse-state            - The Inventory and Warehouse State
                                       Database (public-harvest: real,
                                       fact-checked inventory theory and
                                       warehouse management - SKU and
                                       location data models, stock states,
                                       units of measure, FIFO/LIFO/FEFO,
                                       lead time, goods receipt and
                                       putaway, pick-pack-ship, lot and
                                       expiry tracking, cycle counting, ABC
                                       analysis, reorder-point math, EOQ,
                                       safety stock, reservations and
                                       allocation, putaway strategies,
                                       picking strategies, packing records,
                                       movement records, warehouse layout
                                       and slotting, multi-echelon
                                       inventory, MRP, accuracy, perpetual
                                       vs periodic systems, dynamic safety
                                       stock, replenishment systems,
                                       returns and RMAs, serialization,
                                       physical inventory, analytics, and
                                       the inventory health program;
                                       standard references Harris 1913 EOQ;
                                       Wilson 1934 reorder-point methods;
                                       Silver, Pyke, Peterson Inventory
                                       Management; Nahmias Production and
                                       Operations Analysis; Tompkins et al.
                                       Facilities Planning; Bartholdi and
                                       Hackman Warehouse & Distribution
                                       Science; Chopra and Meindl Supply
                                       Chain Management; APICS Dictionary;
                                       IAS 2 Inventories; ASC 330; GS1
                                       General Specifications; Ohno Toyota
                                       Production System; Womack and Jones
                                       Lean Thinking; OSHA 29 CFR 1910.176)
  inventory-warehouse-state-signature  - The Inventory and Warehouse State
                                       Signature Database (his original
                                       Signature Stock Method: every SKU a
                                       stamped note of state, every
                                       location a fixed address in the
                                       system, every movement a witnessed
                                       passage, stock states the truth of
                                       the shelf, safety stock the honor
                                       margin, replenishment the heartbeat;
                                       src signature, titles suffixed
                                       " (Signature Edition)", never
                                       presented as authentic public
                                       record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-INV- (public) and JAH-INVS- (signature), verified free in
the manifest id_prefix values (2,390 databases) and in all 792 shard index
files (zero exact hits; near-hits JAH-INVENT/Inventors, JAH-INVIS/
Invisibility, JAH-INVEST/Investing are unrelated domains).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_inventory_warehouse_state.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. The merger owns those. Only new untracked paths are created.

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
from entries_inventory_warehouse_state import ENTRIES, SIG_TAIL
from demos_inventory_warehouse_state import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Stock Method: "
                "every SKU a stamped note of state, every location a fixed "
                "address in the system, every movement a witnessed passage, "
                "stock states the truth of the shelf, safety stock the honor "
                "margin, and replenishment the heartbeat of the store. "
                "Clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked inventory theory and "
                "warehouse management: SKU and location data models, stock "
                "states, units of measure, FIFO LIFO and FEFO, lead time, "
                "goods receipt and putaway, pick-pack-ship, lot and expiry "
                "tracking, cycle counting, ABC analysis, reorder-point math, "
                "EOQ, safety stock, reservations and allocation, putaway "
                "strategies, picking strategies, packing records, movement "
                "records, warehouse layout and slotting, multi-echelon "
                "inventory, MRP, accuracy, perpetual and periodic systems, "
                "dynamic safety stock, replenishment systems, returns and "
                "RMAs, serialization, physical inventory, analytics, and "
                "the inventory health program - organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what inventory is, the SKU atom, stock states, location "
              "addresses, units of measure, FIFO and LIFO basics, lead "
              "time, goods receipt, pick-pack-ship, lots and expiry) -> "
              "Compounded (cycle counting, ABC analysis, reorder-point "
              "math, EOQ, safety stock, FEFO, reservations and allocation, "
              "putaway strategies, picking strategies, packing records, "
              "movement records, warehouse layout and slotting) -> "
              "Advanced (multi-echelon inventory, MRP, inventory accuracy, "
              "perpetual vs periodic systems, advanced slotting, dynamic "
              "safety stock, replenishment systems, returns and RMAs, "
              "serialization, the full physical inventory, inventory "
              "analytics, the inventory health program).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search SKU, stock states, locations, units of measure, FIFO, LIFO, FEFO, lead time, receiving, putaway, picking, cycle counting, ABC analysis, reorder point, EOQ, safety stock, kanban, MRP, slotting, serials, inventory turns...",
        "chat_ph": "Ask about inventory and warehouse state...",
        "archive_blurb": ("Seeded %s inventory and warehouse state records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled inventory and warehouse studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about inventory and warehouse state - from what inventory is through the SKU, stock states, locations, units of measure, FIFO and LIFO, lead time, receiving, pick-pack-ship, and lots and expiry, through cycle counting, ABC analysis, reorder points, EOQ, safety stock, FEFO, reservations, putaway, picking, packing, movement records, and layout and slotting, to multi-echelon inventory, MRP, accuracy, perpetual and periodic systems, advanced slotting, dynamic safety stock, replenishment, returns, serialization, the physical inventory, analytics, and the health program." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "inventory-warehouse-study", "gen_demo_kind": "inventory-warehouse-demo",
        "source": source,
    }

CIT_PUB = ("Inventory theory and warehouse management (standard references: "
           "Harris FW. How Many Parts to Make at Once. Factory; 1913 (EOQ); "
           "Wilson RH. A Scientific Routine for Stock Control. Harvard "
           "Business Review; 1934; Silver EA, Pyke DF, Peterson R. Inventory "
           "Management and Production Planning and Scheduling. 3rd ed. Wiley; "
           "1998; Nahmias S. Production and Operations Analysis. 7th ed. "
           "Waveland Press; 2015; Tompkins JA et al. Facilities Planning. "
           "4th ed. Wiley; 2010; Bartholdi JJ, Hackman ST. Warehouse & "
           "Distribution Science. Supply Chain and Logistics Institute; "
           "2019; Chopra S, Meindl P. Supply Chain Management. 7th ed. "
           "Pearson; 2018; APICS Dictionary. ASCM; 17th ed.; IAS 2 "
           "Inventories; ASC 330 Inventory; GS1 General Specifications; "
           "Ohno T. Toyota Production System. Productivity Press; 1988; "
           "Womack JP, Jones DT. Lean Thinking. 2nd ed. Free Press; 2003; "
           "OSHA 29 CFR 1910.176).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Stock "
                     "Method - every SKU a stamped note of state, every "
                     "location a fixed address, every movement a witnessed "
                     "passage - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["inventory-warehouse-state"] = _cfg(
    "inventory-warehouse-state", "The Inventory and Warehouse State Database",
    "Track actual stock, reservations, lead times, movement, expiry, and "
    "replenishment: real, fact-checked inventory theory and warehouse "
    "management, from SKU and location data models through cycle counting, "
    "FIFO, LIFO, FEFO, ABC analysis, reorder-point math, and safety stock, "
    "to slotting, MRP, and the inventory health program, taught "
    "progressively along the ladder.",
    "inventory and warehouse record", "JAH-INV-", "JAH Inventory and Warehouse State Archivist",
    "inventory and warehouse state archivist - tracking actual stock, "
    "reservations, lead times, movement, expiry, and replenishment across "
    "SKU and location data models, counting methods, issuing rules, "
    "reorder math, warehouse operations, and inventory health; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive data "
    "from this system",
    CIT_PUB, "public")
DBCFG["inventory-warehouse-state-signature"] = _cfg(
    "inventory-warehouse-state-signature", "The Inventory and Warehouse State Signature Database",
    "His original Signature Stock Method: every SKU a stamped note of "
    "state, every location a fixed address in the system, every movement "
    "a witnessed passage, stock states the truth of the shelf, safety "
    "stock the honor margin, replenishment the heartbeat. The full ladder "
    "from what inventory is through the SKU, stock states, locations, and "
    "issuing rules, through counting, reorder math, and warehouse "
    "operations, to multi-echelon planning, MRP, and the health program, "
    "reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "inventory and warehouse record", "JAH-INVS-", "JAH Inventory and Warehouse State Archivist (Signature)",
    "inventory and warehouse state archivist - Signature editions: his "
    "original Signature Stock Method, every SKU a stamped note of state "
    "and every movement a witnessed passage, clearly labeled "
    "Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only "
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
    for slug in ("inventory-warehouse-state", "inventory-warehouse-state-signature"):
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

    # CONCURRENCY: manifest.json and api.json are merger-owned. Do NOT touch.
    print("manifest + api.json: SKIPPED (merger handles)", flush=True)
    print("DONE: %d databases, %d records; merger verifies and stamps counts." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
