#!/usr/bin/env python3
"""Entries for the Loving Statements databases (2026-10-17 fun/social batch).

The Loving Statements Database - loving statements: expressions of love,
devotion, and appreciation for partners, family, and friends. Every record
is a statement WITH context guidance: when to say it, and how to personalize
it. Warm and sincere only; screened for hate-adjacent, profane, or
inappropriate content; no religious talk.

34 ladder-ordered records each:

  loving-statements            - The Loving Statements Database
                                 (public-harvest: real, generatable
                                 expressions of love and appreciation -
                                 everyday affection, partner devotion, family
                                 gratitude, friendship loyalty, and profound
                                 devotion - each record a full statement plus
                                 when-to-say-it and how-to-personalize
                                 guidance; reference landmarks: Shakespeare
                                 Sonnet 116 (1609, public domain); Elizabeth
                                 Barrett Browning Sonnets from the Portuguese
                                 (1850, public domain); Kahlil Gibran The
                                 Prophet (1923, public domain); Chapman The 5
                                 Love Languages (1992); Gottman The Seven
                                 Principles for Making Marriage Work (1999);
                                 Rosenberg Nonviolent Communication (1999);
                                 and the other landmarks cited per record)
  loving-statements-signature  - The Loving Statements Signature Database
                                 (his original Signature Devotion Method:
                                 every loving statement a stamped covenant,
                                 love declared deliberately and on the
                                 record, affection treated as eternal data -
                                 devotion as engineering; src signature,
                                 titles suffixed " (Signature Edition)",
                                 never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced): everyday affection ->
heartfelt devotion -> profound devotion. The shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-LVST- (public) and JAH-LVSTS- (signature), verified free
in the manifest (zero hits) and in every one of the 831 shard index files
in jah-databases-data-1 (zero hits).

Demo cores: all real, stdlib-only Python, hand-authored 2026-10-17 and
machine-executed by build.py: statement-of-the-day picker, occasion
matcher, personalization engine, letter formatters, ledgers, and
schedules - each prints real computed values, asserts tight bounds (never
float exact-equality), and ends with the OK marker.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Devotion Method: "
            "every loving statement a stamped covenant, love declared "
            "deliberately and on the record, affection treated as eternal "
            "data, devotion as engineering. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_SHAKESPEARE = ("Shakespeare W. Sonnet 116 (\"Let me not to the marriage of "
                   "true minds admit impediments\"). 1609; public domain.")
CIT_BROWNING = ("Browning EB. Sonnets from the Portuguese. 1850; public "
                "domain.")
CIT_GIBRAN = ("Gibran K. The Prophet. Alfred A. Knopf; 1923; public domain.")
CIT_CHAPMAN = ("Chapman G. The 5 Love Languages. Moody Publishers; 1992.")
CIT_GOTTMAN = ("Gottman JM, Silver N. The Seven Principles for Making "
               "Marriage Work. Crown; 1999.")
CIT_ROSENBERG = ("Rosenberg MB. Nonviolent Communication: A Language of "
                 "Life. PuddleDancer Press; 1999.")
CIT_FROMM = ("Fromm E. The Art of Loving. Harper & Brothers; 1956.")
CIT_LEWIS = ("Lewis CS. The Four Loves. Geoffrey Bles; 1960.")

ENTRIES = [
    # ---------------- Foundations: everyday affection ----------------
    {
        "key": "you_matter",
        "name": "You Matter To Me",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "\"You matter to me, more than you will ever know. Before my feet "
            "hit the floor this morning, you were already on my mind, and I "
            "wanted you to start your day knowing that.\" A foundation "
            "statement: the simplest loving statement there is, said plainly "
            "and without occasion. It answers the quiet question everyone "
            "carries - do I matter to anyone - with a direct yes. This "
            "record teaches the base unit of the whole database: one "
            "sincere sentence, delivered to a person, on an ordinary day."
        ),
        "how_it_works": (
            "Say it on an ordinary day with no special occasion - that is "
            "what makes it land. Morning text, a note in a lunch bag, spoken "
            "over coffee: the channel matters less than the surprise of "
            "receiving love without having earned it. Personalize it by "
            "naming the person and one true detail: \"You matter to me, "
            "Sarah. The way you hummed while making breakfast this morning "
            "stayed with me all day.\" Keep it short; one true sentence "
            "beats a paragraph of decoration. Say their name - hearing your "
            "own name attached to love is the oldest magic there is. Repeat "
            "it often enough that it becomes true background music in their "
            "life, not a rare event."
        ),
        "key_points": [
            "The simplest loving statement is a direct yes to the question everyone quietly carries: do I matter to anyone.",
            "Ordinary days are the best delivery days; love that arrives without an occasion proves it is not a performance.",
            "One true sentence outperforms a decorated paragraph; sincerity is in the specificity, not the length.",
            "Saying the person's name attaches the love to them personally, which is where it belongs.",
            "Repetition is a feature: background music of affection beats rare grand gestures for daily wellbeing.",
        ],
        "requirements": [
            "A plain, direct statement of mattering, in your own voice, not borrowed poetry.",
            "An ordinary-day delivery moment: morning, evening, or a random Tuesday text.",
            "The person's name spoken or written, attached to the statement.",
            "One true personal detail that proves this is about them and not a template.",
            "Zero expectation of a reply; give it and let it sit.",
        ],
        "standards": [
            "Sincerity standard: say only what is true; a small true statement outweighs a large hollow one.",
            "Specificity standard: one concrete detail (a habit, a moment, a trait) proves the statement is personal.",
            "Frequency standard: everyday affection statements are meant to recur, not to be rationed.",
        ],
        "citations": [CIT_CHAPMAN, CIT_ROSENBERG],
        "sig_lens": (
            "Signature lens: this is the base unit of the Signature Devotion "
            "Method - the daily stamp. Where others wait for occasions, the "
            "Signature way declares mattering as standing data, refreshed "
            "every morning, signed by name, witnessed by detail."
        ),
    },
    {
        "key": "simple_thank_you",
        "name": "The Simple Thank You",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "\"Thank you for being you. Not for what you did today, but for "
            "who you are every day - the way you laugh, the way you care, "
            "the way you make ordinary moments feel full.\" A foundation "
            "statement of appreciation that thanks a person for their being "
            "rather than their doing. Most gratitude is transactional - "
            "thanks for the favor, the gift, the help. This one thanks the "
            "existence, which is rarer and lands deeper, because it cannot "
            "be spent or repaid."
        ),
        "how_it_works": (
            "Say it after a stretch of ordinary days, not after a favor - "
            "the point is that no favor triggered it. Best delivered in "
            "person or by voice so the tone carries. Personalize it by "
            "naming two or three traits that are unmistakably theirs: their "
            "laugh, their patience with strangers, the way they always save "
            "you the good seat. Avoid listing achievements; this is about "
            "character, not resume. If they deflect (\"oh, stop\"), do not "
            "retreat - smile and say \"I mean it,\" and let the compliment "
            "land. People who deflect praise are usually the ones who need "
            "it most."
        ),
        "key_points": [
            "Thanking someone for who they are is rarer and deeper than thanking them for what they did.",
            "Deliver it after ordinary days, not favors, so it reads as appreciation of being, not payment for service.",
            "Name character traits, not achievements; this is the person, not the resume.",
            "Voice or in-person delivery carries tone that text cannot fully hold.",
            "When they deflect, hold the line kindly - deflection often signals need, not rejection.",
        ],
        "requirements": [
            "A thank-you aimed at being rather than doing.",
            "Two or three named character traits that are unmistakably theirs.",
            "Delivery by voice or in person when possible.",
            "A calm response ready for deflection: a smile and \"I mean it.\"",
            "No favor or occasion attached - the statement must stand alone.",
        ],
        "standards": [
            "Being-over-doing standard: traits of character, never transactions, are the subject.",
            "Tone standard: warm and steady, never gushing; the weight is in the calm.",
            "Deflection standard: never argue the compliment, just rest it gently and move on.",
        ],
        "citations": [CIT_CHAPMAN, CIT_FROMM],
        "sig_lens": (
            "Signature lens: the Signature way stamps gratitude for being, "
            "not doing - the ledger of existence, not of transactions. It "
            "records the traits as data: laugh, care, presence - filed under "
            "the person's name, permanent."
        ),
    },
    {
        "key": "i_notice_you",
        "name": "I Notice You",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "\"I notice the little things you do that nobody else sees, and "
            "I want you to know I see them. The extra minute you take, the "
            "quiet kindness, the work you do when no one is watching - I "
            "see it, and it matters.\" A foundation statement of witnessed "
            "effort. The most corrosive feeling in relationships is "
            "invisibility: doing the small sustaining things and having "
            "no one register them. This statement is the antidote - proof of "
            "a witness."
        ),
        "how_it_works": (
            "Say it when you catch one of the invisible acts - refilling "
            "something, tidying without comment, checking on someone "
            "quietly. Name the act precisely: \"I saw you refill Mom's "
            "pill organizer before she asked.\" Precision is the whole "
            "mechanism; vague praise (\"you do so much\") does not cure "
            "invisibility. Personalize it by keeping a mental list through "
            "the week of the small unseen things, then delivering one or two "
            "at a calm moment. Do not attach a request or a complaint - "
            "\"I notice you always do the dishes\" must never become \"so "
            "why can't you...\" The statement must be pure witness, or it "
            "poisons the well."
        ),
        "key_points": [
            "Invisibility is the corrosive feeling; being witnessed is the antidote.",
            "Precision names the act exactly - vague praise does not cure feeling unseen.",
            "Deliver it at a calm moment, separate from any request or complaint.",
            "Keep a running mental list through the week so the noticing is real, not invented.",
            "Pure witness only: the moment it carries a demand, it poisons the well.",
        ],
        "requirements": [
            "At least one precisely named small act you actually witnessed.",
            "Delivery separate from requests, corrections, or arguments.",
            "The phrase \"I see it\" or its equivalent, stated plainly.",
            "A running practice of noticing through the week, not a one-time performance.",
            "Zero follow-on asks attached to the statement.",
        ],
        "standards": [
            "Precision standard: name the act, the moment, or the habit exactly.",
            "Purity standard: witness without agenda; no request may ride along.",
            "Continuity standard: noticing is a practice, delivered regularly in small doses.",
        ],
        "citations": [CIT_GOTTMAN, CIT_ROSENBERG],
        "sig_lens": (
            "Signature lens: the Signature way treats noticing as "
            "instrumentation - sensors on, recording the small acts as they "
            "happen, reported back to the person as stamped evidence that "
            "their quiet work entered the record."
        ),
    },
    {
        "key": "good_morning",
        "name": "Good Morning, My Love",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "\"Good morning. You are the first good thought of my day, and "
            "I hope the day is as kind to you as you are to everyone in it.\" "
            "A foundation morning statement for a partner, or adapted for "
            "anyone you love. It does three things in two sentences: it "
            "places them first in your day, it wishes them well, and it "
            "reflects their own kindness back at them. Mornings set the "
            "emotional temperature of the day; this statement sets it warm."
        ),
        "how_it_works": (
            "Say it or send it early, before the day's noise starts - the "
            "earlier, the more it reads as \"first thought.\" Personalize "
            "it with one detail of their day: \"Good morning. First thought "
            "of my day, as always. Knock that presentation out of the park - "
            "I hope the day is as kind to you as you are to everyone in it.\" "
            "For family or friends, swap the framing: \"You were my first "
            "good thought this morning\" works for a mother, a best friend, "
            "a child. Keep a small rotation of morning lines so it never "
            "becomes a copy-pasted ritual - vary the wish, keep the first "
            "thought constant. If you wake up grumpy, say it anyway; the "
            "discipline of the statement is part of the love."
        ),
        "key_points": [
            "Mornings set the emotional temperature of the day; a warm first line sets it warm.",
            "The statement does three jobs: first thought, good wish, reflected kindness.",
            "Early delivery is the proof of \"first thought\" - timing is the message.",
            "One detail of their actual day keeps it from becoming a copy-pasted ritual.",
            "Say it even on grumpy mornings; the discipline is part of the devotion.",
        ],
        "requirements": [
            "Delivery before the day's noise starts, ideally first message or first words.",
            "The \"first good thought\" placement, stated or clearly implied.",
            "One true detail of their day ahead.",
            "A small rotation of wordings so the ritual stays alive.",
            "Adaptable framing for partner, family, or friend.",
        ],
        "standards": [
            "Timing standard: before the day intrudes; lateness dilutes the \"first thought\" claim.",
            "Freshness standard: vary the wish weekly; keep the placement constant.",
            "Discipline standard: the statement goes out on hard mornings too.",
        ],
        "citations": [CIT_CHAPMAN, CIT_BROWNING],
        "sig_lens": (
            "Signature lens: the Signature way opens every day with a "
            "stamped declaration - first thought, logged. It is the "
            "sunrise protocol: before the world gets a word, the loved one "
            "gets the first one, on the record."
        ),
    },
    {
        "key": "make_better",
        "name": "You Make It Better",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "\"Everything is better with you in it - the hard days, the "
            "boring errands, the quiet evenings. You turn ordinary into "
            "something I look forward to.\" A foundation statement about "
            "presence as an upgrade to life. It tells the person that their "
            "value is not in grand gestures but in the ambient improvement "
            "they bring to the mundane. Everyone wants to be the reason "
            "someone's day got better; this statement hands them that "
            "knowledge directly."
        ),
        "how_it_works": (
            "Say it during or right after an ordinary shared moment - the "
            "grocery run, the traffic jam survived together, the quiet "
            "evening on the couch. The contrast between the mundane moment "
            "and the warm statement is what makes it memorable. Personalize "
            "it by naming the specific ordinary thing: \"Even the DMV was "
            "fine with you next to me.\" Works for partners, friends, "
            "siblings, and parents - anyone whose company upgrades your "
            "hours. Avoid saving it for vacations or big events; the whole "
            "point is the ordinary. Say it casually, almost as an "
            "observation, and let them feel it land."
        ),
        "key_points": [
            "Presence as an upgrade: their value is in the ambient improvement of the mundane.",
            "Deliver during or right after an ordinary shared moment for maximum contrast.",
            "Name the specific ordinary thing; the mundane detail is the proof.",
            "Works across partner, friend, sibling, and parent with the same structure.",
            "Casual observational tone lands better than grand declaration here.",
        ],
        "requirements": [
            "An ordinary shared moment as the delivery context.",
            "The named ordinary thing, specific and recent.",
            "The \"better with you\" claim stated plainly.",
            "A casual, observational tone rather than a speech.",
            "No big event required - ordinary is the point.",
        ],
        "standards": [
            "Context standard: ordinary moments only; saving it for vacations misses the point.",
            "Specificity standard: the named mundane detail proves it is real.",
            "Tone standard: observational and easy, never a prepared speech.",
        ],
        "citations": [CIT_FROMM, CIT_LEWIS],
        "sig_lens": (
            "Signature lens: the Signature way measures love in upgraded "
            "ordinary hours - the DMV, the errands, the quiet evenings - and "
            "stamps the finding: this person's presence is a standing "
            "improvement to the baseline of life."
        ),
    },
    {
        "key": "proud_of_you",
        "name": "I Am Proud Of You",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "\"I am proud of you. Not just for what you finished, but for "
            "how you keep going when it is hard. Watching you try is one of "
            "the great honors of my life.\" A foundation statement of pride "
            "that honors effort, not just outcome. Most pride statements "
            "arrive at finish lines; this one honors the middle of the "
            "race, where the person actually lives. It is especially "
            "powerful for children, students, and anyone grinding through "
            "something difficult."
        ),
        "how_it_works": (
            "Say it mid-effort, not at the finish line - during the late "
            "study nights, the hard training weeks, the long job hunt. That "
            "timing tells them the trying itself is seen. Personalize it by "
            "naming what you have watched them endure: \"I watched you "
            "rewrite that chapter four times without quitting.\" Separate "
            "pride in effort from pressure about outcome: never follow it "
            "with \"now go win\" - let the pride stand alone. For children, "
            "say it about character moments too: sharing, apologizing, "
            "trying again after failing. Those are the tries that shape a "
            "life, and naming them teaches the child what pride is really "
            "for."
        ),
        "key_points": [
            "Honor the middle of the race, not just the finish line; effort is where the person lives.",
            "Mid-effort timing tells them the trying itself is seen and valued.",
            "Name what you watched them endure; the witness detail is the mechanism.",
            "Never attach outcome pressure - let the pride stand alone without \"now go win.\"",
            "For children, pride in character moments teaches what pride is really for.",
        ],
        "requirements": [
            "Delivery during the effort, not after the result.",
            "A named endurance detail: what you watched them push through.",
            "The \"honor to watch\" framing, stated sincerely.",
            "No outcome pressure attached to the pride.",
            "Character-moment coverage for children, not just achievements.",
        ],
        "standards": [
            "Timing standard: mid-effort delivery; finish-line-only pride teaches outcome worship.",
            "Separation standard: pride stands alone, never followed by performance demands.",
            "Character standard: for the young, name who they were, not just what they won.",
        ],
        "citations": [CIT_GOTTMAN, CIT_ROSENBERG],
        "sig_lens": (
            "Signature lens: the Signature way records effort as the primary "
            "metric - the middle of the race stamped and honored. Outcomes "
            "fade; the witnessed trying is entered into the permanent "
            "record of who this person is."
        ),
    },
    {
        "key": "home_is_you",
        "name": "Home Is You",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "\"Home was never a place to me. It was always a person. You "
            "are my home, wherever we are.\" A foundation statement that "
            "relocates home from geography to a person. It is one of the "
            "most disarming things you can say to a partner, and it adapts "
            "beautifully to family: a parent telling a faraway child \"you "
            "carry home with you,\" or a child telling a parent \"wherever "
            "you are is home.\" Short, portable, and endlessly reusable."
        ),
        "how_it_works": (
            "Say it in transitional moments - moving day, a hotel room on a "
            "trip, the first night in a new place, or when they are "
            "homesick. The statement reframes displacement as irrelevant "
            "because the anchor travels. Personalize it with the current "
            "setting: \"This apartment is still boxes, but you are here, so "
            "I am home.\" For long-distance love, it is a standing "
            "reassurance: distance changes coordinates, not home. Keep it "
            "short - this is a three-sentence statement by design, and "
            "length would dilute the clean geometry of the idea."
        ),
        "key_points": [
            "Home relocated from geography to a person is one of the most disarming claims in love.",
            "Transitional moments - moves, trips, homesickness - are the natural delivery windows.",
            "The current setting named in the statement proves the anchor travels.",
            "For long-distance love it is a standing reassurance: coordinates change, home does not.",
            "Brevity is structural; the clean geometry of the idea needs three sentences, not thirty.",
        ],
        "requirements": [
            "A transitional or displaced moment as context, or a quiet ordinary night.",
            "The place-to-person relocation stated plainly.",
            "The current setting named to prove the point.",
            "Three-sentence brevity kept intact.",
            "Adaptable direction: partner, parent, child, or chosen family.",
        ],
        "standards": [
            "Context standard: transitions and distance are the natural habitat of this statement.",
            "Brevity standard: short by design; expansion dilutes the geometry.",
            "Direction standard: the claim works in every direction of love, not only romance.",
        ],
        "citations": [CIT_LEWIS, CIT_BROWNING],
        "sig_lens": (
            "Signature lens: the Signature way defines home as a person, "
            "not coordinates - the anchor stamped as portable. Wherever the "
            "loved one stands, the record shows: home is here."
        ),
    },
    {
        "key": "daily_blessing",
        "name": "The Daily Blessing",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "\"I hope today gives back to you even half of what you give to "
            "everyone else. You deserve the same kindness you hand out so "
            "freely.\" A foundation blessing statement for the givers - the "
            "people who pour themselves out for others and rarely get "
            "poured into. It works as a morning send-off or as comfort on a "
            "day they feel unappreciated. The mechanism is reflection: it "
            "holds up a mirror to their generosity and wishes it returned."
        ),
        "how_it_works": (
            "Say it to the givers in your life: the caretaking parent, the "
            "friend everyone calls in crisis, the partner who holds the "
            "household together. Morning delivery frames their whole day; "
            "evening delivery reframes a hard one. Personalize it by naming "
            "their giving: \"You spent the whole weekend helping your "
            "sister move. I hope today hands some of that back to you.\" "
            "The statement also works as a gentle nudge toward self-care "
            "without lecturing - it wishes them kindness rather than "
            "ordering them to rest. Repeat it on the days they seem "
            "depleted; givers rarely ask, so the blessing has to arrive "
            "unasked."
        ),
        "key_points": [
            "Aim it at the givers: caretakers, crisis-friends, household-holders who rarely get poured into.",
            "The mechanism is reflection: mirror their generosity and wish it returned to them.",
            "Name their recent giving to prove you have been paying attention.",
            "It nudges toward self-care by wishing, never by lecturing.",
            "It must arrive unasked; givers almost never request it themselves.",
        ],
        "requirements": [
            "A giver identified: someone who pours out for others regularly.",
            "Their recent giving named specifically.",
            "The reflection mechanism: their kindness wished back upon them.",
            "Morning or post-hard-day delivery timing.",
            "Zero lecturing about rest; the wish does the work.",
        ],
        "standards": [
            "Target standard: the statement belongs to givers; generic delivery dilutes it.",
            "Reflection standard: their generosity mirrored, then wished returned.",
            "Initiative standard: unasked arrival; waiting for a request means waiting forever.",
        ],
        "citations": [CIT_FROMM, CIT_GIBRAN],
        "sig_lens": (
            "Signature lens: the Signature way keeps a ledger on givers - "
            "every poured-out kindness recorded - and issues the daily "
            "rebalancing: may the record show the giving returned, stamped "
            "and wished, every morning."
        ),
    },
    {
        "key": "favorite_sound",
        "name": "Your Laugh Is My Favorite Sound",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "\"Your laugh is my favorite sound in the world. I would know "
            "it in a crowded room, and it is the one thing that can pull me "
            "out of the worst mood I am in.\" A foundation statement of "
            "sensory devotion: it tells the person that something "
            "involuntary and uniquely theirs has become your favorite "
            "thing. Laughter, voice, the way they say your name - these "
            "small sensory details are the texture of love, and naming one "
            "tells them they are known at the level of senses."
        ),
        "how_it_works": (
            "Say it right after you hear the thing - after the laugh, after "
            "they call your name across the house. Immediacy is the proof; "
            "a delayed compliment about a laugh feels filed, an immediate "
            "one feels struck. Personalize it by choosing their true "
            "signature sound: the laugh, the sleepy morning voice, the way "
            "they say a particular word. Describe the effect honestly: "
            "\"it pulls me out of bad moods\" is better than \"it is "
            "beautiful\" because it reports an effect, not an appraisal. "
            "Works for partners, children (their giggle), and close "
            "friends; keep it warm, never teasing about the sound itself."
        ),
        "key_points": [
            "Sensory devotion tells them they are known at the level of senses, not just ideas.",
            "Immediacy is the proof: say it right after the laugh, the voice, the moment.",
            "Report the effect (it lifts my mood) rather than appraising (it is beautiful).",
            "Choose their true signature sound; the specificity is the love.",
            "Warm, never teasing: the sound is treasured, not joked about.",
        ],
        "requirements": [
            "A true signature sound of theirs identified.",
            "Delivery in the moment or immediately after hearing it.",
            "An honest reported effect on you.",
            "The \"favorite\" superlative, meant and not hedged.",
            "A warm tone with zero teasing about the sound.",
        ],
        "standards": [
            "Immediacy standard: in-the-moment delivery; delayed praise feels filed.",
            "Effect standard: report what it does to you, not a judgment of it.",
            "Reverence standard: the treasured thing is never the butt of a joke.",
        ],
        "citations": [CIT_SHAKESPEARE, CIT_CHAPMAN],
        "sig_lens": (
            "Signature lens: the Signature way files sensory data as love "
            "evidence - the laugh catalogued, the voice stamped as favorite. "
            "It declares: of all sounds in the world, this one is entered "
            "first in the record."
        ),
    },
    {
        "key": "choose_daily",
        "name": "I Choose You Daily",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "\"Loving you is not just a feeling I have. It is a choice I "
            "make, every single morning, and I have never once regretted "
            "it.\" A foundation statement that reframes love from weather "
            "to decision. Feelings fluctuate; this statement tells the "
            "person they are not hostage to your moods. It is deeply "
            "reassuring because it answers the fear underneath many "
            "arguments: what if you stop feeling it. The answer: I choose "
            "it, daily, on purpose."
        ),
        "how_it_works": (
            "Say it on an ordinary morning, or after a disagreement has "
            "cooled - never mid-argument, where it sounds like a tactic. "
            "The cooled-after timing proves the choice survived the "
            "friction. Personalize it with the history: \"Twelve years of "
            "mornings, and I choose you on every one of them.\" For newer "
            "love, keep it present-tense and honest: \"Every morning since "
            "we met.\" Do not use it to end a discussion about a real "
            "problem - it is a statement of commitment, not a substitute "
            "for repair. Pair it with action: the choice is credible when "
            "the days show it."
        ),
        "key_points": [
            "Reframing love as daily choice removes the fear of fluctuating feelings.",
            "It answers the hidden question under many arguments: what if you stop feeling it.",
            "Deliver on ordinary mornings or after cooled disagreements, never mid-fight.",
            "History strengthens it: count the mornings when you have them.",
            "It is a commitment statement, not a substitute for repairing real problems.",
        ],
        "requirements": [
            "The choice framing stated plainly: decision, not just feeling.",
            "Calm delivery timing: ordinary morning or post-cooling, never mid-argument.",
            "A morning-count or history detail when one exists.",
            "No use as an argument-ender; repair still happens separately.",
            "Daily action backing the claim, visible to the person.",
        ],
        "standards": [
            "Timing standard: never deployed mid-conflict as a tactic.",
            "Honesty standard: the count of mornings must be true.",
            "Backing standard: the choice is credible only when the days show it.",
        ],
        "citations": [CIT_FROMM, CIT_GOTTMAN],
        "sig_lens": (
            "Signature lens: the Signature way logs love as a daily "
            "decision, stamped each morning - not weather, but will. The "
            "record shows an unbroken chain of chosen mornings, each one "
            "signed, none regretted."
        ),
    },
    {
        "key": "small_things_thanks",
        "name": "Thank You For The Small Things",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "\"Thank you for the coffee you make without being asked, for "
            "the way you warm up the car on cold mornings, for remembering "
            "how I take my tea. These small things are not small to me.\" "
            "A foundation statement that itemizes invisible care. Where \"I "
            "Notice You\" is the witness, this is the receipt: it lists "
            "the small acts back to the person, proving each one landed. "
            "Itemization is powerful because it shows the acts were not "
            "merged into a vague \"thanks for everything\" - each was "
            "felt individually."
        ),
        "how_it_works": (
            "Say it as a list of three to five true small acts, spoken or "
            "written. Collect them over a week: the coffee, the car, the "
            "remembered preference, the charged phone, the saved leftovers. "
            "Personalize it by using their actual habits - the list must be "
            "theirs, not generic. Deliver it at a quiet moment, maybe as a "
            "note left where they will find it. End with the reframe: "
            "\"these small things are not small to me\" - that closing line "
            "is the thesis, and it teaches them that their daily care has "
            "daily weight. Do not turn the list into a scorecard of what "
            "you do back; this is one-directional gratitude."
        ),
        "key_points": [
            "Itemization proves each small act landed individually, not merged into vague thanks.",
            "Collect the true list over a week; the list must be theirs, not generic.",
            "Three to five items is the sweet spot: enough to feel thorough, short enough to feel true.",
            "The closing reframe - not small to me - is the thesis; do not skip it.",
            "One-directional gratitude only; never a scorecard of what you do back.",
        ],
        "requirements": [
            "Three to five true small acts, actually observed over days.",
            "The acts named in their specific form (the coffee, the car, the tea).",
            "The \"not small to me\" closing reframe.",
            "Quiet-moment delivery: note, calm evening, or slow morning.",
            "No reciprocal scorekeeping attached.",
        ],
        "standards": [
            "Truth standard: every listed act must be real and observed, never invented.",
            "Count standard: three to five items; fewer feels thin, more feels like a ledger.",
            "Direction standard: gratitude flows one way in this statement.",
        ],
        "citations": [CIT_CHAPMAN, CIT_GOTTMAN],
        "sig_lens": (
            "Signature lens: the Signature way issues an itemized receipt "
            "for care - each small act logged, dated, and acknowledged. The "
            "record reads: coffee, car, tea, charged phone, saved leftovers "
            "- none of it small, all of it stamped."
        ),
    },
    {
        "key": "safe_with_me",
        "name": "You Are Safe With Me",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "\"You are safe with me. Your feelings, your fears, your bad "
            "days - all of it has a home here, and I will never use it "
            "against you.\" A foundation statement of emotional safety. It "
            "is the precondition for every deeper statement in this "
            "database: no one opens their heart to someone who might "
            "weaponize it. Saying it explicitly matters because safety "
            "assumed is not safety felt - the promise has to be spoken to "
            "be real."
        ),
        "how_it_works": (
            "Say it in a calm, private moment - never during a conflict, "
            "where it sounds like a maneuver. Look them in the eye if you "
            "can; safety is conveyed through steadiness. Personalize it by "
            "naming what they tend to hide: \"You do not have to be the "
            "strong one with me. The scared parts, the tired parts - bring "
            "them here.\" Then prove it over time: when they do show you "
            "something vulnerable, receive it gently and never, ever throw "
            "it back in a later argument. The statement is a contract, and "
            "the fine print is your future behavior. Revisit it after any "
            "fight: \"What you told me is still safe. The argument does not "
            "change that.\""
        ),
        "key_points": [
            "Safety assumed is not safety felt; the promise must be spoken to be real.",
            "It is the precondition for every deeper statement - vulnerability needs a guaranteed receiver.",
            "Name what they tend to hide; the personalization shows you already see it.",
            "The statement is a contract whose fine print is your future behavior.",
            "Revisit it after conflicts: what was shared stays safe regardless of the argument.",
        ],
        "requirements": [
            "Calm, private delivery, never mid-conflict.",
            "Steady presence: eye contact, unhurried tone.",
            "The \"never use it against you\" clause stated explicitly.",
            "Naming of what they tend to hide, personalized.",
            "Future proof: vulnerable shares never weaponized in later arguments.",
        ],
        "standards": [
            "Timing standard: calm moments only; mid-conflict delivery reads as maneuver.",
            "Contract standard: the promise binds future behavior, especially after fights.",
            "Revisit standard: reaffirm after any conflict that touched vulnerable ground.",
        ],
        "citations": [CIT_ROSENBERG, CIT_GOTTMAN],
        "sig_lens": (
            "Signature lens: the Signature way issues safety as a stamped "
            "contract - feelings, fears, bad days all granted asylum, with "
            "the iron clause: nothing shared here is ever weaponized. "
            "Signed, witnessed, binding."
        ),
    },
    {
        "key": "admire_becoming",
        "name": "I Admire Who You Are Becoming",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "\"I admire who you are becoming. I loved who you were, I love "
            "who you are, but watching you grow - the way you face hard "
            "things now, the patience you are building - that might be my "
            "favorite part.\" A foundation statement that loves the "
            "trajectory, not just the snapshot. People fear that growth "
            "will cost them love (\"will you still love me if I change\"); "
            "this statement answers that fear directly: your becoming is "
            "itself beloved."
        ),
        "how_it_works": (
            "Say it when you notice a genuine change: new patience, new "
            "courage, a handled-differently situation. Name the before and "
            "the after: \"A year ago that comment would have wrecked your "
            "week. Today you just smiled. I admire that.\" Personalize it "
            "with the specific growth you have witnessed - the statement "
            "fails if the growth is vague. This is especially powerful for "
            "partners in long relationships (loving the evolving person, "
            "not the memory of who they were) and for children (naming "
            "their growth teaches them to value becoming). Never frame "
            "growth as fixing a flaw; frame it as unfolding a strength."
        ),
        "key_points": [
            "Loving the trajectory answers the fear that growth will cost love.",
            "Name the before and after; vague growth-praise does not convince.",
            "Say it when you witness a genuine handled-differently moment.",
            "For long love, it keeps affection aimed at the living person, not the memory.",
            "Frame growth as unfolding strength, never as fixing a flaw.",
        ],
        "requirements": [
            "A genuine observed change, named with before-and-after.",
            "The \"becoming is beloved\" claim stated directly.",
            "Delivery near the witnessed moment.",
            "Strength-unfolding framing, never flaw-fixing.",
            "Coverage for long partners and growing children alike.",
        ],
        "standards": [
            "Evidence standard: the change must be real and named, never vague.",
            "Framing standard: unfolding, not fixing.",
            "Timing standard: near the witnessed moment, while the evidence is fresh.",
        ],
        "citations": [CIT_FROMM, CIT_LEWIS],
        "sig_lens": (
            "Signature lens: the Signature way charts the person as a "
            "rising curve, not a snapshot - each new patience, each new "
            "courage logged as growth data. The record honors not just who "
            "they are, but the direction they are moving."
        ),
    },
    {
        "key": "way_you_love",
        "name": "The Way You Love",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "\"I love the way you love. The way you remember everyone's "
            "birthday, the way you sit with someone who is hurting instead "
            "of rushing to fix them, the way you make people feel like they "
            "are the only person in the room. Being loved by you taught me "
            "how to love better.\" A foundation statement that admires "
            "their loving itself. It is meta-appreciation: not thanking "
            "them for loving you, but honoring how they love everyone. "
            "This tells them their heart is not just useful to you - it is "
            "beautiful in itself."
        ),
        "how_it_works": (
            "Say it after you watch them love someone else well - with a "
            "friend in crisis, a child, a stranger. The observation of "
            "their love in the wild is what gives the statement its "
            "authority. Personalize it with the witnessed scene: \"Watching "
            "you sit with your mother yesterday, not fixing, just sitting - "
            "that is when I thought: I love the way this person loves.\" "
            "Include the self-effect: \"being loved by you taught me how to "
            "love better\" - it tells them their love is instructive, not "
            "just comforting. Works beautifully for parents (honoring how "
            "they raised you) and for partners whose kindness radiates "
            "outward."
        ),
        "key_points": [
            "Meta-appreciation: honor how they love everyone, not just what their love does for you.",
            "Authority comes from witnessing their love in the wild, with someone else.",
            "Name the witnessed scene; the specificity is the proof.",
            "Include the self-effect: their love taught you to love better.",
            "It tells them their heart is beautiful in itself, not merely useful.",
        ],
        "requirements": [
            "A witnessed scene of them loving someone else well.",
            "The scene named specifically in the statement.",
            "The \"way you love\" framing, distinct from \"love you for.\"",
            "The self-effect included: what their love taught you.",
            "Delivery after the witnessing, while the scene is fresh.",
        ],
        "standards": [
            "Witness standard: the statement must rest on an observed scene, not a general impression.",
            "Distinction standard: about their loving, not about their service to you.",
            "Freshness standard: deliver while the witnessed moment still glows.",
        ],
        "citations": [CIT_LEWIS, CIT_GIBRAN],
        "sig_lens": (
            "Signature lens: the Signature way studies their love as a "
            "masterwork - observed in the wild, documented scene by scene. "
            "The record notes: this is not just love received; it is love "
            "as art, and it taught the observer how to love."
        ),
    },
    {
        "key": "favorite_person",
        "name": "My Favorite Person",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "\"Of all the people in the world, you are my favorite. Not the "
            "most famous or the most impressive - just the one I would "
            "choose, every time, in every life.\" A foundation statement of "
            "chosen-ness. It is playful on the surface and profound "
            "underneath: out of billions, the choice is you, and it would "
            "be you again. The \"every life\" line gives it a touch of "
            "the eternal without heaviness, which is why it works as both "
            "a light tease and a deep truth."
        ),
        "how_it_works": (
            "Say it lightly - over dinner, on a walk, in a text with no "
            "context. The lightness is the delivery system for the depth; "
            "said too solemnly it becomes pressure, said playfully it "
            "becomes treasure. Personalize it with the choosing frame: "
            "\"If I had to pick a teammate for anything - trivia, road "
            "trips, life - it is you.\" For children, it is pure gold: "
            "every child should hear they are someone's favorite person. "
            "For friends, it cements the bond without awkwardness because "
            "the tone stays light. The \"not the most famous\" clause "
            "matters: it says the choosing is about fit and heart, not "
            "status."
        ),
        "key_points": [
            "Chosen-ness out of billions is playful on the surface, profound underneath.",
            "Lightness is the delivery system; solemnity would turn it into pressure.",
            "The \"every life\" line adds eternity without heaviness.",
            "The \"not the most famous\" clause says the choice is about heart, not status.",
            "For children, hearing they are someone's favorite person is pure gold.",
        ],
        "requirements": [
            "Light, playful delivery: dinner, walk, or context-free text.",
            "The out-of-billions choosing frame stated plainly.",
            "The \"every life\" eternity touch, kept light.",
            "The heart-over-status clause included.",
            "A choosing example personalized: trivia, road trips, life.",
        ],
        "standards": [
            "Tone standard: playful treasure, never solemn pressure.",
            "Choosing standard: the billions-to-one frame must be explicit.",
            "Fit standard: heart and fit over fame and status, stated outright.",
        ],
        "citations": [CIT_BROWNING, CIT_CHAPMAN],
        "sig_lens": (
            "Signature lens: the Signature way runs the choosing as a "
            "computation over all people, all lives - and the result is "
            "stamped, every time: this one. The favorite is not a mood; it "
            "is the output of the whole system."
        ),
    },
    {
        "key": "grateful_patience",
        "name": "Gratitude For Your Patience",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "\"Thank you for your patience with me. For the times I was "
            "difficult, distracted, or slow to understand - you stayed "
            "gentle, and I have never taken that for granted.\" A "
            "foundation statement that honors the patience others extend "
            "to us. Patience is the most under-thanked virtue in "
            "relationships: it is exercised daily and acknowledged almost "
            "never. Naming it tells the patient person that their restraint "
            "was seen, and that it mattered."
        ),
        "how_it_works": (
            "Say it after a stretch where you know you were hard to be "
            "around - a stressful project, a grieving period, a learning "
            "curve. Honesty about your own difficulty is what makes the "
            "gratitude credible; vague thanks for \"patience\" without "
            "admitting what tested it feels hollow. Personalize it by "
            "naming the testing period: \"These last three months of night "
            "shifts, I know I was barely present. Thank you for staying "
            "gentle.\" Do not follow it with a repeat of the difficult "
            "behavior - gratitude for patience is a promise to need less "
            "of it. For parents and long-suffering partners, this statement "
            "can land like rain after drought."
        ),
        "key_points": [
            "Patience is the most under-thanked virtue: exercised daily, acknowledged almost never.",
            "Honesty about what tested their patience is what makes the gratitude credible.",
            "Name the testing period specifically; vague thanks feels hollow.",
            "Gratitude for patience is a promise to need less of it going forward.",
            "For the long-patient, this statement can land like rain after drought.",
        ],
        "requirements": [
            "An honest naming of the period or behavior that tested them.",
            "The \"stayed gentle\" acknowledgment, specific.",
            "The \"never taken for granted\" assurance.",
            "Delivery after the testing stretch, in calm.",
            "A forward promise: working to need less patience, not just thanking it.",
        ],
        "standards": [
            "Honesty standard: name what you put them through, or the thanks is hollow.",
            "Forward standard: gratitude must carry a promise of less burden ahead.",
            "Timing standard: after the stretch, in calm - never mid-difficulty as a deflection.",
        ],
        "citations": [CIT_GOTTMAN, CIT_ROSENBERG],
        "sig_lens": (
            "Signature lens: the Signature way audits the patience extended "
            "and finds it extraordinary - every tested month logged, every "
            "gentle response stamped. The record closes the books with "
            "thanks and a forward covenant: less burden ahead."
        ),
    },
    # ---------------- Compounded: heartfelt devotion ----------------
    {
        "key": "hard_season",
        "name": "Through The Hard Season",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "\"I know this season is heavy, and I cannot carry it for you. "
            "But I can stand beside you while you carry it, and I will not "
            "leave. You do not have to be strong for me.\" A compounded "
            "statement for suffering: love that does not fix, does not "
            "flee, and does not demand performance. It is honest about its "
            "limits (\"I cannot carry it for you\") which is exactly why "
            "the promise beside it is believable. This is the statement for "
            "grief, illness, depression, and failure."
        ),
        "how_it_works": (
            "Say it early in the hard season, then prove it with presence: "
            "showing up, sitting in silence, handling the small logistics "
            "without being asked. The statement opens the door; the weeks "
            "after walk through it. Personalize it by naming the weight: "
            "\"I know the treatments are wearing you down\" beats \"I know "
            "things are hard.\" Never follow it with silver linings or "
            "timelines (\"you will be fine by spring\") - the statement's "
            "power is in staying inside the heaviness with them. \"You do "
            "not have to be strong for me\" is the key that unlocks the "
            "mask; say it, and mean it when they fall apart in front of "
            "you. Check back unprompted: the second and third visits prove "
            "the first promise."
        ),
        "key_points": [
            "Honesty about limits (\"I cannot carry it\") is what makes the beside-promise believable.",
            "Love here does not fix, does not flee, and does not demand performance.",
            "Name the weight specifically; generic sympathy does not reach grief.",
            "Never attach silver linings or timelines; stay inside the heaviness with them.",
            "\"You do not have to be strong for me\" unlocks the mask - then honor what comes out.",
        ],
        "requirements": [
            "Early delivery in the hard season, before they have to ask.",
            "The weight named specifically, not generically.",
            "The honest limit stated: what you cannot do.",
            "The beside-promise: presence without fixing or fleeing.",
            "Unprompted follow-through: second and third visits that prove the first words.",
        ],
        "standards": [
            "Honesty standard: name your limits; false omnipotence breaks trust later.",
            "No-fixing standard: presence, logistics, silence - never silver linings or timelines.",
            "Proof standard: the statement is a down payment; the weeks after are the balance.",
        ],
        "citations": [CIT_LEWIS, CIT_ROSENBERG],
        "sig_lens": (
            "Signature lens: the Signature way does not flinch at the hard "
            "season - it logs the weight honestly, declares its limits, and "
            "stamps the beside-promise as binding. Presence is the "
            "deliverable, and it is delivered on schedule, unprompted."
        ),
    },
    {
        "key": "believe_in_you",
        "name": "I Believe In You",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "\"When you doubt yourself, borrow my belief in you. I have "
            "seen what you are capable of, and I am not guessing - I "
            "know.\" A compounded statement that loans confidence. "
            "Self-doubt is loudest right before the leap; this statement "
            "places your certainty where their doubt is, like a "
            "counterweight. \"Borrow\" is the key word: it frames belief "
            "as a resource they can draw on until their own regenerates."
        ),
        "how_it_works": (
            "Say it when you see the doubt: the hesitation before the "
            "application, the audition, the hard conversation. Timing is "
            "everything - belief delivered at the moment of wobble lands "
            "ten times harder than belief delivered at leisure. Personalize "
            "it with evidence: \"I watched you master the last impossible "
            "thing. This is the same muscle.\" Evidence converts the "
            "statement from cheerleading to testimony. Do not inflate: "
            "\"you will definitely win\" is a hostage to fortune; \"you "
            "are capable of this, and I know it\" is unbreakable. After "
            "the event, whatever the outcome, honor the attempt: the loan "
            "of belief is repaid by acknowledging the courage, not just "
            "the win."
        ),
        "key_points": [
            "\"Borrow my belief\" frames confidence as a loanable resource for the season of doubt.",
            "Deliver at the moment of wobble; timing multiplies the impact tenfold.",
            "Evidence converts cheerleading into testimony: name what they have already mastered.",
            "Never inflate into guaranteed outcomes; \"capable\" is unbreakable, \"will win\" is a hostage.",
            "After the event, honor the courage of the attempt regardless of outcome.",
        ],
        "requirements": [
            "A visible moment of doubt as the delivery trigger.",
            "The \"borrow\" framing: belief as a loan, not a lecture.",
            "Concrete evidence of past capability, named.",
            "No guaranteed outcomes promised.",
            "Post-event acknowledgment of courage, win or lose.",
        ],
        "standards": [
            "Timing standard: at the wobble, not at leisure.",
            "Evidence standard: testimony over cheerleading; name the past mastery.",
            "Outcome standard: capable, never guaranteed.",
        ],
        "citations": [CIT_GOTTMAN, CIT_FROMM],
        "sig_lens": (
            "Signature lens: the Signature way extends belief as a formal "
            "loan - underwritten by witnessed evidence, drawn at the moment "
            "of wobble, repayable in courage. The ledger shows: capability "
            "proven, belief issued, no inflated guarantees."
        ),
    },
    {
        "key": "apology_heals",
        "name": "The Apology That Heals",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "\"I was wrong, and I am sorry - truly sorry, not just sorry "
            "you are upset. You deserved better from me, and I will do the "
            "work to be better.\" A compounded repair statement. It is "
            "included in a book of loving statements because repair is a "
            "love language: the willingness to be wrong out loud is one of "
            "the most loving things a person can do. The statement has four "
            "load-bearing parts: ownership, true sorrow, their worth, and "
            "the work ahead."
        ),
        "how_it_works": (
            "Say it once you actually understand what you did - a rushed "
            "apology apologizes for the wrong thing. Name the wrong "
            "specifically: \"I dismissed your worry about the money, and "
            "that was wrong.\" The \"not just sorry you are upset\" clause "
            "is the difference between repair and management; say it and "
            "mean it. Personalize it with the work: \"I am going to listen "
            "all the way through before I respond from now on\" - a named "
            "change, not a vague promise. Then do the work visibly; the "
            "apology is the door, the changed behavior is the house. Never "
            "use it to demand forgiveness on a timeline; the statement "
            "offers repair, it does not invoice for absolution."
        ),
        "key_points": [
            "Repair is a love language: being wrong out loud is profoundly loving.",
            "Four load-bearing parts: ownership, true sorrow, their worth, the work ahead.",
            "Name the wrong specifically; rushed apologies apologize for the wrong thing.",
            "\"Not just sorry you are upset\" separates repair from management.",
            "The apology is the door; changed behavior is the house. Never invoice for absolution.",
        ],
        "requirements": [
            "Full understanding of the wrong before speaking.",
            "The wrong named specifically.",
            "The \"truly sorry, not just sorry you are upset\" distinction.",
            "A named behavioral change, not a vague promise.",
            "Visible follow-through with no demanded forgiveness timeline.",
        ],
        "standards": [
            "Understanding standard: never apologize before you know what for.",
            "Specificity standard: the wrong and the change both named.",
            "No-invoice standard: repair is offered, absolution is never billed.",
        ],
        "citations": [CIT_GOTTMAN, CIT_ROSENBERG],
        "sig_lens": (
            "Signature lens: the Signature way treats repair as engineering "
            "- fault named, root cause understood, corrective action "
            "specified, verification scheduled. The apology is stamped as "
            "the work order; the changed behavior is the completed job."
        ),
    },
    {
        "key": "changed_my_life",
        "name": "You Changed My Life",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "\"Before you, I did not know life could feel like this. You "
            "did not just enter my story - you changed what the story was "
            "about.\" A compounded statement of life-altering love. It "
            "credits the person with a before-and-after in your existence: "
            "not an improvement to a chapter, but a change of genre. This "
            "is the statement for the love that redefined the terms - the "
            "partner, the child, the friend who arrived and rearranged "
            "everything."
        ),
        "how_it_works": (
            "Say it on a milestone that invites reflection: anniversaries, "
            "birthdays, the anniversary of the day you met, or a quiet "
            "night when the weight of it hits you. The reflective occasion "
            "gives the grand claim its natural frame. Personalize it with "
            "the before: \"Before you, my life was a checklist. You made "
            "it a story.\" The before-and-after structure is the whole "
            "mechanism - name both sides honestly. Do not exaggerate the "
            "before into misery if it was not; \"I was fine, and you made "
            "fine feel like the warm-up\" is more credible and more "
            "moving. For a child: \"You did not just join our family; you "
            "taught us what family was for.\""
        ),
        "key_points": [
            "Credits the person with a genre-change in your story, not just a better chapter.",
            "Milestone occasions give the grand claim its natural frame.",
            "The before-and-after structure is the mechanism; name both sides honestly.",
            "Do not exaggerate the before into misery; credible contrast moves more.",
            "For a child: they taught the family what family was for.",
        ],
        "requirements": [
            "A reflective occasion: anniversary, birthday, meeting-day, or a weighty quiet night.",
            "The \"before\" named honestly, without melodrama.",
            "The genre-change claim: what the story became about.",
            "Credible contrast: fine-to-extraordinary beats miserable-to-saved.",
            "A child-adapted version ready for parental use.",
        ],
        "standards": [
            "Occasion standard: reflective milestones frame the grand claim naturally.",
            "Honesty standard: the before must be true; melodrama cheapens the after.",
            "Structure standard: before and after both named; the contrast does the work.",
        ],
        "citations": [CIT_BROWNING, CIT_GIBRAN],
        "sig_lens": (
            "Signature lens: the Signature way records the arrival as a "
            "system event - before-state logged, after-state logged, the "
            "delta stamped as life-altering. The story did not just gain a "
            "character; its genre was reclassified, on the record."
        ),
    },
    {
        "key": "partner_teammate",
        "name": "My Partner, My Teammate",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "\"You are not just the person I love. You are my teammate, my "
            "co-builder, the one I want in the trenches with me when "
            "everything is on the line.\" A compounded statement that "
            "honors partnership as alliance. Romance gets the poetry; "
            "alliance gets the trust. This statement tells a partner they "
            "are chosen for the hard parts too - the 3 a.m. emergencies, "
            "the impossible months, the decisions with no good options. "
            "Being wanted in the trenches is a deeper compliment than being "
            "wanted at the celebration."
        ),
        "how_it_works": (
            "Say it after you have weathered something hard together - the "
            "move, the illness, the lean year - while the shared effort is "
            "still fresh. The recent proof makes the claim undeniable. "
            "Personalize it with the trenches you have shared: \"When the "
            "roof leaked and the car died in the same week, you were calm "
            "and we handled it. That is when I knew: you are my teammate.\" "
            "Use it to reframe conflict too: \"We are on the same team; the "
            "problem is the opponent, not each other\" - the teammate frame "
            "turns fights into strategy sessions. Renew it yearly; "
            "alliances, like vows, appreciate restating."
        ),
        "key_points": [
            "Alliance is deeper than romance: being wanted in the trenches beats being wanted at the celebration.",
            "Deliver after a weathered hardship, while the shared effort is fresh.",
            "Name the trenches you shared; recent proof makes the claim undeniable.",
            "The teammate frame turns conflicts into strategy sessions: same team, problem as opponent.",
            "Renew it yearly; alliances appreciate restating like vows do.",
        ],
        "requirements": [
            "A shared hardship survived together as the proof context.",
            "The trenches named: the specific hard stretch.",
            "The teammate/co-builder framing stated plainly.",
            "The conflict reframe ready: same team, problem as opponent.",
            "Yearly renewal of the alliance statement.",
        ],
        "standards": [
            "Proof standard: the claim must rest on a survived hardship, not a wish.",
            "Frame standard: teammate language in conflict, not just in calm.",
            "Renewal standard: restated yearly, like vows.",
        ],
        "citations": [CIT_GOTTMAN, CIT_FROMM],
        "sig_lens": (
            "Signature lens: the Signature way formalizes the alliance - "
            "co-builder status stamped after field testing in the trenches. "
            "The record shows: tested under load, calm under fire, chosen "
            "for every hard thing ahead."
        ),
    },
    {
        "key": "sacrifices_family",
        "name": "Thank You For Your Sacrifices",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "\"I know what you gave up for this family, and I have never "
            "forgotten it. Every late night, every dream you set aside - it "
            "built the life we stand in now.\" A compounded statement of "
            "family gratitude for the sacrifices that built the present. "
            "Parents, grandparents, and eldest siblings carry invisible "
            "ledgers of deferred dreams; this statement reads the ledger "
            "back to them. It is one of the most powerful things an adult "
            "child can say to a parent."
        ),
        "how_it_works": (
            "Say it when you are old enough to understand the cost - and "
            "say it before it is too late to matter. Holidays, milestone "
            "birthdays, or a quiet visit are natural frames. Personalize "
            "it with the specific deferred dreams you know about: \"You "
            "gave up the nursing degree to keep us fed. I know.\" If you "
            "do not know the specifics, say so honestly and invite them: "
            "\"Tell me what you set aside - I want to know.\" That "
            "invitation is itself a gift; sacrificers rarely get asked. "
            "Connect the sacrifice to the present: \"it built the life we "
            "stand in now\" - this converts the loss into legacy, which is "
            "the only alchemy that honors it. Never follow with guilt "
            "about your own choices; this is their honor, not your debt."
        ),
        "key_points": [
            "Reads the invisible ledger of deferred dreams back to the sacrificer.",
            "One of the most powerful things an adult child can say to a parent.",
            "Name the specific deferred dreams; if unknown, invite the telling.",
            "Convert loss to legacy: the sacrifice built the life you stand in now.",
            "Their honor, not your debt: never attach guilt about your own choices.",
        ],
        "requirements": [
            "Sufficient maturity to understand the cost, stated honestly.",
            "The deferred dreams named, or the invitation to tell them.",
            "The loss-to-legacy conversion: what the sacrifice built.",
            "A natural frame: holiday, milestone, or quiet visit.",
            "Zero guilt-attachment about the speaker's own choices.",
        ],
        "standards": [
            "Knowledge standard: name the dreams, or honestly invite the telling.",
            "Legacy standard: the sacrifice must be converted to what it built.",
            "Honor standard: their honor, never your debt.",
        ],
        "citations": [CIT_LEWIS, CIT_GIBRAN],
        "sig_lens": (
            "Signature lens: the Signature way audits the family ledger - "
            "late nights logged, deferred dreams itemized - and issues the "
            "finding as honor: every set-aside converted to foundation, "
            "every sacrifice stamped as the beams of the house you stand "
            "in."
        ),
    },
    {
        "key": "friend_stayed",
        "name": "The Friend Who Stayed",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "\"Everyone loves you when you are winning. You loved me when "
            "I was losing. That is the difference between a friend and a "
            "brother, and you are the second one.\" A compounded statement "
            "of friendship loyalty. It draws the bright line between "
            "fair-weather and true, and places the friend on the true side "
            "with evidence. Adapt the kinship term to fit (brother, sister, "
            "family) - the point is the promotion from friend to kin by "
            "proof of loyalty."
        ),
        "how_it_works": (
            "Say it after the losing season has passed and you can see it "
            "clearly - or in the middle of it, when the staying is "
            "happening. Both timings work; the middle-of-it version is "
            "braver. Personalize it with the losing season named: \"When "
            "the business failed and I was embarrassed to answer the "
            "phone, you kept calling.\" The evidence of staying is the "
            "whole statement; without it, it is just a nice sentiment. "
            "Choose the kinship promotion that fits your bond and say it "
            "plainly - \"you are my brother\" said to a friend is a "
            "knighthood. Deliver it one-to-one, not in a group toast; this "
            "is a private honor."
        ),
        "key_points": [
            "Draws the bright line between fair-weather and true, with evidence.",
            "The losing season named is the whole statement; without it, mere sentiment.",
            "The kinship promotion (friend to brother/sister) is a knighthood - say it plainly.",
            "Middle-of-the-hard-time delivery is braver than after-the-fact.",
            "Private one-to-one honor, not a group toast.",
        ],
        "requirements": [
            "A named losing season where they stayed.",
            "The staying evidenced: what they actually did.",
            "The kinship promotion stated plainly.",
            "One-to-one private delivery.",
            "Timing either mid-hardship (braver) or clear-eyed after.",
        ],
        "standards": [
            "Evidence standard: the staying must be evidenced, not asserted.",
            "Privacy standard: private honor; group toasts dilute it.",
            "Promotion standard: the kinship word must fit the bond and be said plainly.",
        ],
        "citations": [CIT_LEWIS, CIT_FROMM],
        "sig_lens": (
            "Signature lens: the Signature way promotes by proof - the "
            "losing season logged, the staying evidenced call by call, and "
            "the promotion stamped: from friend to kin, effective "
            "immediately, on the record."
        ),
    },
    {
        "key": "i_forgive_you",
        "name": "I Forgive You",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "\"I forgive you - really forgive you, not the kind that keeps "
            "score. What happened is in the past, and I am choosing our "
            "future over my pride.\" A compounded statement of release. "
            "Forgiveness here is framed as a choice for the future, not a "
            "verdict on the past - which makes it giveable even when the "
            "hurt was real. The \"not the kind that keeps score\" clause is "
            "the load-bearing beam: everyone has heard forgiveness that was "
            "really a ledger entry."
        ),
        "how_it_works": (
            "Say it only when it is true - premature forgiveness is a "
            "loan you will call in later. When the work of processing is "
            "done and the choice is real, say it plainly and completely. "
            "Personalize it by naming what is released: \"I forgive you "
            "for missing the recital. It is in the past.\" Naming the "
            "thing prevents the vague fog where old hurts hide. Then live "
            "it: the released thing must never reappear in future "
            "arguments, or the statement becomes a lie retroactively. If "
            "full forgiveness is not yet true, say the honest intermediate: "
            "\"I am working toward forgiving you, and I want you to know "
            "that.\" That is a loving statement too, and it keeps the "
            "record honest."
        ),
        "key_points": [
            "Framed as a choice for the future, not a verdict on the past - giveable even when hurt was real.",
            "\"Not the kind that keeps score\" is the load-bearing beam; scorekeeping forgiveness is a ledger entry.",
            "Say it only when true; premature forgiveness is a loan you will call in later.",
            "Name the released thing; vague fog is where old hurts hide.",
            "Live it: the released thing never reappears in future arguments.",
        ],
        "requirements": [
            "Genuine readiness: the processing work done before speaking.",
            "The released hurt named specifically.",
            "The no-scorekeeping clause stated plainly.",
            "The future-over-pride framing.",
            "Permanent retirement of the hurt from future arguments.",
        ],
        "standards": [
            "Truth standard: only when real; the honest intermediate (\"working toward\") when not.",
            "Specificity standard: the released thing named, never fogged.",
            "Permanence standard: released means retired from all future arguments.",
        ],
        "citations": [CIT_ROSENBERG, CIT_LEWIS],
        "sig_lens": (
            "Signature lens: the Signature way closes the books cleanly - "
            "the hurt itemized, the release stamped, the ledger zeroed with "
            "no balance carried forward. Future chosen over pride, on the "
            "record, irreversible."
        ),
    },
    {
        "key": "beautiful_to_me",
        "name": "You Are Beautiful To Me",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "\"You are beautiful to me - not in the way magazines mean it, "
            "but in the way that matters: the way your face looks when you "
            "laugh, the way your eyes soften when you care, the way you "
            "look first thing in the morning, entirely yourself.\" A "
            "compounded statement that redefines beauty as the beloved's "
            "truth. It deliberately contrasts commercial beauty with "
            "witnessed beauty, and chooses the witnessed kind. This is "
            "especially healing for anyone who has felt measured against "
            "impossible standards."
        ),
        "how_it_works": (
            "Say it in an unguarded moment - morning, no makeup, "
            "laughing, tired - when they are least performing beauty. The "
            "contrast between their unguardedness and your declaration is "
            "the medicine. Personalize it with their true beautiful "
            "moments: the laugh-face, the caring-eyes, the morning-self. "
            "Never compare them to others (\"more beautiful than...\") - "
            "comparison keeps the measuring system alive; this statement "
            "replaces the system. For long partners, add the time depth: "
            "\"Twenty years, and you are more beautiful to me now\" - "
            "beauty that compounds with knowing is the deepest compliment "
            "of all."
        ),
        "key_points": [
            "Redefines beauty as the beloved's witnessed truth, not commercial standard.",
            "Deliver in unguarded moments; the contrast with their unguardedness is the medicine.",
            "Name their true beautiful moments: laugh-face, caring-eyes, morning-self.",
            "Never compare to others; comparison keeps the measuring system alive.",
            "Time depth compounds it: more beautiful now, after years of knowing.",
        ],
        "requirements": [
            "An unguarded moment as delivery context.",
            "The commercial-vs-witnessed distinction stated.",
            "Their true beautiful moments named specifically.",
            "Zero comparisons to other people.",
            "Time-depth line for long relationships when true.",
        ],
        "standards": [
            "Context standard: unguarded moments; performed moments dilute the medicine.",
            "No-comparison standard: the statement replaces the measuring system.",
            "Truth standard: the named moments must be real witnessed ones.",
        ],
        "citations": [CIT_BROWNING, CIT_SHAKESPEARE],
        "sig_lens": (
            "Signature lens: the Signature way rejects the commercial "
            "measuring system entirely and stamps its own standard: beauty "
            "as witnessed truth. The record lists laugh-face, caring-eyes, "
            "morning-self - and notes the value compounding with every "
            "year of knowing."
        ),
    },
    {
        "key": "anniversary_vow",
        "name": "The Anniversary Vow",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "\"Another year, and I would still choose you - not out of "
            "habit, but out of certainty. You are the best decision I ever "
            "made, and I make it again today.\" A compounded anniversary "
            "statement. Its power is in the denial of habit: long love is "
            "often suspected (even by the lovers) of running on inertia, "
            "and this statement answers that suspicion head-on. It renews "
            "the choice with full knowledge of the cost, which is what "
            "makes it a vow rather than a sentiment."
        ),
        "how_it_works": (
            "Say it on the anniversary itself - dating, wedding, or the "
            "day you met - when the year is being weighed. The occasion "
            "does half the work. Personalize it with the year's evidence: "
            "\"This year had the hospital scare and the new job and your "
            "mother moving in - and I would still choose you, with all of "
            "it.\" The \"with all of it\" is crucial: certainty that has "
            "seen the hard year is worth ten certainties from easy years. "
            "Write it down too - anniversary vows kept in a drawer become "
            "a library of choosing that outlasts memory. Say it looking at "
            "them; this one deserves eyes."
        ),
        "key_points": [
            "Denies habit directly: the choice is certainty, not inertia.",
            "Renewal with full knowledge of the cost is what makes it a vow.",
            "The year's evidence named: certainty after the hard year is worth ten easy ones.",
            "\"With all of it\" is the crucial clause; do not soften it.",
            "Write it down; anniversary vows become a library of choosing.",
        ],
        "requirements": [
            "The anniversary occasion itself as the frame.",
            "The habit-denial stated plainly: certainty, not inertia.",
            "The year's hard evidence named and included in the choosing.",
            "The \"with all of it\" clause kept intact.",
            "Written copy kept, plus spoken delivery with eye contact.",
        ],
        "standards": [
            "Occasion standard: the anniversary frame does half the work; do not waste it.",
            "Knowledge standard: the vow must show it has seen the real year.",
            "Record standard: written and kept; memory alone is not the archive.",
        ],
        "citations": [CIT_SHAKESPEARE, CIT_GOTTMAN],
        "sig_lens": (
            "Signature lens: the Signature way renews the choice as a "
            "formal annual restamping - the year's evidence reviewed, the "
            "hard parts included, the decision reissued with full "
            "knowledge. Not inertia: a vow, re-signed, filed in the growing "
            "library of choosing."
        ),
    },
    {
        "key": "see_your_heart",
        "name": "I See Your Heart",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "\"I see past the armor to the heart underneath, and I love "
            "what I find there. You do not have to perform for me. I "
            "already know, and I already stay.\" A compounded statement "
            "for the guarded: the strong ones, the jokers, the "
            "always-fine people. It tells them the performance is "
            "unnecessary - seen, known, and stayed-with anyway. \"I "
            "already stay\" is the past-tense promise: not I will stay "
            "(future, conditional), but I already stay (present, decided)."
        ),
        "how_it_works": (
            "Say it in a quiet moment after they have let something real "
            "slip - the joke that cracked, the \"I am fine\" that was not "
            "fine. Do not force the armor off; the statement simply "
            "announces that the armor is unnecessary. Personalize it by "
            "naming their armor kindly: \"You do not have to be the funny "
            "one with me. I love the funny one, but I am here for the "
            "quiet one too.\" Never use what you see past the armor as "
            "leverage later - this statement and \"You Are Safe With Me\" "
            "are companion contracts. If they test it by showing you "
            "something ugly, receive it without flinching; the test is the "
            "proof phase."
        ),
        "key_points": [
            "For the guarded: announces the performance is unnecessary.",
            "\"I already stay\" is past-tense and decided; stronger than any future promise.",
            "Name their armor kindly; the personalization proves you actually see it.",
            "Never force the armor off; the statement invites, it does not pry.",
            "When they test it with something ugly, receive without flinching; the test is the proof phase.",
        ],
        "requirements": [
            "A quiet moment, ideally after a real slip past the armor.",
            "Their armor named kindly and specifically.",
            "The \"no performance needed\" release stated.",
            "The \"I already stay\" past-tense promise.",
            "Flinch-free reception when they test it.",
        ],
        "standards": [
            "Invitation standard: announce, never pry; the armor opens on their schedule.",
            "Tense standard: already stay, not will stay.",
            "Proof standard: the test showing must be received without flinching.",
        ],
        "citations": [CIT_ROSENBERG, CIT_LEWIS],
        "sig_lens": (
            "Signature lens: the Signature way sees through to the heart "
            "and stamps what it finds: beloved, no performance required. "
            "The armor is logged as unnecessary equipment - the record "
            "shows the guarded one already known, already stayed-with."
        ),
    },
    {
        "key": "lifetime_gratitude",
        "name": "Gratitude For A Lifetime Of Love",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "\"Everything good in me has your fingerprints on it. The way "
            "I work, the way I love, the way I show up - I learned it "
            "watching you.\" A compounded statement of inherited goodness. "
            "It tells a parent (or grandparent, mentor, elder) that their "
            "love was not just felt but transmitted - that the best parts "
            "of the speaker are their handiwork. For the older generation, "
            "there is no greater reassurance than evidence their love "
            "took root and grew."
        ),
        "how_it_works": (
            "Say it when they can still hear it - this statement has an "
            "expiry date, and everyone knows it. Milestone birthdays, "
            "holidays, or an ordinary visit that you decide to make "
            "extraordinary. Personalize it with the transmitted traits: "
            "\"I work the way you worked. I love the way you loved Mom. I "
            "show up because you always showed up.\" The fingerprints "
            "metaphor needs the specific prints: name three. If the "
            "relationship was imperfect, the statement still works "
            "honestly: \"You were not perfect, but the good in me is "
            "yours.\" That honesty makes it credible rather than "
            "sentimental. Say it in front of the grandchildren if you can; "
            "transmission witnessed becomes tradition."
        ),
        "key_points": [
            "Tells the elder their love was transmitted, not just felt: the best parts are their handiwork.",
            "The fingerprints metaphor needs specific prints: name three transmitted traits.",
            "This statement has an expiry date; say it while they can hear it.",
            "Honest imperfection (\"not perfect, but the good is yours\") beats hollow sentiment.",
            "Witnessed transmission becomes tradition; say it before the next generation when you can.",
        ],
        "requirements": [
            "Delivery while they can hear it; no postponement.",
            "Three specific transmitted traits named.",
            "The fingerprints framing: the good in me is your handiwork.",
            "Honest acknowledgment of imperfection where true.",
            "Next-generation witness when possible.",
        ],
        "standards": [
            "Urgency standard: expiry-dated; postponement is the only failure mode.",
            "Specificity standard: three named traits, never vague \"everything.\"",
            "Honesty standard: imperfection acknowledged beats sentimentality.",
        ],
        "citations": [CIT_GIBRAN, CIT_LEWIS],
        "sig_lens": (
            "Signature lens: the Signature way traces the transmission - "
            "work ethic, love style, showing up - each trait stamped with "
            "its origin. The record reads as provenance: this goodness has "
            "fingerprints, and they are yours."
        ),
    },
    # ---------------- Advanced: profound devotion ----------------
    {
        "key": "my_covenant",
        "name": "My Covenant",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "\"This is my covenant to you: I will love you in the bright "
            "days and the dark ones, in agreement and in argument, in "
            "health and in hardship. My love is not a mood. It is a "
            "promise.\" An advanced vow-statement. It enumerates the "
            "conditions under which love is often withdrawn - darkness, "
            "disagreement, hardship - and pre-commits to all of them. The "
            "closing thesis (\"not a mood, a promise\") is the whole "
            "philosophy of the advanced tier in one line."
        ),
        "how_it_works": (
            "Say it as a formal moment: an anniversary, a recommitment, or "
            "a deliberately chosen evening - this statement wants ceremony, "
            "even a small one. Speak it slowly; vows are ruined by hurry. "
            "Personalize it by adding your own condition-pairs from your "
            "actual life: \"in the city and the country, in plenty and in "
            "the lean months.\" The enumeration is the mechanism - each "
            "pair closes another escape route, which is exactly what makes "
            "it feel safe. Write it, sign it, keep it: a covenant gains "
            "weight from its physical form. Revisit it in the dark days "
            "it names; the statement is a lighthouse built for exactly "
            "those nights."
        ),
        "key_points": [
            "Pre-commits to the conditions under which love is usually withdrawn: darkness, disagreement, hardship.",
            "\"Not a mood, a promise\" is the philosophy of the advanced tier in one line.",
            "The enumeration of condition-pairs is the mechanism; each pair closes an escape route.",
            "Ceremony matters: slow speech, chosen moment, written and signed form.",
            "Revisit it in the dark days it names; it is a lighthouse built for those nights.",
        ],
        "requirements": [
            "A formal, chosen moment with a touch of ceremony.",
            "Slow, deliberate delivery; no hurry.",
            "Condition-pairs enumerated, including personalized ones from real life.",
            "Written, signed, and kept physical form.",
            "Revisit protocol: read it together in the dark days it names.",
        ],
        "standards": [
            "Ceremony standard: chosen moment, slow speech; hurry ruins vows.",
            "Enumeration standard: the pairs must include your real conditions.",
            "Form standard: written and signed; a covenant gains weight from its form.",
        ],
        "citations": [CIT_SHAKESPEARE, CIT_FROMM],
        "sig_lens": (
            "Signature lens: the Signature way issues love as a formal "
            "covenant - conditions enumerated, escape routes closed, "
            "signed and filed. Not a mood: a stamped, binding promise, "
            "built to hold in exactly the dark days it names."
        ),
    },
    {
        "key": "greatest_work",
        "name": "You Are My Greatest Work",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "\"Of everything I have ever built, you are my greatest work. "
            "Not because you are perfect, but because loving you made me "
            "better than I ever was.\" An advanced parent-to-child "
            "statement. It reframes the child not as an achievement but as "
            "the project that improved the builder. The \"not perfect\" "
            "clause is essential: it separates this from pressure, making "
            "clear the greatness is in what the loving did to the parent, "
            "not in what the child must be."
        ),
        "how_it_works": (
            "Say it at their milestones - graduations, weddings, the birth "
            "of their own child - when the arc of the work is visible. Or "
            "say it on an ordinary day, which makes it land harder because "
            "no milestone prompted it. Personalize it with what they taught "
            "you: \"You taught me patience I did not have. You taught me "
            "what actually matters.\" The teaching-reversal (child as "
            "teacher) is the heart of it. Never attach it to their "
            "achievements (\"my greatest work, the doctor\") - the moment "
            "it becomes about resume, it becomes pressure. It is about "
            "what loving them built in you."
        ),
        "key_points": [
            "Reframes the child as the project that improved the builder, not as an achievement.",
            "The \"not perfect\" clause separates it from pressure; greatness is in the loving, not the resume.",
            "Name what they taught you; the teaching-reversal is the heart of it.",
            "Milestone delivery shows the arc; ordinary-day delivery lands harder.",
            "Never attach to achievements; the moment it becomes resume, it becomes pressure.",
        ],
        "requirements": [
            "A parent-to-child direction (adapts to mentor/grandparent).",
            "The \"not because you are perfect\" clause intact.",
            "Named teachings: what loving them built in you.",
            "Milestone or deliberate ordinary-day timing.",
            "Zero attachment to the child's achievements or resume.",
        ],
        "standards": [
            "Direction standard: about what the loving built in the speaker, never the child's performance.",
            "Clause standard: \"not perfect\" must stand; it is the pressure-release valve.",
            "Teaching standard: the reversal (child as teacher) must be named.",
        ],
        "citations": [CIT_GIBRAN, CIT_FROMM],
        "sig_lens": (
            "Signature lens: the Signature way logs the child as the "
            "masterwork - not for perfection, but for what the building "
            "did to the builder. The record shows: patience acquired, "
            "priorities reclassified, the maker remade by the making."
        ),
    },
    {
        "key": "long_promise",
        "name": "The Long Promise",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "\"I do not know what the years will bring, but I know who I "
            "want beside me when they come. That is you. It will always be "
            "you.\" An advanced statement of future-certainty. It is honest "
            "about the unknown (\"I do not know what the years will "
            "bring\") and absolute about the who. That combination - "
            "humility about the future, certainty about the person - is "
            "what makes it believable rather than naive. It is the "
            "forward-looking companion to the anniversary vow's "
            "backward-looking renewal."
        ),
        "how_it_works": (
            "Say it when the future is being discussed or feared: a big "
            "move, a diagnosis, a career change, or simply a late-night "
            "conversation about what is next. The uncertainty in the air "
            "is what the statement answers. Personalize it with the "
            "specific unknowns: \"I do not know if the treatment works or "
            "where the job takes us, but I know who I want beside me.\" "
            "Do not promise outcomes (\"everything will be fine\") - "
            "promise companionship, which is the only promise you can "
            "keep. For young love, keep it proportional: the certainty "
            "about the person can be total even when the timeline is "
            "honestly short so far."
        ),
        "key_points": [
            "Honest about the unknown future, absolute about the who: humility plus certainty equals believable.",
            "Deliver when the future is being discussed or feared; the uncertainty is what it answers.",
            "Name the specific unknowns; the statement meets them one by one.",
            "Promise companionship, never outcomes; companionship is the keepable promise.",
            "Forward-looking companion to the anniversary vow's backward renewal.",
        ],
        "requirements": [
            "A future-facing moment: decision, fear, or late-night what-next talk.",
            "The honest unknown stated first.",
            "The absolute who stated second, without hedging.",
            "Specific unknowns named and met.",
            "Companionship promised; outcomes never promised.",
        ],
        "standards": [
            "Order standard: unknown first, who second; the sequence is the credibility.",
            "Keepability standard: only companionship is promised.",
            "Proportionality standard: certainty about the person can be total at any timeline.",
        ],
        "citations": [CIT_SHAKESPEARE, CIT_BROWNING],
        "sig_lens": (
            "Signature lens: the Signature way files the future as "
            "unknown-variables with one fixed constant: the who. Every "
            "scenario computed, every unknown admitted - and the record "
            "shows the same answer in all of them: you. Always you."
        ),
    },
    {
        "key": "love_remade_me",
        "name": "Love That Remakes",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "\"Loving you remade me. I was smaller before you - smaller in "
            "patience, smaller in courage, smaller in joy. You did not "
            "complete me; you expanded me.\" An advanced statement of "
            "transformative love. It deliberately rejects the \"you "
            "complete me\" frame (which implies prior brokenness) and "
            "replaces it with expansion (which implies prior wholeness, "
            "grown larger). This is the healthier and the truer story, and "
            "saying it teaches both people what love is actually for."
        ),
        "how_it_works": (
            "Say it in a reflective moment when the transformation is "
            "undeniable - looking at old photos, revisiting an old place, "
            "or after someone else remarks on how you have changed. The "
            "external evidence makes the claim land. Personalize it with "
            "the three expansions from your real life: patience, courage, "
            "joy - or yours: \"I was smaller in generosity, smaller in "
            "stillness.\" Keep the rejection of \"complete me\" explicit; "
            "it is a small philosophy lesson inside the love statement, "
            "and it protects the beloved from the burden of being someone's "
            "missing piece. End with gratitude, not debt: expansion is a "
            "gift, not an invoice."
        ),
        "key_points": [
            "Rejects \"you complete me\" (prior brokenness) for expansion (prior wholeness, grown larger).",
            "The healthier and truer story; saying it teaches what love is for.",
            "Name your three real expansions; the specificity is the proof.",
            "The philosophy lesson protects the beloved from being someone's missing piece.",
            "Ends in gratitude, never debt: expansion is a gift, not an invoice.",
        ],
        "requirements": [
            "A reflective moment with undeniable transformation evidence.",
            "Three named expansions from real life.",
            "The explicit rejection of the \"complete me\" frame.",
            "The expansion framing: wholeness grown larger.",
            "Gratitude close with zero debt attached.",
        ],
        "standards": [
            "Frame standard: expansion, never completion; wholeness assumed.",
            "Evidence standard: three real expansions named.",
            "Gift standard: gratitude, never invoice.",
        ],
        "citations": [CIT_FROMM, CIT_GIBRAN],
        "sig_lens": (
            "Signature lens: the Signature way documents the remake - "
            "before-state measured, after-state measured, the delta stamped "
            "as expansion. Not completion of something broken: the "
            "enlargement of something whole, logged trait by trait."
        ),
    },
    {
        "key": "until_the_end",
        "name": "Until The End",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "\"If I get a hundred years, I will spend every one of them "
            "loving you. And if I get one day, I will spend it the same "
            "way. The length never changed the depth.\" An advanced "
            "statement of duration-independent devotion. It removes time "
            "as a variable: the love does not scale with years granted, "
            "which means it cannot be diminished by years denied. This is "
            "the statement for the long marriage, the final chapters, and "
            "anyone who needs to hear that the depth was never about the "
            "count."
        ),
        "how_it_works": (
            "Say it when time is on the mind: big anniversaries, health "
            "scares, the quiet arithmetic of aging. The statement meets "
            "the fear (what if time is short) by removing time from the "
            "equation. Personalize it with your real numbers: \"Thirty "
            "years or thirty days - the way I love you does not have a "
            "volume knob.\" Speak it gently; this is a lullaby-grade "
            "statement, not a speech. It also serves beautifully as a "
            "written line - in a card, a letter, an anniversary book - "
            "where its clean symmetry can be reread. Never use it to "
            "minimize grief about lost time; it does not say the years do "
            "not matter, only that the depth never depended on them."
        ),
        "key_points": [
            "Removes time as a variable: depth never depended on duration.",
            "Meets the fear of short time by taking time out of the equation.",
            "Personalize with real numbers; the symmetry holds at any scale.",
            "Lullaby-grade delivery: gentle, not a speech.",
            "Does not minimize grief; it only relocates the depth off the timeline.",
        ],
        "requirements": [
            "A time-on-the-mind moment: anniversary, scare, or aging arithmetic.",
            "The hundred-years/one-day symmetry stated.",
            "Real numbers personalized when they exist.",
            "Gentle, lullaby-grade delivery.",
            "No minimizing of grief about lost time.",
        ],
        "standards": [
            "Variable standard: time removed from the devotion equation.",
            "Tone standard: gentle lullaby, never speech.",
            "Grief standard: the statement comforts; it never minimizes loss.",
        ],
        "citations": [CIT_SHAKESPEARE, CIT_BROWNING],
        "sig_lens": (
            "Signature lens: the Signature way factors time out of the "
            "devotion equation entirely - a hundred years or one day, the "
            "output is identical. Duration-independent, stamped at maximum "
            "depth regardless of the years granted."
        ),
    },
    {
        "key": "legacy_letter",
        "name": "The Legacy Letter",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "\"Long after I am gone, I want you to remember this: you were "
            "loved - completely, deliberately, out loud. Not in a way you "
            "had to guess at. In a way you could feel in your bones.\" An "
            "advanced legacy statement: love designed to outlast the "
            "lover. It is the capstone of the database because it contains "
            "the whole teaching in one line: love should be complete, "
            "deliberate, and out loud - never left for the beloved to "
            "guess at. Written, kept, and given at the right time, it "
            "becomes a family artifact."
        ),
        "how_it_works": (
            "Write it as a letter, by hand if you can - handwriting carries "
            "the body into the words. This is the one statement in the "
            "database where writing is not optional but essential: it is "
            "designed to be found, kept, and reread. Personalize it with "
            "your whole history: the first meeting, the hard years, the "
            "ordinary Tuesdays that were the real treasure. The \"feel it "
            "in your bones\" line is the standard: audit your life with "
            "this person and ask whether the love was bone-deep obvious; "
            "the letter is both the proof and the final delivery. Give it "
            "at a meaningful time - a milestone birthday, after the birth "
            "of a grandchild - not as a farewell but as a deposit. Keep a "
            "copy; legacies deserve backups."
        ),
        "key_points": [
            "Love designed to outlast the lover: the capstone of the whole database.",
            "Contains the entire teaching: complete, deliberate, out loud - never left to guess.",
            "Writing is essential here, not optional; handwriting carries the body into the words.",
            "The \"feel it in your bones\" line is the audit standard for a life of loving.",
            "Given as a deposit at a meaningful time, not as a farewell; keep a copy.",
        ],
        "requirements": [
            "Written letter form, handwritten when possible.",
            "The whole history personalized: first meeting, hard years, ordinary Tuesdays.",
            "The complete-deliberate-out-loud thesis stated.",
            "The bone-deep audit: was the love obvious in the living of it.",
            "Meaningful-time delivery as a deposit; a kept copy as backup.",
        ],
        "standards": [
            "Form standard: written, preferably handwritten; this one must survive rereading.",
            "Thesis standard: complete, deliberate, out loud - all three, explicit.",
            "Timing standard: deposit at meaning, never only farewell.",
        ],
        "citations": [CIT_BROWNING, CIT_GIBRAN],
        "sig_lens": (
            "Signature lens: the Signature way writes the legacy letter as "
            "the final stamped record - the whole history filed, the "
            "thesis declared, the love made bone-deep obvious and "
            "archived to outlast the author. The last entry in the ledger, "
            "and the one that matters most."
        ),
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks), "entries not in ladder order"
assert len({e["key"] for e in ENTRIES}) == 34, "duplicate keys"
