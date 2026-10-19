#!/usr/bin/env python3
"""Magic Leap's billions -- working demonstration.
Record JAH-FT47-000010 [Foundations] from The Everyday AR Glasses Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT47-000010",
    "title": "Magic Leap's billions",
    "era": "2014-2018",
    "maturity": "Established",
    "ladder_rank": 10,
    "ladder_tier": "Foundations",
    "facts": ["$2.6B raised.", "The hype machine.", "The cautionary tale."],
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
