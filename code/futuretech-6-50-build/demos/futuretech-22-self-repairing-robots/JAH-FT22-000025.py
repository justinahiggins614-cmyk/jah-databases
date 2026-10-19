#!/usr/bin/env python3
"""The 100-year robot -- working demonstration.
Record JAH-FT22-000025 [Advanced] from The Self-Repairing Robots Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT22-000025",
    "title": "The 100-year robot",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 25,
    "ladder_tier": "Advanced",
    "facts": ["Voyager's 45+ years hint at it.", "Maintenance as the design center.", "The longevity milestone."],
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
