#!/usr/bin/env python3
"""The bricklaying robot concept -- working demonstration.
Record JAH-FT21-000005 [Foundations] from The Robot Construction Crews Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT21-000005",
    "title": "The bricklaying robot concept",
    "era": "1960s-1980s",
    "maturity": "Established",
    "ladder_rank": 5,
    "ladder_tier": "Foundations",
    "facts": ["Japanese research programs.", "Bricklaying's irregularity resisted.", "The hard problem named."],
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
