#!/usr/bin/env python3
"""Entries for the Tagalog Language databases (batch 5, 2026-10-17).

Assembled by the shared langkit10 assembler from fact-checked language
data in langdata_tagalog.py. 34 ladder-ordered records (foundations 1-10 /
compounded 11-21 / advanced 22-34).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langkit10 import build_entries, build_sig_tail
from langdata_tagalog import DATA

ENTRIES = build_entries(DATA)
SIG_TAIL = build_sig_tail(DATA)
