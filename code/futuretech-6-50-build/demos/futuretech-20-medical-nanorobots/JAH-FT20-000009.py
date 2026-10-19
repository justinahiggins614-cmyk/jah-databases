#!/usr/bin/env python3
"""mRNA lipid nanoparticles -- working demonstration.
Record JAH-FT20-000009 [Foundations] from The Medical Nanorobots Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT20-000009",
    "title": "mRNA lipid nanoparticles",
    "era": "2020",
    "maturity": "Established",
    "ladder_rank": 9,
    "ladder_tier": "Foundations",
    "facts": ["Pfizer-BioNTech and Moderna, 2020.", "Billions of doses.", "Nanodelivery at planetary scale."],
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
