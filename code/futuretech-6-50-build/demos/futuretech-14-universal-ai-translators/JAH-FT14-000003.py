#!/usr/bin/env python3
"""Esperanto: the constructed bridge -- working demonstration.
Record JAH-FT14-000003 [Foundations] from The Universal AI Translators Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT14-000003",
    "title": "Esperanto: the constructed bridge",
    "era": "1887",
    "maturity": "Established",
    "ladder_rank": 3,
    "ladder_tier": "Foundations",
    "facts": ["Unua Libro, 1887.", "Up to 2 million speakers at peak estimates.", "The constructed-language path to universality."],
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
