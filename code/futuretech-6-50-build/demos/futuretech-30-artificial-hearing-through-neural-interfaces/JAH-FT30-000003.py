#!/usr/bin/env python3
"""Vacuum-tube hearing aids -- working demonstration.
Record JAH-FT30-000003 [Foundations] from The Artificial Hearing Through Neural Interfaces Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT30-000003",
    "title": "Vacuum-tube hearing aids",
    "era": "1920s",
    "maturity": "Established",
    "ladder_rank": 3,
    "ladder_tier": "Foundations",
    "facts": ["Western Electric models.", "The wearable era.", "Tubes in the pocket."],
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
