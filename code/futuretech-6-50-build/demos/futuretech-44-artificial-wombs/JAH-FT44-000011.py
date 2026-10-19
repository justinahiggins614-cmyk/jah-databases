#!/usr/bin/env python3
"""The 14-day rule under review -- working demonstration.
Record JAH-FT44-000011 [Foundations] from The Artificial Wombs Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT44-000011",
    "title": "The 14-day rule under review",
    "era": "2021-2024",
    "maturity": "Emerging",
    "ladder_rank": 11,
    "ladder_tier": "Foundations",
    "facts": ["The ethics milestone.", "The rule, reconsidered.", "How far?"],
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
