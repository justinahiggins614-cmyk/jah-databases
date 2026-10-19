#!/usr/bin/env python3
"""Build the Public Infrastructure Assets database pair (2026-10-17).

  public-infrastructure-assets             - The Public Infrastructure Assets Database
                                             (public-harvest: real, fact-checked
                                             asset register - roads, bridges,
                                             buildings, utilities, condition
                                             ratings, ownership, maintenance)
  public-infrastructure-assets-signature   - The Public Infrastructure Assets Signature Database
                                             (Signature infrastructure
                                             interpretation; src signature;
                                             titles suffixed " (Signature Edition)")

34 records each, ladder-ordered 1-34 (foundations 1-12 / compounded 13-24 /
advanced 25-34). ID prefixes JAH-INFRA-PUB- / JAH-INFRA-SIG- verified free
(zero hits in manifest id_prefix values, exact + substring).

NEVER touches manifest/api/index/README/docs. NEVER commits.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join("/home/hatch/workspace/jah-databases", "code",
                               "civic-gov-common"))
sys.path.insert(0, HERE)
import builder
from entries_infra import ENTRIES
from demos_infra import DEMOS

COMMON = dict(
    record_kind="infrastructure asset record",
    schema=("id, t, g, name, title, description, how_it_works, key_points, "
            "requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
    fields=("Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on "
            "demand and loads only what you open"),
    search_ph="Search assets, condition ratings, bridges, utilities, maintenance...",
    chat_ph="Ask about public infrastructure assets...",
    gen_fields=["Foundations", "Compounded", "Advanced"],
    gen_demo_kind="asset-demo",
    demo_study_label="Infrastructure Asset Study",
    ladder=(" Records are ordered by the teaching ladder: Foundations "
            "(road networks, bridges, water treatment, wastewater, "
            "stormwater, public buildings, parks, street lighting, "
            "traffic signals, sidewalks, parking, solid waste) -> "
            "Compounded (dams, levees, airports, seaports, bus transit, "
            "rail transit, municipal electric, natural gas, broadband, "
            "fire stations, police stations, public hospitals) -> Advanced "
            "(schools, libraries, courthouses, ISO 55000, PASER, NBIS, "
            "lifecycle costing, capital improvement planning, GIS asset "
            "inventories, resilience and climate adaptation)."),
    sig_citation_tail=builder.SIG_TAIL,
)

PUB_TAGLINE = ("The public asset register: roads, bridges, buildings, "
               "utilities, condition ratings, ownership, and maintenance - "
               "real, fact-checked infrastructure knowledge taught "
               "progressively along the ladder.")

PUB = dict(COMMON)
PUB.update(
    name="The Public Infrastructure Assets Database",
    tagline=PUB_TAGLINE,
    meta_desc=(PUB_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-INFRA-PUB-",
    ai="JAH Infrastructure Asset Archivist",
    role=("infrastructure asset archivist - guiding through roads, "
          "bridges, buildings, utilities, condition ratings, ownership, "
          "and maintenance; teaching progressively along the ladder from "
          "foundations through compounded to advanced; answers from many "
          "angles - function, condition, cost, standards, stewardship - "
          "using only archive data from this system"),
    sig_type="Public records organized in the Signature system",
    hero_p=(PUB_TAGLINE + " - Public records - real, fact-checked records "
            "of the assets governments own and maintain: what they are, "
            "how they are rated, what they cost, and how they are kept "
            "serving. Every record carries the full entry: description, "
            "how it works, key points, requirements, standards, citations, "
            "and a working demonstration program." + COMMON["ladder"]),
    archive_blurb=("Seeded public-record infrastructure asset entries, "
                   "marching toward one million records. Presented in "
                   "teaching-ladder order: foundations, compounded, advanced."),
    gen_desc=("Generate clearly-labeled infrastructure asset studies. "
              "Seeded archive records are the authoritative entries."),
    greet=("I am the JAH Infrastructure Asset Archivist. Ask me about "
           "roads, bridges, utilities, condition ratings, and maintenance."),
)

SIG_TAGLINE = ("His original Signature infrastructure interpretation: every "
               "asset reframed as a sworn work of the Signature republic - "
               "covenants of service cast in concrete and steel. Clearly "
               "labeled Signature-made, never presented as authentic public "
               "record.")

SIG = dict(COMMON)
SIG.update(
    name="The Public Infrastructure Assets Signature Database",
    tagline=SIG_TAGLINE,
    meta_desc=(SIG_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-INFRA-SIG-",
    ai="JAH Infrastructure Asset Archivist (Signature)",
    role=("infrastructure asset archivist - Signature editions: his "
          "original Signature infrastructure interpretation of public "
          "assets, clearly labeled Signature-made and never presented as "
          "authentic public record; teaches progressively along the ladder "
          "from foundations through compounded to advanced; answers from "
          "many angles using only archive data from this system"),
    sig_type="Signature originals organized in the Signature system",
    hero_p=(SIG_TAGLINE + " - Signature originals - the Signature lens on "
            "the assets governments own and maintain. Every record "
            "carries the full entry: description, how it works, key "
            "points, requirements, standards, citations, and a working "
            "demonstration program." + COMMON["ladder"]),
    archive_blurb=("Seeded Signature-original infrastructure asset "
                   "interpretations, marching toward one million records. "
                   "Presented in teaching-ladder order: foundations, "
                   "compounded, advanced."),
    gen_desc=("Generate clearly-labeled Signature asset studies. Seeded "
              "archive records are the authoritative entries."),
    greet=("I am the JAH Infrastructure Asset Archivist (Signature). Ask "
           "me about infrastructure through the Signature lens."),
)


def main():
    builder.run_pair("public-infrastructure-assets",
                     "public-infrastructure-assets",
                     "public-infrastructure-assets-signature",
                     PUB, SIG, ENTRIES, DEMOS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
