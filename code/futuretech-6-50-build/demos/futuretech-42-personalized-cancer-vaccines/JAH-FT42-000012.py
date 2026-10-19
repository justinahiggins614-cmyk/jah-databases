#!/usr/bin/env python3
"""Neoantigens discovered -- working demonstration.
Record JAH-FT42-000012 [Foundations] from The Personalized Cancer Vaccines Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT42-000012",
    "title": "Neoantigens discovered",
    "era": "2012-2014",
    "maturity": "Established",
    "ladder_rank": 12,
    "ladder_tier": "Foundations",
    "facts": ["The personal target.", "The fingerprint.", "Your cancer's signature."],
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
