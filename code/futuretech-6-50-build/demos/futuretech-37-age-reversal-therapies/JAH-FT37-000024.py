#!/usr/bin/env python3
"""Longevity clinics -- working demonstration.
Record JAH-FT37-000024 [Advanced] from The Age-Reversal Therapies Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT37-000024",
    "title": "Longevity clinics",
    "era": "2020s",
    "maturity": "Emerging",
    "ladder_rank": 24,
    "ladder_tier": "Advanced",
    "facts": ["The commercial frontier.", "Evidence thin.", "The buyer-beware record."],
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
