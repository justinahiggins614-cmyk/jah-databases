#!/usr/bin/env python3
"""The identity upload debate -- working demonstration.
Record JAH-FT34-000013 [Compounded] from The Mind Uploading Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT34-000013",
    "title": "The identity upload debate",
    "era": "2010s-2020s",
    "maturity": "Emerging",
    "ladder_rank": 13,
    "ladder_tier": "Compounded",
    "facts": ["Chalmers' Reality+ (2022).", "The survival question.", "The debate matured."],
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
