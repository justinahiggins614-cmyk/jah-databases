#!/usr/bin/env python3
"""The microbiome and immunotherapy -- working demonstration.
Record JAH-FT42-000026 [Advanced] from The Personalized Cancer Vaccines Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT42-000026",
    "title": "The microbiome and immunotherapy",
    "era": "2015-2020s",
    "maturity": "Emerging",
    "ladder_rank": 26,
    "ladder_tier": "Advanced",
    "facts": ["Science, 2018.", "The inner ally.", "Microbes matter."],
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
