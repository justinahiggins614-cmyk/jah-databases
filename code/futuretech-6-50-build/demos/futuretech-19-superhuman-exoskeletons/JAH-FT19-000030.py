#!/usr/bin/env python3
"""NASA X1 and the Robo-Glove -- working demonstration.
Record JAH-FT19-000030 [Advanced] from The Superhuman Exoskeletons Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT19-000030",
    "title": "NASA X1 and the Robo-Glove",
    "era": "2012-2016",
    "maturity": "Established",
    "ladder_rank": 30,
    "ladder_tier": "Advanced",
    "facts": ["X1 exoskeleton unveiled 2012.", "Robo-Glove assisted astronauts and workers.", "Space tech for Earth."],
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
