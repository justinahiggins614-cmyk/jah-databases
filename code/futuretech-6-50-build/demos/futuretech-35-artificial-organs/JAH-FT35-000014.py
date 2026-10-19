#!/usr/bin/env python3
"""Artificial lungs: ECMO advances -- working demonstration.
Record JAH-FT35-000014 [Compounded] from The Artificial Organs Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT35-000014",
    "title": "Artificial lungs: ECMO advances",
    "era": "2000s-2020s",
    "maturity": "Emerging",
    "ladder_rank": 14,
    "ladder_tier": "Compounded",
    "facts": ["COVID-19 drove use.", "Wearable prototypes.", "The breathing bridge."],
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
