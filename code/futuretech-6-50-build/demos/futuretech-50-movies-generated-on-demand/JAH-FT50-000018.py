#!/usr/bin/env python3
"""AI actors: the debate -- working demonstration.
Record JAH-FT50-000018 [Compounded] from The Movies Generated on Demand Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT50-000018",
    "title": "AI actors: the debate",
    "era": "2023-2024",
    "maturity": "Emerging",
    "ladder_rank": 18,
    "ladder_tier": "Compounded",
    "facts": ["The 2023 strike.", "The likeness question.", "Faces, contracted."],
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
