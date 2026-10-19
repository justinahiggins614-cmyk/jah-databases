#!/usr/bin/env python3
"""The domestic servant robot in fiction -- working demonstration.
Record JAH-FT23-000001 [Foundations] from The Robotic Personal Assistants Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT23-000001",
    "title": "The domestic servant robot in fiction",
    "era": "1920-1950",
    "maturity": "Established",
    "ladder_rank": 1,
    "ladder_tier": "Foundations",
    "facts": ["Capek's R.U.R., 1920.", "Asimov's domestic robots.", "The dream defined early."],
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
