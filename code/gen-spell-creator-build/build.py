#!/usr/bin/env python3
"""Rebuild gen-spell-creator (public + signature) via the shared fantasy-worlds builder."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'fantasy-worlds-build'))
import build_all
if __name__ == '__main__':
    build_all.build_slug('gen-spell-creator')
