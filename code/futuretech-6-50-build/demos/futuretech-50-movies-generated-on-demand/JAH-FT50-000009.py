#!/usr/bin/env python3
"""Digital cinema -- working demonstration.
Record JAH-FT50-000009 [Foundations] from The Movies Generated on Demand Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT50-000009",
    "title": "Digital cinema",
    "era": "1999-2005",
    "maturity": "Established",
    "ladder_rank": 9,
    "ladder_tier": "Foundations",
    "facts": ["Star Wars Episode I, 1999.", "The projection milestone.", "No more reels."],
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
