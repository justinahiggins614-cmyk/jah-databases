#!/usr/bin/env python3
"""Thought-to-text for stroke -- working demonstration.
Record JAH-FT27-000015 [Compounded] from The Thought-to-Text Communication Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT27-000015",
    "title": "Thought-to-text for stroke",
    "era": "2024",
    "maturity": "Emerging",
    "ladder_rank": 15,
    "ladder_tier": "Compounded",
    "facts": ["Language areas targeted.", "Recovery plus decoding.", "The stroke milestone."],
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
