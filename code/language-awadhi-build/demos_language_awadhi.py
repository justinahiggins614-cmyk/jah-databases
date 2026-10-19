#!/usr/bin/env python3
"""Demo map for the Awadhi Language databases. Auto-built from langkit."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "lang-batch9-common"))
import langkit
from entries_language_awadhi import ENTRIES

DEMOS = langkit.standard_demos(ENTRIES)
