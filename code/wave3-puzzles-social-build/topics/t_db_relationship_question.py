# -*- coding: utf-8 -*-
"""Topic module: db-relationship-question. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-relationship-question", "name": "The Relationship Question Database", "pfx": "JAH-RELQUE-",
    "tagline_pub": "Relationship questions with every prompt deepening bonds - ask what matters: every record carrying the question, when to ask, and a check that it is respectful and open, taught progressively along the ladder.",
    "tagline_sig": "The Signature bond-sight: every question a Signature key, every answer a Signature door. The full ladder from warm-ups through deep dives to Signature-grade intimacy. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Relationship Question",
    "role_pub": "bond coach - writing questions that deepen every relationship",
    "role_sig": "Signature bond coach - teaching Signature bond-sight",
    "record_kind": "relationship question record", "record_kind_plural": "relationship questions",
    "demo_kind": "bond-proof", "demo_title": "Relationship Question Study",
    "search_ph": "Search relationship questions, deep questions, bonding, intimacy...",
    "chat_ph": "Ask for a relationship question...",
    "gen_blurb": "Generate clearly-labeled question studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded relationship questions, every prompt respectful and deepening, marching toward one million records. Presented in teaching-ladder order: warm-ups, deep dives, Signature-grade.",
    "reqs": "Someone you want to know better.",
    "stds": "Every question is open, respectful, and bond-deepening; the demo verifies it.",
    "cites": ["JAH Databases relationship question standard v1.0"],
})


def _rq(tier, question, when, depth):
    return T(
        tier, "Ask: %s" % question[:54].rstrip(" .?") + "...",
        desc_pub='THE QUESTION:\n\n"%s"\n\nASK WHEN: %s\n\nDEPTH: %s'
        % (question, when, depth),
        desc_sig='Signature bond: "%s" - a Signature key turning. The Signature edition treats every honest answer as the bond deepening.' % question[:55],
        how_pub='Ask it: pose it gently, listen fully, and answer it yourself too - mutual vulnerability builds mutual trust.',
        how_sig='The Signature way: one deep question beats ten shallow ones - go slow.',
        keys=['Question: "%s".' % question,
              'Ask when: %s' % when,
              'Depth: %s.' % depth],
        demo=("check", {"code": ["Q = %r" % question],
                        "checks": [("is_question", "Q.strip().endswith('?')"),
                                   ("open_ended", "not Q.lower().startswith(('do you','are you','have you','is it','can you','did you','will you'))"),
                                   ("long_enough", "len(Q) > 18"),
                                   ("respectful", "not any(w in Q.lower() for w in ['stupid','hate','dumb','ugly'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _rq(B, "What was the highlight of your day?", "Daily check-in.", "Warm-up"),
    _rq(B, "What are you looking forward to this week?", "Weekly rhythm.", "Warm-up"),
    _rq(B, "What made you smile today?", "Evening talk.", "Warm-up"),
    _rq(B, "How are you really doing?", "When it matters.", "Warm-up"),
    _rq(B, "What do you need most right now?", "Support moments.", "Warm-up"),
    _rq(B, "What was the best part of your weekend?", "Monday.", "Warm-up"),
    _rq(B, "What are you grateful for today?", "Daily.", "Warm-up"),
    _rq(B, "How did that go for you?", "After events.", "Warm-up"),
    _rq(B, "What would make tomorrow great?", "Evening planning.", "Warm-up"),
    _rq(B, "Who made your day better?", "Gratitude.", "Warm-up"),
    _rq(B, "What are you excited about?", "Energy check.", "Warm-up"),
    _rq(C, "When do you feel most loved?", "Deepening.", "Deep dive"),
    _rq(C, "What do you need when you're upset?", "Care mapping.", "Deep dive"),
    _rq(C, "How do you best receive love?", "Love languages.", "Deep dive"),
    _rq(C, "What are you afraid to tell me?", "Trust built.", "Deep dive"),
    _rq(C, "What do you want more of in this relationship?", "Growth.", "Deep dive"),
    _rq(C, "When did you feel closest to me?", "Bonding.", "Deep dive"),
    _rq(C, "What do you need that you're not getting?", "Honesty.", "Deep dive"),
    _rq(C, "How have I helped you grow?", "Gratitude.", "Deep dive"),
    _rq(C, "What are your dreams for us?", "Future.", "Deep dive"),
    _rq(C, "What hurts that I don't know about?", "Healing.", "Deep dive"),
    _rq(C, "How do you want to be comforted?", "Care.", "Deep dive"),
    _rq(C, "What does commitment mean to you?", "Values.", "Deep dive"),
    _rq(A, "What do you want your life to have stood for?", "Legacy.", "Signature-grade"),
    _rq(A, "When did you last change your mind about us?", "Honesty.", "Signature-grade"),
    _rq(A, "What is the hardest thing you've forgiven?", "Depth.", "Signature-grade"),
    _rq(A, "How have you changed since we met?", "Reflection.", "Signature-grade"),
    _rq(A, "What are you still hoping for?", "Hope.", "Signature-grade"),
    _rq(A, "What would you never want me to know?", "Ultimate trust.", "Signature-grade"),
    _rq(A, "How do you want to be remembered by me?", "Legacy.", "Signature-grade"),
    _rq(A, "What does forever mean to you?", "Commitment.", "Signature-grade"),
    _rq(A, "When do you feel most alive with me?", "Vitality.", "Signature-grade"),
    _rq(A, "What have I never asked you?", "Meta.", "Signature-grade"),
    _rq(A, "How will we keep choosing each other?", "Future.", "Signature-grade"),
]
