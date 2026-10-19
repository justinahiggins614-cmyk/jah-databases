#!/usr/bin/env python3
"""The religion question -- working demonstration.
Record JAH-FT34-000030 [Advanced] from The Mind Uploading Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT34-000030",
    "title": "The religion question",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 30,
    "ladder_tier": "Advanced",
    "facts": ["Diverse theological responses.", "The cultural record.", "Belief meets the copy."],
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
