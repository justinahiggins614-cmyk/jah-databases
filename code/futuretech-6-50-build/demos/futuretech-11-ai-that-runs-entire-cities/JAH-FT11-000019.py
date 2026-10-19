#!/usr/bin/env python3
"""AI urban planners -- working demonstration.
Record JAH-FT11-000019 [Compounded] from The AI That Runs Entire Cities Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT11-000019",
    "title": "AI urban planners",
    "era": "2024",
    "maturity": "Emerging",
    "ladder_rank": 19,
    "ladder_tier": "Compounded",
    "facts": ["Digital twins test plans before building.", "AI generates land-use alternatives.", "Human councils still decide."],
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
