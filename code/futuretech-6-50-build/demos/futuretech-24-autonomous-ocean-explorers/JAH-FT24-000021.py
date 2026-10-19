#!/usr/bin/env python3
"""The Ocean Census: 100,000 species -- working demonstration.
Record JAH-FT24-000021 [Compounded] from The Autonomous Ocean Explorers Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT24-000021",
    "title": "The Ocean Census: 100,000 species",
    "era": "2023",
    "maturity": "Emerging",
    "ladder_rank": 21,
    "ladder_tier": "Compounded",
    "facts": ["Launched 2023 by Nekton and Oxford.", "Expeditions plus eDNA.", "Discovery at industrial scale."],
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
