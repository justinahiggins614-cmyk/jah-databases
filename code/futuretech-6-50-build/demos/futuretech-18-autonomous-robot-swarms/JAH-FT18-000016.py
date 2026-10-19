#!/usr/bin/env python3
"""Construction drone surveys -- working demonstration.
Record JAH-FT18-000016 [Compounded] from The Autonomous Robot Swarms Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT18-000016",
    "title": "Construction drone surveys",
    "era": "2015-2023",
    "maturity": "Established",
    "ladder_rank": 16,
    "ladder_tier": "Compounded",
    "facts": ["Skycatch and DroneDeploy.", "Daily 3D site models.", "The eye of the building swarm."],
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
