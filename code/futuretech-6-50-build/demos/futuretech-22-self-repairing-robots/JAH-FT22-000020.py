#!/usr/bin/env python3
"""Voyager: 45 years of workarounds -- working demonstration.
Record JAH-FT22-000020 [Compounded] from The Self-Repairing Robots Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT22-000020",
    "title": "Voyager: 45 years of workarounds",
    "era": "1977-2024",
    "maturity": "Established",
    "ladder_rank": 20,
    "ladder_tier": "Compounded",
    "facts": ["Launched 1977.", "Thruster switches, heater management from Earth.", "The endurance record."],
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
