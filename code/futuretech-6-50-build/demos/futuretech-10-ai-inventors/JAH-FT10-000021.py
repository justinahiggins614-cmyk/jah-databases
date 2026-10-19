#!/usr/bin/env python3
"""The AI inventor's first true patent (projection) -- working demonstration.
Record JAH-FT10-000021 [Compounded] from The AI Inventors Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT10-000021",
    "title": "The AI inventor's first true patent (projection)",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 21,
    "ladder_tier": "Compounded",
    "facts": ["No jurisdiction grants AI-only inventorship.", "Legislative change would be required.", "The legal milestone of the ladder."],
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
