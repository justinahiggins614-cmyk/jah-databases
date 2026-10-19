#!/usr/bin/env python3
"""Seed entries for the Compassionate Statements databases.

34 ladder-ordered records. Public = real, generatable comfort craft:
words of comfort, empathy, and support for grief, hardship, illness,
and struggle - each record a statement WITH guidance on when and how
to say it genuinely. Tender and sincere only - never platitudes,
never minimizing.

Signature = the same ladder through the Signature lens: compassion as
covenant - the comfort given is a promise kept; tenderness as
strength; presence as the Signature vow. Titles suffixed
" (Signature Edition)", src signature, clearly labeled Signature-made.

Screened: nothing hate-adjacent, profane, or inappropriate; no
religious talk. Every statement checked for minimizing language
("at least", "just", "get over it", "everything happens for a
reason", "be strong") - zero tolerated.

Statement texts are the demo cross-check anchor: build.py asserts
each entry's statement appears verbatim in its demo program.
"""

SIG_TAIL = ("Signature original - compassion as covenant: the comfort "
            "given is a promise kept, tenderness is strength, and presence "
            "is the Signature vow. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_ROGERS = ("Rogers CR. On Becoming a Person: A Therapist's View of "
              "Psychotherapy. Houghton Mifflin; 1961. (empathic listening; "
              "unconditional positive regard)")
CIT_KUBLER = ("Kubler-Ross E, Kessler D. On Grief and Grieving: Finding "
              "the Meaning of Grief Through the Five Stages of Loss. "
              "Scribner; 2014.")
CIT_WORDEN = ("Worden JW. Grief Counseling and Grief Therapy: A Handbook "
              "for the Mental Health Practitioner. 5th ed. Springer; 2018. "
              "(the tasks of mourning)")
CIT_NEIMEYER = ("Neimeyer RA, editor. Techniques of Grief Therapy: Creative "
                "Practices for Counseling the Bereaved. Routledge; 2012.")
CIT_CROWE = ("Crowe K, McDowell E. There Is No Good Card for This: What to "
             "Say and Do When Life Is Scary, Awful, and Unfair to People You "
             "Love. Dey Street; 2017.")
CIT_GOLDMAN = ("Goldman S. How not to say the wrong thing. Los Angeles "
               "Times; 2013. (Ring Theory: comfort in, dump out)")
CIT_VITALTALK = ("VitalTalk. Serious illness communication skills "
                 "curriculum: NURSE statements for responding to emotion "
                 "(Naming, Understanding, Respecting, Supporting, "
                 "Exploring).")
CIT_APA_GRIEF = ("American Psychological Association. Grief: Coping with "
                 "the loss of your loved one. APA Help Center.")

ENTRIES = [
    {
        "key": "simple_presence",
        "name": "The Simple Presence: I Am Here With You",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "statement": ("I am here with you. You do not have to go through "
                      "this alone."),
        "when_to_say": ("Say it in the first moments, when someone is "
                        "reeling and no one knows what comes next - at the "
                        "hospital, on the phone at midnight, in the doorway "
                        "after bad news. It is the opening line of comfort; "
                        "it asks nothing and promises the only thing you "
                        "can honestly promise: your presence."),
        "how_to_say": ("Say it slowly, in a low steady voice, and then "
                       "stop talking. Do not add explanations, stories, or "
                       "silver linings. If you are there in person, sit at "
                       "their level; a hand on a shoulder only if welcome. "
                       "On the phone, let the silence after it breathe - "
                       "the pause is part of the statement."),
        "description": (
            "The simplest compassionate statement is also the strongest: a "
            "plain declaration of presence. When someone's world has just "
            "tilted, their nervous system is scanning for one thing - am I "
            "alone in this. 'I am here with you' answers that scan directly, "
            "before the thinking mind has caught up. It works because it "
            "contains no claim about the future, no evaluation of the "
            "situation, and no request. It does not say things will be "
            "fine, which you cannot know. It does not ask how they feel, "
            "which they may not be able to name yet. It simply places you "
            "beside them. This record teaches the foundation every later "
            "statement builds on: comfort begins with presence, not with "
            "words that fix."
        ),
        "how_it_works": (
            "Presence calms before language persuades. A person in shock or "
            "fresh grief is running on the oldest parts of the brain, which "
            "read safety from bodies and voices long before they parse "
            "sentences. A steady voice saying 'I am here' lowers the sense "
            "of isolation that makes pain feel unsurvivable. The statement "
            "also protects the speaker from the most common failure of "
            "comfort: the rush to say something clever or hopeful. By "
            "giving you a complete, honest sentence to say, it stops you "
            "from filling the silence with platitudes. The second sentence "
            "- 'You do not have to go through this alone' - extends the "
            "first across time: not just this minute, but the road ahead. "
            "Said once, sincerely, it becomes the reference point the "
            "person returns to later: somebody was there."
        ),
        "key_points": [
            "Presence is the foundation of all comfort: before advice, before explanations, before hope, simply be there.",
            "The statement makes no promises about the future and no judgments about the situation - that is why it is always honest.",
            "Short sentences land harder in shock; long speeches get lost. Two sentences are enough.",
            "The silence after the statement is part of it - do not rush to fill it.",
            "This is the line to use when you have no other line. Memorize it.",
        ],
        "requirements": [
            "Say it early - in the first contact after you learn the news, not after days of drafting the perfect message.",
            "Mean it literally: if you say you are here, stay reachable in the days that follow.",
            "Match your body to your words: sit down, slow down, put the phone away.",
            "Do not attach conditions - no 'call me if you need anything' vagueness; the statement itself is the offer.",
            "Say it once. Repeating it turns a vow into a slogan.",
        ],
        "standards": [
            "No minimizing language anywhere near it: never 'at least', 'just', 'get over it', or 'everything happens for a reason'.",
            "No unsolicited advice in the same breath - presence first, practical help later and separately.",
            "Keep the focus on them: do not follow with your own similar story.",
            "If you cannot be present, say what you CAN do instead - never promise presence you will not deliver.",
        ],
        "citations": [CIT_ROGERS, CIT_CROWE, CIT_APA_GRIEF],
        "sig_lens": (
            "The Signature read: presence is the first covenant. Where the "
            "world offers noise, the Signature comforter offers the "
            "strongest currency in the system - themselves, placed beside "
            "another person, with no exit planned. 'I am here' is not a "
            "sentence; it is a signature on an unwritten promise, and the "
            "Signature keeper does not break what they sign."
        ),
    },
    {
        "key": "naming_what_you_see",
        "name": "Naming What You See: This Looks Really Hard",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "statement": ("This looks really hard. I can see how much weight "
                      "you are carrying."),
        "when_to_say": ("Say it when someone is clearly struggling but "
                        "has not named it - the colleague going quiet, the "
                        "friend canceling plans, the family member holding "
                        "it together in public. It opens a door without "
                        "kicking it down: they can walk through or not."),
        "how_to_say": ("Say it as an observation, not a diagnosis - 'this "
                       "looks hard', never 'you look terrible'. Keep your "
                       "tone level and warm, not pitying. Then wait. If "
                       "they deflect with 'I am fine', accept it lightly: "
                       "'Okay. The door is open whenever.' Do not "
                       "interrogate."),
        "description": (
            "Most suffering goes unnamed, and unnamed suffering is lonely "
            "suffering. 'This looks really hard' does a small, powerful "
            "thing: it tells the person that their struggle is visible, "
            "which means it is real. People in hard seasons often wonder "
            "whether they are overreacting; having another person name the "
            "weight gives them permission to set it down, at least in "
            "conversation. The second sentence - 'I can see how much weight "
            "you are carrying' - does two jobs: it shows you have been "
            "paying attention, and it frames their difficulty as a load "
            "rather than a flaw. Loads can be shared. Flaws feel like "
            "verdicts. This record teaches the foundation skill of "
            "naming: say what you see, plainly and kindly, and let the "
            "other person decide what happens next."
        ),
        "how_it_works": (
            "Naming works because the brain treats an unnamed feeling as a "
            "threat without edges - it bleeds into everything. Putting "
            "words to it gives the feeling a boundary, and a bounded "
            "feeling can be faced. When YOU name it for them, gently, you "
            "lend them your prefrontal cortex for a moment: you do the "
            "labeling work their exhausted mind cannot. The phrasing "
            "matters. 'This looks hard' describes the situation; 'you seem "
            "stressed' describes the person, which can feel like judgment. "
            "'Weight you are carrying' is a metaphor with a built-in "
            "kindness: weight implies they have been strong, not that they "
            "have been weak. The statement asks for nothing, which is why "
            "it is safe to receive - there is no test to pass, no cheering "
            "up required."
        ),
        "key_points": [
            "Name the situation, not the person: 'this looks hard' opens; 'you look awful' judges.",
            "Visible struggle confirmed is lonely struggle halved - being seen is itself comfort.",
            "The weight metaphor honors their endurance instead of pathologizing their pain.",
            "Ask for nothing in return; the statement is complete without a response.",
            "If they deflect, leave the door open without pushing through it.",
        ],
        "requirements": [
            "Base it on something real you have observed - specific attention, not generic concern.",
            "Keep it to two sentences; a longer speech starts to sound like a case being built.",
            "Deliver it privately when you can - being seen is comforting, being exposed is not.",
            "Follow their lead after: talk, silence, or subject change are all acceptable answers.",
            "Remember what you noticed, and check back in a few days.",
        ],
        "standards": [
            "Never name it as a diagnosis or a label - no 'you are depressed', no armchair psychology.",
            "No minimizing follow-ups: never 'but look on the bright side' after naming the dark.",
            "Do not share what you noticed with others - an observation of pain is confidential.",
            "Pity is poison: keep your tone level, warm, and peer-to-peer.",
        ],
        "citations": [CIT_ROGERS, CIT_VITALTALK, CIT_CROWE],
        "sig_lens": (
            "The Signature read: to name a burden truly is to lift a "
            "corner of it. The Signature comforter does not flinch from "
            "what they see and does not dress it up - they call the weight "
            "by its true name, which is the oldest form of respect. Seeing "
            "clearly is the covenant; what is seen with honor can be "
            "carried with honor."
        ),
    },
    {
        "key": "permission_to_feel",
        "name": "Permission to Feel: It Is Okay to Feel This Way",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "statement": ("It is okay to feel this way. There is no wrong way "
                      "to feel right now."),
        "when_to_say": ("Say it when someone apologizes for their own "
                        "feelings - 'sorry, I am being emotional', 'I know "
                        "I should be over this', 'I feel silly crying'. "
                        "That apology is the signal: they have absorbed "
                        "the idea that their feelings are a problem, and "
                        "they need explicit permission to drop that idea."),
        "how_to_say": ("Say it firmly but gently, like a fact rather than "
                       "a pep talk. Make eye contact if in person. Do not "
                       "ask what they are feeling first - the permission "
                       "covers all of it, named or not. If tears come, "
                       "treat them as normal weather, not an emergency: "
                       "stay steady, offer a tissue without fuss."),
        "description": (
            "A surprising amount of suffering is suffering about "
            "suffering: people feel bad, then feel bad about feeling bad. "
            "'It is okay to feel this way' cuts that second layer away. It "
            "tells the person that their emotional response is not a "
            "failure of character, a burden on others, or a sign they are "
            "handling things wrong - it is simply what is happening, and "
            "what is happening is allowed. The second sentence widens the "
            "permission: 'no wrong way to feel' covers the anger that "
            "feels disloyal, the numbness that feels broken, the laughter "
            "that feels guilty, the relief that feels shameful. This "
            "record teaches a foundation of comfort: never make someone "
            "audition their feelings for legitimacy. Grant the feeling "
            "citizenship first; everything else gets easier after."
        ),
        "how_it_works": (
            "Permission works by removing the meta-judgment that doubles "
            "pain. When a person believes they should not feel what they "
            "feel, they spend energy suppressing the feeling instead of "
            "moving through it - and suppressed feelings do not shrink, "
            "they ferment. An explicit 'it is okay' from a trusted voice "
            "acts as social proof: if this person I respect says my "
            "feeling is allowed, maybe it is. The statement is deliberately "
            "content-free - it does not name the feeling, so it cannot "
            "name it wrong. It works for grief, fear, anger, shame, and "
            "numbness alike, which makes it one of the most versatile "
            "statements in the database. Said with calm certainty, it "
            "becomes an inner voice the person can replay later when the "
            "self-judgment returns."
        ),
        "key_points": [
            "Feelings do not need a permit, but people in pain often wait for one - be the one who grants it.",
            "The apology for feeling ('sorry I am emotional') is the cue this statement exists for.",
            "Content-free permission cannot miss: it covers anger, numbness, guilt, and relief equally.",
            "Treat tears as weather, not emergency - your calm teaches their nervous system that this is survivable.",
            "Permission granted once becomes an inner voice they can replay later.",
        ],
        "requirements": [
            "Say it with calm certainty, not as a question - 'it IS okay', not 'is it okay?'",
            "Do not follow it with 'but' - any 'but' revokes the permission you just granted.",
            "Let the feeling be whatever size it is; do not grade it.",
            "If they say 'you do not understand', do not argue - say 'you are right, I do not fully, and it is still okay to feel it.'",
            "Extend the permission over time: feelings that are okay today are still okay next month.",
        ],
        "standards": [
            "Never rank feelings: no 'at least you are not...', no comparing their pain to worse pain.",
            "Never set an expiry date on the permission: no 'you will feel better soon' timelines.",
            "Do not confuse permission with approval of harmful actions - feelings are always allowed; actions still have consequences.",
            "No fixing attached: permission is complete on its own.",
        ],
        "citations": [CIT_ROGERS, CIT_KUBLER, CIT_WORDEN],
        "sig_lens": (
            "The Signature read: every feeling is a citizen of the inner "
            "republic, and the Signature comforter does not deport "
            "citizens. To say 'it is okay to feel this way' is to stamp "
            "the passport - anger, grief, fear, numbness, all granted "
            "lawful passage. The covenant is simple: no feeling of theirs "
            "will ever be treated as trespass in your presence."
        ),
    },
    {
        "key": "honest_admission",
        "name": "The Honest Admission: I Do Not Know What to Say",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "statement": ("I do not know what to say, but I am not going "
                      "anywhere."),
        "when_to_say": ("Say it when the situation is so big or so strange "
                        "that every prepared sentence feels false - a "
                        "shocking loss, a tragedy with no shape yet, a "
                        "pain you have never touched. It is the honest "
                        "replacement for silence born of fear, and for "
                        "chatter born of discomfort."),
        "how_to_say": ("Say the first half plainly, without drama or "
                       "self-pity - this is not about your inadequacy, it "
                       "is about the size of what happened. Put the weight "
                       "on the second half: 'but I am NOT going anywhere.' "
                       "Then prove it by staying - in the room, on the "
                       "phone, in the weeks after."),
        "description": (
            "The most honest sentence in comfort is an admission of "
            "speechlessness, and it outperforms almost every clever line "
            "ever written for hard moments. 'I do not know what to say' "
            "does three things at once: it tells the truth, which builds "
            "trust; it refuses to dress the tragedy in pretty language, "
            "which honors its size; and it relieves the pressure on both "
            "sides to perform wisdom. Most failed comfort fails because "
            "the speaker could not tolerate their own helplessness and "
            "filled it with noise - advice, platitudes, stories. The "
            "admission converts helplessness from a shameful secret into "
            "a shared fact. And the second half is the whole point: "
            "not-knowing is acceptable, leaving is not. This record "
            "teaches the foundation honesty: when words fail, say that "
            "words fail, and stay anyway."
        ),
        "how_it_works": (
            "The admission works because grieving people have finely tuned "
            "falsehood detectors. In crisis, the mind scans every voice "
            "for honesty, and rehearsed comfort reads as distance - the "
            "speaker protecting themselves from the rawness. 'I do not "
            "know what to say' passes the scan instantly: it is "
            "verifiably true, it costs the speaker a little pride, and "
            "pride-costly truth is trusted. The second clause then does "
            "the real work. 'I am not going anywhere' is a commitment, "
            "and commitments are what the frightened mind is actually "
            "listening for - not explanations, but evidence that the "
            "social world will hold. The pairing is the mechanism: honesty "
            "about words, certainty about presence. One without the other "
            "fails - honesty alone sounds like retreat, presence alone "
            "without honesty sounds like a script."
        ),
        "key_points": [
            "Admitting speechlessness is not failure; it is the most trusted sentence in hard moments.",
            "The admission must be brief - it is a doorway, not a monologue about your discomfort.",
            "Pair honesty about words with certainty about presence: one without the other fails.",
            "This statement replaces both kinds of failure: frozen silence AND nervous chatter.",
            "The proof comes after: staying is what makes the sentence true.",
        ],
        "requirements": [
            "Keep the focus on them: one admission, then pivot back to their reality.",
            "Do not perform helplessness - no long speeches about how hard this is FOR YOU.",
            "Say it once, early; repeating it starts to sound like an excuse.",
            "After saying it, do something concrete: sit, listen, bring food, handle a task.",
            "If you truly cannot stay, do not say you are not going anywhere - say what you will actually do.",
        ],
        "standards": [
            "Honesty is not a license for bluntness: 'I do not know what to say' is humble, not 'this is awful, wow'.",
            "Never follow the admission with a platitude - that rebuilds exactly the falsehood you just demolished.",
            "Do not make them comfort YOU about your speechlessness.",
            "If words fail completely, a hand on a shoulder and your continued presence say it without language.",
        ],
        "citations": [CIT_CROWE, CIT_ROGERS, CIT_GOLDMAN],
        "sig_lens": (
            "The Signature read: the Signature comforter never counterfeits "
            "wisdom. Where others mint shiny sentences to cover their "
            "helplessness, the Signature keeper admits the empty vault and "
            "offers the one currency that is real - staying. Honesty about "
            "the limits of words is itself the deepest respect for the "
            "size of the pain."
        ),
    },
    {
        "key": "listening_first",
        "name": "Listening First: Silence Before Solutions",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "statement": ("Tell me as much or as little as you want. I am "
                      "listening."),
        "when_to_say": ("Say it when someone starts to open up and then "
                        "stalls - the half-sentence that trails off, the "
                        "'never mind', the look away. It is also the right "
                        "opener when you arrive and they clearly need to "
                        "talk but do not know where to begin."),
        "how_to_say": ("Say it quietly and then actually do it: eyes up, "
                       "mouth closed, phone down. Nod slowly; make small "
                       "sounds of attention, not of judgment. When they "
                       "pause, count to five in your head before you "
                       "speak - most people fill their own pauses if you "
                       "let them. Reflect back what you heard before you "
                       "add anything of your own."),
        "description": (
            "Before any statement of comfort can land, someone has to "
            "listen - and listening is itself a compassionate statement, "
            "spoken with the ears instead of the mouth. 'Tell me as much "
            "or as little as you want' hands the person complete control "
            "of the telling: the scope, the depth, the pace. That control "
            "matters because pain often comes with a loss of control, and "
            "every choice you return to them is a small restoration. 'I "
            "am listening' is a promise with a visible proof - your "
            "attention, which they can see on your face. This record "
            "teaches the foundation discipline of comfort: the best "
            "response to 'I need to talk' is rarely a statement at all. "
            "It is the statement that you will receive whatever they say."
        ),
        "how_it_works": (
            "Listening works because telling is processing. When a person "
            "narrates what happened out loud to a calm, attentive witness, "
            "the brain begins to file the event as a story with a "
            "beginning, middle, and end, instead of a loop that replays "
            "without resolution. The listener's job is to be the safe "
            "container for that filing: no interruptions, no redirecting "
            "to solutions, no visible shock that makes the teller feel "
            "they have said too much. The phrase 'as much or as little' "
            "lowers the stakes of starting, which is the hardest part - "
            "once a person begins and feels safely received, they will "
            "usually say exactly what they needed to say. Your silence, "
            "held warmly, does more work than your sentences."
        ),
        "key_points": [
            "Listening is a statement: 'I am listening' said with the whole body, not just the mouth.",
            "Give them control of the telling - scope, depth, and pace are theirs to set.",
            "Silence held warmly outperforms sentences; count to five before filling a pause.",
            "Reflect before you add: 'what I hear you saying is...' proves the listening was real.",
            "The goal is not to solve but to witness - most telling needs a witness, not a mechanic.",
        ],
        "requirements": [
            "Put the phone away, face them, and keep your expression open - attention must be visible.",
            "Do not interrupt, correct, or redirect until they are clearly finished.",
            "Ask before advising: 'do you want ideas, or do you want me to just listen?' - then honor the answer.",
            "Remember the details they share; follow up on them later by name.",
            "If you feel the urge to fix, notice it and set it aside - that urge is about your discomfort, not their need.",
        ],
        "standards": [
            "What is told in confidence stays in confidence - listening creates a vault, not a broadcast.",
            "No visible shock, disgust, or pity faces - your reactions become their self-judgment.",
            "Never use what they told you as leverage later, even gently.",
            "If they say 'never mind', accept it: 'Okay. I am here when you want.' - the offer stands without pressure.",
        ],
        "citations": [CIT_ROGERS, CIT_VITALTALK, CIT_WORDEN],
        "sig_lens": (
            "The Signature read: the Signature comforter knows that the "
            "ear is mightier than the tongue. To listen fully is to lend "
            "another person your calm while they rebuild their story - a "
            "sacred loan, given without interest and without deadline. "
            "The covenant of listening: what is spoken to you in pain is "
            "held in honor, and never spent elsewhere."
        ),
    },
    {
        "key": "hard_day",
        "name": "Comfort for a Hard Day: Small Words, Real Weight",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "statement": ("Today sounds like it asked too much of you. I am "
                      "sorry it went that way."),
        "when_to_say": ("Say it at the end of a brutal ordinary day - the "
                        "day everything went wrong at work, the errands "
                        "that avalanched, the small humiliations that "
                        "piled up. Not for tragedies; for the grinding "
                        "days that do not qualify as emergencies but still "
                        "hurt."),
        "how_to_say": ("Say it with plain sympathy, not ceremony - this is "
                       "Tuesday-night comfort, not a eulogy. A text is "
                       "fine; so is saying it over dishes. Do not inflate "
                       "it into a big production, and do not minimize it "
                       "into 'everyone has those days'. Meet the day at "
                       "its actual size."),
        "description": (
            "Not all pain is tragedy. Much of human suffering arrives as "
            "an ordinary day that asked too much: the deadline that moved, "
            "the car that died, the rude customer, the sick kid, the "
            "spilled everything. These days rarely get comfort because "
            "they do not feel important enough to mention - and that is "
            "exactly why they need it. 'Today sounds like it asked too "
            "much of you' validates the day at its true size: not a "
            "catastrophe, but genuinely too much. 'I am sorry it went that "
            "way' is the smallest complete apology the universe offers - "
            "not taking blame, just standing beside the fact that it "
            "stung. This record teaches proportion in comfort: match the "
            "statement to the day. Small honest words for small hard "
            "days keep trust intact for the big ones."
        ),
        "how_it_works": (
            "The statement works by refusing both errors people make with "
            "ordinary bad days: inflation and dismissal. Inflation ('oh "
            "no, that is TERRIBLE') feels false and teaches the person "
            "their pain needs drama to count. Dismissal ('everyone has "
            "those days') teaches them their pain does not count at all. "
            "'Asked too much of you' threads the needle - it names the "
            "day as excessive without declaring it historic. The apology "
            "that follows is social glue: research on everyday empathy "
            "shows that acknowledged small pains do not accumulate into "
            "resentment, while unacknowledged ones do. A hard day that is "
            "witnessed ends at midnight; a hard day that is waved away "
            "joins the pile that eventually breaks a person."
        ),
        "key_points": [
            "Ordinary bad days need comfort too - unacknowledged small pains accumulate into big resentment.",
            "Match the statement to the day: plain sympathy for Tuesday, not ceremony and not dismissal.",
            "'Asked too much of you' names excess without declaring catastrophe - proportion is kindness.",
            "A witnessed hard day ends at midnight; a dismissed one joins the pile.",
            "Small honest comfort builds the trust that big comfort will later draw on.",
        ],
        "requirements": [
            "Acknowledge the specific day, not days in general - 'today', not 'life'.",
            "Keep it brief: a text, a sentence over dinner, a squeeze of the shoulder.",
            "Do not problem-solve unless asked - most hard days need witness, not workflow.",
            "If it is a pattern rather than a day, say so gently: 'this has been a lot of todays lately.'",
            "Follow with something restorative if you can: food, quiet, an early night - comfort with hands.",
        ],
        "standards": [
            "No ranking: never 'at least it was not...' - the day gets to be hard at its own size.",
            "No toxic positivity: no 'tomorrow is a new day' speeches before the person has exhaled.",
            "Do not make their bad day about your worse day.",
            "If you caused part of the day, own your part plainly before comforting the rest.",
        ],
        "citations": [CIT_CROWE, CIT_ROGERS, CIT_GOLDMAN],
        "sig_lens": (
            "The Signature read: the Signature keeper honors the small "
            "battles, because wars are won in Tuesdays. To witness an "
            "ordinary hard day with full sincerity is to declare that no "
            "pain of theirs is too small for your attention. The covenant "
            "covers the whole calendar - the historic and the household "
            "alike."
        ),
    },
    {
        "key": "honoring_effort",
        "name": "Honoring Effort: Your Work Matters Even When It Fails",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "statement": ("I saw how hard you worked. The outcome does not "
                      "erase the effort."),
        "when_to_say": ("Say it when effort did not pay off - the failed "
                        "exam after months of study, the lost game after "
                        "hard training, the project that died, the "
                        "application rejected. Say it soon after the "
                        "result, while the person is doing the math that "
                        "effort was wasted."),
        "how_to_say": ("Be specific about what you saw: name the late "
                       "nights, the practice, the care. 'I saw' must be "
                       "true - do not invent witnessing. Say it steadily, "
                       "like a fact entering the record. Do not rush past "
                       "the disappointment to the lesson; let the effort "
                       "be honored first."),
        "description": (
            "Failure has a cruel arithmetic: the mind subtracts the "
            "result from the effort and concludes the effort was worth "
            "nothing. 'I saw how hard you worked' intervenes at exactly "
            "that subtraction - it puts a witness on the record that the "
            "work was real, regardless of the scoreboard. The second "
            "sentence states the principle: outcomes and effort are "
            "separate accounts, and a loss in one is not a loss in the "
            "other. This matters because the person is not just grieving "
            "a result; they are deciding whether trying is still worth "
            "it. Your statement votes for trying. This record teaches a "
            "foundation of encouragement: honor the work first, and let "
            "the person decide what the result means at their own pace."
        ),
        "how_it_works": (
            "The statement works by separating two things the "
            "disappointed mind fuses: effort and outcome. When they fuse, "
            "a bad outcome retroactively poisons the memory of the work, "
            "and the person learns that caring leads to pain - the "
            "beginning of giving up. 'I saw' is doing specific work: "
            "being seen trying is profoundly different from trying "
            "alone, because effort witnessed becomes part of your "
            "identity ('I am someone who works hard') rather than a "
            "secret gamble. The specificity requirement is load-bearing: "
            "generic praise ('you did great') bounces off, but a named "
            "detail ('those 6 a.m. practices') proves the witness is "
            "real. The statement does not deny the disappointment - it "
            "refuses to let the disappointment be the only story."
        ),
        "key_points": [
            "Failure fuses effort and outcome in the mind; comfort must separate them again.",
            "'I saw' must be specific and true - named details prove the witness is real.",
            "You are not denying the disappointment; you are refusing to let it be the only story.",
            "Honor the work before any lesson-talk; lessons can wait, dignity cannot.",
            "Your statement votes for trying again - that vote matters more than you know.",
        ],
        "requirements": [
            "Name something concrete you actually observed - the hours, the preparation, the care.",
            "Say it soon after the result, while the 'effort was wasted' math is still forming.",
            "Let them be disappointed: do not argue them out of the feeling, only out of the verdict on their effort.",
            "Do not predict the next outcome - no 'you will get it next time' guarantees you cannot keep.",
            "If the effort genuinely fell short somewhere, save that conversation for another day entirely.",
        ],
        "standards": [
            "Never say 'at least you tried' - 'at least' shrinks the very effort you mean to honor.",
            "No comparisons to whoever succeeded - this moment is about their work, not the scoreboard.",
            "Do not reframe too fast: 'everything happens for a reason' is banned here.",
            "If you did not actually see the work, say 'tell me about what you put into it' and listen first.",
        ],
        "citations": [CIT_ROGERS, CIT_CROWE, CIT_WORDEN],
        "sig_lens": (
            "The Signature read: in the Signature system, effort is "
            "currency and the ledger is honest. The scoreboard may say "
            "loss, but the Signature keeper reads the deeper books, where "
            "every hour of real work is entered and never erased. To "
            "witness effort truly is to countersign the ledger - and a "
            "countersigned ledger stands, whatever the scoreboard claims."
        ),
    },
    {
        "key": "disappointment",
        "name": "Words for Disappointment: When Hopes Fall Through",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "statement": ("It makes sense that this hurts. You hoped for "
                      "something real."),
        "when_to_say": ("Say it when a hope collapses - the job that went "
                        "to someone else, the relationship that ended, "
                        "the plan that fell through, the news that was "
                        "supposed to be good. Say it when the person is "
                        "caught between the feeling and the judgment of "
                        "the feeling: 'I should not be this upset.'"),
        "how_to_say": ("Say it in a normal voice, not a hushed tragedy "
                       "voice - disappointment is a regular human event, "
                       "and treating it as ordinary is part of the "
                       "comfort. Validate the hope first ('you hoped for "
                       "something real'), because the hope is what makes "
                       "the hurt legitimate."),
        "description": (
            "Disappointment is grief's smaller sibling, and it gets less "
            "respect than it deserves. When hopes fall through, people "
            "often hear - from others and from themselves - that they "
            "should not feel so much about 'just' a job, 'just' a plan, "
            "'just' a what-if. 'It makes sense that this hurts' grants "
            "the feeling logic: of course it hurts, because the hope was "
            "real and the hope mattered. The second sentence honors the "
            "hope itself rather than treating it as naive. This is the "
            "crucial move in comforting disappointment: do not comfort "
            "the person by shrinking what they wanted. Comfort them by "
            "confirming that wanting it was reasonable. This record "
            "teaches proportionate validation: the hurt is legitimate "
            "because the hope was legitimate."
        ),
        "how_it_works": (
            "Disappointment hurts in two layers: the loss itself, and the "
            "embarrassment of caring. The second layer is what keeps "
            "people from seeking comfort - they pre-reject themselves so "
            "others cannot. 'It makes sense' dismantles the second layer "
            "directly: it supplies the logic the person could not supply "
            "for themselves in the moment. Once the feeling is declared "
            "sensible, the person stops spending energy defending their "
            "right to feel and can actually feel. 'You hoped for "
            "something real' does the deeper repair: it protects the "
            "capacity to hope. If every disappointed hope is retroactively "
            "labeled foolish, people stop hoping; if the hope is honored "
            "even in failure, hope survives to try again. The statement "
            "is short because disappointment does not need a speech - it "
            "needs a witness who does not flinch at the size of the "
            "feeling."
        ),
        "key_points": [
            "Disappointment has two layers: the loss, and the embarrassment of caring - address the second one.",
            "'It makes sense' supplies the logic for the feeling that the person cannot supply mid-pain.",
            "Honor the hope, never shrink it: wanting it was reasonable even though it failed.",
            "Protecting the capacity to hope is the long game of comforting disappointment.",
            "A normal voice, not a tragedy voice: disappointment is a regular human event.",
        ],
        "requirements": [
            "Name the hope as real before addressing the hurt - the hope is what legitimizes the feeling.",
            "Do not rush to the next hope: 'there will be other jobs' can wait until the current loss is witnessed.",
            "Let them define the size of it; do not grade disappointment.",
            "If they say 'I am overreacting', disagree plainly: 'You are reacting to something real.'",
            "Check back after the sting fades - disappointment often needs a second, quieter conversation.",
        ],
        "standards": [
            "No 'just' language: never 'it was just a job', 'just a game', 'just a...' - the 'just' is the wound.",
            "No silver-lining sprints: 'this could be a blessing' is banned in the first conversation.",
            "Never compare their disappointment to someone else's bigger loss.",
            "Do not turn it into a lesson about expectations before they have finished feeling it.",
        ],
        "citations": [CIT_CROWE, CIT_ROGERS, CIT_APA_GRIEF],
        "sig_lens": (
            "The Signature read: hope is a Signature asset, and the "
            "Signature keeper does not let a failed hope depreciate the "
            "hopper. To honor a fallen hope as real is to keep the "
            "person's hope-capital intact for the next venture. The "
            "covenant: no hope of theirs will ever be called foolish in "
            "your presence, whatever the outcome."
        ),
    },
    {
        "key": "visiting_sick",
        "name": "Visiting the Sick: Comfort Without Cliches",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "statement": ("I came to sit with you for a while. No need to talk "
                      "unless you want to."),
        "when_to_say": ("Say it when you visit someone who is ill - at "
                        "home, in the hospital, during recovery. Say it at "
                        "the door, before the visit takes shape, so the "
                        "sick person knows the terms: your company, their "
                        "rules."),
        "how_to_say": ("Say it warmly and plainly, then settle in "
                       "visibly: sit down, get comfortable, show you are "
                       "not in a hurry. Bring something small if you can - "
                       "food, a magazine, nothing that demands a reaction. "
                       "If they sleep, let them; your quiet presence in "
                       "the chair is the statement continuing."),
        "description": (
            "Visiting the sick is where comfort most often goes wrong, "
            "because the visitor's anxiety fills the room faster than "
            "their kindness. The sick person is already managing their "
            "illness; they should not have to manage your discomfort too. "
            "'I came to sit with you for a while' sets the visit's terms "
            "up front: duration is modest ('a while'), the agenda is "
            "company, and the sick person owes nothing. 'No need to talk "
            "unless you want to' removes the performance pressure that "
            "makes visits exhausting - the need to be entertaining, "
            "upbeat, or grateful while ill. This record teaches "
            "visit-craft: the best visit asks nothing of the patient, "
            "brings its own ease, and leaves the person less tired than "
            "it found them."
        ),
        "how_it_works": (
            "The statement works by transferring all social obligation "
            "from the patient to the visitor. Illness already steals "
            "energy; a visit that demands conversation, cheer, or "
            "gratitude steals more. By pre-announcing that silence is "
            "acceptable, you remove the tax the visit would otherwise "
            "levy. 'Sit with you' is doing deliberate work against the "
            "instinct to DO something - the sick do not need projects, "
            "they need unhurried company. The permission not to talk also "
            "protects against the classic visitor failure: nervous chatter "
            "about how great they look, miracle recoveries, and other "
            "people's illnesses. A visit with no agenda cannot go wrong "
            "the way an agenda-driven visit can. And 'for a while' is "
            "honest about limits - it promises presence without promising "
            "forever, which makes the promise keepable."
        ),
        "key_points": [
            "The visit must ask nothing of the patient: no performance, no cheer, no gratitude.",
            "Pre-announce the terms at the door: your company, their rules, silence allowed.",
            "Bring your own ease - settle in visibly so they do not have to host you.",
            "'For a while' is honest about limits; keepable promises beat grand ones.",
            "If they sleep, stay quietly: your presence in the chair is the statement continuing.",
        ],
        "requirements": [
            "Keep visits short unless invited longer - twenty good minutes beat an exhausting hour.",
            "Ask about practical needs separately and specifically: 'can I bring groceries Thursday?' not 'let me know if you need anything.'",
            "Talk about normal life, not just illness - they are a person, not a diagnosis.",
            "Wash your hands, stay home if you are sick yourself, and respect medical boundaries.",
            "Come back. One visit is kindness; repeated visits are care.",
        ],
        "standards": [
            "No cliche medicine: banned phrases include 'you look great' (when they do not), 'stay positive', 'everything happens for a reason', and all miracle-cure stories.",
            "Never compare illnesses or tell other people's medical horror stories.",
            "Do not offer medical advice unless you are their clinician and they asked.",
            "No pity face, no whispered tones about them as if they cannot hear - dignity is treatment too.",
        ],
        "citations": [CIT_VITALTALK, CIT_CROWE, CIT_APA_GRIEF],
        "sig_lens": (
            "The Signature read: to sit with the sick asking nothing is "
            "the purest Signature transaction - giving without ledger, "
            "presence without price. The Signature comforter does not "
            "visit to feel helpful; they visit to be present, and the "
            "distinction is everything. In the sickroom, the covenant is "
            "quiet: I will not make your illness about my discomfort."
        ),
    },
    {
        "key": "after_mistake",
        "name": "After a Mistake: Comfort Without Shame",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "statement": ("One mistake does not rewrite who you are. I am "
                      "still here, same as before."),
        "when_to_say": ("Say it when someone has messed up and is "
                        "drowning in shame - the failed test they "
                        "cheated on, the harsh words they cannot take "
                        "back, the error at work, the lapse they are "
                        "ashamed to name. Say it when they expect you to "
                        "recalculate their worth downward."),
        "how_to_say": ("Say it steadily, without a lecture attached. Do "
                       "not lead with the lesson or the consequences - "
                       "those conversations come later, separately. The "
                       "tone is continuity: same voice, same regard as "
                       "before the mistake. If you are disappointed, you "
                       "can say so another day; today is for the person, "
                       "not the performance review."),
        "description": (
            "Shame is the feeling that a mistake has rewritten the self: "
            "not 'I did something bad' but 'I am bad'. Comfort after a "
            "mistake must therefore do one precise job - separate the act "
            "from the identity. 'One mistake does not rewrite who you "
            "are' draws that line explicitly: the deed is real, the "
            "verdict on the person is not. The second sentence - 'I am "
            "still here, same as before' - answers shame's deepest fear, "
            "which is abandonment: that the mistake will cost them their "
            "people. This record teaches shame-first comfort: before "
            "consequences, before lessons, before repair plans, the "
            "person needs to know they are still held. Accountability "
            "lands only on ground that is still solid."
        ),
        "how_it_works": (
            "The statement works because shame isolates, and isolation "
            "blocks every path to repair. A person convinced they are "
            "fundamentally bad does not fix the mistake - they hide from "
            "it, repeat it, or punish themselves instead of repairing "
            "it. 'Does not rewrite who you are' reframes the mistake as "
            "an event in a life rather than the definition of a life, "
            "which is the cognitive shift that makes accountability "
            "possible. 'Same as before' is the anti-abandonment clause: "
            "shame predicts rejection, and predicted rejection becomes "
            "self-fulfilling withdrawal. By declaring continuity "
            "explicitly, you break the prediction. Note what the "
            "statement does NOT do: it does not excuse the mistake, "
            "minimize the harm, or skip consequences. It secures the "
            "person so the consequences can be faced rather than fled."
        ),
        "key_points": [
            "Shame says 'I am bad'; comfort must separate the act from the identity.",
            "The deepest fear in shame is abandonment - 'I am still here' answers it directly.",
            "Secure the person first; accountability lands only on solid ground.",
            "This statement does not excuse the mistake - it makes facing it possible.",
            "Continuity of regard ('same as before') is the medicine; lectures are for later.",
        ],
        "requirements": [
            "Say it before any discussion of consequences or lessons - sequence matters.",
            "Mean the continuity: do not say 'same as before' and then treat them differently for months.",
            "Let them name what happened; do not force a confession as the price of comfort.",
            "If harm was done to others, acknowledge the harmed separately - comfort for the mistake-maker never erases the debt to the harmed.",
            "Return to normal rhythms quickly; prolonged special treatment keeps the shame alive.",
        ],
        "standards": [
            "No 'I told you so', no 'what did you expect' - those are shame with a smile.",
            "Do not broadcast the mistake to others as a cautionary tale.",
            "Never use the comfort as leverage later: 'after all I forgave you...' is banned.",
            "Do not confuse comfort with absolution you cannot grant - you can hold the person; only the harmed can forgive the harm.",
        ],
        "citations": [CIT_ROGERS, CIT_NEIMEYER, CIT_CROWE],
        "sig_lens": (
            "The Signature read: the Signature keeper judges acts and "
            "shelters souls - the two are never confused. A mistake is "
            "an entry in the ledger of deeds, and ledgers can be "
            "balanced; a person is not a ledger. To hold someone 'same "
            "as before' through their worst hour is the covenant of "
            "continuity, and it is what makes all future accountability "
            "honorable instead of cruel."
        ),
    },
    {
        "key": "fear",
        "name": "Standing With Someone in Fear",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "statement": ("Being afraid makes sense right now. We will take "
                      "this one step at a time."),
        "when_to_say": ("Say it when fear is the dominant feeling - "
                        "before surgery, after a threat, during "
                        "uncertainty about the future, in the dark hours "
                        "of a crisis. Say it when the person is bracing, "
                        "catastrophizing, or frozen."),
        "how_to_say": ("Say the first sentence like a doctor confirming a "
                       "diagnosis - calm, certain, normalizing. Say the "
                       "second like a guide, not a cheerleader: 'one step "
                       "at a time' is a method, not a slogan. Slow your "
                       "own breathing visibly; fear is contagious, but so "
                       "is calm."),
        "description": (
            "Fear makes people feel broken for being afraid - as if "
            "courage were the absence of fear and they are failing the "
            "test. 'Being afraid makes sense right now' normalizes the "
            "fear before addressing it: it says the alarm system is "
            "working correctly, not malfunctioning. The second sentence "
            "then does the only thing that actually helps fear: it "
            "shrinks the horizon. Fear feeds on the whole future at "
            "once; 'one step at a time' reduces the future to the next "
            "doable thing. This record teaches fear-first comfort: "
            "validate the alarm, then narrow the field. Do not argue "
            "with fear using statistics - argue with it using the next "
            "step."
        ),
        "how_it_works": (
            "The statement works on fear's two components: the feeling "
            "and the forecast. The feeling - racing heart, tight chest - "
            "is the body doing its job; telling someone 'do not be "
            "afraid' asks the body to stop working, which fails and adds "
            "shame. 'Makes sense' accepts the body's report as valid "
            "data, which paradoxically lets the body stand down - "
            "acknowledged alarms quiet faster than fought ones. The "
            "forecast is fear's real weapon: the mind projecting the "
            "worst across the whole timeline. 'One step at a time' is a "
            "cognitive intervention disguised as comfort - it forces the "
            "mind to process a single next action instead of an infinite "
            "catastrophe. 'We' is doing quiet work too: fear isolates, "
            "and the plural pronoun puts the person back in company for "
            "the steps ahead."
        ),
        "key_points": [
            "Normalize the alarm before addressing it: fear is the system working, not failing.",
            "Shrink the horizon: fear feeds on the whole future; comfort feeds it one step.",
            "'We' puts the frightened person back in company - fear isolates, plurals reconnect.",
            "Your calm is contagious: slow your own breathing and voice first.",
            "Never argue with fear using statistics; argue with it using the next step.",
        ],
        "requirements": [
            "Name one concrete next step together - the smaller the better: 'first we call the nurse'.",
            "Stay through the scary part if you can; fear comforted at a distance is thinner.",
            "Do not promise outcomes you cannot control - promise your presence through whatever comes.",
            "If fear becomes panic, ground first (feet, breath, naming objects) and talk second.",
            "Check in after the feared thing passes - fear leaves an echo that needs witnessing too.",
        ],
        "standards": [
            "Never 'do not be afraid' or 'there is nothing to be afraid of' - those deny the body's valid report.",
            "No horror stories about the thing they fear, even as 'funny' anecdotes.",
            "Do not diagnose their fear as irrational - rationality is not the issue, safety is.",
            "Never use their fear to control them later: 'remember how scared you were' is banned.",
        ],
        "citations": [CIT_VITALTALK, CIT_ROGERS, CIT_APA_GRIEF],
        "sig_lens": (
            "The Signature read: fear is the night watchman doing his "
            "rounds - the Signature keeper does not shoot the watchman "
            "for raising the alarm. To stand with someone in fear is to "
            "take the next step beside them in the dark, lamp held high, "
            "asking nothing of their courage but company. The covenant: "
            "no one walks the frightening road alone while you have legs "
            "to walk it with them."
        ),
    },
    {
        "key": "exhaustion",
        "name": "Words for Exhaustion: When Someone Is Running Empty",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "statement": ("You have been running on empty. Rest is not "
                      "quitting; it is repair."),
        "when_to_say": ("Say it when someone is depleted - the new "
                        "parent, the overworked colleague, the caregiver, "
                        "the student in finals, anyone whose eyes say "
                        "they have nothing left. Say it when they are "
                        "treating rest as a moral failure."),
        "how_to_say": ("Say it with the authority of permission: this is "
                       "a prescription, not a suggestion. Be concrete "
                       "after - 'I will handle dinner', 'take Saturday', "
                       "'sleep, I have got this'. Exhausted people cannot "
                       "convert permission into logistics; do the "
                       "logistics for them."),
        "description": (
            "Exhaustion is the suffering people feel guiltiest about, "
            "because the culture treats tiredness as a character flaw "
            "rather than a physical fact. 'You have been running on "
            "empty' names the tank level honestly - it says the depletion "
            "is real, observed, and not imagined. The second sentence "
            "attacks the guilt directly: 'rest is not quitting; it is "
            "repair.' This reframe is the whole medicine. As long as rest "
            "feels like surrender, the exhausted person will keep "
            "spending what they do not have, and the crash will choose "
            "the timing for them. This record teaches depletion-first "
            "comfort: name the empty tank, legitimize the refill, and - "
            "crucially - help make the rest actually happen."
        ),
        "how_it_works": (
            "The statement works by converting rest from a moral "
            "category to a mechanical one. 'Quitting' is a story about "
            "character; 'repair' is a story about machines, and machines "
            "are allowed maintenance without shame. The exhausted mind, "
            "which cannot think straight enough to grant itself grace, "
            "borrows your framing instead. 'Running on empty' is "
            "doing observational work: it tells the person you have "
            "noticed the cost they have been paying, which is itself a "
            "form of honor - their effort was seen. The critical "
            "follow-through is logistics: permission without coverage is "
            "cruel, because the exhausted person then lies awake "
            "planning. When you say 'I have got this', you are not just "
            "being kind - you are removing the planning burden that "
            "makes rest impossible."
        ),
        "key_points": [
            "Name the depletion honestly: the empty tank is a fact, not a feeling to debate.",
            "Reframe rest as repair, not surrender - mechanical metaphors bypass moral guilt.",
            "Permission without logistics is cruel: do the covering, not just the saying.",
            "Their effort was seen - naming the cost honors what they spent.",
            "Rest prescribed early prevents the crash that chooses its own timing.",
        ],
        "requirements": [
            "Pair the words with a concrete coverage offer: a task taken, a shift covered, a night guarded.",
            "Protect the rest you prescribed - run interference on interruptions.",
            "Do not prescribe rest and then report back with stress: 'while you were out, everything fell apart' revokes it.",
            "Watch for the pattern: one rest fixes a day; repeated exhaustion needs a life change, raised gently later.",
            "Model it yourself - the comforter who never rests teaches that rest is for other people.",
        ],
        "standards": [
            "Never 'we are all tired' - universalizing their depletion denies its specific weight.",
            "No hustle gospel: 'sleep when you are dead', 'no days off' talk is banned here.",
            "Do not keep score of the rest you enabled - 'after all I did so you could rest' is poison.",
            "If exhaustion looks like depression, say so gently and help them get real help - comfort is not treatment.",
        ],
        "citations": [CIT_ROGERS, CIT_CROWE, CIT_APA_GRIEF],
        "sig_lens": (
            "The Signature read: even the finest engine seizes without "
            "oil, and the Signature keeper maintains their people the "
            "way they maintain their machines - with scheduled care, not "
            "shame. To prescribe rest is to declare the person valuable "
            "enough to maintain. The covenant of repair: no one in your "
            "care runs until they break while you watch."
        ),
    },
    {
        "key": "pain_no_fix",
        "name": "Acknowledging Pain Without Trying to Fix It",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "statement": ("I cannot fix this, and I will not pretend I can. "
                      "But I will stay with you in it."),
        "when_to_say": ("Say it when the pain has no solution - terminal "
                        "illness, irreversible loss, chronic conditions, "
                        "injustices that will not be undone. Say it when "
                        "you feel the itch to offer solutions you do not "
                        "have, and say it instead of scratching that itch."),
        "how_to_say": ("Say the first sentence plainly, without apology "
                       "theater - it is a fact, not a confession. Put the "
                       "full weight on the second sentence: 'BUT I will "
                       "stay with you in it.' Then stay. The sentence is "
                       "a contract; the staying is the signature."),
        "description": (
            "The hardest comfort is for pain with no fix, because the "
            "comforter's own helplessness screams to be relieved - usually "
            "by offering false solutions, premature silver linings, or "
            "busywork advice. 'I cannot fix this, and I will not pretend "
            "I can' disarms that scream honestly. It refuses the two "
            "classic failures at once: abandonment ('this is too big for "
            "me') and false rescue ('have you tried...'). The second "
            "sentence then offers the only thing that is actually on the "
            "table: accompaniment. 'Stay with you IN it' is precise - not "
            "above it, not ahead of it pulling them forward, but in it, "
            "at their level. This record teaches the advanced foundation "
            "of comfort: some pain is not a problem to solve but a place "
            "to sit with someone."
        ),
        "how_it_works": (
            "The statement works by resolving the comforter's dilemma "
            "out loud. Unspoken, the dilemma leaks: the person in pain "
            "senses your discomfort with your own uselessness and starts "
            "managing YOUR feelings - the exact reversal comfort must "
            "avoid. Naming your inability to fix removes the performance "
            "pressure from both sides: they stop waiting for your "
            "solution, you stop auditioning solutions. What remains is "
            "the oldest human comfort technology: co-presence in "
            "suffering. Anthropologically, this is what mourning rituals "
            "have always done - not fix the loss but surround it with "
            "people willing to sit inside it. 'In it' also signals "
            "patience: you are not there to hurry them through, which is "
            "what every fix-it impulse is really about - your timeline, "
            "not theirs."
        ),
        "key_points": [
            "Name your inability to fix out loud - unspoken helplessness leaks and reverses the comfort.",
            "Refuse both classic failures at once: abandonment AND false rescue.",
            "'In it, not above it': sit at their level, not ahead pulling them forward.",
            "Some pain is a place to sit with someone, not a problem to solve.",
            "The sentence is a contract; the staying is the signature.",
        ],
        "requirements": [
            "Interrogate your own fix-it urges: ask 'is this for them or for my discomfort?' before speaking.",
            "Offer practical help separately from emotional presence - 'I will sit with you' and 'I will bring dinner' are different sentences.",
            "Stay for the long middle, not just the dramatic beginning - unfixable pain lasts.",
            "Let them set the pace of any movement; your job is accompaniment, not progress.",
            "Take care of your own helplessness elsewhere - with friends, in writing, not on their shoulders.",
        ],
        "standards": [
            "No false solutions: 'have you tried', miracle stories, and internet cures are banned.",
            "No timelines: 'time heals' may be true and is still not yours to deploy as comfort.",
            "Never make their unfixable pain about your growth: 'this taught me so much' is theft.",
            "Do not disappear when the fixing fails - the second sentence is a promise, keep it.",
        ],
        "citations": [CIT_WORDEN, CIT_CROWE, CIT_VITALTALK],
        "sig_lens": (
            "The Signature read: the Signature keeper does not flee the "
            "unfixable and does not lie about it either. Where others "
            "offer counterfeit rescue, the Signature comforter offers "
            "the genuine article: themselves, seated in the ashes, for "
            "as long as the ashes are hot. This is the covenant of the "
            "long sitting - presence as the answer when there is no "
            "answer."
        ),
    },
    {
        "key": "loneliness",
        "name": "Comfort for Loneliness: You Are Not Invisible",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "statement": ("You matter to me, and I notice you. You are not "
                      "invisible here."),
        "when_to_say": ("Say it when someone is lonely in plain sight - "
                        "the quiet one at the gathering, the friend who "
                        "stopped getting invited, the elderly neighbor, "
                        "the new person, the one who says 'I am fine' a "
                        "little too fast. Loneliness rarely announces "
                        "itself; watch for withdrawal."),
        "how_to_say": ("Say it directly and personally - use their name. "
                       "'YOU matter to ME' is specific, which is why it "
                       "works; generic 'people care about you' bounces "
                       "off. Then prove it with specifics: remember what "
                       "they told you, ask about it, include them next "
                       "time without being asked to."),
        "description": (
            "Loneliness is the pain of being unseen, and its cruelest "
            "feature is invisibility about the invisibility - the lonely "
            "person often believes no one would notice if they vanished. "
            "'You matter to me, and I notice you' attacks that belief at "
            "its root with two specific claims: value ('matter') and "
            "attention ('notice'). Both are in the first person, which "
            "matters enormously: 'people care about you' is abstract and "
            "deniable, but 'I notice you' is a witness statement that "
            "cannot be argued away. 'You are not invisible here' defines "
            "the territory - here, in this relationship, in this room, "
            "you register. This record teaches the foundation of "
            "anti-loneliness: specificity. Generic care does not cure "
            "loneliness; being specifically seen by a specific person "
            "does."
        ),
        "how_it_works": (
            "The statement works because loneliness is not about the "
            "number of people around - it is about the felt sense of "
            "mattering to someone. Research on belonging shows that a "
            "single felt connection outperforms a crowd of shallow ones; "
            "the lonely person at the party is the proof. 'I notice you' "
            "delivers the active ingredient: evidence of being held in "
            "another mind. The specificity requirement is the mechanism - "
            "loneliness makes people discount generic reassurance ('they "
            "are just being nice'), but a concrete detail ('I noticed "
            "you were quiet when everyone was laughing') is unfakeable "
            "proof of attention. 'Here' is doing boundary work: it does "
            "not promise the whole world sees them, which would be "
            "false; it promises THIS relationship is a place where they "
            "register, which can be true."
        ),
        "key_points": [
            "Loneliness is unfelt mattering, not headcount - one felt connection beats a crowd.",
            "First-person specifics ('I notice you') cannot be discounted the way generic care can.",
            "Use their name and a concrete detail: proof of attention is unfakeable.",
            "'Here' promises a territory where they register - honest and keepable.",
            "Watch for withdrawal: loneliness rarely announces itself.",
        ],
        "requirements": [
            "Follow the words with inclusion: invite them, specifically, to the next thing.",
            "Remember details and ask about them later - 'how did the interview go' is the statement continuing.",
            "Reach out first sometimes; the lonely often cannot make the first move.",
            "Be consistent: sporadic attention teaches that mattering is conditional.",
            "If loneliness is chronic, help them find community, not just your company - one person cannot be the whole cure.",
        ],
        "standards": [
            "Never 'you have so many friends' or 'but you are always around people' - that denies the felt reality.",
            "Do not make them perform gratitude for being noticed.",
            "No pity invitations: include them because you want them there, and let it show.",
            "Never share their loneliness as gossip - 'poor thing, so lonely' is a second invisibility.",
        ],
        "citations": [CIT_ROGERS, CIT_CROWE, CIT_APA_GRIEF],
        "sig_lens": (
            "The Signature read: in the Signature system, no person is "
            "a ghost. The keeper's gaze is a ledger entry - to be "
            "noticed by the Signature comforter is to be written into "
            "the books as present, valued, and accounted for. The "
            "covenant of the seen: while you stand in my sight, you "
            "will never be invisible."
        ),
    },
    {
        "key": "caregiver",
        "name": "Supporting the Caregiver: Who Cares for the Carer",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "statement": ("You give so much care. Let someone care for you for "
                      "a change - starting with me."),
        "when_to_say": ("Say it to the person holding everyone else up - "
                        "the one caring for an aging parent, a sick "
                        "spouse, a struggling child, while their own "
                        "needs go unmentioned. Say it when they deflect "
                        "concern with 'I am fine, focus on them.'"),
        "how_to_say": ("Say it as an offer, not a suggestion - and arrive "
                       "with the care already planned: 'I am taking your "
                       "Saturday shift', 'dinner is coming Thursday'. "
                       "Caregivers cannot use vague offers; they have no "
                       "bandwidth to design their own relief. Be "
                       "specific, be scheduled, be reliable."),
        "description": (
            "The caregiver is the person everyone leans on and no one "
            "checks on. Their suffering is doubly invisible: first "
            "because all attention flows to the patient, and second "
            "because caregivers themselves treat their own needs as "
            "disloyal. 'You give so much care' breaks the first "
            "invisibility - it witnesses the labor that everyone "
            "benefits from and nobody names. 'Let someone care for you "
            "for a change' breaks the second - it gives explicit "
            "permission to receive, which the caregiver's guilt would "
            "otherwise veto. 'Starting with me' makes it concrete and "
            "immediate rather than theoretical. This record teaches "
            "caregiver-first comfort: the support system needs its own "
            "support system, and the way in is specific, scheduled, "
            "reliable relief - not sympathy, but coverage."
        ),
        "how_it_works": (
            "The statement works by interrupting the caregiver's core "
            "loop: everyone else's needs are urgent, mine can wait, "
            "waiting becomes permanent, depletion becomes identity. "
            "'You give so much care' externalizes the labor - many "
            "caregivers do not even count what they do as work, so "
            "naming it is the first step to valuing it. 'Let someone' "
            "is permission-shaped: it frames receiving care as "
            "allowing rather than taking, which bypasses the guilt. "
            "'Starting with me' collapses the distance between offer "
            "and delivery - caregivers drown in 'let me know if you "
            "need anything' because need-articulation is itself work. "
            "The mechanism that actually saves caregivers is not words "
            "but respite: regular, reliable breaks. The statement is "
            "the doorway; the scheduled Saturday shift is the room "
            "beyond it."
        ),
        "key_points": [
            "The caregiver's suffering is doubly invisible: attention flows past them, and they veto their own needs.",
            "Name the labor: many caregivers do not count what they do as work until someone says it.",
            "Permission must be shaped as 'allowing', not 'taking' - guilt vetoes taking.",
            "Vague offers drown caregivers; specific scheduled relief saves them.",
            "The statement is the doorway; the recurring break is the room beyond it.",
        ],
        "requirements": [
            "Arrive with relief already planned: named task, named day, no planning burden on them.",
            "Be reliable to the point of boring - caregivers cannot rest on maybe.",
            "Ask how THEY are, and wait through the first 'fine' - the real answer is behind it.",
            "Watch for the crash signs: irritability, tears over small things, health neglect - and act, not just notice.",
            "Stay for the long haul: caregiving is measured in months and years, not weeks.",
        ],
        "standards": [
            "Never 'I do not know how you do it' as a substitute for help - admiration is not coverage.",
            "Do not criticize their caregiving choices; they are doing the hardest job with incomplete information.",
            "Never make them beg: if you see the need, offer before they break.",
            "Do not disappear after the crisis phase - chronic caregiving is when support thins and need deepens.",
        ],
        "citations": [CIT_CROWE, CIT_ROGERS, CIT_VITALTALK],
        "sig_lens": (
            "The Signature read: the caregiver is the load-bearing wall "
            "of the whole house, and the Signature keeper maintains "
            "load-bearing walls before they crack. To care for the carer "
            "is not charity - it is structural engineering. The covenant: "
            "no one who holds up your world will ever be left to fall "
            "unheld."
        ),
    },
    {
        "key": "plans_fall_apart",
        "name": "When Plans Fall Apart: Comfort for Shattered Expectations",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "statement": ("You built those plans with real hope. It is okay "
                      "to grieve the future you pictured."),
        "when_to_say": ("Say it when a envisioned future collapses - the "
                        "move that fell through, the business that "
                        "failed, the wedding called off, the retirement "
                        "plan the diagnosis erased. Say it when everyone "
                        "else is rushing them to 'the next chapter' while "
                        "they are still standing in the rubble of this "
                        "one."),
        "how_to_say": ("Say it slowly, giving the lost future its full "
                       "dignity - do not rush past what they pictured. "
                       "Name something specific about the lost plan if "
                       "you know it: 'that little house with the garden'. "
                       "Specificity proves the future was real enough to "
                       "mourn."),
        "description": (
            "People grieve futures, not just pasts. A collapsed plan is "
            "a loss of something that never existed except in the "
            "imagination - which makes it the loneliest kind of loss, "
            "because there is no funeral for a future. 'You built those "
            "plans with real hope' honors the construction work: the "
            "dreaming, the saving, the planning were real labor, and "
            "their product deserves respect even though it will never be "
            "built. 'It is okay to grieve the future you pictured' "
            "grants the crucial permission - most people feel foolish "
            "mourning something that 'never happened'. This record "
            "teaches future-grief: the unlived life is a legitimate "
            "loss, and rushing someone past it ('on to the next thing') "
            "is a second demolition."
        ),
        "how_it_works": (
            "The statement works by legitimizing a loss the world does "
            "not recognize. Disenfranchised grief - grief without social "
            "permission - is harder to process than recognized grief, "
            "because the mourner must fight for the right to mourn while "
            "mourning. Naming the lost future as grieve-worthy removes "
            "that fight. 'Built with real hope' is doing identity work: "
            "the planner was not naive, they were brave enough to "
            "imagine - and imagination is the faculty that will "
            "eventually build the next plan, so it must be protected, "
            "not shamed. The mechanism also buys time honestly: grieving "
            "the pictured future is what clears the ground. People who "
            "are rushed past it do not move on faster; they carry the "
            "unmourned future into every new plan like a crack in the "
            "foundation."
        ),
        "key_points": [
            "Futures are legitimate losses: the unlived life deserves mourning too.",
            "Disenfranchised grief (no social permission) is harder than recognized grief - grant the permission explicitly.",
            "Honor the planning as real labor; the dream was work, not naivete.",
            "Protect the imagination: shamed hope does not build the next plan.",
            "Rushing past the rubble ('next chapter!') is a second demolition - grieve first, rebuild after.",
        ],
        "requirements": [
            "Name something specific about the lost future to prove it was real enough to mourn.",
            "Let them describe what they pictured - the telling is the funeral the future never got.",
            "Do not pitch the next plan until the current loss has been witnessed.",
            "Distinguish what is truly gone from what can be rebuilt - later, gently, together.",
            "Mark the transition when it comes: 'you are allowed to want something new now.'",
        ],
        "standards": [
            "Never 'it was not meant to be' - fatalism about their hope is not comfort.",
            "No 'when one door closes' speeches in the rubble phase.",
            "Do not treat the lost plan as foolish in hindsight - hindsight is not wisdom, it is just later.",
            "Never rush their timeline: the next chapter opens when they turn the page, not when you do.",
        ],
        "citations": [CIT_WORDEN, CIT_NEIMEYER, CIT_CROWE],
        "sig_lens": (
            "The Signature read: a pictured future is a Signature "
            "draft - drawn in hope, filed in the heart. When the draft "
            "is destroyed, the Signature keeper does not call the "
            "draftsman foolish; they honor the drawing and guard the "
            "hand that drew it, because that hand will draft again. The "
            "covenant: no dream of theirs will ever be mocked in your "
            "presence, however it ended."
        ),
    },
    {
        "key": "grief_first_hours",
        "name": "Grief in the First Hours: What to Say at the Start",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "statement": ("I heard the news. I am so sorry. You do not need "
                      "to say anything back."),
        "when_to_say": ("Say it in the first hours after a death - the "
                        "call, the text, the doorstep visit. This is the "
                        "statement for when the loss is fresh, the "
                        "bereaved is in shock, and every word feels "
                        "simultaneously too small and too much."),
        "how_to_say": ("If by text or message, keep it to these three "
                       "sentences - the bereaved will re-read messages in "
                       "the coming days, and brevity ages well. If in "
                       "person, say it quietly and then follow their lead: "
                       "silence, tears, logistics, whatever comes. Do not "
                       "ask 'how are you' - you know how they are."),
        "description": (
            "The first hours of grief are a distinct country with its own "
            "rules: the bereaved is in shock, the phone will not stop, "
            "and every interaction costs energy they do not have. 'I "
            "heard the news' states the fact without making them retell "
            "it - retelling in the first hours is re-wounding. 'I am so "
            "sorry' is the complete condolence; nothing needs to be "
            "added to it, and in the first hours nothing should be. 'You "
            "do not need to say anything back' is the sentence most "
            "condolences forget, and it is the kindest of the three: it "
            "releases the bereaved from the social debt of responding. "
            "This record teaches first-hours protocol: be brief, be "
            "true, ask nothing, and remove every obligation your comfort "
            "might accidentally create."
        ),
        "how_it_works": (
            "The statement is engineered for shock physiology. In acute "
            "grief the brain's language centers are impaired - long "
            "messages literally cannot be processed, and questions "
            "demand answers the bereaved cannot form. Three short "
            "sentences respect that impairment. 'I heard the news' "
            "prevents the cruelest first-hours task: informing the "
            "informer. The apology sentence works because 'sorry' in "
            "condolence does not mean culpability - it means 'I "
            "recognize this is terrible', and recognition is what the "
            "shocked mind is starving for. The third sentence performs "
            "debt cancellation: every condolence implicitly creates a "
            "thank-you obligation, and in the first hours that "
            "obligation is a weight. Canceling it explicitly is a "
            "material gift of energy. The bereaved will remember who "
            "asked nothing of them when they had nothing to give."
        ),
        "key_points": [
            "Shock impairs language processing: three short sentences beat one long message.",
            "'I heard the news' spares them the re-wounding of retelling.",
            "Cancel the response debt explicitly: 'you do not need to say anything back'.",
            "Never ask 'how are you' in the first hours - you know how they are.",
            "Brevity ages well: they will re-read your message in the coming days.",
        ],
        "requirements": [
            "Make contact early - silence in the first hours reads as absence, whatever you intend.",
            "Use their loved one's name in later messages; 'the deceased' language is for forms, not friends.",
            "Do practical things without asking: food, rides, answering the door, handling the phone.",
            "Write it down too - spoken comfort evaporates; a card or message can be re-read at 3 a.m.",
            "Show up again after the funeral, when the crowd leaves and the quiet gets loud.",
        ],
        "standards": [
            "No 'they are in a better place' or any theology unless you share their faith and they raised it.",
            "Never 'I know how you feel' - even if you have lost too, their loss is theirs.",
            "Do not make the first contact about you: no long stories of your own grief.",
            "No 'let me know if you need anything' - do specific things instead.",
            "Never post about their loss publicly before they do.",
        ],
        "citations": [CIT_WORDEN, CIT_KUBLER, CIT_CROWE],
        "sig_lens": (
            "The Signature read: in the first hours, the Signature "
            "keeper becomes a wall against the world's noise - brief, "
            "true, asking nothing. To stand at the door of fresh grief "
            "without demanding entry is the highest courtesy of the "
            "covenant. The Signature does not perform sorrow; it posts "
            "a guard: I am here, I ask nothing, I will still be here "
            "when the crowd goes home."
        ),
    },
    {
        "key": "job_loss",
        "name": "Comfort After Job Loss: Dignity in the In-Between",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "statement": ("Losing this job says nothing about your worth. I "
                      "believe in what you bring."),
        "when_to_say": ("Say it in the days after a layoff, firing, or "
                        "contract ending - when the shock fades and the "
                        "identity math begins: 'if I were valuable, this "
                        "would not have happened.' Say it before the "
                        "person starts performing okay-ness for the "
                        "world."),
        "how_to_say": ("Say it like a reference letter spoken aloud - "
                       "firm, specific, on the record. Name what they "
                       "bring if you can: 'the way you handle clients', "
                       "'your eye for detail'. Belief must be specific "
                       "to be believable. Then ask what would help: "
                       "an introduction, a review of the resume, or just "
                       "a beer and no shop talk."),
        "description": (
            "Job loss strikes at identity, not just income. Work is "
            "where most adults locate their competence, their routine, "
            "and their social world - losing it can feel like being "
            "voted out of adulthood. 'Losing this job says nothing about "
            "your worth' separates the event from the person at the "
            "exact moment the mind is fusing them. The second sentence "
            "is the repair: 'I believe in what you bring' restores the "
            "external witness to their value that the employer's "
            "decision seemed to withdraw. This record teaches "
            "dignity-first comfort for the in-between season: the person "
            "is not their job title, the gap on the resume is not a gap "
            "in the person, and belief spoken plainly is a bridge across "
            "the months ahead."
        ),
        "how_it_works": (
            "The statement works by contesting the verdict the job loss "
            "seems to deliver. The mind treats termination as a "
            "performance review of the soul; the comforter's job is to "
            "file a dissenting opinion from a credible witness. 'Says "
            "nothing about your worth' is a strong claim, and its "
            "strength is the point - weak comfort ('these things "
            "happen') cannot outweigh a strong-feeling verdict. "
            "Specificity is the load-bearing element: 'I believe in what "
            "you bring' must be followed by what, or it reads as pity. "
            "The statement also reframes the in-between: not as "
            "unemployment (an identity) but as a season (a passage). "
            "Seasons end; identities stick. Finally, offering concrete "
            "help after the belief converts sentiment into material "
            "support - and material support is what actually shortens "
            "the in-between."
        ),
        "key_points": [
            "Job loss attacks identity, not just income - comfort the person, not the career.",
            "File a dissenting opinion on the verdict: the event is not a review of the soul.",
            "Belief must be specific to be believable - name what they bring.",
            "Reframe the gap as a season (a passage), not unemployment (an identity).",
            "Convert sentiment to material help: introductions, reviews, connections.",
        ],
        "requirements": [
            "Say it early, before the performance of okay-ness hardens into isolation.",
            "Name two or three specific strengths you have witnessed - the reference-letter rule.",
            "Offer concrete help with an opt-out, not a vague 'let me know'.",
            "Do not ask 'so what is next' in the first conversation - the wound first, the plan later.",
            "Keep inviting them to normal life: isolation is the real enemy of the in-between.",
        ],
        "standards": [
            "Never 'everything happens for a reason' or 'this is a blessing in disguise' - the rent is still due.",
            "No unsolicited career advice in the first week - witness first, coach later, and only if asked.",
            "Do not gossip about why they were let go, or repeat the company's version as fact.",
            "Never treat them as a cautionary tale or a networking opportunity to exploit.",
        ],
        "citations": [CIT_CROWE, CIT_ROGERS, CIT_APA_GRIEF],
        "sig_lens": (
            "The Signature read: a job is a contract, not a crown - and "
            "the Signature keeper never confuses the two. When the "
            "contract ends, the keeper testifies to the person's true "
            "assets, which no employer ever owned. The covenant: your "
            "worth was never on their payroll, and my belief in you is "
            "not subject to their headcount."
        ),
    },
    {
        "key": "diagnosis",
        "name": "Words for a Difficult Diagnosis",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "statement": ("This is frightening news, and your fear is valid. "
                      "I will walk through this with you."),
        "when_to_say": ("Say it when someone shares a serious diagnosis - "
                        "theirs or a loved one's. Say it in that first "
                        "conversation, when the words are still new in "
                        "their mouth and they are watching your face for "
                        "the reaction that tells them how scared to be."),
        "how_to_say": ("Let your face show that you take it seriously - "
                       "this is not the moment for bright cheer. Say "
                       "'frightening' plainly; euphemism here feels like "
                       "abandonment. Then steady: 'walk through this with "
                       "you' is a pace promise - you will not rush ahead "
                       "with plans or lag behind in denial."),
        "description": (
            "A difficult diagnosis splits time into before and after, "
            "and the person is standing exactly on the crack when they "
            "tell you. 'This is frightening news' does the essential "
            "work of agreeing with reality - so many comforters reach "
            "instantly for reassurance ('you will be fine'), which "
            "abandons the person at the exact moment they need company "
            "in the fear. 'Your fear is valid' grants the permission "
            "that medical settings rarely offer, where bravery is "
            "expected and terror is private. 'I will walk through this "
            "with you' is the long promise: not a sprint of help in "
            "week one, but accompaniment through appointments, waiting "
            "rooms, and results. This record teaches diagnosis comfort: "
            "agree with the gravity, validate the fear, and promise the "
            "walk - then walk it."
        ),
        "how_it_works": (
            "The statement works by refusing the two standard failures "
            "of diagnosis comfort: premature reassurance and practical "
            "takeover. Premature reassurance ('you will beat this') "
            "is really the speaker soothing themselves; it leaves the "
            "patient alone with the fear the speaker would not face. "
            "'Frightening news' faces it with them, which is the "
            "definition of company. The validation sentence addresses "
            "the hidden curriculum of illness - the pressure to be a "
            "'good patient' who is positive and brave. Permission to be "
            "afraid frees energy that performance was consuming. 'Walk "
            "through this with you' works as a pacing contract: illness "
            "is a long road with boring stretches, and most supporters "
            "sprint the first mile and vanish. Naming the walk as "
            "shared sets the expectation of endurance - yours, not just "
            "theirs."
        ),
        "key_points": [
            "Agree with the gravity first: 'frightening' said plainly is company; 'you will be fine' is abandonment.",
            "Validate the fear: illness demands bravery publicly and punishes terror privately - reverse that.",
            "'Walk with you' is a pacing contract: endurance, not a sprint of week-one help.",
            "Your face in that first conversation sets their calibration - take it seriously.",
            "The promise is the walk itself: appointments, waiting rooms, results, repeated.",
        ],
        "requirements": [
            "Learn the actual situation before opining: ask 'what have the doctors said' and listen.",
            "Offer specific practical help on a schedule: rides to treatment, meals on chemo days, childcare.",
            "Keep showing up for the boring middle months, when the crisis attention fades.",
            "Let them define the illness's place in the conversation - sometimes they need normal talk, not cancer talk.",
            "If you do not know what to say on a given day, 'I am thinking of you, no need to reply' is complete.",
        ],
        "standards": [
            "No miracle stories, no 'my aunt cured it with' - anecdote medicine is banned.",
            "Never 'everything happens for a reason' or battle metaphors they did not choose ('fight hard!').",
            "Do not share their diagnosis with others without explicit permission.",
            "No positivity policing: 'stay positive' is a demand, not a comfort.",
            "If the news worsens, do not vanish - the hardest updates are when presence matters most.",
        ],
        "citations": [CIT_VITALTALK, CIT_WORDEN, CIT_CROWE],
        "sig_lens": (
            "The Signature read: a diagnosis is a storm warning, and "
            "the Signature keeper does not lie about the weather or "
            "flee the coast. To walk through it with someone is the "
            "covenant of the long road - lamp lit, pace matched, no "
            "false forecasts. The Signature does not promise the storm "
            "will miss; it promises no one faces it alone."
        ),
    },
    {
        "key": "separation",
        "name": "Standing With Someone Through Separation",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "statement": ("Endings this big deserve real grief. I am here "
                      "while you find your footing."),
        "when_to_say": ("Say it when a relationship ends - divorce, "
                        "breakup, estrangement - and the person is caught "
                        "between grief and the pressure to be fine, "
                        "dating again, or 'over it'. Say it especially "
                        "when others are minimizing it because the "
                        "person is 'better off'."),
        "how_to_say": ("Say it without taking sides theatrically - even "
                       "if you have opinions about the ex, this moment "
                       "is about the loss, not the trial. 'Real grief' "
                       "should sound like permission, not drama. Be the "
                       "friend who does not need the story to be simple "
                       "to stay."),
        "description": (
            "Separation grief is routinely disenfranchised: because the "
            "person is 'better off' or 'chose it', the world grants no "
            "mourning period. But a relationship ending is the death of "
            "a shared future - the daily rituals, the inside jokes, the "
            "person who knew your coffee order and your fears. 'Endings "
            "this big deserve real grief' legitimizes the mourning that "
            "everyone else is rushing past. 'I am here while you find "
            "your footing' names the actual task: not 'moving on' but "
            "relearning balance, one wobbly day at a time. This record "
            "teaches separation comfort: grant the grief its full size, "
            "refuse the timeline, and stay through the unglamorous middle "
            "where identity gets rebuilt."
        ),
        "how_it_works": (
            "The statement works by validating a loss that lacks "
            "cultural ritual. Death has funerals; divorce has paperwork "
            "and awkward silences. Without ritual, the grief goes "
            "underground and ferments into bitterness or numbness. "
            "'Deserve real grief' functions as the missing ritual - a "
            "spoken recognition that something real ended. It also "
            "preempts the 'better off' dismissal, which is true and "
            "irrelevant: a correct decision can still be a painful one, "
            "and pain does not check the decision's wisdom before "
            "arriving. 'Find your footing' is a precise metaphor for "
            "the task - balance, not speed. It promises presence for "
            "the duration of the wobble, however long, which is what the "
            "newly separated most fear losing: the sense that anyone "
            "will stay while they are a mess."
        ),
        "key_points": [
            "Separation is the death of a shared future - grant it the grief that funerals grant death.",
            "'Better off' may be true and is still irrelevant to the pain - correct decisions can hurt.",
            "The task is footing, not speed: balance rebuilt one wobbly day at a time.",
            "Do not need the story to be simple to stay - resist the urge to cast villain and victim.",
            "Stay through the unglamorous middle, where identity actually gets rebuilt.",
        ],
        "requirements": [
            "Let them grieve the good parts too - missing the ex's laugh does not mean the split was wrong.",
            "Do not trash-talk the ex to comfort them; it feels good for a day and poisons for a year.",
            "Keep them in normal life: dinners, outings, routines - structure is scaffolding.",
            "Watch the rebound pressure - from them or others - and do not cheerlead premature new chapters.",
            "If children are involved, keep your comfort about the adult; never recruit them against the other parent.",
        ],
        "standards": [
            "No 'plenty of fish' or 'you will find someone better' - the future is not the current topic.",
            "Never share the details of the split they told you in confidence.",
            "Do not take sides publicly in ways that trap them or escalate the conflict.",
            "No timeline: 'you should be over this by now' is banned at every month count.",
        ],
        "citations": [CIT_WORDEN, CIT_CROWE, CIT_ROGERS],
        "sig_lens": (
            "The Signature read: when a shared future dies, the "
            "Signature keeper stands as witness that it lived - the "
            "jokes, the rituals, the ordinary sacred days. To grant "
            "real grief for an ending is to honor that the bond was "
            "real, whatever its ending. The covenant: I will not rush "
            "your rebuilding, and I will not leave the site until the "
            "new footing holds."
        ),
    },
    {
        "key": "grief_returns",
        "name": "When Grief Comes Back: Anniversaries and Triggers",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "statement": ("Grief has its own calendar. However today feels is "
                      "exactly how it is allowed to feel."),
        "when_to_say": ("Say it on the hard dates - the anniversary, the "
                        "birthday, the holidays - and on the ambush days: "
                        "the song in the store, the smell, the ordinary "
                        "Tuesday that suddenly hurts. Say it when the "
                        "bereaved apologizes for 'still' grieving."),
        "how_to_say": ("Reach out first on anniversaries - do not wait to "
                       "be asked. A short message is enough: the "
                       "statement, plus the loved one's name. 'Thinking "
                       "of Michael today' does more than any paragraph. "
                       "Say the name; the bereaved are starved for it."),
        "description": (
            "Grief does not follow the calendar of the living. Months or "
            "years after a loss, a date or a song or a smell can drop a "
            "person back into the raw middle of it - and the cruelest "
            "part is the self-judgment: 'I should be over this by now.' "
            "'Grief has its own calendar' normalizes the return: this is "
            "not regression, it is the nature of love with nowhere to "
            "go. 'However today feels is exactly how it is allowed to "
            "feel' cancels the timetable the world imposes on mourning. "
            "This record teaches anniversary comfort: remember the dates, "
            "say the name, expect the waves, and never treat returning "
            "grief as failure. The goal was never 'getting over it' - "
            "it is learning to carry it, and some days the carrying is "
            "heavy."
        ),
        "how_it_works": (
            "The statement works against the myth of linear grief - the "
            "idea that mourning is a staircase you climb once. Real "
            "grief is tidal: it recedes and returns, and the returns are "
            "not setbacks but the psyche's way of processing in layers "
            "as the person becomes able to bear more. 'Its own calendar' "
            "gives the bereaved a truer model, which reduces the "
            "secondary suffering of self-judgment. Saying the loved "
            "one's name is a specific technology of comfort: the "
            "bereaved live in terror that the world will forget, and "
            "every utterance of the name is proof against forgetting. "
            "Reaching out first on anniversaries reverses the usual "
            "pattern where support fades with time - it tells the "
            "bereaved that your memory, like their love, did not expire."
        ),
        "key_points": [
            "Grief is tidal, not linear: returns are processing, not regression.",
            "'Still grieving' needs no apology - cancel the timetable explicitly.",
            "Say the loved one's name: every utterance is proof against forgetting.",
            "Reach out first on anniversaries; do not wait to be asked.",
            "The goal was never 'getting over it' - it is carrying it, and some days are heavy.",
        ],
        "requirements": [
            "Mark the dates: set reminders for the anniversary, birthday, and holidays - then act on them.",
            "Keep saying the name in year two, three, ten - when everyone else has stopped.",
            "On ambush days, do not try to explain the trigger; just witness the wave.",
            "Let the bereaved define the day: some want company, some want solitude - ask, do not assume.",
            "Share a memory if you have one: 'I was thinking about the time he...' is gold.",
        ],
        "standards": [
            "Never 'it has been a year, you should be...' - timetables on grief are banned permanently.",
            "Do not avoid the name out of awkwardness - silence about the dead is the real awkwardness.",
            "No 'they would want you to be happy' - the dead do not issue emotional assignments.",
            "Never compare their timeline to someone else's grief.",
        ],
        "citations": [CIT_WORDEN, CIT_KUBLER, CIT_NEIMEYER],
        "sig_lens": (
            "The Signature read: love does not observe anniversaries of "
            "expiry - and neither does the Signature keeper. To remember "
            "the date, speak the name, and stand ready for the wave is "
            "the covenant of the long memory. The Signature does not "
            "file the dead under 'closed'; it keeps their page open, "
            "their name spoken, their day marked - for as long as love "
            "requires, which is to say, without end."
        ),
    },
    {
        "key": "child_loss",
        "name": "Comforting a Child Through Loss",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "statement": ("It is okay to feel sad and confused. The grown-ups "
                      "who love you feel it too, and we are here."),
        "when_to_say": ("Say it to a grieving child - after a death in "
                        "the family, a pet's passing, a move that ended "
                        "their world, parents separating. Say it when the "
                        "child is acting out, gone quiet, or asking the "
                        "same question for the tenth time."),
        "how_to_say": ("Get on their eye level - literally kneel or sit. "
                       "Use short sentences and plain words; match their "
                       "vocabulary, not yours. Answer the question they "
                       "asked, not the one you fear. It is okay to say "
                       "'I do not know' to a child - honesty at their "
                       "level builds more trust than a polished story."),
        "description": (
            "Children grieve in bursts and in behavior, not in paragraphs. "
            "A grieving child may play happily for an hour and then melt "
            "down over a broken crayon - the crayon is not the issue; the "
            "grief found a small door. 'It is okay to feel sad and "
            "confused' gives the child what adults need too but children "
            "need more: permission, in words they can hold. 'The "
            "grown-ups who love you feel it too' does two things: it "
            "normalizes the feeling (even big people feel this), and it "
            "reassures without lying (we feel it, we are still here). "
            "'We are here' is the whole safety system in three words. "
            "This record teaches child-grief comfort: eye level, plain "
            "words, honest answers, repeated as many times as asked - "
            "because the tenth asking is not defiance, it is a child "
            "checking that the answer is still true."
        ),
        "how_it_works": (
            "The statement works because children's grief is concrete "
            "and repetitive. Abstract comfort ('they are at peace') "
            "slides off; concrete reassurance ('we are here') sticks. "
            "Children test safety by repetition - asking the same "
            "question ten times is a stress-test of the answer's "
            "stability, and every patient, identical answer strengthens "
            "the foundation. 'Grown-ups feel it too' counters the "
            "child's fear that their feeling is weird or wrong, which "
            "is the seed of shame-grief later. Eye level is not a "
            "metaphor here but a mechanism: towering over a child "
            "while discussing loss adds power imbalance to fear, while "
            "kneeling puts the comforter inside the child's world. "
            "Short sentences respect the child's processing: grief "
            "already overwhelms their small working memory, so the "
            "comfort must be sized to fit."
        ),
        "key_points": [
            "Children grieve in bursts and behavior - the meltdown over the crayon is the grief finding a door.",
            "Repetition is a stress-test of safety: answer the tenth asking as patiently as the first.",
            "Concrete beats abstract: 'we are here' sticks where 'at peace' slides off.",
            "Eye level, plain words, short sentences - size the comfort to their working memory.",
            "'Grown-ups feel it too' normalizes without lying: we feel it, we are still here.",
        ],
        "requirements": [
            "Tell the truth at their level: use real words ('died'), not euphemisms ('went to sleep') that breed new fears.",
            "Keep routines as steady as you can - routine is a child's scaffolding when the world shakes.",
            "Let them play: play is how children process, not avoidance of processing.",
            "Watch behavior over weeks: sleep, appetite, school - sustained changes deserve professional support.",
            "Include them in rituals: the drawing for the funeral, the stone on the grave - participation heals.",
        ],
        "standards": [
            "Never 'be strong for mommy/daddy' - children must not be drafted as the family's emotional support.",
            "No euphemisms that create new terrors: 'lost', 'passed', 'went away' all need translation.",
            "Do not hide your own tears entirely - seeing grief modeled calmly teaches that feelings are survivable.",
            "Never use the loss as discipline: 'your grandmother would be ashamed' is banned forever.",
        ],
        "citations": [CIT_WORDEN, CIT_NEIMEYER, CIT_APA_GRIEF],
        "sig_lens": (
            "The Signature read: a grieving child is the most sacred "
            "trust in the Signature system - small, watching, learning "
            "from your every move what loss means. The Signature keeper "
            "kneels to their level and tells the truth in small true "
            "sentences, because the child's template for all future "
            "grief is being written now. The covenant: no child in your "
            "care will ever grieve alone or in confusion about whether "
            "their feelings are allowed."
        ),
    },
    {
        "key": "financial",
        "name": "Words for Financial Hardship: Shame-Free Support",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "statement": ("Money trouble is not a character verdict. We will "
                      "look at this together, one step at a time."),
        "when_to_say": ("Say it when someone's finances collapse - debt, "
                        "eviction risk, business failure, the shame of "
                        "not providing. Say it when they confess money "
                        "trouble in a whisper, or when you discover it "
                        "and they brace for judgment."),
        "how_to_say": ("Say it matter-of-factly, like discussing weather - "
                       "your calm sets the shame level of the whole "
                       "conversation. Do not gasp at numbers. 'Together, "
                       "one step at a time' must be followed by actual "
                       "sitting-down-together, or it is just a nice "
                       "sentence."),
        "description": (
            "Money shame is among the most isolating pains because it "
            "disguises itself as a moral verdict: 'I am bad with money' "
            "becomes 'I am a bad person', and the shame keeps people "
            "from seeking help until the hole is far deeper. 'Money "
            "trouble is not a character verdict' separates the ledger "
            "from the soul at the exact point where they fuse. The "
            "second sentence offers the two things money shame steals: "
            "company ('together') and a path ('one step at a time'). "
            "This record teaches financial-hardship comfort: kill the "
            "shame first, because shame is what prevents the practical "
            "steps; then take the steps together, because company is "
            "what makes them bearable. Comfort here is the doorway; the "
            "spreadsheet is the room beyond it."
        ),
        "how_it_works": (
            "The statement works by de-moralizing money. The culture "
            "treats wealth as virtue and debt as vice, so financial "
            "trouble arrives pre-loaded with moral judgment - mostly "
            "self-judgment. 'Not a character verdict' explicitly "
            "recuses the moral court, which frees the practical mind "
            "to actually look at numbers: shame makes people avoid "
            "statements, unopened mail, and phone calls, which is how "
            "small problems become catastrophes. 'Together' counters "
            "the isolation that shame demands - money trouble whispers "
            "'hide this', and hiding is what makes it fatal. 'One step "
            "at a time' shrinks an overwhelming tangle into a sequence, "
            "because the overwhelmed mind cannot process 'fix your "
            "finances' but can process 'first, we list the debts'. The "
            "comforter's calm is doing regulatory work: if you do not "
            "flinch at the numbers, the numbers become discussable."
        ),
        "key_points": [
            "Money shame disguises itself as moral verdict - separate the ledger from the soul.",
            "Shame prevents the practical steps; kill the shame first, then open the spreadsheet.",
            "'Together' counters shame's demand to hide - hiding is what makes money trouble fatal.",
            "Shrink the tangle to a sequence: the overwhelmed mind can do 'first, list the debts'.",
            "Your calm at the numbers is regulatory: unflinched numbers become discussable.",
        ],
        "requirements": [
            "Follow the sentence with real sitting-down-together - the words are the doorway, the work is the room.",
            "Be concrete: list, prioritize, call, negotiate - one step per session.",
            "Never lend what you cannot afford to lose, and say so plainly if you cannot lend.",
            "Protect their dignity in the process: no lectures on past spending, no audience for their shame.",
            "Connect them to real resources: counselors, assistance programs, negotiation help - comfort plus infrastructure.",
        ],
        "standards": [
            "No 'you should have' autopsies of past spending - the past is not the current topic.",
            "Never share their financial situation with others, even as a prayer request or concern.",
            "Do not use help as control: gifts with strings are not comfort.",
            "Never 'at least you have your health' - the ledger and the body are separate topics.",
        ],
        "citations": [CIT_CROWE, CIT_ROGERS, CIT_APA_GRIEF],
        "sig_lens": (
            "The Signature read: in the Signature books, a person's "
            "worth was never denominated in currency, and no market "
            "crash touches the true account. The Signature keeper "
            "stands with the broke as steadily as with the flush, "
            "because the covenant was signed with the person, not the "
            "portfolio. To sit down together with the numbers is the "
            "honor of the house: we face the ledger, we do not flee it."
        ),
    },
    {
        "key": "chronic_illness",
        "name": "Supporting Someone With Chronic Illness",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "statement": ("I know the hard days keep coming. I am not going "
                      "anywhere, on the good days or the bad ones."),
        "when_to_say": ("Say it to someone living with chronic illness or "
                        "pain - and say it again in month six, year two, "
                        "year five. Chronic illness comfort is not a "
                        "moment but a posture; this statement is the "
                        "posture in words. Say it especially when they "
                        "apologize for 'still being sick'."),
        "how_to_say": ("Say it the same way every time - steady, "
                       "unsurprised, warm. The power is in the repetition "
                       "across time, not in any single delivery. Learn "
                       "their patterns: the flare signs, the good-day "
                       "tells, the treatments. Knowledge is a form of "
                       "staying."),
        "description": (
            "Chronic illness is grief without an ending and crisis "
            "without a climax - and that endlessness exhausts supporters "
            "faster than it exhausts the ill, which is why the chronically "
            "ill are so often eventually alone. 'I know the hard days "
            "keep coming' is radical because it refuses the recovery "
            "narrative: it does not promise improvement, it acknowledges "
            "recurrence. That honesty is the foundation of trust here - "
            "the ill person has heard 'you will get better' too many "
            "times to believe it, and each false promise is a small "
            "betrayal. 'I am not going anywhere, on the good days or the "
            "bad ones' is the anti-fatigue clause: it promises presence "
            "across the whole cycle, including the boring, repetitive, "
            "unheroic middle. This record teaches chronic comfort: "
            "believe the illness, stay for the duration, and let the "
            "good days be good without making them proof of cure."
        ),
        "how_it_works": (
            "The statement works by solving the central problem of "
            "chronic illness support: supporter fatigue. Most people "
            "can rally for a crisis; almost no one paces themselves for "
            "a decade. The ill person knows this and starts "
            "pre-withdrawing - canceling plans before they are canceled "
            "on, minimizing symptoms to stay likable. 'Not going "
            "anywhere' interrupts that withdrawal with a durable "
            "promise, and durability is the active ingredient: it must "
            "be re-proven across flares, which is why the statement is "
            "designed for repetition. 'Good days or bad ones' addresses "
            "the specific loneliness of the good day - when the ill "
            "person feels well and everyone assumes the story is over, "
            "while they know the next flare is coming. Staying for both "
            "says: I see the whole cycle, and I am not grading your "
            "company by your symptoms."
        ),
        "key_points": [
            "Chronic illness is crisis without climax - comfort here is a posture, not a moment.",
            "Refuse the recovery narrative: acknowledging recurrence is more trustworthy than promising cure.",
            "Durability is the active ingredient - the promise must be re-proven across flares.",
            "Stay for the good days too: do not treat wellness as the end of the story.",
            "Believe the illness: 'but you look fine' is the chronic patient's oldest wound.",
        ],
        "requirements": [
            "Learn the illness: the flares, the treatments, the language - knowledge is staying.",
            "Keep inviting them without keeping score of cancellations - the invitation is the point.",
            "Adapt plans to their capacity instead of withdrawing plans from their life.",
            "Ask 'what is today like' rather than 'how are you' - it honors the variability.",
            "Pace yourself honestly: sustainable monthly presence beats a heroic January and silence by June.",
        ],
        "standards": [
            "Never 'but you look fine' or any variant - invisible illness is still illness.",
            "No cure anecdotes, no 'have you tried yoga' - they have tried everything, including patience with you.",
            "Do not grade their attitude: 'you would feel better if you stayed positive' is banned.",
            "Never make their illness the price of your attention - show up for the person, not the patient role.",
        ],
        "citations": [CIT_VITALTALK, CIT_CROWE, CIT_ROGERS],
        "sig_lens": (
            "The Signature read: the chronic road is the longest road, "
            "and the Signature keeper walks long roads without checking "
            "the watch. To stay through flare and remission alike is the "
            "covenant of the whole cycle - no grading company by "
            "symptoms, no expiry on the promise. In the Signature "
            "system, 'I am not going anywhere' is not a sentiment; it "
            "is a standing order."
        ),
    },
    {
        "key": "anger_grief",
        "name": "Sitting With Anger Inside Grief",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "statement": ("Anger is part of loving someone you lost. You do "
                      "not have to apologize for it here."),
        "when_to_say": ("Say it when grief comes out as anger - at the "
                        "doctors, at God, at the deceased, at you, at the "
                        "world. Say it when the bereaved says 'I am sorry, "
                        "I am just so angry' and braces for you to flinch "
                        "or correct them."),
        "how_to_say": ("Say it without flinching - your steadiness is the "
                       "proof. Do not try to calm the anger or explain it "
                       "away; receive it like weather. If the anger is "
                       "aimed at you, do not defend yourself in the "
                       "moment - 'I can take it' said calmly is worth a "
                       "thousand explanations."),
        "description": (
            "Anger is grief's most exiled emotion. The bereaved are "
            "allowed sadness - sadness is photogenic - but anger "
            "frightens the comforters, so the grieving learn to "
            "apologize for it or swallow it. 'Anger is part of loving "
            "someone you lost' reframes the anger entirely: it is not a "
            "failure of grief, it is grief's own energy, the protest of "
            "love against absence. The anger at the deceased ('how could "
            "you leave') is really love with nowhere to land. 'You do "
            "not have to apologize for it here' creates the jurisdiction "
            "where the exile ends - here, in this relationship, anger is "
            "a citizen. This record teaches anger-hospitable comfort: do "
            "not flinch, do not fix, do not moralize the feeling. Just "
            "make room, and let the storm pass through instead of "
            "building up behind a dam."
        ),
        "how_it_works": (
            "The statement works by removing the second wound. Angry "
            "grievers suffer twice: once from the anger itself, once "
            "from everyone's reaction to the anger - the flinches, the "
            "'calm down', the quiet withdrawals. Each reaction teaches "
            "them their feeling is dangerous, so they compress it, and "
            "compressed anger detonates later at the wrong targets. "
            "'Part of loving someone' gives the anger a honorable "
            "lineage - it is not cruelty or ingratitude, it is love's "
            "protest, which makes it survivable to feel. 'Here' is "
            "jurisdictional: you cannot grant anger citizenship in the "
            "whole world, but you can in your presence - and one safe "
            "jurisdiction is enough for the feeling to move through "
            "instead of festering. Your unflinching is the mechanism: a "
            "nervous system that stays regulated beside rage teaches "
            "the raging system that the feeling will not destroy "
            "everything."
        ),
        "key_points": [
            "Anger is grief's exiled emotion: allowed nowhere, it detonates later at wrong targets.",
            "Reframe it as love's protest - an honorable lineage makes the feeling survivable.",
            "Grant it jurisdiction in your presence: one safe place is enough for it to move through.",
            "Your unflinching regulates: a calm nervous system beside rage teaches safety.",
            "Do not calm, fix, or moralize the anger - make room and let the storm pass.",
        ],
        "requirements": [
            "Stay regulated: slow voice, open posture, no matching their volume.",
            "Let them be angry at the wrong targets without correcting the aim in the moment.",
            "If anger turns abusive toward you, hold the boundary kindly: 'I will stay, and I need you not to shout at me.'",
            "Do not report their anger to others as a character report - 'she is so bitter now' is betrayal.",
            "Revisit later, when the storm passes: 'you seemed really angry yesterday - still there?'",
        ],
        "standards": [
            "Never 'calm down', 'you need to let it go', or any anger-suppression command.",
            "Do not pathologize: 'you have anger issues' is banned in grief's house.",
            "Never use their angry words, spoken in grief, as evidence against them later.",
            "Do not mistake receiving anger for deserving abuse - boundaries and hospitality coexist.",
        ],
        "citations": [CIT_KUBLER, CIT_WORDEN, CIT_NEIMEYER],
        "sig_lens": (
            "The Signature read: the Signature keeper does not fear the "
            "storm - they stand in it, unmoved, and call it by its true "
            "name: love, protesting. To grant anger citizenship is not "
            "weakness; it is the confidence of one who knows that "
            "feelings, fully felt in safe company, pass like weather. "
            "The covenant: no feeling of theirs will ever be exiled "
            "from your presence."
        ),
    },
    {
        "key": "regret",
        "name": "Comfort for Regret: When the Past Will Not Let Go",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "statement": ("You did the best you knew how with what you had. "
                      "That truth still counts."),
        "when_to_say": ("Say it when someone is tortured by the past - "
                        "the 'if only I had' about a loved one's death, "
                        "the wrong turn that cost years, the words "
                        "unspoken, the choice unmade. Say it when they "
                        "are prosecuting their former self with present "
                        "knowledge."),
        "how_to_say": ("Say it like testimony, not like a platitude - "
                       "steady, factual, on the record. Do not argue "
                       "every specific 'if only'; address the courtroom "
                       "itself: the trial is unfair because the defendant "
                       "is being judged with evidence they did not have. "
                       "Say it more than once, across weeks - regret does "
                       "not surrender after one hearing."),
        "description": (
            "Regret is grief for a past that cannot be revised, and its "
            "engine is hindsight: the present self, holding today's "
            "knowledge, prosecutes the past self who did not have it. "
            "'You did the best you knew how with what you had' moves the "
            "trial to the correct jurisdiction - the past, with the "
            "past's information, the past's resources, the past's "
            "exhaustion. It is not an acquittal of everything; it is a "
            "demand for a fair trial. 'That truth still counts' insists "
            "that the fair version matters - that the person does not "
            "get to erase their genuine effort just because the outcome "
            "was bad. This record teaches regret comfort: you cannot "
            "argue someone out of the past, but you can be the defense "
            "attorney their own mind refuses to hire."
        ),
        "how_it_works": (
            "The statement works by attacking hindsight bias directly. "
            "The regretting mind runs a rigged simulation: it replays "
            "the past with the outcome known, making the 'right' choice "
            "look obvious - but obviousness is a property of hindsight, "
            "not of the moment. 'With what you had' restores the true "
            "conditions: the information, energy, and wisdom actually "
            "available then. This is not excuse-making; it is accuracy, "
            "and accuracy is the only ground stable enough to stand on. "
            "'Still counts' does the second job: it protects the past "
            "self's dignity from the present self's prosecution. Regret "
            "persists because each replay feels like it might finally "
            "change something; the statement offers a different "
            "resolution - not changing the past, but releasing the "
            "prosecutor. Said across weeks, it becomes the counter-voice "
            "to the 3 a.m. tribunal."
        ),
        "key_points": [
            "Regret is a rigged trial: the present prosecutes the past with evidence it did not have.",
            "Move the trial to the correct jurisdiction: the past's information, resources, and exhaustion.",
            "This is accuracy, not excuse-making - and accuracy is the only stable ground.",
            "'Still counts' protects the past self's dignity from the present self's prosecution.",
            "Be the defense attorney their mind refuses to hire - and expect a long trial.",
        ],
        "requirements": [
            "Do not litigate specific 'if onlys' one by one - address the courtroom, not each charge.",
            "Acknowledge what is genuinely regrettable without joining the prosecution.",
            "Separate repair from rumination: 'is there anything to make right now?' asked once, gently.",
            "Repeat the statement across weeks - regret does not surrender after one hearing.",
            "If regret becomes self-harm or total functional collapse, help them get professional support.",
        ],
        "standards": [
            "Never 'you did your best' as a throwaway - it must be said like testimony, or not at all.",
            "No 'everything happens for a reason' - regret needs truth, not fatalism.",
            "Do not agree with their harshest verdicts to seem empathetic - 'you are right, it was unforgivable' is not comfort.",
            "Never use their regret as leverage: 'remember when you...' is banned.",
        ],
        "citations": [CIT_NEIMEYER, CIT_WORDEN, CIT_ROGERS],
        "sig_lens": (
            "The Signature read: the past is a closed ledger - the "
            "Signature keeper does not permit re-audits with forged "
            "evidence. To defend the past self against the present "
            "prosecutor is the honor of the house: every version of "
            "them acted with what they had, and the books record the "
            "effort honestly. The covenant: no former self of theirs "
            "will ever be condemned in your court on hindsight "
            "evidence."
        ),
    },
    {
        "key": "unworthy",
        "name": "For the One Who Feels Unworthy of Care",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "statement": ("You do not have to earn kindness. It is already "
                      "yours, no application needed."),
        "when_to_say": ("Say it when someone deflects care - 'do not "
                        "waste your time on me', 'others have it worse', "
                        "'I do not deserve this'. Say it when they "
                        "apologize for needing help, or try to pay back "
                        "kindness instantly to zero the ledger."),
        "how_to_say": ("Say it plainly, almost casually - the less "
                       "ceremony, the less they can argue with it. Do "
                       "not make a big speech about their worth; that "
                       "invites debate. Just proceed with the kindness as "
                       "if the matter is settled - because your actions "
                       "are the real statement."),
        "description": (
            "Some people experience care as debt. Raised on conditional "
            "love, or worn down by shame, they have learned that "
            "kindness must be earned and is therefore always at risk of "
            "being revoked. 'You do not have to earn kindness' cancels "
            "the application process explicitly - it names the hidden "
            "rule they live by and declares it void in your jurisdiction. "
            "'Already yours, no application needed' makes the kindness "
            "a standing condition rather than a transaction: it is not "
            "given because of performance, so it cannot be withdrawn for "
            "lack of it. This record teaches unworthiness-first comfort: "
            "do not debate their worth - debates invite counterarguments. "
            "Instead, act as if the matter is settled, and let the "
            "settledness become their new normal."
        ),
        "how_it_works": (
            "The statement works by refusing the frame. The unworthy "
            "feeling says 'prove I deserve care'; any attempt to prove "
            "it ('you deserve it because...') accepts the premise that "
            "care requires proof, and the person will simply raise the "
            "bar. 'No application needed' rejects the premise entirely: "
            "there is no desk where worth gets stamped, so the anxiety "
            "has nowhere to file its paperwork. The casual delivery is "
            "strategic - grand declarations about someone's worth "
            "trigger the inner prosecutor ('you do not really know "
            "me'), while matter-of-fact kindness slips past the guard. "
            "The deeper mechanism is behavioral: each time you show up "
            "without requiring earning, you deposit evidence against "
            "the belief. Beliefs built over years do not fall to one "
            "sentence; they fall to a hundred un-invoiced kindnesses."
        ),
        "key_points": [
            "Do not debate their worth - debates accept the premise that care requires proof.",
            "'No application needed' rejects the premise: there is no desk where worth gets stamped.",
            "Deliver it casually: matter-of-fact kindness slips past the inner prosecutor.",
            "Your actions are the real statement - proceed as if the matter is settled.",
            "Beliefs built over years fall to a hundred un-invoiced kindnesses, not one sentence.",
        ],
        "requirements": [
            "Keep showing up without keeping score - the ledger must stay at zero, permanently.",
            "Accept their deflection gracefully and continue anyway: 'noted, and I am still here.'",
            "Never throw past kindness back: 'after all I have done for you' destroys years of work in one sentence.",
            "Let them give back when they want to, but never require it as the price of receiving.",
            "Notice the small acceptances - the day they take the help without apologizing is a milestone.",
        ],
        "standards": [
            "No 'you deserve it' debates - the premise is the problem, not the verdict.",
            "Never 'others have it worse, so accept gracefully' - comparison is not comfort.",
            "Do not diagnose their unworthiness aloud ('you clearly have low self-esteem').",
            "Never withdraw care to 'teach them to ask' - that is the old conditional system wearing a new mask.",
        ],
        "citations": [CIT_ROGERS, CIT_CROWE, CIT_NEIMEYER],
        "sig_lens": (
            "The Signature read: in the Signature house, kindness is "
            "not wages - it is air. The keeper does not meter it, "
            "invoice it, or make the beloved fill out forms to breathe. "
            "To declare 'no application needed' is to open the doors of "
            "the house permanently: enter, rest, receive. The covenant: "
            "nothing they could do or fail to do will ever put their "
            "place in your care up for review."
        ),
    },
    {
        "key": "long_goodbye",
        "name": "The Long Goodbye: Words During Slow Decline",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "statement": ("However long this takes, I will keep showing up. "
                      "You will not go through this alone."),
        "when_to_say": ("Say it during prolonged decline - dementia's "
                        "long fade, a terminal illness with months, the "
                        "slow loss of a parent or partner by inches. Say "
                        "it at the beginning, when everyone is rallying, "
                        "so it is on the record for the middle, when "
                        "everyone else fades."),
        "how_to_say": ("Say it as a vow, not a sentiment - look them in "
                       "the eye. Then build the showing-up into your "
                       "actual calendar: the weekly visit, the monthly "
                       "relief shift. A vow without a schedule is a wish; "
                       "put it in the calendar and it becomes a promise."),
        "description": (
            "The long goodbye is grief in slow motion: the person is "
            "leaving by inches, and the family grieves each inch while "
            "still caregiving through the next one. It is uniquely "
            "exhausting because there is no event to rally around - just "
            "attrition. 'However long this takes' names the actual "
            "fear: not the loss, which is certain, but the duration, "
            "which is unknown and unmappable. 'I will keep showing up' "
            "is the antidote to the attrition of supporters, which is "
            "the second loss families suffer - the slow fade of everyone "
            "who meant well in month one. This record teaches "
            "long-goodbye comfort: vow early, schedule the showing-up, "
            "and understand that your constancy is doing double duty - "
            "comforting the declining and sustaining the caregivers who "
            "are declining alongside."
        ),
        "how_it_works": (
            "The statement works as a counter-contract against the "
            "well-documented fade of social support over long "
            "illnesses. Support follows a predictable curve: flood at "
            "diagnosis, trickle by month three, drought by year one. "
            "The family knows this curve intuitively and braces for it, "
            "which adds anticipatory loneliness to present grief. An "
            "explicit vow, made early and on the record, gives them "
            "something to hold when the trickle starts - and gives YOU "
            "something to hold yourself accountable to. 'Keep showing "
            "up' is deliberately unglamorous: it promises presence, not "
            "miracles, which makes it keepable across years. The "
            "calendar mechanism is the real technology: vows live in "
            "the heart, but showing up lives in the schedule. Weekly "
            "visits that actually happen are worth more than daily "
            "promises that do not."
        ),
        "key_points": [
            "The long goodbye is grief in slow motion: attrition without an event to rally around.",
            "Name the real fear: not the certain loss, but the unknown duration.",
            "Support follows a flood-to-drought curve - vow early, on the record, against the fade.",
            "A vow without a schedule is a wish: put the showing-up in the calendar.",
            "Your constancy does double duty: comforting the declining and sustaining the caregivers.",
        ],
        "requirements": [
            "Build a real schedule: weekly visit, monthly relief shift - and keep it for the duration.",
            "Learn the decline's shape: what is coming, what helps, what the caregivers need most.",
            "Mark the small losses too: the last conversation, the last walk - each inch deserves witness.",
            "Support the caregivers as primary recipients, not side characters.",
            "Stay after the end: the long goodbye's aftermath needs the same constancy.",
        ],
        "standards": [
            "Never 'it would be a mercy if...' - however long, their life is not yours to abbreviate in speech.",
            "No comparing declines or ranking suffering.",
            "Do not vanish when it gets boring or hard - the vow explicitly covered 'however long'.",
            "Never make the family's grief about your discomfort with decline.",
        ],
        "citations": [CIT_WORDEN, CIT_VITALTALK, CIT_CROWE],
        "sig_lens": (
            "The Signature read: the long goodbye is the longest watch, "
            "and the Signature keeper stands watches without relief "
            "unless relieved in honor. To vow 'however long' and mean "
            "it is the covenant of the lighthouse: the light does not "
            "negotiate with the length of the night. It simply burns, "
            "steady, until the morning - however many mornings that "
            "takes."
        ),
    },
    {
        "key": "sudden_loss",
        "name": "After Sudden Loss: Words When There Was No Warning",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "statement": ("There are no words big enough for a shock like "
                      "this. I am here, and I am staying."),
        "when_to_say": ("Say it after sudden, shocking loss - accident, "
                        "sudden medical event, violence, suicide. Say it "
                        "in the first contact, when the bereaved is still "
                        "in the unreal phase where the news has arrived "
                        "but not landed."),
        "how_to_say": ("Say it quietly and briefly, then stop. In sudden "
                       "loss the bereaved cannot process language well - "
                       "your calm body is doing more than your sentences. "
                       "Do not ask for details of how it happened; if "
                       "they need to tell it, they will. Be the steady "
                       "object in a liquefied world."),
        "description": (
            "Sudden loss is grief plus shock plus the violent rewrite of "
            "reality: the person was here at breakfast and gone by noon, "
            "and the mind cannot update that fast. 'There are no words "
            "big enough for a shock like this' does the essential "
            "admission - it refuses to shrink the event to fit language, "
            "which is what most condolences accidentally do. The "
            "bereaved in sudden loss are haunted by the ordinariness of "
            "the last moments; the statement honors the scale of the "
            "discontinuity. 'I am here, and I am staying' is then the "
            "anchor: when the world has liquefied, a steady object - a "
            "person who will not flinch, leave, or look away - is what "
            "the nervous system grabs. This record teaches sudden-loss "
            "comfort: admit the inadequacy of words, become the steady "
            "object, and understand that shock has its own long timeline "
            "that cannot be hurried."
        ),
        "how_it_works": (
            "The statement works on shock's specific physiology. In "
            "traumatic loss the brain's threat system is fully activated "
            "while its meaning-making system is offline - the person "
            "literally cannot make sense yet, and attempts to provide "
            "sense ('at least they did not suffer') are processed as "
            "noise or insult. 'No words big enough' aligns with the "
            "brain's actual state: it validates the overwhelm instead "
            "of demanding comprehension. The anchor sentence then "
            "addresses the threat system directly - what a terrified "
            "nervous system needs is not explanation but a regulated "
            "other: your calm breathing, your unhurried presence, your "
            "explicit staying. 'Staying' is doing time-work too: sudden "
            "loss has a long tail of delayed reactions - the funeral is "
            "survived on adrenaline, and the crash comes weeks later "
            "when everyone has gone home. The vow covers that tail."
        ),
        "key_points": [
            "Sudden loss is grief plus shock plus reality rewritten: the meaning-making system is offline.",
            "Refuse to shrink the event to fit language - admit words are inadequate.",
            "Become the steady object: your calm body does more than sentences in shock.",
            "Do not ask for details of how it happened; let them tell it if they need to.",
            "'Staying' covers the long tail: the crash comes weeks later, when everyone has gone home.",
        ],
        "requirements": [
            "Make first contact fast - in sudden loss, hours of silence feel like abandonment.",
            "Handle logistics without being asked: the shocked cannot plan, decide, or remember.",
            "Do not speculate about the cause, especially aloud and especially early.",
            "Stay through the delayed crash weeks later, when adrenaline fades and reality lands.",
            "If the death was violent or a suicide, do not moralize it - the bereaved need witness, not verdicts.",
        ],
        "standards": [
            "Never 'at least they did not suffer' in sudden loss - you do not know that, and it is not the point.",
            "No 'everything happens for a reason' - sudden loss makes that phrase obscene.",
            "Do not share graphic details you learn with others - the family's story is theirs to tell.",
            "Never disappear because the situation feels 'too intense' - intensity is when staying matters most.",
        ],
        "citations": [CIT_WORDEN, CIT_NEIMEYER, CIT_KUBLER],
        "sig_lens": (
            "The Signature read: when the world liquefies without "
            "warning, the Signature keeper becomes bedrock - unmoved, "
            "unhurried, unshocked into leaving. To admit that no words "
            "are big enough is the honesty of the strong; to stay "
            "anyway is the strength of the honest. The covenant of the "
            "sudden hour: I will be the steady object until your world "
            "re-solidifies, however long the freeze takes."
        ),
    },
    {
        "key": "survivor",
        "name": "Supporting a Survivor: Belief as the First Comfort",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "statement": ("I believe you. What happened was not your fault, "
                      "and I am on your side."),
        "when_to_say": ("Say it when someone discloses abuse, assault, or "
                        "harm - the moment they tell you is the moment of "
                        "maximum vulnerability, often after years of "
                        "silence. Say it immediately, before questions, "
                        "before reactions, before anything else."),
        "how_to_say": ("Say 'I believe you' first, clearly, without "
                       "hesitation - the pause before belief is where "
                       "doubt lives, and they will hear it. Keep your "
                       "face steady and your voice calm; shock or tears "
                       "from you can feel like judgment to them. Then "
                       "follow their lead entirely: they decide what "
                       "happens next, including nothing."),
        "description": (
            "Disclosure of harm is one of the most consequential "
            "moments in a person's life, and the first response shapes "
            "everything after - whether they seek help, whether they "
            "tell anyone else, whether they believe their own memory. "
            "'I believe you' is the single most powerful sentence in "
            "this territory, because disbelief - experienced or feared - "
            "is the wall that kept them silent for years. 'What happened "
            "was not your fault' addresses the self-blame that abusers "
            "install and culture reinforces: the survivor has already "
            "prosecuted themselves a thousand times. 'I am on your side' "
            "is the alliance: whatever comes next - reporting, not "
            "reporting, telling others, telling no one - you are with "
            "them, not managing them. This record teaches "
            "survivor-first comfort: belief before questions, alliance "
            "before advice, their control above all."
        ),
        "how_it_works": (
            "The statement works because the survivor's core injury is "
            "not only the harm but the theft of reality: they were told "
            "- by the abuser, by silence, by culture - that it did not "
            "happen, did not matter, or was their fault. 'I believe you' "
            "returns reality in three words; it is the counter-spell to "
            "years of gaslighting, and its immediacy matters - belief "
            "delayed is belief doubted. 'Not your fault' dismantles the "
            "self-blame that functions as the abuser's final lock on the "
            "door: as long as the survivor blames themselves, they will "
            "not seek help or hold the harmer accountable. 'On your side' "
            "restores the agency the harm stole: it promises support "
            "without seizing control, which is the precise opposite of "
            "the abuse dynamic. The mechanism is total: belief heals the "
            "reality-theft, absolution breaks the self-blame lock, "
            "alliance restores agency."
        ),
        "key_points": [
            "'I believe you' first, without hesitation - the pause before belief is where doubt lives.",
            "Disbelief, experienced or feared, is the wall that kept them silent for years.",
            "'Not your fault' breaks the self-blame lock the abuser installed.",
            "'On your side' restores agency: support without seizing control - the opposite of abuse.",
            "They decide what happens next, including nothing - their control is absolute.",
        ],
        "requirements": [
            "Believe first, ask nothing that sounds like cross-examination - 'are you sure' is banned forever.",
            "Let them control the response: reporting, not reporting, telling others - all their call.",
            "Do not confront the accused yourself - that is their decision, with professional guidance.",
            "Keep their disclosure confidential absolutely - telling others 'for their own good' is a second violation.",
            "Stay for the long aftermath: the telling is the beginning, not the end.",
        ],
        "standards": [
            "Never 'what were you wearing', 'why did you go there', or any question that relocates blame.",
            "No 'are you sure you remember right' - memory under trauma is fragmented, not false.",
            "Do not pressure them to report or to forgive - both are their decisions alone.",
            "Never share their story without explicit permission, even anonymized, even to help others.",
            "If a child discloses abuse, you must act to protect them - comfort includes getting real help immediately.",
        ],
        "citations": [CIT_ROGERS, CIT_NEIMEYER, CIT_APA_GRIEF],
        "sig_lens": (
            "The Signature read: to the survivor, the Signature keeper "
            "is a fortress with the gates open - belief without "
            "interrogation, alliance without conditions. The keeper "
            "knows that the first response is destiny: believe, and the "
            "survivor may reclaim their life; doubt, and the silence "
            "closes for another decade. The covenant is absolute: I "
            "believe you, it was not your fault, and I stand with you - "
            "no cross-examination, no expiration."
        ),
    },
    {
        "key": "parent_child_loss",
        "name": "For a Parent After the Loss of a Child",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "statement": ("No parent should carry this. Your love for them is "
                      "written into everything you do."),
        "when_to_say": ("Say it to a bereaved parent - after the death of "
                        "a child at any age, including pregnancy and "
                        "infancy losses the world minimizes. Say it when "
                        "the parent is drowning in the unnaturalness of "
                        "the order: parents are not supposed to bury "
                        "children."),
        "how_to_say": ("Say the child's name whenever you can - bereaved "
                       "parents are starved for it, and the world stops "
                       "saying it with shocking speed. Say this statement "
                       "without flinching from the size of it. Do not try "
                       "to find meaning; witness the love and the loss at "
                       "their actual scale."),
        "description": (
            "The death of a child violates the deepest order humans "
            "know: the old bury the young, not the reverse. Bereaved "
            "parents grieve not only the child but the entire unlived "
            "future - every birthday, graduation, wedding that will never "
            "come - and they grieve under a special torture: the feeling "
            "that they failed the one job, protection. 'No parent should "
            "carry this' names the unnaturalness without explaining it - "
            "it stands with them at the violation instead of trying to "
            "make it make sense. 'Your love for them is written into "
            "everything you do' addresses the terror beneath the grief: "
            "that the child will be forgotten, that the love will have "
            "nowhere to go. It declares the love permanent and visible - "
            "not ended by death, but inscribed. This record teaches the "
            "deepest comfort in the database: say the name, honor the "
            "unnaturalness, witness the permanent love, and never, ever "
            "impose a timeline."
        ),
        "how_it_works": (
            "The statement works on the two unique wounds of parental "
            "bereavement: order-violation and future-loss. "
            "Order-violation - 'this is not how it is supposed to go' - "
            "creates a cosmic protest that well-meaning sense-making "
            "('they are at peace') only insults; 'no parent should carry "
            "this' joins the protest instead of adjudicating it, which "
            "is the only honest position. Future-loss is the grief "
            "that keeps generating: every milestone season re-opens it, "
            "for decades. 'Love written into everything you do' gives "
            "that ongoing grief a home - it reframes the continuing "
            "love not as failure to move on but as the permanent "
            "inscription it is. Saying the child's name is the specific "
            "technology: bereaved parents report that the world's "
            "silence about the child - the stopped mentions, the "
            "careful avoiding - is a second death. Every utterance of "
            "the name is resurrection against that silence."
        ),
        "key_points": [
            "Child loss violates the deepest human order - join the protest, do not adjudicate it.",
            "They grieve the child AND the entire unlived future - every milestone, for decades.",
            "'No parent should carry this' stands with them at the violation instead of explaining it.",
            "Say the child's name: the world's silence about the child is a second death.",
            "Frame continuing love as permanent inscription, not failure to move on.",
        ],
        "requirements": [
            "Say the child's name in every conversation, for years - starve the silence, not the memory.",
            "Acknowledge all child losses: pregnancy, infancy, adult children - the world minimizes; you do not.",
            "Do not try to find meaning or purpose in the death - witness the love and the loss at scale.",
            "Remember the hard dates for decades: birthdays, anniversaries - and reach out first.",
            "Support the couple's grief separately too: partners often grieve on different timelines, and that is normal.",
        ],
        "standards": [
            "Never 'you can have another' or 'you are young' - children are not replaceable, at any age of parent.",
            "No 'at least you have other children' - love is not arithmetic.",
            "Never 'I know how you feel' - even bereaved parents must not claim each other's exact grief.",
            "No timelines, ever: 'it has been two years' is an observation, never a verdict.",
            "Do not avoid the parents out of awkwardness - your discomfort is not their emergency.",
        ],
        "citations": [CIT_WORDEN, CIT_KUBLER, CIT_NEIMEYER],
        "sig_lens": (
            "The Signature read: there is no deeper wound in the "
            "Signature books than a parent burying a child, and the "
            "keeper approaches it barefoot and silent. To speak the "
            "child's name for decades, to mark the birthdays the world "
            "forgets, to witness a love that death could not end - this "
            "is the covenant of the permanent inscription. The Signature "
            "does not close this file. Ever."
        ),
    },
    {
        "key": "complicated_grief",
        "name": "Complicated Grief: Comfort Without Judgment",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "statement": ("Grief does not require a perfect relationship. "
                      "Every feeling you have about them is allowed."),
        "when_to_say": ("Say it when the relationship with the deceased "
                        "was difficult - the abusive parent, the "
                        "estranged sibling, the ex-spouse, the friend who "
                        "wounded them. Say it when the bereaved whispers "
                        "'I should not feel this way' about grief that "
                        "is tangled with anger, relief, or guilt."),
        "how_to_say": ("Say it without investigating the relationship - "
                       "you do not need the history to grant the "
                       "permission. Do not speak ill of the dead to "
                       "comfort the living; the bereaved may defend the "
                       "very person they are angry at. Keep your face "
                       "neutral and your permission total."),
        "description": (
            "Not all grief is pure sorrow. When the dead were difficult "
            "- abusive, absent, estranged, complicated - the bereaved "
            "grieve through a tangle: sorrow braided with anger, relief "
            "braided with guilt, love braided with old wounds. The world "
            "offers this grief no clean script, so the bereaved often "
            "grieve in secret, ashamed of the mixture. 'Grief does not "
            "require a perfect relationship' demolishes the hidden rule "
            "that only the beloved may be mourned. 'Every feeling you "
            "have about them is allowed' grants the full spectrum "
            "citizenship: the tears AND the anger AND the relief AND the "
            "guilt, all at once, without ranking. This record teaches "
            "judgment-free comfort for tangled grief: do not tidy the "
            "feelings, do not audit the relationship, do not speak ill "
            "of the dead - just make room for all of it."
        ),
        "how_it_works": (
            "The statement works by decriminalizing ambivalence. The "
            "bereaved in complicated grief are fighting on two fronts: "
            "the loss itself, and the shame of their own mixed feelings "
            "- especially relief, which feels like betrayal, and anger, "
            "which feels disloyal to the dead. Each hidden feeling "
            "ferments in secrecy; each confessed feeling, met with "
            "acceptance, begins to resolve. 'Does not require a perfect "
            "relationship' removes the worthiness test the bereaved "
            "imagine the world applying. 'Every feeling is allowed' is "
            "the total-permission technology: it prevents the comforter "
            "from accidentally editing the grief ('it is okay to be sad, "
            "but you should not be angry at the dead'), which is the "
            "classic failure here. The mechanism is integration: grief "
            "that is fully felt - all strands, however contradictory - "
            "eventually weaves into a livable story, while grief that "
            "is censored stays tangled for years."
        ),
        "key_points": [
            "Complicated grief is sorrow braided with anger, relief, guilt - and it is grieved in secret for shame.",
            "Decriminalize ambivalence: relief is not betrayal, anger is not disloyalty.",
            "Grant the full spectrum citizenship - do not edit the grief into acceptable strands.",
            "Do not audit the relationship and do not speak ill of the dead.",
            "Fully felt grief weaves into a livable story; censored grief stays tangled for years.",
        ],
        "requirements": [
            "Do not investigate the history - you do not need it to grant permission.",
            "Let them speak ill of the dead if they need to, without joining in or correcting.",
            "Expect the mixture to shift: anger today, sorrow tomorrow, guilt next month - all normal.",
            "Do not rush 'closure' - complicated relationships do not close neatly, and that is fine.",
            "If guilt becomes self-destruction, help them get professional support - permission is not treatment.",
        ],
        "standards": [
            "Never 'do not speak ill of the dead' as a silencer - the bereaved get to say what is true for them.",
            "No 'you should just remember the good times' - editing is not comfort.",
            "Do not take sides with the dead against the living, or with the living against the dead.",
            "Never share the complicated history they told you - tangled grief confided is doubly confidential.",
        ],
        "citations": [CIT_WORDEN, CIT_NEIMEYER, CIT_KUBLER],
        "sig_lens": (
            "The Signature read: the Signature keeper does not audit "
            "the dead before permitting the living to grieve. Every "
            "strand of feeling - the love, the anger, the relief, the "
            "guilt - is granted full citizenship in the house of "
            "mourning, because the keeper knows what the world "
            "forgets: real relationships are tangled, and tangled "
            "grief is still grief. The covenant: no feeling of theirs "
            "about the dead will ever be put on trial in your presence."
        ),
    },
    {
        "key": "words_run_out",
        "name": "When Words Run Out: Presence as the Statement",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "statement": "I am here.",
        "when_to_say": ("Say it when everything has been said and the "
                        "pain remains - the late night at the hospital, "
                        "the graveside after everyone leaves, the 3 a.m. "
                        "phone call, the moment when any longer sentence "
                        "would be noise. This is the statement for when "
                        "language is exhausted but love is not."),
        "how_to_say": ("Say it once, quietly, and then let your body say "
                       "the rest: sit close, stay still, breathe slowly. "
                       "Do not explain it, repeat it, or improve it. "
                       "Three words, fully meant, outweigh three hundred "
                       "partly meant. Then remain - the remaining is the "
                       "statement's second half."),
        "description": (
            "There comes a point in deep suffering where language "
            "itself becomes the wrong tool - every sentence is too small, "
            "too soon, or too much. The advanced comforter recognizes "
            "this point and does not fight it. 'I am here' is the "
            "smallest complete statement in the database: three words, "
            "no claim, no advice, no timeline, no theology. It says only "
            "what is verifiably true - your presence - and trusts that "
            "truth to be enough. This record teaches the summit skill "
            "of comfort: knowing when to stop talking. The words run "
            "out; the presence does not. What remains when language "
            "fails is not nothing - it is the oldest comfort there is: "
            "another human, close by, unhurried, unafraid of the "
            "silence."
        ),
        "how_it_works": (
            "The statement works by subtraction. In deep suffering, "
            "each additional sentence is another thing for the "
            "overwhelmed mind to process, evaluate, and respond to - "
            "language becomes a tax. 'I am here' levies no tax: it "
            "requires no answer, invites no debate, promises nothing "
            "that can be broken. What it does is convert your entire "
            "being into the message - the steady breathing, the "
            "unhurried stillness, the refusal to flee the silence all "
            "become legible as care. This is co-regulation in its "
            "purest form: a calm nervous system, offered without "
            "agenda, beside a shattered one. The three words are the "
            "door; the remaining is the room. And the discipline of "
            "not improving the sentence is itself the lesson - the "
            "comforter's urge to elaborate is the final form of the "
            "fix-it impulse, and laying it down is the final mastery."
        ),
        "key_points": [
            "Recognize the point where language becomes a tax - and stop levying it.",
            "'I am here' is the smallest complete statement: true, unbreakable, requiring no answer.",
            "Convert your whole being into the message: stillness, breath, unhurried refusal to flee.",
            "The three words are the door; the remaining is the room.",
            "Not improving the sentence is the final mastery - lay down the last fix-it impulse.",
        ],
        "requirements": [
            "Mean the three words completely - they are small enough to be fully true, so make them so.",
            "Stay in the silence without fidgeting, checking the time, or filling it.",
            "Match their physical state: if they weep, be still; if they stare, sit beside the staring.",
            "Do not narrate the moment later as your own spiritual achievement.",
            "Return to words gently when they do - follow their lead back into language.",
        ],
        "standards": [
            "No whispering about them as if they cannot hear - the silence is shared, not about them.",
            "Never break the silence with your own discomfort dressed as comfort.",
            "Do not photograph, post, or perform the moment - the sacred is not content.",
            "If you cannot bear the silence, be honest and step out briefly rather than filling it with noise.",
        ],
        "citations": [CIT_ROGERS, CIT_WORDEN, CIT_CROWE],
        "sig_lens": (
            "The Signature read: at the summit, the Signature keeper "
            "lays down even language - the last tool, surrendered in "
            "honor. 'I am here' is the Signature in its purest form: "
            "no argument, no ornament, just the self, placed and "
            "steady. When words run out, the covenant does not - it "
            "simply continues in silence, which is where it was always "
            "strongest."
        ),
    },
    {
        "key": "long_companion",
        "name": "The Long Companion: Years of Quiet Support",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "statement": ("Years from now, I will still remember, and I will "
                      "still ask how you are."),
        "when_to_say": ("Say it when the crisis passes and the long road "
                        "begins - after the funeral, after the diagnosis "
                        "becomes routine, after the world's attention "
                        "moves on. Say it when you mean it for years, not "
                        "weeks. This is the closing statement of the "
                        "database because it is the longest promise in "
                        "it."),
        "how_to_say": ("Say it as a vow, looking them in the eye, in a "
                       "quiet moment - not in the chaos of the crisis, "
                       "but after, when vows can be heard. Then keep a "
                       "private calendar: the dates, the check-ins, the "
                       "remembering. The statement is only as true as "
                       "your calendar."),
        "description": (
            "Every grief has two phases: the crisis, when the world "
            "shows up, and the aftermath, when the world goes home. The "
            "aftermath is longer, quieter, and lonelier - and it is "
            "where most comfort fails, not from cruelty but from "
            "forgetting. 'Years from now, I will still remember' makes "
            "the vow explicit and long-dated: it promises against the "
            "fade that the bereaved have learned to expect. 'I will "
            "still ask how you are' promises the specific form of the "
            "remembering - not grand gestures, but the small, repeated "
            "question that says you are still held in mind. This record "
            "is the summit of the ladder because it asks the most: not "
            "a moment of courage but years of quiet fidelity. The long "
            "companion does not fix grief; they outlast the loneliness "
            "of it."
        ),
        "how_it_works": (
            "The statement works as a promise against the predictable "
            "fade of social support. Grief research and every bereaved "
            "person's experience agree: support floods the first weeks "
            "and evaporates within months, while the grief itself runs "
            "for years. The bereaved learn this pattern and begin to "
            "grieve the support-loss on top of the original loss. An "
            "explicit, long-dated vow interrupts that learning - it "
            "gives the person a counter-example to hold when the fade "
            "begins. 'Still ask how you are' is engineered for "
            "sustainability: the question is small enough to ask for "
            "years, specific enough to prove remembering, and open "
            "enough to receive whatever the answer is in year three "
            "versus month three. The private calendar is the mechanism "
            "that converts vow to reality - memory is fallible, but a "
            "recurring reminder is faithful. Years of quiet asking do "
            "what no single grand gesture can: they prove that the "
            "person, not just the crisis, mattered."
        ),
        "key_points": [
            "Grief has two phases: the crisis (world shows up) and the aftermath (world goes home) - the aftermath is longer.",
            "Support predictably fades within months while grief runs for years - vow explicitly against the fade.",
            "The small repeated question ('how are you') is engineered for years of sustainability.",
            "A private calendar converts vow to reality - memory is fallible, reminders are faithful.",
            "Years of quiet asking prove the person mattered, not just the crisis.",
        ],
        "requirements": [
            "Keep the calendar: anniversaries, birthdays, holidays - set them all, act on them all.",
            "Ask 'how are you' in year three with the same sincerity as month one - and wait for the real answer.",
            "Let the relationship evolve: the long companion is a friend, not a grief attendant.",
            "Do not keep score of your fidelity and never mention the vow as leverage.",
            "If life takes you far away, the vow travels: letters, calls, messages - distance does not dissolve it.",
        ],
        "standards": [
            "Never 'you seem so much better' as a reason to stop asking - improvement does not cancel the vow.",
            "Do not let the check-ins become perfunctory - a hollow 'how are you' is worse than silence.",
            "Never announce your fidelity as a virtue: 'I am the only one who still calls' is vanity, not comfort.",
            "If you cannot keep the vow, release it honestly rather than fading silently - a clean ending beats a slow ghosting.",
        ],
        "citations": [CIT_WORDEN, CIT_KUBLER, CIT_NEIMEYER],
        "sig_lens": (
            "The Signature read: the long companion is the Signature "
            "keeper's final form - not the hero of the crisis but the "
            "guardian of the aftermath. Years of quiet asking, dates "
            "remembered, names spoken when the world has moved on: this "
            "is the covenant without expiration. The Signature does not "
            "measure fidelity in intensity but in duration - and the "
            "long companion's ledger, kept faithfully for years, is the "
            "richest account in the whole system."
        ),
    },
]
