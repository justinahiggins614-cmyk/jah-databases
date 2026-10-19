#!/usr/bin/env python3
"""Autonomous earthmovers -- working demonstration.
Record JAH-FT21-000016 [Compounded] from The Robot Construction Crews Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT21-000016",
    "title": "Autonomous earthmovers",
    "era": "2020-2024",
    "maturity": "Emerging",
    "ladder_rank": 16,
    "ladder_tier": "Compounded",
    "facts": ["Built Robotics retrofits.", "Rio Tinto's autonomous fleet.", "Earthmoving without drivers."],
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
