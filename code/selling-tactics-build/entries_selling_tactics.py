#!/usr/bin/env python3
"""Entries for the Selling Tactics databases (order #4b, 2026-10-17 15:32 EDT).

Dedupe pre-check (whole-system DedupeGate over data/dedupe/exact):
68 planned titles checked; 1 refusal ("Negotiation Fundamentals" already in
the university database) -> renamed to "Fundamentals of Sales Negotiation",
re-checked clean. All other 67 clean on first pass.

This build creates two NEW databases, 34 ladder-ordered records each:

  selling-tactics             - The Selling Tactics Database
                                (public-harvest: real, fact-checked sales
                                knowledge - prospecting, pitches, negotiation,
                                objection handling, closing techniques,
                                follow-up systems, relationship selling, and
                                the ethics of selling; standard references
                                Carnegie How to Win Friends and Influence
                                People 1936; Cialdini Influence rev ed 2021;
                                Rackham SPIN Selling 1988; Ziglar Secrets of
                                Closing the Sale 1984; Miller and Heiman
                                Strategic Selling 1985; Dixon and Adamson The
                                Challenger Sale 2011; Gitomer The Sales Bible
                                1994; Tracy The Psychology of Selling 2004;
                                Sandler 1995; Harvard Business Review sales
                                research; and the other landmarks cited per
                                record)
  selling-tactics-signature   - The Selling Tactics Signature Database
                                (his original Signature Selling Method: every
                                tactic a covenant between seller and buyer,
                                prospecting the search, the pitch the promise,
                                negotiation the balance, the close the
                                handshake, follow-up the bond; src signature,
                                titles suffixed " (Signature Edition)", never
                                presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-SELL- (public) and JAH-SELLS- (signature), verified free
in the manifest and in every shard index (zero hits; JAH-SLT- belongs to
the unrelated Software Labs Taxonomy database, so the SELL form was chosen).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_selling_tactics.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos.

Screening: all tactics are ethical persuasion - no deception, manipulation,
or pressure techniques; nothing hate-adjacent, profane, inappropriate, or
religious; nothing on neutralizing or defeating military or defense-grade
systems. Never the words "bat belt" anywhere. No website references.
No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Selling Method: "
            "every tactic a covenant between seller and buyer, prospecting "
            "the search, the pitch the promise, negotiation the balance, "
            "the close the handshake, and follow-up the bond. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_CARNEGIE = ("Carnegie D. How to Win Friends and Influence People. "
                "Simon and Schuster; 1936.")
CIT_CIALDINI = ("Cialdini RB. Influence: The Psychology of Persuasion. "
                "Revised ed. Harper Business; 2021.")
CIT_RACKHAM = ("Rackham N. SPIN Selling. McGraw-Hill; 1988.")
CIT_ZIGLAR = ("Ziglar Z. Secrets of Closing the Sale. Berkley Books; 1984.")
CIT_MILLER = ("Miller RB, Heiman SE. Strategic Selling. William Morrow; "
              "1985.")
CIT_CHALLENGER = ("Dixon M, Adamson B. The Challenger Sale. Portfolio; "
                  "2011.")
CIT_GITOMER = ("Gitomer J. The Sales Bible. William Morrow; 1994.")
CIT_TRACY = ("Tracy B. The Psychology of Selling. Harper Business; 2004.")
CIT_SANDLER = ("Sandler D. You Cant Teach a Kid to Ride a Bike at a Seminar. "
               "Dutton; 1995.")
CIT_HBR = ("Harvard Business Review. Sales and negotiation research "
           "archive (hbr.org).")

ENTRIES = [
    {
        "key": "what_selling_is",
        "name": "What Selling Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Selling is the process of helping another person or organization "
            "decide to exchange value - money, time, or commitment - for a "
            "product, service, or idea that solves their problem. It runs in "
            "seven stages: prospect, qualify, discover, present, handle "
            "objections, close, and follow up. A typical healthy funnel "
            "converts 100 prospects into 20 qualified leads, 8 real "
            "opportunities, and 2 to 3 closed sales, so activity at the top "
            "drives results at the bottom."),
        "how_it_works": (
            "The seller identifies people with a possible need, checks that "
            "they can decide and pay, asks questions to uncover the real "
            "problem, presents only the parts of the offer that map to that "
            "problem, answers concerns honestly, asks for the decision, and "
            "then stays in touch so the customer succeeds. Each stage feeds "
            "the next, and skipping a stage - presenting before discovering, "
            "or closing before handling objections - is the most common "
            "reason deals stall."),
        "key_points": [
            "Selling is helping someone decide, not pressuring them.",
            "The seven stages are prospect, qualify, discover, present, handle, close, follow up.",
            "Funnel math: 100 prospects yield about 2 to 3 closes in a healthy process.",
            "Skipping stages causes most stalled deals.",
            "Follow-up after the sale protects the sale and seeds the next one.",
        ],
        "requirements": [
            "Define each of the seven stages in your own process.",
            "Track counts at every stage for at least one month.",
            "Never present before discovering the real problem.",
        ],
        "standards": [
            "Record every stage count honestly - fabricated funnel numbers are a planning lie that compounds.",
            "Presentations never precede discovery; the order of stages is the process standard.",
            "Follow-up after the sale is a required stage, not optional courtesy."
        ],
        "citations": [CIT_TRACY, CIT_HBR],
        "sig_lens": (
            "In the Signature Selling Method, selling is a covenant: the "
            "seller promises value, the buyer promises fair exchange, and "
            "both keep their word. Each of the seven stages is a vow kept in "
            "order - search, test, listen, show, answer, seal, and tend."),
    },
    {
        "key": "psychology_buying",
        "name": "The Psychology of Buying",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "People buy for emotional reasons and justify with logic: safety, "
            "status, comfort, belonging, growth, and freedom drive decisions, "
            "and the buyer then looks for facts that support the feeling. "
            "Robert Cialdini documented six principles of ethical influence - "
            "reciprocity, commitment, social proof, authority, liking, and "
            "scarcity - which describe how trust forms, not tricks to force "
            "it. In a buying-decision model, emotional fit carries about 60 "
            "percent of the weight and logical fit about 40 percent, so "
            "sellers must address both the heart and the spreadsheet."),
        "how_it_works": (
            "The buyer first senses whether the seller is trustworthy and "
            "whether the offer feels right, then gathers reasons that confirm "
            "the feeling. The seller earns the emotional vote by listening "
            "and keeping promises, and earns the logical vote with clear "
            "evidence: numbers, references, demonstrations, and guarantees. "
            "Influence principles work only when they are true - real "
            "reciprocity, real social proof, real authority."),
        "key_points": [
            "Emotion decides; logic justifies - address both.",
            "Cialdini six principles: reciprocity, commitment, social proof, authority, liking, scarcity.",
            "Model: 60 percent emotional fit, 40 percent logical fit.",
            "Principles of influence only work when they are genuinely true.",
            "Trust is built by listening and by kept promises.",
        ],
        "requirements": [
            "Name the emotional driver in each of your last five sales.",
            "Back every emotional appeal with one checkable fact.",
            "Never use a principle of influence falsely (fake scarcity, fake proof).",
        ],
        "standards": [
            "Influence principles are used only when genuinely true - real proof, real authority, real scarcity.",
            "Every emotional appeal is paired with at least one checkable fact.",
            "Never manufacture urgency or social proof; false pressure is manipulation, not selling."
        ],
        "citations": [CIT_CIALDINI, CIT_CARNEGIE],
        "sig_lens": (
            "The Signature Selling Method reads the buyer as a whole person: "
            "the feeling that says yes and the reason that defends it. The "
            "covenant of selling requires both votes - the heart must trust "
            "and the mind must agree - and the seller earns each honestly."),
    },
    {
        "key": "prospecting",
        "name": "Prospecting and Finding Customers",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Prospecting is the disciplined search for new potential buyers "
            "before they search for you. Channels include referrals, warm "
            "introductions, networking, cold outreach, content, and "
            "partnerships. The arithmetic is fixed: with 40 outreach attempts "
            "a day, a 10 percent conversation rate, and a 25 percent "
            "meeting rate, a seller books 1 meeting per day and 20 per "
            "month. Prospecting is the one selling activity that cannot be "
            "delegated to luck - the pipeline of next quarter is built this "
            "quarter."),
        "how_it_works": (
            "The seller builds a target list of people who match the ideal "
            "customer, reaches out with a short relevant message, follows up "
            "several times, and converts conversations into meetings. Every "
            "step is counted: attempts, conversations, meetings, proposals, "
            "closes. When a ratio drops, the seller fixes that step instead "
            "of blaming the market."),
        "key_points": [
            "Prospecting feeds the pipeline; without it the funnel empties.",
            "Fixed arithmetic: 40 attempts/day -> ~20 meetings/month at typical rates.",
            "Measure every conversion ratio and fix the weakest step.",
            "Warm channels (referrals, introductions) convert best; cold channels scale.",
            "Consistency beats intensity - daily prospecting wins.",
        ],
        "requirements": [
            "Block daily prospecting time and protect it.",
            "Maintain a target list of at least 100 named prospects.",
            "Track attempts, conversations, and meetings weekly.",
        ],
        "standards": [
            "Prospect daily; the pipeline is a leading indicator of next-quarter revenue.",
            "Count attempts, conversations, and meetings - manage ratios, not moods.",
            "Cold outreach states who you are and why you are writing in the first two lines."
        ],
        "citations": [CIT_GITOMER, CIT_TRACY],
        "sig_lens": (
            "Prospecting is the search of the Signature covenant: the seller "
            "goes looking for people whose problems match the promise. The "
            "search is daily, counted, and honest - every number earned, "
            "never borrowed."),
    },
    {
        "key": "qualifying",
        "name": "Qualifying Leads",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Qualifying separates real opportunities from polite "
            "conversations. The classic BANT screen - Budget, Authority, "
            "Need, Timeline - scores each prospect 0 to 3 on each factor for "
            "a total of 0 to 12; scores of 9 and above get full effort, 6 to "
            "8 get light nurturing, and below 6 get released. An "
            "unqualified pipeline is a fantasy: it inflates forecasts and "
            "wastes presentations on people who cannot buy."),
        "how_it_works": (
            "Early in the conversation the seller asks plain questions: is "
            "there money set aside, who decides, what problem must be "
            "solved, and by when. The answers score the lead. Qualified "
            "leads move to discovery; weak leads go into a nurture track; "
            "disqualified leads are thanked and released so time goes to "
            "real chances."),
        "key_points": [
            "BANT: Budget, Authority, Need, Timeline - score 0-3 each, 12 max.",
            "9+ means pursue, 6-8 means nurture, below 6 means release.",
            "Qualifying protects the forecast from fantasy.",
            "Ask the hard questions early - it is kinder to everyone.",
            "Released leads are not failures; they are time returned.",
        ],
        "requirements": [
            "Score every new lead with BANT before proposing.",
            "Re-qualify on every major change (new contact, new budget year).",
            "Keep a nurture track for 6-8 scores.",
        ],
        "standards": [
            "Score every opportunity on Budget, Authority, Need, and Timeline before proposing.",
            "Release sub-6 BANT scores kindly and quickly - time is the seller scarcest asset.",
            "Re-qualify whenever the buying team or budget year changes."
        ],
        "citations": [CIT_MILLER, CIT_HBR],
        "sig_lens": (
            "Qualifying is the testing of the covenant: does this buyer truly "
            "need the promise, can they keep their side, and is the time "
            "right. The Signature seller tests early and releases kindly - "
            "a false covenant helps no one."),
    },
    {
        "key": "rapport",
        "name": "First Impressions and Rapport",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Buyers form a first impression within seconds, and rapport - "
            "the sense of being understood - decides whether they keep "
            "listening. Dale Carnegie classic rules still hold: use the "
            "person name, show genuine interest, smile, listen more than you "
            "speak, and talk in terms of the other person interests. A "
            "seller who matches the buyer pace, remembers details, and "
            "follows through on small promises earns the right to ask "
            "deeper questions."),
        "how_it_works": (
            "Before the meeting the seller researches the person and the "
            "company. In the first minutes the seller is on time, prepared, "
            "and curious - asking about the buyer world before presenting "
            "anything. Small promises (I will send that article today) are "
            "kept exactly, because reliability in small things predicts "
            "reliability in large ones."),
        "key_points": [
            "First impressions form in seconds and are hard to reverse.",
            "Carnegie rules: name, interest, listening, their terms.",
            "Match the buyer pace and energy.",
            "Keep every small promise exactly.",
            "Rapport is earned by curiosity, not by charm.",
        ],
        "requirements": [
            "Research every prospect before first contact.",
            "Open with questions about them, never with your pitch.",
            "Log and keep every small commitment made.",
        ],
        "standards": [
            "Arrive prepared: research the person and company before first contact.",
            "Open with curiosity about the buyer world, never with a product monologue.",
            "Keep small promises exactly - reliability in small things is the standard."
        ],
        "citations": [CIT_CARNEGIE, CIT_CIALDINI],
        "sig_lens": (
            "Rapport is the first thread of the covenant: the buyer must feel "
            "seen before they will be shown anything. The Signature seller "
            "arrives prepared, curious, and exact in small promises, because "
            "the large promise rests on them."),
    },
    {
        "key": "discovery",
        "name": "Discovery Questions",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Discovery is the question phase that uncovers the buyer real "
            "problem, its cost, and what solving it is worth. Open questions "
            "(what, how, tell me about) gather stories; closed questions "
            "(is, does, when) confirm facts. A strong discovery call runs "
            "about 70 percent open questions to 30 percent closed, and lasts "
            "until the seller can state the problem and its price back to "
            "the buyer in the buyer own words."),
        "how_it_works": (
            "The seller plans questions in four layers: situation (what is "
            "true now), problem (what hurts), implication (what the hurt "
            "costs), and need-payoff (what fixing it is worth). Each answer "
            "is written down and played back for confirmation. Only when "
            "the buyer agrees the problem is expensive does the seller move "
            "to presenting."),
        "key_points": [
            "Discovery finds the real problem and its cost before any pitch.",
            "Open questions gather stories; closed questions confirm facts.",
            "Target ratio: 70 percent open, 30 percent closed.",
            "Play every answer back for confirmation.",
            "No confirmed expensive problem means no presentation yet.",
        ],
        "requirements": [
            "Write discovery questions before every first meeting.",
            "Take notes and read the problem back for agreement.",
            "Quantify the cost of the problem in the buyer numbers.",
        ],
        "standards": [
            "Ask open questions first (70 percent) and closed questions to confirm (30 percent).",
            "Quantify the cost of the problem in the buyer own numbers before presenting.",
            "Play back the problem and win explicit agreement before moving on."
        ],
        "citations": [CIT_RACKHAM, CIT_MILLER],
        "sig_lens": (
            "Discovery is the listening vow of the covenant: the seller "
            "hears the wound before offering the remedy. The Signature "
            "seller asks in layers, writes down every answer, and never "
            "prescribes before the diagnosis is agreed."),
    },
    {
        "key": "product_knowledge",
        "name": "Product Knowledge",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Product knowledge is command of what you sell: features, how "
            "they work, limits, competitors, pricing, and the proof behind "
            "every claim. A seller should be able to answer the 20 hardest "
            "questions about the product without notes, and to map each of "
            "the top 10 features to the buyer problem it solves. Knowledge "
            "without judgment is trivia - the point is knowing which fact "
            "matters to this buyer, now."),
        "how_it_works": (
            "The seller studies the product, uses it personally where "
            "possible, learns the competitor lineup, and keeps a living "
            "answer bank of hard questions with approved answers. Before "
            "each call the seller reviews which features map to this "
            "buyer discovered problems, and leaves the rest out of the "
            "conversation."),
        "key_points": [
            "Know features, limits, competitors, pricing, and proof.",
            "Answer the 20 hardest questions without notes.",
            "Map the top 10 features to buyer problems.",
            "Use the product yourself whenever possible.",
            "Present only what maps to this buyer - leave the rest out.",
        ],
        "requirements": [
            "Maintain a living answer bank of hard questions.",
            "Learn the top three competitors cold.",
            "Review feature-to-problem mapping before each call.",
        ],
        "standards": [
            "Every claim about the product is backed by a checkable source or demonstration.",
            "Know the top three competitors well enough to compare honestly.",
            "Never present a feature you cannot explain and defend."
        ],
        "citations": [CIT_GITOMER, CIT_ZIGLAR],
        "sig_lens": (
            "Product knowledge is knowing the promise you carry: what it "
            "does, what it cannot do, and where it stands against others. "
            "The Signature seller never promises what the product cannot "
            "keep - the covenant depends on it."),
    },
    {
        "key": "listening",
        "name": "Listening as a Selling Skill",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The best sellers talk less than the buyer: the 80-20 rule says "
            "the buyer should speak about 80 percent of the time in "
            "discovery. Active listening means full attention, no "
            "interrupting, short encouragers, note-taking, and playing back "
            "what was heard. In a 30-minute discovery call the buyer should "
            "hold the floor for about 24 minutes; if the seller talks 15, "
            "the ratio has collapsed to 50-50 and discovery is failing."),
        "how_it_works": (
            "The seller asks an open question, then goes quiet and listens "
            "completely - not planning the next line but hearing this one. "
            "Key phrases are written down verbatim. After the buyer finishes, "
            "the seller summarizes: what I heard is... and waits for "
            "correction. Silence after a question is a tool, not a gap."),
        "key_points": [
            "80-20 rule: the buyer talks 80 percent in discovery.",
            "Never interrupt; plan nothing while the buyer speaks.",
            "Write down key phrases verbatim.",
            "Play back summaries and wait for correction.",
            "Silence after a question is a selling tool.",
        ],
        "requirements": [
            "Time your talk ratio on real calls monthly.",
            "Take verbatim notes on buyer phrases.",
            "End discovery with a spoken summary for agreement.",
        ],
        "standards": [
            "The buyer holds the floor 80 percent of discovery; time it monthly.",
            "Never interrupt; note key phrases verbatim for playback.",
            "End discovery with a spoken summary and explicit buyer agreement."
        ],
        "citations": [CIT_CARNEGIE, CIT_RACKHAM],
        "sig_lens": (
            "Listening is the sacred half of the covenant: the seller gives "
            "the buyer the floor and guards it. In Signature selling, the "
            "one who listens longest understands deepest, and understanding "
            "is what the promise is built on."),
    },
    {
        "key": "features_benefits",
        "name": "Features Versus Benefits",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A feature is what the product has; a benefit is what the buyer "
            "gets. Buyers pay for benefits, never for features. The "
            "translation rule: every feature must be followed by so that "
            "you... - the battery lasts 20 hours so that you work a full "
            "day without a charger. A catalog of 10 features becomes 10 "
            "benefits only when each is translated into the buyer outcome; "
            "untranslated features are noise."),
        "how_it_works": (
            "For each feature the seller asks: what does this let the buyer "
            "do, avoid, save, or become. The answer is the benefit, stated "
            "in the buyer words from discovery. Presentations lead with "
            "benefits and keep features as supporting proof - the buyer "
            "remembers what it does for them, not how it works."),
        "key_points": [
            "Features describe the product; benefits describe the buyer outcome.",
            "Translate with: feature, so that you..., benefit.",
            "Buyers pay for benefits, never for features.",
            "Use the buyer own words from discovery.",
            "Lead with benefits; keep features as proof.",
        ],
        "requirements": [
            "Write the feature-to-benefit map for your top 10 features.",
            "Rehearse each translation in plain speech.",
            "Audit one presentation a month for untranslated features.",
        ],
        "standards": [
            "Every feature presented is translated with so that you into a buyer benefit.",
            "Benefits are stated in the buyer own words captured during discovery.",
            "Untranslated features are cut from the presentation."
        ],
        "citations": [CIT_ZIGLAR, CIT_TRACY],
        "sig_lens": (
            "In the Signature covenant the buyer is promised outcomes, not "
            "mechanisms: the feature is the instrument, the benefit is the "
            "music. The Signature seller translates every string - so that "
            "you - before playing a single note."),
    },
    {
        "key": "goals",
        "name": "Setting Sales Goals and Activity Targets",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Goals turn hope into arithmetic: a quota of 60,000 per quarter "
            "at an average deal of 5,000 needs 12 wins; at a 25 percent "
            "close rate that needs 48 qualified opportunities; at a 40 "
            "percent meeting-to-opportunity rate that needs 120 meetings. "
            "Working backward from revenue to daily activity gives a seller "
            "a number to hit every single day - for example 6 outreach "
            "attempts per working day across 20 days to book those "
            "meetings."),
        "how_it_works": (
            "The seller writes the annual goal, divides it into quarters "
            "and months, then converts revenue into activity using real "
            "conversion ratios from their own history. Daily targets for "
            "attempts, conversations, and meetings go on the calendar like "
            "appointments. Progress is reviewed weekly and the plan is "
            "adjusted - goals stay fixed, tactics flex."),
        "key_points": [
            "Convert quota backward: revenue -> wins -> opportunities -> meetings -> attempts.",
            "Example: 60,000 quota needs 120 meetings at typical ratios.",
            "Daily activity targets beat monthly hoping.",
            "Use your own conversion history, not industry averages.",
            "Review weekly; keep goals fixed, flex the tactics.",
        ],
        "requirements": [
            "Write the full backward plan for this quarter.",
            "Put daily activity targets on the calendar.",
            "Review numbers every Friday and adjust tactics.",
        ],
        "standards": [
            "Work backward from quota to daily activity using your own conversion history.",
            "Daily targets are calendar appointments, reviewed every Friday.",
            "Goals stay fixed; tactics flex when the numbers miss."
        ],
        "citations": [CIT_TRACY, CIT_HBR],
        "sig_lens": (
            "The Signature seller counts the covenant in advance: so much "
            "promise to keep, so many kept promises needed, so many "
            "conversations to find them. The goal is a vow with arithmetic, "
            "and the arithmetic is checked every Friday."),
    },
    {
        "key": "time_management",
        "name": "Time Management for Sellers",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A seller week has about 40 working hours; top performers spend "
            "roughly 60 percent (24 hours) in direct selling - calls, "
            "meetings, follow-up - and cap administration at 20 percent "
            "(8 hours), with the rest for learning and planning. Losing just "
            "1 hour a day to low-value tasks costs 20 hours a month, about "
            "half a selling week. Time is protected by batching admin, "
            "time-blocking prospecting, and saying no to meetings without a "
            "buyer."),
        "how_it_works": (
            "The seller audits one week honestly, categorizes every hour, "
            "then rebuilds the calendar: prospecting blocks first, customer "
            "meetings next, admin batched into two short windows. Email and "
            "reports are processed in batches, never dripped through the "
            "day. Every Friday the next week calendar is set before the "
            "weekend."),
        "key_points": [
            "60 percent selling time, 20 percent admin cap.",
            "1 lost hour daily equals 20 hours monthly - half a selling week.",
            "Batch admin; time-block prospecting first.",
            "Say no to meetings without a buyer present.",
            "Set next week calendar every Friday.",
        ],
        "requirements": [
            "Audit one full week of hours honestly.",
            "Block prospecting time before anything else.",
            "Batch email and admin into two daily windows.",
        ],
        "standards": [
            "Protect 60 percent of working hours for direct selling; cap admin at 20 percent.",
            "Prospecting blocks are scheduled before all other discretionary time.",
            "Batch email and reports; never drip admin through selling hours."
        ],
        "citations": [CIT_TRACY, CIT_GITOMER],
        "sig_lens": (
            "Time is the Signature seller most guarded vow: hours given to "
            "the search and to customers are hours kept; hours leaked to "
            "trivia are promises quietly broken. The calendar is the "
            "covenant written in advance."),
    },
    {
        "key": "elevator_pitch",
        "name": "The Elevator Pitch",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The elevator pitch explains what you do in 30 seconds - about "
            "75 words at normal speech - in a way that earns a longer "
            "conversation. The structure is fixed: who you help, the costly "
            "problem they face, what you do differently, and a proof point. "
            "Example frame: I help X who struggle with Y; unlike Z, we W; "
            "last quarter a client like you gained V. It ends with a "
            "question, never with a monologue."),
        "how_it_works": (
            "The seller writes the pitch, times it, and trims it to 30 "
            "seconds. It is customized per audience by swapping the problem "
            "and proof point. It is delivered conversationally, then the "
            "seller stops and asks a question - tell me, how do you handle "
            "Y today - handing the floor to the buyer."),
        "key_points": [
            "30 seconds, about 75 words, one clear structure.",
            "Who you help, their costly problem, your difference, one proof.",
            "Swap problem and proof per audience.",
            "End with a question, never a monologue.",
            "Rehearse until it sounds unrehearsed.",
        ],
        "requirements": [
            "Write and time three audience-specific pitches.",
            "Record yourself and cut every filler word.",
            "Test on a friendly contact before using live.",
        ],
        "standards": [
            "Thirty seconds, about 75 words, four parts: who, problem, difference, proof.",
            "Customize the problem and proof point per audience.",
            "End with a question that hands the floor to the buyer."
        ],
        "citations": [CIT_GITOMER, CIT_ZIGLAR],
        "sig_lens": (
            "The Signature pitch is the promise stated in one breath: who it "
            "serves, what wound it heals, how it differs, and the proof it "
            "has kept. Thirty seconds, seventy-five words, then silence - "
            "the covenant begins with listening."),
    },
    {
        "key": "presentations",
        "name": "Sales Presentations",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A sales presentation is a guided tour of benefits mapped to the "
            "buyer discovered problems - never a generic slide deck. The "
            "structure runs: confirm the problem, show the mapped solution, "
            "prove it works, handle concerns, and agree next steps. In a "
            "30-minute slot the budget is about 5 minutes confirming, 15 "
            "presenting, 5 proving, and 5 agreeing - and the buyer talks "
            "throughout, not just at the end."),
        "how_it_works": (
            "The seller opens by restating the buyer problem for agreement, "
            "then shows only the features that map to it, each translated to "
            "a benefit. Proof follows: demonstrations, references, numbers. "
            "Questions are invited during, not saved for the end. It closes "
            "with agreed next steps, dates, and owners - never with thanks "
            "for your time and silence."),
        "key_points": [
            "Present benefits mapped to discovered problems only.",
            "30-minute budget: 5 confirm, 15 present, 5 prove, 5 agree.",
            "Invite questions during, not after.",
            "Proof beats adjectives - demo, reference, number.",
            "End with dated next steps and owners.",
        ],
        "requirements": [
            "Rebuild your deck around buyer problems, not product sections.",
            "Rehearse the 30-minute budget with a timer.",
            "Collect three provable proof points per offer.",
        ],
        "standards": [
            "Show only features mapped to discovered problems; cut the generic deck.",
            "Budget 30 minutes as 5 confirm, 15 present, 5 prove, 5 agree.",
            "Leave every presentation with dated next steps and named owners."
        ],
        "citations": [CIT_ZIGLAR, CIT_RACKHAM],
        "sig_lens": (
            "The Signature presentation is the promise shown, not told: the "
            "wound confirmed, the remedy mapped, the proof laid out, the "
            "doubts answered, the next vow dated. Nothing generic enters "
            "the room - only what this buyer asked to see."),
    },
    {
        "key": "storytelling",
        "name": "Storytelling in Sales",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Stories sell because brains remember narratives far longer than "
            "lists: a customer story follows the arc of hero (a client like "
            "you), struggle (the costly problem), guide (how we helped), "
            "result (the measured outcome), and moral (what it means for "
            "you). A 90-second story with one real number beats ten minutes "
            "of feature talk. Stories must be true and checkable - invented "
            "case studies destroy trust permanently."),
        "how_it_works": (
            "The seller collects real customer outcomes with permission, "
            "shapes each into the five-beat arc, and keeps them to 90 "
            "seconds. The right story is chosen for the buyer situation - "
            "same industry, same problem, same size. After the result, the "
            "seller asks: would an outcome like that matter to you."),
        "key_points": [
            "Arc: hero, struggle, guide, result, moral.",
            "90 seconds, one real number, then a question.",
            "Match the story to the buyer situation.",
            "Stories must be true and checkable - always.",
            "Narrative memory outlasts feature lists.",
        ],
        "requirements": [
            "Bank five true customer stories with permission.",
            "Shape each to the five-beat, 90-second form.",
            "Retire any story you cannot prove.",
        ],
        "standards": [
            "Stories are true, permissioned, and checkable - invented case studies are forbidden.",
            "Ninety seconds, five beats, one real number, then a question.",
            "Match the story to the buyer industry, problem, and size."
        ],
        "citations": [CIT_GITOMER, CIT_CIALDINI],
        "sig_lens": (
            "The Signature story is a kept promise retold: a hero like you, "
            "a wound like yours, a guide who showed the way, a measured "
            "healing. Ninety seconds of truth, then the question - could "
            "this be your story next."),
    },
    {
        "key": "objection_method",
        "name": "The Objection Handling Method",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Objections are requests for more confidence, not rejections. "
            "The LAER method handles them in four steps: Listen fully, "
            "Acknowledge the concern, Explore what sits behind it, and "
            "Respond with evidence. Roughly 60 percent of stated objections "
            "are surface-level - price often means I do not see the value "
            "yet - so the explore step, which asks what exactly concerns "
            "you, is where real selling happens."),
        "how_it_works": (
            "When the buyer objects, the seller does not argue and does not "
            "fold: listen without interrupting, acknowledge the feeling as "
            "reasonable, ask questions to find the true concern, then answer "
            "that concern with proof. If the objection is valid and the "
            "offer truly does not fit, the honest seller says so - walking "
            "away from a bad fit protects every future deal."),
        "key_points": [
            "Objections are confidence requests, not rejections.",
            "LAER: Listen, Acknowledge, Explore, Respond.",
            "About 60 percent of objections are surface-level - explore first.",
            "Never argue; never fold instantly either.",
            "Admit a genuine bad fit - honesty compounds.",
        ],
        "requirements": [
            "Learn the LAER sequence by heart.",
            "Log every objection and the true concern behind it.",
            "Prepare evidence answers for the top five objections.",
        ],
        "standards": [
            "Follow LAER in order: Listen, Acknowledge, Explore, Respond.",
            "Explore before responding - most stated objections are surface-level.",
            "Admit a genuine bad fit openly; honesty is the long-term standard."
        ],
        "citations": [CIT_ZIGLAR, CIT_SANDLER],
        "sig_lens": (
            "An objection is the buyer testing the covenant before signing "
            "it. The Signature seller listens fully, honors the doubt, digs "
            "for the true fear, and answers with evidence - or admits the "
            "fit is false, because a false covenant poisons the true ones."),
    },
    {
        "key": "price_objections",
        "name": "Handling Price Objections",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Price objections almost always mean the value is unclear, not "
            "that the price is wrong. The method: isolate the concern (is "
            "price the only thing holding you back), restate the value in "
            "the buyer numbers, break the price into smaller units, and "
            "compare against the cost of doing nothing. A 12,000 solution "
            "that saves 40,000 a year is not expensive - it is a 3.3 to 1 "
            "return, and the seller job is to make that arithmetic visible."),
        "how_it_works": (
            "The seller first checks whether price is truly the blocker or "
            "a polite cover. Then the total value is rebuilt from discovery "
            "numbers, the price is reframed per day or per user, and the "
            "cost of inaction is totaled. Discounting is the last resort, "
            "never the first - and any concession is traded for something, "
            "never given freely."),
        "key_points": [
            "Price objections usually signal unclear value.",
            "Isolate: is price the only blocker.",
            "Reframe price per day, per user, per outcome.",
            "Total the cost of doing nothing.",
            "Trade concessions; never give them freely.",
        ],
        "requirements": [
            "Build a value worksheet from each buyer discovery numbers.",
            "Practice the per-day and per-user reframes.",
            "Set discount authority limits in advance.",
        ],
        "standards": [
            "Rebuild value from the buyer discovery numbers before discussing price.",
            "Reframe price per day, per user, or per outcome; total the cost of inaction.",
            "Discounts are traded for concessions, never given freely, and set within pre-approved limits."
        ],
        "citations": [CIT_ZIGLAR, CIT_HBR],
        "sig_lens": (
            "Price is the buyer asking whether the promise is worth the "
            "vow. The Signature seller answers with the buyer own arithmetic "
            "- the saving, the return, the cost of standing still - and "
            "never cheapens the promise to win the signature."),
    },
    {
        "key": "think_over",
        "name": "Handling Think-It-Over Objections",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "I need to think about it means something is unresolved - "
            "usually a hidden concern the buyer will not name. The response "
            "is gentle and direct: I understand completely - so I can help, "
            "what specifically would you like to think through. About 70 "
            "percent of the time this surfaces the real issue, which is "
            "then handled normally. The seller then agrees a specific "
            "follow-up date - Tuesday at 10, not sometime next week."),
        "how_it_works": (
            "The seller validates the pause, asks what exactly needs "
            "thinking, and listens. If a real concern appears, it is "
            "handled with evidence. If the buyer truly needs time, the "
            "seller agrees a concrete next step with date and time, sends a "
            "short summary of value discussed, and calls exactly when "
            "promised. Vague follow-up is how think-it-over becomes never."),
        "key_points": [
            "Think-it-over hides an unnamed concern about 70 percent of the time.",
            "Ask gently what specifically needs thinking through.",
            "Handle the surfaced concern with evidence.",
            "Agree a specific date and time, never sometime.",
            "Send a value summary and call exactly when promised.",
        ],
        "requirements": [
            "Rehearse the gentle surfacing question until natural.",
            "Always leave with a dated next step.",
            "Send the summary within 24 hours.",
        ],
        "standards": [
            "Validate the pause, then ask gently what specifically needs thinking through.",
            "Never leave without a specific dated follow-up appointment.",
            "Send the value summary within 24 hours and call exactly when promised."
        ],
        "citations": [CIT_ZIGLAR, CIT_SANDLER],
        "sig_lens": (
            "When the buyer asks to pause the covenant, the Signature seller "
            "does not push and does not vanish: ask what weighs on the "
            "decision, answer it truly, and set the next meeting like a "
            "kept appointment. Patience with a date is respect; patience "
            "without one is surrender."),
    },
    {
        "key": "negotiation",
        "name": "Fundamentals of Sales Negotiation",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Negotiation is joint problem-solving over price, terms, and "
            "scope - not a contest to win. The zone of possible agreement "
            "(ZOPA) is the overlap between the seller walk-away and the "
            "buyer walk-away: if the seller must have at least 10,000 and "
            "the buyer can pay at most 14,000, the ZOPA is 4,000 wide and "
            "every deal lands inside it. Skilled negotiators trade "
            "concessions in shrinking steps and never split the difference "
            "first, because the first split anchors the rest."),
        "how_it_works": (
            "Before negotiating, the seller sets a target, a walk-away, and "
            "a list of tradable items beyond price (terms, timeline, scope, "
            "references). At the table the seller asks what matters most to "
            "the buyer, trades low-cost-to-me items for high-value-to-them "
            "ones, and makes concessions in decreasing sizes (400, then 200, "
            "then 100) to signal the bottom is near. Everything agreed is "
            "written down before leaving."),
        "key_points": [
            "Negotiation is joint problem-solving, not combat.",
            "ZOPA: the overlap between the two walk-away points.",
            "Set target, walk-away, and tradables before you start.",
            "Concede in shrinking steps; never split the difference first.",
            "Write down everything agreed before leaving.",
        ],
        "requirements": [
            "Define your walk-away price before every negotiation.",
            "List at least five tradable items beyond price.",
            "Confirm the full agreement in writing the same day.",
        ],
        "standards": [
            "Walk-away points are set before negotiation begins, never improvised under pressure.",
            "Every concession is traded for something of value - nothing is given freely.",
            "Final terms are confirmed in writing before work starts.",
        ],
        "citations": [CIT_HBR, CIT_MILLER],
        "sig_lens": (
            "Negotiation is the balancing of the covenant: both sides state "
            "their vows plainly, and the deal is the overlap where both can "
            "keep them. The Signature negotiator trades honestly, concedes "
            "in honest steps, and writes the balance down so neither side "
            "forgets."),
    },
    {
        "key": "trial_closes",
        "name": "Trial Closes",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A trial close is a small question that tests whether the buyer "
            "is ready to decide, asked throughout the sale - not just at "
            "the end. Examples: does this solve the reporting problem, how "
            "does this compare to what you use now, what would stop us "
            "moving forward. If 3 out of 4 trial closes come back positive, "
            "the buyer is ready and the seller can ask for the decision; "
            "if they come back hesitant, more discovery is needed first."),
        "how_it_works": (
            "After each major point the seller asks a low-pressure check: "
            "a question whose yes means progress and whose no reveals what "
            "is missing. Positive answers are noted; concerns are handled "
            "on the spot. Trial closes keep the seller from guessing - "
            "instead of wondering if the buyer is ready, the seller has "
            "asked four times and knows."),
        "key_points": [
            "Trial closes test readiness throughout the sale, not just at the end.",
            "A yes means progress; a no reveals what is missing.",
            "3 out of 4 positive means ready to ask for the decision.",
            "Hesitation means more discovery, not more pressure.",
            "Trial closes replace guessing with knowing.",
        ],
        "requirements": [
            "Plan four trial closes into every presentation.",
            "Log the answers and act on hesitation immediately.",
            "Never ask for the final decision before trial closes pass.",
        ],
        "standards": [
            "Readiness is tested with questions, never assumed from politeness.",
            "A hesitant trial close triggers more discovery, not more pressure.",
            "Log trial-close answers as part of the opportunity record.",
        ],
        "citations": [CIT_ZIGLAR, CIT_SANDLER],
        "sig_lens": (
            "The trial close is the covenant tested in small vows before the "
            "great one: does this heal the wound, does this outweigh the "
            "old way, what still holds you back. The Signature seller asks "
            "early and often, and only seals when the small vows hold."),
    },
    {
        "key": "closing",
        "name": "Closing Techniques",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Closing is simply asking for the decision the buyer is ready "
            "to make. The classic techniques all share one rule: ask "
            "directly and then be quiet. The direct close (shall we move "
            "forward), the choice close (Tuesday or Thursday for delivery), "
            "the summary close (recap of agreed value, then the question), "
            "and the next-step close (agreeing the dated plan) each fit "
            "different buyers. Studies of sales calls show the seller who "
            "asks for the order plainly closes about twice as often as the "
            "one who hopes the buyer volunteers."),
        "how_it_works": (
            "The seller picks the close that matches the buyer style, asks "
            "the question in plain words, and then stops talking - the "
            "first one to speak after the question loses leverage. A yes "
            "is confirmed in writing; a no is treated as an objection and "
            "handled; a maybe becomes a dated next step. Closing is never "
            "a surprise - trial closes have already shown the buyer is "
            "ready."),
        "key_points": [
            "Closing is asking for the decision, plainly and directly.",
            "Ask, then be silent - the first to speak loses leverage.",
            "Match the technique to the buyer: direct, choice, summary, next-step.",
            "A no is an objection to handle; a maybe is a dated next step.",
            "Asking plainly closes about twice as often as hoping.",
        ],
        "requirements": [
            "Learn four closes and match each to a buyer style.",
            "Rehearse the silence after the question.",
            "Confirm every yes in writing the same day.",
        ],
        "standards": [
            "The decision is asked for explicitly - never assumed or hoped for.",
            "After the closing question, the seller waits in silence.",
            "Every closed deal is confirmed in writing with dates and owners.",
        ],
        "citations": [CIT_ZIGLAR, CIT_TRACY],
        "sig_lens": (
            "The close is the sealing of the covenant: the promise stated, "
            "the vow asked, the silence held while the buyer decides. The "
            "Signature seller asks plainly, waits quietly, and writes the "
            "seal down - a covenant unrecorded is a covenant at risk."),
    },
    {
        "key": "followup",
        "name": "Follow-Up Systems",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Most sales close after multiple contacts: industry studies "
            "routinely find that 80 percent of sales need five or more "
            "follow-ups, yet nearly half of sellers stop after one. A "
            "follow-up system is a scheduled cadence - for example day 1 "
            "thank-you, day 3 value note, day 7 check-in, day 14 new proof "
            "point, day 30 final check - each touch adding value, never just "
            "checking in. The system, not willpower, keeps the seller "
            "showing up."),
        "how_it_works": (
            "Every opportunity gets a cadence with dates, channels, and a "
            "value item per touch (an article, a reference, a new number). "
            "The seller works the cadence from the calendar or CRM until "
            "the buyer decides or asks to stop. After the sale, follow-up "
            "continues: delivery check, 30-day success call, 90-day review - "
            "because kept customers buy again and refer."),
        "key_points": [
            "80 percent of sales need five or more follow-ups.",
            "Each touch adds value; never just check in.",
            "Cadence example: day 1, 3, 7, 14, 30 with a value item each.",
            "The system keeps you showing up; willpower does not.",
            "Post-sale follow-up protects revenue and seeds referrals.",
        ],
        "requirements": [
            "Assign every opportunity a written cadence with dates.",
            "Prepare a value item for each scheduled touch.",
            "Run post-sale checks at delivery, 30 days, and 90 days.",
        ],
        "standards": [
            "No opportunity sits without a dated next touch.",
            "Every follow-up carries value for the buyer, not just a nudge.",
            "Post-sale follow-up is scheduled at close, not improvised later.",
        ],
        "citations": [CIT_GITOMER, CIT_HBR],
        "sig_lens": (
            "Follow-up is the tending of the covenant after the sealing: "
            "the promise checked at delivery, at thirty days, at ninety. "
            "The Signature seller shows up on schedule with something of "
            "value, because a covenant tended grows and a covenant ignored "
            "withers."),
    },
    {
        "key": "referrals",
        "name": "Referral Selling",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Referred prospects close faster and at higher rates than cold "
            "ones, because trust transfers with the introduction. The "
            "arithmetic: a seller with 40 happy customers who each yield "
            "0.5 qualified referrals a year gains 20 warm introductions "
            "annually - roughly two months of cold prospecting output for "
            "free. Referrals are asked for, not waited for: at the moment "
            "of delivered value the seller asks who else the customer knows "
            "with the same problem."),
        "how_it_works": (
            "Right after a success - a solved problem, a compliment, a "
            "renewal - the seller asks for introductions by name, not in "
            "general: who do you know at a company like yours facing the "
            "reporting problem we just fixed. The seller makes it easy: a "
            "short forwardable note, a clear ask, and a thank-you whatever "
            "happens. Every referral is followed up within 48 hours."),
        "key_points": [
            "Trust transfers with the introduction - referrals close best.",
            "40 customers at 0.5 referrals each equals 20 warm leads a year.",
            "Ask at the moment of delivered value, by name, not in general.",
            "Provide a forwardable note to make it easy.",
            "Follow up every referral within 48 hours.",
        ],
        "requirements": [
            "Ask for referrals at every delivered success.",
            "Keep a forwardable introduction note ready.",
            "Thank every referrer regardless of outcome.",
        ],
        "standards": [
            "Referrals are requested explicitly at moments of delivered value.",
            "The referrer is never embarrassed - asks are specific and easy to decline.",
            "Every referral receives follow-up within 48 hours.",
        ],
        "citations": [CIT_GITOMER, CIT_CIALDINI],
        "sig_lens": (
            "A referral is one covenant recommending another: a kept promise "
            "speaks, and a new buyer listens. The Signature seller earns "
            "the recommendation by keeping the first promise fully, asks at "
            "the moment of proof, and honors the trust transferred."),
    },
    {
        "key": "upsell",
        "name": "Upselling and Cross-Selling",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Upselling moves the buyer to a better-fit version; cross-selling "
            "adds complementary items that complete the solution. Done "
            "ethically both serve the buyer: the right upgrade saves money "
            "later, the right add-on makes the first purchase work. The "
            "math matters: raising the attach rate from 1.0 to 1.3 items "
            "per order on 200 orders a year at 500 average item value adds "
            "30,000 in annual revenue with zero new customers. The rule is "
            "fit first - recommend only what the buyer genuinely benefits "
            "from."),
        "how_it_works": (
            "After the main decision is secure, the seller suggests the "
            "upgrade or add-on in terms of the buyer goal: since you need "
            "the reports weekly, the automated tier pays for itself in two "
            "months. The buyer can decline with zero pressure, and the "
            "seller accepts it cleanly. Every recommendation is logged with "
            "the reason it fits, so patterns of genuine fit emerge."),
        "key_points": [
            "Upsell: better-fit version. Cross-sell: completing add-ons.",
            "Fit first - recommend only genuine buyer benefit.",
            "Attach rate 1.0 to 1.3 on 200 orders at 500 adds 30,000 yearly.",
            "Frame in the buyer goal, accept no cleanly.",
            "Log the fit reason for every recommendation.",
        ],
        "requirements": [
            "Map genuine upgrades and add-ons for each core offer.",
            "Suggest only after the main decision is secure.",
            "Accept every decline gracefully and immediately.",
        ],
        "standards": [
            "Recommendations serve the buyer fit first, quota second.",
            "No pressure on declines - the relationship outranks the add-on.",
            "Track attach rate and the fit reasons behind it.",
        ],
        "citations": [CIT_GITOMER, CIT_HBR],
        "sig_lens": (
            "The upsell is the covenant extended, never inflated: a better "
            "fit offered because it serves, an add-on because it completes. "
            "The Signature seller recommends only what the buyer would "
            "thank them for later - and takes no cleanly, without a shadow."),
    },
    {
        "key": "spin",
        "name": "SPIN Selling and Consultative Method",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "SPIN Selling, from Neil Rackham research on 35,000 sales calls, "
            "is the consultative method for complex sales: Situation "
            "questions gather facts, Problem questions surface difficulties, "
            "Implication questions develop the cost of the problem, and "
            "Need-payoff questions get the buyer to state the value of "
            "solving it. Rackham found that successful calls used far more "
            "Implication and Need-payoff questions - the buyer convinces "
            "themselves, which beats any seller argument."),
        "how_it_works": (
            "The seller plans SPIN questions in sequence: a few situation "
            "questions (kept short - buyers dislike long fact-finding), "
            "then problem questions until two or three real pains surface, "
            "then implication questions that multiply the pain into money "
            "and risk, then need-payoff questions where the buyer describes "
            "the value of a solution. The presentation then simply mirrors "
            "what the buyer already said they need."),
        "key_points": [
            "SPIN: Situation, Problem, Implication, Need-payoff.",
            "Based on research across 35,000 real sales calls.",
            "Implication questions turn problems into costs.",
            "Need-payoff gets the buyer to state the value themselves.",
            "Keep situation questions short; buyers dislike fact-finding.",
        ],
        "requirements": [
            "Write SPIN sequences for your three most common buyer problems.",
            "Practice implication questions until they feel natural.",
            "Mirror the buyer stated needs in your presentation.",
        ],
        "standards": [
            "Situation questions are researched in advance and kept brief.",
            "The buyer states the value of solving the problem before the seller presents.",
            "Question plans are written before complex calls, not improvised.",
        ],
        "citations": [CIT_RACKHAM, CIT_MILLER],
        "sig_lens": (
            "SPIN is the Signature diagnosis perfected: gather the facts "
            "swiftly, name the wound, count its cost aloud, and let the "
            "buyer speak the value of healing. The seller is the physician "
            "of the covenant - the buyer prescribes their own cure."),
    },
    {
        "key": "value_selling",
        "name": "Value-Based Selling",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Value-based selling prices and positions the offer on the "
            "economic outcome it creates, not on its cost or features. The "
            "core tool is the ROI case: a 25,000 system that saves 400 "
            "hours a year at 75 per hour returns 30,000 yearly - a 120 "
            "percent first-year return with payback in 10 months. Sellers "
            "build the case from the buyer own numbers during discovery, "
            "so the buyer cannot dispute the inputs."),
        "how_it_works": (
            "During discovery the seller captures the buyer current costs, "
            "waste, and risks in hard numbers. The value case is then built "
            "visibly: current cost, cost with the solution, difference, "
            "payback period, three-year return. Conservative assumptions "
            "are used throughout - a value case that survives the buyer "
            "finance team is the one that closes."),
        "key_points": [
            "Sell the economic outcome, not the features or the cost.",
            "Build ROI from the buyer own discovery numbers.",
            "Example: 25,000 cost, 30,000 yearly saving, 10-month payback.",
            "Use conservative assumptions that survive finance scrutiny.",
            "The buyer who built the inputs cannot dispute the outputs.",
        ],
        "requirements": [
            "Capture hard cost numbers in every discovery.",
            "Build a one-page value case for each major opportunity.",
            "Stress-test assumptions with the buyer before presenting.",
        ],
        "standards": [
            "Value cases use the buyer verified numbers, never vendor guesses.",
            "Assumptions are conservative and shown openly.",
            "Payback and ROI are stated alongside the risks, not instead of them.",
        ],
        "citations": [CIT_HBR, CIT_RACKHAM],
        "sig_lens": (
            "Value-based selling weighs the covenant on honest scales: the "
            "cost of the promise against the gold of the outcome, counted "
            "in the buyer own coin. The Signature scales never tilt - "
            "conservative numbers, open assumptions, and the truth even "
            "when it narrows the margin."),
    },
    {
        "key": "enterprise",
        "name": "Enterprise and Complex Sales Cycles",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Enterprise sales run 6 to 18 months, involve 6 to 10 decision "
            "makers, and die most often from no decision rather than from "
            "losing to a competitor. The cycle has five gates: access to "
            "power, problem agreement, solution fit, commercial terms, and "
            "implementation planning. A deal is only real when every gate "
            "has a named owner and a date; a 12-month cycle with 5 gates "
            "means each gate must advance roughly every 10 weeks or the "
            "deal is stalling."),
        "how_it_works": (
            "The seller maps the buying organization, identifies the "
            "economic buyer and the key influencers, and builds a mutual "
            "action plan with dated steps owned by both sides. Each gate "
            "is confirmed before the next opens. When a gate stalls past "
            "its date, the seller re-qualifies rather than pushing - "
            "stalled enterprise deals rarely restart on pressure."),
        "key_points": [
            "Enterprise cycles run 6-18 months with 6-10 decision makers.",
            "Deals die from no decision more than from competitors.",
            "Five gates: access, problem, fit, terms, implementation.",
            "Every gate needs a named owner and a date.",
            "A stalled gate means re-qualify, not push harder.",
        ],
        "requirements": [
            "Map every stakeholder and their role before proposing.",
            "Build a mutual action plan with dated, owned steps.",
            "Re-qualify any gate that misses its date by two weeks.",
        ],
        "standards": [
            "No proposal without confirmed access to the economic buyer.",
            "Mutual action plans carry dates and owners on both sides.",
            "Stalled deals are re-qualified honestly, not forecasted hopefully.",
        ],
        "citations": [CIT_MILLER, CIT_CHALLENGER],
        "sig_lens": (
            "The enterprise covenant is sealed by many hands over many "
            "moons: each gate a vow, each owner a witness, each date a "
            "promise. The Signature seller maps every hand, dates every "
            "vow, and never mistakes a stalled covenant for a living one."),
    },
    {
        "key": "consensus",
        "name": "Multi-Stakeholder Consensus",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "In complex purchases the average buying group now exceeds half "
            "a dozen people, each with different fears: finance fears cost, "
            "IT fears risk, users fear change, executives fear failure. "
            "Consensus is built by giving each stakeholder their own win: "
            "the same solution is presented as savings to finance, safety "
            "to IT, ease to users, and growth to the executive. With 6 "
            "stakeholders each needing a personal yes, the seller runs 6 "
            "parallel value cases, not one."),
        "how_it_works": (
            "The seller identifies every stakeholder, learns each one "
            "personal success criteria, and arms the internal champion with "
            "tailored proof for each colleague. Meetings are prepared "
            "stakeholder by stakeholder. The seller never lets one contact "
            "be the single thread - if the champion leaves, the deal must "
            "survive on its other relationships."),
        "key_points": [
            "Buying groups exceed 6 people with different fears.",
            "Each stakeholder needs their own personal win.",
            "Arm the champion with tailored proof per colleague.",
            "Never single-thread a deal on one contact.",
            "Map fears: finance-cost, IT-risk, users-change, execs-failure.",
        ],
        "requirements": [
            "List every stakeholder and their success criteria.",
            "Prepare tailored proof for each role.",
            "Build at least three independent relationships per account.",
        ],
        "standards": [
            "Every stakeholder win is truthful - the same solution, honestly framed per role.",
            "Single-threaded deals are flagged as at-risk in the forecast.",
            "The champion is equipped, never used as a messenger alone.",
        ],
        "citations": [CIT_CHALLENGER, CIT_MILLER],
        "sig_lens": (
            "A covenant of many hands must be sworn hand by hand: finance "
            "hears the saving, the engineers hear the safety, the users "
            "hear the ease, the leaders hear the growth - one true promise, "
            "six honest framings. The Signature seller leaves no hand "
            "unsworn and no thread single."),
    },
    {
        "key": "key_accounts",
        "name": "Key Account Management",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Key accounts - the top 20 percent of customers - often produce "
            "80 percent of revenue, so they get plans, not just attention. "
            "A key account plan covers the customer goals, the stakeholder "
            "map, the share of their spending you hold, growth plays, and "
            "risks. If a 2,000,000 account grows 10 percent a year through "
            "planned expansion, it adds 200,000 annually - the cheapest "
            "revenue a company can earn."),
        "how_it_works": (
            "Each key account gets a written annual plan reviewed quarterly "
            "with the customer: their objectives, your contribution, joint "
            "initiatives with dates, and an honest risk register. The "
            "account manager meets stakeholders at multiple levels, tracks "
            "satisfaction in numbers, and brings one new idea per quarter - "
            "key accounts stay because they keep gaining, not because of "
            "habit."),
        "key_points": [
            "Top 20 percent of customers often yield 80 percent of revenue.",
            "Every key account gets a written annual plan, reviewed quarterly.",
            "Plan covers goals, stakeholders, share, growth plays, risks.",
            "10 percent growth on a 2,000,000 account adds 200,000 yearly.",
            "Bring one new idea per quarter to earn the renewal.",
        ],
        "requirements": [
            "Write annual plans for every key account.",
            "Review the plan jointly with the customer quarterly.",
            "Track satisfaction and share-of-spending in numbers.",
        ],
        "standards": [
            "Key account plans are written, dated, and jointly reviewed.",
            "Growth plays are proposed as ideas, never imposed.",
            "Risk registers are honest - including risks you cause.",
        ],
        "citations": [CIT_MILLER, CIT_HBR],
        "sig_lens": (
            "The key account is a covenant renewed yearly in writing: their "
            "aims, your part in them, the shared road ahead, the dangers "
            "named aloud. The Signature keeper of great accounts brings a "
            "new gift each quarter, for a covenant that stops growing "
            "starts dying."),
    },
    {
        "key": "pipeline",
        "name": "Pipeline Management and Forecasting",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A pipeline is the ranked list of open opportunities with stage, "
            "value, and close date; a forecast is the honest prediction of "
            "what will close. The weighted forecast multiplies each deal by "
            "its stage probability: four deals of 50,000 at 25, 50, 75, and "
            "90 percent weight to 12,500 + 25,000 + 37,500 + 45,000 = "
            "120,000 expected. Pipeline coverage of 3 times quota is the "
            "healthy standard - 300,000 in pipe for a 100,000 quarter."),
        "how_it_works": (
            "Every opportunity carries a stage with exit criteria, a value, "
            "and a close date - all three kept current weekly. The seller "
            "reviews the pipe every Monday: stalled deals are re-qualified "
            "or removed, dates are corrected, new opportunities are added "
            "from prospecting. Forecasts are built bottom-up from the pipe, "
            "never top-down from the quota."),
        "key_points": [
            "Pipeline: ranked open opportunities with stage, value, close date.",
            "Weighted forecast: value times stage probability, summed.",
            "Example: four 50,000 deals weight to 120,000 expected.",
            "Healthy coverage is 3 times quota.",
            "Forecast bottom-up from the pipe, never top-down from quota.",
        ],
        "requirements": [
            "Keep stage, value, and close date current on every deal.",
            "Review the full pipeline every Monday.",
            "Remove or re-qualify stalled deals instead of carrying them.",
        ],
        "standards": [
            "Stage probabilities reflect your own history, not optimism.",
            "Close dates move only with a stated buyer reason.",
            "Forecasts are built from the pipeline upward.",
        ],
        "citations": [CIT_HBR, CIT_MILLER],
        "sig_lens": (
            "The pipeline is the covenant ledger: every open vow ranked, "
            "valued, and dated; the forecast the honest reading of which "
            "vows will be kept. The Signature ledger carries no ghosts - "
            "stalled vows are faced, dated anew, or released with honor."),
    },
    {
        "key": "crm",
        "name": "CRM Discipline",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A CRM (customer relationship manager) is the seller memory: "
            "every contact, conversation, commitment, and document in one "
            "place. Discipline means logging calls the same day, keeping "
            "next steps dated on every record, and holding data completeness "
            "above 90 percent - 45 complete records out of 50. A seller who "
            "saves 30 minutes a day through instant recall and clean "
            "handoffs reclaims 10 hours a month for actual selling."),
        "how_it_works": (
            "After every meaningful contact the seller logs what was "
            "learned, what was promised, and the dated next step - within "
            "the hour, not at week end. Records carry the stakeholder map, "
            "the value case, and the full history, so any colleague can "
            "continue the relationship. Monthly, the seller audits their "
            "own data completeness and fixes the gaps."),
        "key_points": [
            "The CRM is the seller memory - contacts, talks, promises, documents.",
            "Log within the hour; keep next steps dated on every record.",
            "Hold data completeness above 90 percent.",
            "30 minutes saved daily equals 10 selling hours monthly.",
            "Any colleague must be able to continue from your records.",
        ],
        "requirements": [
            "Log every meaningful contact the same day.",
            "Keep a dated next step on every open record.",
            "Audit your own data completeness monthly.",
        ],
        "standards": [
            "Records are complete enough for a colleague to take over cleanly.",
            "Commitments made to buyers are logged verbatim with dates.",
            "Customer data is kept private and handled with care.",
        ],
        "citations": [CIT_HBR, CIT_GITOMER],
        "sig_lens": (
            "The CRM is the covenant archive: every word spoken, every vow "
            "dated, every hand mapped, kept within the hour while memory is "
            "fresh. The Signature archive is complete above ninety in a "
            "hundred, for a forgotten vow is a vow half-broken."),
    },
    {
        "key": "ethics",
        "name": "Ethics of Selling",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Ethical selling means the buyer would thank you after learning "
            "everything you knew: no deception, no manipulation, no "
            "pressure, no selling what does not fit. The five-rule test: "
            "tell the truth about the product, disclose what matters, never "
            "manufacture urgency, respect a no, and walk away from bad fits. "
            "Unethical wins are expensive - one exposed deception destroys "
            "the trust that a hundred honest sales built."),
        "how_it_works": (
            "Before recommending, the seller runs the sunlight test: would "
            "I be proud if the buyer knew all of this. Limits and downsides "
            "are disclosed before the buyer discovers them. Pressure "
            "tactics - false deadlines, invented scarcity, fear stories - "
            "are refused outright. When the fit is wrong, the seller says so "
            "and, where possible, points the buyer to a better answer."),
        "key_points": [
            "The buyer would thank you after learning everything you knew.",
            "Five rules: truth, disclosure, no fake urgency, respect no, walk from bad fits.",
            "Disclose downsides before the buyer discovers them.",
            "Pressure tactics are refused outright.",
            "One exposed deception destroys a hundred honest sales of trust.",
        ],
        "requirements": [
            "Run the sunlight test before every recommendation.",
            "Disclose material limits in writing.",
            "Document and walk away from bad fits.",
        ],
        "standards": [
            "No deception, manipulation, or pressure - ever, at any quota.",
            "Material facts and limits are disclosed proactively.",
            "Bad fits are declined openly, with a better path offered where possible.",
        ],
        "citations": [CIT_CIALDINI, CIT_CARNEGIE],
        "sig_lens": (
            "Ethics is the covenant itself: without truth there is no "
            "promise, only noise. The Signature seller holds the five rules "
            "as law - truth, disclosure, honest timing, honored refusal, "
            "and the walked-away bad fit - for the covenant outlives every "
            "quota."),
    },
    {
        "key": "winloss",
        "name": "Win-Loss Analysis",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Win-loss analysis is the disciplined study of why deals were "
            "won or lost, done by interviewing buyers after the decision. "
            "The pattern is usually humbling: in many programs the top loss "
            "reason is no decision (about 40 percent), followed by price "
            "value gaps (25 percent) and relationship gaps (20 percent). "
            "Each interview asks what decided it, what nearly changed it, "
            "and what advice the buyer gives - then the answers change "
            "training, messaging, and the offer itself."),
        "how_it_works": (
            "A neutral interviewer - not the seller - calls recent buyers "
            "and lost prospects with five open questions. Answers are coded "
            "into reasons, counted, and reported quarterly. The top two "
            "loss reasons each get an owner and a fix with a date. Wins are "
            "studied equally: what to repeat is as valuable as what to fix."),
        "key_points": [
            "Study wins and losses by interviewing buyers after decisions.",
            "Typical split: 40 percent no-decision, 25 percent value gap, 20 percent relationship.",
            "Use a neutral interviewer, never the seller.",
            "Code reasons, count them, report quarterly.",
            "Top two loss reasons each get an owner and a dated fix.",
        ],
        "requirements": [
            "Interview a sample of wins and losses every quarter.",
            "Code and count reasons; report the top five.",
            "Assign owners and dates to fix the top two loss reasons.",
        ],
        "standards": [
            "Interviews are conducted by a neutral party for honest answers.",
            "Findings are reported with counts, not anecdotes.",
            "Fixes are owned, dated, and tracked to completion.",
        ],
        "citations": [CIT_HBR, CIT_RACKHAM],
        "sig_lens": (
            "Win-loss is the covenant examined after the sealing: why was "
            "the vow kept, why was it broken, what would the buyer teach. "
            "The Signature seller hears the verdict from a neutral voice, "
            "counts the reasons honestly, and repairs what the count "
            "reveals - the next covenant is built on the last one lessons."),
    },
    {
        "key": "challenger",
        "name": "Insight Selling: The Challenger Method",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The Challenger Sale, from research across 6,000 sellers, found "
            "that top performers teach rather than please: they bring "
            "insights the buyer did not have, reframe the problem, and "
            "lead to their solution. The method runs teach, tailor, take "
            "control: teach a surprising insight about the buyer business, "
            "tailor it to each stakeholder, and take control of the process "
            "with a clear path forward. It is insight with backbone - "
            "never aggression, always grounded in the buyer reality."),
        "how_it_works": (
            "The seller arrives with one insight the buyer likely has not "
            "considered - a cost they are blind to, a risk mispriced, an "
            "opportunity missed - supported by evidence. The insight is "
            "tailored per stakeholder, then the seller proposes the "
            "decision path with dates. Pushback is welcomed as engagement; "
            "the seller holds the point with data, not volume."),
        "key_points": [
            "Top performers teach with insight rather than pleasing.",
            "Research base: 6,000 sellers studied.",
            "Teach, tailor, take control - in that order.",
            "Bring one surprising, evidenced insight per meeting.",
            "Backbone means data and conviction, never aggression.",
        ],
        "requirements": [
            "Develop one evidenced insight per target industry.",
            "Tailor the insight to each stakeholder role.",
            "Propose the decision path with dates at every advance.",
        ],
        "standards": [
            "Insights are evidenced and relevant to the buyer business - never generic provocations.",
            "Pushback is treated as engagement and answered with data.",
            "The method teaches; it never manipulates or pressures.",
        ],
        "citations": [CIT_CHALLENGER, CIT_HBR],
        "sig_lens": (
            "The Challenger is the covenant deepened by teaching: the seller "
            "brings a truth the buyer had not seen, fits it to each hand "
            "at the table, and leads the way forward with dates. The "
            "Signature teacher speaks with evidence and backbone - insight "
            "offered as a gift, never wielded as a weapon."),
    },
    {
        "key": "relationship_engine",
        "name": "The Relationship and Referral Engine",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The relationship engine turns one-time buyers into lifetime "
            "advocates who buy again and send others. The economics: "
            "keeping a customer costs roughly one-fifth of winning a new "
            "one, and a 5 percent lift in retention can raise profits 25 to "
            "95 percent. The engine has four gears: deliver excellently, "
            "check in with value, ask for the next need, and systematize "
            "referrals - each customer touched quarterly with something "
            "useful, each success converted into introductions."),
        "how_it_works": (
            "Every customer enters a lifetime cadence: delivery check, "
            "30-day success call, quarterly value touches, annual business "
            "review. Satisfaction is measured, not assumed. At each proof "
            "of value the seller asks for referrals and for the next need. "
            "Advocates are recognized and thanked publicly; their stories "
            "become the proof that powers new prospecting."),
        "key_points": [
            "Retention costs about one-fifth of acquisition.",
            "A 5 percent retention lift can raise profits 25-95 percent.",
            "Four gears: deliver, check in, ask next need, systematize referrals.",
            "Touch every customer quarterly with something useful.",
            "Advocate stories power new prospecting.",
        ],
        "requirements": [
            "Put every customer on a lifetime quarterly cadence.",
            "Measure satisfaction; never assume it.",
            "Convert each success into referrals and the next need.",
        ],
        "standards": [
            "Retention is measured and reported like revenue.",
            "Referral asks happen at proven value moments only.",
            "Advocates are recognized and thanked; their trust is never spent cheaply.",
        ],
        "citations": [CIT_GITOMER, CIT_HBR],
        "sig_lens": (
            "The relationship engine is the covenant made everlasting: kept "
            "promises compounding into loyalty, loyalty into advocacy, "
            "advocacy into new covenants. The Signature seller tends every "
            "customer quarterly with something of value, for the kept "
            "promise is the seed of the next hundred."),
    },
]
