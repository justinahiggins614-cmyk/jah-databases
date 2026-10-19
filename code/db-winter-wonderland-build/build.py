#!/usr/bin/env python3
"""Wave-7 builder for db-winter-wonderland (1000-list wave 7).
Staged only; the coordinator merges manifest fragments.
Property of Justin Addam Higgins (JAH).
"""
import os, sys
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/wave7-build"))
import build_all
build_all.build_slug("db-winter-wonderland")
