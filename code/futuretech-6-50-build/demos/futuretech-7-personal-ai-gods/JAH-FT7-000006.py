#!/usr/bin/env python3
"""Siri: the voice assistant era begins -- working demonstration.
Record JAH-FT7-000006 [Foundations] from The Personal AI Gods Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT7-000006",
    "title": "Siri: the voice assistant era begins",
    "era": "2011",
    "maturity": "Established",
    "ladder_rank": 6,
    "ladder_tier": "Foundations",
    "facts": ["Launched with the iPhone 4S in October 2011.", "Spun out of SRI's CALO project and DARPA funding.", "Set the template: wake word, voice query, spoken answer."],
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
