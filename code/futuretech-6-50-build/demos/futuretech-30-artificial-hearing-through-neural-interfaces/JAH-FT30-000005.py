#!/usr/bin/env python3
"""Digital hearing aids -- working demonstration.
Record JAH-FT30-000005 [Foundations] from The Artificial Hearing Through Neural Interfaces Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT30-000005",
    "title": "Digital hearing aids",
    "era": "1980s-1996",
    "maturity": "Established",
    "ladder_rank": 5,
    "ladder_tier": "Foundations",
    "facts": ["Nicolet's Phoenix, 1987.", "Widex Senso, 1996: fully digital.", "Sound, computed."],
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
