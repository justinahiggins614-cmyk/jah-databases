#!/usr/bin/env python3
"""The 2045 Initiative -- working demonstration.
Record JAH-FT34-000018 [Compounded] from The Mind Uploading Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT34-000018",
    "title": "The 2045 Initiative",
    "era": "2011",
    "maturity": "Emerging",
    "ladder_rank": 18,
    "ladder_tier": "Compounded",
    "facts": ["Launched 2011.", "Avatar milestones.", "The movement."],
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
