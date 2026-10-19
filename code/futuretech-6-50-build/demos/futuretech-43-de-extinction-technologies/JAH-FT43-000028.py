#!/usr/bin/env python3
"""The ivory-billed woodpecker debate -- working demonstration.
Record JAH-FT43-000028 [Advanced] from The De-Extinction Technologies Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT43-000028",
    "title": "The ivory-billed woodpecker debate",
    "era": "2004-2020s",
    "maturity": "Emerging",
    "ladder_rank": 28,
    "ladder_tier": "Advanced",
    "facts": ["The ghost bird.", "The hope milestone.", "Extinct or hiding?"],
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
