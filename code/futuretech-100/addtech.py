#!/usr/bin/env python3
"""Append a tech-dict fragment file into a content module at its __APPEND_POINT__ marker."""
import sys
target, frag = sys.argv[1], sys.argv[2]
src = open(target).read()
marker = "    # __APPEND_POINT__"
assert marker in src, "no marker in " + target
newdict = open(frag).read().strip().rstrip(',')
src = src.replace(marker, "    " + newdict + ",\n" + marker, 1)
open(target, 'w').write(src)
print("appended", frag, "->", target)
