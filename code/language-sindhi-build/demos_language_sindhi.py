#!/usr/bin/env python3
"""Demonstration programs for the Sindhi Language databases.

Real, runnable, stdlib-only Python built by the shared langkit10 demo
builders. The build machine-executes every demo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langkit10 import build_demos

DEMOS = build_demos()
