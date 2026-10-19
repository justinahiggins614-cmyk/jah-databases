#!/usr/bin/env python3
"""Silent speech for everyone -- working demonstration.
Record JAH-FT27-000024 [Advanced] from The Thought-to-Text Communication Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT27-000024",
    "title": "Silent speech for everyone",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 24,
    "ladder_tier": "Advanced",
    "facts": ["NASA's subvocal research, 2000s.", "Throat sensors as the path.", "The quiet milestone."],
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
