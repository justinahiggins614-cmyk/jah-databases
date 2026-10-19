#!/usr/bin/env python3
"""The Human Connectome Project -- working demonstration.
Record JAH-FT33-000019 [Compounded] from The Whole-Brain Emulation Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT33-000019",
    "title": "The Human Connectome Project",
    "era": "2009-2015",
    "maturity": "Established",
    "ladder_rank": 19,
    "ladder_tier": "Compounded",
    "facts": ["1,200 subjects.", "The wiring census.", "The map milestone."],
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
