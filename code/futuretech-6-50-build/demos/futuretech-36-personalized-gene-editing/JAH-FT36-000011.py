#!/usr/bin/env python3
"""Sickle cell: Casgevy approved -- working demonstration.
Record JAH-FT36-000011 [Foundations] from The Personalized Gene Editing Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT36-000011",
    "title": "Sickle cell: Casgevy approved",
    "era": "2023",
    "maturity": "Established",
    "ladder_rank": 11,
    "ladder_tier": "Foundations",
    "facts": ["December 2023.", "Vertex/CRISPR Therapeutics.", "The cure milestone."],
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
