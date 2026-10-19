#!/usr/bin/env python3
"""Ishiguro's Geminoid -- working demonstration.
Record JAH-FT17-000011 [Foundations] from The Humanlike Androids Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT17-000011",
    "title": "Ishiguro's Geminoid",
    "era": "2006",
    "maturity": "Established",
    "ladder_rank": 11,
    "ladder_tier": "Foundations",
    "facts": ["Geminoid HI-1, 2006.", "Teleoperated twin.", "The researcher as his own subject."],
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
