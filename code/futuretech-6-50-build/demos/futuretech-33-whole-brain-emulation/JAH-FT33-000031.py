#!/usr/bin/env python3
"""Scanning the living brain -- working demonstration.
Record JAH-FT33-000031 [Advanced] from The Whole-Brain Emulation Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT33-000031",
    "title": "Scanning the living brain",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 31,
    "ladder_tier": "Advanced",
    "facts": ["Current methods destroy tissue.", "The scanning milestone.", "The gentle map."],
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
