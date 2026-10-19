#!/usr/bin/env python3
"""Macrophages in regeneration -- working demonstration.
Record JAH-FT45-000024 [Advanced] from The Organ Regeneration Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT45-000024",
    "title": "Macrophages in regeneration",
    "era": "2010s",
    "maturity": "Emerging",
    "ladder_rank": 24,
    "ladder_tier": "Advanced",
    "facts": ["The conductor.", "The immune milestone.", "Inflammation, instructive."],
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
