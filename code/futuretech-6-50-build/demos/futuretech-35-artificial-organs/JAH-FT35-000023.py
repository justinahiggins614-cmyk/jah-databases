#!/usr/bin/env python3
"""The trachea scandal: a warning -- working demonstration.
Record JAH-FT35-000023 [Compounded] from The Artificial Organs Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT35-000023",
    "title": "The trachea scandal: a warning",
    "era": "2008-2016",
    "maturity": "Established",
    "ladder_rank": 23,
    "ladder_tier": "Compounded",
    "facts": ["Karolinska scandal.", "Retractions and convictions.", "The cautionary record."],
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
