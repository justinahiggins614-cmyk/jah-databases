#!/usr/bin/env python3
"""Direct-to-consumer DNA testing -- working demonstration.
Record JAH-FT36-000024 [Advanced] from The Personalized Gene Editing Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT36-000024",
    "title": "Direct-to-consumer DNA testing",
    "era": "2007",
    "maturity": "Established",
    "ladder_rank": 24,
    "ladder_tier": "Advanced",
    "facts": ["Launched 2007.", "Millions tested.", "The personal genome."],
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
