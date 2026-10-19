#!/usr/bin/env python3
"""Build driver: language-malagasy pair (public + Signature), 34+34 full records.
Staged builder for the JAH Databases 5k->10k program. Never commits.
Property of Justin Addam Higgins (JAH)."""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "language-batch6-shared"))
from assembler import build_language
import content_malagasy as C

if __name__ == "__main__":
    report = build_language(C.LANG, editions=("public",))
    print(json.dumps(report, indent=1, ensure_ascii=False)[:4000])
    for ed, r in report["editions"].items():
        print(ed, r["slug"], r["records"], "records;", r["demos"], "; cross-title-hits:", len(r["cross_system_title_hits"]),
              "; ctx-hits:", len(r["religious_ctx_hits"]))
