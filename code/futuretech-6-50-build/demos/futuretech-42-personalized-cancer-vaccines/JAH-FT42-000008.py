#!/usr/bin/env python3
"""HPV vaccine: Gardasil -- working demonstration.
Record JAH-FT42-000008 [Foundations] from The Personalized Cancer Vaccines Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT42-000008",
    "title": "HPV vaccine: Gardasil",
    "era": "2006",
    "maturity": "Established",
    "ladder_rank": 8,
    "ladder_tier": "Foundations",
    "facts": ["FDA, 2006.", "Cervical cancer prevented.", "The proof of concept."],
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
