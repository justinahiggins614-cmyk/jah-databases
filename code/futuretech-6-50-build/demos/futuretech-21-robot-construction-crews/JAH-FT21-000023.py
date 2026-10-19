#!/usr/bin/env python3
"""Robot crews for skyscrapers -- working demonstration.
Record JAH-FT21-000023 [Compounded] from The Robot Construction Crews Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT21-000023",
    "title": "Robot crews for skyscrapers",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 23,
    "ladder_tier": "Compounded",
    "facts": ["Shimizu's system was the preview.", "Safety at height is the win.", "The vertical milestone."],
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
