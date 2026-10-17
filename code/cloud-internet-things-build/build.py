#!/usr/bin/env python3
"""Build the Cloud and Internet Things databases for JAH Databases
(Manon's 2026-10-17 15:32 EDT orders #16-17).

Creates two NEW databases, 34 ladder-ordered records each:
  cloud-internet-things            - The Cloud and Internet Things Database
                                     (public-harvest: real, fact-checked
                                     cloud and internet technology)
  cloud-internet-things-signature  - The Cloud and Internet Things Signature
                                     Database
                                     (his original Signature Cloud Method;
                                     src signature, titles suffixed
                                     " (Signature Edition)", never
                                     presented as authentic public record)

ID prefixes: JAH-CIT- (public) and JAH-CITS- (signature), verified free
in the manifest (2,390 databases) and in every shard index in
jah-databases-data-1 (zero hits).

Dedupe pre-check 2026-10-17: all 68 titles checked vs the whole-system
gate before authoring; one refusal ("Serverless Functions" collided with
software-applications JAH-APP-000020) -> retitled to "Serverless
Computing and Functions as a Service", CLEAN.

CONCURRENCY: this script NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. A merger handles those. It only creates new untracked paths.

Never the words "bat belt" anywhere. No website references. No Facebook.
Nothing on neutralizing/defeating military or defense-grade systems.
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
from entries_cloud_internet_things import ENTRIES, SIG_TAIL
from demos_cloud_internet_things import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature Cloud Method: "
                "every cloud service a covenant of capacity, the internet the "
                "great exchange where covenants are kept, scaling the kept "
                "oath, and security the guarded gate. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked cloud and internet "
                "technology: what cloud computing is, how packets travel, "
                "DNS, IP addressing and subnetting, HTTP, TLS and HTTPS, "
                "virtualization, cloud service models (IaaS, PaaS, SaaS), "
                "deployment models, data centers and regions, cloud storage "
                "types, containers, Kubernetes, load balancers and auto "
                "scaling, content delivery networks, virtual networks, "
                "cloud databases, serverless, identity and access "
                "management, message queues and event streams, CI/CD "
                "pipelines, caching, edge computing, IoT connectivity, "
                "cloud security, DDoS defense and WAFs, zero trust, "
                "multi-cloud architecture, observability, FinOps, disaster "
                "recovery, infrastructure as code, service mesh, and the "
                "future internet - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what cloud computing is, how packets travel, DNS, IP "
              "addresses and subnetting, HTTP and the web request, TLS and "
              "HTTPS, virtualization, cloud service models, cloud "
              "deployment models, data centers regions and availability "
              "zones, cloud storage types) -> Compounded (containers and "
              "container images, Kubernetes orchestration, load balancers "
              "and auto scaling, content delivery networks, virtual "
              "networks subnets and firewalls, cloud databases relational "
              "and NoSQL, serverless computing, identity and access "
              "management, message queues and event streams, CI and CD "
              "pipelines, caching) -> Advanced (edge computing, IoT "
              "connectivity, cloud security shared responsibility, DDoS "
              "defense and web application firewalls, zero trust network "
              "architecture, multi-cloud and hybrid architecture, "
              "observability, cloud cost engineering and FinOps, disaster "
              "recovery and backups, infrastructure as code, service mesh, "
              "the future internet).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search cloud computing, packets, DNS, IP addresses, HTTP, TLS, virtualization, IaaS, containers, Kubernetes, load balancers, CDN, serverless, IAM, edge, IoT, MQTT, zero trust, FinOps, disaster recovery...",
        "chat_ph": "Ask about cloud and internet things...",
        "archive_blurb": ("Seeded %s cloud and internet things records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled cloud and internet studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about cloud and internet things - from what cloud computing is through packets, DNS, IP addressing, HTTP, TLS, virtualization, service models, deployment models, data centers, and storage, through containers, Kubernetes, load balancers, CDNs, virtual networks, databases, serverless, IAM, queues, CI/CD, and caching, to edge computing, IoT, cloud security, DDoS defense, zero trust, multi-cloud, observability, FinOps, disaster recovery, infrastructure as code, service mesh, and the future internet." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "cloud-internet-study", "gen_demo_kind": "cloud-internet-demo",
        "source": source,
    }

CIT_PUB = ("Cloud and internet technology (standard references: Mell P, "
           "Grance T. NIST SP 800-145. The NIST Definition of Cloud "
           "Computing; 2011; ISO/IEC 17788:2014 cloud computing overview "
           "and vocabulary; Mockapetris P. RFC 1034/1035 DNS; 1987; Postel "
           "J. RFC 791 IP; 1981; Deering S, Hinden R. RFC 8200 IPv6; 2017; "
           "Fielding R et al. RFC 9110/9112 HTTP; 2022; Rescorla E. RFC "
           "8446 TLS 1.3; 2018; Langley A et al. RFC 9000 QUIC; 2021; "
           "ISO/IEC 20922:2016 MQTT v3.1.1; Kindervag et al. NIST SP "
           "800-207 Zero Trust Architecture; 2020; Joint Task Force. NIST "
           "SP 800-53 Rev. 5; 2020; Burns B et al. Borg, Omega, and "
           "Kubernetes. ACM Queue; 2016; Merkel D. Docker. Linux Journal; "
           "2014; Open Container Initiative image and runtime specs; "
           "Kreps J et al. Kafka; 2011; and the other landmarks cited per "
           "record).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Cloud "
                     "Method - every cloud service a covenant of capacity, "
                     "the internet the great exchange where covenants are "
                     "kept - clearly labeled Signature-made.")

DBCFG = {}
DBCFG["cloud-internet-things"] = _cfg(
    "cloud-internet-things", "The Cloud and Internet Things Database",
    "All cloud and internet things: real, fact-checked cloud service and "
    "deployment models, virtualization, containers, CDNs, DNS, HTTP and "
    "TLS, internet infrastructure, edge computing, and IoT connectivity - "
    "taught progressively along the ladder from foundations to advanced.",
    "cloud and internet record", "JAH-CIT-", "JAH Cloud and Internet Things Archivist",
    "cloud and internet things archivist - all cloud and internet things: "
    "cloud service and deployment models, virtualization, containers, "
    "CDNs, DNS, HTTP and TLS, internet infrastructure, edge computing, "
    "and IoT connectivity; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_PUB, "public")
DBCFG["cloud-internet-things-signature"] = _cfg(
    "cloud-internet-things-signature", "The Cloud and Internet Things Signature Database",
    "His original Signature Cloud Method: every cloud service a covenant "
    "of capacity, the internet the great exchange where covenants are "
    "kept, scaling the kept oath, security the guarded gate. The full "
    "ladder from what cloud computing is through packets, DNS, IP, HTTP, "
    "TLS, virtualization, and service models, through containers, "
    "orchestration, and networking, to edge, IoT, zero trust, FinOps, and "
    "the future internet, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "cloud and internet record", "JAH-CITS-", "JAH Cloud and Internet Things Archivist (Signature)",
    "cloud and internet things archivist - Signature editions: his "
    "original Signature Cloud Method, every cloud service a covenant of "
    "capacity and the internet the great exchange where covenants are "
    "kept, clearly labeled Signature-made and never presented as "
    "authentic public record; teaches progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles "
    "- definition, example, analogy, application, history, math, how-to - "
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
    for slug in ("cloud-internet-things", "cloud-internet-things-signature"):
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

    # NOTE: manifest.json / api.json updates are owned by the merger - not touched here.
    print("records built: %d databases, %d records" % (len(built), total))
    print("NEXT (merger): manifest + api.json entries, restamp, commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
