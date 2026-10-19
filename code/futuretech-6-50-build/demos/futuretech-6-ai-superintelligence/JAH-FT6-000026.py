#!/usr/bin/env python3
"""The intelligence explosion scenario -- working demonstration.
Record JAH-FT6-000026 [Advanced] from The AI Superintelligence Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT6-000026",
    "title": "The intelligence explosion scenario",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 26,
    "ladder_tier": "Advanced",
    "facts": ["Good proposed an ultraintelligent machine could design better machines.", "Takeoff could be slow, fast, or discontinuous \u2014 unknown.", "The scenario is debated, not demonstrated."],
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
