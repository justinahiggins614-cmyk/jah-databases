#!/usr/bin/env python3
"""SpiNNaker: the million-core brain machine -- working demonstration.
Record JAH-FT33-000022 [Compounded] from The Whole-Brain Emulation Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT33-000022",
    "title": "SpiNNaker: the million-core brain machine",
    "era": "2011-2018",
    "maturity": "Emerging",
    "ladder_rank": 22,
    "ladder_tier": "Compounded",
    "facts": ["1 million ARM cores.", "Real-time brain models.", "The hardware path."],
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
