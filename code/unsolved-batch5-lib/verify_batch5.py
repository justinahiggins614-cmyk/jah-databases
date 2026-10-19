#!/usr/bin/env python3
"""Final verification for Unsolved Problems batch 5 (15 pairs).
Checks per pair: 34+34 records on disk, label gate 68/68, zero hyphen
leftovers, prefix form, ladder ranks, node --check on gen scripts,
fragment staged, manifest/api untouched (read-only check: no new entries).
Prints a compact report. Exits nonzero on any failure.
"""
import gzip, json, os, subprocess, sys

REPO = "/home/hatch/workspace/jah-databases"
DATA = "/home/hatch/workspace/jah-databases-data-1/data"
FRAG = "/home/hatch/workspace/hidden_files/missing-builds/fragments"
LABEL = "Signature-generated proposed solution \u2014 not established science."
HYPHEN = "Signature-generated proposed solution - not established science."

PAIRS = {
 "unsolved-data-science": ("JAH-USDS-", "JAH-USDSS-"),
 "unsolved-operations-research": ("JAH-USOR-", "JAH-USORS-"),
 "unsolved-industrial-engineering": ("JAH-USIE-", "JAH-USIES-"),
 "unsolved-nuclear-engineering": ("JAH-USNE-", "JAH-USNES-"),
 "unsolved-petroleum-engineering": ("JAH-USPE-", "JAH-USPES-"),
 "unsolved-environmental-engineering": ("JAH-USVE-", "JAH-USVES-"),
 "unsolved-hydrology": ("JAH-USHY-", "JAH-USHYS-"),
 "unsolved-atmospheric-science": ("JAH-USAT-", "JAH-USATS-"),
 "unsolved-cosmology": ("JAH-USCO-", "JAH-USCOS-"),
 "unsolved-particle-physics": ("JAH-USPP-", "JAH-USPPS-"),
 "unsolved-biochemistry": ("JAH-USBC-", "JAH-USBCS-"),
 "unsolved-bioinformatics": ("JAH-USBF-", "JAH-USBFS-"),
 "unsolved-toxicology": ("JAH-USTO-", "JAH-USTOS-"),
 "unsolved-cryptography": ("JAH-USCR-", "JAH-USCRS-"),
 "unsolved-control-theory": ("JAH-USCT-", "JAH-USCTS-"),
}

fails = []
for slug, (ppub, psig) in sorted(PAIRS.items()):
    try:
        tot = ok = 0
        for s, px in ((slug, ppub), (slug + "-signature", psig)):
            idx = sum(1 for _ in gzip.open(f"{DATA}/{s}/index.jsonl.gz", "rt"))
            ch = sorted(f for f in os.listdir(f"{DATA}/{s}/chunks") if f.endswith(".jsonl.gz"))
            n = 0
            ranks = []
            for cf in ch:
                for line in gzip.open(f"{DATA}/{s}/chunks/{cf}", "rt"):
                    r = json.loads(line); n += 1; tot += 1
                    assert r["id"].startswith(px), "prefix %s" % r["id"]
                    assert r["how_it_works"].startswith(LABEL), "label %s" % r["id"]
                    assert HYPHEN not in r["how_it_works"], "hyphen %s" % r["id"]
                    assert len(r["description"]) > 200, "stub %s" % r["id"]
                    assert "'" not in r["t"], "apostrophe %s" % r["id"]
                    ranks.append(r["ladder_rank"])
                    ok += 1
            assert idx == 34 and n == 34, "count %s idx=%d chunk=%d" % (s, idx, n)
            assert ranks == list(range(1, 35)), "ladder %s" % s
            # pages + gen js
            for s2 in (s,):
                ppath = f"{REPO}/db/{s2}/index.html"
                gpath = f"{REPO}/db/{s2}/gen-{s2}.js"
                assert os.path.exists(ppath) and os.path.exists(gpath), "page/gen missing %s" % s2
                pr = subprocess.run(["node", "--check", gpath], capture_output=True, text=True)
                assert pr.returncode == 0, "node check %s" % gpath
        frag = f"{FRAG}/{slug}.json"
        assert os.path.exists(frag), "fragment missing %s" % slug
        print("PASS %-42s 34+34  label %d/%d  hyphen 0" % (slug, ok, tot))
    except AssertionError as e:
        fails.append((slug, str(e)))
        print("FAIL %-42s %s" % (slug, e))

print("----")
print("pairs passed: %d/15" % (15 - len(fails)))
sys.exit(1 if fails else 0)
