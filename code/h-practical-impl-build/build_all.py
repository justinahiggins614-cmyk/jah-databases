#!/usr/bin/env python3
"""Build the 10 priority-group-H database pairs for JAH Databases (2026-10-17).

10 pairs x (public + Signature) = 20 databases, 34 ladder-ordered records
each = 680 records total.

  repair-manuals-service-procedures        JAH-RMSP-  / JAH-RMSPS-
  installation-commissioning-procedures    JAH-ICOP-  / JAH-ICOPS-
  calibration-adjustment-instructions      JAH-CLBR-  / JAH-CLBRS-
  troubleshooting-decision-trees           JAH-TSHT-  / JAH-TSHTS-
  compatibility-interchangeability-records JAH-CIR-   / JAH-CIRS-
  tooling-fixture-designs                  JAH-TFD-   / JAH-TFDS-
  engineering-case-studies                 JAH-ENCS-  / JAH-ENCSS-
  costed-build-recipes                     JAH-CBR-   / JAH-CBRS-
  field-modification-retrofit-records      JAH-FMRR-  / JAH-FMRRS-
  end-of-life-disposal-procedures          JAH-EOLD-  / JAH-EOLDS-

Slugs + ID prefixes verified free: zero exact/substring hits across the
manifest id_prefix values and no slug in data/manifest.json (checked
2026-10-17 before authoring).

Writes (this builder's scope ONLY - the coordinator merges the rest):
  main repo : db/<slug>/index.html + gen-<slug>.js   (20 DBs)
  shard repo: data/<slug>/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
  build dir : code/h-practical-impl-build/ (shared code + entries)
  fragments : ~/workspace/hidden_files/missing-builds/fragments/<slug>.json
              + manifest-additions.json (this dir)

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes. No website references.
No Facebook.
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import common

sys.path.insert(0, "/home/hatch/workspace/jah-databases/code")
from dedupe_gate import DedupeGate

FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"

# (slug, entries_module)
JOBS = [
    ("repair-manuals-service-procedures", "entries_01_repair"),
    ("installation-commissioning-procedures", "entries_02_install"),
    ("calibration-adjustment-instructions", "entries_03_calibration"),
    ("troubleshooting-decision-trees", "entries_04_troubleshoot"),
    ("compatibility-interchangeability-records", "entries_05_compat"),
    ("tooling-fixture-designs", "entries_06_tooling"),
    ("engineering-case-studies", "entries_07_cases"),
    ("costed-build-recipes", "entries_08_costed"),
    ("field-modification-retrofit-records", "entries_09_retrofit"),
    ("end-of-life-disposal-procedures", "entries_10_eol"),
]


def load_entries(modname):
    spec = importlib.util.spec_from_file_location(
        modname, os.path.join(HERE, modname + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(only=None):
    DBCFG = common.make_cfgs()
    nb = common.load_nb(DBCFG)
    sweep = common.load_sweep()
    gate = DedupeGate("/home/hatch/workspace/jah-databases/data/dedupe/exact")

    manifest_entries = []
    api_entries = []
    gen_files = []
    total_recs = 0

    for slug, modname in JOBS:
        if only and slug != only:
            continue
        m = load_entries(modname)
        out = common.build_pair(DBCFG, nb, sweep, gate, slug, m.E, m.STD, m.CIT)
        for sfx in ("", "-signature"):
            s = slug + sfx
            cfg = dict(DBCFG[s])
            cfg["_slug"] = s
            manifest_entries.append(common.manifest_entry(cfg, 34))
            api_entries.append(common.api_entry(cfg, 34))
            gen_files.append(
                "/home/hatch/workspace/jah-databases/db/%s/gen-%s.js" % (s, s))
            total_recs += 34
        # per-slug fragment for the coordinator (established convention)
        frag = {
            "public": manifest_entries[-2],
            "signature": manifest_entries[-1],
        }
        os.makedirs(FRAGDIR, exist_ok=True)
        with open(os.path.join(FRAGDIR, slug + ".json"), "w",
                  encoding="utf-8") as f:
            json.dump(frag, f, ensure_ascii=False, indent=1)
        print("fragment: %s.json" % slug, flush=True)

    # node --check every gen script
    for g in gen_files:
        r = subprocess.run(["node", "--check", g], capture_output=True,
                           text=True)
        if r.returncode != 0:
            raise RuntimeError("node --check failed for %s: %s"
                               % (g, r.stderr[:300]))
    print("node --check: %d gen scripts clean" % len(gen_files), flush=True)

    # combined staged additions (coordinator merges; we never touch the live files)
    additions = {"manifest": manifest_entries, "api": api_entries}
    outp = os.path.join(HERE, "manifest-additions.json")
    with open(outp, "w", encoding="utf-8") as f:
        json.dump(additions, f, ensure_ascii=False, indent=1)
    print("staged: %s (%d manifest + %d api entries)"
          % (outp, len(manifest_entries), len(api_entries)), flush=True)
    print("TOTAL: %d records across %d databases"
          % (total_recs, len(manifest_entries)), flush=True)


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    main(only)
