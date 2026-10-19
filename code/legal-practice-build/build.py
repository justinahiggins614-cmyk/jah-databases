#!/usr/bin/env python3
"""Build the legal-practice pair. Property of Justin Addam Higgins (JAH)."""
import sys, os, json
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))
import lib
from topics_legal_practice import CFG, TOPICS, demo_builder

HERE = os.path.dirname(os.path.abspath(__file__))

built = lib.build_pair(CFG, TOPICS, demo_builder)
lib.cross_pair_dedupe(built)

frag = []
for edition, prefix, src in (("pub", CFG["prefix_pub"], "public-harvest"),
                             ("sig", CFG["prefix_sig"], "signature")):
    slug = CFG["slug"] if edition == "pub" else CFG["slug"] + "-signature"
    name = CFG["name_pub"] if edition == "pub" else CFG["name_sig"]
    meta = dict(CFG, tagline=(CFG["tagline_pub"] if edition == "pub" else CFG["tagline_sig"]),
                ai_name=(CFG["ai_pub"] if edition == "pub" else CFG["ai_sig"]))
    frag.append(lib.manifest_entry(meta, slug, name, prefix, src, 34))
with open(os.path.join(HERE, "manifest-fragment.json"), "w") as f:
    json.dump(frag, f, indent=1, ensure_ascii=False)
print("manifest-fragment.json written (2 entries, status=staged)")
print("PAIR DONE: legal-practice")
