#!/usr/bin/env python3
"""Bilingualism and cognition -- working demonstration.
Record JAH-FT32-000012 [Foundations] from The Human Brain Enhancement Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT32-000012",
    "title": "Bilingualism and cognition",
    "era": "2000s-2010s",
    "maturity": "Established",
    "ladder_rank": 12,
    "ladder_tier": "Foundations",
    "facts": ["Debated but real findings.", "The linguistic workout.", "The debated boost."],
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
