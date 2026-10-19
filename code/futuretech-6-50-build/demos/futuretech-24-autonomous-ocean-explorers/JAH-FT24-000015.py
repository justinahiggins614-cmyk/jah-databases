#!/usr/bin/env python3
"""Deep-sea mining prospectors -- working demonstration.
Record JAH-FT24-000015 [Compounded] from The Autonomous Ocean Explorers Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT24-000015",
    "title": "Deep-sea mining prospectors",
    "era": "2010s-2020s",
    "maturity": "Established",
    "ladder_rank": 15,
    "ladder_tier": "Compounded",
    "facts": ["Polymetallic nodules mapped.", "ISA regulates exploration.", "The resource question."],
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
