#!/usr/bin/env python3
"""The Diving Bell and the Butterfly -- working demonstration.
Record JAH-FT27-000002 [Foundations] from The Thought-to-Text Communication Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT27-000002",
    "title": "The Diving Bell and the Butterfly",
    "era": "1997",
    "maturity": "Established",
    "ladder_rank": 2,
    "ladder_tier": "Foundations",
    "facts": ["Published 1997.", "One eyelid, one alphabet.", "The human will to speak."],
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
