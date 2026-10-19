#!/usr/bin/env python3
"""Ultrasound neuromodulation -- working demonstration.
Record JAH-FT31-000010 [Foundations] from The Digital Telepathy Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT31-000010",
    "title": "Ultrasound neuromodulation",
    "era": "2010s-2020s",
    "maturity": "Emerging",
    "ladder_rank": 10,
    "ladder_tier": "Foundations",
    "facts": ["Tyler's 2010 discovery.", "Human trials ongoing.", "The precise writer."],
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
