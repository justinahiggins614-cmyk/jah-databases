#!/usr/bin/env python3
"""The quantified memory -- working demonstration.
Record JAH-FT28-000024 [Advanced] from The Memory Prosthetics Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT28-000024",
    "title": "The quantified memory",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 24,
    "ladder_tier": "Advanced",
    "facts": ["Forgetting curves, personal.", "The metacognition milestone.", "Knowing what you know."],
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
