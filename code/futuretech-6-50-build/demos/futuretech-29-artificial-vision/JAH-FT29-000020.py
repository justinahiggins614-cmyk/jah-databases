#!/usr/bin/env python3
"""BrainPort: seeing with the tongue -- working demonstration.
Record JAH-FT29-000020 [Compounded] from The Artificial Vision Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT29-000020",
    "title": "BrainPort: seeing with the tongue",
    "era": "2005-2015",
    "maturity": "Established",
    "ladder_rank": 20,
    "ladder_tier": "Compounded",
    "facts": ["FDA cleared 2015.", "Blind users navigated obstacles.", "The tongue as a display."],
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
