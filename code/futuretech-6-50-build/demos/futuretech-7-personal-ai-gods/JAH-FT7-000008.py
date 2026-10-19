#!/usr/bin/env python3
"""Google Assistant and the knowledge graph -- working demonstration.
Record JAH-FT7-000008 [Foundations] from The Personal AI Gods Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT7-000008",
    "title": "Google Assistant and the knowledge graph",
    "era": "2016",
    "maturity": "Established",
    "ladder_rank": 8,
    "ladder_tier": "Foundations",
    "facts": ["Launched May 2016 across phones and Home devices.", "Drew on the Knowledge Graph launched in 2012.", "Conversational, context-aware answers became the bar."],
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
