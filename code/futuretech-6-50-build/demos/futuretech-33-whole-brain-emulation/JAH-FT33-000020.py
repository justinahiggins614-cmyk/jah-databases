#!/usr/bin/env python3
"""Zebrafish whole-brain imaging -- working demonstration.
Record JAH-FT33-000020 [Compounded] from The Whole-Brain Emulation Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT33-000020",
    "title": "Zebrafish whole-brain imaging",
    "era": "2013",
    "maturity": "Established",
    "ladder_rank": 20,
    "ladder_tier": "Compounded",
    "facts": ["Nature Methods, 2013.", "80,000 neurons live.", "The transparent milestone."],
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
