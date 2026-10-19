# -*- coding: utf-8 -*-
"""Topic module: db-boundary-setting-practice. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-boundary-setting-practice", "name": "The Boundary Setting Practice Database", "pfx": "JAH-BOUSETPRA-",
    "tagline_pub": "Boundary-setting scripts with every line respectful and firm - say no kindly and clearly: every record carrying the situation, the script, and a check that it is kind, clear, and consent-aware, taught progressively along the ladder.",
    "tagline_sig": "The Signature kind-firmness: every script a Signature line, every no a complete sentence. The full ladder from easy declines through hard conversations to Signature-grade boundaries. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Boundary Setting Practice",
    "role_pub": "boundaries coach - scripting kind, clear, firm lines for hard moments",
    "role_sig": "Signature boundaries coach - teaching Signature kind-firmness",
    "record_kind": "boundary script record", "record_kind_plural": "boundary scripts",
    "demo_kind": "script-proof", "demo_title": "Boundary Study",
    "search_ph": "Search boundaries, say no, scripts, assertive, limits...",
    "chat_ph": "Ask for a boundary script...",
    "gen_blurb": "Generate clearly-labeled script studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded boundary scripts, every line checked kind and clear, marching toward one million records. Presented in teaching-ladder order: easy declines, hard conversations, Signature-grade.",
    "reqs": "Self-respect and a willingness to be briefly uncomfortable.",
    "stds": "Every script is kind, clear, firm, and consent-aware; the demo verifies the script contains its key line.",
    "cites": ["JAH Databases respectful communication standard v1.0"],
})


def _bs(tier, situation, script, why, key_line):
    return T(
        tier, "Boundary: %s" % situation[:54].rstrip(" .?") + "...",
        desc_pub='SITUATION:\n\n%s\n\nSAY THIS:\n\n"%s"\n\nWHY IT WORKS: %s'
        % (situation, script, why),
        desc_sig='Signature kind-firmness: %s - held with a Signature line. The Signature edition treats every held boundary as self-respect made audible.' % situation[:55],
        how_pub='Practice it: say the script aloud three times, then use it for real - the first time is the hardest; it gets easier.',
        how_sig='The Signature way: no is a complete sentence - the explanation is optional, the boundary is not.',
        keys=['Situation: %s' % situation,
              'Script: "%s"' % script,
              'Why: %s' % why],
        demo=("check", {"code": ["SCRIPT = %r" % script, "KEY = %r" % key_line],
                        "checks": [("key_line_present", "KEY.lower() in SCRIPT.lower()"),
                                   ("kind_tone", "not any(w in SCRIPT.lower() for w in ['stupid','hate you','shut up'])"),
                                   ("long_enough", "len(SCRIPT) > 20")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _bs(B, "A friend asks to copy your homework.", "I'd rather not share my homework, but I'm happy to help you understand it.", "Offers help while declining the ask - kind and clear.", "rather not share"),
    _bs(B, "Someone keeps borrowing your pen without asking.", "Please ask before borrowing my things - I need my pen for class.", "Names the need plainly, no accusation.", "ask before borrowing"),
    _bs(B, "A friend wants you to skip class with them.", "I'm staying in class today - you should too, honestly.", "Declines and gently redirects.", "staying in class"),
    _bs(B, "Someone teases you about your hobby.", "I enjoy it, and the teasing isn't fun for me - please stop.", "States the feeling and the ask.", "isn't fun for me"),
    _bs(B, "A relative asks about your grades at dinner.", "I'd rather not discuss grades tonight - let's enjoy dinner.", "Deflects with warmth.", "rather not discuss"),
    _bs(B, "A friend texts you constantly during study time.", "I'm studying until 8 - I'll reply after.", "Gives a clear window, not a shutdown.", "until 8"),
    _bs(B, "Someone cuts in front of you in line.", "Excuse me - the line starts back there.", "Polite, direct, assumes nothing.", "line starts"),
    _bs(B, "A coworker dumps their work on you.", "I can't take that on - my plate is full this week.", "Cites capacity, not character.", "can't take that on"),
    _bs(B, "A friend wants to read your diary.", "My diary is private - I need you to respect that.", "Privacy stated as a need.", "is private"),
    _bs(B, "Someone pressures you to drink at a party.", "No thanks, I'm good with what I have.", "Short, cheerful, final.", "No thanks"),
    _bs(B, "A neighbor's music is too loud at night.", "Could you turn it down a bit? I need to sleep.", "Ask framed around your need.", "turn it down"),
    _bs(C, "Your boss asks you to work another weekend.", "I need this weekend off - I've worked the last three. I can help Monday.", "Shows the pattern, offers the alternative.", "need this weekend off"),
    _bs(C, "A friend always vents but never listens.", "I care about you, and I need our talks to go both ways sometimes.", "Names the imbalance kindly.", "both ways"),
    _bs(C, "Family criticizes your career choice.", "I've made my decision thoughtfully, and I need your support - or at least your respect for it.", "Asks for support, settles for respect.", "need your support"),
    _bs(C, "A partner checks your phone without asking.", "My phone is private - if you're worried, let's talk about it directly.", "Redirects snooping to conversation.", "let's talk about it"),
    _bs(C, "Someone guilt-trips you for saying no.", "I've decided, and the guilt-tripping isn't fair - please respect my no.", "Names the tactic, holds the line.", "respect my no"),
    _bs(C, "A friend shares your secrets.", "What I told you was private - I need to know I can trust you going forward.", "Makes trust the topic.", "was private"),
    _bs(C, "Your roommate never cleans.", "We need a cleaning split we both follow - let's set it tonight.", "Proposes the system, not the fight.", "cleaning split"),
    _bs(C, "Someone touches you without consent.", "Please don't touch me without asking - I need that respected.", "Clear, firm, consent-centered.", "without asking"),
    _bs(C, "A client demands instant replies at midnight.", "I reply during work hours - 9 to 6. Emergencies excepted.", "States hours, allows real emergencies.", "work hours"),
    _bs(C, "Your parent reads your messages.", "I need privacy in my messages - please don't read them.", "Need stated simply.", "need privacy"),
    _bs(C, "A friend mocks your boundaries.", "My boundaries aren't jokes - I need them taken seriously.", "Refuses to laugh it off.", "aren't jokes"),
    _bs(C, "Someone trauma-dumps on you constantly.", "I care, and I'm not equipped for this - a counselor could really help.", "Compassionate redirect to professionals.", "not equipped"),
    _bs(A, "Ending a friendship that hurts you.", "This friendship isn't healthy for me anymore - I need to step back. I wish you well.", "Kind, final, no debate invited.", "step back"),
    _bs(A, "Confronting a boss about credit theft.", "My work was presented as yours - I need that corrected going forward.", "Names the act, demands the fix.", "presented as yours"),
    _bs(A, "Telling family you need space.", "I love you, and I need some space right now - I'll reach out when I'm ready.", "Love plus need, plus your timeline.", "need some space"),
    _bs(A, "Refusing a loan to family.", "I can't lend money - it would strain us. I can help in other ways.", "Protects the relationship from the loan.", "can't lend money"),
    _bs(A, "Addressing a partner's drinking.", "I'm worried about your drinking, and I need us to talk about it honestly.", "Care plus honesty, no ultimatum yet.", "need us to talk"),
    _bs(A, "Setting limits with an intrusive in-law.", "We love having you, and visits need planning - let's schedule them.", "Welcome plus structure.", "need planning"),
    _bs(A, "Quitting a toxic job respectfully.", "I'm resigning - my last day is in two weeks. Thank you for the opportunity.", "Professional to the end.", "I'm resigning"),
    _bs(A, "Telling a friend their jokes hurt.", "Those jokes land as insults for me - I need them to stop.", "Impact stated, ask clear.", "need them to stop"),
    _bs(A, "Boundaries after betrayal.", "Trust is broken - I need time and changed behavior before we rebuild.", "Names the price of repair.", "Trust is broken"),
    _bs(A, "Saying no to a wedding party role.", "I'm honored, but I can't take that on - I'll celebrate with you fully.", "Honor plus decline plus presence.", "can't take that on"),
    _bs(A, "Limiting contact with a draining relative.", "I'll call on Sundays - that's what I can offer right now.", "Defines the exact offer.", "on Sundays"),
]
