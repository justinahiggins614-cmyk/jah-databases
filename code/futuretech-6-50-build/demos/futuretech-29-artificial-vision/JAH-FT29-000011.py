#!/usr/bin/env python3
"""PRIMA photovoltaic implant -- working demonstration.
Record JAH-FT29-000011 [Foundations] from The Artificial Vision Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT29-000011",
    "title": "PRIMA photovoltaic implant",
    "era": "2015-2023",
    "maturity": "Emerging",
    "ladder_rank": 11,
    "ladder_tier": "Foundations",
    "facts": ["No wires through the eye.", "Clinical trials ongoing.", "The elegant design."],
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
