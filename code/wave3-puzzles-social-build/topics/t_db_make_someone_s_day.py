# -*- coding: utf-8 -*-
"""Topic module: db-make-someone-s-day. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-make-someone-s-day", "name": "The Make Someone's Day Database", "pfx": "JAH-MAKSOMDAY-",
    "tagline_pub": "Day-making ideas with every gesture kind - brighten someone's day: every record carrying the idea, how to do it, and a check that it is genuine and kind, taught progressively along the ladder.",
    "tagline_sig": "The Signature kindness-sight: every gesture a Signature gift, every brightened day a Signature win. The full ladder from small kindnesses through big ones to Signature-grade generosity. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Make Someone's Day",
    "role_pub": "kindness coach - dealing daily chances to brighten days",
    "role_sig": "Signature kindness coach - teaching Signature kindness-sight",
    "record_kind": "day-making record", "record_kind_plural": "day-making ideas",
    "demo_kind": "kindness-proof", "demo_title": "Make Someone's Day Study",
    "search_ph": "Search kindness, make someone's day, gestures, generosity...",
    "chat_ph": "Ask for a day-making idea...",
    "gen_blurb": "Generate clearly-labeled kindness studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded day-making ideas, every gesture genuine and kind, marching toward one million records. Presented in teaching-ladder order: small kindnesses, big ones, Signature-grade.",
    "reqs": "A heart and five minutes.",
    "stds": "Every idea is genuine, kind, and doable; the demo verifies it.",
    "cites": ["JAH Databases kindness standard v1.0"],
})


def _msd(tier, idea, how, why):
    return T(
        tier, "Brighten: %s" % idea,
        desc_pub="MAKE SOMEONE'S DAY: %s\n\nHOW: %s\n\nWHY IT MATTERS: %s"
        % (idea.upper(), how, why),
        desc_sig="Signature kindness: %s - a Signature gift given. The Signature edition treats every brightened day as the world getting warmer." % idea,
        how_pub="Do it: pick one today, do it fully, and tell no one - anonymous kindness counts double.",
        how_sig="The Signature way: make it specific - generic kindness is nice; specific kindness is unforgettable.",
        keys=["Idea: %s." % idea,
              "How: %s" % how,
              "Why: %s" % why],
        demo=("check", {"code": ["HOW = %r" % how],
                        "checks": [("how_concrete", "len(HOW) > 20"),
                                   ("genuine", "not any(w in HOW.lower() for w in ['show off','brag','post it'])"),
                                   ("kind", "not any(w in HOW.lower() for w in ['prank','trick','embarrass'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _msd(B, "The genuine compliment", "Tell a coworker specifically what they did well today.", "Specific praise sticks."),
    _msd(B, "The held door", "Hold the door and smile at the next person.", "Small courtesies compound."),
    _msd(B, "The thank-you note", "Write three sentences of thanks to someone.", "Written thanks are kept."),
    _msd(B, "The coffee surprise", "Buy coffee for the person behind you.", "Caffeine plus kindness."),
    _msd(B, "The listening ear", "Ask someone how they are - and listen.", "Listening is rare."),
    _msd(B, "The chore steal", "Do a chore before being asked.", "Unasked help delights."),
    _msd(B, "The text check-in", "Text a friend: thinking of you.", "Three words, big warmth."),
    _msd(B, "The smile", "Smile at three strangers today.", "Smiles are contagious."),
    _msd(B, "The tip bump", "Tip generously and thank by name.", "Names matter."),
    _msd(B, "The returned cart", "Return your cart - and one extra.", "Tiny civic grace."),
    _msd(B, "The compliment forward", "Compliment someone to their boss.", "Praise upward amplifies."),
    _msd(C, "The meal train", "Organize meals for a family in need.", "Food is love delivered."),
    _msd(C, "The skill gift", "Offer your skill free to someone who needs it.", "Talent shared doubles."),
    _msd(C, "The errand run", "Do errands for an elderly neighbor.", "Time is the gift."),
    _msd(C, "The book gift", "Give a book you loved with a note.", "Books plus notes last."),
    _msd(C, "The public praise", "Praise someone in front of others.", "Witnessed praise shines."),
    _msd(C, "The apology", "Apologize for the old slight.", "Old wounds can heal."),
    _msd(C, "The welcome", "Welcome the new neighbor properly.", "Belonging starts here."),
    _msd(C, "The fundraiser", "Raise money for someone's need.", "Community rallies."),
    _msd(C, "The mentorship", "Offer an hour of mentoring.", "An hour changes trajectories."),
    _msd(C, "The garden gift", "Share your harvest with neighbors.", "Abundance shared."),
    _msd(C, "The ride offer", "Drive someone who needs it.", "Wheels are freedom."),
    _msd(C, "The celebration", "Celebrate someone's small win loudly.", "Small wins deserve noise."),
    _msd(A, "The scholarship", "Fund a small scholarship.", "Education echoes."),
    _msd(A, "The legacy gift", "Give anonymously to a cause.", "Anonymous is purest."),
    _msd(A, "The reconciliation", "Bridge two estranged people.", "Peace made is priceless."),
    _msd(A, "The house build", "Join the volunteer build day.", "Homes built by hands."),
    _msd(A, "The debt paid", "Pay someone's small debt quietly.", "Freedom given."),
    _msd(A, "The job referral", "Refer someone who needs the break.", "Doors opened."),
    _msd(A, "The hospital visit", "Visit the lonely patient weekly.", "Presence heals."),
    _msd(A, "The eulogy gift", "Write what someone meant to you - now.", "Say it now."),
    _msd(A, "The tradition start", "Start a kindness tradition.", "Traditions outlive us."),
    _msd(A, "The forgiveness", "Forgive the old debt - money or hurt.", "Forgiveness frees two."),
    _msd(A, "The world better", "Pick up litter on your street daily.", "Streets reflect care."),
]
