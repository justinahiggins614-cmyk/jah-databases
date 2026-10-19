#!/usr/bin/env python3
"""Ocean drone fleets -- working demonstration.
Record JAH-FT18-000015 [Compounded] from The Autonomous Robot Swarms Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT18-000015",
    "title": "Ocean drone fleets",
    "era": "2010s-2020s",
    "maturity": "Established",
    "ladder_rank": 15,
    "ladder_tier": "Compounded",
    "facts": ["Saildrone's hurricane missions.", "Wave Gliders crossing oceans.", "The sea's robot swarm."],
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
