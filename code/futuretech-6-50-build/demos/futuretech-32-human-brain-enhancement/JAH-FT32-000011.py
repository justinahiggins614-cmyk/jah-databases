#!/usr/bin/env python3
"""Meditation and mindfulness -- working demonstration.
Record JAH-FT32-000011 [Foundations] from The Human Brain Enhancement Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT32-000011",
    "title": "Meditation and mindfulness",
    "era": "1970s-2010s",
    "maturity": "Established",
    "ladder_rank": 11,
    "ladder_tier": "Foundations",
    "facts": ["MBSR, 1979.", "Attention studies.", "The ancient enhancer, studied."],
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
