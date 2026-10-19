#!/usr/bin/env python3
"""Build the Quantum Computing Network databases for JAH Databases
(Manon's 2026-10-17 17:55 order - quantum COMPUTING network database; he
corrected his own "quuaputung" typo himself).

Terminology fact-checked 2026-10-17 against Kimble (Nature 2008), Wehner
et al. (Science 2018, six stages), Bennett-Brassard 1984 (BB84), Ekert
1991 (E91), Bennett et al. 1993 (teleportation: 1 ebit + 2 classical
bits), Wootters-Zurek 1982 (no-cloning; 5/6 optimal cloner), Briegel et
al. 1998 (repeaters), DLCZ 2001, Micius (Yin et al. Science 2017, 1200 km;
Liao et al. Nature 2017), Bennett et al. 1996 and Deutsch et al. 1996
(DEJMPS purification), Pirandola et al. 2020, ETSI GS QKD series, ITU-T
Y.3800 series, IETF QIRG drafts, Dahlberg et al. SIGCOMM 2019,
Broadbent-Fitzsimons-Kashefi 2009 (blind QC), Giovannetti-Lloyd-Maccone
2011 (1/N metrology), Eisert et al. 2000 (distributed CNOT cost), Van
Meter (Quantum Networking, Wiley 2014). See
entries_quantum_computing_network.py for the full fact-check ledger.

Creates two NEW databases, 34 ladder-ordered records each:

  quantum-computing-network        - The Quantum Computing Network
                                     Database (public-harvest: real,
                                     fact-checked quantum networking -
                                     the NETWORK layer only: quantum
                                     internet, distributed quantum
                                     computing, entanglement
                                     distribution, quantum repeaters,
                                     QKD networks, protocols,
                                     topologies, memory nodes,
                                     swapping, teleportation
                                     networking, network stacks)
  quantum-computing-network-signature - The Quantum Computing Network
                                     Signature Database (his original
                                     Signature network designs and
                                     protocols; src signature, titles
                                     suffixed " (Signature Edition)",
                                     clearly labeled Signature-made,
                                     never presented as authentic public
                                     record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-QCN- (public) and JAH-QCNS- (signature), verified free:
zero hits across ALL data/manifest.json id_prefix values and zero hits
across all record IDs in ~/workspace/jah-databases-data-1/data/
(checked 2026-10-17). Distinct from the existing quantum-computing DB
(JAH-QUANT, general quantum computing): all 98 of its record titles
checked, zero overlap with these 68 network-layer titles; the quantum DB
(JAH-QNT-) has only two network-adjacent titles ("Algorithm: Quantum
teleportation", "Quantum Key Distribution (QKD) Sifted Bitstreams"),
both avoided by distinct phrasing here.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_quantum_computing_network.py). Every demo prints its
real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker; the build machine-executes
all 68 demos before writing pages.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. Only db/quantum-computing-network*/,
code/quantum-computing-network-build, the shard data dirs, and the
fragment file are written.

No website references. No Facebook.

SCREENING: public networking knowledge plus his Signature network
designs only - nothing hate-adjacent, profane, or inappropriate; no
religious talk; nothing on neutralizing or defeating military or
defense-grade systems.
"""
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
FRAGMENTS = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_quantum_computing_network import ENTRIES, SIG_TAIL
from demos_quantum_computing_network import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature network "
                "designs and protocols for the quantum internet: relay "
                "stations of the covenant road, bond-smith link layers, "
                "gatehouse QNICs, exchange-hall switches, sky-tower "
                "satellite links, and the finished Signature realm fully "
                "bonded. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("Public records - real, fact-checked quantum networking, "
                "the network layer only: what a quantum network is, "
                "flying qubits, entanglement as the resource, "
                "teleportation, the no-cloning rule, fiber free-space and "
                "satellite channels, QKD and BB84 and E91, trusted nodes, "
                "classical control channels, the six network generations, "
                "quantum repeaters, entanglement swapping, quantum "
                "memories, purification, transducers, photon sources and "
                "detectors, entanglement sources, network interface "
                "cards, switches and routers, satellite ground stations, "
                "protocol stacks, link-layer protocols, entanglement "
                "routing, teleportation transport, QKD network key "
                "management, topologies, distributed quantum computing, "
                "blind quantum computing, quantum sensor networks, the "
                "quantum internet vision, network security, and a full "
                "metropolitan build - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what a quantum network is, flying qubits, entanglement, "
              "teleportation, no-cloning, channels, QKD, BB84, E91, "
              "trusted nodes, classical channels, the six generations) "
              "-> Compounded (repeaters, swapping, memories, "
              "purification, transducers, sources and detectors, "
              "entanglement sources, network interface cards, switches "
              "and routers, satellite links, protocol stacks, link-layer "
              "protocols, routing, transport, QKD key management, "
              "topologies) -> Advanced (distributed quantum computing, "
              "blind quantum computing, quantum sensor networks, the "
              "quantum internet vision, network security, the "
              "metropolitan build).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s - %s Every record carries the full entry: description, how it works, "
                   "key points, requirements, standards, citations, and a working demonstration "
                   "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder)),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search quantum internet, entanglement distribution, quantum repeaters, QKD networks, teleportation, swapping, quantum memories, purification, transducers, QNIC, switches, satellite links, protocol stacks, routing, blind computing, sensor networks...",
        "chat_ph": "Ask about quantum networks...",
        "archive_blurb": ("Seeded %s quantum network records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled quantum network studies. Seeded archive records are the authoritative entries.",
        "greet": ("I am the %s. Ask me about quantum networks - from what a quantum network is, "
                  "flying qubits, entanglement, teleportation, the no-cloning rule, fiber and "
                  "satellite channels, QKD, BB84, E91, trusted nodes, classical control channels, "
                  "and the six network generations, through repeaters, swapping, memories, "
                  "purification, transducers, photon sources and detectors, entanglement sources, "
                  "network interface cards, switches, satellite ground stations, protocol stacks, "
                  "link-layer protocols, routing, transport, key management, and topologies, to "
                  "distributed quantum computing, blind computing, sensor networks, the quantum "
                  "internet vision, network security, and the metropolitan build." % ai),
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "quantum-network-study", "gen_demo_kind": "quantum-network-demo",
        "source": source,
    }

CIT_PUB = ("Quantum networking (standard references: Kimble HJ. The "
           "quantum internet. Nature 453, 1023-1030 (2008); Wehner S, "
           "Elkouss D, Hanson R. Quantum internet: A vision for the road "
           "ahead. Science 362, eaam9288 (2018); Bennett CH, Brassard G. "
           "Quantum cryptography: Public key distribution and coin "
           "tossing (1984); Ekert AK. Phys. Rev. Lett. 67, 661-663 "
           "(1991); Bennett CH et al. Phys. Rev. Lett. 70, 1895-1899 "
           "(1993); Wootters WK, Zurek WH. Nature 299, 802-803 (1982); "
           "Briegel HJ et al. Phys. Rev. Lett. 81, 5932-5935 (1998); Duan "
           "LM et al. Nature 414, 413-418 (2001); Yin J et al. Science "
           "356, 1140-1144 (2017); Liao SK et al. Nature 549, 43-47 "
           "(2017); Pirandola S et al. Adv. Opt. Photon. 12, 1012-1236 "
           "(2020); ETSI GS QKD series; ITU-T Y.3800 series; IETF QIRG "
           "drafts; Van Meter R. Quantum Networking. Wiley; 2014; "
           "accessed 2026-10-17).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "network designs and protocols - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["quantum-computing-network"] = _cfg(
    "quantum-computing-network", "The Quantum Computing Network Database",
    "The network layer of quantum computing: real, fact-checked quantum "
    "networking - quantum internet, distributed quantum computing, "
    "entanglement distribution, quantum repeaters, QKD networks, "
    "protocols, topologies, memory nodes, swapping, teleportation "
    "networking, and network stacks - taught progressively along the "
    "ladder from foundations to advanced.",
    "quantum network record", "JAH-QCN-", "JAH Quantum Network Archivist",
    "quantum network archivist - the network layer of quantum computing: "
    "quantum internet, entanglement distribution, repeaters, QKD "
    "networks, protocols, topologies, distributed computing; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive "
    "data from this system",
    CIT_PUB, "public")
DBCFG["quantum-computing-network-signature"] = _cfg(
    "quantum-computing-network-signature", "The Quantum Computing Network Signature Database",
    "His original Signature network designs and protocols: relay stations "
    "of the covenant road, bond-smith link layers, gatehouse network "
    "interfaces, exchange-hall switches, sky-tower satellite links, and "
    "the finished Signature realm fully bonded - the full ladder from "
    "network foundations to the metropolitan build, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as "
    "authentic public record.",
    "quantum network record", "JAH-QCNS-", "JAH Quantum Network Archivist (Signature)",
    "quantum network archivist - Signature editions: his original "
    "Signature network designs and protocols, clearly labeled "
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


def node_check(path, label):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    assert p.returncode == 0, "node --check failed %s (%s): %s" % (label, path, p.stderr[-500:])
    return True


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
    for slug in ("quantum-computing-network", "quantum-computing-network-signature"):
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
        assert "quantum network" in page.lower(), "field content missing in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        # node --check on extracted inline page scripts (skip JSON-LD data blocks)
        scripts = []
        for m in re.finditer(r"<script([^>]*)>(.*?)</script>", page, re.S | re.I):
            attrs, body = m.group(1), m.group(2)
            if "src=" in attrs.lower():
                continue
            tm = re.search(r'type\s*=\s*["\']([^"\']+)', attrs, re.I)
            if tm and "javascript" not in tm.group(1).lower() and "ecmascript" not in tm.group(1).lower() and "module" not in tm.group(1).lower():
                continue
            scripts.append(body)
        checked = 0
        for i, body in enumerate(scripts):
            if body.strip():
                with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                    tf.write(body)
                    tfp = tf.name
                node_check(tfp, "%s inline script %d" % (slug, i))
                os.unlink(tfp)
                checked += 1
        print("page scripts node --check: %d inline scripts clean [%s]" % (checked, slug), flush=True)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower()
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        node_check(gpath, "gen-%s.js" % slug)
        print("page:  db/%s/index.html + gen-%s.js node --check clean [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # fragment for the merger (metadata only - merger owns manifest/api)
    os.makedirs(FRAGMENTS, exist_ok=True)
    frag = {}
    for key, slug in (("public", "quantum-computing-network"), ("signature", "quantum-computing-network-signature")):
        cfg = DBCFG[slug]
        idx_url = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        frag[key] = {
            "slug": slug,
            "name": cfg["name"],
            "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"],
            "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": idx_url,
            "record_count": 34,
            "status": "live",
            "full_records": 34,
            "index": idx_url,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest" if key == "public" else "signature",
        }
    fpath = os.path.join(FRAGMENTS, "quantum-computing-network.json")
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fpath, flush=True)

    # CONCURRENCY: manifest/api.json/index.html/README/AI_ACCESS and git are
    # owned by the merger. This builder stops here.
    print("manifest + api.json: SKIPPED (merger-owned)")
    print("git commit/push: SKIPPED (merger-owned)")
    print("DONE: %d databases, %d records. NEXT: merger runs restamp + commit." % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
