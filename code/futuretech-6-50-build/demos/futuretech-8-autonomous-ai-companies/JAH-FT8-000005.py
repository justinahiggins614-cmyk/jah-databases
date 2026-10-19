#!/usr/bin/env python3
"""Spreadsheets: VisiCalc and Lotus 1-2-3 -- working demonstration.
Record JAH-FT8-000005 [Foundations] from The Autonomous AI Companies Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT8-000005",
    "title": "Spreadsheets: VisiCalc and Lotus 1-2-3",
    "era": "1979-1983",
    "maturity": "Established",
    "ladder_rank": 5,
    "ladder_tier": "Foundations",
    "facts": ["VisiCalc launched 1979 for the Apple II.", "Lotus 1-2-3 (1983) drove IBM PC adoption.", "One person could do the work of a whole accounting team."],
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
