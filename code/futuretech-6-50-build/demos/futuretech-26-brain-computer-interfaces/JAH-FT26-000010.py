#!/usr/bin/env python3
"""Motor imagery BCIs -- working demonstration.
Record JAH-FT26-000010 [Foundations] from The Brain-Computer Interfaces Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT26-000010",
    "title": "Motor imagery BCIs",
    "era": "1990s-2000s",
    "maturity": "Established",
    "ladder_rank": 10,
    "ladder_tier": "Foundations",
    "facts": ["Graz BCI competitions.", "Rehab applications.", "Thinking it moves it."],
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
