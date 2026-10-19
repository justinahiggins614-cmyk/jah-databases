# -*- coding: utf-8 -*-
"""Topic module: db-difficult-conversation-helper. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-difficult-conversation-helper", "name": "The Difficult Conversation Helper Database", "pfx": "JAH-DIFCONHEL-",
    "tagline_pub": "Difficult conversation guides with every approach kind and honest - say the hard thing well: every record carrying the conversation, the opener, the structure, and a check that it is respectful and clear, taught progressively along the ladder.",
    "tagline_sig": "The Signature courage-sight: every hard talk a Signature bridge, every honest word a Signature gift. The full ladder from small hards through big ones to Signature-grade honesty. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Difficult Conversation Helper",
    "role_pub": "honesty coach - scripting hard conversations that heal instead of harm",
    "role_sig": "Signature honesty coach - teaching Signature courage-sight",
    "record_kind": "conversation guide record", "record_kind_plural": "conversation guides",
    "demo_kind": "talk-proof", "demo_title": "Difficult Conversation Study",
    "search_ph": "Search difficult conversations, hard talks, honesty, feedback...",
    "chat_ph": "Ask for a conversation guide...",
    "gen_blurb": "Generate clearly-labeled guide studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded conversation guides, every approach kind and honest, marching toward one million records. Presented in teaching-ladder order: small hards, big ones, Signature-grade.",
    "reqs": "Courage and care in equal measure.",
    "stds": "Every guide uses 'I' language, states needs clearly, and invites dialogue; never attacks.",
    "cites": ["JAH Databases honest communication standard v1.0"],
})


def _dc2(tier, topic, opener, structure, tip):
    return T(
        tier, "Hard talk: %s" % topic[:54].rstrip(" .?") + "...",
        desc_pub='THE CONVERSATION: %s\n\nOPEN WITH:\n\n"%s"\n\nSTRUCTURE:\n%s\n\nCOACH TIP: %s'
        % (topic, opener, "\n".join("  %d. %s" % (i + 1, s) for i, s in enumerate(structure)), tip),
        desc_sig='Signature courage: %s - said the Signature way. The Signature edition treats every hard talk had well as the relationship getting stronger.' % topic[:55],
        how_pub='Have it: pick a calm time, use the opener, follow the structure - and listen as much as you speak.',
        how_sig='The Signature way: state the need before the complaint - needs invite help; complaints invite defense.',
        keys=['Topic: %s' % topic,
              'Opener: "%s"' % opener,
              'Structure: %d steps.' % len(structure),
              'Tip: %s' % tip],
        demo=("check", {"code": ["OPENER = %r" % opener, "STRUCT = %r" % structure,
                                  "WORDS = OPENER.lower().replace(chr(39), \" \").split()",
                                  "HAS_I = any(w in WORDS for w in [\"i\", \"im\", \"ive\", \"my\", \"we\"]) or any(p in OPENER.lower() for p in [\"i feel\", \"i need\", \"i want\"])"],
                        "checks": [("opener_uses_i_language", "HAS_I"),
                                   ("structure_present", "len(STRUCT) >= 3"),
                                   ("kind", "not any(w in (OPENER + ' '.join(STRUCT)).lower() for w in ['you always','you never','stupid','idiot'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _dc2(B, "Telling a friend they hurt your feelings.", "I felt hurt when that happened, and I wanted you to know.", ["Say what happened, plainly.", "Say how it felt.", "Say what you need going forward.", "Listen to their side."], "Feelings first, facts second."),
    _dc2(B, "Asking a roommate to clean up.", "I need our place cleaner - can we talk about a plan?", ["Name the specific mess.", "Propose a schedule.", "Agree together.", "Check in weekly."], "Specific beats general."),
    _dc2(B, "Declining extra work politely.", "I'm at capacity right now, and I want to be honest about that.", ["State your current load.", "Decline clearly.", "Offer what you CAN do.", "Suggest who else could help."], "Honesty now prevents resentment later."),
    _dc2(B, "Telling someone their joke offended you.", "That joke didn't land well for me - can I tell you why?", ["Name the joke.", "Explain the impact.", "Ask for care going forward."], "Impact, not intent, is the topic."),
    _dc2(B, "Asking for a raise.", "I'd like to discuss my compensation - I've grown in this role.", ["List your contributions.", "Name the number.", "Listen to the response.", "Agree on next steps."], "Numbers beat nerves."),
    _dc2(B, "Ending a subscription or commitment.", "I need to step back from this commitment.", ["Be direct and early.", "Give the reason briefly.", "Thank them.", "Offer a transition."], "Early and direct is kindest."),
    _dc2(B, "Telling a friend you need space.", "I care about you, and I need a little space right now.", ["Affirm the friendship.", "Name the need.", "Set the timeframe.", "Reconnect as promised."], "Space with a return date."),
    _dc2(B, "Giving gentle feedback.", "Can I share an observation? I think it'd help.", ["Ask permission.", "Be specific.", "Offer support.", "Follow up kindly."], "Permission first."),
    _dc2(B, "Saying no to a favor.", "I can't do that one - my plate's full.", ["Decline clearly.", "Keep it brief.", "Offer an alternative if you can."], "Brief is kind."),
    _dc2(B, "Addressing lateness.", "I've noticed the lateness, and it affects me - can we talk?", ["Name the pattern.", "Say the impact.", "Ask what's going on.", "Agree on a fix."], "Curiosity before conclusions."),
    _dc2(B, "Talking about money with friends.", "I want us to be comfortable - can we talk budget?", ["Name the concern.", "Propose options.", "Agree together."], "Money talk prevents money fights."),
    _dc2(C, "Confronting a partner about distance.", "I've been feeling distant from you, and I miss us.", ["Share the feeling.", "Ask about their experience.", "Name one need each.", "Plan connection time."], "Miss-us beats blame-you."),
    _dc2(C, "Telling your boss you're overwhelmed.", "I'm overwhelmed, and I want to solve it before it affects my work.", ["Name the load.", "Show the impact.", "Propose priorities.", "Ask for support."], "Solutions, not just stress."),
    _dc2(C, "Discussing a parent's driving.", "I'm worried about your safety on the road - can we talk?", ["Lead with love.", "Name specific incidents.", "Offer alternatives.", "Involve them in the plan."], "Dignity throughout."),
    _dc2(C, "Addressing a friend's drinking.", "I'm worried about you, and I care too much to stay quiet.", ["Name what you've seen.", "Say you care.", "Offer support.", "Set your own boundary."], "Care plus boundary."),
    _dc2(C, "Negotiating with a difficult client.", "I want this to work for both of us - let's reset.", ["Name the friction.", "Restate the shared goal.", "Propose terms.", "Get it in writing."], "Shared goal first."),
    _dc2(C, "Telling family about a big decision.", "I've made a big decision I want to share with you.", ["Share the decision.", "Explain your reasoning.", "Ask for support.", "Give them time."], "Share, don't seek permission."),
    _dc2(C, "Apologizing sincerely.", "I was wrong, and I'm sorry - no excuses.", ["Name what you did.", "Say the impact you see.", "Ask how to repair.", "Change visibly."], "No 'but' after sorry."),
    _dc2(C, "Setting boundaries with in-laws.", "We love you, and we need to set some rhythms that work for us.", ["Affirm love.", "Name the need.", "Propose the rhythm.", "Hold kindly."], "Love plus structure."),
    _dc2(C, "Discussing chores with a partner.", "I feel the load is uneven - can we rebalance?", ["Name the feeling.", "Show the split.", "Redesign together.", "Review monthly."], "Data plus feelings."),
    _dc2(C, "Firing someone kindly.", "This isn't working out, and I want to handle it respectfully.", ["Be direct.", "Name the reasons briefly.", "Offer support.", "Part with dignity."], "Direct is kind."),
    _dc2(C, "Talking to kids about divorce.", "We love you, and some things are changing.", ["Lead with love.", "Be age-honest.", "Reassure concretely.", "Keep routines."], "Love, honesty, routine."),
    _dc2(C, "Addressing gossip.", "I heard something that concerns me - is it true?", ["Name what you heard.", "Ask directly.", "Listen fully.", "Decide together."], "Direct beats detective."),
    _dc2(A, "Ending a long friendship.", "This friendship isn't working for me anymore, and I owe you honesty.", ["Be honest and kind.", "Name the pattern.", "Don't debate.", "Wish well."], "Honest endings are gifts."),
    _dc2(A, "Confronting infidelity.", "I know what happened, and we need to talk honestly.", ["State what you know.", "Ask for truth.", "Name your needs.", "Decide with support."], "Truth first, decisions second."),
    _dc2(A, "Intervention for addiction.", "We love you, and we're worried - will you listen?", ["Gather the team.", "Write specific concerns.", "Offer treatment.", "Set boundaries."], "Love plus consequences."),
    _dc2(A, "Discussing end-of-life wishes.", "I want to honor your wishes - can we talk about them?", ["Ask gently.", "Listen deeply.", "Write it down.", "Share with family."], "Honor through asking."),
    _dc2(A, "Reporting wrongdoing.", "I've seen something I can't ignore.", ["Document facts.", "Use proper channels.", "Protect yourself.", "Persist."], "Courage with records."),
    _dc2(A, "Leaving a faith community.", "My beliefs have changed, and I'm stepping back.", ["Be honest.", "Thank sincerely.", "Set boundaries.", "Keep kind ties."], "Honest exits keep doors open."),
    _dc2(A, "Confronting abuse.", "What's happening is not okay, and I need it to stop.", ["Name it plainly.", "State the boundary.", "Get support.", "Prioritize safety."], "Safety first, always."),
    _dc2(A, "Negotiating a divorce.", "I want this to be fair and kind.", ["Name the goal.", "Disclose fully.", "Mediate first.", "Protect the kids."], "Fair and kind is possible."),
    _dc2(A, "Telling the truth after years.", "There's something I've hidden, and you deserve the truth.", ["Tell it all.", "Accept anger.", "Answer everything.", "Change visibly."], "Full truth, full patience."),
    _dc2(A, "Quitting a dream gracefully.", "I'm letting this dream go, and I'm at peace.", ["Name the decision.", "Honor what it gave.", "Choose the next.", "Celebrate the pivot."], "Endings are beginnings."),
    _dc2(A, "Asking for help when proud.", "I need help, and it's hard for me to say.", ["Admit the need.", "Be specific.", "Accept graciously.", "Thank sincerely."], "Asking is strength."),
]
