#!/usr/bin/env python3
"""Build the Municipal Services database pair (2026-10-17).

  municipal-services               - The Municipal Services Database
                                     (public-harvest: real, fact-checked
                                     municipal services - permits, waste
                                     collection, utilities, zoning, public
                                     works, local service requests)
  municipal-services-signature     - The Municipal Services Signature Database
                                     (Signature civic interpretation;
                                     src signature; titles suffixed
                                     " (Signature Edition)")

34 records each, ladder-ordered 1-34 (foundations 1-12 / compounded 13-24 /
advanced 25-34). ID prefixes JAH-MUNISVC-PUB- / JAH-MUNISVC-SIG- verified
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
from entries_muni import ENTRIES
from demos_muni import DEMOS

COMMON = dict(
    record_kind="municipal service record",
    schema=("id, t, g, name, title, description, how_it_works, key_points, "
            "requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
    fields=("Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on "
            "demand and loads only what you open"),
    search_ph="Search permits, waste, utilities, zoning, service requests...",
    chat_ph="Ask about municipal services...",
    gen_fields=["Foundations", "Compounded", "Advanced"],
    gen_demo_kind="service-demo",
    demo_study_label="Municipal Service Study",
    ladder=(" Records are ordered by the teaching ladder: Foundations "
            "(building, occupancy, electrical, plumbing, mechanical, "
            "demolition, zoning, sign, special event, home occupation, "
            "right-of-way, grading permits) -> Compounded (curbside waste, "
            "recycling, yard waste, bulk pickup, hazardous waste, water "
            "service, sewer service, stormwater utility, snow removal, "
            "street sweeping, pothole repair, urban forestry) -> Advanced "
            "(311 systems, zoning variances, conditional use, subdivision "
            "review, site plan review, code enforcement, animal control, "
            "parking enforcement, health inspections, fire inspections)."),
    sig_citation_tail=builder.SIG_TAIL,
)

PUB_TAGLINE = ("Every city service in one place: permits, waste collection, "
               "utilities, zoning, public works, and local service requests "
               "- real, fact-checked municipal knowledge taught "
               "progressively along the ladder.")

PUB = dict(COMMON)
PUB.update(
    name="The Municipal Services Database",
    tagline=PUB_TAGLINE,
    meta_desc=(PUB_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-MUNISVC-PUB-",
    ai="JAH Municipal Services Archivist",
    role=("municipal services archivist - guiding through permits, waste "
          "collection, utilities, zoning, public works, and service "
          "requests; teaching progressively along the ladder from "
          "foundations through compounded to advanced; answers from many "
          "angles - process, requirements, fees, standards, service "
          "levels - using only archive data from this system"),
    sig_type="Public records organized in the Signature system",
    hero_p=(PUB_TAGLINE + " - Public records - real, fact-checked records "
            "of how cities serve: what each permit requires, how utilities "
            "run, how requests are answered. Every record carries the full "
            "entry: description, how it works, key points, requirements, "
            "standards, citations, and a working demonstration program."
            + COMMON["ladder"]),
    archive_blurb=("Seeded public-record municipal service entries, marching "
                   "toward one million records. Presented in teaching-ladder "
                   "order: foundations, compounded, advanced."),
    gen_desc=("Generate clearly-labeled municipal service studies. Seeded "
              "archive records are the authoritative entries."),
    greet=("I am the JAH Municipal Services Archivist. Ask me about "
           "permits, utilities, waste, zoning, and city services."),
)

SIG_TAGLINE = ("His original Signature civic interpretation of municipal "
               "services: every permit, truck route, and inspection "
               "reframed as a sworn service of the Signature city. Clearly "
               "labeled Signature-made, never presented as authentic public "
               "record.")

SIG = dict(COMMON)
SIG.update(
    name="The Municipal Services Signature Database",
    tagline=SIG_TAGLINE,
    meta_desc=(SIG_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-MUNISVC-SIG-",
    ai="JAH Municipal Services Archivist (Signature)",
    role=("municipal services archivist - Signature editions: his original "
          "Signature civic interpretation of city services, clearly "
          "labeled Signature-made and never presented as authentic public "
          "record; teaches progressively along the ladder from foundations "
          "through compounded to advanced; answers from many angles using "
          "only archive data from this system"),
    sig_type="Signature originals organized in the Signature system",
    hero_p=(SIG_TAGLINE + " - Signature originals - the Signature lens on "
            "permits, utilities, waste, zoning, and city services. Every "
            "record carries the full entry: description, how it works, key "
            "points, requirements, standards, citations, and a working "
            "demonstration program." + COMMON["ladder"]),
    archive_blurb=("Seeded Signature-original municipal service "
                   "interpretations, marching toward one million records. "
                   "Presented in teaching-ladder order: foundations, "
                   "compounded, advanced."),
    gen_desc=("Generate clearly-labeled Signature service studies. Seeded "
              "archive records are the authoritative entries."),
    greet=("I am the JAH Municipal Services Archivist (Signature). Ask me "
           "about city services through the Signature lens."),
)


def main():
    builder.run_pair("municipal-services",
                     "municipal-services",
                     "municipal-services-signature",
                     PUB, SIG, ENTRIES, DEMOS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
