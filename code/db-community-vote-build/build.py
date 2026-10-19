#!/usr/bin/env python3
"""Thin builder for db-community-vote (public + Signature pair).
Delegates to the wave-10 master builder. Staged only; the coordinator merges.
"""
import os, sys
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/wave10-build")
import master_build
sys.exit(master_build.build_item("db-community-vote"))
