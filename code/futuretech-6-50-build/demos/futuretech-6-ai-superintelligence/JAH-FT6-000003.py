#!/usr/bin/env python3
"""Logic Theorist: machines prove theorems -- working demonstration.
Record JAH-FT6-000003 [Foundations] from The AI Superintelligence Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT6-000003",
    "title": "Logic Theorist: machines prove theorems",
    "era": "1956",
    "maturity": "Established",
    "ladder_rank": 3,
    "ladder_tier": "Foundations",
    "facts": ["Written by Allen Newell and Herbert Simon.", "It proved 38 of the first 52 theorems attempted.", "First program engineered to mimic human problem-solving."],
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
