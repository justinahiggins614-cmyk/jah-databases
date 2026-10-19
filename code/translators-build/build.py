#!/usr/bin/env python3
"""Builder for translators (public + Signature pair). Staged only; the coordinator merges."""
import os, sys
sys.path.insert(0, os.path.expanduser("~/workspace/hidden_files/gapaudit-p3-arts-history"))
import build_driver
build_driver.build_one("TRANSLATORS")
