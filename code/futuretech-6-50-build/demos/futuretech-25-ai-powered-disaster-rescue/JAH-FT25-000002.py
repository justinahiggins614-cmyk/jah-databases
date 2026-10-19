#!/usr/bin/env python3
"""Search and rescue dogs -- working demonstration.
Record JAH-FT25-000002 [Foundations] from The AI-Powered Disaster Rescue Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT25-000002",
    "title": "Search and rescue dogs",
    "era": "1800s-1900s",
    "maturity": "Established",
    "ladder_rank": 2,
    "ladder_tier": "Foundations",
    "facts": ["St. Bernards in the Alps.", "Modern SAR dogs from the 1970s.", "The biological rescue robot."],
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
