#!/usr/bin/env python3
"""Frontier labs name superintelligence the goal -- working demonstration.
Record JAH-FT6-000023 [Compounded] from The AI Superintelligence Future Technology Database.
Property of Justin Addam Higgins (JAH). Maturity: Emerging.
"""
record = {
    "id": "JAH-FT6-000023",
    "title": "Frontier labs name superintelligence the goal",
    "era": "2023-2025",
    "maturity": "Emerging",
    "ladder_rank": 23,
    "ladder_tier": "Compounded",
    "facts": ["OpenAI's charter targets AGI that benefits humanity.", "SSI Inc. was founded in 2024 focused on safe superintelligence.", "Anthropic's public essays project continued capability gains."],
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
