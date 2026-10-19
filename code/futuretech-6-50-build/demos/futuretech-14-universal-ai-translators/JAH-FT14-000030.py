#!/usr/bin/env python3
"""Machine translation in crisis response -- working demonstration.
Record JAH-FT14-000030 [Advanced] from The Universal AI Translators Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT14-000030",
    "title": "Machine translation in crisis response",
    "era": "2010s-2020s",
    "maturity": "Established",
    "ladder_rank": 30,
    "ladder_tier": "Advanced",
    "facts": ["Translators Without Borders deployed MT in disasters.", "Haiti 2010 showed the life-saving need.", "Translation as emergency infrastructure."],
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
