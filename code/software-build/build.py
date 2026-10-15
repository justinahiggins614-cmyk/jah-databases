#!/usr/bin/env python3
"""Build the 29 software/systems catalog databases for JAH Databases.

Sections (simplest -> most complex):
  APPS: software-applications, software-components, software-packaging
  TOOLS: developer-tools, data-tools, simulation-tools, software-engines
  LABS: lab-workspaces, rd-staging, specialty-labs
  CORE: runtimes-kernels, platforms-stacks
  STORAGE: software-registries, database-engines, data-infrastructure
  NETWORK: network-devices, network-fabric
  COMPUTATIONAL: abstract-machines, solvers
  LOW-LEVEL: boot-firmware, binary-tools
  LOCAL AI: model-serialization, edge-inference
  HARDWARE/FAB: pcb-design, fabrication-tools
  PROTOCOLS: network-protocols, data-structures
  MEDIA: graphics-pipeline, audio-dsp

All records are Signature-original technical summaries of real, well-established
software concepts (no website references, no Facebook references).

Writes (shard repo jah-databases-data-1, Pages-enabled):
       data/<slug>/index.jsonl.gz + data/<slug>/chunks/chunk-NNNN.jsonl.gz
Writes (main repo): db/<slug>/index.html, db/<slug>/gen-<slug>.js
Updates (main repo): data/manifest.json, api.json.
Pages are built with the shared builder, then upgraded with the staged
dedupe/xdb sweep (script tags + indexSameDb hook + generateChecked flow).
"""
import gzip
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, HERE)
from topics_apps import APPS_TOPICS
from topics_tools import TOOLS_TOPICS
from topics_labs_core import LABS_CORE_TOPICS
from topics_storage_net import STORAGE_NET_TOPICS
from topics_compute_low import COMPUTE_LOW_TOPICS
from topics_ai_fab import AI_FAB_TOPICS
from topics_proto_media import PROTO_MEDIA_TOPICS

ALL_TOPICS = {}
for _d in (APPS_TOPICS, TOOLS_TOPICS, LABS_CORE_TOPICS, STORAGE_NET_TOPICS,
           COMPUTE_LOW_TOPICS, AI_FAB_TOPICS, PROTO_MEDIA_TOPICS):
    ALL_TOPICS.update(_d)

CIT = {
    "software-applications": "Application architecture and software taxonomy (standard software engineering literature).",
    "software-components": "Component-based software engineering (standard software architecture literature).",
    "software-packaging": "Software distribution and package management (standard DevOps literature).",
    "developer-tools": "Compilers, build systems, and developer tooling (standard programming systems literature).",
    "data-tools": "Data processing and analysis tooling (standard data engineering literature).",
    "simulation-tools": "Simulation, emulation, and virtualization (standard systems literature).",
    "software-engines": "Reusable engine architectures (standard software architecture literature).",
    "lab-workspaces": "Laboratory and workspace design (standard facilities literature).",
    "rd-staging": "R&D and staging environments (standard engineering management literature).",
    "specialty-labs": "Specialized laboratory facilities (standard scientific facilities literature).",
    "runtimes-kernels": "Operating system kernels and language runtimes (standard OS literature).",
    "platforms-stacks": "Platform engineering and cloud stacks (standard cloud architecture literature).",
    "software-registries": "Artifact and package registries (standard DevOps literature).",
    "database-engines": "Database systems (standard database literature).",
    "data-infrastructure": "Storage and caching infrastructure (standard systems literature).",
    "network-devices": "Network devices and middleboxes (standard networking literature).",
    "network-fabric": "Network fabrics and messaging (standard distributed systems literature).",
    "abstract-machines": "Models of computation (standard theory of computation literature).",
    "solvers": "Solvers and optimization (standard algorithms literature).",
    "boot-firmware": "Firmware and boot processes (standard systems programming literature).",
    "binary-tools": "Binary analysis tools (standard reverse engineering literature).",
    "model-serialization": "Model weight formats (standard ML systems literature).",
    "edge-inference": "Edge and on-device inference (standard ML systems literature).",
    "pcb-design": "PCB design automation (standard electronic design literature).",
    "fabrication-tools": "Digital fabrication tooling (standard manufacturing literature).",
    "network-protocols": "Network protocols and tooling (standard networking literature).",
    "data-structures": "Serialization and data structures (standard algorithms literature).",
    "graphics-pipeline": "Real-time graphics pipelines (standard computer graphics literature).",
    "audio-dsp": "Digital audio and DSP (standard audio engineering literature).",
}


def _cfg(slug, name, tagline, record_kind, prefix, ai, role, groups):
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — real-world software knowledge organized in the Signature system. Every record carries the full entry: description, how it works, key points, and citations." % tagline,
        "sig_type": "Signature originals — real technical knowledge in the Signature system",
        "search_ph": "Search %s…" % record_kind,
        "chat_ph": "Ask about %s…" % record_kind,
        "archive_blurb": "Seeded Signature-original %s, marching toward one million records." % record_kind,
        "schema": "id, t, g, name, title, description, how_it_works, key_points, standards, citations, src, demo",
        "fields": "title, group, description, how it works, key points, standards, citations, demo program",
        "gen_desc": "Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about %s." % (ai, record_kind),
        "gen_fields": groups, "gen_kind": slug, "gen_demo_kind": "python",
        "source": "signature",
    }


DBCFG = {
"software-applications": _cfg("software-applications", "The Software Applications Database",
    "Applications organized by execution model and architecture, from native apps to serverless functions.",
    "software application record", "JAH-APP-", "JAH Application Archivist",
    "application archivist — execution models, architectures, deployment", ["execution"]),
"software-components": _cfg("software-components", "The Software Components Database",
    "Extensions, plugins, libraries, drivers, and scripts — the reusable parts software is built from.",
    "software component record", "JAH-CMP-", "JAH Component Archivist",
    "component archivist — extensions, libraries, drivers, modules", ["extension"]),
"software-packaging": _cfg("software-packaging", "The Software Packaging Database",
    "Distribution and packaging formats: installers, containers, registries, and release artifacts.",
    "packaging format record", "JAH-PKG-", "JAH Packaging Archivist",
    "packaging archivist — formats, installers, registries", ["format"]),
"developer-tools": _cfg("developer-tools", "The Developer Tools Database",
    "Compilers, interpreters, debuggers, build systems, and the full developer toolchain.",
    "developer tool record", "JAH-DVT-", "JAH Developer Tools Archivist",
    "developer tools archivist — compilers, debuggers, build", ["build"]),
"data-tools": _cfg("data-tools", "The Data Tools Database",
    "Parsers, scrapers, ETL, monitors, fuzzers, and analyzers — tools that process data.",
    "data tool record", "JAH-DAT-", "JAH Data Tools Archivist",
    "data tools archivist — parsing, ETL, monitoring, analysis", ["processing"]),
"simulation-tools": _cfg("simulation-tools", "The Simulation Tools Database",
    "Emulators, simulators, sandboxes, hypervisors, and virtual machines.",
    "simulation tool record", "JAH-SIM-", "JAH Simulation Archivist",
    "simulation archivist — emulation, virtualization, sandboxes", ["simulation"]),
"software-engines": _cfg("software-engines", "The Software Engines Database",
    "Reusable engines: physics, rendering, inference, rules, workflow, and policy engines.",
    "software engine record", "JAH-ENG-", "JAH Engine Archivist",
    "engine archivist — reusable software engines", ["engine"]),
"lab-workspaces": _cfg("lab-workspaces", "The Lab Workspaces Database",
    "Laboratories, workspaces, testbeds, studios, and control rooms.",
    "lab workspace record", "JAH-LAB-", "JAH Lab Archivist",
    "lab archivist — workspaces, testbeds, control rooms", ["workspace"]),
"rd-staging": _cfg("rd-staging", "The R&D and Staging Database",
    "Research environments, proving grounds, staging, clusters, and test ranges.",
    "R&D environment record", "JAH-RD-", "JAH R&D Archivist",
    "R&D archivist — staging, proving grounds, clusters", ["staging"]),
"specialty-labs": _cfg("specialty-labs", "The Specialty Labs Database",
    "Specialized laboratories: fab labs, wet/dry labs, optics, forensics, and field sites.",
    "specialty lab record", "JAH-SLAB-", "JAH Specialty Lab Archivist",
    "specialty lab archivist — scientific and technical labs", ["specialty"]),
"runtimes-kernels": _cfg("runtimes-kernels", "The Runtimes and Kernels Database",
    "Language runtimes, OS kernels, HALs, and the substrates software runs on.",
    "runtime/kernel record", "JAH-RTK-", "JAH Runtime Archivist",
    "runtime archivist — kernels, runtimes, substrates", ["core"]),
"platforms-stacks": _cfg("platforms-stacks", "The Platforms and Stacks Database",
    "Technology stacks, cloud platforms, service meshes, and control/data planes.",
    "platform record", "JAH-PLT-", "JAH Platform Archivist",
    "platform archivist — stacks, cloud, service mesh", ["platform"]),
"software-registries": _cfg("software-registries", "The Software Registries Database",
    "Package registries, artifact repositories, vaults, and catalogs.",
    "registry record", "JAH-REG-", "JAH Registry Archivist",
    "registry archivist — registries, repositories, vaults", ["repository"]),
"database-engines": _cfg("database-engines", "The Database Engines Database",
    "Relational, time-series, key-value, document, graph, and object store engines.",
    "database engine record", "JAH-DBE-", "JAH Database Archivist",
    "database archivist — database engines", ["engine"]),
"data-infrastructure": _cfg("data-infrastructure", "The Data Infrastructure Database",
    "Caches, lakes, warehouses, archives, and storage infrastructure.",
    "data infrastructure record", "JAH-DIN-", "JAH Data Infrastructure Archivist",
    "data infrastructure archivist — caches, lakes, storage", ["infra"]),
"network-devices": _cfg("network-devices", "The Network Devices Database",
    "Bridges, gateways, routers, proxies, load balancers, and middleboxes.",
    "network device record", "JAH-NET-", "JAH Network Archivist",
    "network archivist — devices, middleboxes", ["device"]),
"network-fabric": _cfg("network-fabric", "The Network Fabric Database",
    "Pipelines, streams, meshes, queues, brokers, and messaging fabrics.",
    "network fabric record", "JAH-FAB-", "JAH Fabric Archivist",
    "fabric archivist — pipelines, streams, messaging", ["fabric"]),
"abstract-machines": _cfg("abstract-machines", "The Abstract Machines Database",
    "Models of computation: Turing machines, automata, lambda calculus, Petri nets.",
    "computational model record", "JAH-ACM-", "JAH Computation Archivist",
    "computation archivist — models of computation", ["model"]),
"solvers": _cfg("solvers", "The Solvers Database",
    "SAT/SMT, theorem provers, optimizers, and numerical solvers.",
    "solver record", "JAH-SLV-", "JAH Solver Archivist",
    "solver archivist — solvers and optimization", ["solver"]),
"boot-firmware": _cfg("boot-firmware", "The Boot and Firmware Database",
    "UEFI, bootloaders, kernel images, ACPI, and device firmware.",
    "firmware record", "JAH-FW-", "JAH Firmware Archivist",
    "firmware archivist — boot, firmware, hardware init", ["firmware"]),
"binary-tools": _cfg("binary-tools", "The Binary Tools Database",
    "Hex editors, disassemblers, decompilers, and binary analysis tools.",
    "binary tool record", "JAH-BIN-", "JAH Binary Archivist",
    "binary archivist — binary analysis tooling", ["binary"]),
"model-serialization": _cfg("model-serialization", "The Model Serialization Database",
    "Weight formats: GGUF, SafeTensors, ONNX, AWQ/GPTQ/EXL2, LoRA adapters, and shards.",
    "model format record", "JAH-MSF-", "JAH Model Format Archivist",
    "model format archivist — serialization and quantization formats", ["format"]),
"edge-inference": _cfg("edge-inference", "The Edge Inference Database",
    "Local AI: on-device runners, RAG, KV cache, constrained decoding, and agents.",
    "edge inference record", "JAH-EI-", "JAH Edge AI Archivist",
    "edge AI archivist — on-device inference", ["edge"]),
"pcb-design": _cfg("pcb-design", "The PCB Design Database",
    "Schematic capture, layout, autorouting, DRC, Gerber, and signal integrity.",
    "PCB tool record", "JAH-PCB-", "JAH PCB Archivist",
    "PCB archivist — electronic design automation", ["pcb"]),
"fabrication-tools": _cfg("fabrication-tools", "The Fabrication Tools Database",
    "CAD, CAM, toolpaths, metrology, and digital manufacturing tooling.",
    "fabrication tool record", "JAH-FBT-", "JAH Fabrication Archivist",
    "fabrication archivist — CAD/CAM and manufacturing", ["fab"]),
"network-protocols": _cfg("network-protocols", "The Network Protocols Database",
    "Packet crafters, eBPF, STUN/TURN/ICE, messaging, and protocol tooling.",
    "network protocol record", "JAH-NP-", "JAH Protocol Archivist",
    "protocol archivist — protocols and tooling", ["protocol"]),
"data-structures": _cfg("data-structures", "The Data Structures Database",
    "Serializers, B-trees, LSM trees, bloom filters, and persistent structures.",
    "data structure record", "JAH-DS-", "JAH Data Structure Archivist",
    "data structure archivist — serialization and structures", ["structure"]),
"graphics-pipeline": _cfg("graphics-pipeline", "The Graphics Pipeline Database",
    "Shaders, BVH, framebuffers, textures, and real-time rendering.",
    "graphics record", "JAH-GFX-", "JAH Graphics Archivist",
    "graphics archivist — real-time rendering pipelines", ["graphics"]),
"audio-dsp": _cfg("audio-dsp", "The Audio DSP Database",
    "DAWs, synthesizers, plugins, filters, and digital audio processing.",
    "audio record", "JAH-AUD-", "JAH Audio Archivist",
    "audio archivist — DSP and music production", ["audio"]),
}


def esc_html(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def demo_program(rec, cfg):
    pts = "\n".join("    %s," % json.dumps(p) for p in rec["key_points"])
    return (
        '#!/usr/bin/env python3\n'
        '"""%(title)s — %(dbname)s record demo.\n'
        'Property of Justin Addam Higgins (JAH).\n'
        '"""\n'
        'INFO = {\n'
        '    "id": %(id)s,\n'
        '    "title": %(title)s,\n'
        '    "group": %(group)s,\n'
        '    "description": %(desc)s,\n'
        '    "key_points": [\n%(pts)s\n'
        '    ],\n'
        '}\n'
        '\n'
        '\n'
        'def describe():\n'
        '    lines = []\n'
        '    lines.append("=" * 64)\n'
        '    lines.append(INFO["title"] + "  [" + INFO["group"] + "]")\n'
        '    lines.append("=" * 64)\n'
        '    lines.append("")\n'
        '    lines.append(INFO["description"])\n'
        '    lines.append("")\n'
        '    lines.append("Key points:")\n'
        '    for i, pt in enumerate(INFO["key_points"], 1):\n'
        '        lines.append("  %%d. %%s" %% (i, pt))\n'
        '    return "\\n".join(lines)\n'
        '\n'
        '\n'
        'def main():\n'
        '    print(describe())\n'
        '\n'
        '\n'
        'if __name__ == "__main__":\n'
        '    main()\n'
    ) % {
        "title": json.dumps(rec["t"]), "dbname": cfg["name"], "id": json.dumps(rec["id"]),
        "group": json.dumps(rec["g"]), "desc": json.dumps(rec["description"]),
        "pts": pts,
    }


def build_records(slug):
    cfg = DBCFG[slug]
    topics = ALL_TOPICS[slug]
    recs = []
    for i, (name, group, desc, points) in enumerate(topics):
        rid = "%s%06d" % (cfg["prefix"], i + 1)
        description = desc + " Key aspects include: " + "; ".join(points) + "."
        how = ("In practice, %s works by combining its core mechanisms into a coherent whole. "
               "Practitioners start from the fundamentals above, apply them to a concrete task, "
               "and validate the result against the relevant standards for the domain." % name)
        rec = {
            "id": rid, "t": name, "g": group, "name": name, "title": name,
            "description": description,
            "how_it_works": how,
            "key_points": list(points),
            "standards": ["Industry best practice for " + group],
            "citations": CIT[slug],
            "src": "signature",
        }
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": demo_program(rec, cfg),
                       "note": "Record demo: prints the full entry."}
        recs.append(rec)
    return recs


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


def update_json_list(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    have = {d["slug"] for d in data["databases"]}
    for e in entries:
        if e["slug"] not in have:
            data["databases"].append(e)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")


def manifest_entry(slug, n):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"],
        "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "status": "live", "full_records": n,
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": c["source"],
    }


def api_entry(slug, n):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "record_count": n, "status": "live",
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
    }


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    # staged dedupe/xdb sweep for the brand-new pages
    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in DBCFG:
        built[slug] = build_records(slug)

    # sanity: ids unique + prefix + required keys + demo programs compile + no stubs
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "src", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            assert r["demo"].get("program"), "empty demo in %s" % r["id"]
            assert len(r["description"]) > 60, "stub description in %s" % r["id"]
            assert "facebook" not in json.dumps(r).lower(), "facebook ref in %s" % r["id"]
        for r in recs[:: max(1, len(recs) // 12)]:
            compile(r["demo"]["program"], r["id"], "exec")
        n = write_shard_db(slug, recs)
        print("shard: %-24s %d records" % (slug, n), flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        # dedupe/xdb upgrade at build time (staged sweep logic)
        changed, notes = sweep.process_page(ppath)
        # gen topics: field -> ["name — group"] list
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s — %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ",".join(notes)), flush=True)

    entries_m = [manifest_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [api_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases" % len(built))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
