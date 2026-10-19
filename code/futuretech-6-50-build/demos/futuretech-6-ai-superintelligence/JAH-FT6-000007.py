#!/usr/bin/env python3
"""Deep Blue defeats Kasparov -- working demonstration.
Record JAH-FT6-000007 [Foundations] from The AI Superintelligence Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT6-000007",
    "title": "Deep Blue defeats Kasparov",
    "era": "1997",
    "maturity": "Established",
    "ladder_rank": 7,
    "ladder_tier": "Foundations",
    "facts": ["Searched about 200 million chess positions per second.", "First machine to beat a reigning world champion in a match.", "Showed search plus heuristics could master a deep intellectual game."],
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
