#!/usr/bin/env python3
"""Sensorama -- working demonstration.
Record JAH-FT46-000004 [Foundations] from The Fully Immersive Virtual Worlds Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT46-000004",
    "title": "Sensorama",
    "era": "1962",
    "maturity": "Established",
    "ladder_rank": 4,
    "ladder_tier": "Foundations",
    "facts": ["1962.", "Sight, sound, smell, vibration.", "The experience machine."],
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
