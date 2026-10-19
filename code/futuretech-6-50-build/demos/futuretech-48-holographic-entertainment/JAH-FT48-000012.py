#!/usr/bin/env python3
"""Light-field displays -- working demonstration.
Record JAH-FT48-000012 [Foundations] from The Holographic Entertainment Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT48-000012",
    "title": "Light-field displays",
    "era": "2020s",
    "maturity": "Emerging",
    "ladder_rank": 12,
    "ladder_tier": "Foundations",
    "facts": ["The display milestone.", "The glasses-free 3D.", "Light, complete."],
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
