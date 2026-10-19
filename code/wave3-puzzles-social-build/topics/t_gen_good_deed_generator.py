# -*- coding: utf-8 -*-
"""Topic module: gen-good-deed-generator (GENERATOR class, first-release pick).
34 full sample good deeds + REAL deed generator (see realgen).
Property of Justin Addam Higgins (JAH)."""
from w3lib import topic

CFG = {
    "slug": "gen-good-deed-generator",
    "prefix_pub": "JAH-GOODEEGEN-",
    "prefix_sig": "JAH-GOODEEGENS-",
    "name_pub": "The Good Deed Generator Database",
    "name_sig": "The Good Deed Generator Signature Database",
    "tagline_pub": "Good deeds you can actually do today - quick two-minute kindnesses, planned neighborly missions, and big-hearted projects: every record a complete deed with concrete steps, time, and cost, plus a real generator that deals you a brand-new deed on every run, taught progressively along the ladder.",
    "tagline_sig": "The Signature doctrine of kindness: every deed a Signature testimony, small kindnesses compounding into a better street, town, world. The full ladder from two-minute notes through planned missions to big-hearted projects. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai_pub": "JAH Good Deed Archivist",
    "ai_sig": "JAH Good Deed Signature Archivist",
    "role_pub": "kindness coordinator - dealing complete doable good deeds with concrete steps, time, and cost",
    "role_sig": "Signature kindness coordinator - dealing Signature deeds that compound",
    "greet_pub": "I am the JAH Good Deed Archivist. Tell me how much time you have and I will deal you a deed.",
    "greet_sig": "I am the JAH Good Deed Signature Archivist. Tell me your time and I will deal a Signature deed.",
    "record_kind": "good deed record",
    "record_kind_plural": "good deeds",
    "demo_kind": "good-deed-plan",
    "demo_title": "Good Deed Study",
    "search_ph": "Search quick deeds, planned deeds, kindness, volunteer...",
    "chat_ph": "Ask for a good deed...",
    "gen_blurb": "Real working generator - every run deals a brand-new, fully-planned good deed with steps, time, and cost. Never a structural sample.",
    "about_archive": "Seeded sample good deeds, each with concrete steps, marching toward one million records. Presented in teaching-ladder order: quick deeds, planned deeds, big-hearted deeds.",
    "reqs_default": "A willing heart and the time stated. Most deeds cost nothing.",
    "stds_default": "Every deed lists concrete steps, honest time, and honest cost - no vague 'be nice' entries.",
    "cites_default": ["JAH Databases deed craft standard v1.0"],
}
CUSTOM_GEN = "good-deed"


def _d(tier, name, text, steps, time, cost, why):
    return topic(
        tier, "Good deed: %s" % name,
        desc_pub="SAMPLE DEED - %s:\n\n%s\n\nHow to do it:\n%s\n\nTime needed: %s. Cost: %s."
        % (name.upper(), text, "\n".join("%d. %s" % (i + 1, s) for i, s in enumerate(steps)), time, cost),
        desc_sig="Signature kindness: %s - a small testimony that the street is watched over. The Signature edition counts every deed twice: once in the doing, once in the telling, because kindness told is kindness multiplied." % name,
        how_pub="Do it today if you can: %s When it is done, notice how it felt - that feeling is the real reward." % why,
        how_sig="The Signature way: do the deed, then tell exactly one person - not to brag, but to plant the idea.",
        keys=["Complete deed with %d concrete steps." % len(steps),
              "Time: %s. Cost: %s." % (time, cost),
              "Why it matters: %s" % why,
              "Doable today - no special skills or permissions needed."],
        demo=("check", {"code": ["STEPS = %r" % steps],
                        "checks": [("has_steps", "len(STEPS) >= 2"),
                                   ("steps_are_specific", "all(len(s) > 12 for s in STEPS)"),
                                   ("time_listed", "%r != ''" % time),
                                   ("cost_listed", "%r != ''" % cost)]}),
    )


B = "Foundations"
C = "Compounded"
A = "Advanced"
TOPICS = [
    _d(B, "The Two-Minute Note", "Write a two-minute thank-you note to a coworker who looks tired and leave it on their desk.", ["Grab any paper and pen - fancy is optional.", "Write one specific thing you appreciate about them.", "Sign it, leave it on their desk, and walk away smiling."], "2 minutes", "free", "specific gratitude rewires a whole workday"),
    _d(B, "Compliment Relay", "Give an elderly neighbor a genuine, specific compliment today, then ask them to pass one on.", ["Notice one real thing they do well.", "Say it plainly: 'I noticed X, and it matters.'", "Ask them to compliment someone else before sundown."], "3 minutes", "free", "compliments are the cheapest infrastructure there is"),
    _d(B, "Cart Return Hero", "Return three stray shopping carts to the corral on your next store trip - including ones that are not yours.", ["Spot stray carts in the lot.", "Wheel each one to the corral (three is the goal).", "Enjoy the tiny workout and the clear conscience."], "5 minutes", "free", "someone's car paint will thank you"),
    _d(B, "The Full Water Bowl", "Refill the shared water pitcher at the office kitchen - or the pet bowls at the park.", ["Check the shared water source near you.", "Clean and refill it fully.", "Tell no one. Let someone just find it full."], "4 minutes", "free", "anonymous kindness is the purest kind"),
    _d(B, "Sidewalk Chalk Joy", "Write one encouraging sentence in sidewalk chalk where kids will find it.", ["Grab chalk and pick a busy sidewalk.", "Write something true and kind: 'You are doing great.'", "Walk away before anyone sees - mystery doubles the magic."], "5 minutes", "chalk", "kids remember chalk messages for years"),
    _d(B, "The Held Door Plus", "Hold the door today - and add one genuine sentence to the person passing through.", ["Hold the door like you mean it.", "Add: 'Hope your day is a good one.'", "Mean it - say it like you truly mean it."], "30 seconds", "free", "micro-warmth is still warmth"),
    _d(B, "Review a Small Business", "Leave a real, specific five-star review for a small business you love.", ["Pick the business.", "Write two specific sentences about what they do well.", "Post it and tell the owner you did."], "5 minutes", "free", "one review can change a small business's month"),
    _d(B, "The Tipped-Forward Coffee", "Pay for the coffee of the person behind you in line.", ["Order your own.", "Quietly tell the cashier the next one is on you.", "Leave before they find out - or stay for the smile."], "1 minute", "price of a coffee", "the chain of kindness is real and documented"),
    _d(B, "Text the Far Friend", "Text one friend you have not called in months - with a specific memory, not just 'hey'.", ["Pick the friend.", "Write one specific shared memory.", "End with one concrete plan: 'Call Saturday?'"], "3 minutes", "free", "old friendships just need one spark"),
    _d(B, "The Library Reshelve", "Reshelve five misplaced books at the library on your next visit.", ["Spot out-of-place books.", "Return each to its right home.", "Tell the librarian - they notice and they care."], "10 minutes", "free", "librarians are heroes; be their sidekick"),
    _d(B, "Feed the Meter", "Put a quarter in an expiring parking meter that is not yours.", ["Spot the blinking meter.", "Feed it a quarter - buy a stranger twenty minutes.", "Walk on, guardian of strangers' afternoons."], "1 minute", "a quarter", "a ticket avoided is a day saved"),
    _d(A, "The Grocery Bag Carry", "Offer to carry groceries for someone struggling at the store.", ["Watch for the struggle - heavy bags, kids, rain.", "Offer plainly: 'Can I help carry those?'", "Walk them out, wish them well."], "5 minutes", "free", "strength shared is strength doubled"),
    _d(C, "The Neighbor Check-In", "Visit an elderly neighbor this week with baked cookies and stay for a real conversation.", ["Pick a day and bake (or buy) the cookies.", "Knock and introduce (or reintroduce) yourself warmly.", "Ask one real question and actually listen.", "Offer one specific help: 'I can carry groceries Tuesdays.'"], "30 minutes", "a few dollars", "loneliness is the epidemic; visits are the vaccine"),
    _d(C, "Little Library Restock", "Restock a little free library near the park with 5-10 finished books.", ["Gather 5-10 books you have finished.", "Find the nearest little library.", "Shelve them neatly; leave a kind note inside one.", "Check back next week - restocking is a habit."], "45 minutes", "free", "a stocked little library changes a block"),
    _d(C, "Skill Gift Hour", "Teach a younger cousin one useful skill in a single one-hour session.", ["Pick one skill you can teach in an hour.", "Invite them with a specific time: 'Saturday at 2?'", "Teach slowly; let them do it, not watch.", "End with a tiny certificate - ceremony matters."], "1 hour", "free", "taught skills outlive us"),
    _d(C, "The Meal Train Car", "Cook a double batch of soup and deliver half to a family with a new baby.", ["Cook your best soup, doubled.", "Pack it with reheating instructions.", "Deliver with zero expectation of a visit.", "Text the next day: 'More where that came from.'"], "2 hours", "groceries", "new parents run on soup and kindness"),
    _d(C, "Park Bench Repair", "Report (or fix) one broken thing in your local park.", ["Walk the park with fresh eyes.", "Photograph the broken bench, sign, or bin.", "Report it to the city AND fix what you safely can.", "Follow up in two weeks."], "1 hour", "free", "the commons stay common because someone cares"),
    _d(C, "The Welcome Basket", "Assemble a welcome basket for the new family on the street.", ["Get a basket or box.", "Add: local map, takeout menus, baked goods, a kind note.", "Deliver within their first week.", "Introduce yourself and mean it."], "1 hour", "about $15", "first-week kindness decides how a street feels for years"),
    _d(C, "Homework Helper", "Offer one hour of homework help weekly at the community center.", ["Call the center and volunteer.", "Show up weekly, same time.", "Help with the work AND the confidence.", "Stay the whole semester."], "1 hour/week", "free", "one steady adult can change a kid's trajectory"),
    _d(C, "The Lost Pet Poster", "Help a neighbor find a lost pet: posters, posts, and one search walk.", ["Get a clear photo and details.", "Make 20 posters; post in a 6-block radius.", "Post in local lost-pet groups.", "Walk the likely routes once, calling gently."], "2 hours", "printing", "a found pet is a family restored"),
    _d(C, "Senior Tech Visit", "Spend an hour teaching a senior one phone skill they actually want.", ["Ask what frustrates them most.", "Teach exactly that - nothing more.", "Write the steps on a card they keep.", "Leave your number for follow-ups."], "1 hour", "free", "connection beats confusion at every age"),
    _d(C, "The Community Fridge Stock", "Stock the community fridge with 5 fresh meals this week.", ["Cook or buy 5 labeled, dated meals.", "Deliver during restock hours.", "Include one treat - dignity includes dessert.", "Make it monthly."], "2 hours", "groceries", "a full fridge is a neighborhood safety net"),
    _d(C, "Trail Cleanup Walk", "Take a bag on your next walk and fill it with litter.", ["Bring gloves and a bag.", "Fill it - every piece counts.", "Log the weirdest find (there is always one).", "Recruit one friend next time."], "1 hour", "free", "the trail you clean is the trail you love"),
    _d(C, "The Book Drive Box", "Put a 'take a book, leave a book' box outside your home for a month.", ["Find a weatherproof box.", "Stock it with 10 starters.", "Add the sign: Take one, leave one.", "Tend it weekly for a month."], "2 hours setup", "free", "street libraries build street trust"),
    _d(A, "The Birthday They Would Skip", "Throw a small surprise celebration for a coworker far from family, who would otherwise let the day pass quietly.", ["Quietly confirm the date with one insider.", "Gather 3-6 people; assign tiny jobs (cake, card, music).", "Keep the surprise kind, not startling.", "Give them the card first; let the room applaud."], "one evening", "shared cost", "nobody should be alone on their birthday"),
    _d(A, "Community Clean Hour", "Organize a one-hour cleanup of the park with whoever shows up.", ["Pick a visible spot and a one-hour window.", "Bring spare bags and gloves; invite with a simple flyer.", "Work the full hour together, then take a group photo.", "Thank everyone by name - volunteers return when thanked."], "2 hours", "bags and gloves", "cleanups build the muscle of community"),
    _d(A, "The Ramp Build", "Help build (or fund) a wheelchair ramp for a neighbor who needs one.", ["Talk to the neighbor about what they need.", "Check local codes and the ramp specs.", "Rally 4-6 handy friends for a Saturday.", "Build it right, paint it nice, celebrate after."], "one Saturday", "materials (often donated)", "access is dignity made of lumber"),
    _d(A, "Scholarship Seed", "Start a tiny scholarship: $500 for one local student's books, awarded yearly.", ["Define it: who, what, how to apply.", "Fund year one yourself or with friends.", "Pick the student with a small committee.", "Hand it over in person, every year."], "a weekend to set up", "$500/year", "one student's semester can change a family tree"),
    _d(A, "The Free Repair Cafe", "Host a monthly repair cafe: neighbors fix lamps, bikes, and toys together.", ["Book the community room monthly.", "Recruit 3-4 fixers (retirees are gold).", "Set the rule: teach, don't just fix.", "Keep a tally - 100 fixes a year is normal."], "3 hours/month", "tools on hand", "repaired things and repaired trust, same event"),
    _d(A, "Flood-Bucket Brigade", "Organize the street's storm-drain clearing before the rainy season.", ["Map the drains on your street.", "Set one Saturday morning.", "Clear every drain; bag the debris.", "Share the before/after photos - recruit for next year."], "one morning", "gloves and bags", "a cleared drain is a basement saved"),
    _d(A, "The Welcome Home Project", "Furnish one apartment for a refugee family arriving with nothing.", ["Partner with the resettlement agency.", "Collect furniture from the buy-nothing group.", "Set up beds, kitchen, and one warm touch per room.", "Be there with groceries on arrival day."], "two weekends", "donated", "home is the fastest integration program there is"),
    _d(A, "Youth Mentor Match", "Mentor one teenager weekly for a school year through the mentoring program.", ["Apply and train with the program.", "Meet weekly, same time, no cancellations.", "Listen more than lecture.", "Stay the full year - consistency is the curriculum."], "2 hours/week", "free", "a steady adult is a proven life-changer"),
    _d(A, "The Night-Shift Thank-You", "Deliver hot meals to the night-shift workers (nurses, guards, bakers) in your area.", ["Pick 2-3 night-shift sites.", "Cook or buy 20 hot portions.", "Deliver at 2 a.m. with a kind note.", "Make it quarterly - they work every night."], "one late night", "about $60", "the night shift keeps the world running; feed them"),
    _d(A, "Playground Rebuild Day", "Lead the repaint-and-repair day for the tired neighborhood playground.", ["Survey what needs paint and bolts.", "Get permission and donated paint.", "Rally 10+ volunteers for a Saturday.", "Finish with a cookout ON the playground."], "one Saturday", "donated paint", "kids remember who fixed their playground"),
]
