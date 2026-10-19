# -*- coding: utf-8 -*-
"""Topic module: db-new-friend-adventure. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-new-friend-adventure", "name": "The New Friend Adventure Database", "pfx": "JAH-NEWFRIADV-",
    "tagline_pub": "New-friend adventures with every outing friendship-tested - turn acquaintances into friends: every record carrying the adventure, the plan, and a check that it builds real connection, taught progressively along the ladder.",
    "tagline_sig": "The Signature friend-sight: every adventure a Signature outing, every new friend a Signature gift. The full ladder from easy outings through bold ones to Signature-grade friendship building. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "New Friend Adventure",
    "role_pub": "friendship guide - turning acquaintances into friends through shared adventure",
    "role_sig": "Signature friendship guide - teaching Signature friend-sight",
    "record_kind": "friend adventure record", "record_kind_plural": "friend adventures",
    "demo_kind": "bond-proof", "demo_title": "New Friend Adventure Study",
    "search_ph": "Search new friends, adventures, friendship building, outings...",
    "chat_ph": "Ask for a new-friend adventure...",
    "gen_blurb": "Generate clearly-labeled adventure studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded friend adventures, every outing connection-building, marching toward one million records. Presented in teaching-ladder order: easy outings, bold ones, Signature-grade.",
    "reqs": "An acquaintance and an invitation.",
    "stds": "Every adventure is low-pressure, public, and builds real connection; the demo verifies it.",
    "cites": ["JAH Databases friendship standard v1.0"],
})


def _nfa(tier, adventure, plan, why):
    return T(
        tier, "Adventure: %s" % adventure,
        desc_pub='NEW FRIEND ADVENTURE: %s\n\nTHE PLAN: %s\n\nWHY IT BONDS: %s'
        % (adventure.upper(), plan, why),
        desc_sig='Signature friendship: %s - a Signature outing for a Signature bond. The Signature edition treats every new friend as the circle widening.' % adventure,
        how_pub='Do it: invite casually, keep it short, and follow up within days - the follow-up is the friendship.',
        how_sig='The Signature way: do the thing they mentioned - remembered details build fastest.',
        keys=['Adventure: %s.' % adventure,
              'Plan: %s' % plan,
              'Why: %s' % why],
        demo=("check", {"code": ["PLAN = %r" % plan],
                        "checks": [("plan_concrete", "len(PLAN) > 25"),
                                   ("low_pressure", "not any(w in PLAN.lower() for w in ['must','forced','trapped'])"),
                                   ("connecting", "any(w in PLAN.lower() for w in ['talk','together','share','chat','laugh','learn','explore','discuss','listen','gathering','dinner','stories','load'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _nfa(B, "Coffee catch-up", "Meet for coffee; talk for an hour; share one story each.", "Stories build bridges."),
    _nfa(B, "Walk and talk", "Walk the park loop together; chat the whole way.", "Walking eases talking."),
    _nfa(B, "Lunch break", "Share lunch near work; learn one new thing.", "Meals bond."),
    _nfa(B, "Bookstore browse", "Browse together; recommend one book each.", "Taste shared."),
    _nfa(B, "Farmers market", "Wander and taste; share finds.", "Discovery together."),
    _nfa(B, "Museum hour", "Visit one exhibit together; discuss your favorites.", "Opinions bond."),
    _nfa(B, "Ice cream run", "Get ice cream cones; walk and talk together.", "Sweet simplicity."),
    _nfa(B, "Park bench chat", "Sit on the park bench and talk for an hour together.", "Time is the gift."),
    _nfa(B, "Library visit", "Explore; find weird books together.", "Curiosity shared."),
    _nfa(B, "Thrift hunt", "Hunt treasures; laugh at finds.", "Playful bonding."),
    _nfa(B, "Garden stroll", "Walk the gardens together; photograph and share favorites.", "Beauty shared."),
    _nfa(C, "Cooking night", "Cook a meal together; share the work and the food.", "Teamwork tastes good."),
    _nfa(C, "Hiking half-day", "Hike the moderate trail; talk at the top.", "Effort bonds."),
    _nfa(C, "Game night", "Play board games; laugh at losses.", "Play reveals."),
    _nfa(C, "Volunteer shift", "Volunteer together for a morning.", "Values align."),
    _nfa(C, "Class together", "Take the beginner class side by side and learn together.", "Learning together."),
    _nfa(C, "Concert outing", "See live music; share the excitement.", "Music moves."),
    _nfa(C, "Sports game", "Cheer together; share snacks.", "Fandom bonds."),
    _nfa(C, "Beach day", "Swim, sun, and talk for hours.", "Relaxed depth."),
    _nfa(C, "Road trip", "Drive somewhere new; explore together.", "Adventure bonds."),
    _nfa(C, "Potluck dinner", "Each brings a dish; share stories.", "Food plus tales."),
    _nfa(C, "Art class", "Paint together; compare results.", "Creative courage."),
    _nfa(C, "Trivia team", "Enter as a team; combine brains and laugh together.", "Thinking together."),
    _nfa(A, "Weekend trip", "Travel together for two days.", "Time deepens."),
    _nfa(A, "Project build", "Build something together, like a shelf or a garden box.", "Making bonds."),
    _nfa(A, "The deep talk", "Share your life stories fully over a long dinner.", "Vulnerability connects."),
    _nfa(A, "Adventure challenge", "Do the scary-fun thing together.", "Courage shared."),
    _nfa(A, "The tradition start", "Start a monthly ritual, like first-Friday dinners.", "Rituals root."),
    _nfa(A, "The introduction", "Introduce them to your circle at a relaxed gathering.", "Inclusion is love."),
    _nfa(A, "The collaboration", "Work on a project together.", "Creating together."),
    _nfa(A, "The celebration", "Celebrate their win big with a surprise gathering.", "Joy shared doubles."),
    _nfa(A, "The support", "Show up in their hard time; listen and share the load.", "Presence proves."),
    _nfa(A, "The years", "Keep showing up for years; share the ups and downs.", "Consistency is everything."),
    _nfa(A, "The family merge", "Blend your friend groups at a casual party; share stories together.", "Circles widening."),
]
