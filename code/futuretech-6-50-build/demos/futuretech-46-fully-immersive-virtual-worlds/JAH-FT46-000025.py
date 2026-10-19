#!/usr/bin/env python3
"""The holodeck: Star Trek TNG -- working demonstration.
Record JAH-FT46-000025 [Advanced] from The Fully Immersive Virtual Worlds Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT46-000025",
    "title": "The holodeck: Star Trek TNG",
    "era": "1987",
    "maturity": "Established",
    "ladder_rank": 25,
    "ladder_tier": "Advanced",
    "facts": ["1987.", "The cultural blueprint.", "The wish."],
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
