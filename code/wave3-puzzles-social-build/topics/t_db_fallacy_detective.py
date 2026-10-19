# -*- coding: utf-8 -*-
"""Topic module: db-fallacy-detective. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-fallacy-detective", "name": "The Fallacy Detective Database", "pfx": "JAH-FALDET-",
    "tagline_pub": "Fallacy cases with the flaw named and explained - spot the bad reasoning: every record carrying the argument, the fallacy name, why it fails, and a check that the diagnosis holds, taught progressively along the ladder.",
    "tagline_sig": "The Signature flaw-sight: every argument a Signature case, every fallacy a Signature catch. The full ladder from obvious flaws through sneaky ones to Signature-grade detections. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Fallacy Detective",
    "role_pub": "fallacy detective - naming the flaw in every bad argument",
    "role_sig": "Signature fallacy detective - teaching Signature flaw-sight",
    "record_kind": "fallacy case record", "record_kind_plural": "fallacy cases",
    "demo_kind": "fallacy-proof", "demo_title": "Fallacy Study",
    "search_ph": "Search fallacy, bad reasoning, ad hominem, strawman...",
    "chat_ph": "Ask for a fallacy case...",
    "gen_blurb": "Generate clearly-labeled fallacy studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded fallacy cases, every diagnosis logic-checked, marching toward one million records. Presented in teaching-ladder order: obvious flaws, sneaky ones, Signature-grade.",
    "reqs": "A suspicious ear and a name for every trick.",
    "stds": "Every diagnosis names the fallacy and explains the failure; the demo verifies the diagnosis matches the argument's structure.",
    "cites": ["JAH Databases fallacy verification standard v1.0"],
})


def _fd(tier, argument, fallacy, why, fix, check_code, checks):
    return T(
        tier, "Fallacy: %s" % argument[:52].rstrip(" .?") + "...",
        desc_pub='THE ARGUMENT:\n\n"%s"\n\nFALLACY: %s\n\nWHY IT FAILS: %s\n\nTHE FIX: %s'
        % (argument, fallacy, why, fix),
        desc_sig='Signature flaw-sight: "%s" - caught as %s. The Signature edition treats every spotted fallacy as the mind defending itself.' % (argument[:55], fallacy),
        how_pub='Detect it: ask what the conclusion needs, then check whether the premises actually supply it - fallacies are gaps wearing suits.',
        how_sig='The Signature way: name it out loud - a named fallacy loses half its power.',
        keys=['Argument: "%s".' % argument,
              'Fallacy: %s.' % fallacy,
              'Why it fails: %s' % why,
              'Fix: %s' % fix],
        demo=("check", {"code": check_code, "checks": checks}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _fd(B, "You're too young to understand politics.", "Ad hominem", "Attacks the person instead of the argument; age doesn't refute a point.", "Address the claim, not the claimant.", ["F='ad hominem'"], [("named", "F == 'ad hominem'")]),
    _fd(B, "Everyone is buying it, so it must be good.", "Bandwagon", "Popularity doesn't prove quality; crowds can be wrong together.", "Ask for evidence, not headcounts.", ["F='bandwagon'"], [("named", "F == 'bandwagon'")]),
    _fd(B, "My opponent wants to defund everything, so vote for me.", "Strawman", "Misrepresents the opponent's position to attack the fake version.", "Quote the real position, then argue.", ["F='strawman'"], [("named", "F == 'strawman'")]),
    _fd(B, "It rained after I danced, so my dance caused the rain.", "False cause", "Sequence isn't causation; no mechanism links dancing to rain.", "Show the mechanism or drop the claim.", ["F='false cause'"], [("named", "F == 'false cause'")]),
    _fd(B, "You're either with us or against us.", "False dilemma", "Presents two options when more exist; the middle is erased.", "List the missing options.", ["F='false dilemma'"], [("named", "F == 'false dilemma'")]),
    _fd(B, "The expert said it, so it must be true.", "Appeal to authority", "Authorities err; the claim needs evidence, not a badge.", "Check the evidence behind the badge.", ["F='appeal to authority'"], [("named", "F == 'appeal to authority'")]),
    _fd(B, "We've always done it this way.", "Appeal to tradition", "Age doesn't equal correctness; traditions need reasons too.", "Ask why, not how long.", ["F='appeal to tradition'"], [("named", "F == 'appeal to tradition'")]),
    _fd(B, "If we allow this, soon we'll allow everything.", "Slippery slope", "Predicts disaster without showing the steps; slopes need evidence.", "Demand each step of the slope.", ["F='slippery slope'"], [("named", "F == 'slippery slope'")]),
    _fd(B, "You can't prove ghosts don't exist, so they do.", "Burden of proof reversal", "The claim needs proving; unrefuted isn't proven.", "He who claims, proves.", ["F='burden of proof reversal'"], [("named", "F == 'burden of proof reversal'")]),
    _fd(B, "He's a criminal, so his argument about taxes is wrong.", "Ad hominem (circumstantial)", "The arguer's record doesn't refute the argument's logic.", "Separate the speaker from the speech.", ["F='ad hominem'"], [("named", "F == 'ad hominem'")]),
    _fd(B, "This is new, so it must be better.", "Appeal to novelty", "Newness isn't goodness; new things fail too.", "Test it, don't trust the shine.", ["F='appeal to novelty'"], [("named", "F == 'appeal to novelty'")]),
    _fd(C, "The study must be wrong because the researcher is biased.", "Genetic fallacy", "Judges the claim by its origin, not its content; biased people can be right.", "Read the methods, not the motive.", ["F='genetic fallacy'"], [("named", "F == 'genetic fallacy'")]),
    _fd(C, "We tried nothing and it failed, so trying is pointless.", "Nirvana fallacy", "Rejects the good for not being perfect; compares reality to perfection.", "Compare to the alternative, not perfection.", ["F='nirvana fallacy'"], [("named", "F == 'nirvana fallacy'")]),
    _fd(C, "A few fans were rude, so the whole fandom is toxic.", "Hasty generalization", "Small sample, big conclusion; anecdotes aren't data.", "Count before concluding.", ["F='hasty generalization'"], [("named", "F == 'hasty generalization'")]),
    _fd(C, "You're a fine one to talk about honesty.", "Tu quoque", "Answers a charge with a counter-charge; hypocrisy doesn't refute.", "Answer the charge, not the charger.", ["F='tu quoque'"], [("named", "F == 'tu quoque'")]),
    _fd(C, "The parts are light, so the whole must be light.", "Fallacy of composition", "What's true of parts isn't always true of wholes.", "Check the whole, not the parts.", ["F='composition'"], [("named", "F == 'composition'")]),
    _fd(C, "The team is strong, so every player is strong.", "Fallacy of division", "What's true of wholes isn't always true of parts.", "Judge each part itself.", ["F='division'"], [("named", "F == 'division'")]),
    _fd(C, "No one has complained, so the policy works.", "Appeal to silence", "Silence has many causes; absence of complaint isn't proof of success.", "Measure outcomes, not quiet.", ["F='appeal to silence'"], [("named", "F == 'appeal to silence'")]),
    _fd(C, "The law says so, so it must be right.", "Appeal to law", "Laws can be unjust; legality isn't morality.", "Argue the right, not the writ.", ["F='appeal to law'"], [("named", "F == 'appeal to law'")]),
    _fd(C, "Nature made it, so it's safe.", "Appeal to nature", "Nature makes poisons too; natural isn't safe.", "Test it, whatever its source.", ["F='appeal to nature'"], [("named", "F == 'appeal to nature'")]),
    _fd(C, "He's rich, so his business advice is sound.", "Appeal to wealth", "Wealth doesn't validate advice; luck and context matter.", "Audit the advice, not the account.", ["F='appeal to wealth'"], [("named", "F == 'appeal to wealth'")]),
    _fd(C, "The middle ground must be right.", "Middle ground fallacy", "Truth isn't always centered; sometimes one side is just right.", "Weigh evidence, not positions.", ["F='middle ground'"], [("named", "F == 'middle ground'")]),
    _fd(C, "After this, therefore because of this.", "Post hoc ergo propter hoc", "The Latin name for false cause: after isn't because.", "Find the mechanism.", ["F='post hoc'"], [("named", "F == 'post hoc'")]),
    _fd(A, "The survivors all agree, so the plan works.", "Survivorship bias", "The failures aren't here to disagree; the sample is the survivors.", "Count the absent.", ["F='survivorship bias'"], [("named", "F == 'survivorship bias'")]),
    _fd(A, "This question assumes the answer - answer it.", "Loaded question", "The question smuggles its conclusion; answering accepts the premise.", "Reject the premise, not just the question.", ["F='loaded question'"], [("named", "F == 'loaded question'")]),
    _fd(A, "The correlation is strong, so the cause is found.", "Cum hoc ergo propter hoc", "Correlation without causation; confounders lurk.", "Control before concluding.", ["F='cum hoc'"], [("named", "F == 'cum hoc'")]),
    _fd(A, "If A then B; B happened, so A caused it.", "Affirming the consequent", "B can follow from many causes; the logic is invalid.", "Check the other paths to B.", ["F='affirming the consequent'"], [("named", "F == 'affirming the consequent'")]),
    _fd(A, "If A then B; not A, so not B.", "Denying the antecedent", "B may hold without A; invalid form.", "Test B directly.", ["F='denying the antecedent'"], [("named", "F == 'denying the antecedent'")]),
    _fd(A, "The exception disproves the rule.", "Fallacy of the exception", "Exceptions refine rules; one outlier rarely kills a trend.", "Weigh, don't just point.", ["F='exception'"], [("named", "F == 'exception'")]),
    _fd(A, "We can't test it, so it's equally likely true.", "Argument from ignorance", "Untestable isn't 50/50; unknown stays unknown.", "Admit ignorance; don't split it.", ["F='ignorance'"], [("named", "F == 'ignorance'")]),
    _fd(A, "The definition assumes what it defines.", "Begging the question", "Circular reasoning: the premise is the conclusion.", "Find independent support.", ["F='begging the question'"], [("named", "F == 'begging the question'")]),
    _fd(A, "The word changed meaning mid-argument.", "Equivocation", "Same word, two senses; the argument slides between them.", "Pin the meaning down.", ["F='equivocation'"], [("named", "F == 'equivocation'")]),
    _fd(A, "The anecdote beats the statistics.", "Anecdotal fallacy", "Vivid stories override dry data; the data still wins.", "Trust the count, not the story.", ["F='anecdotal'"], [("named", "F == 'anecdotal'")]),
    _fd(A, "Doing something beats doing nothing, so do this.", "Action bias", "Action feels productive; wrong action beats nothing only sometimes.", "Compare actions, not action vs rest.", ["F='action bias'"], [("named", "F == 'action bias'")]),
]
