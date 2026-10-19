#!/usr/bin/env python3
"""Build script for the The Personalized Gene Editing Future Technology Database — delegates to the shared futuretech-6-50 builder.
Property of Justin Addam Higgins (JAH)."""
import os, sys, json, importlib.util
_shared = os.path.expanduser('~/workspace/jah-databases/code/futuretech-6-50-build/build.py')
_spec = importlib.util.spec_from_file_location('ft650_build', _shared)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
if __name__ == '__main__':
    print(json.dumps(_mod.build_item('futuretech-36-personalized-gene-editing'), indent=1))
