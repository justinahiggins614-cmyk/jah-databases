#!/usr/bin/env python3
"""HTC Vive and room-scale -- working demonstration.
Record JAH-FT46-000014 [Compounded] from The Fully Immersive Virtual Worlds Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT46-000014",
    "title": "HTC Vive and room-scale",
    "era": "2016",
    "maturity": "Established",
    "ladder_rank": 14,
    "ladder_tier": "Compounded",
    "facts": ["2016.", "Walking in VR.", "The space, real."],
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
