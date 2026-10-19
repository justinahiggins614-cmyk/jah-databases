#!/usr/bin/env python3
"""Roomba: the home swarm of one -- working demonstration.
Record JAH-FT18-000006 [Foundations] from The Autonomous Robot Swarms Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT18-000006",
    "title": "Roomba: the home swarm of one",
    "era": "2002",
    "maturity": "Established",
    "ladder_rank": 6,
    "ladder_tier": "Foundations",
    "facts": ["Launched 2002.", "Random-bounce navigation at first.", "Millions sold."],
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
