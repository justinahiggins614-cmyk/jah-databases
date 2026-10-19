#!/usr/bin/env python3
"""Disney animatronics -- working demonstration.
Record JAH-FT17-000007 [Foundations] from The Humanlike Androids Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT17-000007",
    "title": "Disney animatronics",
    "era": "1963-1964",
    "maturity": "Established",
    "ladder_rank": 7,
    "ladder_tier": "Foundations",
    "facts": ["Enchanted Tiki Room, 1963.", "Lincoln at the 1964 World's Fair.", "Entertainment androids' birth."],
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
