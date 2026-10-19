# -*- coding: utf-8 -*-
"""Topic module: db-friendship-compatibility-game-2. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-friendship-compatibility-game-2", "name": "The Friendship Compatibility Game 2 Database", "pfx": "JAH-FRICOMGA2-",
    "tagline_pub": "Friendship compatibility games with every round fun - how well do you know each other: every record carrying the game, the rules, and a check that it is kind and playable, taught progressively along the ladder.",
    "tagline_sig": "The Signature know-you-sight: every game a Signature test, every match a Signature delight. The full ladder from easy rounds through deep ones to Signature-grade knowing. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Friendship Compatibility Game 2",
    "role_pub": "game master - dealing rounds that reveal how well friends know each other",
    "role_sig": "Signature game master - teaching Signature know-you-sight",
    "record_kind": "compatibility game record", "record_kind_plural": "compatibility games",
    "demo_kind": "match-proof", "demo_title": "Compatibility Game Study",
    "search_ph": "Search friendship, compatibility, games, how well do you know...",
    "chat_ph": "Ask for a compatibility game...",
    "gen_blurb": "Generate clearly-labeled game studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded compatibility games, every round kind and playable, marching toward one million records. Presented in teaching-ladder order: easy rounds, deep ones, Signature-grade.",
    "reqs": "A friend and honest answers.",
    "stds": "Every game is kind, playable, and reveals connection; the demo verifies it.",
    "cites": ["JAH Databases game quality standard v1.0"],
})


def _fg(tier, game, rules, scoring):
    return T(
        tier, "Game: %s" % game,
        desc_pub='FRIENDSHIP GAME: %s\n\nRULES: %s\n\nSCORING: %s'
        % (game.upper(), rules, scoring),
        desc_sig='Signature knowing: %s - a Signature test of the bond. The Signature edition treats every matched answer as the friendship proving itself.' % game,
        how_pub='Play it: answer honestly, compare, and laugh at the misses - the misses are the fun.',
        how_sig='The Signature way: bet on the answers first - wagers make knowing thrilling.',
        keys=['Game: %s.' % game,
              'Rules: %s' % rules,
              'Scoring: %s' % scoring],
        demo=("check", {"code": ["RULES = %r" % rules, "SCORING = %r" % scoring],
                        "checks": [("rules_concrete", "len(RULES) > 20"),
                                   ("scoring_clear", "len(SCORING) > 10"),
                                   ("kind", "not any(w in (RULES+SCORING).lower() for w in ['humiliat','mock','insult'])")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _fg(B, "Favorite Things Match", "Each writes their favorite food, movie, and song; compare.", "1 point per match; 3 is a perfect round."),
    _fg(B, "Two Truths and a Dream", "Share two truths and one dream; the other guesses the dream.", "1 point per correct guess."),
    _fg(B, "The Prediction Game", "Predict each other's answer before revealing.", "1 point per correct prediction."),
    _fg(B, "This or That", "Answer 20 this-or-that questions simultaneously.", "Count the matches out of 20."),
    _fg(B, "The Memory Test", "Name 5 shared memories; the other adds details.", "1 point per confirmed memory."),
    _fg(B, "Draw Each Other", "Draw portraits in 2 minutes; vote on likeness.", "Most likable wins (everyone wins)."),
    _fg(B, "The Compliment Round", "Trade compliments for 3 minutes.", "You both win."),
    _fg(B, "Guess the Song", "Hum songs; the other guesses.", "1 point per correct guess."),
    _fg(B, "The Story Finish", "One starts a story; the other finishes it.", "Best ending wins applause."),
    _fg(B, "Would You Rather", "Answer 10 would-you-rathers together.", "Matches count; debates are bonus."),
    _fg(B, "The Superlative Vote", "Vote each other 'most likely to...' for 10 categories.", "Laughs are the score."),
    _fg(C, "The Deep 20", "Answer 20 deeper questions; predict first.", "1 point per match; discuss the misses."),
    _fg(C, "Life Timeline", "Draw your life timelines; compare milestones.", "Shared milestones score double."),
    _fg(C, "The Values Rank", "Rank 10 values; compare orders.", "Score by rank correlation (close counts)."),
    _fg(C, "Dream Interpretation", "Share a recent dream; the other interprets.", "Best interpretation wins."),
    _fg(C, "The Fear Share", "Share fears; the other responds with care.", "Care is the score."),
    _fg(C, "Childhood Stories", "Tell three childhood stories; the other retells one.", "Accuracy plus heart."),
    _fg(C, "The Gratitude Exchange", "List 10 things you appreciate about each other.", "Finish the list together."),
    _fg(C, "Future Predictions", "Predict where you'll both be in 5 years.", "Seal and open in 5 years."),
    _fg(C, "The Apology Game", "Share small hurts; repair them.", "Repairs are the points."),
    _fg(C, "Talent Show", "Perform hidden talents for each other.", "Applause decides."),
    _fg(C, "The Interview", "Interview each other for 10 minutes.", "Best question wins."),
    _fg(C, "Memory Lane Quiz", "Quiz each other on shared history.", "1 point per correct answer."),
    _fg(A, "The Life Story", "Tell your full story; the other reflects it back.", "Feeling known is the win."),
    _fg(A, "The Shadow Share", "Share something you've never told anyone.", "Trust is the score."),
    _fg(A, "The Legacy Game", "Describe each other's legacy.", "Tears mean perfect score."),
    _fg(A, "The Forgiveness Round", "Name old hurts; forgive.", "Lighter hearts win."),
    _fg(A, "The Dream Build", "Design your shared future in detail.", "Excitement is the metric."),
    _fg(A, "The Wisdom Exchange", "Share your hardest-earned lesson.", "Wisdom shared doubles."),
    _fg(A, "The Gratitude Marathon", "100 appreciations in one sitting.", "Reach 100 together."),
    _fg(A, "The Truth Chair", "Ask anything; answer honestly.", "Honesty is the only rule."),
    _fg(A, "The Time Capsule", "Fill a box for your future selves.", "Seal it with a date."),
    _fg(A, "The Vow Game", "Write friendship vows.", "Mean every word."),
    _fg(A, "The Eulogy Game", "Write each other's (loving) eulogy.", "The loving kind only - tears of joy."),
]
