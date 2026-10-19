# -*- coding: utf-8 -*-
"""Topic module: db-intergenerational-activity. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-intergenerational-activity", "name": "The Intergenerational Activity Database", "pfx": "JAH-INTGENACT-",
    "tagline_pub": "Intergenerational activities with every generation included - bridge the ages: every record carrying the activity, how all ages join, and a check that it is welcoming and safe, taught progressively along the ladder.",
    "tagline_sig": "The Signature bridge-sight: every activity a Signature bridge, every generation a Signature gift. The full ladder from easy bridges through deep ones to Signature-grade togetherness. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Intergenerational Activity",
    "role_pub": "bridge builder - designing activities where every age belongs",
    "role_sig": "Signature bridge builder - teaching Signature bridge-sight",
    "record_kind": "intergenerational activity record", "record_kind_plural": "intergenerational activities",
    "demo_kind": "bridge-proof", "demo_title": "Intergenerational Study",
    "search_ph": "Search generations, grandparents, kids, elders, family activities...",
    "chat_ph": "Ask for an intergenerational activity...",
    "gen_blurb": "Generate clearly-labeled activity studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded intergenerational activities, every generation welcomed and safe, marching toward one million records. Presented in teaching-ladder order: easy bridges, deep ones, Signature-grade.",
    "reqs": "Two generations and mutual respect.",
    "stds": "Every activity includes all ages safely and respectfully; the demo verifies it.",
    "cites": ["JAH Databases intergenerational standard v1.0"],
})


def _iga(tier, activity, how, why):
    return T(
        tier, "Activity: %s" % activity,
        desc_pub='INTERGENERATIONAL ACTIVITY: %s\n\nHOW ALL AGES JOIN: %s\n\nWHY IT BRIDGES: %s'
        % (activity.upper(), how, why),
        desc_sig='Signature bridge: %s - the generations meeting as one. The Signature edition treats every shared activity as time itself being shared.' % activity,
        how_pub='Do it: invite both generations, assign roles by strength, and let the stories flow - the activity is the excuse; the talk is the point.',
        how_sig='The Signature way: let the elders teach and the young do - everyone gives what they have.',
        keys=['Activity: %s.' % activity,
              'How: %s' % how,
              'Why: %s' % why],
        demo=("check", {"code": ["HOW = %r" % how],
                        "checks": [("how_concrete", "len(HOW) > 25"),
                                   ("includes_ages", "any(w in HOW.lower() for w in ['kid','child','elder','grandparent','teen','senior','young','old'])"),
                                   ("safe", "not any(w in HOW.lower() for w in ['dangerous','unsupervised','risky'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _iga(B, "Story time", "Grandparents read to kids; kids pick the books; elders tell the tales.", "Stories flow both ways."),
    _iga(B, "Cookie baking", "Elders share recipes; kids measure and stir; everyone tastes.", "Recipes are inheritance."),
    _iga(B, "Garden planting", "Elders teach planting; kids dig and water; all watch it grow.", "Growing together."),
    _iga(B, "Photo sorting", "Elders name the faces; kids scan the photos; all laugh.", "Memory preserved."),
    _iga(B, "Card games", "Teach kids the classic games; elders deal; all play.", "Games bridge everything."),
    _iga(B, "Puzzle table", "The big puzzle stays out; kids and grandparents add pieces together.", "Slow fun together."),
    _iga(B, "Bird watching", "Elders know the birds; kids spot them; all list.", "Nature teaches patience."),
    _iga(B, "Music sharing", "Elders play their songs; kids play theirs; all dance.", "Music is timeless."),
    _iga(B, "Cooking lesson", "Grandma's dish, taught hands-on; kids cook; all eat.", "Taste of heritage."),
    _iga(B, "Walk together", "Slow walk; elders set pace; kids explore ahead; all talk.", "Walking talks."),
    _iga(B, "Craft afternoon", "Simple crafts; elders guide; kids create; all display.", "Made together."),
    _iga(C, "Oral history", "Teens interview elders on video; elders tell all; all archive.", "History saved."),
    _iga(C, "Tech swap", "Kids teach phones; elders teach cursive; all learn.", "Skills both ways."),
    _iga(C, "Community service", "All ages volunteer together; elders lead; kids energy.", "Service unites."),
    _iga(C, "Fishing trip", "Elders teach casting; kids reel; all wait.", "Patience shared."),
    _iga(C, "Quilting circle", "Elders piece; kids design; all stitch stories.", "Warmth woven."),
    _iga(C, "Theater outing", "All attend the play; elders share context; kids react.", "Stories shared."),
    _iga(C, "Recipe book", "Compile family recipes; elders dictate; kids type; all taste-test.", "Legacy cooked."),
    _iga(C, "Garden harvest", "All pick; elders preserve; kids deliver to neighbors.", "Harvest shared."),
    _iga(C, "Game tournament", "Video games: kids teach; elders try; all laugh.", "Laughter guaranteed."),
    _iga(C, "Art class", "Paint together; elders share techniques; kids experiment.", "Art ageless."),
    _iga(C, "Music jam", "Elders bring instruments; kids bring beats; all play.", "Jam session."),
    _iga(C, "Stargazing", "Elders know constellations; kids use the app; all wonder.", "Wonder shared."),
    _iga(A, "Legacy project", "Build something permanent together; elders design; young build.", "Permanence together."),
    _iga(A, "Wisdom circle", "Elders share life lessons; young ask anything; all listen.", "Wisdom transferred."),
    _iga(A, "The documentary", "Film the elders' stories; young edit; all premiere.", "Stories immortal."),
    _iga(A, "Mentor match", "Pair elders with youth for a year; meet monthly.", "Year of growth."),
    _iga(A, "The festival", "Plan the family festival; elders judge; young perform.", "Celebration all ages."),
    _iga(A, "Heritage trip", "Visit the homeland together; elders guide; young document.", "Roots visited."),
    _iga(A, "The business", "Start the family business; elders advise; young run.", "Enterprise family."),
    _iga(A, "The scholarship", "Fund a scholarship; elders choose; young apply.", "Giving forward."),
    _iga(A, "The reunion", "Gather four generations; elders host; all celebrate.", "Four generations, one table."),
    _iga(A, "The time capsule", "Bury for 25 years; elders choose items; kids add.", "Future gift."),
    _iga(A, "The promise", "Elders share their vows; young make theirs; all witness.", "Vows across time."),
]
