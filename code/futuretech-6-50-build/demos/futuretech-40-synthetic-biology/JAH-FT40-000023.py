#!/usr/bin/env python3
"""The BioBrick registry -- working demonstration.
Record JAH-FT40-000023 [Compounded] from The Synthetic Biology Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT40-000023",
    "title": "The BioBrick registry",
    "era": "2003-2010s",
    "maturity": "Established",
    "ladder_rank": 23,
    "ladder_tier": "Compounded",
    "facts": ["The parts list.", "The open-source bio.", "Lego for genes."],
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
