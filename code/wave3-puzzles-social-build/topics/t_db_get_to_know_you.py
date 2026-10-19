# -*- coding: utf-8 -*-
"""Topic module: db-get-to-know-you. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-get-to-know-you", "name": "The Get to Know You Database", "pfx": "JAH-GTKY-",
    "tagline_pub": "Get-to-know-you questions with every prompt genuinely usable - from strangers to friends: every record carrying the question, when to ask it, and a check that it is warm and open, taught progressively along the ladder.",
    "tagline_sig": "The Signature meeting-sight: every question a Signature bridge, every answer a Signature gift. The full ladder from first hellos through real knowing to Signature-grade connection. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Get to Know You",
    "role_pub": "connection coach - writing questions that turn strangers into friends",
    "role_sig": "Signature connection coach - teaching Signature meeting-sight",
    "record_kind": "get-to-know-you record", "record_kind_plural": "get-to-know-you questions",
    "demo_kind": "bridge-proof", "demo_title": "Get to Know You Study",
    "search_ph": "Search get to know you, questions, icebreakers, new friends...",
    "chat_ph": "Ask for a get-to-know-you question...",
    "gen_blurb": "Generate clearly-labeled question studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded get-to-know-you questions, every prompt warm and open, marching toward one million records. Presented in teaching-ladder order: first hellos, real knowing, Signature-grade.",
    "reqs": "Curiosity about other people.",
    "stds": "Every question is open, kind, and stage-appropriate; the demo verifies it.",
    "cites": ["JAH Databases question quality standard v1.0"],
})


def _gtky(tier, question, when, tip):
    return T(
        tier, "Question: %s" % question[:54].rstrip(" .?") + "...",
        desc_pub='THE QUESTION:\n\n"%s"\n\nASK WHEN: %s\n\nCOACH TIP: %s'
        % (question, when, tip),
        desc_sig='Signature meeting: "%s" - a Signature bridge. The Signature edition treats every answered question as two people closer.' % question[:55],
        how_pub='Ask it: pose the question, then truly listen - the follow-up question is where friendship starts.',
        how_sig='The Signature way: answer it yourself first - shared vulnerability first.',
        keys=['Question: "%s".' % question,
              'Ask when: %s' % when,
              'Tip: %s' % tip],
        demo=("check", {"code": ["Q = %r" % question],
                        "checks": [("is_question", "Q.strip().endswith('?')"),
                                   ("open_ended", "not Q.lower().startswith(('do you','are you','have you','is it','can you','did you'))"),
                                   ("long_enough", "len(Q) > 18"),
                                   ("kind", "not any(w in Q.lower() for w in ['stupid','hate','ugly','dumb'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _gtky(B, "Where are you from originally?", "First conversations.", "Follow with what you loved about it."),
    _gtky(B, "What do you do for fun around here?", "New in town.", "Local tips bond fast."),
    _gtky(B, "How did you end up in this class?", "Classmates.", "Origin stories are easy."),
    _gtky(B, "What kind of music are you into?", "Casual chat.", "Music taste is safe and fun."),
    _gtky(B, "What food have you enjoyed most here?", "Shared places.", "Food talk is universal."),
    _gtky(B, "What shows are you watching lately?", "Small talk.", "Watchlists are windows."),
    _gtky(B, "What pets have been part of your life?", "Animal lovers.", "Pet people light up."),
    _gtky(B, "What did you do last weekend?", "Monday chat.", "Weekends reveal lives."),
    _gtky(B, "How long have you lived here?", "Neighbors.", "Tenure talk is easy."),
    _gtky(B, "What is your favorite thing about this neighborhood?", "Neighbors.", "Local love bonds."),
    _gtky(B, "Where did you go to school?", "Getting background.", "Schools shape stories."),
    _gtky(C, "What is something you're passionate about?", "Going deeper.", "Passion is attractive."),
    _gtky(C, "How do you like to spend your free time?", "Learning rhythms.", "Time reveals values."),
    _gtky(C, "What is the best advice you've gotten?", "Wisdom exchange.", "Advice reveals mentors."),
    _gtky(C, "What are you working toward right now?", "Goals talk.", "Ambitions bond."),
    _gtky(C, "What is a skill you'd love to learn?", "Aspiration.", "Dreams are fun."),
    _gtky(C, "How would your friends describe you?", "Self-view.", "Revealing and fun."),
    _gtky(C, "What is your favorite memory from last year?", "Positive reflection.", "Joy shared doubles."),
    _gtky(C, "What does your ideal weekend look like?", "Lifestyle.", "Weekends are honest."),
    _gtky(C, "What are you most grateful for these days?", "Gratitude.", "Thanks deepen talk."),
    _gtky(C, "How do you recharge when you're drained?", "Self-care.", "Reveals rhythms."),
    _gtky(C, "What is something you've changed your mind about?", "Growth.", "Change is interesting."),
    _gtky(C, "What tradition matters most to you?", "Roots.", "Traditions are stories."),
    _gtky(A, "What do you want your life to stand for?", "Deep talk.", "Legacy questions matter."),
    _gtky(A, "When did you last feel truly proud?", "Pride.", "Pride reveals values."),
    _gtky(A, "What fear have you outgrown?", "Growth.", "Outgrown fears inspire."),
    _gtky(A, "How have you changed in five years?", "Reflection.", "Change witnessed."),
    _gtky(A, "What are you still hoping for?", "Hope.", "Hope is brave."),
    _gtky(A, "Who shaped you most?", "Gratitude.", "Mentors matter."),
    _gtky(A, "What lesson took longest to learn?", "Wisdom.", "Slow lessons stick."),
    _gtky(A, "What would you tell your younger self?", "Compassion.", "Time-travel talk."),
    _gtky(A, "What does a good life mean to you?", "Philosophy.", "The big one, gently."),
    _gtky(A, "What are you working through right now?", "Trust required.", "Only with rapport."),
    _gtky(A, "When do you feel most alive?", "Vitality.", "Aliveness is beautiful."),
]
