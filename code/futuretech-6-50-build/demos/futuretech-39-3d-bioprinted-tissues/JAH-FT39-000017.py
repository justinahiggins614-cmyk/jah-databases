#!/usr/bin/env python3
"""Laser-assisted bioprinting -- working demonstration.
Record JAH-FT39-000017 [Compounded] from The 3D-Bioprinted Tissues Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT39-000017",
    "title": "Laser-assisted bioprinting",
    "era": "2004",
    "maturity": "Established",
    "ladder_rank": 17,
    "ladder_tier": "Compounded",
    "facts": ["The precise deposition.", "The laser writer.", "Light places life."],
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
