#!/usr/bin/env python3
"""Partial reprogramming -- working demonstration.
Record JAH-FT37-000012 [Foundations] from The Age-Reversal Therapies Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT37-000012",
    "title": "Partial reprogramming",
    "era": "2016",
    "maturity": "Established",
    "ladder_rank": 12,
    "ladder_tier": "Foundations",
    "facts": ["Cell, 2016.", "Cyclic OSKM.", "Youth, partial."],
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
