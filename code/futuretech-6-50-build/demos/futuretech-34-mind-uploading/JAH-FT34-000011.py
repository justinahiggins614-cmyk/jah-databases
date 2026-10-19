#!/usr/bin/env python3
"""Digital immortality startups -- working demonstration.
Record JAH-FT34-000011 [Foundations] from The Mind Uploading Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT34-000011",
    "title": "Digital immortality startups",
    "era": "2010s-2020s",
    "maturity": "Emerging",
    "ladder_rank": 11,
    "ladder_tier": "Foundations",
    "facts": ["Nectome's 2018 prize and controversy.", "The business of forever.", "The commercial edge."],
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
