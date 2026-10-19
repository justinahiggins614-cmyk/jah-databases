#!/usr/bin/env python3
"""Boston Dynamics Atlas: the athlete -- working demonstration.
Record JAH-FT16-000009 [Foundations] from The The Humanoid Robot Boom Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT16-000009",
    "title": "Boston Dynamics Atlas: the athlete",
    "era": "2013-2023",
    "maturity": "Established",
    "ladder_rank": 9,
    "ladder_tier": "Foundations",
    "facts": ["Acquired by Google 2013; Hyundai 2021.", "Backflips (2017), parkour (2021).", "Redefined what humanoids could do."],
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
