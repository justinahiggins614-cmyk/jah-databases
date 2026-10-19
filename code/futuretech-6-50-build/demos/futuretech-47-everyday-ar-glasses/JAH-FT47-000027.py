#!/usr/bin/env python3
"""Meta Orion -- working demonstration.
Record JAH-FT47-000027 [Advanced] from The Everyday AR Glasses Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT47-000027",
    "title": "Meta Orion",
    "era": "2024",
    "maturity": "Emerging",
    "ladder_rank": 27,
    "ladder_tier": "Advanced",
    "facts": ["September 2024.", "The neural wristband.", "The research reveal."],
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
