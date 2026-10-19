#!/usr/bin/env python3
"""Import all wave-5 content modules (registers 49 items into lib.ITEMS)."""
import content_mystery_detective      # 6
import content_mystery_detective_b    # 5
import content_mystery_codes          # 3
import content_mystery_stories        # 4
import content_mystery_places         # 7
import content_mystery_signals        # 5 -> mystery total 30? see below
import content_generators             # 4 (gen-*)
import content_civ_build              # 7
import content_civ_space              # 3
import content_civ_global             # 10

# mystery theme = 29: 25 db-* + 4 gen-*
MYSTERY_SLUGS = {
    "db-unsolved-mystery-explorer",
    "db-who-did-it",
    "db-missing-object-mystery",
    "db-mystery-box-museum",
    "db-mystery-tournament",
    "db-grand-finale-reveal",
    "db-ancient-codebreaker",
    "db-secret-code-club",
    "db-hidden-pattern-mystery",
    "db-haunted-hotel-adventure",
    "db-midnight-radio-mystery",
    "db-interactive-mystery-story",
    "db-secret-archive-adventure",
    "db-secret-society-worldbuilder",
    "db-mysterious-photograph",
    "db-forgotten-artifact",
    "db-cryptic-map",
    "db-secret-passage",
    "db-secret-identity-puzzle",
    "db-artifact-authentication-game",
    "db-cryptid-encyclopedia",
    "db-strange-signal",
    "db-cosmic-mystery",
    "db-mystery-sound-detective",
    "db-unusual-footprint",
    "gen-detective-case-generator",
    "gen-hidden-message-factory",
    "gen-strange-diary",
    "gen-endless-adventure-generator",
}

# civilization-space theme = 20
CIV_SLUGS = {
    "db-build-a-civilization",
    "db-civilization-simulator",
    "db-build-a-nation",
    "db-mega-structure-concept",
    "db-space-habitat-civilization",
    "db-future-education-system",
    "db-future-farm",
    "db-lunar-economy",
    "db-mars-economy",
    "db-space-manufacturing-network",
    "db-global-problem-solver",
    "db-world-improvement-challenge",
    "db-planet-repair-concept",
    "db-biodiversity-recovery",
    "db-clean-water-for-everyone",
    "db-global-learning-access",
    "db-universal-accessibility",
    "db-human-potential",
    "db-civilization-milestones",
    "db-big-future-ideas-gallery",
}


def family_for(slug):
    if slug in MYSTERY_SLUGS:
        return "M"
    if slug in CIV_SLUGS:
        return "C"
    raise KeyError("slug %r not in wave-5 theme sets" % slug)
