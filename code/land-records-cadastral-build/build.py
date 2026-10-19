#!/usr/bin/env python3
"""Build the Land Records Cadastral database pair (2026-10-17).

  land-records-cadastral             - The Land Records Cadastral Database
                                       (public-harvest: real, fact-checked
                                       land records - parcel boundaries,
                                       survey records, land use, ownership
                                       instruments, mapping)
  land-records-cadastral-signature   - The Land Records Cadastral Signature Database
                                       (Signature land interpretation;
                                       src signature; titles suffixed
                                       " (Signature Edition)")

34 records each, ladder-ordered 1-34 (foundations 1-12 / compounded 13-24 /
advanced 25-34). ID prefixes JAH-LANDREC-PUB- / JAH-LANDREC-SIG- verified
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
from entries_landrec import ENTRIES
from demos_landrec import DEMOS

COMMON = dict(
    record_kind="land record",
    schema=("id, t, g, name, title, description, how_it_works, key_points, "
            "requirements, standards, citations, src, ladder_rank, ladder_tier, demo"),
    fields=("Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on "
            "demand and loads only what you open"),
    search_ph="Search parcels, surveys, deeds, easements, mapping...",
    chat_ph="Ask about land records and surveying...",
    gen_fields=["Foundations", "Compounded", "Advanced"],
    gen_demo_kind="parcel-demo",
    demo_study_label="Land Records Study",
    ladder=(" Records are ordered by the teaching ladder: Foundations "
            "(parcel numbers, metes and bounds, the Public Land Survey "
            "System, warranty deeds, quitclaim deeds, title search, survey "
            "monuments, plat maps, easements, liens, zoning, the county "
            "recorder) -> Compounded (Torrens registration, GIS cadastral "
            "mapping, LiDAR, GNSS surveying, total stations, boundary "
            "disputes, adverse possession, mineral rights, water rights, "
            "conservation easements, eminent domain, land trusts) -> "
            "Advanced (FGDC cadastral standard, title insurance and deed "
            "fraud, 3D cadastre, GLO historical records, BLM land records, "
            "digital registries, accuracy classes, surveyor licensing, "
            "datums, disaster recovery)."),
    sig_citation_tail=builder.SIG_TAIL,
)

PUB_TAGLINE = ("The complete cadastre: parcel boundaries, survey records, "
               "land use, ownership instruments, and mapping - real, "
               "fact-checked land-record knowledge taught progressively "
               "along the ladder.")

PUB = dict(COMMON)
PUB.update(
    name="The Land Records Cadastral Database",
    tagline=PUB_TAGLINE,
    meta_desc=(PUB_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-LANDREC-PUB-",
    ai="JAH Land Records Archivist",
    role=("land records archivist - guiding through parcel boundaries, "
          "survey records, land use, ownership instruments, and mapping; "
          "teaching progressively along the ladder from foundations "
          "through compounded to advanced; answers from many angles - "
          "description, evidence, procedure, law, mapping - using only "
          "archive data from this system"),
    sig_type="Public records organized in the Signature system",
    hero_p=(PUB_TAGLINE + " - Public records - real, fact-checked records "
            "of how land is described, divided, recorded, and mapped: "
            "from parcel numbers and deeds through surveys and easements "
            "to digital registries. Every record carries the full entry: "
            "description, how it works, key points, requirements, "
            "standards, citations, and a working demonstration program."
            + COMMON["ladder"]),
    archive_blurb=("Seeded public-record land-record entries, marching "
                   "toward one million records. Presented in teaching-ladder "
                   "order: foundations, compounded, advanced."),
    gen_desc=("Generate clearly-labeled land record studies. Seeded archive "
              "records are the authoritative entries."),
    greet=("I am the JAH Land Records Archivist. Ask me about parcels, "
           "surveys, deeds, easements, and land mapping."),
)

SIG_TAGLINE = ("His original Signature land interpretation: every parcel, "
               "monument, and deed reframed through the Signature land "
               "system - sworn measures and covenants of the ground. "
               "Clearly labeled Signature-made, never presented as "
               "authentic public record.")

SIG = dict(COMMON)
SIG.update(
    name="The Land Records Cadastral Signature Database",
    tagline=SIG_TAGLINE,
    meta_desc=(SIG_TAGLINE + " Property of Justin Addam Higgins."),
    prefix="JAH-LANDREC-SIG-",
    ai="JAH Land Records Archivist (Signature)",
    role=("land records archivist - Signature editions: his original "
          "Signature land interpretation of parcels, surveys, deeds, and "
          "mapping, clearly labeled Signature-made and never presented as "
          "authentic public record; teaches progressively along the ladder "
          "from foundations through compounded to advanced; answers from "
          "many angles using only archive data from this system"),
    sig_type="Signature originals organized in the Signature system",
    hero_p=(SIG_TAGLINE + " - Signature originals - the Signature land "
            "lens on boundaries, surveys, instruments, and maps. Every "
            "record carries the full entry: description, how it works, key "
            "points, requirements, standards, citations, and a working "
            "demonstration program." + COMMON["ladder"]),
    archive_blurb=("Seeded Signature-original land-record interpretations, "
                   "marching toward one million records. Presented in "
                   "teaching-ladder order: foundations, compounded, advanced."),
    gen_desc=("Generate clearly-labeled Signature land studies. Seeded "
              "archive records are the authoritative entries."),
    greet=("I am the JAH Land Records Archivist (Signature). Ask me about "
           "land records through the Signature land lens."),
)


def main():
    builder.run_pair("land-records-cadastral",
                     "land-records-cadastral",
                     "land-records-cadastral-signature",
                     PUB, SIG, ENTRIES, DEMOS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
