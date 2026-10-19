#!/usr/bin/env python3
"""Wave 5 content: GENERATOR-class items (4). Real working client-side generators."""
import sys, os
sys.path.insert(0, os.path.join(os.path.expanduser("~/workspace/jah-databases"), "code", "wave5-build"))
from lib import register
from gen_custom import GEN_CUSTOM

CITE_GEN = ("Generator and sample records are Signature-made demonstrations of the craft; sample cases "
            "are fictional, clearly labeled, and fully worked.")

# ================================================================ gen-detective-case-generator
register({
 "slug": "gen-detective-case-generator", "name": "The Detective Case Generator",
 "tagline": ("Generate complete new detective cases: victims, suspects, motives, clues, and fair "
             "alibi-elimination solutions - every case solvable."),
 "record_kind": "generated detective case",
 "pub_line": ("Sample detective cases - fully worked fictional cases with fair solutions; the generator "
              "produces genuine new cases on demand."),
 "ai": "JAH Case Generator",
 "role": ("generator of detective cases - creating new solvable mysteries; answering from many angles - "
          "the case, the clues, the solution - using only archive data"),
 "search_ph": "Search manor cases, locked rooms, alibi puzzles...",
 "chat_ph": "Generate a new case...",
 "fields": ["Manor Cases", "Locked Rooms", "Alibi Puzzles"],
 "gen_desc": "Generate genuine new detective cases - victims, suspects, clues, fair solutions. Seeded sample cases are the authoritative entries.",
 "greet": "Every case here is solvable - and the generator makes new ones. Shall we open a case?",
 "gen_kind": "detective-case",
 "citation": CITE_GEN,
 "demo_default": "eliminate",
 "custom_records": GEN_CUSTOM["gen-detective-case-generator"]["records"],
})

# ================================================================ gen-hidden-message-factory
register({
 "slug": "gen-hidden-message-factory", "name": "The Hidden Message Factory",
 "tagline": ("Encode real hidden messages: acrostics, Caesar shifts, rail-fence ciphers, and every-Nth-letter "
             "puzzles - every message genuinely decodable."),
 "record_kind": "hidden message record",
 "pub_line": ("Sample hidden messages - fully worked encodings with real decode logic; the factory "
              "produces genuine new hidden messages on demand."),
 "ai": "JAH Message Encoder",
 "role": ("encoder of hidden messages - creating genuinely decodable puzzles; answering from many angles - "
          "the cover text, the method, the reveal - using only archive data"),
 "search_ph": "Search acrostics, Caesar ciphers, rail fence...",
 "chat_ph": "Encode a message...",
 "fields": ["Acrostics", "Ciphers", "Steganography"],
 "gen_desc": "Encode genuine hidden messages - real acrostic, Caesar, rail-fence, and skip-letter encodings. Seeded sample messages are the authoritative entries.",
 "greet": "Every message here really hides something - and the factory encodes new ones. What shall we hide?",
 "gen_kind": "hidden-message",
 "citation": CITE_GEN,
 "demo_default": "acrostic",
 "custom_records": GEN_CUSTOM["gen-hidden-message-factory"]["records"],
})

# ================================================================ gen-strange-diary
register({
 "slug": "gen-strange-diary", "name": "The Strange Diary Generator",
 "tagline": ("Generate complete strange diaries: dated entries, unreliable narrators, and the truth behind "
             "them - every diary fully written."),
 "record_kind": "generated strange diary",
 "pub_line": ("Sample strange diaries - fully written fictional diaries with six dated entries and the "
              "truth revealed; the generator produces genuine new diaries on demand."),
 "ai": "JAH Diary Keeper",
 "role": ("keeper of strange diaries - writing complete fictional diaries; answering from many angles - "
          "the entries, the narrator, the truth - using only archive data"),
 "search_ph": "Search lighthouse diaries, manor diaries, ship logs...",
 "chat_ph": "Open a new diary...",
 "fields": ["Manor Diaries", "Voyage Logs", "Lighthouse Journals"],
 "gen_desc": "Generate genuine new strange diaries - dated entries, narrators, arcs, and the truth behind them. Seeded sample diaries are the authoritative entries.",
 "greet": "Every diary here is fully written - entries to truth. Shall we open one?",
 "gen_kind": "strange-diary",
 "citation": CITE_GEN,
 "demo_default": "report",
 "custom_records": GEN_CUSTOM["gen-strange-diary"]["records"],
})

# ================================================================ gen-endless-adventure-generator
register({
 "slug": "gen-endless-adventure-generator", "name": "The Endless Adventure Generator",
 "tagline": ("Generate complete adventure frameworks: hooks, locations, characters, twists, and onward "
             "hooks - every adventure playable."),
 "record_kind": "generated adventure framework",
 "pub_line": ("Sample adventure frameworks - fully worked fictional adventures with hooks, twists, and "
              "onward hooks; the generator produces genuine new adventures on demand."),
 "ai": "JAH Adventure Weaver",
 "role": ("weaver of endless adventures - creating complete playable frameworks; answering from many "
          "angles - the hook, the places, the twists - using only archive data"),
 "search_ph": "Search sunken libraries, sky cities, deep roads...",
 "chat_ph": "Weave a new adventure...",
 "fields": ["Quests", "Journeys", "Expeditions"],
 "gen_desc": "Generate genuine new adventure frameworks - themes, hooks, locations, characters, twists, and onward hooks. Seeded sample adventures are the authoritative entries.",
 "greet": "Every adventure here is playable - hook to onward hook. Where shall we go?",
 "gen_kind": "endless-adventure",
 "citation": CITE_GEN,
 "demo_default": "checklist",
 "custom_records": GEN_CUSTOM["gen-endless-adventure-generator"]["records"],
})
