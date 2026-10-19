# -*- coding: utf-8 -*-
"""Topic module: db-secret-supporter. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-secret-supporter", "name": "The Secret Supporter Database", "pfx": "JAH-SECSUP-",
    "tagline_pub": "Secret supporter missions with every act kind - lift someone secretly: every record carrying the mission, how to stay secret, and a check that it is genuine and welcome, taught progressively along the ladder.",
    "tagline_sig": "The Signature secret-sight: every mission a Signature gift, every secret act a Signature kindness. The full ladder from small secrets through big ones to Signature-grade generosity. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Secret Supporter",
    "role_pub": "secret kindness coach - dealing missions of anonymous support",
    "role_sig": "Signature secret kindness coach - teaching Signature secret-sight",
    "record_kind": "secret mission record", "record_kind_plural": "secret missions",
    "demo_kind": "secret-proof", "demo_title": "Secret Supporter Study",
    "search_ph": "Search secret supporter, anonymous kindness, missions...",
    "chat_ph": "Ask for a secret mission...",
    "gen_blurb": "Generate clearly-labeled mission studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded secret missions, every act genuine and welcome, marching toward one million records. Presented in teaching-ladder order: small secrets, big ones, Signature-grade.",
    "reqs": "A kind heart and a poker face.",
    "stds": "Every mission is anonymous, welcome, and kind; never creepy or intrusive.",
    "cites": ["JAH Databases anonymous kindness standard v1.0"],
})


def _ss(tier, mission, how_secret, why):
    return T(
        tier, "Mission: %s" % mission,
        desc_pub='SECRET MISSION: %s\n\nSTAY SECRET BY: %s\n\nWHY IT MATTERS: %s'
        % (mission.upper(), how_secret, why),
        desc_sig='Signature secret: %s - given without a name. The Signature edition treats every anonymous gift as kindness at its purest.' % mission,
        how_pub='Do it: complete the mission, leave no trace, and never claim credit - the secret is the gift.',
        how_sig='The Signature way: one mission a week - secret kindness is a practice.',
        keys=['Mission: %s.' % mission,
              'Stay secret: %s' % how_secret,
              'Why: %s' % why],
        demo=("check", {"code": ["M = %r" % mission, "S = %r" % how_secret],
                        "checks": [("mission_concrete", "len(M) > 8"),
                                   ("secret_kept", "len(S) > 15"),
                                   ("welcome", "not any(w in (M+S).lower() for w in ['stalk','spy','follow them','creepy'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _ss(B, "Leave an encouraging note", "Unsigned, on their desk before they arrive.", "Anonymous courage."),
    _ss(B, "Pay for their coffee", "Tell the cashier; leave before they know.", "Caffeine kindness."),
    _ss(B, "Compliment via a friend", "Tell their friend to pass it on.", "Praise travels."),
    _ss(B, "Leave flowers", "On the doorstep, no card.", "Flowers speak."),
    _ss(B, "Do their chore", "Finish it before they notice.", "Help unseen."),
    _ss(B, "Send the book", "Mail the book with no return address.", "Books travel."),
    _ss(B, "The full tank", "Fill their car secretly.", "Fuel for the week."),
    _ss(B, "The lunch surprise", "Leave lunch at their office.", "Fed anonymously."),
    _ss(B, "The playlist", "Share the anonymous playlist.", "Music heals."),
    _ss(B, "The plant", "Leave a plant on their porch.", "Green gift."),
    _ss(B, "The generous tip", "Tip big; leave before the reaction.", "Generosity given."),
    _ss(C, "Cover their shift", "Swap without telling them it was you.", "Rest given."),
    _ss(C, "The grocery run", "Leave groceries at their door.", "Fed in secret."),
    _ss(C, "Pay their bill", "Cover the table anonymously.", "Dinner gifted."),
    _ss(C, "The repair", "Fix what's broken while they're out.", "Mended unseen."),
    _ss(C, "The recommendation", "Recommend them for the opportunity.", "Doors opened quietly."),
    _ss(C, "The babysitting offer", "Offer via a mutual friend.", "Rest for parents."),
    _ss(C, "The donation", "Donate in their name.", "Honor given."),
    _ss(C, "The secret ride", "Arrange their ride home.", "Safe passage."),
    _ss(C, "The subscription", "Gift the subscription anonymously.", "Year of joy."),
    _ss(C, "The class", "Pay for their class.", "Learning gifted."),
    _ss(C, "The retreat", "Fund their weekend away.", "Rest funded."),
    _ss(C, "The needed tool", "Leave the tool they need.", "Work eased."),
    _ss(A, "The debt cleared", "Pay it through a third party.", "Freedom given."),
    _ss(A, "The scholarship", "Fund it anonymously.", "Future funded."),
    _ss(A, "The house repair", "Organize the crew secretly.", "Home healed."),
    _ss(A, "The medical bill", "Pay it via the charity.", "Health helped."),
    _ss(A, "The dream funded", "Back their project anonymously.", "Dreams backed."),
    _ss(A, "The legacy", "Give the big gift with no name.", "Legacy anonymous."),
    _ss(A, "The rescue", "Intervene through proper channels.", "Saved quietly."),
    _ss(A, "The second chance", "Create the opportunity.", "Chances given."),
    _ss(A, "The reunion", "Bring them together secretly.", "Reunited."),
    _ss(A, "The tribute", "Honor them publicly, anonymously.", "Honored unseen."),
    _ss(A, "The tradition", "Start the annual secret gift.", "Kindness institutionalized."),
]
