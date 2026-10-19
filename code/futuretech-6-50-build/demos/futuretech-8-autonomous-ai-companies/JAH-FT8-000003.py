#!/usr/bin/env python3
"""Computers enter the office -- working demonstration.
Record JAH-FT8-000003 [Foundations] from The Autonomous AI Companies Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT8-000003",
    "title": "Computers enter the office",
    "era": "1954-1964",
    "maturity": "Established",
    "ladder_rank": 3,
    "ladder_tier": "Foundations",
    "facts": ["GE's UNIVAC payroll run in 1954.", "IBM System/360 (1964) standardized business computing.", "Automation of white-collar routine work began."],
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
