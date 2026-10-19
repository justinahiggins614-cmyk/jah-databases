#!/usr/bin/env python3
"""The end of misunderstanding -- working demonstration.
Record JAH-FT31-000030 [Advanced] from The Digital Telepathy Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT31-000030",
    "title": "The end of misunderstanding",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 30,
    "ladder_tier": "Advanced",
    "facts": ["Understanding isn't agreement.", "Privacy's final stand.", "The paradox milestone."],
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
