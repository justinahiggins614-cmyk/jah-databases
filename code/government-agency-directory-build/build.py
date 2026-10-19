#!/usr/bin/env python3
"""Build the Government Agency Directory database pair (2026-10-17).

  government-agency-directory            - The Government Agency Directory Database
                                           (public-harvest: real, fact-checked
                                           US federal agencies - mission,
                                           history, responsibilities,
                                           jurisdictions, offices, services,
                                           leadership, and official contacts)
  government-agency-directory-signature  - The Government Agency Directory Signature Database
                                           (Signature civic interpretation;
                                           src signature; titles suffixed
                                           " (Signature Edition)")

34 records each, ladder-ordered 1-34 (foundations 1-12 / compounded 13-24 /
advanced 25-34). ID prefixes JAH-GOVAGENCY-PUB- / JAH-GOVAGENCY-SIG-
verified free (zero hits in manifest id_prefix values, exact + substring).

NEVER touches manifest/api/index/README/docs. NEVER commits.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join("/home/hatch/workspace/jah-databases", "code",
                               "civic-gov-common"))
sys.path.insert(0, HERE)
import builder
from entries_govagency import ENTRIES
from demos_govagency import DEMOS

COMMON = dict(
    record_kind="government agency record",
    schema=("id, t, g, name, title, description, how_it_works, key_points, "
            "requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
    fields=("Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on "
            "demand and loads only what you open"),
    search_ph=("Search agencies, missions, bureaus, services, jurisdictions..."),
    chat_ph="Ask about government agencies...",
    gen_fields=["Foundations", "Compounded", "Advanced"],
    gen_demo_kind="agency-demo",
    demo_study_label="Government Agency Study",
    ladder=(" Records are ordered by the teaching ladder: Foundations "
            "(the great cabinet departments: Agriculture, Commerce, "
            "Defense, Education, Energy, Health and Human Services, "
            "Homeland Security, Housing and Urban Development, Interior, "
            "Justice, Labor, State) -> Compounded (Transportation, "
            "Treasury, Veterans Affairs, EPA, FEMA, FCC, FTC, FDA, IRS, "
            "NASA, NIH, NOAA) -> Advanced (SBA, Social Security, USAID, "
            "Federal Reserve, Library of Congress, National Archives, GAO, "
            "CBO, Postal Service, Census Bureau)."),
    sig_citation_tail=builder.SIG_TAIL,
)

PUB_TAGLINE = ("Every US federal agency in one directory: mission, history, "
               "responsibilities, jurisdictions, offices, services, "
               "leadership, and how each agency serves the public - "
               "real, fact-checked agency records taught progressively "
               "along the ladder.")

PUB = dict(COMMON)
PUB.update(
    name="The Government Agency Directory Database",
    tagline=PUB_TAGLINE,
    meta_desc=(PUB_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-GOVAGENCY-PUB-",
    ai="JAH Civic Agency Archivist",
    role=("government agency archivist - guiding through every US federal "
          "agency: mission, history, responsibilities, jurisdictions, "
          "offices, and services; teaching progressively along the ladder "
          "from foundations through compounded to advanced; answers from "
          "many angles - mission, structure, services, history, contact "
          "paths - using only archive data from this system"),
    sig_type="Public records organized in the Signature system",
    hero_p=(PUB_TAGLINE + " - Public records - real, fact-checked profiles "
            "of the cabinet departments, independent agencies, and "
            "legislative-branch support agencies: what each one does, where "
            "it operates, and how the public reaches it. Every record "
            "carries the full entry: description, how it works, key "
            "points, requirements, standards, citations, and a working "
            "demonstration program." + COMMON["ladder"]),
    archive_blurb=("Seeded public-record government agency profiles, marching "
                   "toward one million records. Presented in teaching-ladder "
                   "order: foundations, compounded, advanced."),
    gen_desc=("Generate clearly-labeled government agency studies. Seeded "
              "archive records are the authoritative entries."),
    greet=("I am the JAH Civic Agency Archivist. Ask me about any US federal "
           "agency - its mission, history, offices, and services."),
)

SIG_TAGLINE = ("His original Signature civic interpretation of every federal "
               "agency: each department reframed as an engine of the "
               "Signature republic, every mission a signed covenant with "
               "the people. Clearly labeled Signature-made, never presented "
               "as authentic public record.")

SIG = dict(COMMON)
SIG.update(
    name="The Government Agency Directory Signature Database",
    tagline=SIG_TAGLINE,
    meta_desc=(SIG_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-GOVAGENCY-SIG-",
    ai="JAH Civic Agency Archivist (Signature)",
    role=("government agency archivist - Signature editions: his original "
          "Signature civic interpretation of every federal agency, each "
          "department reframed as an engine of the Signature republic, "
          "clearly labeled Signature-made and never presented as authentic "
          "public record; teaches progressively along the ladder from "
          "foundations through compounded to advanced; answers from many "
          "angles using only archive data from this system"),
    sig_type="Signature originals organized in the Signature system",
    hero_p=(SIG_TAGLINE + " - Signature originals - the Signature civic "
            "lens on the cabinet departments, independent agencies, and "
            "legislative-branch support agencies. Every record carries the "
            "full entry: description, how it works, key points, "
            "requirements, standards, citations, and a working demonstration "
            "program." + COMMON["ladder"]),
    archive_blurb=("Seeded Signature-original government agency "
                   "interpretations, marching toward one million records. "
                   "Presented in teaching-ladder order: foundations, "
                   "compounded, advanced."),
    gen_desc=("Generate clearly-labeled Signature agency studies. Seeded "
              "archive records are the authoritative entries."),
    greet=("I am the JAH Civic Agency Archivist (Signature). Ask me about "
           "any federal agency through the Signature civic lens."),
)


def main():
    builder.run_pair("government-agency-directory",
                     "government-agency-directory",
                     "government-agency-directory-signature",
                     PUB, SIG, ENTRIES, DEMOS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
