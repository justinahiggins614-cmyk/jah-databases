#!/usr/bin/env python3
"""The working superintelligence: what done looks like -- working demonstration.
Record JAH-FT6-000034 [Advanced] from The AI Superintelligence Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT6-000034",
    "title": "The working superintelligence: what done looks like",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 34,
    "ladder_tier": "Advanced",
    "facts": ["This record is the destination, not a description of anything built.", "Every prior record in this database is a step toward it.", "Maturity will move from speculative only with verified demonstrations."],
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
