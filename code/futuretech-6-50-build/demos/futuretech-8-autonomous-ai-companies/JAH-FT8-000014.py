#!/usr/bin/env python3
"""Generative AI does marketing content -- working demonstration.
Record JAH-FT8-000014 [Compounded] from The Autonomous AI Companies Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT8-000014",
    "title": "Generative AI does marketing content",
    "era": "2022-2023",
    "maturity": "Established",
    "ladder_rank": 14,
    "ladder_tier": "Compounded",
    "facts": ["Widespread enterprise adoption after 2022.", "Content production costs fell sharply.", "Brand voice control became the new skill."],
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
