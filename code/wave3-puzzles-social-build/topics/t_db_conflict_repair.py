# -*- coding: utf-8 -*-
"""Topic module: db-conflict-repair. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-conflict-repair", "name": "The Conflict Repair Database", "pfx": "JAH-CONREP-",
    "tagline_pub": "Conflict repair guides with every step respectful - mend what broke: every record carrying the rupture, the repair steps, and a check that the approach is kind and consent-aware, taught progressively along the ladder.",
    "tagline_sig": "The Signature mending-sight: every rupture a Signature wound, every repair a Signature healing. The full ladder from small hurts through deep breaks to Signature-grade reconciliation. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Conflict Repair",
    "role_pub": "repair guide - scripting the mending of hurt relationships",
    "role_sig": "Signature repair guide - teaching Signature mending-sight",
    "record_kind": "repair guide record", "record_kind_plural": "repair guides",
    "demo_kind": "repair-proof", "demo_title": "Conflict Repair Study",
    "search_ph": "Search conflict, repair, apology, forgiveness, arguments...",
    "chat_ph": "Ask for a repair guide...",
    "gen_blurb": "Generate clearly-labeled repair studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded repair guides, every step respectful and consent-aware, marching toward one million records. Presented in teaching-ladder order: small hurts, deep breaks, Signature-grade.",
    "reqs": "Humility and patience.",
    "stds": "Every guide centers the hurt person's needs, never demands forgiveness, and is consent-aware.",
    "cites": ["JAH Databases respectful repair standard v1.0"],
})


def _cr(tier, rupture, steps, note):
    return T(
        tier, "Repair: %s" % rupture[:54].rstrip(" .?") + "...",
        desc_pub='THE RUPTURE:\n\n%s\n\nREPAIR STEPS:\n%s\n\nREPAIR NOTE: %s'
        % (rupture, "\n".join("  %d. %s" % (i + 1, s) for i, s in enumerate(steps)), note),
        desc_sig='Signature mending: %s - the Signature path back. The Signature edition treats every genuine repair as the relationship choosing to live.' % rupture[:55],
        how_pub='Repair it: go in order, go slowly, and let the hurt person set the pace - repair is offered, never demanded.',
        how_sig='The Signature way: apologize for the impact, not your intent - intent explains, impact matters.',
        keys=['Rupture: %s' % rupture,
              'Steps: %d, each respectful.' % len(steps),
              'Note: %s' % note],
        demo=("check", {"code": ["STEPS = %r" % steps],
                        "checks": [("steps_present", "len(STEPS) >= 3"),
                                   ("no_demands", "not any('demand forgiveness' in s.lower() for s in STEPS)"),
                                   ("kind_language", "not any(w in ' '.join(STEPS).lower() for w in ['stupid','worthless','hate you'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _cr(B, "You forgot your friend's birthday.", ["Apologize promptly and plainly.", "Celebrate late with real effort.", "Set a reminder for next year."], "Late effort beats perfect memory."),
    _cr(B, "You snapped at someone when tired.", ["Name it: 'I snapped, and that wasn't fair.'", "Ask how it landed.", "Rest, then reconnect."], "Tired explains; it doesn't excuse."),
    _cr(B, "You broke a borrowed item.", ["Tell them before they notice.", "Replace or repair it.", "Offer something extra for the trouble."], "Confession plus restitution."),
    _cr(B, "You shared something told in confidence.", ["Admit exactly what you shared.", "Apologize to the person exposed.", "Prove discretion going forward."], "Trust is rebuilt by evidence."),
    _cr(B, "You stood someone up.", ["Apologize without excuses.", "Reschedule at their convenience.", "Show up early next time."], "The reschedule is the apology."),
    _cr(B, "You took credit for a group idea.", ["Correct the record publicly.", "Name who really did it.", "Share the next win loudly."], "Credit given back double."),
    _cr(B, "You gossiped about a friend.", ["Tell them what you said.", "Apologize to them, not around them.", "Stop the story at its source."], "Kill the gossip at the root."),
    _cr(B, "You lost a borrowed book.", ["Confess quickly.", "Buy a replacement copy.", "Add a note of apology inside."], "Replace plus a little more."),
    _cr(B, "You laughed at someone's mistake.", ["Apologize for laughing.", "Acknowledge it hurt.", "Defend them next time."], "Laughter wounds; defense heals."),
    _cr(B, "You forgot to reply for weeks.", ["Apologize for the silence.", "Explain briefly, not defensively.", "Re-engage with a real question."], "Silence needs a bridge back."),
    _cr(B, "You double-booked a friend.", ["Own the mistake.", "Let them pick the new plan.", "Keep the new plan sacred."], "Their pick, your priority."),
    _cr(C, "You lied about something small.", ["Tell the truth now, fully.", "Explain why you lied.", "Accept that trust dips before it recovers."], "Truth late beats lies maintained."),
    _cr(C, "A harsh argument with a sibling.", ["Cool down first - hours, not minutes.", "Apologize for your part specifically.", "Listen to their part fully.", "Agree on one change each."], "Specific apologies, mutual changes."),
    _cr(C, "You missed their big moment.", ["Acknowledge what it meant to them.", "Apologize for the absence.", "Create a new moment together."], "You can't rewind; you can rebuild."),
    _cr(C, "Money lent, resentment grown.", ["Talk about the money plainly.", "Set a repayment plan or forgive it.", "Never lend what you can't gift."], "Clarity or forgiveness - pick one."),
    _cr(C, "You criticized them publicly.", ["Apologize publicly too.", "Praise publicly going forward.", "Keep critiques private forever."], "Public wounds need public repair."),
    _cr(C, "A broken promise to a child.", ["Admit it plainly - kids know.", "Explain in their words.", "Keep the next ten promises visibly."], "Kids count; make the count good."),
    _cr(C, "Workplace credit dispute.", ["Document who did what.", "Raise it calmly with facts.", "Propose shared credit going forward."], "Facts first, feelings second at work."),
    _cr(C, "You chose sides in their divorce.", ["Admit you chose.", "Apologize to the hurt one.", "Stay neutral going forward."], "Neutrality is the repair."),
    _cr(C, "A friendship faded from neglect.", ["Reach out honestly: 'I dropped the ball.'", "Suggest a concrete plan.", "Follow through visibly."], "Neglect repairs with consistency."),
    _cr(C, "You broke a diet pact together.", ["Confess with humor.", "Restart together.", "Set kinder rules."], "Pacts bend; restart them."),
    _cr(C, "Holiday hosting blowup.", ["Let everyone cool down.", "Apologize for your part.", "Plan next year differently.", "Write the new plan down."], "Plans prevent repeats."),
    _cr(C, "You read their journal.", ["Confess what you read.", "Apologize for the violation.", "Never ask about its contents.", "Earn privacy back slowly."], "Privacy violations need time."),
    _cr(A, "Betrayal of trust in a partnership.", ["Full honest disclosure.", "Answer every question patiently.", "Accept consequences.", "Rebuild over months, not days.", "Consider counseling together."], "Betrayal repair is a marathon."),
    _cr(A, "Estranged parent and child.", ["Write the first letter kindly.", "Listen more than defend.", "Meet on neutral ground.", "Go slowly - years, not weeks."], "Estrangement thaws slowly."),
    _cr(A, "Business partnership collapse.", ["Separate facts from feelings.", "Mediate, don't litigate first.", "Divide fairly.", "Write the lessons down."], "Fair division preserves dignity."),
    _cr(A, "A lie that grew for years.", ["Tell the whole truth at once.", "Accept anger without defense.", "Answer follow-ups for as long as needed.", "Change the pattern visibly."], "Years of lies need months of truth."),
    _cr(A, "Addiction's damage to family.", ["Get help first - action before words.", "Apologize without demanding forgiveness.", "Make amends where possible.", "Stay consistent for years."], "Recovery is the apology."),
    _cr(A, "Sibling inheritance fight.", ["Get independent valuations.", "Mediate with a neutral third party.", "Put agreements in writing.", "Prioritize the relationship over the assets."], "Assets divide; siblings remain."),
    _cr(A, "Public shaming online.", ["Delete and apologize publicly.", "Make private amends too.", "Advocate against shaming.", "Accept that some won't forgive."], "Public harm needs public repair."),
    _cr(A, "A friendship ended over politics.", ["Acknowledge the real hurt beneath.", "Agree on no-go topics.", "Rebuild on shared history.", "Respect the boundary."], "History can outlast disagreement."),
    _cr(A, "Parental favoritism wounds.", ["Name it gently with the parent.", "Hear their perspective.", "Ask for specific changes.", "Build your own chosen family too."], "Some wounds need outside support."),
    _cr(A, "Workplace bullying aftermath.", ["Document everything.", "Report through proper channels.", "Seek support.", "Change teams if needed.", "Heal on your timeline."], "Safety first, repair second."),
    _cr(A, "A broken engagement.", ["Grieve honestly.", "Return items gracefully.", "Give mutual friends space.", "Wish well from a distance."], "Endings deserve grace too."),
]
