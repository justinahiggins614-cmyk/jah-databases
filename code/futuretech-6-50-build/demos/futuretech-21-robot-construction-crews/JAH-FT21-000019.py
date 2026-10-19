#!/usr/bin/env python3
"""Swarm-built pavilions -- working demonstration.
Record JAH-FT21-000019 [Compounded] from The Robot Construction Crews Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT21-000019",
    "title": "Swarm-built pavilions",
    "era": "2014-2024",
    "maturity": "Emerging",
    "ladder_rank": 19,
    "ladder_tier": "Compounded",
    "facts": ["Termite-inspired builders (2014).", "ETH Zurich's DFAB.", "The swarm mason."],
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
