#!/usr/bin/env python3
"""Algorithmic trading automates markets -- working demonstration.
Record JAH-FT8-000007 [Foundations] from The Autonomous AI Companies Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT8-000007",
    "title": "Algorithmic trading automates markets",
    "era": "1990s-2000s",
    "maturity": "Established",
    "ladder_rank": 7,
    "ladder_tier": "Foundations",
    "facts": ["Program trading grew through the 1990s.", "High-frequency trading dominated by the 2010s.", "The first domain where machines outran human operators entirely."],
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
