#!/usr/bin/env python3
"""Build the Humanitarian Disaster Relief database pair (2026-10-17).

  humanitarian-disaster-relief             - The Humanitarian Disaster Relief Database
                                             (public-harvest: real, fact-checked
                                             relief knowledge - aid logistics,
                                             shelter, resource coordination,
                                             recovery, needs assessment)
  humanitarian-disaster-relief-signature   - The Humanitarian Disaster Relief Signature Database
                                             (Signature relief interpretation;
                                             src signature; titles suffixed
                                             " (Signature Edition)")

34 records each, ladder-ordered 1-34 (foundations 1-12 / compounded 13-24 /
advanced 25-34). ID prefixes JAH-HUMRELIEF-PUB- / JAH-HUMRELIEF-SIG- verified
free (zero hits in manifest id_prefix values, exact + substring).

NEVER touches manifest/api/index/README/docs. NEVER commits.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join("/home/hatch/workspace/jah-databases", "code",
                               "civic-gov-common"))
sys.path.insert(0, HERE)
import builder
from entries_relief import ENTRIES
from demos_relief import DEMOS

COMMON = dict(
    record_kind="disaster relief record",
    schema=("id, t, g, name, title, description, how_it_works, key_points, "
            "requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
    fields=("Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on "
            "demand and loads only what you open"),
    search_ph="Search relief, shelter, logistics, recovery, coordination...",
    chat_ph="Ask about disaster relief and humanitarian aid...",
    gen_fields=["Foundations", "Compounded", "Advanced"],
    gen_demo_kind="relief-demo",
    demo_study_label="Disaster Relief Study",
    ladder=(" Records are ordered by the teaching ladder: Foundations "
            "(declarations, EOCs, incident command, search and rescue, "
            "sheltering, mass feeding, first aid, evacuation, alerts, "
            "damage assessment, CERT, recovery centers) -> Compounded "
            "(supply chains, last-mile logistics, WASH, medical teams, "
            "field hospitals, temporary housing, debris, volunteers, "
            "donations, psychological first aid, animal sheltering, power "
            "restoration) -> Advanced (needs assessment, cluster system, "
            "Sphere standards, cash assistance, early recovery, build back "
            "better, risk reduction, stockpiles, civil-military "
            "coordination, accountability)."),
    sig_citation_tail=builder.SIG_TAIL,
)

PUB_TAGLINE = ("The complete relief guide: aid logistics, shelter, resource "
               "coordination, recovery, and needs assessment - real, "
               "fact-checked humanitarian knowledge taught progressively "
               "along the ladder.")

PUB = dict(COMMON)
PUB.update(
    name="The Humanitarian Disaster Relief Database",
    tagline=PUB_TAGLINE,
    meta_desc=(PUB_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-HUMRELIEF-PUB-",
    ai="JAH Disaster Relief Archivist",
    role=("disaster relief archivist - guiding through aid logistics, "
          "shelter, resource coordination, recovery, and needs assessment; "
          "teaching progressively along the ladder from foundations "
          "through compounded to advanced; answers from many angles - "
          "operations, standards, coordination, humanity - using only "
          "archive data from this system"),
    sig_type="Public records organized in the Signature system",
    hero_p=(PUB_TAGLINE + " - Public records - real, fact-checked records "
            "of how humanity responds when disaster strikes. Every record "
            "carries the full entry: description, how it works, key "
            "points, requirements, standards, citations, and a working "
            "demonstration program." + COMMON["ladder"]),
    archive_blurb=("Seeded public-record disaster relief entries, marching "
                   "toward one million records. Presented in teaching-ladder "
                   "order: foundations, compounded, advanced."),
    gen_desc=("Generate clearly-labeled disaster relief studies. Seeded "
              "archive records are the authoritative entries."),
    greet=("I am the JAH Disaster Relief Archivist. Ask me about aid "
           "logistics, shelter, coordination, and recovery."),
)

SIG_TAGLINE = ("His original Signature relief interpretation: every rescue, "
               "shelter, and supply line reframed as a sworn covenant of "
               "humanity. Clearly labeled Signature-made, never presented "
               "as authentic public record.")

SIG = dict(COMMON)
SIG.update(
    name="The Humanitarian Disaster Relief Signature Database",
    tagline=SIG_TAGLINE,
    meta_desc=(SIG_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-HUMRELIEF-SIG-",
    ai="JAH Disaster Relief Archivist (Signature)",
    role=("disaster relief archivist - Signature editions: his original "
          "Signature relief interpretation of humanitarian response, "
          "clearly labeled Signature-made and never presented as authentic "
          "public record; teaches progressively along the ladder from "
          "foundations through compounded to advanced; answers from many "
          "angles using only archive data from this system"),
    sig_type="Signature originals organized in the Signature system",
    hero_p=(SIG_TAGLINE + " - Signature originals - the Signature lens on "
            "relief: logistics, shelter, coordination, recovery. Every "
            "record carries the full entry: description, how it works, key "
            "points, requirements, standards, citations, and a working "
            "demonstration program." + COMMON["ladder"]),
    archive_blurb=("Seeded Signature-original disaster relief "
                   "interpretations, marching toward one million records. "
                   "Presented in teaching-ladder order: foundations, "
                   "compounded, advanced."),
    gen_desc=("Generate clearly-labeled Signature relief studies. Seeded "
              "archive records are the authoritative entries."),
    greet=("I am the JAH Disaster Relief Archivist (Signature). Ask me "
           "about relief through the Signature lens."),
)


def main():
    builder.run_pair("humanitarian-disaster-relief",
                     "humanitarian-disaster-relief",
                     "humanitarian-disaster-relief-signature",
                     PUB, SIG, ENTRIES, DEMOS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
