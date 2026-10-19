#!/usr/bin/env python3
"""Open-source humanoids -- working demonstration.
Record JAH-FT16-000025 [Advanced] from The The Humanoid Robot Boom Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT16-000025",
    "title": "Open-source humanoids",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 25,
    "ladder_tier": "Advanced",
    "facts": ["3D printing plus commodity parts.", "Safety liability is the issue.", "The democratization milestone."],
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
