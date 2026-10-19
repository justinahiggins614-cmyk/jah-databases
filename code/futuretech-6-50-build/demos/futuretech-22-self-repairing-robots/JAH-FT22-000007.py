#!/usr/bin/env python3
"""The Mars rovers' longevity -- working demonstration.
Record JAH-FT22-000007 [Foundations] from The Self-Repairing Robots Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT22-000007",
    "title": "The Mars rovers' longevity",
    "era": "2004-2018",
    "maturity": "Established",
    "ladder_rank": 7,
    "ladder_tier": "Foundations",
    "facts": ["Fault workarounds from Earth.", "Heater and wheel strategies.", "Endurance by ingenuity."],
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
