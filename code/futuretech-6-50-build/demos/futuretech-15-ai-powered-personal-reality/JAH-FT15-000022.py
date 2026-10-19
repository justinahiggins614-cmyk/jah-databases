#!/usr/bin/env python3
"""The generated sitcom: your cast, your jokes -- working demonstration.
Record JAH-FT15-000022 [Compounded] from The AI-Powered Personal Reality Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT15-000022",
    "title": "The generated sitcom: your cast, your jokes",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 22,
    "ladder_tier": "Compounded",
    "facts": ["Nothing like this exists.", "Humor is AI's hard problem.", "The sitcom that knows you."],
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
