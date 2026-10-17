#!/usr/bin/env python3
"""Build the JAH Signature Cloud databases for JAH Databases
(2026-10-17 15:32 EDT, order #15).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,390 databases)
PLUS every shard index title in jah-databases-data-1 (zero 'JAH-CLD'
substring hits): zero 'jah-signature-cloud*' slugs/names; zero title
collisions for all 68 titles via code/dedupe_gate.py (0 refusals).
The order names this exact database, so BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  jah-signature-cloud            - The JAH Signature Cloud Database
                                   (public-harvest: real, fact-checked cloud
                                   computing technology - service models
                                   IaaS/PaaS/SaaS, deployment models,
                                   virtualization, storage, networking,
                                   scaling; standard references NIST SP
                                   800-145 (Mell and Grance, 2011);
                                   ISO/IEC 17788:2014; ISO/IEC 17789:2014;
                                   the CNCF cloud native definition; the
                                   Twelve-Factor App (Wiggins, 2011); Google
                                   Site Reliability Engineering (2016); the
                                   AWS Well-Architected Framework;
                                   Kubernetes documentation; and the other
                                   landmarks cited per record)
  jah-signature-cloud-signature  - The JAH Signature Cloud Signature Database
                                   (his original Signature Cloud Method: the
                                   cloud reframed as his Signature system -
                                   every workload a stamped Signature vessel,
                                   the control plane the Signature authority,
                                   regions the armory halls, scaling the
                                   summoned strength; src signature, titles
                                   suffixed " (Signature Edition)", never
                                   presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CLD- (public) and JAH-CLDS- (signature), verified free
in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_jah_signature_cloud.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
It writes only: db/jah-signature-cloud{,-signature}/ (index.html +
gen-*.js), the shard data under jah-databases-data-1, and the merger
fragment at ~/workspace/hidden_files/missing-builds/fragments/.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing on neutralizing or defeating military or
defense-grade systems.
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
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/jah-signature-cloud.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_jah_signature_cloud import ENTRIES, SIG_TAIL
from demos_jah_signature_cloud import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Cloud Method: "
                "the cloud reframed as his Signature system - every workload "
                "a stamped Signature vessel, the control plane the Signature "
                "authority, regions the armory halls, scaling the summoned "
                "strength. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("Public records - real, fact-checked cloud computing "
                "technology: service models (IaaS, PaaS, SaaS), deployment "
                "models (public, private, hybrid, community), "
                "virtualization and hypervisors, regions and availability "
                "zones, virtual networking, object block and file storage, "
                "identity and access management, pricing and measured "
                "service, containers and Kubernetes, serverless, managed "
                "databases, load balancing and auto scaling, CDNs, cloud "
                "security, observability, infrastructure as code, messaging, "
                "disaster recovery, CI/CD, FinOps, cloud-native design, "
                "multi-region architecture, migration, service mesh, "
                "confidential computing, and the Well-Architected "
                "Framework - every record carrying description, how it "
                "works, key points, requirements, standards, citations, and "
                "a working demonstration program, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what cloud computing is, the five essential "
              "characteristics, service models, deployment models, the "
              "shared responsibility model, virtualization and hypervisors, "
              "regions availability zones and edge, virtual networking, "
              "cloud storage types, identity and access management, "
              "pay-as-you-go pricing, cloud APIs and the control plane) -> "
              "Compounded (virtual machines and instance families, "
              "containers, Kubernetes, serverless, object storage, block "
              "and file storage, managed databases, load balancing and auto "
              "scaling, CDNs and edge caching, cloud network security, "
              "observability, infrastructure as code, message queues and "
              "events, backup and disaster recovery) -> Advanced (CI/CD "
              "pipelines, cost optimization and FinOps, the twelve-factor "
              "app, multi-region architecture and CAP, cloud migration, "
              "service mesh, confidential computing, the Well-Architected "
              "Framework and SRE).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search IaaS, PaaS, SaaS, virtualization, VPCs, subnets, IAM, regions, availability zones, Kubernetes, serverless, object storage, load balancing, auto scaling, CDN, FinOps, twelve-factor, CAP theorem, service mesh...",
        "chat_ph": "Ask about cloud computing...",
        "archive_blurb": ("Seeded %s cloud computing records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled cloud computing studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about cloud computing - from what the cloud is through the five characteristics, service models, deployment models, shared responsibility, virtualization, regions, networking, storage, identity, pricing, and APIs, through virtual machines, containers, Kubernetes, serverless, databases, load balancing, CDNs, security, observability, infrastructure as code, messaging, and disaster recovery, to CI/CD, FinOps, twelve-factor design, multi-region architecture, migration, service mesh, confidential computing, and the Well-Architected Framework." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "signature-cloud-study", "gen_demo_kind": "signature-cloud-demo",
        "source": source,
    }

CIT_PUB = ("Cloud computing (standard references: Mell P, Grance T. The "
           "NIST Definition of Cloud Computing. NIST Special Publication "
           "800-145; 2011; ISO/IEC 17788:2014 Information technology - "
           "Cloud computing - Overview and vocabulary; ISO/IEC 17789:2014 "
           "Information technology - Cloud computing - Reference "
           "architecture; Wiggins A. The Twelve-Factor App. 2011; Beyer B "
           "et al. Site Reliability Engineering: How Google Runs Production "
           "Systems. O Reilly Media; 2016; Amazon Web Services. AWS "
           "Well-Architected Framework. AWS Whitepaper; current; Cloud "
           "Native Computing Foundation. Kubernetes Documentation. CNCF; "
           "current; NIST SP 800-207 Zero Trust Architecture; NIST SP "
           "800-53 Security and Privacy Controls; Brewer E. Towards Robust "
           "Distributed Systems. 2000; Gilbert S, Lynch N. Brewer "
           "Conjecture and the Feasibility of Consistent, Available, "
           "Partition-Tolerant Web Services. 2002; FinOps Foundation "
           "Framework; OpenTelemetry specification; SLSA framework).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Cloud "
                     "Method - the cloud reframed as his Signature system, "
                     "every workload a stamped Signature vessel - clearly "
                     "labeled Signature-made.")

DBCFG = {}
DBCFG["jah-signature-cloud"] = _cfg(
    "jah-signature-cloud", "The JAH Signature Cloud Database",
    "Cloud computing as real technology: the five NIST characteristics, "
    "IaaS PaaS and SaaS, deployment models, virtualization, regions and "
    "zones, networking, storage, identity, pricing, containers, Kubernetes, "
    "serverless, databases, scaling, security, observability, and the "
    "advanced architecture disciplines - every record fact-checked with a "
    "working demonstration, taught progressively along the ladder.",
    "signature cloud record", "JAH-CLD-", "JAH Signature Cloud Archivist",
    "signature cloud archivist - real, fact-checked cloud computing "
    "technology across service models, deployment models, virtualization, "
    "storage, networking, and scaling; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from "
    "many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["jah-signature-cloud-signature"] = _cfg(
    "jah-signature-cloud-signature", "The JAH Signature Cloud Signature Database",
    "His original Signature Cloud Method: the cloud reframed as his "
    "Signature system - every workload a stamped Signature vessel, the "
    "control plane the Signature authority, regions the armory halls, "
    "scaling the summoned strength. The full ladder from what the cloud "
    "is through the characteristics, models, virtualization, networking, "
    "and storage, through compute, data, and operations, to the advanced "
    "architecture disciplines, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "signature cloud record", "JAH-CLDS-", "JAH Signature Cloud Archivist (Signature)",
    "signature cloud archivist - Signature editions: his original Signature "
    "Cloud Method, the cloud reframed as his Signature system with every "
    "workload a stamped Signature vessel, clearly labeled Signature-made "
    "and never presented as authentic public record; teaches progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
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
    for slug in ("jah-signature-cloud", "jah-signature-cloud-signature"):
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
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # JS hygiene: node --check on extracted page scripts and gen-*.js
    import re as _re
    for slug in built:
        ddir = os.path.join(REPO, "db", slug)
        page = open(os.path.join(ddir, "index.html"), encoding="utf-8").read()
        i = 0
        for m in _re.finditer(r"<script([^>]*)>(.*?)</script>", page, _re.S):
            attrs, s = m.group(1), m.group(2)
            if "src=" in attrs:
                continue
            tm = _re.search(r'\btype\s*=\s*["\']([^"\']+)["\']', attrs)
            if tm and "javascript" not in tm.group(1).lower():
                continue  # JSON-LD and other non-JS blocks
            if not s.strip():
                continue
            tmp = "/tmp/jsc-%s-%d.js" % (slug, i)
            i += 1
            open(tmp, "w", encoding="utf-8").write(s)
            p = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
            assert p.returncode == 0, "node --check failed page script %d in %s: %s" % (i, slug, p.stderr[:500])
        for gf in (os.path.join(ddir, "gen-%s.js" % slug),):
            p = subprocess.run(["node", "--check", gf], capture_output=True, text=True)
            assert p.returncode == 0, "node --check failed %s: %s" % (gf, p.stderr[:500])
    print("js hygiene: node --check clean on page scripts and gen-*.js", flush=True)

    # apostrophe-free check on role/ai_name/greet/search strings
    for slug, cfg in DBCFG.items():
        for k in ("ai", "role", "greet", "search_ph", "chat_ph"):
            assert "'" not in cfg[k], "apostrophe in %s.%s" % (slug, k)
    print("js strings: role/ai_name/greet/search apostrophe-free", flush=True)

    # merger fragment (the merger owns manifest.json and api.json)
    frag = {
        "public": {
            "slug": "jah-signature-cloud",
            "name": DBCFG["jah-signature-cloud"]["name"],
            "tagline": DBCFG["jah-signature-cloud"]["tagline"],
            "record_kind": DBCFG["jah-signature-cloud"]["record_kind"],
            "id_prefix": DBCFG["jah-signature-cloud"]["prefix"],
            "ai_name": DBCFG["jah-signature-cloud"]["ai"],
            "local_index": SHARD_BASE + "/data/jah-signature-cloud/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/jah-signature-cloud/index.jsonl.gz",
            "chunk_pattern": "data/jah-signature-cloud/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest",
        },
        "signature": {
            "slug": "jah-signature-cloud-signature",
            "name": DBCFG["jah-signature-cloud-signature"]["name"],
            "tagline": DBCFG["jah-signature-cloud-signature"]["tagline"],
            "record_kind": DBCFG["jah-signature-cloud-signature"]["record_kind"],
            "id_prefix": DBCFG["jah-signature-cloud-signature"]["prefix"],
            "ai_name": DBCFG["jah-signature-cloud-signature"]["ai"],
            "local_index": SHARD_BASE + "/data/jah-signature-cloud-signature/index.jsonl.gz",
            "record_count": 34, "status": "live", "full_records": 34,
            "index": SHARD_BASE + "/data/jah-signature-cloud-signature/index.jsonl.gz",
            "chunk_pattern": "data/jah-signature-cloud-signature/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature",
        },
    }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)
    print("manifest + api.json: NOT touched (merger owns them).")
    print("built %d databases, %d records total" % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
