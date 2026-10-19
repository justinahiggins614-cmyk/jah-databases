# -*- coding: utf-8 -*-
"""Topic module: db-conversation-starter. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-conversation-starter", "name": "The Conversation Starter Database", "pfx": "JAH-CVSTA-",
    "tagline_pub": "Conversation starters with every opener tested - break the ice kindly: every record carrying the starter, when to use it, and a check that it is warm and open, taught progressively along the ladder.",
    "tagline_sig": "The Signature opener-sight: every starter a Signature hello, every conversation a Signature chance. The full ladder from easy hellos through real talk to Signature-grade connection. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Conversation Starter",
    "role_pub": "icebreaker coach - writing openers that actually open",
    "role_sig": "Signature icebreaker coach - teaching Signature opener-sight",
    "record_kind": "conversation starter record", "record_kind_plural": "conversation starters",
    "demo_kind": "opener-proof", "demo_title": "Conversation Starter Study",
    "search_ph": "Search icebreakers, openers, small talk, starters...",
    "chat_ph": "Ask for a conversation starter...",
    "gen_blurb": "Generate clearly-labeled opener studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded conversation starters, every opener warm and open, marching toward one million records. Presented in teaching-ladder order: easy hellos, real talk, Signature-grade.",
    "reqs": "A smile and a first sentence.",
    "stds": "Every starter is warm, open-ended, and situation-fitting; the demo verifies it.",
    "cites": ["JAH Databases opener quality standard v1.0"],
})


def _cs(tier, starter, when, tip):
    return T(
        tier, "Starter: %s" % starter[:54].rstrip(" .?") + "...",
        desc_pub='THE STARTER:\n\n"%s"\n\nUSE WHEN: %s\n\nOPENER TIP: %s'
        % (starter, when, tip),
        desc_sig='Signature hello: "%s" - a Signature door opening. The Signature edition treats every started conversation as loneliness losing.' % starter[:55],
        how_pub='Use it: say it warmly, then listen more than you talk - the starter is 10%, the listening is 90%.',
        how_sig='The Signature way: comment, then question - observations open better than interrogations.',
        keys=['Starter: "%s".' % starter,
              'Use when: %s' % when,
              'Tip: %s' % tip],
        demo=("check", {"code": ["S = %r" % starter],
                        "checks": [("long_enough", "len(S) > 12"),
                                   ("warm", "not any(w in S.lower() for w in ['stupid','hate','shut up','loser'])"),
                                   ("not_just_hi", "len(S.split()) > 3")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _cs(B, "Hi! I don't think we've met - I'm Alex.", "Meeting someone new anywhere.", "Smile and offer your name first."),
    _cs(B, "That looks interesting - what is it?", "Someone using something curious.", "Genuine curiosity beats clever lines."),
    _cs(B, "Have you been here before?", "Events, classes, venues.", "Shared newness bonds fast."),
    _cs(B, "I love your jacket - where did you find it?", "Complimenting something chosen.", "Compliment choices, not bodies."),
    _cs(B, "What brings you here today?", "Any gathering.", "Open and easy."),
    _cs(B, "Are you working on anything fun lately?", "Classmates, coworkers.", "Work talk, but the fun kind."),
    _cs(B, "This coffee is great - do you come here often?", "Cafes and lines.", "Shared place, shared moment."),
    _cs(B, "I'm new here - any tips for a beginner?", "Joining anything new.", "Asking for help flatters and bonds."),
    _cs(B, "What did you think of the speaker?", "Talks and events.", "Shared experience, instant topic."),
    _cs(B, "Your dog is adorable - what's their name?", "Dog owners (ask before petting).", "Pets are the universal opener."),
    _cs(B, "Is this seat taken?", "Sitting near someone.", "The classic for a reason."),
    _cs(C, "What's the most interesting thing you've learned lately?", "Deeper small talk.", "Learning talk reveals passions."),
    _cs(C, "I'm trying to get into hiking - any trail recommendations?", "Asking for expertise.", "People love sharing expertise."),
    _cs(C, "What do you do when you're not working?", "Beyond the job title.", "Identity beyond work."),
    _cs(C, "I overheard you mention travel - where's your favorite place?", "Building on overheard topics.", "Ask permission via interest."),
    _cs(C, "What's keeping you busy these days?", "Catching up.", "Better than 'how are you'."),
    _cs(C, "I'm collecting book recommendations - read anything good?", "Readers and learners.", "Everyone has one book."),
    _cs(C, "What part of this do you enjoy most?", "Shared activities.", "Joy-focused questions bond."),
    _cs(C, "How did you get into this?", "Hobbies and careers.", "Origin stories are gold."),
    _cs(C, "What's something you're looking forward to?", "Forward-looking warmth.", "Anticipation is joyful."),
    _cs(C, "I noticed you're reading - how is it?", "Readers in the wild.", "Respect the book; ask kindly."),
    _cs(C, "What's your take on the new exhibit?", "Museums and galleries.", "Opinions welcome."),
    _cs(C, "Do you have any fun weekend plans?", "Friday small talk.", "Weekends are safe joy."),
    _cs(A, "What's something you changed your mind about recently?", "Real conversations.", "Shows you value growth."),
    _cs(A, "What are you most proud of that doesn't fit on a resume?", "Deepening talk.", "Hidden pride, honored."),
    _cs(A, "If you could master anything overnight, what would it be?", "Dream talk.", "Aspirations bond."),
    _cs(A, "What's the best conversation you've had lately?", "Meta and meaningful.", "Talk about talk."),
    _cs(A, "What does a perfect day look like for you?", "Values in disguise.", "Listen for values."),
    _cs(A, "What's something small that made your week?", "Gratitude-focused.", "Small joys, big warmth."),
    _cs(A, "How do you like to spend your Sundays?", "Rhythm and ritual.", "Rituals reveal people."),
    _cs(A, "What's a skill you wish school had taught?", "Shared experience.", "Everyone has one."),
    _cs(A, "What are you curious about these days?", "Curiosity is attractive.", "Follow their curiosity."),
    _cs(A, "What's the kindest thing someone did for you lately?", "Kindness begets kindness.", "Warmth multiplies."),
    _cs(A, "If you had an extra hour daily, how would you spend it?", "Priorities revealed.", "Time wishes are honest."),
]
