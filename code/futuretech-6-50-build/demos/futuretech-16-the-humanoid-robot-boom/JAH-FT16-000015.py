#!/usr/bin/env python3
"""Humanoid pilots multiply -- working demonstration.
Record JAH-FT16-000015 [Compounded] from The The Humanoid Robot Boom Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT16-000015",
    "title": "Humanoid pilots multiply",
    "era": "2024-2025",
    "maturity": "Emerging",
    "ladder_rank": 15,
    "ladder_tier": "Compounded",
    "facts": ["Mercedes, BMW, Amazon trials.", "Tasks: totes, parts, sorting.", "Pilots, not production \u2014 yet."],
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
