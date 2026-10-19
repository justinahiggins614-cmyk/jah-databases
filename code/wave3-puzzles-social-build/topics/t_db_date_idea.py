# -*- coding: utf-8 -*-
"""Topic module: db-date-idea. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-date-idea", "name": "The Date Idea Database", "pfx": "JAH-DATIDE-",
    "tagline_pub": "Date ideas for every stage with every plan doable - never run out of dates: every record carrying the idea, the plan, and a check that it is respectful and fun, taught progressively along the ladder.",
    "tagline_sig": "The Signature date-sight: every idea a Signature plan, every date a Signature memory. The full ladder from sweet outings through adventures to Signature-grade romance. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Date Idea",
    "role_pub": "date designer - dreaming up dates for every stage and budget",
    "role_sig": "Signature date designer - teaching Signature date-sight",
    "record_kind": "date idea record", "record_kind_plural": "date ideas",
    "demo_kind": "date-proof", "demo_title": "Date Idea Study",
    "search_ph": "Search date ideas, date night, romance, outings...",
    "chat_ph": "Ask for a date idea...",
    "gen_blurb": "Generate clearly-labeled date studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded date ideas, every plan respectful and fun, marching toward one million records. Presented in teaching-ladder order: sweet outings, adventures, Signature-grade.",
    "reqs": "Someone special and a plan.",
    "stds": "Every idea is respectful, consent-aware, and genuinely doable; the demo verifies concreteness.",
    "cites": ["JAH Databases date quality standard v1.0"],
})


def _di(tier, idea, plan, budget, why):
    return T(
        tier, "Date: %s" % idea,
        desc_pub='DATE IDEA: %s\n\nTHE PLAN: %s\n\nBUDGET: %s\n\nWHY IT WORKS: %s'
        % (idea.upper(), plan, budget, why),
        desc_sig='Signature date: %s - a Signature plan for a Signature night. The Signature edition treats every good date as the relationship getting its flowers.' % idea,
        how_pub='Do it: pick one that fits your stage, plan the details, and be present - the plan is 20%, presence is 80%.',
        how_sig='The Signature way: end every date with the next one planned - momentum is romance.',
        keys=['Idea: %s.' % idea,
              'Plan: %s' % plan,
              'Budget: %s.' % budget,
              'Why: %s' % why],
        demo=("check", {"code": ["PLAN = %r" % plan, "BUDGET = %r" % budget],
                        "checks": [("plan_concrete", "len(PLAN) > 25"),
                                   ("budget_stated", "BUDGET in ('free','cheap','moderate','splurge')"),
                                   ("respectful", "not any(w in PLAN.lower() for w in ['humiliat','force','trick'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _di(B, "Sunset picnic", "Pack dinner; find the west-facing hill; arrive 30 minutes before sunset.", "cheap", "Nature does the decorating."),
    _di(B, "Coffee and bookstore", "Browse together; each buys the other a book.", "cheap", "Thoughtful and easy."),
    _di(B, "Movie under stars", "Outdoor screening with blankets and popcorn.", "cheap", "Classic romance, upgraded."),
    _di(B, "Cook together", "Pick a recipe; cook it side by side.", "cheap", "Teamwork tastes good."),
    _di(B, "Museum wander", "Get lost in the galleries; debate favorites.", "cheap", "Culture plus conversation."),
    _di(B, "Farmers market", "Buy ingredients; cook them after.", "cheap", "Two dates in one."),
    _di(B, "Stargazing", "Drive out of town; bring the star app.", "free", "Wonder is free."),
    _di(B, "Board game night", "Two-player games and snacks at home.", "free", "Playful and cozy."),
    _di(B, "Beach walk", "Walk the shoreline at golden hour.", "free", "Simple and timeless."),
    _di(B, "Library date", "Find each other strange books.", "free", "Free and full of surprises."),
    _di(B, "Ice cream walk", "Get cones; walk the neighborhood.", "cheap", "Sweet simplicity."),
    _di(C, "Cooking class", "Take the couples pasta class downtown.", "moderate", "Learn and eat."),
    _di(C, "Wine tasting", "Visit the vineyard's tasting room.", "moderate", "Grown-up adventure."),
    _di(C, "Concert night", "See the band you both love.", "moderate", "Shared music, shared memory."),
    _di(C, "Kayak morning", "Paddle the calm lake at dawn.", "moderate", "Teamwork on water."),
    _di(C, "Comedy club", "Laugh together at the late show.", "moderate", "Laughter bonds."),
    _di(C, "Art and dinner", "Gallery then the cozy restaurant.", "moderate", "Culture plus cuisine."),
    _di(C, "Hiking picnic", "Hike to the overlook; picnic at top.", "cheap", "Effort plus reward."),
    _di(C, "Trivia duo", "Enter the pub quiz as a team.", "cheap", "Brains plus beer."),
    _di(C, "Pottery date", "Throw pots together at the downtown pottery studio.", "moderate", "Messy and memorable."),
    _di(C, "Jazz and dessert", "Jazz club, then the dessert bar.", "moderate", "Smooth and sweet."),
    _di(C, "Bike adventure", "Rent bikes; explore the river trail.", "cheap", "Wind and freedom."),
    _di(C, "Theater night", "See the local theater's Friday night play together.", "moderate", "Stories together."),
    _di(A, "Weekend getaway", "Book the cabin; unplug for two days.", "splurge", "Time away, together."),
    _di(A, "Hot air balloon", "Sunrise balloon ride for two.", "splurge", "Once-in-a-lifetime."),
    _di(A, "Chef's table", "The tasting menu at the special restaurant.", "splurge", "Celebration dining."),
    _di(A, "Road trip", "Drive the coast with no fixed plan.", "moderate", "Adventure bonds."),
    _di(A, "Dance lessons", "Six weeks of salsa together.", "moderate", "Investment in fun."),
    _di(A, "Cabin retreat", "Rent the lakeside cabin for the weekend.", "splurge", "Quiet togetherness."),
    _di(A, "Festival weekend", "Camp at the music festival.", "moderate", "Music and mud."),
    _di(A, "Anniversary redo", "Recreate your first date exactly.", "cheap", "Nostalgia is powerful."),
    _di(A, "Surprise trip", "Plan everything; reveal at the airport.", "splurge", "The ultimate surprise."),
    _di(A, "Vow renewal trip", "Renew vows where you honeymooned.", "splurge", "Full circle."),
    _di(A, "Learn together", "Take the six-week course as a pair.", "moderate", "Growing together."),
]
