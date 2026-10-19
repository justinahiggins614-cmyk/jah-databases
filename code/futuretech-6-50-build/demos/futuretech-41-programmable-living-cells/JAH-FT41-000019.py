#!/usr/bin/env python3
"""Insulin from engineered bacteria -- working demonstration.
Record JAH-FT41-000019 [Compounded] from The Programmable Living Cells Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT41-000019",
    "title": "Insulin from engineered bacteria",
    "era": "1978-1982",
    "maturity": "Established",
    "ladder_rank": 19,
    "ladder_tier": "Compounded",
    "facts": ["Genentech, 1978.", "FDA, 1982.", "The product milestone."],
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
