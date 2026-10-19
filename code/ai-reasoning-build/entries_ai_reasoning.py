#!/usr/bin/env python3
"""Aggregate the five content parts + top-ups into ENTRIES: full records.

Brief = (title, focus, steps, worked, measure, pitfall).
Composed record fields: description, how_it_works, key_points,
requirements, standards, citations, sig_lens + demo_key/group/rank/tier.
"""

import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import entries_p1, entries_p2, entries_p3, entries_p4, entries_p5, entries_p6

SIG_TAIL = ("Signature-method record: an original work by Justin Addam "
            "Higgins (JAH), clearly labeled Signature-made and never "
            "presented as authentic public record.")

ABILITIES = {}
for mod in (entries_p1, entries_p2, entries_p3, entries_p4, entries_p5):
    for k, v in mod.ABILITIES.items():
        assert k not in ABILITIES, "dup ability " + k
        ABILITIES[k] = v

# apply removals
for key, titles in entries_p6.REMOVE.items():
    recs = ABILITIES[key]["records"]
    for t in titles:
        recs[:] = [b for b in recs if b[0] != t]

# apply insertions (in listed order)
for key, ins in entries_p6.EXTRA.items():
    recs = ABILITIES[key]["records"]
    for idx, brief in ins:
        recs.insert(min(idx, len(recs)), brief)

ORDER = ["session-memory", "long-term-memory", "episodic-memory",
         "semantic-memory", "procedural-memory", "chain-of-thought",
         "planning-decomposition", "tool-use", "rag-retrieval",
         "summarization", "question-answering", "self-correction",
         "multi-agent", "persona-communication", "code-reasoning",
         "math-reasoning", "multimodal", "working-memory", "explanation",
         "instruction-following", "context-window-management", "negotiation",
         "teaching-explanation", "uncertainty-handling", "united"]
assert set(ORDER) == set(ABILITIES), "order/ability mismatch"

CODES = {"session-memory": "SM", "long-term-memory": "LM",
         "episodic-memory": "EM", "semantic-memory": "SEM",
         "procedural-memory": "PM", "chain-of-thought": "COT",
         "planning-decomposition": "PD", "tool-use": "TU",
         "rag-retrieval": "RAG", "summarization": "SUM",
         "question-answering": "QA", "self-correction": "SC",
         "multi-agent": "MA", "persona-communication": "PC",
         "code-reasoning": "CR", "math-reasoning": "MR", "multimodal": "MM",
         "working-memory": "WM", "explanation": "EX",
         "instruction-following": "IF", "context-window-management": "CW",
         "negotiation": "NEG", "teaching-explanation": "TE",
         "uncertainty-handling": "UH", "united": "UA"}

TIER_OF = lambda r: ("foundations" if r <= 11 else
                     "compounded" if r <= 23 else "advanced")

FIT = ("This record sits on the teaching ladder of its database, "
       "building on earlier records and preparing later ones: each "
       "record is a complete, practical lesson that can be applied "
       "immediately and combined with the others into working systems.")

def compose(key, pos, brief):
    prof = ABILITIES[key]
    title, focus, steps, worked, measure, pitfall = brief
    rank = pos + 1
    tier = TIER_OF(rank)
    group = "%s-%s" % (prof["core"], tier)
    primer = prof["primers"][pos % len(prof["primers"])]
    steps_txt = " ".join("Step %d: %s" % (i + 1, s)
                         for i, s in enumerate(steps))
    description = ("%s %s On the %s rung of the ladder (rank %d of 34), "
                   "it teaches one working piece of the ability: "
                   "concrete enough to practice today, principled enough "
                   "to combine with every other record in this database."
                   % (focus, FIT, tier, rank))
    how = ("%s In practice: %s Worked example: %s Measurement: %s "
           "Failure mode to watch: %s"
           % (primer, steps_txt, worked, measure, pitfall))
    key_points = [
        focus,
        "The working sequence: " + "; ".join(steps[:3]) + ".",
        "How to tell it is working: " + measure,
        "What goes wrong: " + pitfall,
    ]
    requirements = [
        "Practice the working sequence on a real task before considering it learned.",
        measure,
        "Record what worked and what did not; bring the notes to the next record on the ladder.",
    ]
    standards = [
        prof["std"],
        "This record's bar: " + measure,
    ]
    return {
        "demo_key": "%s-%02d" % (CODES[key], rank),
        "name": title,
        "group": group,
        "ladder_rank": rank,
        "ladder_tier": tier,
        "description": description,
        "how_it_works": how,
        "key_points": key_points,
        "requirements": requirements,
        "standards": standards,
        "citations": list(prof["citations"]),
        "sig_lens": prof["sig_lens"],
    }

ENTRIES = {}   # ability key -> list of composed entries
for key in ORDER:
    recs = ABILITIES[key]["records"]
    assert len(recs) == 34, "%s has %d" % (key, len(recs))
    ENTRIES[key] = [compose(key, i, b) for i, b in enumerate(recs)]

ALL = [e for key in ORDER for e in ENTRIES[key]]
assert len(ALL) == 850
assert len({e["demo_key"] for e in ALL}) == 850
