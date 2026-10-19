#!/usr/bin/env python3
"""Kernel's non-invasive ambition -- working demonstration.
Record JAH-FT26-000022 [Compounded] from The Brain-Computer Interfaces Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT26-000022",
    "title": "Kernel's non-invasive ambition",
    "era": "2017-2021",
    "maturity": "Emerging",
    "ladder_rank": 22,
    "ladder_tier": "Compounded",
    "facts": ["Founded by Bryan Johnson, 2016.", "Flow helmet measured brain activity.", "The consumer neuroscience bet."],
}
def ladder_progress(rank, total=34):
    return rank / total
progress = ladder_progress(record["ladder_rank"])
print("Record: %s (%s)" % (record["title"], record["era"]))
print("Maturity: %s" % record["maturity"])
print("Ladder: rank %d of 34 (%s) -- %.1f%% along the ladder" % (record["ladder_rank"], record["ladder_tier"], progress * 100))
for i, f in enumerate(record["facts"], 1):
    print("Fact %d: %s" % (i, f))
checksum = sum(ord(c) for c in record["id"] + record["title"]) % 100000
print("Record checksum: %d" % checksum)
print("OK")
