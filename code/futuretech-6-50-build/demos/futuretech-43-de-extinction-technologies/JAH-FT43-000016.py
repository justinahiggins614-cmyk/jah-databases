#!/usr/bin/env python3
"""Coral and seed banks -- working demonstration.
Record JAH-FT43-000016 [Compounded] from The De-Extinction Technologies Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT43-000016",
    "title": "Coral and seed banks",
    "era": "1970s-2000s",
    "maturity": "Established",
    "ladder_rank": 16,
    "ladder_tier": "Compounded",
    "facts": ["Svalbard, 2008.", "The backup.", "Prevention first."],
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
