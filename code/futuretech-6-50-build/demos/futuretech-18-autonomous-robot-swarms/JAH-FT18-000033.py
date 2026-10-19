#!/usr/bin/env python3
"""Swarms on other worlds -- working demonstration.
Record JAH-FT18-000033 [Advanced] from The Autonomous Robot Swarms Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT18-000033",
    "title": "Swarms on other worlds",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 33,
    "ladder_tier": "Advanced",
    "facts": ["The far end of the speculative ladder.", "Exploration multiplies with swarms.", "The working version of the whole technology."],
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
