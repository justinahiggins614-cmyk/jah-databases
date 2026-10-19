#!/usr/bin/env python3
"""Nanorobots vs cancer, routinely -- working demonstration.
Record JAH-FT20-000024 [Advanced] from The Medical Nanorobots Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT20-000024",
    "title": "Nanorobots vs cancer, routinely",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 24,
    "ladder_tier": "Advanced",
    "facts": ["Early demos in mice.", "Human translation is unproven.", "The oncology milestone."],
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
