#!/usr/bin/env python3
"""Cellular therapeutics for diabetes -- working demonstration.
Record JAH-FT41-000027 [Advanced] from The Programmable Living Cells Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT41-000027",
    "title": "Cellular therapeutics for diabetes",
    "era": "2014-2024",
    "maturity": "Emerging",
    "ladder_rank": 27,
    "ladder_tier": "Advanced",
    "facts": ["The implantable factory.", "The diabetes crossover.", "Cells as devices."],
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
