#!/usr/bin/env python3
"""Build the installation-commissioning-procedures pair (public + Signature) for JAH Databases.

Thin wrapper around the shared group-H builder in
code/h-practical-impl-build/. Run directly, or via
code/h-practical-impl-build/build_all.py for the whole group.

Writes (this builder's scope ONLY - the coordinator merges the rest):
  main repo : db/installation-commissioning-procedures/index.html + gen-installation-commissioning-procedures.js
              db/installation-commissioning-procedures-signature/index.html + gen-installation-commissioning-procedures-signature.js
  shard repo: data/installation-commissioning-procedures/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/installation-commissioning-procedures-signature/index.jsonl.gz + chunks/chunk-0000.jsonl.gz

NEVER touches: data/manifest.json, api.json. NEVER git commits or pushes.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/h-practical-impl-build")
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code")
import build_all

if __name__ == "__main__":
    build_all.main(only="installation-commissioning-procedures")
