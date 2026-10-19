#!/usr/bin/env python3
"""The printing press: media for the masses -- working demonstration.
Record JAH-FT15-000002 [Foundations] from The AI-Powered Personal Reality Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT15-000002",
    "title": "The printing press: media for the masses",
    "era": "1440",
    "maturity": "Established",
    "ladder_rank": 2,
    "ladder_tier": "Foundations",
    "facts": ["Movable type, circa 1440.", "Books became affordable.", "Mass media began; personalization waited centuries."],
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
