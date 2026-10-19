#!/usr/bin/env python3
"""Twins that age with you -- working demonstration.
Record JAH-FT12-000023 [Compounded] from The AI Digital Twins of Humans Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT12-000023",
    "title": "Twins that age with you",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 23,
    "ladder_tier": "Compounded",
    "facts": ["People change; static twins go stale.", "Continual learning without forgetting is hard.", "The lifelong twin problem."],
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
