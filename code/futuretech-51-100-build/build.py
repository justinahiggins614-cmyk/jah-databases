#!/usr/bin/env python3
"""Convenience wrapper for the futuretech 51-100 pair builder.
Delegates to build_all.py (supports --batch <file> | --all | --only <slug>).
NOTE (2026-10-18): this file was reconstructed after a sibling worker accidentally
overwrote the original; if it differed, the owning worker should restore their version.
Property of Justin Addam Higgins (JAH)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_all import main

if __name__ == '__main__':
    main()
