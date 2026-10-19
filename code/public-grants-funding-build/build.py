#!/usr/bin/env python3
"""Build the Public Grants Funding database pair (2026-10-17).

  public-grants-funding              - The Public Grants Funding Database
                                       (public-harvest: real, fact-checked
                                       grants knowledge - eligibility,
                                       application requirements, funding
                                       periods, awards, reporting)
  public-grants-funding-signature    - The Public Grants Funding Signature Database
                                       (Signature funding interpretation;
                                       src signature; titles suffixed
                                       " (Signature Edition)")

34 records each, ladder-ordered 1-34 (foundations 1-12 / compounded 13-24 /
advanced 25-34). ID prefixes JAH-GRANTFUND-PUB- / JAH-GRANTFUND-SIG- verified
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
from entries_grants import ENTRIES
from demos_grants import DEMOS

COMMON = dict(
    record_kind="grant funding record",
    schema=("id, t, g, name, title, description, how_it_works, key_points, "
            "requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
    fields=("Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on "
            "demand and loads only what you open"),
    search_ph="Search grants, eligibility, applications, awards, reporting...",
    chat_ph="Ask about grants and funding...",
    gen_fields=["Foundations", "Compounded", "Advanced"],
    gen_demo_kind="grant-demo",
    demo_study_label="Grant Funding Study",
    ladder=(" Records are ordered by the teaching ladder: Foundations "
            "(federal grant basics, state grants, formula grants, "
            "discretionary grants, block grants, matching, eligibility, "
            "SAM.gov, UEI, narratives, budgets, indirect rates) -> "
            "Compounded (cost sharing, review and scoring, notices of "
            "award, period of performance, allowable costs, Uniform "
            "Guidance, procurement, subrecipient monitoring, payment "
            "management, continuations, no-cost extensions, carryover) -> "
            "Advanced (single audit, SF-425, performance reporting, "
            "closeout, fraud prevention, program income, equipment "
            "disposition, record retention, debarment checks, direct vs "
            "indirect costs)."),
    sig_citation_tail=builder.SIG_TAIL,
)

PUB_TAGLINE = ("The complete grants guide: eligibility, application "
               "requirements, funding periods, awards, and reporting - "
               "real, fact-checked grants knowledge taught progressively "
               "along the ladder.")

PUB = dict(COMMON)
PUB.update(
    name="The Public Grants Funding Database",
    tagline=PUB_TAGLINE,
    meta_desc=(PUB_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-GRANTFUND-PUB-",
    ai="JAH Grants Funding Archivist",
    role=("grants funding archivist - guiding through eligibility, "
          "applications, funding periods, awards, and reporting; teaching "
          "progressively along the ladder from foundations through "
          "compounded to advanced; answers from many angles - rules, "
          "process, finance, compliance, stewardship - using only archive "
          "data from this system"),
    sig_type="Public records organized in the Signature system",
    hero_p=(PUB_TAGLINE + " - Public records - real, fact-checked records "
            "of how public grants work, from first application to final "
            "audit. Every record carries the full entry: description, how "
            "it works, key points, requirements, standards, citations, "
            "and a working demonstration program." + COMMON["ladder"]),
    archive_blurb=("Seeded public-record grant funding entries, marching "
                   "toward one million records. Presented in teaching-ladder "
                   "order: foundations, compounded, advanced."),
    gen_desc=("Generate clearly-labeled grant funding studies. Seeded "
              "archive records are the authoritative entries."),
    greet=("I am the JAH Grants Funding Archivist. Ask me about grant "
           "eligibility, applications, awards, and reporting."),
)

SIG_TAGLINE = ("His original Signature funding interpretation: every grant "
               "rule reframed as a sworn covenant of public investment. "
               "Clearly labeled Signature-made, never presented as "
               "authentic public record.")

SIG = dict(COMMON)
SIG.update(
    name="The Public Grants Funding Signature Database",
    tagline=SIG_TAGLINE,
    meta_desc=(SIG_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-GRANTFUND-SIG-",
    ai="JAH Grants Funding Archivist (Signature)",
    role=("grants funding archivist - Signature editions: his original "
          "Signature funding interpretation of grants knowledge, clearly "
          "labeled Signature-made and never presented as authentic public "
          "record; teaches progressively along the ladder from foundations "
          "through compounded to advanced; answers from many angles using "
          "only archive data from this system"),
    sig_type="Signature originals organized in the Signature system",
    hero_p=(SIG_TAGLINE + " - Signature originals - the Signature lens on "
            "grants: eligibility, applications, awards, reporting. Every "
            "record carries the full entry: description, how it works, key "
            "points, requirements, standards, citations, and a working "
            "demonstration program." + COMMON["ladder"]),
    archive_blurb=("Seeded Signature-original grant funding interpretations, "
                   "marching toward one million records. Presented in "
                   "teaching-ladder order: foundations, compounded, advanced."),
    gen_desc=("Generate clearly-labeled Signature funding studies. Seeded "
              "archive records are the authoritative entries."),
    greet=("I am the JAH Grants Funding Archivist (Signature). Ask me "
           "about grants through the Signature lens."),
)


def main():
    builder.run_pair("public-grants-funding",
                     "public-grants-funding",
                     "public-grants-funding-signature",
                     PUB, SIG, ENTRIES, DEMOS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
