#!/usr/bin/env python3
"""Neuralink's first human implant -- working demonstration.
Record JAH-FT26-000013 [Compounded] from The Brain-Computer Interfaces Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT26-000013",
    "title": "Neuralink's first human implant",
    "era": "2024",
    "maturity": "Established",
    "ladder_rank": 13,
    "ladder_tier": "Compounded",
    "facts": ["January 2024.", "Cursor control demonstrated.", "The high-bandwidth bet."],
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
