# -*- coding: utf-8 -*-
"""Topic module: db-creative-first-date. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-creative-first-date", "name": "The Creative First Date Database", "pfx": "JAH-CREFIRDAT-",
    "tagline_pub": "Creative first date ideas with every plan doable - make the first impression count: every record carrying the idea, the plan, and a check that it is respectful and low-pressure, taught progressively along the ladder.",
    "tagline_sig": "The Signature first-impression: every date a Signature plan, every idea a Signature spark. The full ladder from easy outings through memorable ones to Signature-grade first dates. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Creative First Date",
    "role_pub": "date planner - designing first dates that are fun and low-pressure",
    "role_sig": "Signature date planner - teaching Signature first-impression craft",
    "record_kind": "first date idea record", "record_kind_plural": "first date ideas",
    "demo_kind": "date-proof", "demo_title": "First Date Study",
    "search_ph": "Search first date, date ideas, creative dates, outings...",
    "chat_ph": "Ask for a first date idea...",
    "gen_blurb": "Generate clearly-labeled date studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded first date ideas, every plan respectful and low-pressure, marching toward one million records. Presented in teaching-ladder order: easy outings, memorable ones, Signature-grade.",
    "reqs": "Someone to ask and the courage to ask.",
    "stds": "Every idea is public, low-pressure, respectful, and consent-aware; either person can leave easily.",
    "cites": ["JAH Databases respectful dating standard v1.0"],
})


def _fd2(tier, idea, plan, why):
    return T(
        tier, "First date: %s" % idea,
        desc_pub='FIRST DATE IDEA: %s\n\nTHE PLAN: %s\n\nWHY IT WORKS: %s'
        % (idea.upper(), plan, why),
        desc_sig='Signature first impression: %s - a Signature plan for a Signature meeting. The Signature edition treats every good first date as two strangers becoming less strange.' % idea,
        how_pub='Do it: suggest it lightly, let them choose the time, and keep it short - great first dates end with wanting more.',
        how_sig='The Signature way: plan the date, not the outcome - the plan is yours; the connection is mutual.',
        keys=['Idea: %s.' % idea,
              'Plan: %s' % plan,
              'Why: %s' % why],
        demo=("check", {"code": ["IDEA = %r" % idea, "PLAN = %r" % plan,
                                  "VENUES = ['cafe','park','museum','walk','market','library','garden','tour','picnic','bookstore','zoo','gallery','shop','store','class','trail','lake','pub','theater','show','festival','aquarium','downtown','studio','golf','trivia','hike','kayak','movie','food','bank','town','reading','comedy','kite','beach']"],
                        "checks": [("plan_concrete", "len(PLAN) > 25"),
                                   ("low_pressure", "not any(w in PLAN.lower() for w in ['trapped','no escape','must stay'])"),
                                   ("public_setting", "any(w in (IDEA + ' ' + PLAN).lower() for w in VENUES)")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _fd2(B, "Coffee and a walk", "Meet at the corner cafe for coffee, then walk through the nearby park.", "Short, public, easy to extend or end."),
    _fd2(B, "Bookstore browse", "Meet at the bookstore; each picks a book for the other.", "Playful and revealing."),
    _fd2(B, "Farmers market", "Wander the market Saturday morning; buy one thing each.", "Casual, sensory, full of topics."),
    _fd2(B, "Museum morning", "Visit the museum's free morning; pick favorite pieces.", "Built-in conversation everywhere."),
    _fd2(B, "Picnic in the park", "Pack simple food; find a sunny spot.", "Relaxed and romantic, low cost."),
    _fd2(B, "Ice cream crawl", "Visit three ice cream shops; rank the flavors.", "Sweet and silly."),
    _fd2(B, "Library date", "Explore the library; each finds a weird book.", "Quiet, free, full of surprises."),
    _fd2(B, "Botanical garden", "Walk the gardens; photograph favorites.", "Beautiful and unhurried."),
    _fd2(B, "Street food tour", "Try five street vendors downtown.", "Adventure in small bites."),
    _fd2(B, "Used record store", "Dig through vinyl; play finds at the listening station.", "Music taste revealed."),
    _fd2(B, "Zoo morning", "Arrive at opening; see the animals wake up.", "Joyful and easy."),
    _fd2(C, "Cooking class", "Take the beginner pasta class together.", "Teamwork plus dinner."),
    _fd2(C, "Pottery painting", "Paint pottery at the studio; pick up next week.", "Creative and a built-in second date."),
    _fd2(C, "Mini golf", "Play 18 holes; loser buys ice cream.", "Playful competition."),
    _fd2(C, "Trivia night", "Join the pub trivia as a team of two.", "Shows how you think together."),
    _fd2(C, "Sunset hike", "Easy trail timed for sunset.", "Effort plus reward."),
    _fd2(C, "Art gallery + coffee", "Gallery first, then coffee to discuss.", "Culture plus conversation."),
    _fd2(C, "Flea market hunt", "Each finds the weirdest item under $5.", "Treasure hunting together."),
    _fd2(C, "Kayak rental", "Rent a tandem kayak for the calm lake.", "Teamwork on water."),
    _fd2(C, "Outdoor movie", "Bring blankets to the park screening.", "Classic with a twist."),
    _fd2(C, "Baking challenge", "Bake something at home... (better: the cupcake shop's decorate-your-own).", "Sweet and hands-on."),
    _fd2(C, "Aquarium visit", "Wander the aquarium's dark halls.", "Wonder plus closeness."),
    _fd2(C, "Board game cafe", "Meet at the board game cafe; the staff teaches you a two-player game.", "Playful and low-pressure."),
    _fd2(A, "Sunrise breakfast", "Meet before dawn at the hilltop park; watch sunrise with breakfast.", "Effort shows interest."),
    _fd2(A, "Volunteer together", "Serve at the food bank for a morning.", "Values revealed fast."),
    _fd2(A, "Day trip", "Drive to the nearby town; explore all day.", "Adventure bonds."),
    _fd2(A, "Stargazing", "Drive out of town; bring telescope app.", "Wonder under stars."),
    _fd2(A, "Dance class", "Take the beginner salsa class at the downtown studio.", "Brave and fun."),
    _fd2(A, "Food truck festival", "Sample everything at the festival.", "Feast and wander."),
    _fd2(A, "Historic walking tour", "Take the guided old-town tour.", "Stories plus strolling."),
    _fd2(A, "Comedy show", "Laugh together at the improv night.", "Laughter bonds."),
    _fd2(A, "Picnic + kite", "Fly kites after the picnic.", "Playful joy."),
    _fd2(A, "Bookstore + readings", "Attend the author reading, then browse.", "Minds meeting."),
    _fd2(A, "Garden volunteer", "Plant together at the community garden.", "Growing together, literally."),
]
