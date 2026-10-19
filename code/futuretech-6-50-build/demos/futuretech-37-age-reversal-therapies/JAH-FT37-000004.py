#!/usr/bin/env python3
"""Telomeres and telomerase -- working demonstration.
Record JAH-FT37-000004 [Foundations] from The Age-Reversal Therapies Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT37-000004",
    "title": "Telomeres and telomerase",
    "era": "1984-2009",
    "maturity": "Established",
    "ladder_rank": 4,
    "ladder_tier": "Foundations",
    "facts": ["Nobel Prize 2009.", "The aglet of DNA.", "The end-protection."],
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
