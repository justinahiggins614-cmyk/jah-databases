#!/usr/bin/env python3
"""Human-robot construction teams -- working demonstration.
Record JAH-FT21-000031 [Advanced] from The Robot Construction Crews Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT21-000031",
    "title": "Human-robot construction teams",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 31,
    "ladder_tier": "Advanced",
    "facts": ["Centaur construction.", "Craft plus machine.", "The collaboration milestone."],
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
