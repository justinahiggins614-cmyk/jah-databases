# -*- coding: utf-8 -*-
"""Topic module: db-club-finder. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-club-finder", "name": "The Club Finder Database", "pfx": "JAH-CLUFIN-",
    "tagline_pub": "Club-finding guides with every path actionable - find your people: every record carrying the interest, where to look, the first step, and a check that the advice is concrete, taught progressively along the ladder.",
    "tagline_sig": "The Signature belonging-sight: every interest a Signature door, every club a Signature home. The full ladder from easy joins through niche hunts to Signature-grade community building. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Club Finder",
    "role_pub": "community guide - pointing every interest toward its people",
    "role_sig": "Signature community guide - teaching Signature belonging-sight",
    "record_kind": "club-finding record", "record_kind_plural": "club-finding guides",
    "demo_kind": "finder-proof", "demo_title": "Club Finder Study",
    "search_ph": "Search clubs, groups, interests, hobbies, community...",
    "chat_ph": "Ask how to find a club...",
    "gen_blurb": "Generate clearly-labeled finder studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded club-finding guides, every path actionable, marching toward one million records. Presented in teaching-ladder order: easy joins, niche hunts, Signature-grade.",
    "reqs": "An interest and the courage to show up once.",
    "stds": "Every guide names concrete places to look and a first step; the demo verifies concreteness.",
    "cites": ["JAH Databases community guide standard v1.0"],
})


def _cf(tier, interest, where, first_step, tip):
    return T(
        tier, "Find your %s" % interest,
        desc_pub='INTEREST: %s\n\nWHERE TO LOOK:\n%s\n\nFIRST STEP: %s\n\nGUIDE TIP: %s'
        % (interest, where, first_step, tip),
        desc_sig='Signature belonging: the %s people are out there - the Signature path leads to them. The Signature edition treats every found club as loneliness losing.' % interest,
        how_pub='Do it: take the first step this week - showing up once is 90% of joining.',
        how_sig='The Signature way: go three times before judging - belonging takes reps.',
        keys=['Interest: %s.' % interest,
              'Where: %s' % where,
              'First step: %s' % first_step,
              'Tip: %s' % tip],
        demo=("check", {"code": ["WHERE = %r" % where, "STEP = %r" % first_step],
                        "checks": [("where_concrete", "len(WHERE) > 20"),
                                   ("step_actionable", "len(STEP) > 15"),
                                   ("step_is_action", "any(v in STEP.lower() for v in ['go','visit','join','ask','sign','attend','show','call','play','try','take','bring','post','fix','volunteer','complete','watch','get','say','walk'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _cf(B, "book club", "Your local library's bulletin board and events page; ask the front desk.", "Go to the next meeting - visitors are always welcome.", "Bring the book only if you've read it; listening is fine."),
    _cf(B, "running group", "Park notice boards, running store group runs, free apps' local groups.", "Show up for the beginner run - nobody is fast at first.", "Run at your pace; the group waits."),
    _cf(B, "chess club", "Library, community center, school; free online clubs with local chapters.", "Play one casual game - ratings don't matter yet.", "Losing is the lesson; enjoy it."),
    _cf(B, "gardening club", "Community gardens, nursery workshops, neighborhood associations.", "Visit a workday - bring gloves.", "Ask the oldest member everything."),
    _cf(B, "cooking group", "Community center classes, library workshops, local food co-ops.", "Join one class - aprons provided.", "Taste everything; volunteer to chop."),
    _cf(B, "hiking buddies", "Trailhead boards, outdoor stores, park ranger programs.", "Join the easy trail walk.", "Bring water and a snack to share."),
    _cf(B, "art class", "Rec centers, art supply stores, library workshops.", "Try the drop-in sketch night.", "No talent required - that's the point."),
    _cf(B, "yoga group", "Studios' community classes, parks in summer, rec centers.", "Take the beginner class.", "Tell the teacher you're new."),
    _cf(B, "volunteer crew", "Food banks, animal shelters, park cleanups - all need hands.", "Sign up for one shift.", "One shift tells you everything."),
    _cf(B, "board game night", "Game stores' weekly nights, library events, cafes.", "Walk in and ask to join a table.", "Say you're new - gamers teach."),
    _cf(B, "choir", "Churches, community centers, schools - many need voices.", "Attend one rehearsal.", "You don't need to read music yet."),
    _cf(C, "amateur astronomy", "Observatories' public nights, astronomy societies, dark-sky parks.", "Attend a star party - telescopes provided.", "Ask 'what's that bright one?' - everyone loves answering."),
    _cf(C, "birdwatching", "Audubon chapters, nature reserves, dawn walks.", "Join the dawn walk - binoculars often loaned.", "Learn five local birds first."),
    _cf(C, "photography club", "Camera stores, art centers, online groups with meetups.", "Bring any camera - phones count.", "Share one photo; ask for feedback."),
    _cf(C, "writing workshop", "Libraries, bookstores, community colleges.", "Bring two pages to share.", "Feedback is a gift - give it kindly."),
    _cf(C, "cycling club", "Bike shops' group rides, trail associations.", "Join the no-drop ride.", "No-drop means nobody gets left."),
    _cf(C, "rock climbing", "Climbing gyms' intro nights and clubs.", "Take the belay class.", "Trust the rope; trust the partner."),
    _cf(C, "language exchange", "Libraries, cultural centers, conversation apps' meetups.", "Go and stumble - that's the method.", "Teach your language too."),
    _cf(C, "community theater", "Local theaters' auditions and crew calls.", "Volunteer for crew first.", "Crew sees everything; acts come later."),
    _cf(C, "makerspace", "Libraries with maker labs, independent workshops.", "Take the safety orientation.", "Make something small first."),
    _cf(C, "dance class", "Studios' beginner nights, cultural centers.", "Try the absolute-beginner class.", "Everyone is bad at first - that's the fun."),
    _cf(C, "kayak group", "Outfitters' group paddles, paddling clubs.", "Join the flat-water paddle.", "Stay with the group; signal early."),
    _cf(C, "genealogy society", "Libraries' history rooms, societies, archives.", "Bring one family name.", "The librarians are detectives - ask."),
    _cf(A, "starting your own club", "No club exists? Libraries and rec centers offer free meeting space.", "Post one flyer with a date, time, and place.", "Three people is a club - start there."),
    _cf(A, "competitive debate", "Leagues, colleges, community debate societies.", "Watch one debate, then judge one.", "Judging teaches faster than debating."),
    _cf(A, "open-source coding", "Hackathons, library code nights, online repos with local meetups.", "Fix one typo-level issue.", "Small fixes earn mentors."),
    _cf(A, "urban sketching", "Online chapters with local meetups, art stores.", "Go sketch in public once.", "Bad sketches in public build courage."),
    _cf(A, "sailing club", "Marinas' crew boards, sailing schools, racing nights.", "Volunteer as rail crew.", "Say 'I can pull ropes' - you're hired."),
    _cf(A, "beekeeping association", "County associations, agricultural extensions.", "Attend the spring intro course.", "Don't buy bees until year two."),
    _cf(A, "historical reenactment", "Regiments and societies recruit at fairs.", "Attend one event as a spectator-helper.", "Start with the civilian impression."),
    _cf(A, "amateur radio", "Clubs run licensing classes; field days welcome all.", "Get the technician license - the class teaches it.", "Call signs are earned, not bought."),
    _cf(A, "trail maintenance crew", "Trail associations, park volunteer programs.", "Join one workday.", "Bring work gloves; leave with friends."),
    _cf(A, "community orchestra", "Community music schools, conductor postings.", "Go audition on your instrument.", "Second violin is a fine throne."),
    _cf(A, "mentoring youth", "Big-brother/sister programs, schools, clubs.", "Complete the background check and training.", "Show up consistently - that's the magic."),
]
