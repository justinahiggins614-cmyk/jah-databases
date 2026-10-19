#!/usr/bin/env python3
"""Thin builder for home-safety (public + Signature pair).
Delegates to the everyday-life master builder. Staged only; the coordinator merges.
"""
import os, sys
sys.path.insert(0, "/home/hatch/workspace/hidden_files/everyday-build")
import master_ev
sys.exit(master_ev.build_item("home-safety"))
