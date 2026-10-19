#!/usr/bin/env python3
"""Build the end-of-life-disposal-procedures pair (public + Signature) for JAH Databases.

Thin wrapper around the shared group-H builder in
code/h-practical-impl-build/. Run directly, or via
code/h-practical-impl-build/build_all.py for the whole group.

Writes (this builder's scope ONLY - the coordinator merges the rest):
  main repo : db/end-of-life-disposal-procedures/index.html + gen-end-of-life-disposal-procedures.js
              db/end-of-life-disposal-procedures-signature/index.html + gen-end-of-life-disposal-procedures-signature.js
  shard repo: data/end-of-life-disposal-procedures/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/end-of-life-disposal-procedures-signature/index.jsonl.gz + chunks/chunk-0000.jsonl.gz

NEVER touches: data/manifest.json, api.json. NEVER git commits or pushes.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/h-practical-impl-build")
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code")
import build_all

if __name__ == "__main__":
    build_all.main(only="end-of-life-disposal-procedures")
