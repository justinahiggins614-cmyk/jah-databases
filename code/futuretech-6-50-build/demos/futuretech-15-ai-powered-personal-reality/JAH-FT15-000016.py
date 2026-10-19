#!/usr/bin/env python3
"""AI Dungeon: stories that never end -- working demonstration.
Record JAH-FT15-000016 [Compounded] from The AI-Powered Personal Reality Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Established.
"""
record = {
    "id": "JAH-FT15-000016",
    "title": "AI Dungeon: stories that never end",
    "era": "2019",
    "maturity": "Established",
    "ladder_rank": 16,
    "ladder_tier": "Compounded",
    "facts": ["Latitude's AI Dungeon, 2019.", "Infinite stories from prompts.", "The player co-authors with AI."],
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
