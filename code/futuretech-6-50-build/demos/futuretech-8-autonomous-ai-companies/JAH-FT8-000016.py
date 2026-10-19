#!/usr/bin/env python3
"""The one-person unicorn hypothesis -- working demonstration.
Record JAH-FT8-000016 [Compounded] from The Autonomous AI Companies Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT8-000016",
    "title": "The one-person unicorn hypothesis",
    "era": "2024",
    "maturity": "Emerging",
    "ladder_rank": 16,
    "ladder_tier": "Compounded",
    "facts": ["Sam Altman publicly predicted the one-person unicorn.", "Micro-teams ship products that once needed hundreds.", "No one-person billion-dollar company exists yet."],
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
