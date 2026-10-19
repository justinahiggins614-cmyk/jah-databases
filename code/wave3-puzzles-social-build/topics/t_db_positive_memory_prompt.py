# -*- coding: utf-8 -*-
"""Topic module: db-positive-memory-prompt. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-positive-memory-prompt", "name": "The Positive Memory Prompt Database", "pfx": "JAH-POSMEPRO-",
    "tagline_pub": "Positive memory prompts with every prompt uplifting - revisit the good times: every record carrying the prompt, how to savor it, and a check that it is warm and specific, taught progressively along the ladder.",
    "tagline_sig": "The Signature remember-sight: every prompt a Signature door, every memory a Signature treasure. The full ladder from sweet prompts through deep ones to Signature-grade savoring. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Positive Memory Prompt",
    "role_pub": "memory keeper - prompting the good times back to life",
    "role_sig": "Signature memory keeper - teaching Signature remember-sight",
    "record_kind": "memory prompt record", "record_kind_plural": "memory prompts",
    "demo_kind": "savor-proof", "demo_title": "Positive Memory Study",
    "search_ph": "Search memories, prompts, nostalgia, savoring, good times...",
    "chat_ph": "Ask for a memory prompt...",
    "gen_blurb": "Generate clearly-labeled prompt studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded memory prompts, every prompt warm and specific, marching toward one million records. Presented in teaching-ladder order: sweet prompts, deep ones, Signature-grade.",
    "reqs": "A past worth revisiting.",
    "stds": "Every prompt is specific, positive, and savoring-oriented; the demo verifies it.",
    "cites": ["JAH Databases memory prompt standard v1.0"],
})


def _pmp(tier, prompt, savor, why):
    return T(
        tier, "Remember: %s" % prompt[:54].rstrip(" .?") + "...",
        desc_pub='MEMORY PROMPT: %s\n\nSAVOR IT: %s\n\nWHY IT HELPS: %s'
        % (prompt, savor, why),
        desc_sig='Signature remembering: %s - a Signature treasure revisited. The Signature edition treats every savored memory as the past paying dividends.' % prompt[:55],
        how_pub='Use it: close your eyes, relive the details, and tell someone - shared memories double.',
        how_sig='The Signature way: write it down - written memories outlive moods.',
        keys=['Prompt: %s' % prompt,
              'Savor: %s' % savor,
              'Why: %s' % why],
        demo=("check", {"code": ["PROMPT = %r" % prompt, "SAVOR = %r" % savor],
                        "checks": [("prompt_specific", "len(PROMPT) > 20"),
                                   ("savor_actionable", "len(SAVOR) > 15"),
                                   ("positive", "not any(w in (PROMPT+SAVOR).lower() for w in ['trauma','abuse','hate','regret'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _pmp(B, "Recall your favorite birthday party.", "Picture the cake, the faces, the laughter.", "Joy revisited is joy renewed."),
    _pmp(B, "Remember a perfect sunny day.", "Feel the warmth; hear the sounds.", "Sunshine stored."),
    _pmp(B, "Think of a time you laughed hard.", "Replay the joke; feel the laugh.", "Laughter echoes."),
    _pmp(B, "Recall a delicious meal.", "Taste it again in memory.", "Flavor remembered."),
    _pmp(B, "Remember your favorite trip.", "Walk the streets in your mind.", "Travel twice."),
    _pmp(B, "Think of a proud moment.", "Stand tall in the memory.", "Pride renewed."),
    _pmp(B, "Recall a kind stranger.", "See their face; feel the kindness.", "Kindness remembered."),
    _pmp(B, "Remember your best school day.", "Hear the bell; see friends.", "Youth revisited."),
    _pmp(B, "Think of a cozy evening.", "Feel the blanket; hear the quiet.", "Cozy stored."),
    _pmp(B, "Recall a surprise that delighted you.", "Replay the reveal.", "Delight doubled."),
    _pmp(B, "Remember a beautiful place.", "See the colors; breathe the air.", "Beauty banked."),
    _pmp(C, "Recall the day you met your best friend.", "Replay the first hello.", "Friendship's first page."),
    _pmp(C, "Remember overcoming something hard.", "Feel the struggle, then the win.", "Strength proven."),
    _pmp(C, "Think of your proudest creation.", "See it finished; feel the pride.", "Made things last."),
    _pmp(C, "Recall a family tradition.", "Smell the familiar smells.", "Roots revisited."),
    _pmp(C, "Remember a standing ovation moment.", "Hear the applause.", "Applause echoes."),
    _pmp(C, "Think of the best advice you got.", "Hear their voice.", "Wisdom replayed."),
    _pmp(C, "Recall a perfect morning.", "Feel the fresh start.", "Mornings renew."),
    _pmp(C, "Remember helping someone.", "See their relief.", "Giving remembered."),
    _pmp(C, "Think of a brave thing you did.", "Feel the fear, then the courage.", "Courage catalogued."),
    _pmp(C, "Recall the funniest family story.", "Retell it aloud.", "Stories retold live."),
    _pmp(C, "Remember a milestone reached.", "Stand at the finish line again.", "Milestones mark."),
    _pmp(C, "Think of a song tied to joy.", "Play it now; dance like no one is watching.", "Music unlocks."),
    _pmp(A, "Recall the moment you knew your path.", "Feel the certainty.", "Purpose remembered."),
    _pmp(A, "Remember a reconciliation.", "Feel the relief.", "Peace revisited."),
    _pmp(A, "Think of your biggest growth.", "See the before and after.", "Growth witnessed."),
    _pmp(A, "Recall a legacy moment.", "Feel the continuity.", "Continuity comforts."),
    _pmp(A, "Remember pure wonder.", "Feel small and amazed.", "Wonder renews."),
    _pmp(A, "Think of unconditional love received.", "Rest in the memory.", "Love stored."),
    _pmp(A, "Recall your bravest love.", "Feel the open heart.", "Love's courage."),
    _pmp(A, "Remember the best day ever.", "Relive it fully.", "The best, twice."),
    _pmp(A, "Think of peace found.", "Breathe the calm.", "Calm banked."),
    _pmp(A, "Recall gratitude's peak.", "Feel the fullness.", "Gratitude overflows."),
    _pmp(A, "Remember coming home.", "Feel the arrival.", "Home, always."),
]
