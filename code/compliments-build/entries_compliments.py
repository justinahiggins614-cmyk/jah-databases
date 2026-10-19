#!/usr/bin/env python3
"""Entries for the Compliments databases (Manon's 16:15 orders, 2026-10-17,
fun/social batch).

Verified 2026-10-17: RAW checks over the full manifest (2,398 databases)
plus every shard index title in jah-databases-data-1 (831 index files):
zero 'compliment*' slugs/names; zero title collisions for all 68 titles
(34 public + 34 Signature Edition) against the whole-system dedupe gate.
ID prefixes JAH-CMPL- (public) and JAH-CMPLS- (signature) verified free:
zero hits in manifest id_prefix values, zero hits in all 831 shard index
files. BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  compliments            - The Compliments Database
                           (public-harvest: genuine compliments for every
                           occasion - character, effort, appearance
                           (tasteful), skills, kindness - each record a
                           compliment WITH delivery guidance: when to say
                           it, how to make it specific and sincere;
                           sincere and kind only - never backhanded, never
                           flirtatious; standard references Dweck Mindset
                           2006, Henderlong and Lepper 2002, Gottman and
                           Silver 1999, Losada and Heaphy 2004, Deci and
                           Ryan 1985, Emmons and McCullough 2003,
                           Fredrickson 2009, Seligman 2011, Grant 2013,
                           Cialdini 2021, Stone and Heen 2014)
  compliments-signature  - The Compliments Signature Database
                           (his original Signature Word of Recognition:
                           every compliment a stamped instrument of the
                           spoken word, recognition the covenant between
                           giver and receiver, sincerity the seal, timing
                           the delivery, and the remembered compliment the
                           kept record; src signature, titles suffixed
                           " (Signature Edition)", never presented as
                           authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present everyday kindness -> deep recognition.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_compliments.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before the pages
are written. Demo scenarios mirror their entries; entry text is
cross-checked against demo outputs.

Screened 2026-10-17: nothing hate-adjacent, profane, or inappropriate; no
religious talk; compliments sincere and kind only.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Word of "
            "Recognition: every compliment a stamped instrument of the "
            "spoken word, recognition the covenant between giver and "
            "receiver, sincerity the seal, timing the delivery, and the "
            "remembered compliment the kept record. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_DWECK = ("Dweck CS. Mindset: The New Psychology of Success. Random "
             "House; 2006.")
CIT_HENDERLONG = ("Henderlong J, Lepper MR. The effects of praise on "
                  "children's intrinsic motivation: a review and synthesis. "
                  "Psychological Bulletin. 2002;128(5):774-795.")
CIT_GOTTMAN = ("Gottman JM, Silver N. The Seven Principles for Making "
               "Marriage Work. Crown; 1999.")
CIT_LOSADA = ("Losada M, Heaphy E. The role of positivity and connectivity "
              "in the performance of business teams: a nonlinear dynamics "
              "model. American Behavioral Scientist. 2004;47(6):740-765.")
CIT_DECI = ("Deci EL, Ryan RM. Intrinsic Motivation and Self-Determination "
            "in Human Behavior. Plenum; 1985.")
CIT_EMMONS = ("Emmons RA, McCullough ME. Counting blessings versus burdens: "
              "an experimental investigation of gratitude and subjective "
              "well-being in daily life. Journal of Personality and Social "
              "Psychology. 2003;84(2):112-127.")
CIT_FREDRICKSON = ("Fredrickson BL. Positivity: Top-Notch Research Reveals "
                   "the 3-to-1 Ratio That Will Change Your Life. Crown; "
                   "2009.")
CIT_SELIGMAN = ("Seligman MEP. Flourish: A Visionary New Understanding of "
                "Happiness and Well-being. Free Press; 2011.")
CIT_GRANT = ("Grant AM. Give and Take: Why Helping Others Drives Our "
             "Success. Viking; 2013.")
CIT_CIALDINI = ("Cialdini RB. Influence: The Psychology of Persuasion. Rev "
                "ed. Harper Business; 2021.")
CIT_STONE = ("Stone D, Heen S. Thanks for the Feedback: The Science and Art "
             "of Receiving Feedback Well. Viking; 2014.")

ENTRIES = [
    {
        "key": "thank_you",
        "name": "Thank You, and I Mean It",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The thank-you is the foundation of every compliment that "
            "follows: a plain, sincere acknowledgment that someone's action "
            "mattered to you. It works because gratitude is specific "
            "recognition - it tells the other person exactly what they did "
            "and what it meant, which is why a real thank-you lands while a "
            "thrown-off thanks barely registers. Research on gratitude "
            "practice shows that naming the benefit concretely is what "
            "turns a pleasantry into something the receiver remembers for "
            "years. This record teaches the anatomy of a thank-you that "
            "counts: the action named, the effect stated, and the feeling "
            "owned. Say it for small things as well as large ones, because "
            "the small thank-yous are the ones most people never hear and "
            "remember longest."
        ),
        "how_it_works": (
            "Say it within the day, while the action is fresh - a "
            "thank-you delivered late reads as an afterthought. Name the "
            "specific action first: not thanks for everything but thanks "
            "for staying late Tuesday to fix the report. Then name the "
            "effect it had on you: it let me walk into the meeting calm "
            "instead of scrambling. Then own the feeling briefly: I am "
            "genuinely grateful. Keep it short; a thank-you that rambles "
            "starts to sound like it is asking for something. Look the "
            "person in the eye or, in writing, use their name and one "
            "concrete detail. Never attach a request to a thank-you - the "
            "moment you add and could you also, the gratitude becomes "
            "currency. For written thanks, one paragraph beats one page."
        ),
        "key_points": [
            "Name the specific action, then the effect it had on you, then the feeling - action, effect, feeling is the whole anatomy of a thank-you that counts.",
            "Deliver it the same day when you can; freshness is what separates a real thank-you from an afterthought.",
            "Thank people for small things too - the small thank-yous are the ones most people never hear and remember the longest.",
            "Never attach a request to a thank-you; the moment you add and could you also, the gratitude turns into currency.",
            "One concrete detail beats ten adjectives - Tuesday, the rain, the extra hour are what make it believable.",
        ],
        "requirements": [
            "The exact action named in plain words, not a vague thanks for everything.",
            "The effect on you stated honestly: what their action changed, spared, or made possible.",
            "Timely delivery - same day when possible, never so late it needs an apology attached.",
            "No request, hint, or follow-up ask riding along with the gratitude.",
            "Eye contact in person, or the person's name plus one concrete detail in writing.",
        ],
        "standards": [
            "Gratitude is stated as the speaker's own feeling (I am grateful), never as a judgment of the receiver's worth.",
            "Specificity is the sincerity test: a thank-you that could be copied to anyone was written for no one.",
            "Written thanks stay brief - one paragraph carries more weight than one page of generalities.",
        ],
        "citations": [CIT_EMMONS, CIT_GRANT, CIT_CIALDINI],
        "sig_lens": (
            "The Signature read: a thank-you is the smallest stamped "
            "instrument in the recognition armory, and it is struck the "
            "same way as the largest - name the deed, name the worth, seal "
            "it with sincerity. Where public practice counts blessings, "
            "the Signature Word files each thank-you as a kept record: "
            "who did what, what it was worth, and when the seal was set."
        ),
    },
    {
        "key": "small_efforts",
        "name": "Noticing Small Efforts",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Most effort in any home, team, or friendship is small and "
            "invisible: the dish washed without being asked, the email "
            "answered at midnight, the extra five minutes of practice. "
            "Noticing small efforts is the compliment of paying attention - "
            "it tells someone that their quiet contributions are seen, "
            "which is the single fastest way to make more of them happen. "
            "Psychology of praise is clearest here: recognition of effort "
            "and process builds the willingness to keep trying, while "
            "silence teaches people that only loud results count. This "
            "record teaches the habit of the daily scan - looking back "
            "over the day for one small effort worth naming - and the "
            "phrasing that keeps it sincere: I noticed you did X, and it "
            "helped."
        ),
        "how_it_works": (
            "Build the habit first: each evening, recall one small effort "
            "someone made that day. Then name it within twenty-four hours, "
            "privately and briefly - small efforts deserve small, warm "
            "recognition, not a ceremony. Use the formula I noticed: I "
            "noticed you wiped down the counters before you left - thank "
            "you. The word noticed is the whole compliment; it proves you "
            "were paying attention. Be truthful about scale: do not call a "
            "small effort heroic, because inflation makes the next "
            "recognition unbelievable. Praise the effort and the process, "
            "not just the outcome - I saw how carefully you went through "
            "it. Rotate who you notice so the same two people do not "
            "collect all the attention."
        ),
        "key_points": [
            "The word noticed is the whole compliment - it proves you were paying attention to effort nobody asked you to watch.",
            "Praise effort and process, not just outcomes; recognition of trying is what builds the willingness to keep trying.",
            "Keep the scale honest: do not call a small effort heroic, because inflation makes the next recognition unbelievable.",
            "Deliver it privately and briefly - small efforts deserve warm recognition, not a ceremony.",
            "Do a daily scan for one small effort worth naming, and rotate who you notice so attention spreads fairly.",
        ],
        "requirements": [
            "A genuine observation - only name efforts you actually saw, never invent one to fill a quota.",
            "The word noticed or saw, stating plainly that their effort registered with you.",
            "Honest scale: the praise matches the size of the effort, with no inflation.",
            "Private, brief delivery within a day of the effort.",
            "Attention to process (how carefully, how steadily) alongside any outcome.",
        ],
        "standards": [
            "Effort praise follows the process-praise finding: recognize strategy, persistence, and care, not fixed traits.",
            "Every claimed observation must be real - a fabricated I noticed destroys trust faster than silence.",
            "Recognition is distributed, not hoarded: the same person is not the only one noticed week after week.",
        ],
        "citations": [CIT_DWECK, CIT_HENDERLONG, CIT_DECI],
        "sig_lens": (
            "The Signature read: small efforts are the loose change of the "
            "covenant economy, and the Signature Word counts every coin. "
            "Where public praise waits for the finished work, the "
            "recognition instrument is struck at the first honest effort - "
            "because the armory keeps records of trying, not just of "
            "triumph."
        ),
    },
    {
        "key": "you_are_kind",
        "name": "You Are a Kind Person",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Telling someone they are kind is a character compliment - it "
            "names who they are, not just what they did. It belongs at the "
            "foundation because kindness is the trait people most hope is "
            "true of them and least often hear confirmed. The compliment "
            "works when it is tied to evidence: you are kind is a slogan, "
            "but the way you sat with her until she stopped crying - you "
            "are a kind person is a verdict the receiver can believe. "
            "Character praise carries more weight than action praise, which "
            "is exactly why it must be earned by something real and "
            "delivered sparingly. This record teaches how to give the "
            "weightiest everyday compliment without making it cheap: "
            "evidence first, trait second, and never as flattery for a "
            "favor."
        ),
        "how_it_works": (
            "Wait for a genuine moment - kindness named without evidence "
            "sounds like flattery. When you see it, describe the moment "
            "first in one sentence: you stayed with her until she stopped "
            "crying. Then draw the trait conclusion: that is who you are - "
            "you are a kind person. Keep your voice matter-of-fact; "
            "character verdicts delivered breathlessly sound performed. Say "
            "it once and let it stand - repeating you are so kind every "
            "week wears the words smooth. Never use it as the setup for a "
            "request, and never say it to someone in the middle of being "
            "unkind in hopes of steering them; the compliment must describe "
            "reality, not negotiate it. In writing, the same structure "
            "holds: the story, then the sentence."
        ),
        "key_points": [
            "Evidence first, trait second: describe the kind moment, then draw the conclusion - the story is what makes the verdict believable.",
            "Deliver it matter-of-factly; a character verdict said breathlessly sounds performed.",
            "Say it once and let it stand - weekly repetition wears the words smooth and cheapens them.",
            "Never use a kindness compliment as the setup for a request or as steering during unkind behavior.",
            "Character praise outweighs action praise, which is exactly why it must be earned by something real.",
        ],
        "requirements": [
            "A real, witnessed kind act as the evidence - never a general impression alone.",
            "The moment described in one concrete sentence before the trait is named.",
            "A calm, matter-of-fact delivery that lets the words carry their own weight.",
            "No request attached and no steering motive behind it.",
            "Sparring use: rare enough that each instance still lands.",
        ],
        "standards": [
            "Trait language is only used when the evidence genuinely supports a pattern or a defining moment, not a single polite gesture.",
            "The compliment describes reality as observed; it is never used to negotiate behavior.",
            "Kindness named must be kindness freely given - obligatory politeness does not qualify.",
        ],
        "citations": [CIT_HENDERLONG, CIT_SELIGMAN, CIT_GRANT],
        "sig_lens": (
            "The Signature read: naming kindness is entering a trait into "
            "the kept record, and the Signature Word enters only what the "
            "evidence proves. Where public speech hands out kind the way "
            "loose change is handed out, the stamped instrument is struck "
            "once, with the deed engraved beside the name."
        ),
    },
    {
        "key": "hello_by_name",
        "name": "Greeting People by Name",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Using someone's name when you greet them is the smallest "
            "compliment in this database and one of the most powerful: it "
            "says you know who they are and that they matter enough to be "
            "remembered. A name is the sound each person answers to most "
            "readily, and hearing it in a greeting turns a generic hello "
            "into personal recognition. This works in every setting - the "
            "workplace hallway, the shop counter, the family kitchen - and "
            "it costs nothing but attention. The skill is not just saying "
            "the name but learning it in the first place: listening when "
            "introduced, repeating it once, and using it within the "
            "conversation. This record teaches name-greeting as a daily "
            "recognition practice, including how to recover gracefully "
            "when a name slips."
        ),
        "how_it_works": (
            "Learn the name deliberately: when introduced, repeat it once "
            "right away - great to meet you, Ana - which both fixes it in "
            "memory and flatters honestly. Use it in the next greeting "
            "within the same day; a name used promptly is a name kept. In "
            "greetings, place it naturally at the start or end - Morning, "
            "Marcus or Good to see you, Priya - not wedged awkwardly "
            "mid-sentence. Use it sparingly in conversation: once per "
            "exchange is recognition, five times is a sales technique. If "
            "a name slips, recover honestly and quickly: I am sorry, your "
            "name has slipped my mind - could you remind me? People forgive "
            "a forgotten name instantly when the asking is sincere, and "
            "they remember that you cared enough to ask. For hard names, "
            "ask about pronunciation once and get it right thereafter."
        ),
        "key_points": [
            "Repeat a new name once at introduction - it fixes the name in memory and gives honest, instant recognition.",
            "Use the name in the next greeting the same day; a name used promptly is a name kept.",
            "Once per exchange is recognition; five times per exchange is a sales technique.",
            "Recover from a slipped name honestly and quickly - people forgive the forgetting when the asking is sincere.",
            "Ask once about a hard pronunciation, then get it right every time after.",
        ],
        "requirements": [
            "The correct name, pronounced as its owner pronounces it.",
            "Natural placement at the start or end of the greeting, never forced mid-sentence.",
            "Restrained frequency: recognition, not repetition.",
            "An honest recovery line ready for the inevitable slip.",
            "Attention at introduction - listening the first time so there is less to recover later.",
        ],
        "standards": [
            "Never guess at a name you do not know; asking is respectful, guessing wrong is not.",
            "Nicknames are only used when the person uses them for themselves.",
            "Name-greeting is offered to everyone, not rationed by rank - the practice is recognition, not networking.",
        ],
        "citations": [CIT_CIALDINI, CIT_GRANT, CIT_DECI],
        "sig_lens": (
            "The Signature read: a name spoken in greeting is the "
            "recognition instrument struck at its simplest setting - the "
            "covenant of knowing. The Signature Word keeps a record of "
            "names because every kept record begins with knowing who "
            "stands before you."
        ),
    },
    {
        "key": "punctuality",
        "name": "Praising Punctuality",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Punctuality is respect made visible: every on-time arrival "
            "says your time matters to me. Praising it is a foundation "
            "compliment because it is fully within the other person's "
            "control, entirely observable, and almost never praised - "
            "people notice lateness instantly and treat punctuality as the "
            "unremarkable default. That asymmetry is the opportunity: the "
            "person who is always on time has been performing a small act "
            "of respect for years, usually in silence. Naming it tells "
            "them the discipline is seen. This record covers praising "
            "punctuality without sounding like a manager with a stopwatch: "
            "warm, brief, and tied to the respect it shows, not the clock "
            "it obeys."
        ),
        "how_it_works": (
            "Praise the pattern, not the single instance - I can always "
            "count on you to be on time lands better than you were on time "
            "today, which can sound surprised. Tie it to respect, not the "
            "clock: you are always on time, and it tells me you respect "
            "everyone's time. Say it privately and briefly; punctuality "
            "praise delivered as a public announcement can embarrass. Do "
            "not praise punctuality in someone who is struggling with it - "
            "a single on-time arrival praised effusively reads as "
            "surprise at low expectations. If you lead a team, praise the "
            "reliable ones by name occasionally so reliability stops being "
            "invisible. And match the compliment yourself: praising "
            "punctuality while arriving late is a joke nobody laughs at."
        ),
        "key_points": [
            "Praise the pattern, not the instance - I can always count on you beats you were on time today, which can sound surprised.",
            "Tie it to respect, not the clock: punctuality is respect made visible.",
            "Deliver it privately and briefly; a public announcement about timeliness can embarrass.",
            "Do not effusively praise a single on-time arrival from someone struggling - it reads as surprise at low expectations.",
            "Match it yourself: praising punctuality while arriving late is a joke nobody laughs at.",
        ],
        "requirements": [
            "An observed pattern of timeliness, not a one-off arrival.",
            "Framing as respect for others time, not obedience to a clock.",
            "Private, brief delivery - a sentence, not a speech.",
            "Expectations kept honest: no inflated praise for basic compliance.",
            "The giver's own punctuality in order, so the words are not undercut.",
        ],
        "standards": [
            "Punctuality praise recognizes discipline freely chosen; it is not a tool for shaming the late.",
            "The compliment never quantifies minutes like a timesheet - warmth, not measurement, is the register.",
            "Cultural differences in time norms are respected; the praise is for reliability within shared expectations.",
        ],
        "citations": [CIT_GRANT, CIT_DECI, CIT_CIALDINI],
        "sig_lens": (
            "The Signature read: punctuality is a covenant kept with the "
            "clock, and the Signature Word honors kept covenants. Where "
            "public speech only ever notices the broken appointment, the "
            "stamped instrument records the hundred kept ones - because "
            "the armory files reliability, not just rescue."
        ),
    },
    {
        "key": "good_question",
        "name": "Praising a Good Question",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A good question is thinking made audible, and praising one is "
            "among the highest-leverage compliments in any classroom, "
            "meeting, or family: it rewards curiosity in front of everyone "
            "watching, which teaches the whole room that asking is safe. "
            "Most people have been trained out of asking by years of "
            "silence or smirks, so the person who asks anyway is doing "
            "something brave. That is a great question does two jobs at "
            "once - it honors the asker and it licenses the next question. "
            "This record teaches how to praise questions without "
            "condescension: name what made it good, answer it fully, and "
            "never praise the question as a way of dodging the answer."
        ),
        "how_it_works": (
            "Respond to the question first with genuine engagement - the "
            "praise must never substitute for an answer. Then name what "
            "made it good, specifically: that is a sharp question because "
            "it catches the assumption we were all making. Keep the "
            "praise to one sentence; a paragraph of praise before the "
            "answer feels like stalling. Say it in front of others when "
            "the question was asked publicly - public questions deserve "
            "public credit, and the room learns that curiosity is safe "
            "here. Never praise a question you then dismiss, and never "
            "use great question as a throat-clearing filler before every "
            "answer; rationed praise is believed, automatic praise is "
            "noise. With children, praise the asking itself - I love that "
            "you asked that - because the habit matters more than any "
            "single question."
        ),
        "key_points": [
            "Answer first, praise second - praise must never substitute for or stall the actual answer.",
            "Name what made it good specifically: it catches the assumption we were all making.",
            "Praise public questions publicly; the room learns that curiosity is safe here.",
            "Never praise a question you then dismiss, and never use great question as automatic filler.",
            "With children, praise the asking itself - the habit matters more than any single question.",
        ],
        "requirements": [
            "A real question with genuine merit - not every utterance earns the label.",
            "A full, respectful answer given before or alongside the praise.",
            "One specific reason the question was good, stated in a sentence.",
            "Public credit for publicly asked questions.",
            "Rationed use: great question said to everything means nothing.",
        ],
        "standards": [
            "Question praise is honest engagement, never a stalling tactic or a dodge.",
            "No question is praised and then mocked; the praise commits the giver to taking it seriously.",
            "Curiosity from any rank or age is eligible - the intern's question gets the same respect as the expert's.",
        ],
        "citations": [CIT_DWECK, CIT_STONE, CIT_DECI],
        "sig_lens": (
            "The Signature read: a good question is an instrument of "
            "discovery being tuned in public, and the Signature Word "
            "recognizes the tuning. Where public rooms reward the person "
            "with the answer, the stamped record honors the person brave "
            "enough to ask - because every kept answer began as an asked "
            "question."
        ),
    },
    {
        "key": "work_in_progress",
        "name": "Acknowledging Hard Work in Progress",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Almost all praise arrives at the finish line, which means the "
            "long middle of any hard effort goes unrecognized - the weeks "
            "of study before the exam, the months of training before the "
            "race, the draft chapters nobody will read. Acknowledging hard "
            "work in progress fills that gap: it tells someone mid-effort "
            "that the work itself is visible and valued, not just the "
            "result. This is process praise at its most practical, and the "
            "research behind it is direct - people persist longer at hard "
            "things when the effort is recognized while it is happening. "
            "The compliment is simple in form: I see how hard you are "
            "working on this. Its power is in the timing: said mid-struggle, "
            "it becomes fuel; said only at the end, it is just a trophy."
        ),
        "how_it_works": (
            "Say it in the middle, not at the end - the whole point is "
            "recognition during the effort. Name what you observe about "
            "the work itself: the early mornings, the careful revisions, "
            "the way they keep going after setbacks. Do not predict the "
            "outcome - you are going to ace it turns recognition into "
            "pressure; instead honor the present: the work you are "
            "putting in is real and it shows. Keep it brief and warm, "
            "then leave them to the work - hovering after praising is "
            "surveillance. If the effort is invisible to most people, say "
            "so: nobody sees these hours but I do. Never praise "
            "in-progress work you have not actually observed; people "
            "mid-effort can smell invented encouragement instantly."
        ),
        "key_points": [
            "Say it in the middle, not at the end - recognition during the effort becomes fuel; at the end it is just a trophy.",
            "Name what you observe about the work itself: early mornings, careful revisions, persistence after setbacks.",
            "Do not predict the outcome - honoring the present effort beats loading it with expectations.",
            "Keep it brief, then leave them to the work; hovering after praising feels like surveillance.",
            "If the effort is invisible to most, say so: nobody sees these hours but I do.",
        ],
        "requirements": [
            "Real observation of the ongoing effort - never invented encouragement.",
            "Mid-effort timing, while the work is still happening.",
            "Specifics about the process: what the effort looks like day to day.",
            "No outcome predictions or pressure attached to the recognition.",
            "Brevity: a warm sentence, then space to keep working.",
        ],
        "standards": [
            "In-progress praise describes the present honestly; it never manufactures optimism about results.",
            "The giver praises only effort actually witnessed - mid-effort people detect invented encouragement instantly.",
            "Recognition of process is kept separate from evaluation of results.",
        ],
        "citations": [CIT_DWECK, CIT_HENDERLONG, CIT_DECI],
        "sig_lens": (
            "The Signature read: work in progress is a covenant still "
            "being written, and the Signature Word reads the draft aloud "
            "with honor. Where public praise waits for the finished "
            "instrument, the stamped record is set mid-forging - because "
            "the armory values the hammering, not just the blade."
        ),
    },
    {
        "key": "calm_under_pressure",
        "name": "Complimenting Calm Under Pressure",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "When everything goes wrong - the system crashes, the deadline "
            "collides, the room panics - the person who stays calm is "
            "performing an act of leadership whether or not they hold any "
            "title. Complimenting calm under pressure names a trait most "
            "people do not know they have until someone reflects it back: "
            "the ability to steady a room by steadying themselves. This "
            "compliment matters because calm is contagious in both "
            "directions, and the calm person rarely gets credit - everyone "
            "remembers the crisis, nobody remembers who kept it from "
            "becoming a catastrophe. Say it after the storm passes, tie it "
            "to the specific moment, and note the effect: when you stayed "
            "level, the rest of us could think."
        ),
        "how_it_works": (
            "Wait until the pressure has passed - praising calm mid-crisis "
            "can sound like commentary from the sidelines. Then name the "
            "specific moment: when the server went down in front of the "
            "client, you did not flinch. Name the effect on others, "
            "because that is the real compliment: your steadiness let the "
            "rest of us think straight. Keep your tone admiring but "
            "matter-of-fact; gushing about someone's calm can make them "
            "feel like a curiosity. Do not add but you must have been "
            "terrified inside - speculating about their inner state "
            "undercuts the compliment. If you were the one panicking, "
            "honesty strengthens it: I was rattled, and watching you stay "
            "level helped me."
        ),
        "key_points": [
            "Wait until the pressure has passed; praising calm mid-crisis sounds like sideline commentary.",
            "Name the specific moment - when the server went down, you did not flinch.",
            "Name the effect on others: your steadiness let the rest of us think straight.",
            "Keep it admiring but matter-of-fact; gushing makes the calm person feel like a curiosity.",
            "Never speculate about their inner state - but you must have been terrified inside undercuts the compliment.",
        ],
        "requirements": [
            "A real high-pressure moment the giver witnessed firsthand.",
            "The specific behavior named: what the calm looked like in action.",
            "The effect on the room or team stated plainly.",
            "Timing after the crisis, not during it.",
            "No speculation about hidden fear or inner turmoil.",
        ],
        "standards": [
            "Calm is praised as observed steadiness, never as the absence of feeling.",
            "The compliment credits the effect on others, not just the personal trait.",
            "It is never used to shame those who did panic - recognition, not comparison.",
        ],
        "citations": [CIT_FREDRICKSON, CIT_SELIGMAN, CIT_GRANT],
        "sig_lens": (
            "The Signature read: calm under pressure is the covenant held "
            "when the storm tests it, and the Signature Word stamps the "
            "kept covenant highest. Where public memory keeps the crisis, "
            "the kept record keeps the steadiness - because the armory "
            "files who held the line, not just who won the day."
        ),
    },
    {
        "key": "thank_publicly",
        "name": "Thanking Someone Publicly",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A private thank-you warms one person; a public thank-you "
            "warms one person and teaches everyone watching what this "
            "group values. Thanking someone publicly - in a meeting, in a "
            "team note, at a family table - multiplies recognition: the "
            "receiver gets the honor of being seen, and the audience gets "
            "a live example of the behavior worth repeating. The risk is "
            "proportional to the reward: done clumsily it embarrasses, "
            "done rarely it looks political, done with specifics it "
            "inspires. This record teaches the public thank-you done "
            "right: brief, specific, about contribution rather than "
            "personality, and closed before it becomes a speech."
        ),
        "how_it_works": (
            "Choose moments that genuinely merit it - weekly public "
            "thanks become background noise. Keep it under thirty seconds "
            "spoken or three sentences written; brevity is what keeps it "
            "from embarrassing. Name the contribution, not just the "
            "person: I want to thank Dana, whose testing caught the bug "
            "before launch. Face the group, not just the person, so it "
            "reads as shared news rather than a private moment staged. "
            "Never surprise someone who hates the spotlight - know your "
            "people, and for the spotlight-shy, praise the work publicly "
            "while thanking them privately. Close cleanly and move on; "
            "lingering turns gratitude into a ceremony. And spread it: if "
            "the same star gets every public thanks, the practice reads "
            "as favoritism."
        ),
        "key_points": [
            "A public thank-you teaches the whole room what the group values - it multiplies recognition.",
            "Keep it under thirty seconds or three sentences; brevity is what keeps it from embarrassing.",
            "Name the contribution, not just the person: whose testing caught the bug before launch.",
            "Know your people: for the spotlight-shy, praise the work publicly and thank them privately.",
            "Spread it around - if the same star gets every public thanks, the practice reads as favoritism.",
        ],
        "requirements": [
            "A contribution genuinely worth public notice, chosen with restraint.",
            "Specific naming of what was done, in a sentence or two.",
            "Brevity: thirty seconds spoken, three sentences written, then done.",
            "Audience awareness - never staging a private moment for unwilling spotlights.",
            "Rotation of honorees so recognition does not read as favoritism.",
        ],
        "standards": [
            "Public thanks honor contribution, never personality, flattery, or politics.",
            "The spotlight-shy are protected: their work may be praised publicly while thanks stay private.",
            "Frequency is rationed so each instance keeps its weight - weekly rituals become noise.",
        ],
        "citations": [CIT_LOSADA, CIT_GRANT, CIT_CIALDINI],
        "sig_lens": (
            "The Signature read: public thanks are the covenant read "
            "aloud before witnesses, and the Signature Word reads them "
            "with the same care as private ones. Where public ritual "
            "risks theater, the stamped instrument stays brief, specific, "
            "and true - because witnesses remember what was real."
        ),
    },
    {
        "key": "consistency",
        "name": "Noticing Consistency",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Consistency is the most under-praised virtue in any human "
            "system: the teammate who delivers every week, the friend who "
            "calls every month, the neighbor who waves every morning. "
            "Because it never spikes and never breaks, it becomes "
            "invisible - and invisible effort eventually asks itself why "
            "it bothers. Noticing consistency is the compliment that "
            "answers that question: you show up, every time, and it "
            "matters. It works because it names the pattern rather than "
            "the incident, which tells the person their reliability is a "
            "known and valued fact, not a lucky streak. Say it "
            "periodically, not constantly - quarterly recognition of "
            "steadiness lands; weekly commentary on it becomes surveillance."
        ),
        "how_it_works": (
            "Name the pattern with its timeframe: you have called every "
            "Sunday for a year - that steadiness means the world to Mom. "
            "The timeframe is the compliment; it proves you have been "
            "paying attention long enough to see the pattern. Deliver it "
            "in a quiet moment, not as a performance review - consistency "
            "praise works best as an aside, warm and brief. Do not attach "
            "it to a request for more: and I hope you keep it up turns "
            "recognition into a leash. If the consistent person is going "
            "through a rough patch, this is the moment the compliment "
            "matters most - steadiness praised during struggle becomes "
            "strength. Avoid comparing them to inconsistent others; the "
            "compliment is about them, not a lesson for someone else."
        ),
        "key_points": [
            "Name the pattern with its timeframe - every Sunday for a year; the timeframe proves you have been paying attention.",
            "Deliver it as a warm aside in a quiet moment, not as a performance review.",
            "Never attach and I hope you keep it up - recognition with a leash attached is not recognition.",
            "Say it during their rough patches too; steadiness praised during struggle becomes strength.",
            "No comparisons to inconsistent others - the compliment is about them, not a lesson for someone else.",
        ],
        "requirements": [
            "A genuine observed pattern over a real timeframe - weeks, months, or years.",
            "The timeframe stated plainly as the proof of attention.",
            "Quiet, warm, brief delivery outside any formal evaluation.",
            "No request for continuation attached.",
            "No comparison to less consistent people.",
        ],
        "standards": [
            "Consistency praise is periodic, not constant - quarterly lands, weekly becomes surveillance.",
            "The pattern claimed must be real and sustained; a month does not make a pattern.",
            "It is never wielded as an indirect rebuke to others.",
        ],
        "citations": [CIT_DECI, CIT_GRANT, CIT_SELIGMAN],
        "sig_lens": (
            "The Signature read: consistency is the covenant renewed daily "
            "without ceremony, and the Signature Word keeps the longest "
            "records for the quietest renewals. Where public eyes chase "
            "the spike, the stamped instrument files the steady line - "
            "because the armory knows the line outlasts the spike."
        ),
    },
    {
        "key": "listening",
        "name": "Praising Good Listening",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Everyone wants to be heard and almost nobody is told they "
            "are good at hearing others. Praising good listening - you "
            "really listened to me - is a foundation compliment with "
            "compounded returns: it rewards the rarest social skill, it "
            "makes the listener more likely to keep listening, and it "
            "models for everyone nearby what attention looks like. Good "
            "listening is observable: the follow-up question that proves "
            "they tracked the story, the remembered detail weeks later, "
            "the absence of interruption. Name those specifics and the "
            "compliment becomes undeniable. This is also one of the safest "
            "compliments in the database - it can be given to anyone, "
            "about anyone, with zero risk of flirtation or favoritism."
        ),
        "how_it_works": (
            "Point to the evidence: you remembered what I told you three "
            "weeks ago - you really listen. Specifics are everything "
            "here, because listening is invisible unless its traces are "
            "named. Say it soon after the listening happened, while the "
            "warmth of being heard is fresh. Keep it simple and direct - "
            "you are a great listener is complete; no elaboration needed. "
            "Say it to people in listening roles especially: the friend "
            "everyone vents to, the manager who holds space, the "
            "grandparent who asks and then actually waits for the answer. "
            "Never praise listening as a consolation prize - at least you "
            "listen - and never follow it by immediately unloading; "
            "praising the listener then exploiting them teaches them to "
            "stop."
        ),
        "key_points": [
            "Point to the evidence: the remembered detail, the follow-up question, the absence of interruption.",
            "Say it soon after the listening, while the warmth of being heard is fresh.",
            "You are a great listener is complete - no elaboration needed.",
            "Praise the habitual listeners especially: the friend everyone vents to, the manager who holds space.",
            "Never praise listening then immediately exploit it; the listener taught to expect unloading will stop listening.",
        ],
        "requirements": [
            "Real evidence of attention: a remembered detail, a tracking question, patience without interruption.",
            "Timely delivery while the experience of being heard is fresh.",
            "Simple, direct phrasing with no backhanded framing.",
            "No immediate unloading after the praise.",
            "Eligibility for everyone - listening praise carries zero risk of favoritism.",
        ],
        "standards": [
            "Listening praise names observable traces of attention, never vague vibes.",
            "It is never a consolation prize (at least you listen) or a prelude to venting.",
            "The compliment stands alone; it asks nothing of the listener in return.",
        ],
        "citations": [CIT_STONE, CIT_GRANT, CIT_DECI],
        "sig_lens": (
            "The Signature read: listening is the covenant of receiving, "
            "and the Signature Word honors the receiver as highly as the "
            "giver. Where public speech prizes the voice, the stamped "
            "instrument records the ear - because every kept word was "
            "first kept by someone who listened."
        ),
    },
    {
        "key": "time_gift",
        "name": "Thanking Someone for Their Time",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Time is the one gift that cannot be re-given, refunded, or "
            "replaced, which makes thanking someone for their time one of "
            "the most honest compliments in the foundation tier. Every "
            "meeting attended, every favor's hour, every long phone call "
            "is a slice of a finite life handed over - and most of it is "
            "taken for granted by everyone except the giver. Naming the "
            "gift - thank you for giving me your afternoon - tells the "
            "person you understand the true price of what they gave. This "
            "compliment is especially powerful upward: thanking a busy "
            "person for their time acknowledges their scarcity honestly, "
            "and thanking anyone for unhurried time honors the rarest "
            "form of attention."
        ),
        "how_it_works": (
            "Name the time given, specifically: thank you for the two "
            "hours, not just thanks for your time. Acknowledge the cost "
            "honestly when you know it: I know how packed your week is, "
            "which makes this afternoon mean more. If the time was "
            "unhurried - no checking the clock, no rushing - say so, "
            "because unhurried attention is the compliment inside the "
            "compliment. Deliver it at the end of the time together, not "
            "days later; the closing moment is when the gift is freshest. "
            "In writing, one line suffices. Never thank someone for "
            "their time while wasting it - the compliment is voided by "
            "the meeting that should have been an email. And when someone "
            "thanks you for your time, accept it simply: it was my "
            "pleasure beats a deflecting no problem."
        ),
        "key_points": [
            "Name the time given specifically - the two hours, not just your time; specificity honors the true price.",
            "Acknowledge the cost when you know it: I know how packed your week is.",
            "If the attention was unhurried, say so - unhurried time is the compliment inside the compliment.",
            "Deliver it at the close of the time together, when the gift is freshest.",
            "Never thank someone for time you then waste; accept such thanks yourself with it was my pleasure.",
        ],
        "requirements": [
            "The actual time given, named in real units - hours, an afternoon, a morning.",
            "Honest acknowledgment of its cost when the giver is busy.",
            "Recognition of unhurried attention when it was given.",
            "Delivery at the natural close of the shared time.",
            "The giver's own respect for time, so the words are not voided by waste.",
        ],
        "standards": [
            "Time thanks are proportional - two hours gets named, two minutes gets a nod, neither gets a speech.",
            "The compliment never serves as an apology for wasting the time it claims to honor.",
            "Gracious acceptance is part of the practice: deflecting thanks teaches people to stop giving time.",
        ],
        "citations": [CIT_GRANT, CIT_EMMONS, CIT_DECI],
        "sig_lens": (
            "The Signature read: given time is the one currency the "
            "armory cannot mint, only receive - and the Signature Word "
            "records every deposit. Where public thanks treat time as "
            "free, the stamped instrument names the hours, because a "
            "covenant measured in irreplaceable hours is the dearest "
            "covenant of all."
        ),
    },
    {
        "key": "craftsmanship",
        "name": "Praising Craftsmanship",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Craftsmanship is care made visible in the work itself: the "
            "joint that fits without filler, the code with no loose ends, "
            "the meal plated like it matters. Praising craftsmanship "
            "differs from praising effort - it honors the standard the "
            "person holds themselves to, not just the hours they spent. "
            "The compliment lands hardest when it names the detail only a "
            "careful eye would catch, because that proves the praise comes "
            "from real looking, not politeness. Look at the dovetails on "
            "this drawer tells a woodworker you actually saw the work. "
            "This record teaches craftsmanship praise as connoisseurship: "
            "specific, knowledgeable, and honest about what excellence "
            "costs the maker."
        ),
        "how_it_works": (
            "Study the work before you speak - craftsmanship praise "
            "without observation is noise to a craftsperson. Name the "
            "specific detail that shows the standard: the seams on this "
            "are invisible, the transitions in this chapter are seamless. "
            "Name the standard it implies: this is the work of someone "
            "who refuses to ship almost-right. If you understand the "
            "craft, say what the detail cost: hand-cutting those takes "
            "patience most people do not have. Deliver it to the maker "
            "directly, not just to the room - craftspeople hear about "
            "their work secondhand too often. Never praise craftsmanship "
            "you cannot see or evaluate; a vague this is amazing to a "
            "master reads as tourist talk. And never follow it with a "
            "discount request - admiring the work then haggling insults "
            "the standard you just praised."
        ),
        "key_points": [
            "Name the detail only a careful eye would catch - that proves the praise comes from real looking, not politeness.",
            "Name the standard it implies: this is the work of someone who refuses to ship almost-right.",
            "If you know the craft, name what the detail cost in skill or patience.",
            "Deliver it to the maker directly; craftspeople hear about their work secondhand too often.",
            "Never admire the work and then haggle - praising the standard then discounting it is an insult.",
        ],
        "requirements": [
            "Actual study of the work before speaking - observation first, praise second.",
            "A named detail that demonstrates the maker's standard.",
            "The implied standard stated: what this level of care says about the maker.",
            "Direct delivery to the craftsperson.",
            "No haggling, discount-seeking, or favor-asking attached.",
        ],
        "standards": [
            "Craftsmanship praise is connoisseurship: specific, knowledgeable, and honest about what excellence costs.",
            "Vague superlatives without observed detail are withheld - tourist talk helps no maker.",
            "The compliment honors the standard, never the price tag or the speed.",
        ],
        "citations": [CIT_DWECK, CIT_DECI, CIT_SELIGMAN],
        "sig_lens": (
            "The Signature read: craftsmanship is the covenant between "
            "maker and work, kept in every invisible joint - and the "
            "Signature Word reads covenants, not surfaces. Where public "
            "praise admires the shine, the stamped instrument names the "
            "dovetail, because the armory files the standard, and the "
            "standard lives in the details."
        ),
    },
    {
        "key": "well_run_meeting",
        "name": "Complimenting a Well-Run Meeting",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Nobody dreams of running meetings, which is exactly why the "
            "person who runs a good one deserves to hear it: a meeting "
            "that starts on time, stays on purpose, hears every voice, "
            "and ends with clear decisions is a genuine skill, performed "
            "weekly for an audience that only notices meetings when they "
            "are terrible. Complimenting a well-run meeting tells the "
            "facilitator that the invisible labor - the agenda, the "
            "timekeeping, the redirecting of tangents, the drawing out of "
            "quiet voices - was seen and valued. Name the mechanics, not "
            "just the vibe: you kept us to the agenda and still made room "
            "for the hard question. Say it and watch meeting quality rise "
            "across the whole team."
        ),
        "how_it_works": (
            "Say it right after the meeting ends, while the good feeling "
            "is fresh - a quick that was a well-run meeting in the "
            "hallway beats a formal note a week later. Name one or two "
            "mechanics: the agenda was tight, you gave everyone airtime, "
            "we left with decisions. Keep it peer-to-peer warm, not "
            "evaluative - you are a colleague, not their reviewer. If you "
            "lead the team, say it in front of the group occasionally; "
            "public credit for facilitation teaches everyone that the "
            "skill is valued here. Do not praise the meeting just because "
            "it was short - brevity without decisions is evasion, not "
            "skill. And if the meeting was good because one difficult "
            "person was managed well, praise the facilitation generally "
            "rather than naming the difficulty."
        ),
        "key_points": [
            "Say it right after adjournment, while the good feeling is fresh - the hallway beats the formal note.",
            "Name the mechanics: the tight agenda, the airtime for quiet voices, the clear decisions at the end.",
            "Keep it peer-to-peer warm, not evaluative; you are a colleague, not their reviewer.",
            "Do not praise mere brevity - a short meeting without decisions is evasion, not skill.",
            "Praise difficult facilitation generally; never name the difficult person who was managed.",
        ],
        "requirements": [
            "A genuinely well-run meeting - agenda, timekeeping, inclusion, decisions.",
            "One or two named mechanics, not just a good vibe.",
            "Prompt delivery, right after the meeting.",
            "Warm peer tone, free of evaluation or condescension.",
            "Discretion about any difficult dynamics that were handled.",
        ],
        "standards": [
            "Meeting praise rewards facilitation skill, never mere shortness or agreeableness.",
            "Public credit is occasional; constant public praise of the facilitator becomes politics.",
            "The compliment is honest - a mediocre meeting praised teaches the team that standards are theater.",
        ],
        "citations": [CIT_LOSADA, CIT_GRANT, CIT_STONE],
        "sig_lens": (
            "The Signature read: a well-run meeting is many covenants "
            "kept in one hour - time, voice, and decision - and the "
            "Signature Word honors the keeper of the hour. Where public "
            "rooms remember only the bad meetings, the stamped record "
            "files the good one, because the armory keeps what works."
        ),
    },
    {
        "key": "courage",
        "name": "Acknowledging Everyday Courage",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Courage is usually pictured as dramatic, but most of it is "
            "quiet: speaking up in the meeting, starting over at forty, "
            "telling the truth when silence would be easier, walking into "
            "the unfamiliar room. Acknowledging everyday courage names "
            "bravery people do not credit themselves with - they call it "
            "just doing what had to be done, and they are usually "
            "understating it. The compliment works by reflecting back the "
            "cost of the act: that took guts, and I want you to know I "
            "saw it. This is a compounded compliment because it requires "
            "judgment - distinguishing real courage from recklessness, "
            "and honoring the fear that was felt alongside the action, "
            "since courage without fear is just temperament."
        ),
        "how_it_works": (
            "Name the act and its cost together: speaking up to the boss "
            "like that took real courage - most of us stayed quiet. The "
            "cost is the compliment; without it, the praise floats. "
            "Acknowledge the fear as part of the bravery, never as its "
            "opposite: I know that was not easy for you makes it braver, "
            "not weaker. Say it privately if the act was costly - public "
            "praise for private bravery can expose. Distinguish courage "
            "from recklessness honestly; praising a reckless act as brave "
            "teaches the wrong lesson. Do not inflate: reserve courage "
            "for acts with real stakes, or the word thins to meaninglessness. "
            "And never use it to push someone toward the next risk - "
            "honoring courage is not recruiting for it."
        ),
        "key_points": [
            "Name the act and its cost together - the cost is the compliment; without it the praise floats.",
            "Honor the fear as part of the bravery: I know that was not easy makes it braver, not weaker.",
            "Say it privately when the act was costly; public praise for private bravery can expose.",
            "Distinguish courage from recklessness honestly; praising recklessness as brave teaches the wrong lesson.",
            "Reserve the word for real stakes, and never use the praise to recruit for the next risk.",
        ],
        "requirements": [
            "A real act with real stakes - cost, risk, or fear genuinely faced.",
            "The cost named alongside the act, plainly and without drama.",
            "Acknowledgment that fear was present and overcome, not absent.",
            "Private delivery when the bravery was personal or costly.",
            "No recruitment: the praise honors the past act, not the next one.",
        ],
        "standards": [
            "Courage is praised only where stakes were real; inflation thins the word to meaninglessness.",
            "Recklessness is never relabeled as bravery, however dramatic the outcome.",
            "The compliment respects the person's own framing - if they call it just doing my job, the praise nods to that humility.",
        ],
        "citations": [CIT_SELIGMAN, CIT_FREDRICKSON, CIT_DECI],
        "sig_lens": (
            "The Signature read: everyday courage is the covenant kept "
            "while afraid, and the Signature Word stamps it among the "
            "highest records. Where public eyes save courage for "
            "battlefields, the kept record files the meeting, the "
            "fresh start, the hard truth - because the armory measures "
            "the fear faced, not the stage."
        ),
    },
    {
        "key": "clear_writing",
        "name": "Praising Clear Writing",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Clear writing is clear thinking made transferable, and it is "
            "rarer than it looks: most professional prose is foggy with "
            "jargon, hedging, and sentences that wander. Praising clear "
            "writing tells the writer that their invisible labor - the "
            "deleting, the restructuring, the choosing of the plain word - "
            "was seen. The compliment is most valuable when it names what "
            "the clarity did for the reader: I understood the whole "
            "proposal in one read, or this email saved us a meeting. "
            "Writers remember specific praise about their craft far longer "
            "than generic nice work, because writing is personal in a way "
            "few work products are. This record teaches praise that "
            "reads the work like an editor: precise, evidence-based, and "
            "encouraging without flattery."
        ),
        "how_it_works": (
            "Quote or point to the specific passage: the second paragraph "
            "explains the tradeoff so cleanly I finally got it. Name the "
            "effect on you as reader - understood in one read, no "
            "follow-up questions needed - because effect is the proof of "
            "clarity. Praise the craft decisions when you can spot them: "
            "the plain words, the short sentences where it counted, the "
            "example before the abstraction. Deliver it in writing when "
            "the work was writing; a reply that quotes the good line "
            "doubles the compliment. Do not praise clarity you did not "
            "experience - skimming then praising is detectable. And keep "
            "it about the writing, not the writer's intelligence; clear "
            "writing praised as smart writing shifts the credit from "
            "craft to talent."
        ),
        "key_points": [
            "Quote the passage: the second paragraph explains the tradeoff so cleanly I finally got it.",
            "Name the effect on you as reader - understood in one read is the proof of clarity.",
            "Praise craft decisions: the plain word chosen, the example placed before the abstraction.",
            "Deliver it in writing when the work was writing; quoting the good line doubles it.",
            "Praise the craft, not the intelligence - clear writing is a skill practiced, not a gift revealed.",
        ],
        "requirements": [
            "The work actually read, not skimmed - praise from real reading only.",
            "A quoted or pointed-to passage as the evidence.",
            "The reader's experience named: what the clarity made possible.",
            "Craft-level specifics where the giver can spot them.",
            "Credit to practice and decision, not to innate talent.",
        ],
        "standards": [
            "Writing praise is editorial: precise and evidence-based, never vague superlatives.",
            "It honors the labor of revision - clarity is recognized as work, not accident.",
            "The compliment addresses the work on the page, not the worth of the author.",
        ],
        "citations": [CIT_DWECK, CIT_STONE, CIT_DECI],
        "sig_lens": (
            "The Signature read: clear writing is thought filed so "
            "another mind can find it, and the Signature Word keeps the "
            "best-filed thoughts highest. Where public praise calls it "
            "talent, the stamped instrument records the deleting and the "
            "restructuring - because the armory files the work, not the "
            "gift."
        ),
    },
    {
        "key": "patience",
        "name": "Complimenting Patience",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Patience is strength at rest: the parent explaining for the "
            "tenth time, the teacher waiting out the silence, the "
            "technician on hold with support for an hour without "
            "bitterness. It is almost never praised because its triumphs "
            "are invisible - nothing happened, nobody exploded, the "
            "difficult thing got done calmly. Complimenting patience makes "
            "the invisible visible: I watched you explain it three times "
            "without a flicker of irritation - that is real patience. The "
            "compliment matters most to people whose patience is "
            "structural to their role - caregivers, teachers, support "
            "workers - because their central virtue is the one least "
            "likely to be named. Say it with admiration, not surprise; "
            "surprise implies you expected them to snap."
        ),
        "how_it_works": (
            "Name the specific trying situation and the calm response: "
            "the line was out the door and you treated every person like "
            "the first. Admire, do not marvel - your patience is remarkable "
            "lands; I do not know how you did not lose it implies you "
            "expected failure. Say it after the trying period, not during; "
            "mid-strain praise can feel like commentary. If their patience "
            "is with you personally - you have explained this to me four "
            "times - own it fully and gratefully, because that is the "
            "hardest patience to acknowledge. Never praise patience that "
            "was actually passivity or fear of conflict; the compliment "
            "must honor chosen calm, not avoidance. And check the tank: "
            "sometimes the kindest follow-up to praising patience is "
            "offering relief."
        ),
        "key_points": [
            "Name the trying situation and the calm response together - the line was out the door and you treated every person like the first.",
            "Admire, do not marvel: your patience is remarkable lands, while I do not know how you did not lose it implies expected failure.",
            "Say it after the strain, not during; mid-strain praise feels like commentary.",
            "When their patience was with you, own it fully - that is the hardest patience to acknowledge.",
            "Honor chosen calm, never passivity; and sometimes the kindest follow-up is offering relief.",
        ],
        "requirements": [
            "A genuinely trying situation met with genuine calm.",
            "The situation and the response both named, specifically.",
            "Admiring tone, free of surprise-at-not-snapping.",
            "Timing after the strain has passed.",
            "Honesty about whose benefit the patience served, especially when it served the giver.",
        ],
        "standards": [
            "Patience praised is chosen calm under real strain - not avoidance, not passivity, not fear of conflict.",
            "The compliment never implies the person was expected to fail.",
            "Structural patience (caregivers, teachers, support workers) is recognized as the central virtue it is.",
        ],
        "citations": [CIT_SELIGMAN, CIT_FREDRICKSON, CIT_GRANT],
        "sig_lens": (
            "The Signature read: patience is the covenant held at rest, "
            "strength refusing to become force - and the Signature Word "
            "files it among the disciplines. Where public eyes miss what "
            "did not explode, the stamped record keeps the calm hour, "
            "because the armory knows the battle not fought is also a "
            "victory."
        ),
    },
    {
        "key": "tasteful_appearance",
        "name": "Tasteful Appearance Compliments",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Appearance compliments are the highest-risk category in this "
            "database, which is why they have their own record and their "
            "own rules. Done right, they are lovely: noticing the care "
            "someone put into how they present themselves honors effort "
            "and choice. Done wrong, they embarrass, objectify, or "
            "harass. The bright line is choice versus body: compliment "
            "what they chose - the color, the cut, the craftsmanship, the "
            "coordination - never the body underneath. That jacket is a "
            "great color on you is safe; anything about the body wearing "
            "it is not. This record teaches the safe harbor: specific, "
            "choice-focused, brief, peer-appropriate, and never repeated "
            "to the same person until it becomes attention."
        ),
        "how_it_works": (
            "Compliment the choice, never the body: the color, the style, "
            "the way it is put together. Keep it to one sentence and move "
            "on - lingering turns a compliment into scrutiny. Match the "
            "relationship: warm appearance praise belongs between peers "
            "and friends; from a manager to a report, keep it rare, "
            "brief, and strictly about professional presentation. Never "
            "comment on weight, shape, age markers, or anything the "
            "person did not choose. Never repeat appearance compliments "
            "to the same person regularly - frequency converts "
            "compliment to attention, and attention to discomfort. If in "
            "doubt, compliment the effort behind the appearance instead: "
            "you always look so put-together, or redirect to something "
            "safer entirely. And accept gracefully when you receive one: "
            "thank you is complete."
        ),
        "key_points": [
            "Compliment the choice, never the body: the color, the cut, the coordination - never what is underneath.",
            "One sentence, then move on; lingering turns a compliment into scrutiny.",
            "Match the relationship: peer warmth is fine, manager-to-report stays rare, brief, and professional.",
            "Never comment on weight, shape, age, or anything unchosen - and never repeat it to the same person regularly.",
            "When in doubt, praise the effort behind the look, or choose a safer compliment entirely.",
        ],
        "requirements": [
            "Focus strictly on chosen elements: color, style, fit, coordination, craftsmanship.",
            "One-sentence brevity with a clean exit - no lingering.",
            "Relationship-appropriate warmth and frequency.",
            "Zero commentary on body, weight, age, or unchosen traits.",
            "No repetition that converts compliment into attention.",
        ],
        "standards": [
            "The choice-versus-body line is absolute: anything about the body is out, however positively meant.",
            "Power differences tighten the rules - the higher the giver's rank, the briefer and rarer the compliment.",
            "If there is any doubt about reception, the compliment is withheld or redirected - safety over charm.",
        ],
        "citations": [CIT_CIALDINI, CIT_STONE, CIT_DECI],
        "sig_lens": (
            "The Signature read: tasteful appearance praise honors the "
            "care a person takes with their own presentation - the "
            "covenant of showing up well - and the Signature Word keeps "
            "it at exactly that. Where careless speech crosses the line "
            "into the body, the stamped instrument stops at the choice, "
            "because the armory records effort, never exposure."
        ),
    },
    {
        "key": "mentorship",
        "name": "Praising a Good Mentor",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A good mentor changes the trajectory of a life and then "
            "usually downplays it: oh, you did the work yourself. Praising "
            "a good mentor corrects the record - it tells them that their "
            "guidance was not just helpful but formative, and it does so "
            "while the mentor can still hear it. The most powerful mentor "
            "praise is specific about the turning point: when you told me "
            "to apply anyway, that changed everything. This compliment "
            "compounds over time because mentors rarely learn their "
            "impact; they plant and walk away, and most never see the "
            "harvest. Telling them - years later, out of the blue - is "
            "one of the highest-return messages a person can send. This "
            "record covers both the timely thanks and the long-delayed "
            "letter that arrives like sunlight."
        ),
        "how_it_works": (
            "Name the turning point: the specific advice, introduction, "
            "or belief they offered that changed your path. Describe the "
            "before and after briefly - I was ready to quit, and your "
            "words kept me in - because the contrast is the compliment. "
            "Credit their judgment, not just their kindness: you saw "
            "something in me before I saw it. Say it directly to them "
            "whenever possible; secondhand praise of mentors evaporates. "
            "The long-delayed message is not awkward - I have been meaning "
            "to tell you for years is a perfect opening, and mentors "
            "treasure these above all. If you now mentor others because "
            "of them, say so: your influence is multiplying. Never praise "
            "a mentor while asking for another favor; let the gratitude "
            "stand unaccompanied."
        ),
        "key_points": [
            "Name the turning point: the specific advice or belief that changed your path.",
            "Describe the before and after briefly - the contrast is the compliment.",
            "Credit their judgment, not just their kindness: you saw something in me before I saw it.",
            "The long-delayed message is never awkward - I have been meaning to tell you for years is a perfect opening.",
            "If you now mentor others because of them, say so: your influence is multiplying.",
        ],
        "requirements": [
            "A specific turning point or sustained guidance, named concretely.",
            "The before-and-after stated briefly and honestly.",
            "Credit to the mentor's judgment and belief, not only their time.",
            "Direct delivery to the mentor whenever possible.",
            "No accompanying request - the gratitude stands alone.",
        ],
        "standards": [
            "Mentor praise corrects the record honestly; it never invents influence that was not there.",
            "The long-delayed thanks is treated as timely - impact recognized late is still recognized.",
            "It distinguishes mentorship from mere supervision: guidance that changed trajectory, not just assigned tasks.",
        ],
        "citations": [CIT_GRANT, CIT_DWECK, CIT_SELIGMAN],
        "sig_lens": (
            "The Signature read: a mentor plants covenants in other "
            "people's futures and walks away before the harvest - and the "
            "Signature Word returns to the planter with the yield "
            "counted. Where public memory forgets the guide, the stamped "
            "record files the turning point, because the armory keeps the "
            "lineage of every instrument it holds."
        ),
    },
    {
        "key": "integrity",
        "name": "Complimenting Integrity",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Integrity is doing the right thing when nobody is watching, "
            "which creates a paradox for praise: the finest examples are "
            "the ones nobody saw. Complimenting integrity therefore "
            "usually happens at the moments it becomes visible - the "
            "returned wallet, the admitted mistake, the refused shortcut, "
            "the credit shared upward. Naming it matters because integrity "
            "is expensive: every honest choice forgoes something easier, "
            "and the person paying that price deserves to know the price "
            "is seen. You did the hard right thing when the easy wrong "
            "thing was right there is a compliment about character at "
            "full weight. This record teaches integrity praise that "
            "honors the cost without moralizing - admiration, not a sermon."
        ),
        "how_it_works": (
            "Name the choice and what it cost: you told the client about "
            "the error before they found it, knowing it would cost us the "
            "week. The cost named is what makes it integrity rather than "
            "luck. Keep the tone admiring and plain - that took real "
            "character - not preachy; nobody wants their honesty turned "
            "into a lecture. Say it soon after the act, while the "
            "alternative was still tempting in memory. If you benefited "
            "from their integrity, say so honestly: your honesty saved me "
            "too. Never praise integrity as a surprise - I did not think "
            "you had it in you - and never use it to set them up as the "
            "designated conscience of the group; the compliment honors, "
            "it does not conscript."
        ),
        "key_points": [
            "Name the choice and what it cost - the cost named is what makes it integrity rather than luck.",
            "Keep it admiring and plain, never preachy; nobody wants honesty turned into a lecture.",
            "Say it soon after, while the tempting alternative is still fresh in memory.",
            "If you benefited from their integrity, say so honestly: your honesty saved me too.",
            "Honor, do not conscript: never make them the designated conscience of the group.",
        ],
        "requirements": [
            "A real honest choice with a real cost or temptation, witnessed or reliably known.",
            "The choice and its cost both named, plainly.",
            "Admiring, non-moralizing tone.",
            "Prompt delivery after the act.",
            "No surprise framing and no conscription into a conscience role.",
        ],
        "standards": [
            "Integrity praise honors the cost paid, never the ease of the choice.",
            "It is admiration, not a sermon - the giver does not preach from the compliment.",
            "The compliment never becomes a leash: honored integrity is not assigned future integrity.",
        ],
        "citations": [CIT_DECI, CIT_SELIGMAN, CIT_GRANT],
        "sig_lens": (
            "The Signature read: integrity is the covenant kept in the "
            "dark, and the Signature Word stamps the dark-kept covenant "
            "as the truest of all. Where public praise needs an audience, "
            "the kept record needs only the deed - because the armory "
            "files what was done unseen as the highest proof."
        ),
    },
    {
        "key": "unseen_work",
        "name": "Recognizing Behind-the-Scenes Work",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Every smooth operation runs on invisible labor: the setup "
            "before the event, the cleanup after, the prep nobody "
            "applauds, the maintenance that prevents the crisis nobody "
            "hears about. Recognizing behind-the-scenes work is the "
            "compliment of looking where the lights do not point. It "
            "matters disproportionately because invisible workers develop "
            "a quiet theory that nobody notices - and one specific "
            "recognition can retire that theory for years. The trick is "
            "knowing the work exists: ask what had to happen for this to "
            "look easy, then praise what you learn. Nobody saw the three "
            "hours of prep, but I know, and it showed is a compliment "
            "the spotlight never delivers."
        ),
        "how_it_works": (
            "Find the invisible work first: ask, notice, or simply think "
            "about what had to happen for this to look effortless. Name "
            "it concretely: the room was set, the materials were ready, "
            "the follow-ups were already sent. Deliver it directly to the "
            "worker, not just about them to others - the point is that "
            "they hear it. Acknowledge the asymmetry honestly: nobody "
            "claps for setup, so I am saying it - this does not run "
            "without you. If you have any power to make the invisible "
            "visible - a mention in the meeting, a line in the report - "
            "use it; structural recognition beats private thanks for "
            "systemic invisibility. Do not praise behind-the-scenes work "
            "and then keep the worker behind the scenes by design; "
            "sometimes the compliment should come with a spotlight."
        ),
        "key_points": [
            "Look where the lights do not point: ask what had to happen for this to look easy, then praise it.",
            "Deliver it directly to the worker - the point is that they hear it, not just that others do.",
            "Name the asymmetry honestly: nobody claps for setup, so I am saying it.",
            "Use any power you have to make the invisible structurally visible - a mention, a line in the report.",
            "Do not praise the behind-the-scenes worker while keeping them there by design; sometimes add a spotlight.",
        ],
        "requirements": [
            "Real knowledge of the invisible work - found by asking or noticing, never assumed.",
            "Concrete naming of what was done out of sight.",
            "Direct delivery to the person who did it.",
            "Honest acknowledgment that the work usually goes unrecognized.",
            "Structural visibility where the giver has the power to grant it.",
        ],
        "standards": [
            "Invisible-work praise is investigative: the giver does the work of finding the work.",
            "It never romanticizes invisibility - being unseen is a condition to fix, not a virtue to praise.",
            "Credit is given where the lights do not point, without moving the worker into an unwanted spotlight.",
        ],
        "citations": [CIT_GRANT, CIT_LOSADA, CIT_DECI],
        "sig_lens": (
            "The Signature read: behind-the-scenes work is the covenant "
            "kept in the darkroom where the instruments are made - and "
            "the Signature Word develops that film. Where public applause "
            "follows the spotlight, the stamped record follows the "
            "setup crew, because the armory knows every polished "
            "instrument was finished by unseen hands."
        ),
    },
    {
        "key": "problem_solving",
        "name": "Praising Problem Solving",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Problem solving is the skill of turning stuck into moving, "
            "and praising it well means praising the thinking, not just "
            "the solution. Anyone can admire the answer; the compliment "
            "with weight names the move: the way you reframed it, the "
            "question that cracked it, the patience to test instead of "
            "guess. This matters because problem solvers are often "
            "valued only for outcomes - fix it - while the reasoning that "
            "makes them reliable goes unremarked. Praising the method "
            "teaches everyone watching how to think, and it tells the "
            "solver their mind is seen, not just their output. The "
            "record's rule: admire the path, honor the persistence, and "
            "name the specific intellectual move."
        ),
        "how_it_works": (
            "Name the specific move: the way you isolated it to the "
            "timing issue instead of rewriting everything - that was "
            "sharp. Praise the method alongside the result: both the "
            "answer and how you got there. If the solving involved "
            "persistence through dead ends, honor that too - most people "
            "quit at the second dead end, you mapped all five. Ask them "
            "to walk through it when others are present; public "
            "narration of good thinking is praise plus teaching. Do not "
            "praise the solution while ignoring a messy process that "
            "caused the problem - honesty keeps the compliment credible. "
            "And credit collaborators by name if the solving was shared; "
            "nothing poisons praise like a stolen share of it."
        ),
        "key_points": [
            "Name the specific intellectual move: the reframe, the isolating question, the test instead of the guess.",
            "Praise the method alongside the result - the path is the repeatable part.",
            "Honor persistence through dead ends: most quit at the second, you mapped all five.",
            "Ask them to walk through it publicly; narration of good thinking is praise plus teaching.",
            "Credit collaborators by name; nothing poisons praise like a stolen share.",
        ],
        "requirements": [
            "A real solved problem with a real observed or explained method.",
            "The specific thinking move named, not just the answer admired.",
            "Recognition of persistence through the dead ends where it occurred.",
            "Honesty about the process - no praising outcomes built on ignored messes.",
            "Shared credit distributed by name when the solving was joint.",
        ],
        "standards": [
            "Problem-solving praise is intellectual: it addresses the reasoning, not just the result.",
            "The method praised must be sound - cleverness that caused the problem is not praised as solving it.",
            "Teaching is part of the honor: good thinking narrated helps the whole room.",
        ],
        "citations": [CIT_DWECK, CIT_DECI, CIT_STONE],
        "sig_lens": (
            "The Signature read: problem solving is the instrument "
            "tuning itself mid-performance, and the Signature Word "
            "records the tuning, not just the note. Where public praise "
            "buys the answer, the stamped record files the method - "
            "because the armory keeps repeatable instruments, not lucky "
            "ones."
        ),
    },
    {
        "key": "humor",
        "name": "Complimenting Humor That Lifts a Room",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Humor that lifts a room is a social skill of the highest "
            "order: reading tension, timing the release, and giving "
            "everyone permission to breathe. It is almost never praised "
            "as a skill - funny people get laughs, which feels like "
            "reward enough, but the craft behind the laugh goes "
            "unnamed. Complimenting it tells the person their humor is "
            "not just entertainment but care: you knew exactly when we "
            "needed that. The line to hold is kind humor only - wit that "
            "lifts versus wit that targets. This record praises the "
            "lifters: the ones whose jokes leave everyone, including the "
            "butt of nothing, feeling better."
        ),
        "how_it_works": (
            "Name the moment and the shift: when the budget news landed, "
            "your joke broke the tension and we could think again. Praise "
            "the timing and the reading of the room, not just the joke - "
            "the skill is knowing when, not just being funny. Keep it to "
            "kind humor strictly; never praise wit that targeted someone, "
            "however clever, because that teaches the wrong craft. Say it "
            "afterward, privately or lightly - humor praised too "
            "solemnly embarrasses the funny. If their humor regularly "
            "carries the team through hard weeks, say that plainly: you "
            "keep this team's spirits up and we notice. Do not try to "
            "top their joke in the same breath; the compliment is the "
            "gift, not an opening for your set."
        ),
        "key_points": [
            "Name the moment and the shift: your joke broke the tension and we could think again.",
            "Praise the timing and the reading of the room - the skill is knowing when, not just being funny.",
            "Kind humor only: never praise wit that targeted someone, however clever.",
            "Say it afterward and lightly; humor praised too solemnly embarrasses the funny.",
            "Do not top their joke in the same breath - the compliment is the gift, not your opening.",
        ],
        "requirements": [
            "Humor that lifted rather than targeted - kind wit only.",
            "The specific moment and the emotional shift it caused, both named.",
            "Praise for timing and social reading, not just funniness.",
            "Light, warm delivery after the moment.",
            "No piggybacking jokes and no praise for humor at someone's expense.",
        ],
        "standards": [
            "Only lifting humor is eligible - wit that wounds is never praised, however brilliant.",
            "The compliment addresses the social skill (reading the room, timing relief), not mere joke inventory.",
            "It is given without performing in return; the giver does not compete with the praised.",
        ],
        "citations": [CIT_FREDRICKSON, CIT_SELIGMAN, CIT_GRANT],
        "sig_lens": (
            "The Signature read: lifting humor is the instrument that "
            "tunes the whole room at once, and the Signature Word "
            "records the tuning. Where public laughter spends itself "
            "and is gone, the stamped record keeps the moment the "
            "tension broke - because the armory files what steadied the "
            "many, not just the witty few."
        ),
    },
    {
        "key": "comeback",
        "name": "Praising a Comeback From a Mistake",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Everyone makes mistakes; the rare thing is the comeback - "
            "owning it fully, fixing what can be fixed, learning visibly, "
            "and returning stronger without bitterness or excuse. Praising "
            "a comeback is delicate because it must honor the recovery "
            "without celebrating the error or reopening the wound. The "
            "formula is forward-looking: the way you owned that, fixed "
            "it, and came back better - that is character. This "
            "compliment matters enormously because most people, after "
            "failing publicly, brace for permanent judgment; being "
            "recognized for the recovery instead teaches them - and "
            "everyone watching - that mistakes are chapters, not verdicts."
        ),
        "how_it_works": (
            "Wait until the recovery is real - praising a comeback "
            "mid-collapse is premature and can sound like consolation. "
            "Name the three beats: the owning, the fixing, the return - "
            "you owned it, you fixed it, you came back better. Keep the "
            "mistake itself undescribed; everyone knows what happened, "
            "and relitigating it reopens the wound. Praise the response, "
            "never the error - that failure taught you well is still "
            "about the failure; focus on the character shown after. Say "
            "it privately for serious mistakes, publicly for small ones "
            "where the lesson helps the room. Never use it to claim "
            "credit for their growth - I always knew you would - and "
            "never hold the old mistake over them later; the compliment "
            "is a closed chapter."
        ),
        "key_points": [
            "Wait until the recovery is real; praising a comeback mid-collapse sounds like consolation.",
            "Name the three beats: the owning, the fixing, the return - you owned it, you fixed it, you came back better.",
            "Leave the mistake undescribed; relitigating it reopens the wound.",
            "Praise the response, never the error; focus on the character shown after.",
            "Never claim credit for their growth, and never hold the old mistake over them later.",
        ],
        "requirements": [
            "A genuine recovery: owned, addressed, and visibly learned from.",
            "The three beats named - owning, fixing, returning - without describing the error.",
            "Forward-looking framing: character shown, not failure analyzed.",
            "Private delivery for serious mistakes; public only when the lesson serves the room.",
            "The chapter stays closed afterward - no later weaponizing of the old mistake.",
        ],
        "standards": [
            "Comeback praise honors recovery, never the error - the mistake is not relitigated or romanticized.",
            "Timing respects the wound: only genuine recovery, never mid-collapse consolation.",
            "The compliment is a closed chapter; the giver does not reopen it later for leverage.",
        ],
        "citations": [CIT_DWECK, CIT_STONE, CIT_SELIGMAN],
        "sig_lens": (
            "The Signature read: a comeback is the covenant re-forged "
            "after breaking - and the Signature Word holds that "
            "re-forging is stronger than the original casting. Where "
            "public memory files the break, the stamped record files "
            "the repair, because the armory values the instrument that "
            "was broken and made true again."
        ),
    },
    {
        "key": "whole_character",
        "name": "Complimenting a Person's Whole Character",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "At the advanced tier, compliments stop being about moments "
            "and start being about the person: a considered statement of "
            "who someone is, built from years of evidence. Complimenting a "
            "person's whole character - you are one of the most honest, "
            "generous, steady people I have ever known - is the heaviest "
            "instrument in the database, and it must be wielded with "
            "corresponding care. It works only from a deep well of shared "
            "history; from a shallow acquaintance it sounds like flattery "
            "or need. The structure is evidence, pattern, verdict: years "
            "of observed moments, the trait they reveal, and the plain "
            "statement of what you have concluded. Delivered rightly, "
            "people remember it for the rest of their lives."
        ),
        "how_it_works": (
            "Draw only on long history - this compliment requires years, "
            "not weeks, of knowing someone. Build it in three parts: the "
            "evidence (in twenty years I have never seen you take the "
            "easy way), the pattern (that is not luck, that is who you "
            "are), the verdict (you are the most principled person I "
            "know). Deliver it in a quiet, private moment - whole-character "
            "verdicts are intimate, and audiences cheapen them. Speak "
            "slowly and plainly; weight comes from calm, not volume. "
            "Mean every word absolutely, because this is the compliment "
            "people test against their self-doubt for years - any "
            "hollowness will be found. Say it once in the relationship's "
            "life, maybe twice; this is not a renewable resource. And "
            "never deliver it as a eulogy-in-advance during a health "
            "scare unless they ask - timing can turn honor into alarm."
        ),
        "key_points": [
            "Draw only on long history - years of knowing, not weeks; shallow roots make it flattery.",
            "Build it in three parts: the evidence, the pattern, the verdict.",
            "Deliver it privately and slowly; weight comes from calm, not volume, and audiences cheapen it.",
            "Mean every word absolutely - this is the compliment people test against self-doubt for years.",
            "Say it once, maybe twice, in a relationship's life; this is not a renewable resource.",
        ],
        "requirements": [
            "Years of shared history providing genuine, repeated evidence.",
            "The three-part structure: evidence, pattern, verdict.",
            "Private, quiet, unhurried delivery.",
            "Absolute sincerity - every word true and tested.",
            "Rarity: once or twice per relationship, never routine.",
        ],
        "standards": [
            "Whole-character verdicts are only given from deep knowledge; acquaintances do not qualify.",
            "Every claim in the verdict must survive the receiver's own self-doubt test for years.",
            "It is never deployed for effect, timing, or occasion - only when it is true and ready.",
        ],
        "citations": [CIT_SELIGMAN, CIT_GRANT, CIT_DECI],
        "sig_lens": (
            "The Signature read: a whole-character verdict is the full "
            "audit of a kept record, read aloud once - and the Signature "
            "Word audits only what decades of evidence prove. Where "
            "public speech spends superlatives freely, the stamped "
            "instrument is struck rarely and rings for years, because "
            "the armory files a life's character as its heaviest holding."
        ),
    },
    {
        "key": "lifetime_achievement",
        "name": "The Lifetime Achievement Tribute",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The lifetime achievement tribute is recognition at full "
            "scale: honoring what someone built, served, or gave across "
            "decades - the career, the cause, the family raised, the "
            "institution founded. Unlike the whole-character compliment, "
            "which is private and personal, the tribute is often public "
            "and often formal: the retirement dinner, the award night, "
            "the anniversary. Its craft is selection and proportion - "
            "choosing the few achievements that represent the many, and "
            "giving each its true weight without turning the evening "
            "into a resume recital. The best tributes spend as much time "
            "on what the work meant to others as on what was "
            "accomplished, because meaning is what the honoree will "
            "carry home."
        ),
        "how_it_works": (
            "Research before you speak: gather the real milestones, and "
            "ask others for the stories you missed - the tribute's "
            "richness comes from many witnesses. Structure it as arc, "
            "not list: where they started, what they built, whom it "
            "served, what endures. Spend at least half the time on "
            "meaning-to-others: the careers launched, the people "
            "sheltered, the standard set. Name two or three defining "
            "moments in detail rather than twenty in passing; depth "
            "honors, inventory bores. Keep it under five minutes spoken "
            "unless you are the designated speaker - tribute inflation "
            "punishes the honoree with endurance. End looking forward: "
            "what they built continues, and so does the gratitude. "
            "Deliver a written copy afterward; the spoken tribute fades, "
            "the letter is kept."
        ),
        "key_points": [
            "Research first: gather real milestones and ask others for the stories you missed.",
            "Structure it as an arc - where they started, what they built, whom it served, what endures.",
            "Spend half the time on meaning-to-others: the careers launched, the people sheltered, the standard set.",
            "Two or three defining moments in depth beat twenty in passing; inventory bores, depth honors.",
            "Deliver a written copy afterward; the spoken tribute fades, the letter is kept.",
        ],
        "requirements": [
            "Real research: verified milestones plus gathered witness stories.",
            "Arc structure rather than chronological inventory.",
            "Equal weight to meaning-to-others as to accomplishments.",
            "Defined moments in depth, not a catalog of everything.",
            "A written copy for keeping, delivered after the event.",
        ],
        "standards": [
            "The tribute is proportioned: selection and depth over completeness.",
            "It honors the honoree's actual values - achievements they are proud of, not the speaker's preferences.",
            "Length respects the audience and the honoree; endurance is not honor.",
        ],
        "citations": [CIT_SELIGMAN, CIT_GRANT, CIT_LOSADA],
        "sig_lens": (
            "The Signature read: a lifetime tribute is the full ledger "
            "read before witnesses, every page balanced - and the "
            "Signature Word balances ledgers with care. Where public "
            "ceremony risks inventory, the stamped record tells the arc "
            "and files the written copy, because the armory keeps what "
            "endures, and meaning endures longest."
        ),
    },
    {
        "key": "moral_courage",
        "name": "Praising Moral Courage",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Moral courage - standing for what is right when it costs "
            "standing - is the rarest virtue this database honors, and "
            "its praise must match its weight. The whistleblower, the "
            "dissenter in the unanimous room, the person who returns the "
            "money nobody would miss: these acts are lonely by nature, "
            "and the actor often pays in full before anyone applauds. "
            "Praising moral courage tells them the price was seen and the "
            "stand mattered, which is sometimes the only payment they "
            "will ever receive. This is advanced because the stakes are "
            "real - careers, relationships, safety - and the praise must "
            "be equally real: no inflation, no appropriation of their "
            "bravery, and absolute discretion about what should stay "
            "private."
        ),
        "how_it_works": (
            "Name the stand and its true cost: you spoke up knowing it "
            "could cost you the promotion - that is moral courage. "
            "Never inflate or borrow their bravery: do not claim you "
            "would have done the same, and do not make their stand "
            "about your admiration. Protect their privacy fiercely - ask "
            "what may be repeated before repeating anything; some "
            "courage must stay quiet to stay safe. Deliver it directly "
            "and soberly; this is not a celebratory compliment. If their "
            "stand cost them tangibly, pair words with practical support "
            "where you can - a reference, a connection, a door opened - "
            "because praise without solidarity is cheap at high stakes. "
            "And stand with them visibly when it is safe to do so; the "
            "greatest praise for moral courage is company."
        ),
        "key_points": [
            "Name the stand and its true cost - the cost is what makes it moral courage.",
            "Never inflate or borrow their bravery; do not claim you would have done the same.",
            "Protect their privacy fiercely - ask what may be repeated before repeating anything.",
            "Pair words with practical solidarity where you can: a reference, a connection, a door opened.",
            "The greatest praise for moral courage is company - stand with them visibly when it is safe.",
        ],
        "requirements": [
            "A genuine stand for what is right at genuine personal cost.",
            "The stand and its cost named plainly, without inflation.",
            "Absolute discretion: nothing repeated without permission.",
            "Direct, sober delivery - never celebratory or casual.",
            "Practical solidarity offered alongside the words where possible.",
        ],
        "standards": [
            "Moral courage is praised only where real cost was risked or paid - comfort-zone dissent does not qualify.",
            "The giver never appropriates the bravery or centers their own admiration.",
            "Safety governs everything: no praise is worth endangering the praised.",
        ],
        "citations": [CIT_SELIGMAN, CIT_DECI, CIT_GRANT],
        "sig_lens": (
            "The Signature read: moral courage is the covenant kept "
            "when keeping it costs everything - and the Signature Word "
            "files it as the highest proof a record can hold. Where "
            "public applause arrives late or never, the stamped "
            "instrument is set promptly and quietly, because the armory "
            "honors the lonely stand above all stands."
        ),
    },
    {
        "key": "lifes_work",
        "name": "Honoring a Life's Work",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A life's work is what someone gave their decades to - the "
            "practice, the craft, the cause, the family, the body of work "
            "that is inseparable from who they are. Honoring it differs "
            "from the lifetime tribute in register: this is personal, "
            "often one-to-one, and it addresses meaning rather than "
            "milestones. What you built matters - and I want you to know "
            "I see the whole of it. The compliment lands hardest at the "
            "transitions: retirement, the closing of the shop, the last "
            "class taught, the moment someone wonders whether it was all "
            "worth it. Your answer, given honestly and specifically, can "
            "settle that question for them. This record teaches how to "
            "say the truest thing about someone's decades."
        ),
        "how_it_works": (
            "Choose a transition moment - retirement, closing, passing "
            "the torch - when the question was it worth it is alive. "
            "Speak to the whole, not the highlights: not the awards but "
            "the forty years of showing up. Name what endures because of "
            "them: the students teaching now, the patients healed, the "
            "street that is safer, the children who carry the values. "
            "Use the second person and the long view: look at what your "
            "life made. Be specific enough to prove you truly see it - "
            "vague praise of a life's work sounds like a greeting card. "
            "If you are part of what endures - their student, their "
            "child, their successor - say so; I am part of your life's "
            "work is the deepest form of this compliment. Write it down; "
            "this is a letter, not just a sentence."
        ),
        "key_points": [
            "Choose a transition moment, when the question was it worth it is alive.",
            "Speak to the whole - the forty years of showing up - not just the highlights.",
            "Name what endures because of them: the students teaching now, the values carried on.",
            "Be specific enough to prove you truly see it; vague praise of a life's work is a greeting card.",
            "If you are part of what endures, say so - and write it down; this is a letter.",
        ],
        "requirements": [
            "Decades of real work, genuinely known to the giver.",
            "A transition moment when the meaning question is present.",
            "The enduring effects named specifically, not the awards listed.",
            "Second-person, long-view address: look at what your life made.",
            "Written form - a letter that can be kept and re-read.",
        ],
        "standards": [
            "A life's work is honored for its meaning and endurance, never reduced to its accolades.",
            "Specificity is the sincerity test at this scale - generalities are withheld.",
            "The giver writes only what is true; a life's work cannot be flattered, only witnessed.",
        ],
        "citations": [CIT_SELIGMAN, CIT_EMMONS, CIT_GRANT],
        "sig_lens": (
            "The Signature read: a life's work is the complete filing - "
            "every year a page, every page kept - and the Signature "
            "Word reads the whole file back to its author. Where public "
            "honor counts the awards, the stamped record counts the "
            "showing-up, because the armory files endurance as the "
            "truest measure of a life."
        ),
    },
    {
        "key": "living_tribute",
        "name": "The Living Tribute: Say It While They Can Hear It",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The living tribute is a simple, radical practice: give "
            "people their flowers while they can still smell them. Say "
            "the eulogy-grade things - what they meant, what they built, "
            "who they are - while they are alive to hear it. Most deep "
            "praise in human life is delivered too late, spoken over "
            "silence to grieving rooms; the living tribute corrects "
            "that timing. It is not morbid - it is the opposite: a "
            "celebration scheduled deliberately, whether as a letter, a "
            "gathering, or a single long conversation. The record's "
            "standing rule: if you would say it at their funeral, find "
            "a way to say it at their table."
        ),
        "how_it_works": (
            "Start with the funeral test: write down what you would say "
            "about them if you had to speak - then plan to say the "
            "truest parts now. Choose the form that fits: a letter for "
            "the private, a gathering of witnesses for the communal, a "
            "long walk-and-talk for the intimate. Frame it as "
            "celebration, not farewell - I wanted you to hear this while "
            "I can watch you hear it. Include the specific stories, not "
            "just the verdicts; the living want the memories, not just "
            "the summary. Invite others to add their verses - the "
            "tribute compounds with voices. Do not wait for a diagnosis "
            "or a milestone; the practice is scheduled by love, not by "
            "occasion. And receive such tributes gracefully when your "
            "turn comes: let people finish."
        ),
        "key_points": [
            "Apply the funeral test: write what you would say over silence, then say the truest parts at their table.",
            "Frame it as celebration, not farewell - I wanted you to hear this while I can watch you hear it.",
            "Include specific stories, not just verdicts; the living want the memories too.",
            "Invite others to add verses - the tribute compounds with voices.",
            "Schedule it by love, not by occasion; do not wait for a diagnosis or a milestone.",
        ],
        "requirements": [
            "Eulogy-grade honesty: only things true enough for the final word.",
            "A deliberate form - letter, gathering, or long conversation - planned, not improvised.",
            "Celebration framing, free of farewell tones.",
            "Specific stories alongside the verdicts.",
            "Timing by intention, not by crisis or calendar.",
        ],
        "standards": [
            "The living tribute is never morbid theater; it is scheduled celebration of a present life.",
            "Every word must be true enough to stand as a final word - the standard is eulogy-grade.",
            "It is given without any hint of farewell; the honoree's alarm is never the price of the honor.",
        ],
        "citations": [CIT_SELIGMAN, CIT_EMMONS, CIT_FREDRICKSON],
        "sig_lens": (
            "The Signature read: the living tribute is the kept record "
            "read aloud to its own author - and the Signature Word holds "
            "that no record should first be read over silence. Where "
            "public custom saves the truest words for last, the stamped "
            "instrument is delivered at the table, because the armory "
            "files praise for the living, to the living."
        ),
    },
    {
        "key": "mentor_legacy",
        "name": "Recognizing a Mentor's Legacy",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A mentor's legacy is the compounding nobody sees: the "
            "students who became teachers, the apprentices who trained "
            "apprentices, the values propagating through generations of "
            "people the mentor never met. Recognizing it means showing "
            "the mentor the tree, not just the seed - mapping how far "
            "their influence traveled. This is the advanced form of "
            "mentor praise: it requires research, witnesses, and often "
            "the detective work of tracing lines of influence. The "
            "compliment's power is revelation - most mentors have no "
            "idea of the scale. Your teaching is now four generations "
            "deep is news, not flattery, and it lands like nothing else "
            "in this database."
        ),
        "how_it_works": (
            "Do the research: trace the lines - who did they teach, who "
            "did those students teach, where did the methods travel. "
            "Gather witnesses: collect a sentence or two from each "
            "generation - she taught me, I teach others now. Present the "
            "tree visually or as a simple generational count; scale made "
            "visible is the compliment. Name the through-line: the "
            "standard, the kindness, the method that survived every "
            "hand-off. Deliver it as revelation - I do not think you "
            "know how far this went - because the not-knowing is what "
            "makes it land. If the mentor is gone, deliver it to their "
            "family or their institution; legacy recognition keeps "
            "working after a life. Document it: the mapped legacy is a "
            "gift to every branch of the tree."
        ),
        "key_points": [
            "Trace the lines: who they taught, who those students taught, where the methods traveled.",
            "Gather a sentence from each generation - the witnesses are the evidence.",
            "Present the tree as scale made visible; generational count is the compliment.",
            "Name the through-line: the standard or kindness that survived every hand-off.",
            "Deliver it as revelation, document it as a gift to every branch, and carry it to family or institution if the mentor is gone.",
        ],
        "requirements": [
            "Real traced lines of influence across at least two generations.",
            "Witness sentences from the branches, gathered honestly.",
            "The scale presented plainly - counts, generations, reach.",
            "The through-line named: what actually propagated.",
            "Documentation that outlasts the telling.",
        ],
        "standards": [
            "Legacy claims are researched, not imagined - every branch named must be real.",
            "The through-line honored is the mentor's actual contribution, not the speaker's projection.",
            "It is revelation, not flattery: the scale must genuinely surprise to qualify as news.",
        ],
        "citations": [CIT_GRANT, CIT_SELIGMAN, CIT_DWECK],
        "sig_lens": (
            "The Signature read: a mentor's legacy is the lineage of "
            "the instrument - every hand it passed through, every hand "
            "it shaped - and the Signature Word keeps lineages longest "
            "of all. Where public memory keeps the name, the stamped "
            "record keeps the tree, because the armory files not the "
            "seed but the forest."
        ),
    },
    {
        "key": "grace_hard_times",
        "name": "Complimenting Grace in Hard Times",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Grace in hard times - bearing grief, illness, loss, or ruin "
            "without becoming bitter - is the virtue people admire most "
            "and praise least, because suffering makes others awkward. "
            "The silence around it is the problem this compliment solves: "
            "the person carrying the heavy thing often feels invisible "
            "inside their own struggle, and being told the way you are "
            "carrying this is remarkable breaks that isolation. This is "
            "advanced because the line between honoring and intruding is "
            "thin: the compliment must acknowledge the weight without "
            "claiming to understand it, admire the bearing without "
            "romanticizing the pain, and never, ever suggest the "
            "suffering was worthwhile."
        ),
        "how_it_works": (
            "Acknowledge the weight first, plainly: what you are going "
            "through is enormous - no minimizing, no silver linings. "
            "Then honor the bearing: and the grace you are bringing to "
            "it is remarkable. Never claim to understand - I know how "
            "you feel is a trespass; I cannot imagine is respect. Keep "
            "it brief and private; suffering praised publicly becomes "
            "spectacle. Do not praise too early - in the rawest weeks, "
            "presence beats praise; the compliment belongs to the "
            "carrying, not the crisis. Never suggest the pain had "
            "purpose: everything happens for a reason is not a "
            "compliment, it is an injury. Pair the words with practical "
            "help where you can; grace praised and then abandoned is "
            "witnessed and left."
        ),
        "key_points": [
            "Acknowledge the weight first and plainly - no minimizing, no silver linings, ever.",
            "Honor the bearing, not the pain: the grace you are bringing to it is remarkable.",
            "Never claim to understand: I cannot imagine is respect, I know how you feel is trespass.",
            "Keep it brief and private; suffering praised publicly becomes spectacle.",
            "Pair words with practical help; grace praised and then abandoned is witnessed and left.",
        ],
        "requirements": [
            "A real hardship, genuinely known - never assumed or pried into.",
            "The weight acknowledged plainly before any praise is offered.",
            "The bearing honored without romanticizing the suffering.",
            "Private, brief delivery at the right time - the carrying, not the rawest crisis.",
            "Practical help offered alongside the words where possible.",
        ],
        "standards": [
            "The pain is never given purpose - everything happens for a reason is forbidden here.",
            "Understanding is never claimed; the giver's ignorance is owned, not hidden.",
            "Timing respects the wound: presence first in crisis, praise in the carrying.",
        ],
        "citations": [CIT_SELIGMAN, CIT_FREDRICKSON, CIT_EMMONS],
        "sig_lens": (
            "The Signature read: grace in hard times is the covenant "
            "carried unbroken through fire - and the Signature Word "
            "bows before the carrying. Where public comfort reaches "
            "for reasons, the stamped instrument offers only witness: "
            "the weight seen, the bearing honored, because the armory "
            "files courage in grief as its most solemn holding."
        ),
    },
    {
        "key": "unsung_hero",
        "name": "Recognizing the Unsung Hero",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The unsung hero is the person whose contribution vastly "
            "exceeds their recognition: the aide who holds the ward "
            "together, the volunteer who never misses, the colleague "
            "whose fixes everyone uses and nobody credits. Recognizing "
            "them is advanced because it requires investigation - finding "
            "the gap between contribution and credit - and because the "
            "recognition itself must be handled with care: some unsung "
            "heroes chose the shadows, and dragging them into light they "
            "did not ask for is not a gift. The compliment's structure "
            "is arithmetic made human: here is what you give, here is "
            "what you get credited for, and the difference is what I am "
            "naming today."
        ),
        "how_it_works": (
            "Investigate first: map the real contribution - who relies "
            "on their work, what breaks without them. Measure the gap "
            "honestly: everyone uses your fixes and nobody knows your "
            "name. Ask before amplifying: some heroes prefer the "
            "shadows - would you be comfortable if I mentioned this at "
            "the meeting? If yes, sing it properly: specific "
            "contribution, named publicly, credit assigned. If no, "
            "honor them privately and deeply - the private unsung-hero "
            "recognition is still transformative. Fix the structure "
            "where you can: the best follow-up to naming an unsung hero "
            "is changing the system that left them unsung. Never use "
            "their heroism to guilt others; the recognition is about "
            "them, not a lesson plan."
        ),
        "key_points": [
            "Investigate first: map the real contribution and who relies on it.",
            "Measure the gap honestly: here is what you give, here is the credit you get.",
            "Ask before amplifying - some heroes chose the shadows, and consent governs the spotlight.",
            "If yes, sing it properly and publicly; if no, honor them privately and deeply.",
            "Fix the structure where you can; never use their heroism to guilt others.",
        ],
        "requirements": [
            "A verified gap between contribution and recognition - investigated, not assumed.",
            "The contribution mapped: who relies on it, what breaks without it.",
            "Consent before any public amplification.",
            "Specific, named credit when amplified; deep private honor when not.",
            "Structural follow-up where the giver has power to change the system.",
        ],
        "standards": [
            "The unsung hero's preference governs: shadows chosen are respected, not overridden.",
            "Contribution claims are verified - imagined heroism helps no one.",
            "Recognition aims at correction (of the credit gap), never at using the hero as an example to shame others.",
        ],
        "citations": [CIT_GRANT, CIT_LOSADA, CIT_DECI],
        "sig_lens": (
            "The Signature read: the unsung hero keeps the covenant "
            "with no expectation of witness - and the Signature Word "
            "considers the unwitnessed covenant the purest of all. "
            "Where public systems forget the load-bearers, the stamped "
            "record measures the gap and names it, because the armory "
            "refuses to let its truest instruments go unfiled."
        ),
    },
    {
        "key": "forgiveness",
        "name": "Praising Forgiveness",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Forgiveness - releasing a genuine grievance without being "
            "asked, or accepting a real apology and truly letting go - "
            "is among the hardest human acts, and praising it honors "
            "strength most people never witness. This compliment is "
            "advanced because it touches real wounds: it must honor the "
            "releaser without minimizing what was released, and it must "
            "never pressure anyone toward forgiving. The way you let "
            "that go, fully and without keeping score - that is "
            "extraordinary acknowledges both the injury and the "
            "magnitude of the release. It is given after the fact, "
            "privately, and with zero agenda beyond witness: the "
            "forgiver's freedom, seen and named."
        ),
        "how_it_works": (
            "Wait until the forgiveness is real and settled - praising "
            "it mid-process pressures the outcome. Acknowledge the "
            "injury honestly first: what they did was genuinely wrong, "
            "and you had every right to hold it. Then honor the "
            "release: and you let it go completely - no scorekeeping, "
            "no cold storage. That is rare strength. Keep it private "
            "always; forgiveness praised publicly can humiliate the "
            "forgiven or expose the forgiver. Never praise forgiveness "
            "to encourage more of it - the compliment witnesses, it "
            "does not recruit. Never suggest the injury did not matter; "
            "minimizing the wound insults the magnitude of the release. "
            "And never, ever praise someone for forgiving something "
            "unforgiven to pressure them - that is manipulation wearing "
            "praise's clothes."
        ),
        "key_points": [
            "Wait until the forgiveness is real and settled; praising it mid-process pressures the outcome.",
            "Acknowledge the injury honestly first - what was done was genuinely wrong.",
            "Then honor the release: no scorekeeping, no cold storage - that is rare strength.",
            "Keep it private always; public forgiveness-praise can humiliate or expose.",
            "Never praise to recruit more forgiveness, never minimize the wound, never praise the unforgiven to pressure.",
        ],
        "requirements": [
            "A genuine grievance genuinely released - settled, not performed.",
            "The injury acknowledged honestly before the release is honored.",
            "The completeness of the release named: no scorekeeping.",
            "Strictly private delivery.",
            "Zero agenda: witness only, never recruitment or pressure.",
        ],
        "standards": [
            "The wound is never minimized to make the forgiveness look easy - magnitude of release requires magnitude of injury.",
            "Forgiveness is never praised prospectively or prescriptively; the compliment follows the fact.",
            "Privacy is absolute: all parties' dignity governs every word.",
        ],
        "citations": [CIT_SELIGMAN, CIT_STONE, CIT_FREDRICKSON],
        "sig_lens": (
            "The Signature read: forgiveness is the covenant's heaviest "
            "release - the ledger closed by choice, not by payment - "
            "and the Signature Word files it as freedom's own record. "
            "Where public speech rushes to move on, the stamped "
            "instrument honors the wound first and the release second, "
            "because the armory knows what letting go truly costs."
        ),
    },
    {
        "key": "life_changing",
        "name": "The Compliment That Changes a Life",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The capstone of the ladder: the compliment that changes a "
            "life. These are real and documented in human experience - "
            "the teacher's you have a gift, you should write, that "
            "redirected a career; the stranger's your voice deserves to "
            "be heard, that undid years of silence; the friend's you "
            "would be a great father, that steadied a drifting man. "
            "What makes them life-changing is not eloquence but timing "
            "and truth: a true thing said at the exact moment someone "
            "could receive it, naming a possibility they had not dared "
            "to claim. This record cannot teach you to manufacture such "
            "moments - they cannot be manufactured - but it can teach "
            "readiness: paying the kind of attention that notices the "
            "unclaimed possibility, and having the courage to name it "
            "plainly when you see it."
        ),
        "how_it_works": (
            "Practice the attention first: watch for the unclaimed "
            "possibility - the talent dismissed, the dream deferred, "
            "the strength the person cannot see in themselves. When you "
            "see it, name it plainly and specifically: you have a real "
            "gift for this - you should do it properly. Say it with "
            "complete conviction; a life-changing compliment hedged is "
            "a life-changing compliment lost. Do not dress it up - "
            "plain words carry further than poetry here. Accept that "
            "you will rarely know it worked; these compliments ripen "
            "for years underground. Never aim for life-changing as a "
            "goal - the moment you perform for impact, sincerity dies; "
            "aim only at truth, spoken at the right time. And when "
            "someone tells you years later that your words changed "
            "their life, receive it simply: I am glad. I meant it."
        ),
        "key_points": [
            "Watch for the unclaimed possibility: the talent dismissed, the dream deferred, the unseen strength.",
            "Name it plainly and specifically, with complete conviction - hedged is lost.",
            "Plain words carry further than poetry; do not dress it up.",
            "Accept that you will rarely know it worked; these compliments ripen underground for years.",
            "Never aim for life-changing as a goal - aim only at truth, spoken at the right time.",
        ],
        "requirements": [
            "A genuine unclaimed possibility, truly seen - never invented for effect.",
            "Plain, specific naming of the possibility with full conviction.",
            "Right-time delivery: the moment the person could receive it.",
            "Zero performance of impact - truth is the only aim.",
            "Gracious, simple reception if the recipient ever reports back years later.",
        ],
        "standards": [
            "Life-changing compliments cannot be manufactured; readiness and truth are the only methods.",
            "The possibility named must be real and within the person's reach - false callings harm.",
            "The giver seeks no credit and no follow-up; the seed is planted and released.",
        ],
        "citations": [CIT_DWECK, CIT_SELIGMAN, CIT_DECI],
        "sig_lens": (
            "The Signature read: the life-changing compliment is the "
            "instrument struck once that rings for decades - and the "
            "Signature Word holds such strikings as the armory's "
            "highest purpose. Where public speech chases impact, the "
            "stamped record seeks only the true thing at the true "
            "moment, because the armory knows: truth, timed, is the "
            "strongest instrument ever forged."
        ),
    },
]
