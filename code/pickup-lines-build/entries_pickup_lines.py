#!/usr/bin/env python3
"""Entries for the Pickup Lines databases (Manon 16:15 orders, fun/social batch).

The Pickup Lines Database (pickup-lines) and The Pickup Lines Signature
Database (pickup-lines-signature): clean, clever, wholesome pickup lines -
bookish, science-themed, kind, funny - each record a pickup line WITH
context notes (when it works, why it works, delivery tips). WHOLESOME AND
RESPECTFUL ONLY: clever and kind, never crude, never objectifying, nothing
profane, no religious talk. Every line screened against the
wholesome-respect canon (2026-10-17).

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced): simple clean kind openers ->
bookish and science lines with wordplay -> clever multi-line constructions.
The shard index is written in ladder order so pages present simple ->
compounded -> complex.

ID prefixes: JAH-PKUP- (public) and JAH-PKUPS- (signature), verified free
in the manifest id_prefix values and in every shard index file
(zero hits, 2026-10-17).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_pickup_lines.py). Every demo prints its real computed values
(word counts, delivery-time estimates, line-of-the-day hash picks, context
matcher scores), asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Kindness Method: "
            "every line a covenant of respect, spoken once and honestly, the "
            "speaker bringing the best of himself and leaving the other "
            "person brighter than he found them. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_SCREEN = ("Screened against the JAH Databases wholesome-respect canon "
              "(2026-10-17): clean, kind, respectful, non-objectifying; "
              "nothing crude, nothing profane, no religious talk.")
CIT_TRAD = ("Traditional pickup-line genre; wording screened and original "
            "to this archive.")
CIT_ORIG = ("Archive original, composed for this database and screened "
            "against the wholesome-respect canon (2026-10-17).")

STD_WHOLESOME = ("Wholesome-respect canon (2026-10-17): the line is clean, "
                 "kind, and respectful - never crude, never objectifying, "
                 "nothing profane.")
STD_CONSENT = ("Consent standard: delivered once, warmly; if the other "
               "person is not interested, the line ends with a smile and a "
               "genuine wish for a good day - never repeated, never "
               "pressured.")
STD_HONEST = ("Honesty standard: every compliment in the line must be true; "
              "never flatter what is not meant, never perform interest that "
              "is not real.")

ENTRIES = [
    {
        "key": "simple_hello",
        "name": "The Warm Hello",
        "line": "Hi. I could not walk past without saying hello. I am ___, and you looked like someone worth knowing.",
        "tags": ["kind", "simple", "anywhere", "daytime"],
        "group": "Kind Openers",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The line: \"Hi. I could not walk past without saying hello. I am ___, "
            "and you looked like someone worth knowing.\" Context notes: this is "
            "the simplest opener in the archive and the one every ladder starts "
            "with. It works in daylight public places - bookstores, coffee shops, "
            "parks, museum lines, volunteer events - anywhere a stranger may "
            "reasonably be spoken to. It works best when the other person is "
            "unhurried and unaccompanied by headphones, and when you mean every "
            "word of it. Fill the blank with your real first name; the honesty "
            "of the introduction is the whole mechanism."
        ),
        "how_it_works": (
            "Why it works: it is honest about its own motive, names no "
            "appearance, promises nothing, and asks for nothing - it only "
            "offers a beginning. The phrase \"worth knowing\" compliments "
            "character rather than looks, which keeps it respectful. Delivery "
            "tips: smile first, then speak; keep your body angled slightly "
            "away so the other person never feels cornered; say your name "
            "clearly and then stop - let them answer. If they smile back, "
            "ask one easy question about the place you are in. If they do "
            "not, wish them a good day and mean it."
        ),
        "key_points": [
            "The line: \"Hi. I could not walk past without saying hello. I am ___, and you looked like someone worth knowing.\"",
            "When it works: daylight public settings, unhurried stranger, genuine intent.",
            "Why it works: honest motive, compliments character not looks, asks nothing.",
            "Delivery tip: smile first, angle slightly away, say your name, then stop and listen.",
        ],
        "requirements": [
            "Mean it: only approach someone you genuinely would like to know.",
            "Daylight public setting where conversation is socially normal.",
            "One delivery only; accept any answer gracefully.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Warm Hello as the first covenant of the "
            "Signature Kindness Method - the speaker brings his real name "
            "and his real intent, offers a beginning, and claims nothing. "
            "Spoken once, honestly, with the Signature mark: leave the "
            "other person brighter than you found them, whatever they "
            "answer."
        ),
    },
    {
        "key": "genuine_compliment",
        "name": "The Genuine Compliment",
        "line": "I hope this is okay to say - you have a wonderful laugh. It just made my whole coffee break better.",
        "tags": ["kind", "compliment", "cafe", "genuine"],
        "group": "Kind Openers",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The line: \"I hope this is okay to say - you have a wonderful "
            "laugh. It just made my whole coffee break better.\" Context "
            "notes: this opener compliments something a person chose to do "
            "rather than how they look - their laugh, their kindness to a "
            "cashier, the book they are reading, the song they are humming. "
            "It works in cafes, waiting rooms, bookstores, and anywhere you "
            "have genuinely observed something admirable. It must be true; "
            "a manufactured compliment is felt instantly and poisons the "
            "whole exchange."
        ),
        "how_it_works": (
            "Why it works: the opening phrase \"I hope this is okay to say\" "
            "asks permission before the compliment lands, which makes the "
            "whole line feel safe. Complimenting a chosen action rather than "
            "appearance keeps it respectful and non-objectifying. Delivery "
            "tips: keep it brief - say the line, smile, and let them respond; "
            "do not stack a second compliment on top of the first. Speak at "
            "normal volume, not stage volume. If they thank you, you may ask "
            "one light question; if they turn away, the compliment still "
            "did its work."
        ),
        "key_points": [
            "The line: \"I hope this is okay to say - you have a wonderful laugh. It just made my whole coffee break better.\"",
            "When it works: anywhere you have genuinely observed something admirable.",
            "Why it works: asks permission first, compliments chosen action rather than appearance.",
            "Delivery tip: one compliment only, normal volume, let them respond.",
        ],
        "requirements": [
            "The compliment must be true and specific to something observed.",
            "Compliment actions and choices, never the body.",
            "Accept thanks or silence with equal grace.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Genuine Compliment as Signature noticing - "
            "the speaker trains his attention on what people do well and "
            "names it aloud. Signature-made kindness is specific, true, and "
            "given without invoice; the compliment is complete the moment it "
            "is spoken, whether or not a conversation follows."
        ),
    },
    {
        "key": "shared_moment",
        "name": "The Shared Moment Opener",
        "line": "Did you see that sunset? I needed at least one other person to agree it was spectacular.",
        "tags": ["kind", "moment", "outdoors", "shared"],
        "group": "Kind Openers",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The line: \"Did you see that sunset? I needed at least one other "
            "person to agree it was spectacular.\" Context notes: this opener "
            "borrows its occasion from the world - a sunset, street music, a "
            "dog doing something funny, a great band at a festival. It works "
            "outdoors and at events where strangers naturally share an "
            "experience. It works best when the moment is genuinely striking, "
            "because shared wonder is the easiest bridge between two "
            "strangers. Adapt the first sentence to whatever is actually "
            "happening; the second sentence is the engine."
        ),
        "how_it_works": (
            "Why it works: it recruits the other person as a co-witness "
            "rather than a target - you are both on the same side, looking "
            "at the same wonder. \"I needed\" is honest and a little "
            "vulnerable, which reads as warm rather than slick. Delivery "
            "tips: gesture toward the thing you are talking about; keep the "
            "tone delighted rather than rehearsed; after they agree, ask "
            "what brought them here today. Never manufacture a moment - "
            "pointing at an ordinary Tuesday and calling it spectacular "
            "breaks the spell."
        ),
        "key_points": [
            "The line: \"Did you see that sunset? I needed at least one other person to agree it was spectacular.\"",
            "When it works: outdoors or at events, around a genuinely striking shared moment.",
            "Why it works: recruits the other person as co-witness; honest vulnerability reads warm.",
            "Delivery tip: gesture at the moment, sound delighted, adapt the first sentence to reality.",
        ],
        "requirements": [
            "A real shared moment must actually be happening.",
            "Adapt the opener to the true occasion; never manufacture one.",
            "Follow with a question about them, not about you.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Shared Moment as Signature witnessing - two "
            "strangers made momentary kin by the same wonder. The Signature "
            "speaker points at the world, not at himself; the line succeeds "
            "when both people leave happier about the sunset, whatever else "
            "happens."
        ),
    },
    {
        "key": "helpful_question",
        "name": "The Helpful Question",
        "line": "You look like you know this place - what is the one thing here I absolutely should not miss?",
        "tags": ["kind", "question", "travel", "cafe"],
        "group": "Kind Openers",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The line: \"You look like you know this place - what is the one "
            "thing here I absolutely should not miss?\" Context notes: this "
            "is the traveler's opener and the newcomer's friend. It works in "
            "cafes, museums, bookstores, markets, campuses, and new cities - "
            "anywhere local knowledge is flattering to share. It works best "
            "when you are genuinely new to the place, because the question "
            "is real and the answer helps you. It positions the other person "
            "as the expert, which most people enjoy."
        ),
        "how_it_works": (
            "Why it works: asking for guidance reverses the usual pressure "
            "of an opener - instead of performing for them, you invite them "
            "to shine. \"The one thing\" forces a real opinion rather than a "
            "polite shrug, and opinions start conversations. Delivery tips: "
            "ask it like you mean it, because you do; listen to the whole "
            "answer before responding; thank them specifically for the "
            "recommendation. If the conversation flows, introduce yourself "
            "by name before it ends."
        ),
        "key_points": [
            "The line: \"You look like you know this place - what is the one thing here I absolutely should not miss?\"",
            "When it works: cafes, museums, markets, campuses - anywhere local knowledge flatters.",
            "Why it works: makes the other person the expert; real opinions start real conversations.",
            "Delivery tip: ask like you mean it, listen fully, thank them specifically.",
        ],
        "requirements": [
            "Be genuinely new to the place or genuinely curious.",
            "Listen to the full answer; do not interrupt with your own story.",
            "Introduce yourself by name if the conversation continues.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Helpful Question as Signature humility - the "
            "speaker arrives as the student and crowns the stranger the "
            "teacher. In the Signature method, the person who asks the honest "
            "question is never the lesser party; curiosity is the highest "
            "compliment one mind can pay another."
        ),
    },
    {
        "key": "honest_intro",
        "name": "The Honest Introduction",
        "line": "I will be honest - I came over because talking to strangers is how I meet my favorite people. I am ___.",
        "tags": ["kind", "honest", "anywhere", "direct"],
        "group": "Kind Openers",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The line: \"I will be honest - I came over because talking to "
            "strangers is how I meet my favorite people. I am ___.\" Context "
            "notes: this is the direct line for people who dislike games. It "
            "works at social gatherings, community events, classes, and "
            "hobby meetups - places where meeting people is the point. It "
            "works best delivered with a relaxed smile and zero hurry, "
            "because the line's power is its transparency. Fill the blank "
            "with your real name; the line is a promise that what follows "
            "will also be honest."
        ),
        "how_it_works": (
            "Why it works: it disarms the stranger's main worry - \"what "
            "does this person want?\" - by answering it before it is asked. "
            "\"My favorite people\" is a warm, confident frame that flatters "
            "without overpromising. Delivery tips: say \"I will be honest\" "
            "like a confession, not a sales pitch; pause after your name so "
            "they can offer theirs; then ask what brought them here. Never "
            "use this line as a prelude to a pitch, a joke at their "
            "expense, or anything but genuine conversation."
        ),
        "key_points": [
            "The line: \"I will be honest - I came over because talking to strangers is how I meet my favorite people. I am ___.\"",
            "When it works: social gatherings, classes, hobby meetups - where meeting people is the point.",
            "Why it works: answers \"what do you want?\" before it is asked; transparent and warm.",
            "Delivery tip: confession tone not sales tone; pause after your name; ask what brought them.",
        ],
        "requirements": [
            "Use only where conversation with strangers is socially normal.",
            "Follow the introduction with genuine conversation, never a pitch.",
            "Real name, real intent - the line is a promise.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Honest Introduction as the Signature oath - "
            "the speaker states his motive plainly and binds himself to it. "
            "No maneuver, no mask; the Signature mark is that the words and "
            "the intent are the same thing, and the other person can feel "
            "it."
        ),
    },
    {
        "key": "bright_smile",
        "name": "The Bright Smile Opener",
        "line": "Hi. [smile] I am ___. That is the whole line - the smile was doing most of the work.",
        "tags": ["kind", "simple", "smile", "anywhere"],
        "group": "Kind Openers",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The line: \"Hi. [smile] I am ___. That is the whole line - the "
            "smile was doing most of the work.\" Context notes: the shortest "
            "complete opener in the archive, and proof that brevity is a "
            "virtue. It works anywhere a greeting is welcome - passing on a "
            "trail, in a class, at a community event. It works best when the "
            "smile is real, because the meta-joke only lands if the warmth "
            "is genuine. This is the line for people who freeze up trying "
            "to be clever: you do not need clever, you need kind."
        ),
        "how_it_works": (
            "Why it works: it admits its own simplicity, and that honesty "
            "is charming. The smile carries the emotional content; the words "
            "just give the other person something to respond to. Delivery "
            "tips: the smile must reach your eyes - think of something you "
            "genuinely like about the day; keep your hands visible and "
            "relaxed; after your name, add one observation about the shared "
            "setting so the conversation has somewhere to go."
        ),
        "key_points": [
            "The line: \"Hi. [smile] I am ___. That is the whole line - the smile was doing most of the work.\"",
            "When it works: anywhere a greeting is welcome; best for the cleverness-shy.",
            "Why it works: admits its simplicity; the real smile carries the emotion.",
            "Delivery tip: smile with your eyes, hands relaxed, follow with one setting observation.",
        ],
        "requirements": [
            "A genuine smile - the line fails on a forced one.",
            "A setting where a greeting is socially welcome.",
            "One follow-up observation ready so the moment continues.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Bright Smile as the smallest Signature "
            "covenant - the least words carrying the most warmth. The "
            "Signature method teaches that kindness needs no ornament; a "
            "true smile, honestly given, is a complete work."
        ),
    },
    {
        "key": "kind_observation",
        "name": "The Kind Observation",
        "line": "I saw you help that kid pick up his dropped books. That was genuinely lovely to watch.",
        "tags": ["kind", "observation", "character", "anywhere"],
        "group": "Kind Openers",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The line: \"I saw you help that kid pick up his dropped books. "
            "That was genuinely lovely to watch.\" Context notes: this "
            "opener is earned - you can only use it after witnessing real "
            "kindness. It works anywhere: streets, campuses, stores, parks. "
            "It works best when the observation is fresh, within the last "
            "few minutes, so it reads as moved rather than rehearsed. Adapt "
            "the first sentence to what you actually saw: helping an elder "
            "with a door, returning a dropped wallet, calming a crying "
            "child."
        ),
        "how_it_works": (
            "Why it works: it tells the other person that their goodness "
            "was seen, which is one of the rarest compliments in the world. "
            "It also reveals your own values - you notice kindness - which "
            "is attractive in the truest sense. Delivery tips: speak "
            "quietly and sincerely, as if sharing something precious; do not "
            "embellish what you saw; after they respond, introduce yourself. "
            "Never invent an observation - a false witness is worse than "
            "silence."
        ),
        "key_points": [
            "The line: \"I saw you help that kid pick up his dropped books. That was genuinely lovely to watch.\"",
            "When it works: within minutes of witnessing real kindness, anywhere.",
            "Why it works: being seen in goodness is rare; it reveals your values too.",
            "Delivery tip: quiet sincerity, no embellishment, adapt to what you truly saw.",
        ],
        "requirements": [
            "You must have actually witnessed the kind act.",
            "Describe it plainly; never embellish or invent.",
            "Quiet, sincere tone - this is not a performance.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Kind Observation as Signature testimony - "
            "the speaker bears witness to goodness and says so aloud. In "
            "the Signature method, naming another person's kindness is "
            "itself a kind act, and the record of it outlasts the moment."
        ),
    },
    {
        "key": "coffee_line",
        "name": "The Coffee Invitation",
        "line": "Can I buy you a coffee? No strings, no pitch - just good conversation with an interesting stranger.",
        "tags": ["kind", "coffee", "invitation", "cafe"],
        "group": "Kind Openers",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The line: \"Can I buy you a coffee? No strings, no pitch - just "
            "good conversation with an interesting stranger.\" Context "
            "notes: the classic invitation, cleaned to its kindest form. It "
            "works in and around coffee shops, bookstores with cafes, and "
            "campus quads - anywhere coffee is a small, low-pressure gift. "
            "It works best mid-morning or mid-afternoon, when a coffee is a "
            "pleasure rather than a commitment. The explicit \"no strings\" "
            "is load-bearing: it must be true, and your manner afterward "
            "must prove it."
        ),
        "how_it_works": (
            "Why it works: it names the fear (strings, pitch) and removes it "
            "before asking, which makes the small yes easy. A coffee is the "
            "perfect stake - real enough to be kind, small enough to refuse. "
            "Delivery tips: ask it lightly, as if the answer barely matters "
            "to you; if yes, let them choose the drink and the table; if no, "
            "smile and say \"enjoy your day\" and go. Never hover after a "
            "no, and never treat the coffee as currency owed."
        ),
        "key_points": [
            "The line: \"Can I buy you a coffee? No strings, no pitch - just good conversation with an interesting stranger.\"",
            "When it works: in and around coffee shops, mid-morning or mid-afternoon.",
            "Why it works: names and removes the fear; the stake is small enough to refuse.",
            "Delivery tip: ask lightly, let them choose, accept no with a smile and go.",
        ],
        "requirements": [
            "\"No strings\" must be true in word and manner afterward.",
            "They choose the drink, the table, and the length of stay.",
            "A no ends it instantly, warmly, with no hovering.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Coffee Invitation as Signature hospitality - "
            "a small gift freely given, with the giver's hands open. The "
            "Signature mark is in the \"no strings\": the coffee is complete "
            "as kindness the moment it is offered, whatever the answer."
        ),
    },
    {
        "key": "bookstore_hello",
        "name": "The Bookstore Hello",
        "line": "Anyone reading that book in public is someone I want to know. What is it about?",
        "tags": ["kind", "bookish", "bookstore", "readers"],
        "group": "Kind Openers",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The line: \"Anyone reading that book in public is someone I "
            "want to know. What is it about?\" Context notes: the reader's "
            "opener - it works in bookstores, libraries, cafes, parks, and "
            "on transit wherever someone is visibly reading. It works best "
            "when you have a genuine curiosity about books, because readers "
            "can tell. The question \"what is it about\" is deliberate: it "
            "asks for their take, not a plot summary, and takes invite "
            "passion."
        ),
        "how_it_works": (
            "Why it works: it compliments taste and curiosity - qualities of "
            "mind - and then hands the floor to the other person. Readers "
            "love talking about books; you have given them their favorite "
            "subject. Delivery tips: note the actual book before speaking "
            "so the line is specific; keep your voice low in quiet spaces; "
            "if you have read it, say so after they answer, not before. "
            "Never interrupt deep reading - a furrowed brow means come back "
            "never."
        ),
        "key_points": [
            "The line: \"Anyone reading that book in public is someone I want to know. What is it about?\"",
            "When it works: bookstores, libraries, cafes, transit - wherever readers read.",
            "Why it works: compliments mind and taste; hands them their favorite subject.",
            "Delivery tip: note the real book, keep voice low, never interrupt deep reading.",
        ],
        "requirements": [
            "Genuine curiosity about books; readers detect pretense.",
            "Note the actual title before speaking.",
            "Never interrupt someone deep in reading.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Bookstore Hello as Signature fellowship of "
            "readers - two minds meeting at the shelf. The Signature "
            "speaker honors the book first and the person through it; the "
            "conversation that follows is a shared margin note."
        ),
    },
    {
        "key": "music_note",
        "name": "The Music Note Opener",
        "line": "You have been humming that song for ten minutes and now it is stuck in my head too - in a good way.",
        "tags": ["kind", "music", "playful", "anywhere"],
        "group": "Kind Openers",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The line: \"You have been humming that song for ten minutes and "
            "now it is stuck in my head too - in a good way.\" Context "
            "notes: the playful observer's opener. It works wherever people "
            "hum, tap, or sing along - waiting lines, parks, campuses, "
            "transit platforms. It works best when the humming is cheerful "
            "and the setting is relaxed, because the line borrows the "
            "music's lightness. The closing \"in a good way\" is essential - "
            "it converts a potential complaint into a compliment."
        ),
        "how_it_works": (
            "Why it works: it proves you were paying attention to something "
            "small and delightful, and it frames the other person as a "
            "source of joy rather than noise. Playfulness without edge is "
            "disarming. Delivery tips: grin when you say it; if you know "
            "the song, name it - shared taste is instant rapport; keep the "
            "tone teasing-warm, never mocking. If they seem embarrassed, "
            "reassure quickly: \"No, really, it made the wait better.\""
        ),
        "key_points": [
            "The line: \"You have been humming that song for ten minutes and now it is stuck in my head too - in a good way.\"",
            "When it works: relaxed settings where someone is cheerfully humming or tapping along.",
            "Why it works: proves delighted attention; \"in a good way\" converts complaint to compliment.",
            "Delivery tip: grin, name the song if you know it, teasing-warm never mocking.",
        ],
        "requirements": [
            "The humming must be real and cheerful; never mock.",
            "Keep it light; reassure quickly if they seem embarrassed.",
            "\"In a good way\" is load-bearing - never drop it.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Music Note as Signature listening - the "
            "speaker's attention tuned to small joys. In the Signature "
            "method, noticing what makes a stranger happy and saying so is "
            "a complete act of fellowship, whatever song follows."
        ),
    },
    {
        "key": "library_book",
        "name": "The Library Book Line",
        "line": "Are you a library book? Because I keep checking you out.",
        "tags": ["bookish", "classic", "library", "wordplay"],
        "group": "Bookish Lines",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"Are you a library book? Because I keep checking you "
            "out.\" Context notes: the most famous bookish pickup line in "
            "the genre, kept here in its cleanest form. It works in "
            "libraries, bookstores, and among readers anywhere - the joke "
            "lands only where \"checking out\" is library vocabulary. It "
            "works best delivered with a knowing grin that says you know it "
            "is a classic; the charm is in the shared recognition, not the "
            "surprise. Use it where books are the common ground."
        ),
        "how_it_works": (
            "Why it works: the pun turns a library chore into a compliment, "
            "and classics carry social proof - the other person has likely "
            "heard it, which makes it a shared joke rather than a cold "
            "approach. Delivery tips: deliver it lightly and fast, like "
            "tossing a paper airplane; the grin sells it, not the words. "
            "Follow immediately with something real - \"Okay, real question: "
            "what are you reading?\" - so the pun is the door, not the "
            "house. Never use it twice on the same person."
        ),
        "key_points": [
            "The line: \"Are you a library book? Because I keep checking you out.\"",
            "When it works: libraries, bookstores, among readers - where the pun is shared vocabulary.",
            "Why it works: classic with social proof; the pun is the door, not the house.",
            "Delivery tip: light and fast with a grin; follow immediately with a real question.",
        ],
        "requirements": [
            "Use only where books are the common ground.",
            "Deliver with a grin that admits it is a classic.",
            "Follow with a genuine question; never let the pun stand alone.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_TRAD, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Library Book as Signature wordplay - the "
            "old joke polished and returned to the shelf it came from. The "
            "Signature speaker uses the classic to open, then proves "
            "himself with a real question; the pun is the handshake, the "
            "conversation is the covenant."
        ),
    },
    {
        "key": "gatsby_line",
        "name": "The Great Gatsby Line",
        "line": "In my younger and more vulnerable years, my father gave me some advice - go talk to interesting strangers. So here I am.",
        "tags": ["bookish", "classic", "literary", "party"],
        "group": "Bookish Lines",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"In my younger and more vulnerable years, my father "
            "gave me some advice - go talk to interesting strangers. So here "
            "I am.\" Context notes: a playful twist on the most famous "
            "opening line in American literature, from F. Scott "
            "Fitzgerald's The Great Gatsby (1925). It works at parties, "
            "book clubs, literary events, and anywhere the reference will "
            "be caught. It works best on readers, who will hear the echo "
            "and smile before the line even finishes."
        ),
        "how_it_works": (
            "Why it works: borrowing Gatsby's cadence gives the line "
            "instant style, and the subverted ending - \"go talk to "
            "interesting strangers\" - is funny precisely because it is not "
            "what Fitzgerald wrote. It flatters the listener twice: once by "
            "calling them interesting, once by trusting them to catch the "
            "reference. Delivery tips: use a storyteller's rhythm, slow on "
            "\"younger and more vulnerable years\"; land the punchline with "
            "a shrug and a smile. If they catch the reference, you have "
            "instant rapport; if not, the line still works as a charming "
            "confession."
        ),
        "key_points": [
            "The line: \"In my younger and more vulnerable years, my father gave me some advice - go talk to interesting strangers. So here I am.\"",
            "When it works: parties, book clubs, literary events - where the Gatsby echo is caught.",
            "Why it works: borrowed cadence gives style; the subverted ending flatters twice.",
            "Delivery tip: storyteller rhythm, shrug and smile on the punchline.",
        ],
        "requirements": [
            "Works best where the literary reference will land.",
            "Deliver with storyteller rhythm, not rushed.",
            "Mean the compliment: they must actually seem interesting.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_TRAD, CIT_SCREEN,
                      "Fitzgerald FS. The Great Gatsby. Scribner; 1925. Opening line echoed and subverted."],
        "sig_lens": (
            "Signature lens: the Gatsby Line as Signature borrowing - the "
            "speaker tips his hat to the canon and makes it his own. "
            "Signature-made lines may stand on the shoulders of the great "
            "books, but they always walk forward in the speaker's own "
            "shoes."
        ),
    },
    {
        "key": "plot_twist",
        "name": "The Plot Twist",
        "line": "Every good story needs a plot twist. I have a feeling you might be mine.",
        "tags": ["bookish", "story", "romantic", "evening"],
        "group": "Bookish Lines",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"Every good story needs a plot twist. I have a "
            "feeling you might be mine.\" Context notes: the storyteller's "
            "romantic line. It works in the evening - at readings, wine "
            "bars, theaters, gallery nights - where a little drama is "
            "welcome. It works best when there is already a flicker of "
            "mutual interest, because \"plot twist\" implies the story was "
            "already underway. It is bolder than the foundation lines; save "
            "it for when the conversation has already begun."
        ),
        "how_it_works": (
            "Why it works: it casts the meeting as a story, which is "
            "flattering and cinematic, and \"I have a feeling\" keeps it "
            "hopeful rather than presumptuous. Delivery tips: lower your "
            "voice slightly and hold eye contact on \"mine\"; smile right "
            "after so the drama does not curdle into intensity. Then ask "
            "them about their own story - the line opens a book, it does "
            "not close one. Never use it cold on a stranger with no prior "
            "exchange."
        ),
        "key_points": [
            "The line: \"Every good story needs a plot twist. I have a feeling you might be mine.\"",
            "When it works: evening settings with a flicker of mutual interest already present.",
            "Why it works: casts the meeting as a story; \"I have a feeling\" keeps it hopeful.",
            "Delivery tip: softer voice, eye contact on \"mine\", smile after, then ask their story.",
        ],
        "requirements": [
            "Use only after some mutual exchange, never cold.",
            "Keep it hopeful, never presumptuous.",
            "Follow by asking about their story.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Plot Twist as Signature narrative - the "
            "speaker invites the other person to co-author what comes next. "
            "No one is written into a Signature story without consent; the "
            "twist is offered, never imposed."
        ),
    },
    {
        "key": "well_read",
        "name": "The Well-Read Heart",
        "line": "You must read a lot - your eyes have that well-traveled look.",
        "tags": ["bookish", "compliment", "mind", "cafe"],
        "group": "Bookish Lines",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"You must read a lot - your eyes have that "
            "well-traveled look.\" Context notes: a compliment of the mind "
            "disguised as a compliment of the eyes. It works in bookstores, "
            "libraries, cafes, and anywhere thoughtful people gather. It "
            "works best when it might actually be true - on someone with a "
            "book in hand or a faraway thoughtful gaze - because the line "
            "is a guess that flatters by being generous. It says: I see "
            "depth in you."
        ),
        "how_it_works": (
            "Why it works: \"well-traveled\" is a beautiful phrase for a "
            "reader, and attributing depth to someone is among the finest "
            "compliments. The hedge \"you must\" makes it a playful guess "
            "rather than a claim. Delivery tips: say it warmly and simply, "
            "without over-explaining; if they laugh and say \"I do read a "
            "lot,\" ask what is on their shelf right now; if they say \"not "
            "really,\" grin and say \"well, you look like you should\" - "
            "but only if the moment is light."
        ),
        "key_points": [
            "The line: \"You must read a lot - your eyes have that well-traveled look.\"",
            "When it works: bookstores, libraries, cafes - where thoughtfulness shows.",
            "Why it works: compliments depth of mind; the hedge keeps it a playful guess.",
            "Delivery tip: warm and simple; ask what is on their shelf if they agree.",
        ],
        "requirements": [
            "Best when the guess might be true; never deploy randomly.",
            "Compliment mind and character, never the body.",
            "Have a graceful reply ready for \"not really.\"",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Well-Read Heart as Signature recognition - "
            "the speaker honors the inner life he senses in another. "
            "Signature kindness looks past the surface for the traveler "
            "within, and says what it finds aloud."
        ),
    },
    {
        "key": "dogeared_page",
        "name": "The Dog-Eared Page",
        "line": "You are the page I keep coming back to.",
        "tags": ["bookish", "sweet", "short", "evening"],
        "group": "Bookish Lines",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"You are the page I keep coming back to.\" Context "
            "notes: the shortest bookish line in the archive - eight words. "
            "It works after you have already spoken for a while: at the end "
            "of a good conversation, when parting at a book club, or when "
            "saying goodnight after a first meeting. It works best as a "
            "parting line, because \"coming back to\" promises a return. "
            "Never use it as an opener; it needs the weight of an evening "
            "behind it."
        ),
        "how_it_works": (
            "Why it works: brevity is power - eight words, one image, and "
            "the image says \"you are worth re-reading.\" As a parting "
            "line it leaves the other person with the best possible last "
            "impression. Delivery tips: say it quietly, at the moment of "
            "parting, with a genuine smile; then actually come back - ask "
            "for a way to continue the conversation, or name the next "
            "meeting. The line is a promise; keep it."
        ),
        "key_points": [
            "The line: \"You are the page I keep coming back to.\"",
            "When it works: as a parting line after a good conversation, never as an opener.",
            "Why it works: eight words, one image - \"worth re-reading\" - promising return.",
            "Delivery tip: quiet at parting, genuine smile, then actually arrange the return.",
        ],
        "requirements": [
            "Use only after a real conversation, never cold.",
            "Mean the promise: arrange a real next meeting.",
            "Quiet delivery; this is not a stage line.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Dog-Eared Page as Signature promise - "
            "eight words that bind the speaker to return. In the Signature "
            "method a parting line is a covenant: the page is marked, and "
            "the reader comes back."
        ),
    },
    {
        "key": "unfinished_chapter",
        "name": "The Unfinished Chapter",
        "line": "I feel like our story is an unfinished chapter. Want to help me write the next page?",
        "tags": ["bookish", "story", "invitation", "evening"],
        "group": "Bookish Lines",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"I feel like our story is an unfinished chapter. "
            "Want to help me write the next page?\" Context notes: the "
            "bookish invitation - it turns \"can I see you again\" into "
            "shared authorship. It works at the end of a first meeting that "
            "went well: a book club, a reading, a long cafe conversation. "
            "It works best when the evening genuinely felt too short, "
            "because the line names a feeling both people already have. "
            "\"Help me\" makes it collaborative rather than demanding."
        ),
        "how_it_works": (
            "Why it works: it frames a second meeting as co-creation, which "
            "is more exciting than a mere repeat, and \"unfinished chapter\" "
            "flatters the evening you just shared. Delivery tips: say it "
            "with hope, not need; propose something concrete for the next "
            "page - \"there is a reading Thursday, want to go?\" - so the "
            "metaphor lands on a real plan. If they hesitate, smile and "
            "say \"the chapter keeps either way\" and leave warmly."
        ),
        "key_points": [
            "The line: \"I feel like our story is an unfinished chapter. Want to help me write the next page?\"",
            "When it works: end of a first meeting that genuinely felt too short.",
            "Why it works: frames a second meeting as co-creation; \"help me\" is collaborative.",
            "Delivery tip: hopeful not needy; land the metaphor on a concrete plan.",
        ],
        "requirements": [
            "Use only after a meeting that went well.",
            "Propose a concrete next page, not a vague someday.",
            "Accept hesitation warmly; never press.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Unfinished Chapter as Signature "
            "co-authorship - the speaker offers the pen, not just the page. "
            "A Signature story is never written alone; the invitation is "
            "the first sentence they write together."
        ),
    },
    {
        "key": "cute_science",
        "name": "The Copper Tellurium Line",
        "line": "Are you made of copper and tellurium? Because you are Cu-Te.",
        "tags": ["science", "chemistry", "classic", "wordplay"],
        "group": "Science Lines",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"Are you made of copper and tellurium? Because you "
            "are Cu-Te.\" Context notes: the most famous science pickup "
            "line in the genre - Cu (copper) + Te (tellurium) spells "
            "\"cutie.\" It works in labs, science museums, university "
            "campuses, and anywhere the periodic table is common knowledge. "
            "It works best delivered with a scientist's grin, because the "
            "joke is a shared password among science people. Like the "
            "library-book line, its power is recognition, not surprise."
        ),
        "how_it_works": (
            "Why it works: the pun rewards the listener's knowledge - "
            "getting the joke feels good, and feeling smart next to someone "
            "is attractive. It is sweet rather than smooth, which reads as "
            "safe. Delivery tips: say \"Cu-Te\" as \"cutie,\" then spell it "
            "with your fingers in the air if they look puzzled; laugh at "
            "yourself a little - the line is nerdy and proud of it. Follow "
            "with a real question about their field: \"Okay, real question - "
            "what is your science?\""
        ),
        "key_points": [
            "The line: \"Are you made of copper and tellurium? Because you are Cu-Te.\"",
            "When it works: labs, campuses, science museums - where the periodic table is shared knowledge.",
            "Why it works: rewards the listener's knowledge; sweet and nerdy reads as safe.",
            "Delivery tip: pronounce it \"cutie,\" laugh at yourself, follow with a real question.",
        ],
        "requirements": [
            "Use where the chemistry reference will land.",
            "Own the nerdiness; never apologize for it.",
            "Follow with genuine curiosity about their field.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_TRAD, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Copper Tellurium as Signature alchemy - the "
            "old formula recited with new joy. The Signature speaker wears "
            "his nerdiness as a badge; the elements combine, and so - with "
            "consent and laughter - might two people."
        ),
    },
    {
        "key": "gravity_line",
        "name": "The Gravity Line",
        "line": "You must be gravity, because I am falling for you.",
        "tags": ["science", "physics", "classic", "sweet"],
        "group": "Science Lines",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"You must be gravity, because I am falling for you.\" "
            "Context notes: the classic physics pickup line, gentle as a "
            "feather. It works anywhere - it needs no special setting, only "
            "a moment of mutual warmth. It works best after a few minutes "
            "of good conversation, when \"falling for you\" is a sweet "
            "exaggeration both people can smile at. It is the physics "
            "equivalent of a hand-drawn card: simple, sincere, a little "
            "cheesy, and all the better for it."
        ),
        "how_it_works": (
            "Why it works: everyone knows gravity, so no knowledge is "
            "required, and \"falling\" is the oldest metaphor for affection "
            "- the line borrows ten thousand love songs' credibility. "
            "Delivery tips: deliver it softly, almost as an aside, with a "
            "shy smile; the understatement is the charm. Do not oversell it "
            "- the line is a feather, and feathers do not need throwing "
            "arms. Best followed by something honest: \"Okay, that was "
            "cheesy, but I am really enjoying talking to you.\""
        ),
        "key_points": [
            "The line: \"You must be gravity, because I am falling for you.\"",
            "When it works: after a few minutes of warm conversation, anywhere.",
            "Why it works: universal metaphor; the cheese is the charm.",
            "Delivery tip: soft, almost an aside, shy smile; follow with honest warmth.",
        ],
        "requirements": [
            "Use after some conversation, not as a cold opener.",
            "Deliver softly; never oversell it.",
            "Mean the warmth underneath the cheese.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_TRAD, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Gravity Line as Signature attraction in the "
            "truest sense - two people drawn together, honestly named. The "
            "Signature speaker falls upward, toward kindness; the line is "
            "light because the feeling is real."
        ),
    },
    {
        "key": "photosynthesis",
        "name": "The Photosynthesis Compliment",
        "line": "You must be the sun - everything in my day just started revolving around you.",
        "tags": ["science", "astronomy", "compliment", "daytime"],
        "group": "Science Lines",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"You must be the sun - everything in my day just "
            "started revolving around you.\" Context notes: the astronomy "
            "compliment - grand, warm, and impossible to take as anything "
            "but kind. It works in daylight, at planetariums, on hikes, at "
            "outdoor festivals - anywhere the sun is doing its work. It "
            "works best delivered with open delight, because the line's "
            "scale is its joke: comparing a person to a star is absurd, and "
            "the absurdity is the gift."
        ),
        "how_it_works": (
            "Why it works: it is a compliment of cosmic scale with zero "
            "physical specificity - it praises presence, not appearance. The "
            "heliocentric image (everything revolving around them) says "
            "\"you matter\" in the grandest terms. Delivery tips: gesture "
            "up at the actual sun if it is out; grin at the absurdity - you "
            "know it is over the top, and that is the point. Keep it to one "
            "orbit: say the line, smile, and move to real conversation "
            "before the metaphor wears thin."
        ),
        "key_points": [
            "The line: \"You must be the sun - everything in my day just started revolving around you.\"",
            "When it works: daylight, planetariums, hikes, festivals - where the sun is present.",
            "Why it works: cosmic-scale compliment of presence, not appearance.",
            "Delivery tip: grin at the absurdity, gesture at the real sun, then move to real talk.",
        ],
        "requirements": [
            "Praise presence, never the body.",
            "Own the over-the-top scale with a grin.",
            "One orbit only; then real conversation.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Sun as Signature center - the speaker "
            "orbits the other person's light honestly and says so. In the "
            "Signature method, telling someone they brighten your day is a "
            "complete kindness; the astronomy is just the wrapping."
        ),
    },
    {
        "key": "bunsen_smile",
        "name": "The Bunsen Burner Smile",
        "line": "Is your smile a Bunsen burner? Because it is burning with the steadiest blue flame I have ever seen.",
        "tags": ["science", "chemistry", "smile", "lab"],
        "group": "Science Lines",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"Is your smile a Bunsen burner? Because it is "
            "burning with the steadiest blue flame I have ever seen.\" "
            "Context notes: the chemistry-lab compliment - it praises a "
            "smile using the hottest, cleanest flame in the lab (blue means "
            "complete combustion). It works in labs, classrooms, science "
            "museums, and among students anywhere. It works best on someone "
            "who is actually smiling, because the line is a mirror held up "
            "to a real moment. The science is accurate, which science "
            "people will appreciate."
        ),
        "how_it_works": (
            "Why it works: it is specific - not \"nice smile\" but a whole "
            "little theory of why the smile matters - and specificity reads "
            "as attention. The blue-flame detail rewards science knowledge. "
            "Delivery tips: say it while they are smiling, with admiration "
            "rather than performance; if they ask what a blue flame means, "
            "explain happily - teaching is flirting for nerds. Never use it "
            "on someone who is not smiling; complimenting a frown with "
            "fire imagery misfires."
        ),
        "key_points": [
            "The line: \"Is your smile a Bunsen burner? Because it is burning with the steadiest blue flame I have ever seen.\"",
            "When it works: labs, classrooms, among students - while they are actually smiling.",
            "Why it works: specific theory of the smile; the blue-flame detail rewards science knowledge.",
            "Delivery tip: admiration not performance; explain happily if asked.",
        ],
        "requirements": [
            "Use only while they are genuinely smiling.",
            "The science must be right: blue flame is the hot clean one.",
            "Admiration, never performance.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Bunsen Burner as Signature fire - steady, "
            "blue, and honest. The Signature speaker's admiration burns "
            "clean: no smoke, no show, just the true color of attention "
            "paid well."
        ),
    },
    {
        "key": "noble_gas",
        "name": "The Noble Gas Line",
        "line": "You must be a noble gas, because you complete me - no reaction required.",
        "tags": ["science", "chemistry", "wordplay", "sweet"],
        "group": "Science Lines",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"You must be a noble gas, because you complete me - "
            "no reaction required.\" Context notes: the chemistry "
            "wordplay line - noble gases have full outer electron shells, "
            "so they are complete without bonding. It works among "
            "chemistry students, in labs, at science events, and anywhere "
            "the reference lands. It works best with a gentle, self-aware "
            "delivery, because \"you complete me\" is a famous movie line "
            "wearing a lab coat - the double reference is the joke."
        ),
        "how_it_works": (
            "Why it works: two layers - the chemistry (full shells need "
            "nothing) and the movie quote - reward the listener twice. \"No "
            "reaction required\" is the clever turn: it says the "
            "completeness is already there. Delivery tips: pause slightly "
            "before \"no reaction required\" - the pause is where the laugh "
            "lives; deliver the movie line straight, then break into a "
            "grin. If they do not know noble gases, explain in one "
            "sentence: \"they are the elements that are already complete.\""
        ),
        "key_points": [
            "The line: \"You must be a noble gas, because you complete me - no reaction required.\"",
            "When it works: among chemistry people - labs, classes, science events.",
            "Why it works: double reward - the chemistry and the movie quote; \"no reaction required\" is the turn.",
            "Delivery tip: pause before the punchline; explain in one sentence if needed.",
        ],
        "requirements": [
            "Best where the chemistry reference lands.",
            "Pause before the punchline; the pause holds the laugh.",
            "One-sentence explanation ready for non-chemists.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Noble Gas as Signature completeness - the "
            "speaker honors someone who needs nothing to be whole, and "
            "offers to orbit anyway. Signature love never demands a "
            "reaction; it recognizes the full shell and celebrates it."
        ),
    },
    {
        "key": "hypothesis",
        "name": "The Hypothesis Opener",
        "line": "My hypothesis: this conversation will be the best part of my day. Care to help me test it?",
        "tags": ["science", "method", "invitation", "playful"],
        "group": "Science Lines",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The line: \"My hypothesis: this conversation will be the best "
            "part of my day. Care to help me test it?\" Context notes: the "
            "scientific-method opener - it turns the scientific process "
            "into an invitation. It works on campuses, at conferences, in "
            "labs and libraries - anywhere the word \"hypothesis\" gets a "
            "smile. It works best as an actual opener because it contains "
            "its own call to action: \"care to help me test it\" is a "
            "question that starts the experiment immediately."
        ),
        "how_it_works": (
            "Why it works: it is optimistic (\"best part of my day\") "
            "without being presumptuous (\"hypothesis\" admits it is "
            "untested), and it recruits the other person as a co-researcher "
            "rather than a subject. Delivery tips: deliver it like a real "
            "proposal - bright, curious, pen-ready; if the conversation "
            "goes well, close the loop later: \"hypothesis confirmed.\" "
            "Scientists love a confirmed hypothesis, and the callback is "
            "charming. Never fake the method: actually listen, actually "
            "test."
        ),
        "key_points": [
            "The line: \"My hypothesis: this conversation will be the best part of my day. Care to help me test it?\"",
            "When it works: campuses, conferences, labs - as a true opener with a built-in call to action.",
            "Why it works: optimistic but untested; recruits them as co-researcher.",
            "Delivery tip: bright and curious; close the loop later with \"hypothesis confirmed.\"",
        ],
        "requirements": [
            "Actually listen; the method must be real.",
            "Optimistic, never presumptuous.",
            "Close the loop honestly at the end.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Hypothesis as Signature experiment - the "
            "speaker stakes his day on a guess and invites peer review. In "
            "the Signature method every meeting is data, every conversation "
            "a trial, and the kindest hypothesis is the one you test with "
            "your full attention."
        ),
    },
    {
        "key": "dictionary_def",
        "name": "The Dictionary Definition",
        "line": "I looked up captivating in the dictionary, and it just said your name.",
        "tags": ["bookish", "dictionary", "compliment", "witty"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"I looked up captivating in the dictionary, and it "
            "just said your name.\" Context notes: the lexicographer's "
            "compliment - it promotes the other person from an example "
            "sentence to the definition itself. It works among word lovers: "
            "bookstores, libraries, writing workshops, trivia nights. It "
            "works best delivered deadpan, because the humor is in the "
            "absurd image of a dictionary that just gives up and names "
            "them. Swap \"captivating\" for any true adjective - radiant, "
            "remarkable, delightful - but it must be true."
        ),
        "how_it_works": (
            "Why it works: definitions are authoritative, so being the "
            "definition is the highest linguistic compliment; the deadpan "
            "delivery makes it funny rather than heavy. Delivery tips: say "
            "it straight, like reporting a fact, then let the smile break "
            "through - the crack is the charm. Follow with a question that "
            "proves you are interested in the person behind the definition: "
            "\"So what is the etymology - where are you from?\" Never use a "
            "word you would not defend; the dictionary does not lie."
        ),
        "key_points": [
            "The line: \"I looked up captivating in the dictionary, and it just said your name.\"",
            "When it works: among word lovers - bookstores, workshops, trivia nights.",
            "Why it works: being the definition is the highest linguistic compliment; deadpan makes it funny.",
            "Delivery tip: straight-faced report, then let the smile crack; follow with real curiosity.",
        ],
        "requirements": [
            "The adjective must be true and defensible.",
            "Deadpan delivery; the crack is the charm.",
            "Follow with curiosity about the person, not the wordplay.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Dictionary as Signature naming - the "
            "speaker gives the other person the highest entry in his "
            "lexicon. In the Signature method, what you name someone in "
            "your private dictionary is a covenant; \"captivating\" is "
            "entered in ink."
        ),
    },
    {
        "key": "star_chart",
        "name": "The Star Chart Line",
        "line": "If every star is a wish, you must be the whole constellation I wished on.",
        "tags": ["science", "astronomy", "romantic", "evening"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"If every star is a wish, you must be the whole "
            "constellation I wished on.\" Context notes: the astronomer's "
            "romantic line, built as a two-step: the premise (stars are "
            "wishes) then the escalation (not a star - the whole "
            "constellation). It works on clear evenings, at observatories, "
            "on night hikes, at outdoor concerts under the sky. It works "
            "best when stars are actually visible, because the line points "
            "at the real sky and borrows its grandeur."
        ),
        "how_it_works": (
            "Why it works: the structure is a miniature argument - premise, "
            "then a conclusion that out-scales the premise - and the "
            "escalation from star to constellation is the delightful "
            "surprise. Delivery tips: look up at the sky on the first half, "
            "then at them on the second; the glance is the punctuation. "
            "Keep your voice soft; grandeur whispered is romance, grandeur "
            "shouted is theater. If clouds hide the stars, adapt: \"the "
            "stars are shy tonight, so I will say it plainly.\""
        ),
        "key_points": [
            "The line: \"If every star is a wish, you must be the whole constellation I wished on.\"",
            "When it works: clear evenings, observatories, night hikes - where stars are visible.",
            "Why it works: premise-then-escalation; star to constellation is the surprise.",
            "Delivery tip: eyes to sky on premise, to them on conclusion; whisper the grandeur.",
        ],
        "requirements": [
            "Best under a real visible sky; adapt honestly if cloudy.",
            "Soft voice; grandeur whispered, never shouted.",
            "The glance from sky to them is load-bearing.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Constellation as Signature navigation - "
            "the speaker charts his wishes by another person's light. In "
            "the Signature method, wishing is honest work; the constellation "
            "is named, and the course is set kindly."
        ),
    },
    {
        "key": "periodic_serenade",
        "name": "The Periodic Table Serenade",
        "line": "Roses are red, violets are blue, you are my favorite element, and I have the data to prove it.",
        "tags": ["science", "chemistry", "poem", "witty"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"Roses are red, violets are blue, you are my "
            "favorite element, and I have the data to prove it.\" Context "
            "notes: the valentine rebuilt for scientists - the classic "
            "four-line poem with a lab report for a punchline. It works in "
            "classrooms, labs, and among science students, especially "
            "around Valentine's season or as a note rather than spoken. It "
            "works best written - on a card, a whiteboard, a lab notebook "
            "margin - because \"data\" implies evidence, and evidence can "
            "be listed: the smile data, the laugh data, the kindness data."
        ),
        "how_it_works": (
            "Why it works: the first two lines set up the oldest poem in "
            "English, and the last two swerve into the lab - the collision "
            "of romance and rigor is the joke. \"I have the data\" is funny "
            "because affection is famously unquantifiable. Delivery tips: "
            "if spoken, recite the first two lines sweetly and the last two "
            "like a researcher presenting findings; if written, actually "
            "list two or three \"data points\" underneath - real observed "
            "kindnesses. Never present fake data; the observations must be "
            "true."
        ),
        "key_points": [
            "The line: \"Roses are red, violets are blue, you are my favorite element, and I have the data to prove it.\"",
            "When it works: classrooms, labs, science students - best written, with real data points below.",
            "Why it works: oldest poem collides with lab rigor; the affection-data joke lands.",
            "Delivery tip: sweet recitation then researcher tone; list true observed kindnesses as data.",
        ],
        "requirements": [
            "Any listed data points must be true observations.",
            "Works best written; spoken needs the tone shift.",
            "Keep the romance-to-rigor collision playful.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Serenade as Signature peer review - "
            "affection submitted with evidence. The Signature method holds "
            "that the best compliments are reproducible: observed, "
            "recorded, and true on replication."
        ),
    },
    {
        "key": "algorithm_us",
        "name": "The Algorithm of Us",
        "line": "If I wrote an algorithm for the perfect evening, every path would lead to you.",
        "tags": ["science", "computing", "clever", "evening"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"If I wrote an algorithm for the perfect evening, "
            "every path would lead to you.\" Context notes: the programmer's "
            "romantic line - it borrows the language of search algorithms, "
            "where every path converging means the optimum is proven. It "
            "works among tech people, at hackathons, in computer science "
            "classes, and at tech meetups. It works best delivered with "
            "quiet confidence, because the line's claim is total: not some "
            "paths, every path."
        ),
        "how_it_works": (
            "Why it works: it translates \"I really want to spend the "
            "evening with you\" into a proof, and proofs are the love "
            "language of technical minds. \"Every path\" is the romantic "
            "escalation - thoroughness as devotion. Delivery tips: say it "
            "like stating a result, then soften with a smile; if they are "
            "technical, they may riff back (\"what is the time complexity "
            "of us?\") - play along. Keep it to one execution; algorithms "
            "that loop forever are bugs, not romance."
        ),
        "key_points": [
            "The line: \"If I wrote an algorithm for the perfect evening, every path would lead to you.\"",
            "When it works: among tech people - hackathons, CS classes, meetups.",
            "Why it works: affection translated into proof; thoroughness as devotion.",
            "Delivery tip: state it like a result, soften with a smile, play along with riffs.",
        ],
        "requirements": [
            "Best where the computing metaphor is shared language.",
            "One execution; do not loop the line.",
            "Mean the devotion underneath the cleverness.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Algorithm as Signature optimization - "
            "every path evaluated, every path converging on kindness. The "
            "Signature method proves its affections the way it proves its "
            "code: by running them, honestly, to completion."
        ),
    },
    {
        "key": "constellation_map",
        "name": "The Constellation Map",
        "line": "Astronomers map constellations by connecting bright points. I just found my brightest one.",
        "tags": ["science", "astronomy", "clever", "evening"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"Astronomers map constellations by connecting bright "
            "points. I just found my brightest one.\" Context notes: the "
            "astronomer's two-sentence construction - a true fact, then a "
            "personal conclusion. It works at planetariums, observatories, "
            "night events, and on clear evenings generally. It works best "
            "when delivered as a quiet realization rather than a "
            "performance, because \"I just found\" implies the discovery "
            "happened live, in front of them."
        ),
        "how_it_works": (
            "Why it works: the first sentence is real astronomy, which "
            "establishes credibility and calm; the second applies the "
            "method to the person, which is the romantic turn. \"Brightest "
            "one\" compliments luminosity of spirit, not looks. Delivery "
            "tips: pause between the sentences - the pause is the "
            "telescope focusing; deliver the second sentence looking at "
            "them, softly. Then ask what they find bright in the world - "
            "turn the observation back outward."
        ),
        "key_points": [
            "The line: \"Astronomers map constellations by connecting bright points. I just found my brightest one.\"",
            "When it works: planetariums, observatories, clear evenings - as a quiet realization.",
            "Why it works: true fact then personal conclusion; compliments luminosity of spirit.",
            "Delivery tip: pause between sentences like a focusing telescope; then ask outward.",
        ],
        "requirements": [
            "Deliver as realization, not performance.",
            "The pause between sentences is load-bearing.",
            "Compliment spirit, never appearance.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Map as Signature cartography - the speaker "
            "charts the bright points he finds in people. In the Signature "
            "method, attention is the telescope and kindness the "
            "constellation; both are pointed outward."
        ),
    },
    {
        "key": "time_traveler",
        "name": "The Time Traveler",
        "line": "I am not a time traveler, but I can see us laughing about this moment a year from now.",
        "tags": ["science", "physics", "future", "sweet"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"I am not a time traveler, but I can see us laughing "
            "about this moment a year from now.\" Context notes: the "
            "future-casting line - it skips past the awkward present into a "
            "warm imagined future. It works when a first meeting is going "
            "well and both people are laughing: at parties, dinners, long "
            "walks, festivals. It works best mid-laughter, because the line "
            "claims the laughter will continue - and in that moment, it is "
            "already true."
        ),
        "how_it_works": (
            "Why it works: the denial (\"I am not a time traveler\") is "
            "funny and disarming, and the vision it offers - us, laughing, "
            "a year from now - is the most hopeful picture a new "
            "acquaintance can paint. It says \"I want this to last\" "
            "without the weight of saying it plainly. Delivery tips: say "
            "it mid-laugh, lightly, like the thought just occurred; do not "
            "linger on it or explain it - let the future sit there, "
            "glowing. Then keep laughing; the line is a toast, not a "
            "contract."
        ),
        "key_points": [
            "The line: \"I am not a time traveler, but I can see us laughing about this moment a year from now.\"",
            "When it works: mid-laughter in a first meeting that is going well.",
            "Why it works: the denial disarms; the imagined future is hope without weight.",
            "Delivery tip: light and mid-laugh, do not explain it; it is a toast, not a contract.",
        ],
        "requirements": [
            "Use only when genuine laughter is already happening.",
            "Light delivery; never linger or oversell.",
            "Hope, never pressure about the future.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Time Traveler as Signature foresight - "
            "the speaker sees the kindness continuing and says so. "
            "Signature hope is always offered, never extracted; the future "
            "is an invitation, and the laughter is already the answer."
        ),
    },
    {
        "key": "permission_slip",
        "name": "The Librarian Permission Slip",
        "line": "I checked with the librarian, and I have official permission to check you out.",
        "tags": ["bookish", "library", "playful", "witty"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"I checked with the librarian, and I have official "
            "permission to check you out.\" Context notes: the library-book "
            "line's bureaucratic sequel - it adds a whole imaginary "
            "permission process to the classic pun. It works in libraries "
            "and bookstores, and best on someone who already smiled at the "
            "original library-book line - it is a callback, a second verse. "
            "It works best delivered with mock solemnity, as if the "
            "permission slip were a real document."
        ),
        "how_it_works": (
            "Why it works: it takes the familiar pun and adds a layer of "
            "absurd officialdom - the humor is in the imagined paperwork. "
            "As a callback it rewards continuity: \"we have a running joke "
            "now.\" Delivery tips: straight face, official tone, as if "
            "reading from a form; then break - the break is the punchline. "
            "If they play along (\"let me see the slip\"), improvise: \"it "
            "is being laminated.\" Callbacks build rapport faster than any "
            "single line."
        ),
        "key_points": [
            "The line: \"I checked with the librarian, and I have official permission to check you out.\"",
            "When it works: libraries and bookstores, as a callback after the library-book line landed.",
            "Why it works: absurd officialdom on a familiar pun; callbacks build rapport.",
            "Delivery tip: mock solemnity, then break; improvise if they play along.",
        ],
        "requirements": [
            "Best as a callback; needs the first line's goodwill.",
            "Mock solemnity, then the break.",
            "Play along if they riff back.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Permission Slip as Signature paperwork - "
            "even the joke is filed properly. The Signature speaker builds "
            "rapport the honest way: one shared laugh at a time, each "
            "properly stamped and remembered."
        ),
    },
    {
        "key": "chemistry_eq",
        "name": "The Chemistry Equation",
        "line": "You plus me - I ran the numbers, and it is the most balanced equation I have ever seen.",
        "tags": ["science", "chemistry", "clever", "sweet"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"You plus me - I ran the numbers, and it is the "
            "most balanced equation I have ever seen.\" Context notes: the "
            "stoichiometry of affection - a balanced equation is "
            "chemistry's image of perfect fairness, nothing wasted, "
            "everything accounted for. It works among science students and "
            "at academic social events. It works best delivered with "
            "playful precision, because \"I ran the numbers\" is funniest "
            "when said about something gloriously unquantifiable."
        ),
        "how_it_works": (
            "Why it works: \"balanced\" is doing double duty - chemically "
            "correct and emotionally ideal - and the image promises "
            "fairness, which is deeply attractive. The mock rigor (\"I ran "
            "the numbers\") frames affection as a result, not a whim. "
            "Delivery tips: tap an imaginary calculator or notebook on \"I "
            "ran the numbers\"; grin at the absurdity. Then prove the "
            "balance by listening as much as you talk - the line promises "
            "equilibrium, so demonstrate it."
        ),
        "key_points": [
            "The line: \"You plus me - I ran the numbers, and it is the most balanced equation I have ever seen.\"",
            "When it works: among science students, academic socials - with playful precision.",
            "Why it works: \"balanced\" means chemically correct and emotionally fair.",
            "Delivery tip: mime the calculation; then demonstrate balance by listening equally.",
        ],
        "requirements": [
            "Demonstrate the promised balance: listen as much as you talk.",
            "Playful precision; never dead-serious about the math.",
            "Fairness must be real, not just wordplay.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Equation as Signature stoichiometry - "
            "nothing wasted, everything accounted for, both sides equal. "
            "In the Signature method, affection is balanced by design: "
            "give and receive, speak and listen, in perfect equilibrium."
        ),
    },
    {
        "key": "odyssey_opener",
        "name": "The Odyssey Opener",
        "line": "It took Odysseus ten years to get home. It took me one look to know I wanted to talk to you.",
        "tags": ["bookish", "classic", "epic", "witty"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"It took Odysseus ten years to get home. It took me "
            "one look to know I wanted to talk to you.\" Context notes: "
            "the epic simile - ten years of wandering versus one look. It "
            "works at literary events, classics departments, book clubs, "
            "and on anyone who loves the old stories. It works best with a "
            "storyteller's relish, because the line's pleasure is its "
            "scale: your journey was longer than the Odyssey and ended the "
            "moment you saw them."
        ),
        "how_it_works": (
            "Why it works: the contrast (ten years vs. one look) is the "
            "engine - epic time collapsed into an instant, which is exactly "
            "how attraction feels. Naming Odysseus flatters the listener's "
            "literacy. Delivery tips: give \"ten years\" its full weight - "
            "slow down, let the epic breathe - then quicken on \"one look\"; "
            "the tempo change is the magic. End with a real question, or "
            "the epic has no second act."
        ),
        "key_points": [
            "The line: \"It took Odysseus ten years to get home. It took me one look to know I wanted to talk to you.\"",
            "When it works: literary events, classics lovers - with storyteller relish.",
            "Why it works: ten years vs. one look - epic time collapsed into the instant attraction feels like.",
            "Delivery tip: slow on \"ten years,\" quicken on \"one look\"; end with a real question.",
        ],
        "requirements": [
            "Best where the Odyssey reference is caught.",
            "Tempo change is load-bearing: slow, then quick.",
            "Follow with a real question; epics need second acts.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_TRAD, CIT_SCREEN,
                      "Homer. The Odyssey. Trans. Wilson E. Norton; 2017. Epic journey echoed and collapsed."],
        "sig_lens": (
            "Signature lens: the Odyssey as Signature homecoming - every "
            "long road in the method ends at a person worth knowing. The "
            "Signature speaker has wandered, learned, and arrived; the one "
            "look is earned by the ten years."
        ),
    },
    {
        "key": "astronomers_wish",
        "name": "The Astronomer Wish",
        "line": "I wished on every star last night, and this morning you were standing here.",
        "tags": ["science", "astronomy", "romantic", "morning"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"I wished on every star last night, and this "
            "morning you were standing here.\" Context notes: the "
            "wish-fulfillment line - it claims the universe answered. It "
            "works in the morning after a starry night: on camping trips, "
            "at dawn events, on morning hikes, at sunrise gatherings. It "
            "works best when last night genuinely had stars, because the "
            "line borrows reality's magic. It is the most romantic line in "
            "the archive; reserve it for when the feeling is real."
        ),
        "how_it_works": (
            "Why it works: it is a complete little story - wishing, night, "
            "morning, arrival - and stories with happy endings feel true "
            "even when we know they are wishes. \"Every star\" is "
            "delightfully thorough. Delivery tips: say it softly, like "
            "telling a secret the universe told you; morning light does "
            "half the work, so let it. Do not use it lightly - a line this "
            "romantic spent casually devalues the currency. Mean the "
            "wonder."
        ),
        "key_points": [
            "The line: \"I wished on every star last night, and this morning you were standing here.\"",
            "When it works: mornings after real starry nights - camping, dawn hikes, sunrise gatherings.",
            "Why it works: a complete story - wishing, night, morning, arrival - with a happy ending.",
            "Delivery tip: soft, like a secret; let the morning light work; mean the wonder.",
        ],
        "requirements": [
            "Reserve for when the feeling is real; never spend casually.",
            "Best after a genuinely starry night.",
            "Soft delivery; the line is a secret, not a speech.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Wish as Signature gratitude - the speaker "
            "thanks the night sky for the morning. In the Signature method, "
            "wonder is never performed; it is witnessed, recorded, and "
            "spoken softly to the one who caused it."
        ),
    },
    {
        "key": "poets_proof",
        "name": "The Poet Proof",
        "line": "Poets say the eyes are windows. Yours just showed me a view I never want to leave.",
        "tags": ["bookish", "poetry", "romantic", "evening"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"Poets say the eyes are windows. Yours just showed "
            "me a view I never want to leave.\" Context notes: the poetic "
            "proof - premise from the poets, conclusion from the heart. It "
            "works in the evening, in quiet moments of real connection: "
            "after a long talk, during a slow dance, on a night walk. It "
            "works best when eye contact is already natural between you, "
            "because the line names what is already happening. This is a "
            "late-ladder line: it needs the evening's weight behind it."
        ),
        "how_it_works": (
            "Why it works: it borrows the poets' authority for the premise, "
            "then makes it personal - the oldest move in rhetoric, and it "
            "still works. \"A view I never want to leave\" is tender "
            "without being possessive. Delivery tips: hold the eye contact "
            "the line is about; say it slowly, letting each clause land. "
            "Then be quiet for a moment - the silence after is part of the "
            "line. Never use it without the evening's weight; premature "
            "poetry curdles."
        ),
        "key_points": [
            "The line: \"Poets say the eyes are windows. Yours just showed me a view I never want to leave.\"",
            "When it works: quiet evening moments of real connection, with natural eye contact.",
            "Why it works: poets' authority plus personal conclusion; tender without possessive.",
            "Delivery tip: hold the gaze, slow clauses, then silence - the pause is part of the line.",
        ],
        "requirements": [
            "Needs the evening's weight; never premature.",
            "Hold the eye contact the line names.",
            "Tender, never possessive.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Poet's Proof as Signature beholding - the "
            "speaker looks long and kindly, and reports what he sees. In "
            "the Signature method, attention is the rarest gift; given "
            "fully, it becomes a view worth staying for."
        ),
    },
    {
        "key": "kindness_theorem",
        "name": "The Kindness Theorem",
        "line": "Theorem: kindness is the most attractive quality in the universe. Proof: you, standing here.",
        "tags": ["science", "math", "kindness", "capstone"],
        "group": "Witty Multi-Liners",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The line: \"Theorem: kindness is the most attractive quality "
            "in the universe. Proof: you, standing here.\" Context notes: "
            "the capstone of the archive - the whole ladder's lesson "
            "compressed into a two-line proof. It works as a closing line "
            "after any good meeting: the theorem states the database's "
            "thesis, and the proof is the person in front of you. It works "
            "best when you have witnessed their kindness during your time "
            "together, because then the proof is not flattery - it is a "
            "cited result."
        ),
        "how_it_works": (
            "Why it works: the theorem-proof structure is the language of "
            "certainty, and applying it to kindness makes the compliment "
            "feel proven rather than performed. \"You, standing here\" is "
            "the shortest possible proof. Delivery tips: announce \"Theorem\" "
            "like a lecturer, then deliver the proof warmly and directly; "
            "the contrast between formal frame and tender content is the "
            "charm. Cite your evidence if asked: \"Exhibit A - you helped "
            "that kid with his books.\" The archive ends where it began: "
            "with kindness, noticed."
        ),
        "key_points": [
            "The line: \"Theorem: kindness is the most attractive quality in the universe. Proof: you, standing here.\"",
            "When it works: as a closing line after a good meeting where you witnessed their kindness.",
            "Why it works: theorem-proof structure makes the compliment feel proven, not performed.",
            "Delivery tip: lecturer tone for the theorem, warm for the proof; cite evidence if asked.",
        ],
        "requirements": [
            "The proof must be earned: cite real witnessed kindness.",
            "Formal frame, tender content; the contrast is the charm.",
            "A closing line, not an opener.",
        ],
        "standards": [STD_WHOLESOME, STD_CONSENT, STD_HONEST],
        "citations": [CIT_ORIG, CIT_SCREEN],
        "sig_lens": (
            "Signature lens: the Kindness Theorem as the Signature QED - "
            "the whole method proven in two lines. Kindness, noticed and "
            "named, is the most attractive quality in the universe; the "
            "archive rests its case on the person standing in front of you."
        ),
    },
]
