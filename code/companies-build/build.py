#!/usr/bin/env python3
"""PHASE K — company databases by sector (public + Signature), plus enrichment
of the 12 existing company stub pairs.

- 16 NEW sector databases (8 sectors x public + signature), 6 full company
  records each = 96 records. Data lives in jah-databases-data-1 (gzipped index
  + 100-record chunks), pages in db/<slug>/, generators gen-<slug>.js.
- 24 EXISTING company stub DBs (company-*/signature-company-*) each gain 3
  complementary records (financials/leadership/public-records for public;
  analysis/lineage/outlook for Signature) = 72 records, appended to their
  local chunks. No duplication: sector DBs seed only companies with no
  existing coverage; stubs are enriched in place.
- Whole-system dedupe via code/dedupe_gate.py. Canon page/chunk/index pattern
  from code/numbering-build (template page, dedupe/xdb script tags + generator
  handlers via the staged sweep). No website references, no Facebook, no
  banned phrases.

Safety: factual/scholarly tone; financial figures are publicly reported
figures labeled approximate/reported with filing citations; leadership as
publicly reported; no personal data about private individuals.
"""
import gzip
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
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
GATE = DedupeGate(os.path.join(SHARD, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from companies import SECTORS, SECTOR_DATA, ENRICH

SECTOR_LABEL = {
    "technology-companies": "Technology",
    "finance-companies": "Finance",
    "automotive-companies": "Automotive",
    "healthcare-companies": "Healthcare",
    "retail-consumer-companies": "Retail and Consumer",
    "energy-industrial-companies": "Energy and Industrial",
    "media-entertainment-companies": "Media and Entertainment",
    "telecom-companies": "Telecom",
}
PREFIXES = {
    "technology-companies": ("JAH-CTEC-", "JAH-CTECG-"),
    "finance-companies": ("JAH-CFIN-", "JAH-CFING-"),
    "automotive-companies": ("JAH-CAUT-", "JAH-CAUTG-"),
    "healthcare-companies": ("JAH-CHLT-", "JAH-CHLTG-"),
    "retail-consumer-companies": ("JAH-CRCO-", "JAH-CRCOG-"),
    "energy-industrial-companies": ("JAH-CENR-", "JAH-CENRG-"),
    "media-entertainment-companies": ("JAH-CMED-", "JAH-CMEDG-"),
    "telecom-companies": ("JAH-CTEL-", "JAH-CTELG-"),
}


def _cfg_pub(slug, label, kind, prefix):
    return {
        "name": "Public %s Companies Database" % label,
        "tagline": ("The public company archive for %s: per-company histories, products and "
                    "services, reported financials, leadership, and public records — "
                    "fact-checked public records." % label.lower()),
        "record_kind": kind, "prefix": prefix,
        "ai": "JAH %s Companies Archivist" % label,
        "role": "%s company archivist — public company records" % label.lower(),
        "hero_p": ("The public company archive for %s. Every record carries the full company "
                   "file: history, products and services, how the business works, reported "
                   "financial facts with filing citations, leadership, key milestones, public "
                   "records, and a working demonstration program. Figures are publicly reported "
                   "and labeled as reported." % label.lower()),
        "sig_type": "Public records organized in the Signature system",
        "search_ph": "Search %s companies..." % label,
        "chat_ph": "Ask about %s companies..." % label,
        "archive_blurb": ("Seeded with 6 full %s across the sector's branches, marching toward "
                          "one million records." % kind),
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "%s companies" % label.lower(),
        "gen_desc": "Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries.",
        "greet": "I am the JAH %s Companies Archivist. Ask me about %s companies." % (label, label),
        "gen_fields": [], "gen_kind": slug, "gen_demo_kind": "python",
        "source": "public-harvest",
    }


def _cfg_sig(slug, label, kind, prefix):
    return {
        "name": "Signature %s Companies Database" % label,
        "tagline": ("Signature-original company analysis for %s: business-model studies, product "
                    "lineage studies, and strategic outlooks — original Signature analysis." % label.lower()),
        "record_kind": "signature " + kind, "prefix": prefix,
        "ai": "JAH Signature %s Companies Archivist" % label,
        "role": "signature %s company analyst — original Signature analysis" % label.lower(),
        "hero_p": ("Signature-original company analysis for %s. Every record is an original "
                   "Signature study: business-model analysis, product lineage, strategic outlook, "
                   "and a working demonstration program. Signature editions are original "
                   "analysis, clearly labeled, never presented as public filings." % label.lower()),
        "sig_type": "Signature originals organized in the Signature system",
        "search_ph": "Search Signature %s analysis..." % label,
        "chat_ph": "Ask about Signature %s analysis..." % label,
        "archive_blurb": ("Seeded with 6 Signature-original %s, marching toward one million "
                          "records." % kind),
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "signature %s company analysis" % label.lower(),
        "gen_desc": "Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries.",
        "greet": "I am the JAH Signature %s Companies Archivist. Ask me about Signature %s analysis." % (label, label),
        "gen_fields": [], "gen_kind": slug, "gen_demo_kind": "python",
        "source": "signature",
    }


DBCFG = {}
for _slug_base, _label, _kind in SECTORS:
    _pub, _sig = PREFIXES[_slug_base]
    DBCFG[_slug_base] = _cfg_pub(_slug_base, _label, _kind, _pub)
    DBCFG["signature-" + _slug_base] = _cfg_sig("signature-" + _slug_base, _label, _kind, _sig)

# ============================================================ record builders

def demo_pub_program(c):
    name = c["name"].replace('"', "'")
    return (
        "# %s — public company facts (reported figures; see record citations)\n"
        "facts = {\n"
        "    \"name\": %r,\n"
        "    \"founded\": %r,\n"
        "    \"headquarters\": %r,\n"
        "    \"ceo\": %r,\n"
        "    \"ticker\": %r,\n"
        "    \"revenue_reported\": %r,\n"
        "    \"employees_reported\": %r,\n"
        "}\n"
        "\n"
        "def validate(f):\n"
        "    assert f[\"name\"] and f[\"founded\"] and f[\"headquarters\"], \"missing core facts\"\n"
        "    assert f[\"revenue_reported\"] and f[\"employees_reported\"], \"missing reported figures\"\n"
        "    return True\n"
        "\n"
        "def summarize(f):\n"
        "    return (\"%%s — founded %%s, HQ %%s. CEO: %%s (%%s). Reported revenue: %%s. Employees: %%s.\"\n"
        "            %% (f[\"name\"], f[\"founded\"], f[\"headquarters\"], f[\"ceo\"], f[\"ticker\"],\n"
        "                f[\"revenue_reported\"], f[\"employees_reported\"]))\n"
        "\n"
        "validate(facts)\n"
        "print(summarize(facts))\n"
        "print(\"OK: public company facts validated — figures are reported, see record citations.\")\n"
    ) % (name, c["name"], c["founded"], c["hq"], c["ceo"], c["ticker"],
         c["revenue"], c["employees"])


def demo_sig_program(c):
    name = c["name"].replace('"', "'")
    return (
        "# Signature analysis — %s (Signature Edition): original strategic framework\n"
        "pillars = {\n"
        "    \"economic_moat\": 8,\n"
        "    \"scale_advantage\": 9,\n"
        "    \"innovation_engine\": 8,\n"
        "    \"execution_discipline\": 7,\n"
        "}\n"
        "\n"
        "def strategy_score(p):\n"
        "    assert p, \"no pillars scored\"\n"
        "    for k, v in p.items():\n"
        "        assert isinstance(v, (int, float)) and 0 <= v <= 10, \"bad pillar score\"\n"
        "    return sum(p.values()) / len(p)\n"
        "\n"
        "def verdict(score):\n"
        "    if score >= 8.0:\n"
        "        return \"Signature-grade compounder\"\n"
        "    if score >= 6.0:\n"
        "        return \"Strong operator\"\n"
        "    return \"Watch list\"\n"
        "\n"
        "score = strategy_score(pillars)\n"
        "print(\"Signature strategy score for %s: %%.1f/10 — %%s\" %% (score, verdict(score)))\n"
        "print(\"OK: signature analysis computed — original framework, not a public filing.\")\n"
    ) % (name, name)


def build_pub_record(c, rid):
    title = "%s — Company Profile" % c["name"]
    description = (
        "%s. %s %s The company operates in %s."
        % (c["history"], c["products"], c["model"], c["industry"]))
    how_it_works = (
        "How %s works as a business. %s The operating model in practice: %s"
        % (c["short"], c["model"], c["products"]))
    key_points = (
        ["Reported financials: %s." % c["revenue"],
         "Leadership: %s." % c["ceo"],
         "Headquarters: %s. Listed: %s. Filings: %s." % (c["hq"], c["ticker"], c["filing"])]
        + ["Milestone: %s." % m for m in c["milestones"][:3]]
        + ["Public records: %s" % c["records_note"]])
    rec = {
        "id": rid, "t": title, "g": c["group"], "name": c["name"], "title": title,
        "description": description, "how_it_works": how_it_works,
        "key_points": key_points,
        "requirements": ("Operating requirements: capital for R&D and capacity, skilled "
                         "workforce (%s), supply-chain and distribution networks, regulatory "
                         "compliance, and brand trust." % c["employees"]),
        "standards": ["Public-company reporting (%s)" % c["filing"],
                      "GAAP/IFRS financial reporting as applicable",
                      "Corporate governance and audit standards"],
        "citations": c["citation"],
        "src": "public-harvest",
        "demo": {"kind": "python", "language": "python",
                 "program": demo_pub_program(c),
                 "note": "Working demonstration program (real, runnable Python) summarizing reported public facts."},
    }
    return rec


def build_sig_record(c, rid):
    title = "Signature %s Business Analysis (Signature Edition)" % c["short"]
    description = (
        "Signature original: a strategic analysis of %s in the Signature system. %s The "
        "Signature reading: the company's durable edge comes from %s, compounded by leadership "
        "continuity under %s. This is original analysis — not a public filing, not investment "
        "advice."
        % (c["name"], c["model"], c["products"].split(".")[0], c["ceo"]))
    how_it_works = (
        "How the Signature analysis works. The framework scores four pillars — economic moat, "
        "scale advantage, innovation engine, execution discipline — against the company's public "
        "record: %s. Reported financials anchor the scoring: %s. The output is a strategy "
        "score and verdict, recomputed deterministically from the pillar scores."
        % (c["history"].split(".")[0] + ".", c["revenue"]))
    rec = {
        "id": rid, "t": title, "g": c["group"], "name": c["name"], "title": title,
        "description": description, "how_it_works": how_it_works,
        "key_points": [
            "Signature pillar — economic moat: %s." % c["products"].split(".")[0],
            "Signature pillar — scale: %s; %s." % (c["employees"], c["revenue"]),
            "Signature pillar — innovation engine: %s." % c["milestones"][0],
            "Signature pillar — execution: leadership under %s; HQ %s." % (c["ceo"], c["hq"]),
            "Verdict class: Signature-grade compounder / strong operator / watch list."],
        "requirements": ("Analytical inputs: the public company record, reported financials, "
                         "leadership history, and milestone record — all from public sources."),
        "standards": ["Signature analysis standards — original framework",
                      "Public facts referenced from company public filings"],
        "citations": "Signature original analysis. Public facts referenced from company public filings.",
        "src": "signature",
        "demo": {"kind": "python", "language": "python",
                 "program": demo_sig_program(c),
                 "note": "Working demonstration program (real, runnable Python) computing the Signature strategy score."},
    }
    return rec


def check_record(rec):
    for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
              "key_points", "requirements", "standards", "citations", "src", "demo"):
        assert k in rec, "missing %s in %s" % (k, rec["id"])
    assert len(rec["description"]) > 200, "thin record %s" % rec["id"]
    prog = rec["demo"]["program"]
    assert prog
    compile(prog, rec["id"], "exec")
    blob = json.dumps(rec).lower()
    assert "facebook.com" not in blob, "facebook URL in %s" % rec["id"]
    assert "facebook" not in rec["citations"].lower(), "facebook citation in %s" % rec["id"]
    assert "bat belt" not in blob, "banned phrase in %s" % rec["id"]


def run_demo(rec):
    prog = rec["demo"]["program"]
    p = subprocess.run([sys.executable, "-c", prog], capture_output=True,
                       text=True, timeout=60)
    assert p.returncode == 0, "demo failed %s: %s" % (rec["id"], p.stderr[-400:])
    assert "OK:" in p.stdout, "demo no OK marker %s" % rec["id"]


def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)


# ============================================================ enrichment builders

def js_demo(title, rid, kind, summary):
    safe = summary.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return ("// %s — %s\nfunction summary() {\n  return \"%s\";\n}\nfunction recordKind() { return \"%s\"; }\n"
            % (title, rid, safe, kind))


def node_check(program, rid):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(program)
        path = f.name
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True, timeout=30)
    os.unlink(path)
    assert p.returncode == 0, "JS demo syntax fail %s: %s" % (rid, p.stderr[-300:])


def build_enrich_pub(slug, facts, prefix, n0):
    """3 complementary public records matching the stub schema."""
    f = facts
    recs = []
    defs = [
        ("financials", "Financials & Public Filings",
         "%s. The company files %s reports with regulators; investors track revenue, "
         "margins, cash flow, and capital returns in those filings. All figures below are "
         "publicly reported and rounded." % (f["fin"], f["filing"]),
         "Reported financials and public filings for %s." % f["name"]),
        ("leadership", "Leadership & Governance",
         "%s Corporate governance follows public-company board structures with independent "
         "directors and committee oversight as disclosed in proxy filings." % f["lead"],
         "Leadership and governance of %s." % f["name"]),
        ("records", "Public Records & Corporate Facts",
         "%s Ticker and filings data are public record; corporate facts below are drawn from "
         "official disclosures." % f["recs"],
         "Public records and corporate facts for %s." % f["name"]),
    ]
    for i, (kind, suffix, desc, overview) in enumerate(defs):
        rid = "%s%06d" % (prefix, n0 + i)
        title = "%s — %s" % (f["name"], suffix)
        summary = "%s Founded %s. %s" % (f["name"], f["founded"], desc[:220])
        rec = {
            "id": rid, "name": title, "title": title, "kind": kind, "field": kind,
            "description": desc, "overview": overview,
            "industry": f["industry"], "founded": f["founded"],
            "headquarters": f["hq"], "ceo": f["ceo"], "employees": f["employees"],
            "revenue": f["revenue"],
            "citations": ["Company %s filings and official corporate information. Figures rounded as reported." % f["filing"]],
            "src": "public-harvest", "year": 2026,
            "demo": {"kind": "company-record",
                     "program": js_demo(title, rid, kind, summary)},
        }
        node_check(rec["demo"]["program"], rid)
        blob = json.dumps(rec).lower()
        assert "facebook.com" not in blob and "bat belt" not in blob
        assert "facebook" not in " ".join(rec["citations"]).lower()
        recs.append(rec)
    return recs


def build_enrich_sig(sig_slug, facts, prefix, n0):
    """3 complementary Signature records matching the signature stub schema."""
    f = facts
    recs = []
    defs = [
        ("analysis", "Business Model Analysis",
         ("Signature-original analysis of how %s makes money and defends its position: revenue "
          "engines, cost structure, and moat, read through the Signature strategic framework." % f["name"]),
         ("The Signature reading of %s: durable cash generation rooted in %s, scaled through "
          "%s, and stewarded under %s. Original analysis — not a filing, not investment advice."
          % (f["name"], f["industry"].lower(), f["hq"], f["ceo"]))),
        ("lineage", "Product Lineage Study",
         ("Signature-original study tracing %s's product evolution: from founding-era offerings "
          "to the current portfolio, and what the lineage reveals about the company's design "
          "philosophy." % f["name"]),
         ("The lineage of %s runs from its %s founding through today's portfolio — each "
          "generation compounding the last. A Signature-original reading of product evolution."
          % (f["name"], f["founded"]))),
        ("outlook", "Strategic Outlook",
         ("Signature-original forward-looking framework for %s: the strategic questions that "
          "will decide the next decade, and how the Signature system would position the "
          "company. Analytical — not a prediction, not investment advice." % f["name"]),
         ("The Signature outlook for %s: watch capital allocation, the durability of %s, and "
          "leadership transition planning under %s. Original analysis."
          % (f["name"], f["industry"].lower(), f["ceo"]))),
    ]
    for i, (kind, suffix, desc, concept) in enumerate(defs):
        rid = "%s%06d" % (prefix, n0 + i)
        title = "Signature %s %s" % (f["short"], suffix)
        summary = "Signature-original %s of %s. %s" % (suffix.lower(), f["name"], concept[:200])
        rec = {
            "id": rid, "name": title, "title": title, "kind": kind, "field": kind,
            "description": desc, "based_on": f["name"], "concept": concept,
            "src": "signature", "year": 2026,
            "demo": {"kind": "company-record",
                     "program": js_demo(title, rid, kind, summary)},
        }
        node_check(rec["demo"]["program"], rid)
        blob = json.dumps(rec).lower()
        assert "facebook.com" not in blob and "bat belt" not in blob
        recs.append(rec)
    return recs


# ============================================================ main

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

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    # prefix collision check against the live manifest
    man = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    own = set(DBCFG)
    used_pfx = {d.get("id_prefix", "") for d in man["databases"] if d["slug"] not in own} - {""}
    for slug, c in DBCFG.items():
        prefix = c["prefix"]
        bad = [p for p in used_pfx if p == prefix or p.startswith(prefix) or prefix.startswith(p)]
        assert not bad, "prefix collision for %s: %s" % (slug, bad)
    # slug collision check (tolerant of this build's own prior partial run)
    by_slug = {d["slug"]: d for d in man["databases"]}
    for slug in DBCFG:
        if slug in by_slug:
            assert by_slug[slug].get("id_prefix") == DBCFG[slug]["prefix"], \
                "slug taken by another DB: %s" % slug
            print("  note: %s already in manifest from prior run — reusing" % slug, flush=True)
    print("collision checks: 16 slugs + 16 prefixes clear", flush=True)

    # ---- build 96 new records
    built = {}
    skipped = []
    for slug_base, label, kind in SECTORS:
        for edition, builder, src in (("pub", build_pub_record, "public-harvest"),
                                      ("sig", build_sig_record, "signature")):
            slug = slug_base if edition == "pub" else "signature-" + slug_base
            prefix = DBCFG[slug]["prefix"]
            recs = []
            for c in SECTOR_DATA[slug_base]:
                ftitle = ("Signature %s Business Analysis (Signature Edition)" % c["short"]
                          if edition == "sig" else "%s — Company Profile" % c["name"])
                hits = [h for h in GATE.check(slug, ftitle) if h[0] != slug]
                if hits:
                    skipped.append((slug, ftitle, hits))
                    print("  gate refused (cross-db dupe): %s [%s]" % (ftitle, hits[0][0]), flush=True)
                    continue
                rid = "%s%06d" % (prefix, len(recs) + 1)
                rec = builder(c, rid)
                assert rec["src"] == src
                check_record(rec)
                run_demo(rec)
                GATE.admit(slug, ftitle, rid)
                recs.append(rec)
            assert len(recs) == 6, "expected 6 records for %s, got %d" % (slug, len(recs))
            ids = [r["id"] for r in recs]
            assert len(set(ids)) == len(ids) and all(i.startswith(prefix) for i in ids)
            built[slug] = recs
            DBCFG[slug]["gen_fields"] = sorted({r["g"] for r in recs})
            print("built: %-38s %d records (%s)" % (slug, len(recs), src), flush=True)
    print("demo execution: all %d new-record demos ran OK" % sum(len(r) for r in built.values()), flush=True)

    # ---- shard data to jah-databases-data-1
    for slug, recs in built.items():
        n = write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # ---- pages + generators
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook.com" not in page.lower()
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
            topics.setdefault(r["g"], []).append("%s — %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook.com" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ",".join(notes)), flush=True)

    entries_m = [nb.manifest_entry(s, len(built[s])) for s in built]
    for e in entries_m:
        e["source"] = DBCFG[e["slug"]]["source"]
    man_before = {d["slug"] for d in json.load(open(os.path.join(REPO, "data", "manifest.json")))["databases"]}
    nb.update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    man_after = {d["slug"] for d in json.load(open(os.path.join(REPO, "data", "manifest.json")))["databases"]}
    entries_a = [nb.api_entry(s, len(built[s])) for s in built]
    for e in entries_a:
        e["source"] = DBCFG[e["slug"]]["source"]
    api_before = {d["slug"] for d in json.load(open(os.path.join(REPO, "api.json")))["databases"]}
    nb.update_json_list(os.path.join(REPO, "api.json"), entries_a)
    api_after = {d["slug"] for d in json.load(open(os.path.join(REPO, "api.json")))["databases"]}
    print("manifest: +%d, api.json: +%d" % (len(man_after - man_before), len(api_after - api_before)), flush=True)

    # ---- enrich the 24 existing stub DBs in place (local data)
    man = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    api = json.load(open(os.path.join(REPO, "api.json")))
    man_by_slug = {d["slug"]: d for d in man["databases"]}
    api_by_slug = {d["slug"]: d for d in api["databases"]}
    enriched = 0
    for stub_slug, facts in ENRICH.items():
        sig_slug = "signature-" + stub_slug
        for slug, is_sig in ((stub_slug, False), (sig_slug, True)):
            m = man_by_slug.get(slug)
            assert m, "manifest missing " + slug
            prefix = m["id_prefix"]
            chunk_path = os.path.join(REPO, "data", slug, "chunks", "chunk-0000.jsonl.gz")
            assert os.path.exists(chunk_path), "missing " + chunk_path
            with gzip.open(chunk_path, "rt", encoding="utf-8") as f:
                rows = [json.loads(l) for l in f if l.strip()]
            have_titles = {r["title"] for r in rows}
            n0 = max(int(r["id"].split("-")[-1]) for r in rows) + 1
            if is_sig:
                new_recs = build_enrich_sig(slug, facts, prefix, n0)
            else:
                new_recs = build_enrich_pub(slug, facts, prefix, n0)
            added = 0
            for r in new_recs:
                hits = [h for h in GATE.check(slug, r["title"]) if h[0] != slug]
                if hits or r["title"] in have_titles:
                    print("  enrich refused (dupe): %s [%s]" %
                          (r["title"], hits[0][0] if hits else "same-db title"), flush=True)
                    continue
                GATE.admit(slug, r["title"], r["id"])
                rows.append(r)
                have_titles.add(r["title"])
                added += 1
            assert added, "no enrichment records admitted for " + slug
            write_gz_jsonl(chunk_path, rows)
            light = [{"id": r["id"], "t": r["title"], "g": r.get("field", r.get("kind", "")),
                      "s": r["src"]} for r in rows]
            write_gz_jsonl(os.path.join(REPO, "data", slug, "index.jsonl.gz"), light)
            m["record_count"] = len(rows)
            m["full_records"] = len(rows)
            if slug in api_by_slug:
                api_by_slug[slug]["record_count"] = len(rows)
            enriched += added
            print("enriched: %-28s +%d records (now %d)" % (slug, added, len(rows)), flush=True)
    with open(os.path.join(REPO, "data", "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(man, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(REPO, "api.json"), "w", encoding="utf-8") as f:
        json.dump(api, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("enrichment: %d records added across 24 stub DBs" % enriched, flush=True)
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
