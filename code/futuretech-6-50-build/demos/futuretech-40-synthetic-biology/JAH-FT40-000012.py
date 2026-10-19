#!/usr/bin/env python3
"""Venter's synthetic genome -- working demonstration.
Record JAH-FT40-000012 [Foundations] from The Synthetic Biology Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT40-000012",
    "title": "Venter's synthetic genome",
    "era": "2010",
    "maturity": "Established",
    "ladder_rank": 12,
    "ladder_tier": "Foundations",
    "facts": ["Science, 2010.", "'Synthia.'", "Life, written."],
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
