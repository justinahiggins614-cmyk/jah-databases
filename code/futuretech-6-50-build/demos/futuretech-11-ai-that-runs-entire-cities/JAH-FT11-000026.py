#!/usr/bin/env python3
"""City AI and democratic oversight -- working demonstration.
Record JAH-FT11-000026 [Advanced] from The AI That Runs Entire Cities Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Speculative.
"""
record = {
    "id": "JAH-FT11-000026",
    "title": "City AI and democratic oversight",
    "era": "2025+",
    "maturity": "Speculative",
    "ladder_rank": 26,
    "ladder_tier": "Advanced",
    "facts": ["Algorithmic transparency laws are early.", "Participatory budgeting hints at the model.", "Legitimacy is the binding constraint."],
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
