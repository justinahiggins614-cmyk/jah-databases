# -*- coding: utf-8 -*-
"""Topic module: db-welcome-to-the-group. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-welcome-to-the-group", "name": "The Welcome to the Group Database", "pfx": "JAH-WELTOGRO-",
    "tagline_pub": "Group welcome guides with every newcomer embraced - make everyone belong: every record carrying the situation, the welcome move, and a check that it is warm and inclusive, taught progressively along the ladder.",
    "tagline_sig": "The Signature welcome-sight: every newcomer a Signature guest, every welcome a Signature embrace. The full ladder from easy hellos through real inclusion to Signature-grade belonging. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Welcome to the Group",
    "role_pub": "welcoming coach - making every newcomer feel they belong",
    "role_sig": "Signature welcoming coach - teaching Signature welcome-sight",
    "record_kind": "welcome guide record", "record_kind_plural": "welcome guides",
    "demo_kind": "belong-proof", "demo_title": "Welcome Study",
    "search_ph": "Search welcome, newcomers, inclusion, belonging, groups...",
    "chat_ph": "Ask for a welcome guide...",
    "gen_blurb": "Generate clearly-labeled welcome studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded welcome guides, every move warm and inclusive, marching toward one million records. Presented in teaching-ladder order: easy hellos, real inclusion, Signature-grade.",
    "reqs": "An open circle.",
    "stds": "Every guide is warm, inclusive, and actionable; the demo verifies it.",
    "cites": ["JAH Databases welcoming standard v1.0"],
})


def _wtg(tier, situation, move, why):
    return T(
        tier, "Welcome: %s" % situation,
        desc_pub='SITUATION: %s\n\nTHE WELCOME MOVE: %s\n\nWHY IT WORKS: %s'
        % (situation.upper(), move, why),
        desc_sig='Signature welcome: %s - embraced the Signature way. The Signature edition treats every welcomed newcomer as the circle proving its worth.' % situation,
        how_pub='Do it: notice the newcomer, make the first move, and follow up - belonging takes three touches.',
        how_sig='The Signature way: learn their name and use it - names are the first belonging.',
        keys=['Situation: %s.' % situation,
              'Move: %s' % move,
              'Why: %s' % why],
        demo=("check", {"code": ["MOVE = %r" % move],
                        "checks": [("move_concrete", "len(MOVE) > 20"),
                                   ("inclusive", "not any(w in MOVE.lower() for w in ['ignore','exclude','clique'])"),
                                   ("welcoming", "any(w in MOVE.lower() for w in ['welcome','invite','introduce','greet','include','show','offer','ask','smile'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _wtg(B, "New kid at school", "Greet them warmly, show them around, and invite them to sit with you at lunch.", "First-day kindness remembered forever."),
    _wtg(B, "New coworker", "Welcome them, offer help, and invite them to lunch.", "Work friends start day one."),
    _wtg(B, "New neighbor", "Knock with a welcome note and introduce yourself.", "Neighbors become friends."),
    _wtg(B, "New club member", "Introduce them around and pair them with a buddy.", "Buddies prevent lost newcomers."),
    _wtg(B, "New in the group chat", "Greet them, explain the jokes, include them.", "Chats have cultures; share them."),
    _wtg(B, "New teammate", "Welcome them to the team; show them the ropes.", "Teams thrive on welcome."),
    _wtg(B, "New student in class", "Smile, share your notes, invite them to study.", "Notes shared are friendships started."),
    _wtg(B, "Guest at dinner", "Welcome them warmly; include them in conversation.", "Guests should glow."),
    _wtg(B, "New volunteer", "Thank them, show them the work, pair them up.", "Volunteers stay where welcomed."),
    _wtg(B, "New in the neighborhood", "Invite them to the block event.", "Events enroll."),
    _wtg(B, "Plus-one at the party", "Greet them, introduce them around.", "Plus-ones need allies."),
    _wtg(C, "New in-law", "Welcome them genuinely; include them in traditions.", "Family grows by welcome."),
    _wtg(C, "New boss", "Offer help learning the ropes; be patient.", "Bosses are newcomers too."),
    _wtg(C, "Stepfamily blending", "Include everyone; create new traditions.", "Blending takes welcome."),
    _wtg(C, "New roommate", "Welcome them; set expectations kindly; share the space.", "Homes need harmony."),
    _wtg(C, "New team lead", "Welcome them; support their start; share context.", "Leaders need welcome too."),
    _wtg(C, "Exchange student", "Show them the town; include them daily.", "Far from home needs near friends."),
    _wtg(C, "New parent in the group", "Include the kids; invite the family.", "Families welcome families."),
    _wtg(C, "Returning member", "Welcome them back warmly; catch them up.", "Returnees need re-welcome."),
    _wtg(C, "New believer", "Welcome without pressure; answer questions.", "Faith welcomes gently."),
    _wtg(C, "New hobbyist", "Welcome them; teach the basics; cheer their progress.", "Beginners become regulars."),
    _wtg(C, "Newly single friend", "Include them; don't pity.", "Dignity in welcome."),
    _wtg(C, "New citizen", "Welcome them; celebrate with them; help them belong.", "Belonging is the gift."),
    _wtg(A, "The outsider", "Invite them in deliberately; learn their story.", "Outsiders become insiders."),
    _wtg(A, "The rival group", "Welcome rivals to the joint event.", "Rivals can become allies."),
    _wtg(A, "The different one", "Welcome their difference openly; celebrate it.", "Difference enriches."),
    _wtg(A, "The quiet one", "Greet them warmly; draw them out gently; value their quiet.", "Quiet voices matter."),
    _wtg(A, "The struggling one", "Offer help without pity.", "Dignity always."),
    _wtg(A, "The former enemy", "Welcome the reconciliation.", "Peace welcomed."),
    _wtg(A, "The next generation", "Welcome them in; hand over with grace; mentor.", "Legacies transfer."),
    _wtg(A, "The prodigal", "Welcome home without lecture.", "Home is home."),
    _wtg(A, "The stranger", "Greet them as a friend not yet known.", "Strangers are friends early."),
    _wtg(A, "The future", "Welcome change itself.", "Change welcomed."),
    _wtg(A, "Everyone", "Build the culture where all are welcome.", "Culture is the ultimate welcome."),
]
