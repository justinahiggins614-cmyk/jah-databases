#!/usr/bin/env python3
"""Whole-brain emulation research -- working demonstration.
Record JAH-FT34-000012 [Foundations] from The Mind Uploading Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT34-000012",
    "title": "Whole-brain emulation research",
    "era": "2020s",
    "maturity": "Emerging",
    "ladder_rank": 12,
    "ladder_tier": "Foundations",
    "facts": ["The WBE link.", "The technical path.", "Copy before transfer."],
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
