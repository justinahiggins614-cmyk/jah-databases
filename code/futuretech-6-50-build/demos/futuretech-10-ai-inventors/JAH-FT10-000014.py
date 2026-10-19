#!/usr/bin/env python3
"""AI chip design in production -- working demonstration.
Record JAH-FT10-000014 [Compounded] from The AI Inventors Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT10-000014",
    "title": "AI chip design in production",
    "era": "2021-2024",
    "maturity": "Established",
    "ladder_rank": 14,
    "ladder_tier": "Compounded",
    "facts": ["Google's floorplanning RL used for TPU generations.", "Faster design cycles reported.", "AI inventing the hardware it runs on."],
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
