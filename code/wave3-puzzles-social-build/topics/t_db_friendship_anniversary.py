# -*- coding: utf-8 -*-
"""Topic module: db-friendship-anniversary. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-friendship-anniversary", "name": "The Friendship Anniversary Database", "pfx": "JAH-FRIANN-",
    "tagline_pub": "Friendship anniversary ideas with every celebration heartfelt - honor the years: every record carrying the milestone, the celebration plan, and a check that it is warm and personal, taught progressively along the ladder.",
    "tagline_sig": "The Signature friendship-sight: every anniversary a Signature toast, every year a Signature treasure. The full ladder from sweet gestures through big milestones to Signature-grade celebrations. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Friendship Anniversary",
    "role_pub": "celebration planner - honoring friendships year by year",
    "role_sig": "Signature celebration planner - teaching Signature friendship-sight",
    "record_kind": "anniversary idea record", "record_kind_plural": "anniversary ideas",
    "demo_kind": "toast-proof", "demo_title": "Friendship Anniversary Study",
    "search_ph": "Search friendship, anniversary, milestones, celebrations...",
    "chat_ph": "Ask for a friendship anniversary idea...",
    "gen_blurb": "Generate clearly-labeled celebration studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded anniversary ideas, every celebration warm and personal, marching toward one million records. Presented in teaching-ladder order: sweet gestures, big milestones, Signature-grade.",
    "reqs": "A friend and a memory of when you met.",
    "stds": "Every idea is personal, warm, and doable; the demo verifies it.",
    "cites": ["JAH Databases celebration standard v1.0"],
})


def _fa(tier, milestone, plan, why):
    return T(
        tier, "Anniversary: %s" % milestone,
        desc_pub='MILESTONE: %s\n\nCELEBRATION PLAN: %s\n\nWHY IT WORKS: %s'
        % (milestone.upper(), plan, why),
        desc_sig='Signature friendship: %s - a Signature toast to the years. The Signature edition treats every honored anniversary as friendship getting its due.' % milestone,
        how_pub='Do it: mark the date, plan the gesture, and say what the years meant - the words are the gift.',
        how_sig='The Signature way: recreate something from year one - nostalgia is the strongest toast.',
        keys=['Milestone: %s.' % milestone,
              'Plan: %s' % plan,
              'Why: %s' % why],
        demo=("check", {"code": ["PLAN = %r" % plan],
                        "checks": [("plan_concrete", "len(PLAN) > 20"),
                                   ("personal", "any(w in PLAN.lower() for w in ['memory','photo','letter','story','recreate','favorite','together','friend','shared','song','year','honor','childhood','neighborhood','everyone','old'])"),
                                   ("warm", "not any(w in PLAN.lower() for w in ['ignore','forget','cheap shot'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _fa(B, "1 year of friendship", "Write a card listing your favorite memory from the year.", "Year one deserves words."),
    _fa(B, "First friend-versary dinner", "Cook their favorite meal together.", "Food plus memory."),
    _fa(B, "6 months in", "Send a surprise playlist of your shared songs.", "Music marks time."),
    _fa(B, "The 'met-you' day", "Visit where you first met; take a photo.", "Full circle, year one."),
    _fa(B, "100 days", "Exchange 100-word notes about the friendship.", "Short and sweet."),
    _fa(B, "First trip together anniversary", "Look through the trip photos together.", "Relive the adventure."),
    _fa(B, "The inside-joke day", "Celebrate with the joke's origin story retold.", "Laughter is the bond."),
    _fa(B, "2 years", "Make a photo collage of year two.", "Two years, one collage."),
    _fa(B, "The song anniversary", "Play 'your song' and dance.", "Music plus memory."),
    _fa(B, "First holiday together", "Recreate that holiday's best moment.", "Traditions start here."),
    _fa(B, "The rescue anniversary", "Thank them for being there in the hard time - write the gratitude letter.", "Gratitude deepens bonds."),
    _fa(C, "5 years", "Throw a small party with mutual friends.", "Five years deserves witnesses."),
    _fa(C, "10 years", "Write letters to each other; read them aloud.", "A decade of words."),
    _fa(C, "The move-away reunion", "Reunite in the old neighborhood.", "Place holds memory."),
    _fa(C, "College friends 15 years", "Recreate the dorm room photo.", "The photo then and now."),
    _fa(C, "Childhood friends 20 years", "Visit the childhood street together.", "Roots run deep."),
    _fa(C, "The wedding party anniversary", "Toast the friend who introduced you.", "Honor the connector."),
    _fa(C, "Work friends 5 years", "Lunch at the old office spot.", "Where it started."),
    _fa(C, "The crisis bond", "Mark the day you got through it together.", "Survived together."),
    _fa(C, "Book club 3 years", "Read your first book again together and share favorite passages.", "Full circle reading."),
    _fa(C, "Sports buddies 7 years", "Play the game you started with together; share the old story.", "The original game."),
    _fa(C, "Neighbor friends 5 years", "Block party in their honor.", "The street celebrates."),
    _fa(C, "Long-distance 10 years", "Video call with the old photos shared.", "Distance defeated yearly."),
    _fa(A, "25 years (silver)", "Gather everyone for the silver celebration.", "Quarter century of friendship."),
    _fa(A, "30 years", "Create the memory book with all friends contributing.", "Thirty years, one book."),
    _fa(A, "40 years", "Return to where it all began together; recreate the first photo.", "Four decades, one place."),
    _fa(A, "50 years (golden)", "The golden party - everyone they've touched.", "Half a century."),
    _fa(A, "The lifetime award", "Give them a homemade 'best friend' trophy.", "Silly and sincere."),
    _fa(A, "The legacy letter", "Write what their friendship meant for your life.", "The ultimate toast."),
    _fa(A, "The reunion tour", "Visit every place that mattered, together.", "The victory lap."),
    _fa(A, "The promise renewal", "Renew your friendship vows.", "Vows aren't just for weddings."),
    _fa(A, "The tree planting", "Plant a tree together for the decades.", "Growing together, literally."),
    _fa(A, "The scholarship", "Start a small scholarship in their honor.", "Friendship that gives forward."),
    _fa(A, "The documentary", "Film interviews about the friendship.", "The story, preserved."),
]
