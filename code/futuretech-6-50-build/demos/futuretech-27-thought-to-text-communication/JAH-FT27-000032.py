#!/usr/bin/env python3
"""The working thought-to-text -- working demonstration.
Record JAH-FT27-000032 [Advanced] from The Thought-to-Text Communication Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT27-000032",
    "title": "The working thought-to-text",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 32,
    "ladder_tier": "Advanced",
    "facts": ["This record is the destination, not a description of anything built.", "Speed plus privacy.", "Maturity moves only with verified systems."],
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
