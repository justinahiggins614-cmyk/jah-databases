#!/usr/bin/env python3
"""Tangerine: shot on iPhone -- working demonstration.
Record JAH-FT50-000024 [Advanced] from The Movies Generated on Demand Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT50-000024",
    "title": "Tangerine: shot on iPhone",
    "era": "2015",
    "maturity": "Established",
    "ladder_rank": 24,
    "ladder_tier": "Advanced",
    "facts": ["Sundance, 2015.", "The democratization.", "Cinema in your pocket."],
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
