#!/usr/bin/env python3
"""Pilot items for pipeline validation (removed after validation)."""

ITEMS = [
 {
  "slug": "db-ultimate-versus",
  "name": "The Ultimate Versus Database",
  "class": "PUBLIC-DATABASE",
  "kind": "versus",
  "record_kind": "versus showdown record",
  "tagline": "Head-to-head showdowns between the great contenders of every field - animals, machines, ideas, and designs - judged on transparent weighted criteria so you can see exactly why the winner won.",
  "ai": "JAH Versus Archivist",
  "role": "versus archivist - staging fair head-to-head showdowns across animals, machines, structures, ideas, and designs; every verdict computed from disclosed weighted criteria, teaching how to judge anything transparently",
  "greet": "I am the JAH Versus Archivist. Name any two contenders and I will stage a fair showdown - or browse the archive's judged matchups.",
  "search_ph": "Search cheetah vs falcon, steel vs titanium, pyramid vs skyscraper...",
  "chat_ph": "Ask who would win any matchup...",
  "gen_desc": "Generate clearly-labeled versus showdowns with transparent criteria. Seeded archive records are the authoritative entries.",
  "cite_pool": "Guinness World Records 2025; standard engineering references (Marks' Standard Handbook for Mechanical Engineers 12th ed.; MatWeb material property data).",
  "gen_kind": "ultimate-versus-study",
  "gen_demo_kind": "ultimate-versus-demo",
  "groups": ["Animal Showdowns", "Machine Showdowns", "Idea & Design Showdowns"],
  "topics": [
   {"t": "Cheetah vs Peregrine Falcon", "g": "Animal Showdowns", "a": "Cheetah", "b": "Peregrine Falcon",
    "n": "The land speed king meets the sky's dive-bomber. One is built for the sprint across open savanna, the other for the stoop - a hunting dive no land animal can touch.",
    "crit": [("Top speed (km/h)", 35, 60, 100), ("Endurance at pace", 25, 85, 45), ("Maneuverability", 25, 80, 75), ("Acceleration", 15, 95, 60)],
    "facts": ["A cheetah reaches 100 km/h in about three seconds.", "A stooping peregrine is the fastest animal on Earth at over 320 km/h.", "Cheetahs must rest after a sprint or risk overheating."],
    "cite": ["National Geographic animal speed references."]},
  ] + [
   {"t": "Placeholder Showdown %d" % i, "g": "Animal Showdowns", "a": "Contender A%d" % i, "b": "Contender B%d" % i,
    "n": "Pilot placeholder narrative for showdown %d." % i,
    "crit": [("Criterion one", 50, 70, 60), ("Criterion two", 50, 55, 65)],
    "facts": ["Pilot fact."], "cite": []} for i in range(2, 35)
  ],
 },
]
