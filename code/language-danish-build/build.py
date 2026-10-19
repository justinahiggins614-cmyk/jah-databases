#!/usr/bin/env python3
"""Build the Danish language database pair (ranks 71-80, batch 8).
Thin wrapper - the shared engine lives in
code/language-batch8-build/. Run: python3 build.py
NEVER touches data/manifest.json or api.json. NEVER commits.
"""
import os
import sys
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/language-batch8-build")
import build_batch8

if __name__ == "__main__":
    sys.exit(build_batch8.main(["danish"]))
