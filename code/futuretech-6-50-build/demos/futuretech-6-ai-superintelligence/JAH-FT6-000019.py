#!/usr/bin/env python3
"""Reasoning models: test-time compute -- working demonstration.
Record JAH-FT6-000019 [Compounded] from The AI Superintelligence Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT6-000019",
    "title": "Reasoning models: test-time compute",
    "era": "2024",
    "maturity": "Emerging",
    "ladder_rank": 19,
    "ladder_tier": "Compounded",
    "facts": ["OpenAI o1 arrived September 2024 with RL-trained reasoning.", "Large gains on mathematics and coding benchmarks.", "A new scaling dimension beyond training compute."],
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
