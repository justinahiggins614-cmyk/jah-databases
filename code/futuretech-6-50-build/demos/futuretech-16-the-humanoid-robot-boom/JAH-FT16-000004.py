#!/usr/bin/env python3
"""Honda P2 and the walking breakthrough -- working demonstration.
Record JAH-FT16-000004 [Foundations] from The The Humanoid Robot Boom Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT16-000004",
    "title": "Honda P2 and the walking breakthrough",
    "era": "1996",
    "maturity": "Established",
    "ladder_rank": 4,
    "ladder_tier": "Foundations",
    "facts": ["Secret E0-P2 program since 1986.", "P2 unveiled 1996; ASIMO 2000.", "Stable bipedal walking solved."],
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
