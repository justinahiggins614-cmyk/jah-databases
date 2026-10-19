#!/usr/bin/env python3
"""Smart water and waste networks -- working demonstration.
Record JAH-FT11-000015 [Compounded] from The AI That Runs Entire Cities Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT11-000015",
    "title": "Smart water and waste networks",
    "era": "2020s",
    "maturity": "Emerging",
    "ladder_rank": 15,
    "ladder_tier": "Compounded",
    "facts": ["Acoustic sensors find pipe leaks.", "AI routes garbage trucks by fill-level.", "Quiet but widespread deployment."],
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
