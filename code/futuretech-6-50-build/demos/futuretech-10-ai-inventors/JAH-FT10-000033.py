#!/usr/bin/env python3
"""The invention singularity -- working demonstration.
Record JAH-FT10-000033 [Advanced] from The AI Inventors Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT10-000033",
    "title": "The invention singularity",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 33,
    "ladder_tier": "Advanced",
    "facts": ["The far end of the speculative ladder.", "Whether limits exist is unknown.", "The working version of the whole technology."],
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
