# -*- coding: utf-8 -*-
"""Topic module: db-couples-challenge. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-couples-challenge", "name": "The Couples Challenge Database", "pfx": "JAH-COUCHA-",
    "tagline_pub": "Couples challenges with every activity kind and connecting - grow together: every record carrying the challenge, how to play, and a check that it is positive and consent-aware, taught progressively along the ladder.",
    "tagline_sig": "The Signature together-sight: every challenge a Signature date, every completed one a Signature memory. The full ladder from sweet games through deep dives to Signature-grade bonding. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Couples Challenge",
    "role_pub": "togetherness coach - dealing challenges that connect couples",
    "role_sig": "Signature togetherness coach - teaching Signature together-sight",
    "record_kind": "couples challenge record", "record_kind_plural": "couples challenges",
    "demo_kind": "bond-proof", "demo_title": "Couples Challenge Study",
    "search_ph": "Search couples, date night, challenges, together, bonding...",
    "chat_ph": "Ask for a couples challenge...",
    "gen_blurb": "Generate clearly-labeled challenge studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded couples challenges, every activity positive and consent-aware, marching toward one million records. Presented in teaching-ladder order: sweet games, deep dives, Signature-grade.",
    "reqs": "A partner and playful honesty.",
    "stds": "Every challenge is positive, respectful, and consent-aware; both partners must be willing.",
    "cites": ["JAH Databases relationship positivity standard v1.0"],
})


def _cc(tier, title, how, win):
    return T(
        tier, "Challenge: %s" % title,
        desc_pub='COUPLES CHALLENGE: %s\n\nHOW TO PLAY: %s\n\nYOU WIN WHEN: %s'
        % (title.upper(), how, win),
        desc_sig='Signature together: %s - a Signature memory in the making. The Signature edition treats every completed challenge as the bond getting stronger.' % title,
        how_pub='Play it: agree to the challenge together, play kindly, and debrief after - the talk after is half the game.',
        how_sig='The Signature way: lose gracefully, win kindly - the challenge serves the couple, not the score.',
        keys=['Challenge: %s.' % title,
              'How: %s' % how,
              'Win: %s' % win],
        demo=("check", {"code": ["HOW = %r" % how, "WIN = %r" % win],
                        "checks": [("how_concrete", "len(HOW) > 20"),
                                   ("win_clear", "len(WIN) > 10"),
                                   ("kind", "not any(w in (HOW+WIN).lower() for w in ['humiliat','punish','force'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _cc(B, "The Compliment Shower", "Take turns giving genuine compliments for 5 minutes.", "You both feel warm and seen."),
    _cc(B, "The Cook-Off", "Each cooks a dish; the other judges kindly.", "Dinner is delicious either way."),
    _cc(B, "The Memory Lane", "Share your three favorite memories together.", "You both smile at the same ones."),
    _cc(B, "The No-Phone Dinner", "Phones in another room for the whole meal.", "You talk for an hour straight."),
    _cc(B, "The Stargazing Date", "Lie back and name constellations together.", "You spot five together."),
    _cc(B, "The Playlist Swap", "Make each other a 5-song playlist.", "You both love at least one new song."),
    _cc(B, "The Picnic Surprise", "One plans a surprise picnic; the other just shows up.", "The surprise lands."),
    _cc(B, "The Love Note Hunt", "Hide five notes; the other finds them.", "All five are found and read aloud."),
    _cc(B, "The Dance Lesson", "Learn a dance from a video together.", "You can do the steps (badly counts)."),
    _cc(B, "The Photo Walk", "Walk and photograph ten beautiful things.", "You compare favorites after."),
    _cc(B, "The Breakfast in Bed", "One serves the other breakfast in bed.", "It's eaten with joy."),
    _cc(C, "The 36 Questions", "Ask each other the famous 36 questions.", "You finish all 36 honestly."),
    _cc(C, "The Dream Map", "Draw your shared 5-year dream on one page.", "The page is full and exciting."),
    _cc(C, "The Gratitude Week", "Share one gratitude daily for a week.", "Seven days, seven gratitudes."),
    _cc(C, "The Skill Swap", "Teach each other your best skill.", "You can both do the basics."),
    _cc(C, "The Volunteer Date", "Volunteer together for a day.", "You help someone together."),
    _cc(C, "The No-Spend Weekend", "A full fun weekend spending nothing.", "Monday arrives and it was great."),
    _cc(C, "The Letter Exchange", "Write love letters; read them aloud.", "There are happy tears."),
    _cc(C, "The Adventure Draw", "Write 20 date ideas; draw one blind.", "You do whatever comes out."),
    _cc(C, "The Interview", "Interview each other like journalists.", "You learn three new things."),
    _cc(C, "The Time Capsule", "Bury a box to open in 5 years.", "It's sealed with a date."),
    _cc(C, "The Apology Audit", "Each shares one small hurt; repair it.", "Both feel heard."),
    _cc(C, "The Silent Hike", "Hike an hour in comfortable silence.", "The silence feels good."),
    _cc(A, "The Life Story Night", "Tell your full life story in one evening.", "You both feel deeply known."),
    _cc(A, "The Fear Share", "Share your biggest fear; hold space.", "No fixing, just holding."),
    _cc(A, "The Values Summit", "Rank your top 5 values; compare.", "You understand each other's top 3."),
    _cc(A, "The Forgiveness Ritual", "Name old hurts; forgive out loud.", "The air feels lighter."),
    _cc(A, "The Future Self Letters", "Write to each other from 10 years ahead.", "You read them together, amazed."),
    _cc(A, "The Hard Conversation", "Discuss the topic you've avoided.", "You finish closer, not further."),
    _cc(A, "The Vow Renewal", "Write new vows; speak them.", "You mean every word."),
    _cc(A, "The Couple's Legacy", "Start something together that outlasts you both.", "The first step is taken."),
    _cc(A, "The Unplugged Weekend", "48 hours, no screens, just each other.", "You don't miss the screens."),
    _cc(A, "The Gratitude Marathon", "100 gratitudes in one sitting.", "You reach 100."),
    _cc(A, "The Dream Trip Plan", "Plan the dream trip in detail.", "The itinerary exists."),
]
