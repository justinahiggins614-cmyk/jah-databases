#!/usr/bin/env python3
"""Cancer vaccines for Lynch syndrome -- working demonstration.
Record JAH-FT42-000025 [Advanced] from The Personalized Cancer Vaccines Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT42-000025",
    "title": "Cancer vaccines for Lynch syndrome",
    "era": "2020s",
    "maturity": "Emerging",
    "ladder_rank": 25,
    "ladder_tier": "Advanced",
    "facts": ["The prevention trial.", "The hereditary milestone.", "Vaccines before tumors."],
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
