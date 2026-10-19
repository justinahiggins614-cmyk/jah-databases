#!/usr/bin/env python3
"""Build script for the futuretech-ai-that-builds-better-ai database — delegates to the shared futuretech-100 builder.
Each slug dir: code/<slug>-build/build.py calls build_slug(slug).
Property of Justin Addam Higgins (JAH)."""
import os, sys, importlib.util
_shared = os.path.expanduser('~/workspace/jah-databases/code/futuretech-100/build_all.py')
_spec = importlib.util.spec_from_file_location('ft100_build_all', _shared)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
if __name__ == '__main__':
    _mod.build_slug('futuretech-ai-that-builds-better-ai')
