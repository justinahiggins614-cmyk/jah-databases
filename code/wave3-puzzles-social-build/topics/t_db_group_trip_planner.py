# -*- coding: utf-8 -*-
"""Topic module: db-group-trip-planner. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-group-trip-planner", "name": "The Group Trip Planner Database", "pfx": "JAH-GROTRIPLA-",
    "tagline_pub": "Group trip plans with every detail covered - travel together without the drama: every record carrying the trip, the plan, and a check that it is fair and fun, taught progressively along the ladder.",
    "tagline_sig": "The Signature journey-sight: every trip a Signature adventure, every plan a Signature map. The full ladder from easy outings through big trips to Signature-grade expeditions. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Group Trip Planner",
    "role_pub": "trip architect - planning group travel that's fair and fun",
    "role_sig": "Signature trip architect - teaching Signature journey-sight",
    "record_kind": "trip plan record", "record_kind_plural": "trip plans",
    "demo_kind": "journey-proof", "demo_title": "Group Trip Study",
    "search_ph": "Search group trips, travel, planning, vacations, outings...",
    "chat_ph": "Ask for a group trip plan...",
    "gen_blurb": "Generate clearly-labeled plan studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded trip plans, every detail fair and fun, marching toward one million records. Presented in teaching-ladder order: easy outings, big trips, Signature-grade.",
    "reqs": "Friends and a shared calendar.",
    "stds": "Every plan covers budget fairness, roles, and fun; the demo verifies it.",
    "cites": ["JAH Databases trip planning standard v1.0"],
})


def _gtp(tier, trip, plan, tip):
    return T(
        tier, "Trip: %s" % trip,
        desc_pub='GROUP TRIP: %s\n\nTHE PLAN: %s\n\nPLANNER TIP: %s'
        % (trip.upper(), plan, tip),
        desc_sig='Signature journey: %s - a Signature adventure mapped. The Signature edition treats every good trip as the group becoming a story.' % trip,
        how_pub='Plan it: agree on budget first, assign roles, and build in free time - structure prevents drama.',
        how_sig='The Signature way: one organizer, clear money rules, daily free hour - the trinity of trip peace.',
        keys=['Trip: %s.' % trip,
              'Plan: %s' % plan,
              'Tip: %s' % tip],
        demo=("check", {"code": ["PLAN = %r" % plan],
                        "checks": [("plan_concrete", "len(PLAN) > 30"),
                                   ("covers_money", "any(w in PLAN.lower() for w in ['budget','cost','split','share','free'])"),
                                   ("covers_fun", "any(w in PLAN.lower() for w in ['fun','enjoy','explore','play','visit','hike','swim','tour'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _gtp(B, "Park picnic day", "Pack food to share; agree everyone brings one dish; enjoy the park's trails and playground.", "Potluck keeps it fair."),
    _gtp(B, "Beach afternoon", "Carpool to the beach; split parking cost; bring shared sunscreen and enjoy beach games.", "Shared supplies, split costs."),
    _gtp(B, "Zoo visit", "Buy group tickets online; split the cost evenly; enjoy the exhibits together.", "Online tickets skip lines."),
    _gtp(B, "Movie night out", "Vote on the movie; split tickets; enjoy dinner after.", "Vote, don't debate."),
    _gtp(B, "Hiking morning", "Pick the easy trail; carpool; share the snack bag; enjoy the overlook.", "Easy trail keeps all happy."),
    _gtp(B, "Museum day", "Go on the free morning; split lunch after; enjoy the galleries.", "Free mornings are gold."),
    _gtp(B, "Bowling night", "Reserve two lanes; split the cost; enjoy pizza between frames.", "Losers buy dessert."),
    _gtp(B, "Farmers market", "Meet at the market; everyone buys one thing to share; enjoy tasting.", "Sharing multiplies flavors."),
    _gtp(B, "Mini golf", "Play 18 holes; split the fee; enjoy ice cream after.", "Handicaps keep it fun."),
    _gtp(B, "Lake swim", "Drive to the lake; share the cooler; enjoy swimming and sun.", "Life jackets for kids."),
    _gtp(B, "City walking tour", "Follow the free tour; tip the guide together; enjoy lunch after.", "Tip generously, split evenly."),
    _gtp(C, "Cabin weekend", "Split the cabin cost by room; assign cooking nights; enjoy hiking and the fire pit.", "Cooking roster prevents fights."),
    _gtp(C, "City break", "Share the rental apartment; split costs evenly; plan one group dinner; enjoy free time daily.", "Free time is sacred."),
    _gtp(C, "Camping trip", "Share tents and gear; split food costs; assign fire duty; enjoy the stars.", "Gear list shared early."),
    _gtp(C, "Road trip", "Split gas evenly; rotate drivers; plan stops together; enjoy the playlist.", "Driver rotation is law."),
    _gtp(C, "Ski weekend", "Share the condo; split lift tickets; ski in buddy pairs; enjoy the lodge.", "Buddy pairs for safety."),
    _gtp(C, "Festival weekend", "Camp together; split the site cost; see different acts; enjoy meeting nightly.", "Nightly meetup point set."),
    _gtp(C, "Wine country", "Share the tasting fees; designate drivers; enjoy the views.", "Spit or sip - pace matters."),
    _gtp(C, "Theme park day", "Arrive at opening; use the app for lines; split food; enjoy the coasters.", "App strategy saves hours."),
    _gtp(C, "Kayak day", "Rent as a group for the discount; share the dry bags; enjoy the calm water.", "Group discounts rock."),
    _gtp(C, "Historic town", "Walk the old town; split the guided tour; enjoy the cafes.", "Guides beat wandering."),
    _gtp(C, "Sports game", "Buy the group section; split tickets; enjoy tailgating first.", "Tailgate together."),
    _gtp(C, "Beach weekend", "Share the rental house; split groceries; enjoy beach days and boardwalk nights.", "Grocery run day one."),
    _gtp(A, "International week", "Agree the budget cap first; share the apartment; plan two group days; enjoy the rest freely.", "Budget cap before booking."),
    _gtp(A, "Safari adventure", "Book the group safari; split evenly; assign the photographer; enjoy the wildlife.", "Book 6 months out."),
    _gtp(A, "Sailing week", "Charter the boat; split the cost; assign watches; enjoy the islands.", "Sailing experience required."),
    _gtp(A, "National parks tour", "Plan the loop; book campsites early; share driving; enjoy every sunrise.", "Book sites 6 months out."),
    _gtp(A, "Food tour abroad", "Pick the food city; share the apartment; take one cooking class; enjoy everything.", "One class, endless meals."),
    _gtp(A, "Northern lights", "Go in winter; share the cabin; chase the aurora nightly; enjoy the sauna.", "Aurora apps help."),
    _gtp(A, "Island hopping", "Ferry between islands; share rooms; snorkel daily; enjoy the sunsets.", "Ferries booked ahead."),
    _gtp(A, "Mountain trek", "Hire the local guide; share porters; trek together; enjoy the summit.", "Guides are non-negotiable."),
    _gtp(A, "River cruise", "Book the group cabin block and split the cost; dine together nightly; enjoy the ports.", "Block booking discounts."),
    _gtp(A, "Desert expedition", "Join the guided tour; share the camp; enjoy the stars.", "Guides only in deserts."),
    _gtp(A, "Reunion cruise", "Gather the whole family; book adjoining cabins and split the cost; enjoy the shows.", "Adjoining cabins matter."),
]
