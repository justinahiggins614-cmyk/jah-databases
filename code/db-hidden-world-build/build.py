#!/usr/bin/env python3
"""Build script for db-hidden-world (funsocial-wave1, JAH Databases).
Delegates to the wave driver. Staged only - never touches data/manifest.json
or api.json, never commits. Property of Justin Addam Higgins (JAH).
"""
import os
import sys

sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/funsocial-wave1"))
import run_wave1

if __name__ == "__main__":
    run_wave1.build_one("db-hidden-world")
