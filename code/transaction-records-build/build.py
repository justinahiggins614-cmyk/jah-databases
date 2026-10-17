#!/usr/bin/env python3
"""Build the Transaction Records databases for JAH Databases
(missing-115 #46, Wave 1 - operational data).

Item 46 scope: orders, purchases, payments, returns, transfers, and
reconciliations - the anatomy of a transaction record, lifecycle states
(pending/settled/reversed), double-entry reconciliation, idempotency keys,
chargebacks/refunds, audit trails. Public records cite real standards
(ISO 20022, NACHA, SWIFT MT/MX message types, PCI DSS as public-standards
context).

Two databases, 34 ladder-ordered records each:

  transaction-records            - The Transaction Records Database
                                   (public-harvest: real, fact-checked
                                   operational transaction data; standard
                                   references ISO 20022-1:2021; NACHA
                                   Operating Rules & Guidelines; SWIFT MT
                                   (MT103/MT202/MT940/950) and MX
                                   migration; PCI DSS v4.0 March 2022;
                                   ISO 8583-1:2021; ISO 4217:2015; Federal
                                   Reserve FedNow; The Clearing House RTP;
                                   RFC 9110 idempotency; standard
                                   financial accounting texts)
  transaction-records-signature  - The Transaction Records Signature Database
                                   (his original Signature Transaction
                                   Method: every transaction a sealed
                                   covenant between parties, the ledger the
                                   book of covenants, reconciliation the
                                   truth-telling, the idempotency seal that
                                   cannot be double-stamped, and the audit
                                   trail the unbroken chain of witness;
                                   src signature, titles suffixed
                                   " (Signature Edition)", never presented
                                   as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
non-decreasing; foundations -> compounded -> advanced); the shard index is
written in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-TRX- (public) and JAH-TRXS- (signature), verified free
2026-10-17: zero hits in all 2,390 manifest id_prefix values and zero hits
in all 789 shard index.jsonl.gz files in jah-databases-data-1.

Dedupe: all 68 titles checked against the WHOLE system via DedupeGate
before authoring - zero refusals.

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_transaction_records.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; this build machine-executes all 68 demos.

This build writes ONLY new untracked paths: db/transaction-records[/-signature]/
pages, code/ build files, shard data dirs, and the merger fragment.
It NEVER touches data/manifest.json, api.json, index.html, README.md, or
docs/AI_ACCESS.md, and NEVER git commits or pushes - the merger handles
those.

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
from entries_transaction_records import ENTRIES, SIG_TAIL
from demos_transaction_records import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Transaction "
                "Method: every transaction a sealed covenant between "
                "parties, the ledger the book of covenants, reconciliation "
                "the truth-telling, the idempotency seal that cannot be "
                "double-stamped, and the audit trail the unbroken chain of "
                "witness. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("Public records - real, fact-checked operational "
                "transaction data: orders, purchases, payments, returns, "
                "transfers, and reconciliations; the anatomy of a "
                "transaction record, lifecycle states "
                "(pending/settled/reversed), double-entry reconciliation, "
                "idempotency keys, chargebacks and refunds, and audit "
                "trails - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a transaction record is, the anatomy of a record, "
              "lifecycle states, transaction types, double-entry basics, "
              "reading a receipt, minor units and rounding, timestamps and "
              "value dates, parties, identifiers) -> Compounded (order "
              "records, authorization and capture, payment methods "
              "compared, idempotency keys, refunds, returns, chargebacks, "
              "bank transfers, the card transaction flow, reconciliation, "
              "clearing and settlement, fees) -> Advanced (double-entry at "
              "scale, ISO 20022, SWIFT MT and MX, NACHA record layout, PCI "
              "DSS, fraud signals, audit trails, multi-currency and FX, "
              "append-only ledger design, reversals, real-time payments, "
              "the full lifecycle end to end).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search orders, payments, refunds, chargebacks, reconciliation, idempotency, ISO 20022, NACHA, SWIFT, PCI DSS, ledgers, audit trails...",
        "chat_ph": "Ask about transaction records...",
        "archive_blurb": ("Seeded %s transaction records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled transaction record studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about transaction records - from what a record is through anatomy, lifecycle states, types, double-entry, receipts, minor units, timestamps, parties, and identifiers, through orders, authorization and capture, payment methods, idempotency, refunds, returns, chargebacks, bank transfers, card flow, reconciliation, settlement, and fees, to double-entry at scale, ISO 20022, SWIFT, NACHA, PCI DSS, fraud signals, audit trails, FX, ledger design, reversals, and real-time payments." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "transaction-record-study", "gen_demo_kind": "transaction-record-demo",
        "source": source,
    }

CIT_PUB = ("Transaction records (standard references: ISO 20022-1:2021 "
           "financial services message scheme - pain.001, pacs.008, "
           "pacs.002, camt.053; NACHA Operating Rules & Guidelines - file "
           "header type 1, batch header type 5, entry detail type 6, "
           "addenda type 7, batch control type 8, file control type 9, "
           "return reason codes; SWIFT MT standards - MT103 customer "
           "credit transfer, MT202 financial institution transfer, "
           "MT940/950 statements, and the MX migration to pacs.008/009 "
           "and camt.053; PCI Security Standards Council PCI DSS v4.0, "
           "March 2022; ISO 8583-1:2021 card-originated messages; ISO "
           "4217:2015 currency codes and minor units; Federal Reserve "
           "FedNow Service operating procedures, launched July 2023; The "
           "Clearing House Real-Time Payments rules, operating since "
           "2017; RFC 9110 HTTP Semantics idempotency; standard "
           "financial accounting texts for double-entry bookkeeping).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "Transaction Method - every transaction a sealed "
                     "covenant between parties, the ledger the book of "
                     "covenants - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["transaction-records"] = _cfg(
    "transaction-records", "The Transaction Records Database",
    "Orders, purchases, payments, returns, transfers, and "
    "reconciliations: real, fact-checked operational transaction data - "
    "the anatomy of a transaction record, lifecycle states "
    "(pending/settled/reversed), double-entry reconciliation, idempotency "
    "keys, chargebacks and refunds, and audit trails - taught "
    "progressively along the ladder.",
    "transaction record", "JAH-TRX-", "JAH Transaction Records Archivist",
    "transaction records archivist - orders, purchases, payments, returns, "
    "transfers, and reconciliations; the anatomy of a transaction record, "
    "lifecycle states, double-entry reconciliation, idempotency keys, "
    "chargebacks and refunds, audit trails; teaching progressively along "
    "the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["transaction-records-signature"] = _cfg(
    "transaction-records-signature", "The Transaction Records Signature Database",
    "His original Signature Transaction Method: every transaction a "
    "sealed covenant between parties, the ledger the book of covenants, "
    "reconciliation the truth-telling, the idempotency seal that cannot "
    "be double-stamped, and the audit trail the unbroken chain of "
    "witness. The full ladder from what a record is through anatomy, "
    "lifecycle, types, double-entry, receipts, minor units, timestamps, "
    "parties, and identifiers, through orders, auth and capture, payment "
    "methods, idempotency, refunds, returns, chargebacks, transfers, "
    "card flow, reconciliation, settlement, and fees, to double-entry at "
    "scale, ISO 20022, SWIFT, NACHA, PCI DSS, fraud signals, audit "
    "trails, FX, ledger design, reversals, and real-time payments, "
    "reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "transaction record", "JAH-TRXS-", "JAH Transaction Records Archivist (Signature)",
    "transaction records archivist - Signature editions: his original "
    "Signature Transaction Method, every transaction a sealed covenant "
    "between parties and the ledger the book of covenants, clearly "
    "labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations "
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
    for slug in ("transaction-records", "transaction-records-signature"):
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

    # NOTE: manifest.json / api.json updates are the merger's job - this
    # build deliberately does not touch them.
    print("manifest + api.json: SKIPPED (merger appends %d databases, %d records)" % (len(built), total))
    print("DONE: %d databases, %d records. Merger: restamp, commit, push." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
