#!/usr/bin/env python3
"""Build the Apex-Reality + Made-With databases for JAH Databases (Manon's orders).

Six databases, 34 full records each (204 total):

  apex-reality-computer            - The Apex-Reality Computer Concept Database
  apex-reality-computer-signature  - The Apex-Reality Computer Signature Database
  apex-reality-federation          - The Apex-Reality Federation Concept Database
  apex-reality-federation-signature- The Apex-Reality Federation Signature Database
  made-with-databases              - The Made-With Databases Archive
  made-with-databases-signature    - The Made-With Databases Signature Archive

ABSOLUTE HONESTY RULE (Manon's canon): everything Apex-Reality is built as
SIGNATURE CONCEPT - speculative throughout, labeled as concept/design on
every record and in every demo, NEVER presented as proven real-world fact
or a real starship. Branding: Justin Addam Higgins, A7 Signature Dominion.

The computer pages get a working interactive console demo (concept simulator).
The federation pages get an interactive Federation Registry (name yourself +
your starship with uniqueness checking, ship parameters, patent-style
blueprint, ship AI persona, registry entry, inter-ship comms, shared mission
database, unified A7 control layer) - all labeled concept experience.

No Facebook, no YouTube, no website references anywhere. No manifest/api.json
writes (the coordinator merges).
"""
import gzip
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

spec = importlib.util.spec_from_file_location(
    "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
nb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nb)

sspec = importlib.util.spec_from_file_location(
    "sweep", "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py")
sweep = importlib.util.module_from_spec(sspec)
sspec.loader.exec_module(sweep)

OWNER = "Justin Addam Higgins"
SPEC_TAG = ("SPECULATIVE CONCEPT - a Signature concept design by Justin Addam "
            "Higgins (A7 Signature Dominion). Not a proven real-world fact. "
            "Not a real starship.")

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, hero_p, sig_type,
         source, fields, gen_desc, greet):
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role, "hero_p": hero_p,
        "sig_type": sig_type,
        "search_ph": "Search %s..." % record_kind,
        "chat_ph": "Ask about %s..." % record_kind,
        "archive_blurb": "Seeded %s %s, marching toward one million records." % (
            "Signature-original" if source == "signature" else "concept-design", record_kind),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, "
                   "requirements, standards, citations, src, ladder_rank, ladder_tier, "
                   "demo, provenance, last_verified"),
        "fields": " · ".join(fields),
        "gen_desc": gen_desc,
        "greet": greet,
        "gen_fields": fields, "gen_kind": slug, "gen_demo_kind": "python",
        "source": source,
    }

CONCEPT_SIG = "Signature concept designs (speculative) organized in the Signature system"
SIG_ORIG = "Signature originals organized in the Signature system"
PUB_REC = "Public records organized in the Signature system"

COMPUTER_HERO = ("His Signature systems as concept designs: the JAH-UALNS number line, "
    "the AUA-JM2 protocol, plasma/light/void nanobot systems, portal theory, "
    "the warp console, the reality bridge, and the time-aware memory engine. "
    "Every record is a full concept file: description, how the concept works, "
    "key points, requirements, and a working concept-simulation program. ")
COMPUTER_HERO_PUB = (COMPUTER_HERO + SPEC_TAG)
COMPUTER_HERO_SIG = (COMPUTER_HERO +
    "Signature-stamped edition: the A7 Signature Dominion's own design writeups, "
    "in his voice, every file carrying the Signature mark. " + SPEC_TAG)

FED_HERO = ("The multi-user concept layer: name yourself and your starship, enter "
    "ship parameters, receive a patent-style blueprint and a personalized ship AI "
    "persona, and take your place in the Federation registry - with inter-ship "
    "comms, a shared mission database, and the unified A7 control layer. ")
FED_HERO_PUB = (FED_HERO + SPEC_TAG)
FED_HERO_SIG = (FED_HERO +
    "Signature-stamped edition: the A7 Signature Dominion's own registry canon. "
    + SPEC_TAG)

MW_HERO = ("New things created USING the network's databases get archived here: "
    "what was made, which databases were used, and the result. Every record is a "
    "full creation file: description, how it was built, key points, requirements, "
    "and a working demonstration program.")
MW_HERO_SIG = (MW_HERO + " Signature-stamped edition: his own telling of what the "
    "network has made, every file carrying the Signature mark.")

DBCFG = {
 "apex-reality-computer": _cfg(
    "apex-reality-computer", "The Apex-Reality Computer Concept Database",
    "Signature concept designs for the Apex-Reality Computer: number line, protocol, nanobots, portals, warp, memory.",
    "apex-reality concept file", "JAH-APX-",
    "JAH Apex-Reality Archivist", "apex-reality archivist - signature concept systems",
    COMPUTER_HERO_PUB, CONCEPT_SIG, "public",
    ["core-concepts", "systems-integration", "apex-engineering"],
    "Generate clearly-labeled structural concept studies. Seeded archive records are the authoritative entries.",
    "I am the JAH Apex-Reality Archivist. Ask me about the Apex-Reality concept systems."),
 "apex-reality-computer-signature": _cfg(
    "apex-reality-computer-signature", "The Apex-Reality Computer Signature Database",
    "The Signature-stamped Apex-Reality concept designs, in his voice, under the A7 Signature Dominion.",
    "apex-reality concept file", "JAH-APXG-",
    "JAH Apex-Reality Archivist (Signature)", "apex-reality archivist - signature concept systems, Signature editions",
    COMPUTER_HERO_SIG, SIG_ORIG, "signature",
    ["core-concepts", "systems-integration", "apex-engineering"],
    "Generate clearly-labeled structural concept studies. Seeded archive records are the authoritative entries.",
    "I am the JAH Apex-Reality Archivist, Signature edition. Ask me about the Apex-Reality concept systems."),
 "apex-reality-federation": _cfg(
    "apex-reality-federation", "The Apex-Reality Federation Concept Database",
    "The multi-user concept layer: ship registry, blueprints, ship AI personas, fleet comms, missions, A7 command.",
    "federation concept file", "JAH-AFD-",
    "JAH Federation Registrar", "federation registrar - ship registry and fleet systems",
    FED_HERO_PUB, CONCEPT_SIG, "public",
    ["federation-core", "fleet-systems", "a7-command"],
    "Generate clearly-labeled structural concept studies. Seeded archive records are the authoritative entries.",
    "I am the JAH Federation Registrar. Ask me about the Federation concept systems."),
 "apex-reality-federation-signature": _cfg(
    "apex-reality-federation-signature", "The Apex-Reality Federation Signature Database",
    "The Signature-stamped Federation registry canon of the A7 Signature Dominion.",
    "federation concept file", "JAH-AFDG-",
    "JAH Federation Registrar (Signature)", "federation registrar - fleet systems, Signature editions",
    FED_HERO_SIG, SIG_ORIG, "signature",
    ["federation-core", "fleet-systems", "a7-command"],
    "Generate clearly-labeled structural concept studies. Seeded archive records are the authoritative entries.",
    "I am the JAH Federation Registrar, Signature edition. Ask me about the Federation concept systems."),
 "made-with-databases": _cfg(
    "made-with-databases", "The Made-With Databases Archive",
    "Things made using the network databases: what was made, which databases were used, and the result.",
    "made-with creation file", "JAH-MW-",
    "JAH Made-With Curator", "made-with curator - creations built on the network databases",
    MW_HERO, PUB_REC, "public",
    ["network-builds", "user-creations", "signature-works"],
    "Generate clearly-labeled structural creation studies. Seeded archive records are the authoritative entries.",
    "I am the JAH Made-With Curator. Ask me about things made with the network databases."),
 "made-with-databases-signature": _cfg(
    "made-with-databases-signature", "The Made-With Databases Signature Archive",
    "His own telling of what the network has made, Signature-stamped.",
    "made-with creation file", "JAH-MWG-",
    "JAH Made-With Curator (Signature)", "made-with curator - network creations, Signature editions",
    MW_HERO_SIG, SIG_ORIG, "signature",
    ["network-builds", "user-creations", "signature-works"],
    "Generate clearly-labeled structural creation studies. Seeded archive records are the authoritative entries.",
    "I am the JAH Made-With Curator, Signature edition. Ask me about things made with the network databases."),
}
nb.DBCFG = DBCFG

SLUGS = ["apex-reality-computer", "apex-reality-computer-signature",
         "apex-reality-federation", "apex-reality-federation-signature",
         "made-with-databases", "made-with-databases-signature"]

# ---------------------------------------------------------------- helpers

def _q(s):
    return json.dumps(s)


def _hdr_concept(name, rid, group):
    return ('#!/usr/bin/env python3\n"""' + name.replace('"""', '"') + ' — concept simulation demo.\n'
            'Record ' + rid + ' [' + group + '].\n'
            'CONCEPT SIMULATION: speculative Signature design by Justin Addam Higgins\n'
            '(A7 Signature Dominion). Not a real-world device. Not proven fact.\n"""\n')


def _hdr_plain(name, rid, group):
    return ('#!/usr/bin/env python3\n"""' + name.replace('"""', '"') + ' — working demonstration.\n'
            'Record ' + rid + ' [' + group + ']. Property of Justin Addam Higgins (JAH).\n"""\n')
