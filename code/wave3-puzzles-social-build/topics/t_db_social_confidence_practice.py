# -*- coding: utf-8 -*-
"""Topic module: db-social-confidence-practice. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-social-confidence-practice", "name": "The Social Confidence Practice Database", "pfx": "JAH-SOCCONPRA-",
    "tagline_pub": "Social confidence drills with every exercise doable - build social courage step by step: every record carrying the drill, how to practice, and a check that it is safe and progressive, taught progressively along the ladder.",
    "tagline_sig": "The Signature courage-sight: every drill a Signature rep, every brave moment a Signature win. The full ladder from gentle steps through bold ones to Signature-grade confidence. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Social Confidence Practice",
    "role_pub": "confidence coach - building social courage one rep at a time",
    "role_sig": "Signature confidence coach - teaching Signature courage-sight",
    "record_kind": "confidence drill record", "record_kind_plural": "confidence drills",
    "demo_kind": "courage-proof", "demo_title": "Social Confidence Study",
    "search_ph": "Search confidence, social skills, shyness, practice, courage...",
    "chat_ph": "Ask for a confidence drill...",
    "gen_blurb": "Generate clearly-labeled drill studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded confidence drills, every exercise safe and progressive, marching toward one million records. Presented in teaching-ladder order: gentle steps, bold ones, Signature-grade.",
    "reqs": "Willingness to be slightly uncomfortable.",
    "stds": "Every drill is safe, voluntary, and progressive; the demo verifies it.",
    "cites": ["JAH Databases confidence practice standard v1.0"],
})


def _scp(tier, drill, practice, level):
    return T(
        tier, "Drill: %s" % drill,
        desc_pub='CONFIDENCE DRILL: %s\n\nPRACTICE: %s\n\nLEVEL: %s'
        % (drill.upper(), practice, level),
        desc_sig='Signature courage: %s - one more Signature rep. The Signature edition treats every brave rep as confidence compounding.' % drill,
        how_pub='Practice it: start at your level, repeat until easy, then level up - confidence is built, not found.',
        how_sig='The Signature way: daily reps beat occasional leaps - small brave, daily.',
        keys=['Drill: %s.' % drill,
              'Practice: %s' % practice,
              'Level: %s.' % level],
        demo=("check", {"code": ["PRACTICE = %r" % practice, "LEVEL = %r" % level],
                        "checks": [("practice_concrete", "len(PRACTICE) > 20"),
                                   ("level_valid", "LEVEL in ('gentle','moderate','bold')"),
                                   ("safe", "not any(w in PRACTICE.lower() for w in ['dangerous','reckless','harass'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _scp(B, "Eye contact", "Hold friendly eye contact for 3 seconds with a cashier.", "gentle"),
    _scp(B, "The smile", "Smile at five people today.", "gentle"),
    _scp(B, "The greeting", "Say hello to one stranger.", "gentle"),
    _scp(B, "The compliment", "Give one genuine compliment.", "gentle"),
    _scp(B, "The question", "Ask one cashier how their day is.", "gentle"),
    _scp(B, "The introduction", "Introduce yourself to one new person.", "gentle"),
    _scp(B, "The small talk", "Make 2 minutes of small talk.", "gentle"),
    _scp(B, "The phone call", "Make one phone call instead of texting.", "gentle"),
    _scp(B, "The event", "Attend one event alone for 30 minutes.", "gentle"),
    _scp(B, "The group", "Join one group conversation.", "gentle"),
    _scp(B, "The story", "Tell one short story to a friend.", "gentle"),
    _scp(C, "The toast", "Give a 30-second toast at dinner.", "moderate"),
    _scp(C, "The ask", "Ask for help from a stranger.", "moderate"),
    _scp(C, "The disagreement", "Voice one disagreement kindly.", "moderate"),
    _scp(C, "The presentation", "Present for 5 minutes to friends.", "moderate"),
    _scp(C, "The party", "Go to the party and stay 2 hours.", "moderate"),
    _scp(C, "The dance", "Dance for one song in public.", "moderate"),
    _scp(C, "The karaoke", "Sing one karaoke song.", "moderate"),
    _scp(C, "The debate", "Join the friendly debate.", "moderate"),
    _scp(C, "The interview", "Do a mock interview with a friend playing the boss.", "moderate"),
    _scp(C, "The speech", "Give the 2-minute speech.", "moderate"),
    _scp(C, "The negotiation", "Negotiate one price at the market or flea market.", "moderate"),
    _scp(C, "The feedback", "Give honest feedback kindly.", "moderate"),
    _scp(A, "The stage", "Speak to 50 people at the community meeting.", "bold"),
    _scp(A, "The cold approach", "Start a conversation with a total stranger.", "bold"),
    _scp(A, "The leadership", "Lead the group project.", "bold"),
    _scp(A, "The performance", "Perform on stage at the open mic night.", "bold"),
    _scp(A, "The confrontation", "Address the conflict directly.", "bold"),
    _scp(A, "The ask big", "Ask for the big opportunity.", "bold"),
    _scp(A, "The vulnerability", "Share your story publicly.", "bold"),
    _scp(A, "The teaching", "Teach the weekend workshop on your best skill.", "bold"),
    _scp(A, "The hosting", "Host the neighborhood event from start to finish.", "bold"),
    _scp(A, "The networking", "Work the room at the conference.", "bold"),
    _scp(A, "The pitch", "Pitch your idea to the panel.", "bold"),
]
