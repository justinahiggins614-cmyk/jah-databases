#!/usr/bin/env python3
"""The organ shortage -- working demonstration.
Record JAH-FT35-000017 [Compounded] from The Artificial Organs Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT35-000017",
    "title": "The organ shortage",
    "era": "2000s-2020s",
    "maturity": "Established",
    "ladder_rank": 17,
    "ladder_tier": "Compounded",
    "facts": ["100,000+ waiting in the US.", "The moral driver.", "Why artificial organs matter."],
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
