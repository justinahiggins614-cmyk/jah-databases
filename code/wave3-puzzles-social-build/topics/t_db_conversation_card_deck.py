# -*- coding: utf-8 -*-
"""Topic module: db-conversation-card-deck. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-conversation-card-deck", "name": "The Conversation Card Deck Database", "pfx": "JAH-CONCARDDE-",
    "tagline_pub": "Conversation cards with every prompt genuinely usable - draw a card, start talking: every record carrying the card's question, why it works, and a check that it is open and kind, taught progressively along the ladder.",
    "tagline_sig": "The Signature talking-sight: every card a Signature door, every answer a Signature gift. The full ladder from easy cards through deep ones to Signature-grade conversations. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Conversation Card Deck",
    "role_pub": "card master - dealing prompts that open real conversations",
    "role_sig": "Signature card master - teaching Signature talking-sight",
    "record_kind": "conversation card record", "record_kind_plural": "conversation cards",
    "demo_kind": "card-proof", "demo_title": "Conversation Card Study",
    "search_ph": "Search conversation, cards, questions, icebreakers, talk...",
    "chat_ph": "Ask for a conversation card...",
    "gen_blurb": "Generate clearly-labeled card studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded conversation cards, every prompt open and kind, marching toward one million records. Presented in teaching-ladder order: easy cards, deep ones, Signature-grade.",
    "reqs": "People and a willingness to listen.",
    "stds": "Every card asks an open question that invites real answers; the demo verifies openness.",
    "cites": ["JAH Databases conversation quality standard v1.0"],
})


def _cc(tier, question, why, followup):
    return T(
        tier, "Card: %s" % question[:54].rstrip(" .?") + "...",
        desc_pub='THE CARD:\n\n"%s"\n\nWHY IT WORKS: %s\n\nFOLLOW-UP: %s'
        % (question, why, followup),
        desc_sig='Signature talking: "%s" - a Signature door opening. The Signature edition treats every answered card as two people meeting properly.' % question[:55],
        how_pub='Play it: draw a card, answer it yourself first, then ask - vulnerability invites vulnerability.',
        how_sig='The Signature way: listen to the whole answer before your next card - the follow-up is the game.',
        keys=['Card: "%s".' % question,
              'Why it works: %s' % why,
              'Follow-up: %s' % followup],
        demo=("check", {"code": ["Q = %r" % question],
                        "checks": [("is_question", "Q.strip().endswith('?')"),
                                   ("open_ended", "not Q.lower().startswith(('do you','are you','have you','is it','can you'))"),
                                   ("long_enough", "len(Q) > 20"),
                                   ("kind", "not any(w in Q.lower() for w in ['stupid','hate','ugly'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _cc(B, "What is your favorite way to spend a free afternoon?", "Easy, positive, and revealing.", "What makes that so enjoyable?"),
    _cc(B, "What food could you eat every week without getting bored?", "Everyone has an answer; joy is universal.", "What is the perfect version of it?"),
    _cc(B, "What is a small thing that always makes you smile?", "Small joys are safe and sweet.", "When did you last notice it?"),
    _cc(B, "If you could learn any skill instantly, what would it be?", "Dreams are fun to share.", "What would you do with it first?"),
    _cc(B, "What is your favorite season, and why?", "Opinions without stakes.", "What is your best memory of it?"),
    _cc(B, "What movie have you watched more than twice?", "Comfort watches reveal comfort.", "What keeps you coming back?"),
    _cc(B, "What is the best trip you have ever taken?", "Travel stories are gifts.", "What surprised you most there?"),
    _cc(B, "What hobby have you always wanted to try?", "Aspiration is bonding.", "What stops you from starting?"),
    _cc(B, "What is your go-to comfort food?", "Comfort is intimate but safe.", "Who made it best?"),
    _cc(B, "If you had a free Saturday with no obligations, what would you do?", "Freedom fantasies are joyful.", "Who would you bring?"),
    _cc(B, "What song never fails to lift your mood?", "Music is memory.", "What memory does it carry?"),
    _cc(C, "What is something you believed as a kid that turned out wrong?", "Funny and humanizing.", "How did you find out?"),
    _cc(C, "What is the most useful thing anyone ever taught you?", "Gratitude plus wisdom.", "Who taught it?"),
    _cc(C, "What would you do differently if you could relive one year?", "Reflective without being heavy.", "What did that year teach you?"),
    _cc(C, "What is a tradition from your family you want to keep?", "Roots and values.", "How did it start?"),
    _cc(C, "When do you feel most like yourself?", "Identity, gently asked.", "What brings that feeling?"),
    _cc(C, "What is the kindest thing a stranger ever did for you?", "Kindness stories heal.", "Did you pay it forward?"),
    _cc(C, "What fear have you mostly outgrown?", "Growth, honestly shared.", "What helped you outgrow it?"),
    _cc(C, "What is something you're proud of that few people know?", "Hidden pride deserves air.", "Why haven't you shared it?"),
    _cc(C, "If you could have dinner with anyone, living or not, who?", "Values in disguise.", "What would you ask them?"),
    _cc(C, "What is the best advice you've ever received?", "Wisdom exchange.", "Did you follow it?"),
    _cc(C, "What small habit improved your life most?", "Practical intimacy.", "How did you start it?"),
    _cc(C, "What place feels like home to you, and why?", "Belonging, explored.", "What makes it home?"),
    _cc(A, "What do you want your life to have stood for?", "Legacy, asked with care.", "What step moves toward it?"),
    _cc(A, "When did you last change your mind about something important?", "Intellectual honesty.", "What changed it?"),
    _cc(A, "What is the hardest thing you've ever forgiven?", "Depth with consent - only with trust.", "What made forgiveness possible?"),
    _cc(A, "What would you attempt if you knew you couldn't fail?", "Dreams without fear.", "What's the first small step?"),
    _cc(A, "How have you changed most in the last five years?", "Growth, witnessed.", "What caused the change?"),
    _cc(A, "What does a good life mean to you?", "Philosophy, personally.", "Are you living it?"),
    _cc(A, "What are you still hoping for?", "Hope is vulnerable and brave.", "What keeps the hope alive?"),
    _cc(A, "What lesson took you longest to learn?", "Wisdom earned slowly.", "What finally taught it?"),
    _cc(A, "Who shaped you most, and how?", "Gratitude with depth.", "Have you told them?"),
    _cc(A, "What would you tell your younger self?", "Compassion across time.", "Would they listen?"),
    _cc(A, "What are you most grateful for right now?", "Presence and thanks.", "How do you show it?"),
]
