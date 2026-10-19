# -*- coding: utf-8 -*-
"""Topic module: db-community-challenge. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-community-challenge", "name": "The Community Challenge Database", "pfx": "JAH-COMCHA-",
    "tagline_pub": "Community challenges with every mission doable - rally your neighborhood: every record carrying the challenge, the steps, and a check that it is concrete and kind, taught progressively along the ladder.",
    "tagline_sig": "The Signature together-sight: every challenge a Signature rally, every completed mission a Signature win. The full ladder from easy acts through big projects to Signature-grade community building. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Community Challenge",
    "role_pub": "community captain - dealing missions that bring neighborhoods together",
    "role_sig": "Signature community captain - teaching Signature together-sight",
    "record_kind": "community challenge record", "record_kind_plural": "community challenges",
    "demo_kind": "mission-proof", "demo_title": "Community Challenge Study",
    "search_ph": "Search community, challenges, neighborhood, volunteer, missions...",
    "chat_ph": "Ask for a community challenge...",
    "gen_blurb": "Generate clearly-labeled mission studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded community challenges, every mission doable and kind, marching toward one million records. Presented in teaching-ladder order: easy acts, big projects, Signature-grade.",
    "reqs": "Neighbors and a weekend.",
    "stds": "Every challenge is concrete, kind, and doable; the demo verifies the steps are actionable.",
    "cites": ["JAH Databases community mission standard v1.0"],
})


def _cc(tier, title, mission, steps, tip):
    return T(
        tier, "Challenge: %s" % title,
        desc_pub='COMMUNITY CHALLENGE: %s\n\nMISSION: %s\n\nSTEPS:\n%s\n\nCAPTAIN TIP: %s'
        % (title.upper(), mission,
           "\n".join("  %d. %s" % (i + 1, s) for i, s in enumerate(steps)), tip),
        desc_sig='Signature together: %s - the neighborhood rising as one. The Signature edition treats every completed challenge as the community proving itself.' % title,
        how_pub='Run it: recruit three neighbors, set a date, and do the steps - done beats perfect.',
        how_sig='The Signature way: photograph the before and after - proof recruits the next crew.',
        keys=['Challenge: %s.' % title,
              'Mission: %s' % mission,
              'Steps: %d, each actionable.' % len(steps),
              'Tip: %s' % tip],
        demo=("check", {"code": ["STEPS = %r" % steps],
                        "checks": [("steps_actionable", "len(STEPS) >= 3"),
                                   ("steps_concrete", "all(len(s) > 12 for s in STEPS)"),
                                   ("kind_mission", "not any(w in ' '.join(STEPS).lower() for w in ['hate','attack','destroy'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _cc(B, "The Porch Light Welcome", "Welcome every new neighbor within a week of moving in.", ["Watch for moving trucks on your street.", "Knock with a small welcome note.", "Invite them to the next neighborhood event."], "Notes beat nothing; visits beat notes."),
    _cc(B, "The Litter Sweep", "Pick up litter on your block every Saturday.", ["Grab a bag and gloves Saturday morning.", "Walk your block's sidewalks.", "Recruit one neighbor next week."], "Same time weekly builds the habit."),
    _cc(B, "The Food Drive Sprint", "Collect 50 cans for the food bank this month.", ["Place a box by your door with a sign.", "Tell five neighbors.", "Deliver together at month's end."], "Visible boxes fill themselves."),
    _cc(B, "The Senior Check-In", "Visit one elderly neighbor weekly.", ["Pick a neighbor living alone.", "Knock every Sunday afternoon.", "Bring something small to share."], "Consistency matters more than gifts."),
    _cc(B, "The Little Library", "Build or stock a free book box.", ["Get a weatherproof box.", "Mount it curbside with permission.", "Seed it with 20 books."], "Seed generously; it empties fast."),
    _cc(B, "The Sidewalk Chalk Day", "Cover the block in chalk art one Sunday.", ["Buy chalk in bulk.", "Invite every kid on the street.", "Photograph the gallery."], "Themes help: 'our street in 2050'."),
    _cc(B, "The Lost Pet Network", "Create a street pet-alert chain.", ["List every pet with a photo.", "Share phone numbers.", "Test the chain once."], "Test before you need it."),
    _cc(B, "The Garden Share", "Trade surplus garden produce.", ["Put extras on a curb table.", "Post in the neighborhood group.", "Swap, don't sell."], "Zucchini season needs this."),
    _cc(B, "The Storm Prep Buddy", "Pair every elderly resident with a buddy.", ["Map the vulnerable households.", "Assign buddies.", "Exchange emergency numbers."], "Do it before storm season."),
    _cc(B, "The Book Swap", "Monthly book exchange on the block.", ["Pick a monthly Saturday.", "Everyone brings three books.", "Leftovers go to the little library."], "Kids' books move fastest."),
    _cc(B, "The Welcome Basket", "Assemble baskets for new families.", ["Keep a stash of local maps and coupons.", "Add homemade treats.", "Deliver within the first week."], "The map matters most."),
    _cc(C, "The Block Party", "Throw a street party for 100 neighbors.", ["Get the street-closure permit.", "Recruit a grill team and a music team.", "Invite every household in person.", "Plan the rain backup."], "In-person invites triple turnout."),
    _cc(C, "The Community Garden", "Turn the vacant lot into gardens.", ["Get the owner's permission in writing.", "Divide into plots.", "Set water and compost rules.", "Hold a planting day."], "Written permission first, always."),
    _cc(C, "The Tutoring Circle", "Free homework help twice a week.", ["Find a free room (library).", "Recruit five tutors.", "Match tutors to kids.", "Track progress monthly."], "Consistency beats brilliance."),
    _cc(C, "The Tool Library", "Share tools block-wide.", ["Catalog donated tools.", "Set borrowing rules.", "Appoint a keeper.", "Open Saturdays."], "Ladders and drills go first."),
    _cc(C, "The Mural Project", "Paint a neighborhood mural.", ["Get wall permission.", "Hold a design contest.", "Buy paint with donations.", "Paint over two weekends."], "Kids' designs win hearts."),
    _cc(C, "The Night Watch", "Organize a friendly evening walk group.", ["Set the route and time.", "Invite widely - safety in numbers.", "Carry lights, not weapons.", "Report, don't confront."], "Friendliness is the deterrent."),
    _cc(C, "The Repair Cafe", "Monthly fix-it gathering.", ["Recruit handy volunteers.", "Set up stations (sewing, bikes, electronics).", "Advertise widely.", "Track items saved from trash."], "Count the saves - it motivates."),
    _cc(C, "The History Walk", "Create a self-guided neighborhood history tour.", ["Research five historic spots.", "Write the plaques.", "Print the map.", "Lead the first walk."], "Old photos make it magic."),
    _cc(C, "The Playground Build", "Refresh the old playground.", ["Survey parents for needs.", "Get permits and funds.", "Organize build day.", "Plan maintenance."], "Build day needs 30 volunteers."),
    _cc(C, "The Language Table", "Weekly conversation practice for newcomers.", ["Pick a welcoming cafe.", "Set the weekly time.", "Pair learners with speakers.", "Celebrate progress monthly."], "Food helps every language."),
    _cc(C, "The Seed Bank", "Share seeds seasonally.", ["Collect heirloom seeds.", "Label everything.", "Hold spring swap day.", "Teach saving seeds."], "Label or it's chaos."),
    _cc(C, "The Choir Flash", "Surprise choir performance downtown.", ["Recruit 20 singers.", "Rehearse three songs.", "Pick the spot and time.", "Film the performance."], "Three songs is plenty."),
    _cc(A, "The Vacant Lot Transformation", "Turn three vacant lots into pocket parks.", ["Map the lots and owners.", "Negotiate temporary use.", "Design with neighbors.", "Build in phases.", "Set stewardship."], "Phases keep momentum."),
    _cc(A, "The Mutual Aid Network", "Block-wide help exchange.", ["Sign up 50 households.", "Build the needs/offers board.", "Set response norms.", "Run a monthly potluck."], "The potluck is the network."),
    _cc(A, "The Youth Council", "Teen-led neighborhood projects.", ["Recruit 12 teens.", "Give them a real budget.", "Pair with adult mentors.", "Let them lead publicly."], "Real budget = real respect."),
    _cc(A, "The Emergency Plan", "Whole-block disaster readiness.", ["Map risks and resources.", "Assign roles.", "Drill twice a year.", "Keep the kit list current."], "Drills reveal the gaps."),
    _cc(A, "The Co-op Store", "Neighborhood-owned grocery.", ["Survey demand.", "Incorporate as a co-op.", "Find the space.", "Hire from the block.", "Open in phases."], "Start with the survey."),
    _cc(A, "The Scholarship Fund", "Send one local kid to camp yearly.", ["Set the criteria.", "Fundraise at events.", "Pick transparently.", "Celebrate the winner."], "Transparency is everything."),
    _cc(A, "The Oral History Project", "Record 100 elder stories.", ["Train teen interviewers.", "Schedule the interviews.", "Archive at the library.", "Publish the best."], "Teens + elders = magic."),
    _cc(A, "The Green Corridor", "Connect parks with planted paths.", ["Map the route.", "Get permissions.", "Plant in stages.", "Maintain monthly."], "Native plants survive."),
    _cc(A, "The Time Bank", "Trade hours, not dollars.", ["Set the hour currency.", "Build the directory.", "Broker first exchanges.", "Celebrate 1,000 hours."], "First exchanges need brokering."),
    _cc(A, "The Festival", "Annual neighborhood festival.", ["Form the committee.", "Book the street.", "Recruit food and music.", "Plan year one small.", "Grow the festival yearly."], "Year one small, year five legendary."),
    _cc(A, "The Legacy Project", "Endow something permanent.", ["Pick the thing (bench, tree, fund).", "Raise the money.", "Install with ceremony.", "Maintain forever."], "Ceremony makes it stick."),
]
