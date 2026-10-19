#!/usr/bin/env python3
"""Telepathic consent protocols -- working demonstration.
Record JAH-FT31-000028 [Advanced] from The Digital Telepathy Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT31-000028",
    "title": "Telepathic consent protocols",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 28,
    "ladder_tier": "Advanced",
    "facts": ["Consent must be explicit.", "The legal record.", "Knocking before entering."],
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
