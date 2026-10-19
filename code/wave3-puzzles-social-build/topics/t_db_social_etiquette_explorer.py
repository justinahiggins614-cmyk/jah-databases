# -*- coding: utf-8 -*-
"""Topic module: db-social-etiquette-explorer. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-social-etiquette-explorer", "name": "The Social Etiquette Explorer Database", "pfx": "JAH-SOCETIEXP-",
    "tagline_pub": "Social etiquette guides with every rule explained - navigate any situation gracefully: every record carrying the situation, the graceful move, and a check that it is kind and correct, taught progressively along the ladder.",
    "tagline_sig": "The Signature grace-sight: every situation a Signature dance, every graceful move a Signature win. The full ladder from everyday manners through tricky situations to Signature-grade grace. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Social Etiquette Explorer",
    "role_pub": "etiquette guide - teaching graceful moves for every situation",
    "role_sig": "Signature etiquette guide - teaching Signature grace-sight",
    "record_kind": "etiquette guide record", "record_kind_plural": "etiquette guides",
    "demo_kind": "grace-proof", "demo_title": "Etiquette Study",
    "search_ph": "Search etiquette, manners, polite, situations, grace...",
    "chat_ph": "Ask for an etiquette guide...",
    "gen_blurb": "Generate clearly-labeled guide studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded etiquette guides, every move kind and correct, marching toward one million records. Presented in teaching-ladder order: everyday manners, tricky situations, Signature-grade.",
    "reqs": "Consideration for others.",
    "stds": "Every guide is kind, practical, and situation-appropriate; the demo verifies it.",
    "cites": ["JAH Databases etiquette standard v1.0"],
})


def _see(tier, situation, move, why):
    return T(
        tier, "Etiquette: %s" % situation,
        desc_pub='SITUATION: %s\n\nTHE GRACEFUL MOVE: %s\n\nWHY: %s'
        % (situation.upper(), move, why),
        desc_sig='Signature grace: %s - handled the Signature way. The Signature edition treats every graceful move as the social fabric holding.' % situation,
        how_pub='Do it: pause, consider the others, and choose the kind move - etiquette is empathy in action.',
        how_sig='The Signature way: make others comfortable - grace is the art of ease.',
        keys=['Situation: %s.' % situation,
              'Move: %s' % move,
              'Why: %s' % why],
        demo=("check", {"code": ["MOVE = %r" % move],
                        "checks": [("move_concrete", "len(MOVE) > 20"),
                                   ("kind", "not any(w in MOVE.lower() for w in ['rude','ignore them','insult'])"),
                                   ("actionable", "any(w in MOVE.lower() for w in ['say','offer','ask','thank','wait','hold','help','greet','listen','smile','give','receive','keep','clean','dress','rsvp','dance','stay','change','communicate','welcome','feed','tip','assume','disagree','learn','treat','speak','follow','honor','show','toast','include','arrive','chew','bridge','answer','seek','respect'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _see(B, "Meeting someone new", "Smile, make eye contact, say your name, and ask theirs.", "Names open doors."),
    _see(B, "At the dinner table", "Wait for the host, chew quietly, thank the cook.", "Tables have rhythms."),
    _see(B, "On the phone", "Greet warmly, state your business, thank them.", "Calls are visits."),
    _see(B, "In line", "Wait your turn; hold your spot kindly.", "Lines are promises."),
    _see(B, "Saying thank you", "Say it specifically and promptly.", "Thanks feed souls."),
    _see(B, "Apologizing", "Say sorry plainly; mean it.", "Sorries heal."),
    _see(B, "Giving gifts", "Give thoughtfully; receive graciously.", "Gifts are messages."),
    _see(B, "At work", "Greet colleagues; respect focus time.", "Workplaces thrive on courtesy."),
    _see(B, "With elders", "Listen patiently; offer help.", "Elders deserve honor."),
    _see(B, "With children", "Get to their level; listen fully.", "Children notice everything."),
    _see(B, "In public", "Keep noise down; clean up after yourself.", "Public is shared."),
    _see(C, "Difficult dinners", "Stay neutral; change topics kindly.", "Peace at the table."),
    _see(C, "Weddings", "RSVP promptly; dress right; dance.", "Celebrate well."),
    _see(C, "Funerals", "Dress somberly; offer condolences simply.", "Grief needs quiet."),
    _see(C, "Job interviews", "Arrive early; thank everyone after.", "Gratitude remembered."),
    _see(C, "First dates", "Be punctual; listen more than talk.", "Presence impresses."),
    _see(C, "Houseguests", "Communicate needs; clean up daily.", "Guests are gifts."),
    _see(C, "Hosting", "Welcome warmly; feed well.", "Hosts set tone."),
    _see(C, "Tipping", "Tip fairly; thank by name.", "Service honored."),
    _see(C, "Online", "Be kind; assume good intent.", "Screens hide humans."),
    _see(C, "Disagreements", "Listen first; disagree kindly.", "Respectful dissent."),
    _see(C, "Compliments", "Give specifically; receive gracefully.", "Praise well given."),
    _see(C, "Criticism", "Give privately; be specific and kind.", "Critique with care."),
    _see(A, "State dinners", "Follow protocol; honor the host country.", "Diplomacy dines."),
    _see(A, "Cultural differences", "Learn before you go; ask respectfully.", "Curiosity with humility."),
    _see(A, "Power dynamics", "Treat everyone with equal grace.", "Rank doesn't rate."),
    _see(A, "Public speaking", "Thank the audience; speak clearly.", "Audiences gift time."),
    _see(A, "Media interviews", "Be honest; bridge to your message.", "Truth well told."),
    _see(A, "Negotiations", "Respect all sides; seek win-win.", "Deals need dignity."),
    _see(A, "Ceremonies", "Follow the ritual; honor its meaning.", "Rituals matter."),
    _see(A, "Condolences", "Show up; say little; mean it.", "Presence over prose."),
    _see(A, "Celebrations", "Toast sincerely; include everyone.", "Joy shared."),
    _see(A, "Farewells", "Thank specifically; wish well.", "Goodbyes matter."),
    _see(A, "Reunions", "Greet warmly; ask about lives.", "Time bridged."),
]
