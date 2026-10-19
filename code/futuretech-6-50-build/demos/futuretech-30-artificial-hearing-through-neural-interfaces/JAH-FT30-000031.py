#!/usr/bin/env python3
"""The signing-stealing debate -- working demonstration.
Record JAH-FT30-000031 [Advanced] from The Artificial Hearing Through Neural Interfaces Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT30-000031",
    "title": "The signing-stealing debate",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 31,
    "ladder_tier": "Advanced",
    "facts": ["The community's voice matters.", "Choice, not mandate.", "The cultural record."],
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
