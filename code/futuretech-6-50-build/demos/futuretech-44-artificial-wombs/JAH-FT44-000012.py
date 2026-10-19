#!/usr/bin/env python3
"""Artificial placenta research -- working demonstration.
Record JAH-FT44-000012 [Foundations] from The Artificial Wombs Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT44-000012",
    "title": "Artificial placenta research",
    "era": "2010s-2020s",
    "maturity": "Emerging",
    "ladder_rank": 12,
    "ladder_tier": "Foundations",
    "facts": ["The lung bridge.", "The placenta, partial.", "Gas exchange, external."],
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
