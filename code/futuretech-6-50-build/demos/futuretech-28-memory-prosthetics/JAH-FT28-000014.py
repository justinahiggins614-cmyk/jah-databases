#!/usr/bin/env python3
"""Closed-loop memory stimulation -- working demonstration.
Record JAH-FT28-000014 [Compounded] from The Memory Prosthetics Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT28-000014",
    "title": "Closed-loop memory stimulation",
    "era": "2018-2023",
    "maturity": "Emerging",
    "ladder_rank": 14,
    "ladder_tier": "Compounded",
    "facts": ["Ezzyat et al., Current Biology.", "State-dependent enhancement.", "Timing is everything."],
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
