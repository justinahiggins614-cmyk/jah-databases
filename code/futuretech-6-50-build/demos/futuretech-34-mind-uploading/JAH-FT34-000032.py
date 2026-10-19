#!/usr/bin/env python3
"""The working mind upload -- working demonstration.
Record JAH-FT34-000032 [Advanced] from The Mind Uploading Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT34-000032",
    "title": "The working mind upload",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 32,
    "ladder_tier": "Advanced",
    "facts": ["This record is the destination, not a description of anything built.", "Verification is everything.", "Maturity moves only with demonstrated uploads."],
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
