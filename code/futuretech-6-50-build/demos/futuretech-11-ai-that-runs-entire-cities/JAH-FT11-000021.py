#!/usr/bin/env python3
"""Algorithmic congestion pricing -- working demonstration.
Record JAH-FT11-000021 [Compounded] from The AI That Runs Entire Cities Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT11-000021",
    "title": "Algorithmic congestion pricing",
    "era": "2025",
    "maturity": "Speculative",
    "ladder_rank": 21,
    "ladder_tier": "Compounded",
    "facts": ["Singapore's ERP is the early model.", "AI could price every road segment continuously.", "Equity effects need careful design."],
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
