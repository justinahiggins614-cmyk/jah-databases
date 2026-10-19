#!/usr/bin/env python3
"""The perceptron learns from examples -- working demonstration.
Record JAH-FT6-000004 [Foundations] from The AI Superintelligence Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT6-000004",
    "title": "The perceptron learns from examples",
    "era": "1958",
    "maturity": "Established",
    "ladder_rank": 4,
    "ladder_tier": "Foundations",
    "facts": ["Frank Rosenblatt built the Mark I perceptron.", "Minsky and Papert's 1969 critique slowed neural network research.", "The core ideas returned decades later in deep learning."],
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
