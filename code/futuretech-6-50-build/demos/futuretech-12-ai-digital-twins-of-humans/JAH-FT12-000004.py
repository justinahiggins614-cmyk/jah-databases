#!/usr/bin/env python3
"""ELIZA and the personal confessional -- working demonstration.
Record JAH-FT12-000004 [Foundations] from The AI Digital Twins of Humans Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT12-000004",
    "title": "ELIZA and the personal confessional",
    "era": "1966",
    "maturity": "Established",
    "ladder_rank": 4,
    "ladder_tier": "Foundations",
    "facts": ["Weizenbaum's program at MIT.", "Users confided personal material.", "The human side of the twin relationship."],
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
