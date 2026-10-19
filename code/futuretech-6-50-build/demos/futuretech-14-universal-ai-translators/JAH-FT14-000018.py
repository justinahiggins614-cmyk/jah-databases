#!/usr/bin/env python3
"""Whale song structure mapped -- working demonstration.
Record JAH-FT14-000018 [Compounded] from The Universal AI Translators Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT14-000018",
    "title": "Whale song structure mapped",
    "era": "2023",
    "maturity": "Emerging",
    "ladder_rank": 18,
    "ladder_tier": "Compounded",
    "facts": ["Sperm whale codas show phonetic-like structure.", "Published in Nature Communications (2024).", "A step toward understanding, not talking."],
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
