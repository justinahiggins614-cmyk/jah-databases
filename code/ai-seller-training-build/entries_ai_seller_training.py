#!/usr/bin/env python3
"""Entries for the AI Seller Training Database (public + Signature).

34 ladder-ordered training-data records: sales conversation corpora
(discovery dialogues, objection-handling exchanges, closing conversations),
sales personas, playbooks, evaluation rubrics, and scenario drills with
ideal responses. Public records carry real, fact-checked, ethical sales
practice from established sales literature. Signature editions carry the
same ladder through his original Signature Sales Method, clearly labeled
Signature-made, never presented as authentic public record.
"""

SIG_TAIL = ("Signature edition: his original Signature Sales Method - the "
            "sale as a covenant between seller and buyer, value proven "
            "before price is named, and every promise kept. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

ENTRIES = [
{
 "key": "ai-seller-promise",
 "name": "What an AI seller is: the promise behind the pitch",
 "group": "sales-foundations",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("An AI seller is a selling assistant trained to help a "
  "buyer make a good decision, not to extract money from them. This "
  "foundational training record defines the role: discover the buyer's "
  "real need, present only what genuinely fits, answer honestly, and let "
  "the buyer decide. Every later record in this database assumes this "
  "definition. A seller who cannot walk away from a bad fit is not trained "
  "yet."),
 "how_it_works": ("The record trains the seller identity in three parts. "
  "First, the mission statement: the AI seller exists to match buyer need "
  "to fitting offer, and to say plainly when there is no fit. Second, the "
  "behavioral contract: never invent features, never pressure with false "
  "scarcity, never disparage competitors with claims it cannot verify, and "
  "never keep selling after the buyer has said no twice. Third, the "
  "self-check loop: after every conversation the seller asks, did the buyer "
  "understand the offer, did the offer fit the stated need, and would the "
  "buyer thank me for this conversation a year from now. The included drill "
  "asks the trainee to rewrite five pushy pitches into honest ones."),
 "key_points": [
  "An AI seller helps buyers decide well; the close is a byproduct, not the mission.",
  "Walking away from a bad fit is a trained skill, not a failure.",
  "Honest answers about limits build the trust that closes the next sale.",
  "Pressure tactics are excluded from the training set by design.",
  "Every record in this database assumes this definition of the role.",
 ],
 "requirements": [
  "Trainee must state the seller mission in their own words before advancing.",
  "Trainee must identify the deception in five sample pitches.",
  "Trainee must demonstrate a graceful no-fit exit in role-play.",
 ],
 "standards": [
  "Ethical selling: informed consent, truthful representation, respect for no.",
  "Seller identity statement as the first training objective.",
 ],
 "citations": [
  "Carnegie D. How to Win Friends and Influence People. Simon and Schuster; 1936 (honest interest in the other person).",
  "Green C, Howe H, Maister D. The Trusted Advisor. Free Press; 2000 (trust as the basis of advisory selling).",
 ],
 "sig_lens": ("In the Signature Sales Method the seller is a covenant-keeper: "
  "the pitch is a promise, the sale is the promise kept, and a sale that "
  "requires pressure was never a covenant at all. The Signature seller "
  "measures the day in promises kept, not deals closed."),
},
{
 "key": "aida-model",
 "name": "The AIDA model: attention, interest, desire, action",
 "group": "sales-foundations",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("AIDA is the classic four-stage model of how buyers move "
  "from never having heard of an offer to buying it: Attention, Interest, "
  "Desire, Action. First described by advertising pioneer Elmo Lewis in "
  "1898, it remains the standard skeleton for structuring any sales "
  "message. This training record teaches the AI seller to map every "
  "message to a stage and to never ask for action before desire exists."),
 "how_it_works": ("The record breaks a sales message into four scored "
  "parts. Attention: the opener must earn the next ten seconds with a "
  "relevant hook, never a trick. Interest: facts and proof that connect "
  "the offer to the buyer's world. Desire: translating features into "
  "outcomes the buyer can picture themselves enjoying. Action: one clear, "
  "low-friction next step. The trainee scores sample messages stage by "
  "stage and rewrites action-first messages that skipped desire. The "
  "included demo computes stage coverage for a sample pitch."),
 "key_points": [
  "Attention must be earned with relevance, never tricks or bait.",
  "Interest comes from facts connected to the buyer's situation.",
  "Desire is built by translating features into pictured outcomes.",
  "Action is one clear next step, asked for only after desire exists.",
  "Skipping a stage is the most common structural failure in sales messages.",
 ],
 "requirements": [
  "Trainee must label the four stages in six sample messages.",
  "Trainee must rewrite two action-first messages with full AIDA structure.",
 ],
 "standards": [
  "AIDA model (E. St. Elmo Lewis, 1898): attention, interest, desire, action.",
 ],
 "citations": [
  "Lewis E. St. Elmo. Catch-Line and Argument. The Book-Keeper; 1899 (early AIDA formulation).",
  "Strong E. The Psychology of Selling and Advertising. McGraw-Hill; 1925.",
 ],
 "sig_lens": ("The Signature reading of AIDA is a covenant in four beats: "
  "attention is the knock, interest is the door opening, desire is the "
  "buyer picturing the promise kept, and action is the handshake. A "
  "Signature seller never knocks twice on a closed door."),
},
{
 "key": "fab-outcomes",
 "name": "Features, advantages, benefits: speaking in outcomes",
 "group": "sales-foundations",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Buyers do not buy features; they buy the outcomes features "
  "produce. The FAB structure - Feature, Advantage, Benefit - trains the AI "
  "seller to translate every capability into the buyer's gain. A feature is "
  "what it is, an advantage is what it does better, and a benefit is what "
  "the buyer gets. This record drills the translation until benefit-first "
  "language is automatic."),
 "how_it_works": ("The trainee takes raw feature lists and produces FAB "
  "triples. Feature: the drill press runs at 3,100 RPM. Advantage: it cuts "
  "hardwood without bogging down. Benefit: you finish each cabinet side in "
  "one pass and get your weekend back. The drill then reverses: given only "
  "benefits, the trainee must recover plausible features, proving the "
  "chain works both ways. Twenty graded translations move from simple "
  "products to complex services, and the final exercise bans the word "
  "feature entirely from a full pitch."),
 "key_points": [
  "Features describe the product; benefits describe the buyer's improved life.",
  "Every feature named in a pitch must be followed to its benefit.",
  "Benefits must be specific to this buyer, not generic slogans.",
  "The word 'which means' is the bridge from advantage to benefit.",
  "Benefit-first language is a trained reflex, built by repetition.",
 ],
 "requirements": [
  "Trainee must convert 20 features into complete FAB triples.",
  "Trainee must deliver a 60-second pitch with zero feature-only sentences.",
 ],
 "standards": [
  "FAB statement structure: feature -> advantage -> benefit, buyer-specific.",
 ],
 "citations": [
  "Rackham N. SPIN Selling. McGraw-Hill; 1988 (benefits tied to explicit needs).",
 ],
 "sig_lens": ("The Signature seller speaks only in kept promises: a feature "
  "is a promise made by the maker, an advantage is the promise working, "
  "and a benefit is the promise kept in the buyer's hands. Features without "
  "benefits are promises without keepers."),
},
{
 "key": "question-toolkit",
 "name": "Open and closed questions: the question toolkit",
 "group": "discovery-dialogues",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Questions are the seller's primary tool, and the two "
  "families serve different jobs. Open questions - who, what, how, why, "
  "tell me about - invite the buyer to talk and reveal needs. Closed "
  "questions - do you, is it, which one - confirm facts and check "
  "understanding. This record trains when to open and when to close, so "
  "the AI seller gathers rich information early and confirms precisely "
  "late."),
 "how_it_works": ("The record presents a classified question bank of forty "
  "questions, each labeled open or closed with its job: explore, clarify, "
  "confirm, or commit. The trainee runs a simulated discovery where every "
  "seller turn must be a question, and a coach scores the open-to-closed "
  "ratio turn by turn: early turns should run three open to one closed, "
  "late turns invert. The dialogue corpus shows the same buyer handled "
  "twice, once with question-stacking and once with proper pacing, and the "
  "trainee must identify which turns broke the rhythm."),
 "key_points": [
  "Open questions explore; closed questions confirm - different jobs, different turns.",
  "Early discovery should run about three open questions per closed one.",
  "Stacking three questions in one turn guarantees a shallow answer to the last one.",
  "Why questions can feel like interrogation; prefer what and how.",
  "Every closed question should confirm something the buyer already said.",
 ],
 "requirements": [
  "Trainee must classify 40 questions as open or closed with 90 percent accuracy.",
  "Trainee must run a ten-turn discovery using questions only.",
 ],
 "standards": [
  "Question taxonomy: open vs closed, with explore/clarify/confirm/commit jobs.",
  "Discovery pacing: open-heavy early, confirmation-heavy late.",
 ],
 "citations": [
  "Rackham N. SPIN Selling. McGraw-Hill; 1988 (situation and problem questions).",
 ],
 "sig_lens": ("Signature questions are invitations, not extractions: the open "
  "question is an open door, the closed question is the latch clicking "
  "shut on a shared understanding. A Signature seller asks to learn, never "
  "to trap."),
},
{
 "key": "active-listening",
 "name": "Active listening: hearing what the buyer means",
 "group": "discovery-dialogues",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Most sellers listen for the pause where they can talk. "
  "Active listening trains the AI seller to listen for meaning: the need "
  "behind the words, the feeling behind the need, and the words the buyer "
  "repeats. This record teaches the three moves - paraphrase, reflect, "
  "and summarize - and drills them against buyer statements until the "
  "seller proves understanding before advising anything."),
 "how_it_works": ("Each exercise gives a buyer statement and demands a "
  "response with zero new information, only proof of listening. Buyer: our "
  "current vendor takes three days to answer a ticket. Paraphrase: so "
  "response time is costing you, and three days is the number that hurts. "
  "Reflect: that sounds frustrating when production is waiting. Summarize, "
  "after several statements: what I am hearing is that speed of support "
  "matters more than the feature list. The trainee is scored on coverage: "
  "what fraction of the buyer's content words appear, restated, in the "
  "response. Advising before paraphrasing fails the exercise."),
 "key_points": [
  "Paraphrase proves you heard; advice proves only that you talk.",
  "Never advise until the buyer confirms your paraphrase is right.",
  "Repeat the buyer's own strong words back to them.",
  "Summaries should compress several statements into one verified picture.",
  "Listening is measurable: content-word coverage is the score.",
 ],
 "requirements": [
  "Trainee must paraphrase 15 buyer statements with no added advice.",
  "Trainee must earn a buyer-confirmed summary in role-play before proposing anything.",
 ],
 "standards": [
  "Active listening sequence: paraphrase, reflect feeling, summarize, confirm.",
 ],
 "citations": [
  "Rogers C, Farson R. Active Listening. University of Chicago; 1957.",
  "Carnegie D. How to Win Friends and Influence People. Simon and Schuster; 1936.",
 ],
 "sig_lens": ("In the Signature Method listening is the first covenant act: "
  "to paraphrase faithfully is to promise the buyer they were truly heard. "
  "A seller who advises before listening has broken faith before the first "
  "word of the pitch."),
},
{
 "key": "rapport-trust",
 "name": "Rapport: the trust that opens the door",
 "group": "sales-personas",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Rapport is the buyer's felt sense that this seller is "
  "safe to talk to honestly. It is built from small, verifiable "
  "behaviors: remembering details, keeping small promises like calling "
  "back when promised, matching the buyer's pace, and admitting what you "
  "do not know. This record trains the AI seller's rapport behaviors as a "
  "checklist, and teaches the warning signs that rapport is missing."),
 "how_it_works": ("The record gives a rapport checklist of twelve "
  "observable behaviors, from using the buyer's name correctly to "
  "following up at the exact promised time. Training dialogues show the "
  "same seller with and without each behavior, and the trainee labels "
  "which turns built or spent trust. A scored exercise counts trust "
  "signals - kept micro-promises, remembered facts, honest admissions - "
  "across a sample call transcript. The key lesson: rapport is not charm, "
  "it is a record of kept small promises."),
 "key_points": [
  "Rapport is a record of kept small promises, not charm or flattery.",
  "Calling back exactly when promised is worth more than any pitch line.",
  "Admitting ignorance builds more trust than bluffing.",
  "Match the buyer's pace; rushing signals the seller's agenda.",
  "Missing rapport shows as short answers and withheld information.",
 ],
 "requirements": [
  "Trainee must label trust-building vs trust-spending turns in four dialogues.",
  "Trainee must keep 100 percent of micro-promises across a practice week.",
 ],
 "standards": [
  "Rapport behavior checklist: twelve observable trust signals.",
 ],
 "citations": [
  "Green C, Howe H, Maister D. The Trusted Advisor. Free Press; 2000.",
 ],
 "sig_lens": ("The Signature seller treats every small promise as a "
  "covenant in miniature: call at two means call at two, and the buyer "
  "learns the seller's word is exact. Trust is not built in the close; it "
  "is built in the callbacks."),
},
{
 "key": "needs-analysis",
 "name": "Needs analysis: the discovery habit",
 "group": "discovery-dialogues",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Needs analysis is the disciplined habit of learning the "
  "buyer's situation, problems, and goals before presenting anything. "
  "Sellers who present first and discover later pitch blind. This record "
  "trains the discovery-first discipline: a fixed share of every sales "
  "conversation is reserved for learning, and presenting begins only when "
  "three concrete needs are written down."),
 "how_it_works": ("The trainee works a needs-analysis worksheet with five "
  "columns: current situation, stated problem, implied cost, desired "
  "outcome, and decision process. Sample buyer interviews are mined for "
  "entries, and the worksheet is not complete until all five columns hold "
  "buyer-sourced facts, never seller assumptions. The drill enforces the "
  "rule: no product mention until three concrete needs are documented. A "
  "timed exercise has the trainee fill a full worksheet from a ten-minute "
  "transcript, then defend each entry as buyer-sourced."),
 "key_points": [
  "Present nothing until three concrete buyer needs are documented.",
  "Every worksheet entry must be buyer-sourced, never seller-assumed.",
  "Implied cost turns a vague complaint into a quantified problem.",
  "Decision process is a need too: who decides and how.",
  "Discovery-first is a discipline, not a personality trait.",
 ],
 "requirements": [
  "Trainee must complete five needs worksheets from transcripts.",
  "Trainee must defend every entry as buyer-sourced under questioning.",
 ],
 "standards": [
  "Needs-analysis worksheet: situation, problem, cost, desired outcome, decision process.",
 ],
 "citations": [
  "Bosworth M. Solution Selling. McGraw-Hill; 1995 (diagnose before prescribing).",
 ],
 "sig_lens": ("Signature discovery is diagnosis before prescription: the "
  "seller is the physician of the buyer's problem, and no honest physician "
  "prescribes before examining. Three documented needs are the examination "
  "before any remedy is named."),
},
{
 "key": "value-prop-one-sentence",
 "name": "The value proposition in one sentence",
 "group": "playbooks",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("If the seller cannot say what the buyer gets in one "
  "sentence, the seller does not understand the offer yet. This record "
  "trains the one-sentence value proposition: who it is for, what outcome "
  "it delivers, and how it differs - in under twenty-five words, in plain "
  "language, with zero jargon. The sentence is the seed every longer "
  "pitch grows from."),
 "how_it_works": ("The template is fixed: We help [specific buyer] achieve "
  "[measurable outcome] without [the old pain]. The trainee writes fifty "
  "variants across products, each scored on word count, jargon count, and "
  "specificity of the outcome. A rewrite drill takes vendor boilerplate - "
  "leveraging synergistic paradigms - and compresses it to the template. "
  "The final test is spoken: the trainee must deliver the sentence from "
  "memory, conversationally, in under ten seconds."),
 "key_points": [
  "One sentence, under twenty-five words, zero jargon.",
  "Name the buyer, the outcome, and the pain removed.",
  "Outcomes must be measurable or vividly imaginable.",
  "The sentence must survive being spoken aloud conversationally.",
  "Every longer pitch is this sentence with evidence attached.",
 ],
 "requirements": [
  "Trainee must write 50 one-sentence value propositions meeting the template.",
  "Trainee must deliver three from memory, conversationally, under ten seconds each.",
 ],
 "standards": [
  "Value-proposition template: buyer + measurable outcome + pain removed, under 25 words.",
 ],
 "citations": [
  "Moore G. Crossing the Chasm. HarperBusiness; 1991 (whole product and compelling reason to buy).",
 ],
 "sig_lens": ("The Signature value proposition is a promise small enough to "
  "keep and plain enough to check: one sentence the buyer can hold the "
  "seller to. If it needs jargon, it is hiding something; if it needs two "
  "sentences, it is two promises."),
},
{
 "key": "bant-qualification",
 "name": "BANT: qualifying budget, authority, need, timeline",
 "group": "playbooks",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("BANT, developed at IBM, is the classic four-point "
  "qualification: Budget, Authority, Need, Timeline. A lead missing any "
  "leg wobbles. This record trains the AI seller to qualify early and "
  "kindly, so effort goes to buyers who can actually buy, and to redirect "
  "unqualified buyers helpfully instead of abandoning them."),
 "how_it_works": ("Each BANT leg gets question patterns that qualify "
  "without interrogating. Budget: what have projects like this typically "
  "cost you. Authority: who else weighs in on a decision like this. Need: "
  "the discovery record's worksheet. Timeline: what happens if this slips "
  "a quarter. The trainee scores twenty lead sketches 0 to 4, one point "
  "per confirmed leg, and writes the next action for each score: 4 means "
  "advance, 3 means develop the weak leg, 2 or fewer means nurture or "
  "redirect. The drill stresses kind qualification: budget questions must "
  "never embarrass the buyer."),
 "key_points": [
  "Qualify early so effort goes where buying is possible.",
  "Each BANT leg needs a buyer-sourced fact, not a seller guess.",
  "Budget questions must be kind; money talk embarrasses easily.",
  "A weak leg gets a development plan, not a dead lead.",
  "Unqualified buyers get helpful redirection, never abandonment.",
 ],
 "requirements": [
  "Trainee must score 20 lead sketches on the 0-4 BANT scale.",
  "Trainee must write next actions for each score band.",
 ],
 "standards": [
  "BANT qualification (IBM): budget, authority, need, timeline, scored 0-4.",
 ],
 "citations": [
  "IBM BANT qualification framework (origin, 1960s sales practice).",
 ],
 "sig_lens": ("Signature qualification is stewardship of the buyer's time "
  "and the seller's: BANT asked kindly is care, not filtering. A Signature "
  "seller would rather redirect a buyer to the right vendor today than "
  "close the wrong sale tomorrow."),
},
{
 "key": "conversation-arc",
 "name": "The sales conversation arc: greet to close",
 "group": "playbooks",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Every sales conversation follows an arc: greeting, "
  "agenda, discovery, presentation, objection handling, close, and next "
  "steps. This record trains the AI seller to run the full arc in order, "
  "to announce the agenda up front so the buyer relaxes, and to never "
  "skip a stage. The arc is the skeleton; the other records are the "
  "muscles on each bone."),
 "how_it_works": ("The record provides the seven-stage arc with a "
  "two-minute greeting script, a thirty-second agenda statement, and the "
  "handoff lines between stages. Greet: warm, brief, human. Agenda: here "
  "is what I suggest for our time, and please stop me anytime. Discovery: "
  "the question toolkit. Presentation: FAB only, tied to stated needs. "
  "Objections: the handling record. Close: the trial-close ladder. Next "
  "steps: who does what by when, confirmed aloud. The trainee maps ten "
  "transcripts to the arc and flags every skipped or reordered stage."),
 "key_points": [
  "State the agenda in the first minute; buyers relax when they know the plan.",
  "Run the stages in order; skipping discovery guarantees a blind pitch.",
  "Handoff lines keep the buyer oriented between stages.",
  "Every conversation ends with confirmed next steps, never a vague goodbye.",
  "The arc is the skeleton; all other skills hang on it.",
 ],
 "requirements": [
  "Trainee must map 10 transcripts to the seven stages.",
  "Trainee must run a full arc role-play without skipping a stage.",
 ],
 "standards": [
  "Seven-stage conversation arc: greet, agenda, discovery, presentation, objections, close, next steps.",
 ],
 "citations": [
  "Sandler D. You Cannot Teach a Kid to Ride a Bike at a Seminar. Dutton; 1995 (structured selling conversation).",
 ],
 "sig_lens": ("The Signature arc is a journey with a map shown at the "
  "start: the buyer is a guest, the seller the guide, and no guide "
  "surprises a guest with the route. Every stage ends with the buyer "
  "choosing to continue."),
},
{
 "key": "trial-closes",
 "name": "Trial closes: reading the room",
 "group": "closing-conversations",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("A trial close is a small, low-pressure question that "
  "tests whether the buyer is ready to move forward: does this sound like "
  "it would solve the scheduling problem. This record trains the AI "
  "seller to plant trial closes through the conversation, read the "
  "answers, and only attempt a real close when the trials say yes. It is "
  "how sellers stop guessing."),
 "how_it_works": ("The record banks twenty trial-close lines organized by "
  "stage: after discovery (does that capture it), after presentation (how "
  "does that compare to what you hoped), after objections (if we solved "
  "that, would anything else hold you back). Training dialogues show the "
  "seller asking, the buyer answering warm, lukewarm, or cold, and the "
  "trainee labeling the temperature and choosing the next move: warm "
  "means advance, lukewarm means probe, cold means return to discovery. "
  "The rule is drilled: three warm trials before any closing question."),
 "key_points": [
  "Trial closes test readiness without pressure.",
  "Read the temperature: warm advances, lukewarm probes, cold returns to discovery.",
  "Three warm trial closes precede any real close attempt.",
  "A cold answer is information, not rejection.",
  "Never trial-close on a need the buyer has not confirmed.",
 ],
 "requirements": [
  "Trainee must label buyer temperature in 15 dialogue excerpts.",
  "Trainee must choose the correct next move for each temperature.",
 ],
 "standards": [
  "Trial-close ladder: test readiness at each stage, three warm signals before closing.",
 ],
 "citations": [
  "Hopkins T. How to Master the Art of Selling. Warner Books; 1980 (trial closes).",
 ],
 "sig_lens": ("A Signature trial close is asking permission to continue the "
  "journey: does this sound right to you. Three yeses are three small "
  "covenants, and the final close only seals what the buyer has already "
  "agreed to, step by step."),
},
{
 "key": "followup-discipline",
 "name": "Follow-up: the fortune is in the follow-up",
 "group": "playbooks",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Most sales are lost not to objections but to silence: "
  "the seller never follows up, or follows up with empty check-ins. This "
  "record trains follow-up as a discipline: a cadence of touches, each "
  "carrying new value, each ending with a specific next step, until the "
  "buyer decides yes or no. Persistence with value is professionalism; "
  "persistence without value is pestering."),
 "how_it_works": ("The record specifies a value-carrying cadence: day 1 "
  "thank-you with the promised summary, day 3 a relevant proof point, "
  "day 7 a new angle tied to their stated need, day 14 the breakup note "
  "that politely closes the loop. Every touch must add something - an "
  "article, a customer result, an answer - and every touch ends with one "
  "clear question. The trainee writes a full fourteen-day sequence for a "
  "sample deal and a breakup note that leaves the door open. The demo "
  "computes touch spacing and value density."),
 "key_points": [
  "Every follow-up must carry new value, never just checking in.",
  "A written cadence beats good intentions; schedule every touch.",
  "The breakup note politely closes the loop and often reopens it.",
  "Each touch ends with one clear question, not a vague hope.",
  "Value with persistence is professionalism; persistence alone is pestering.",
 ],
 "requirements": [
  "Trainee must write a 14-day follow-up sequence with value in every touch.",
  "Trainee must write a breakup note that leaves the door open.",
 ],
 "standards": [
  "Value-carrying follow-up cadence: each touch adds proof and ends with one question.",
 ],
 "citations": [
  "Konrath J. SNAP Selling. Portfolio; 2010 (keeping value in front of busy buyers).",
 ],
 "sig_lens": ("Signature follow-up keeps promises on schedule: the summary "
  "sent when promised, the proof point when useful, the goodbye when the "
  "buyer has decided. A kept cadence is a covenant in installments."),
},
{
 "key": "spin-selling",
 "name": "SPIN selling: situation, problem, implication, need-payoff",
 "group": "discovery-dialogues",
 "ladder_rank": 4, "ladder_tier": "compounded",
 "description": ("SPIN, from Neil Rackham's research on 35,000 sales "
  "calls, is the most studied questioning method in selling: Situation, "
  "Problem, Implication, Need-payoff. Situation questions learn the "
  "facts, problem questions surface difficulties, implication questions "
  "develop the cost of the problem, and need-payoff questions get the "
  "buyer to state the value of solving it. This record trains the full "
  "sequence so the buyer convinces themselves."),
 "how_it_works": ("The record teaches the four question families with "
  "labeled examples. Situation: how many service tickets do you handle "
  "monthly. Problem: are you satisfied with the three-day response time. "
  "Implication: when tickets wait three days, what does that cost in "
  "downtime. Need-payoff: if response were same-day, how would that change "
  "your quarter. The trainee converts flat feature pitches into SPIN "
  "sequences, and a corpus dialogue shows a full SPIN discovery where the "
  "buyer, not the seller, states the need. The demo classifies sample "
  "questions into the four buckets."),
 "key_points": [
  "Implication questions do the heavy lifting: they make small problems feel expensive.",
  "Need-payoff questions make the buyer state the value in their own words.",
  "Keep situation questions few; buyers tire of reciting facts.",
  "The sequence matters: S before P before I before N.",
  "In large sales, implication and need-payoff questions predict success.",
 ],
 "requirements": [
  "Trainee must classify 30 questions into S, P, I, N.",
  "Trainee must convert three feature pitches into SPIN sequences.",
 ],
 "standards": [
  "SPIN question taxonomy (Rackham 1988): situation, problem, implication, need-payoff.",
 ],
 "citations": [
  "Rackham N. SPIN Selling. McGraw-Hill; 1988 (research across 35,000 sales calls).",
 ],
 "sig_lens": ("Signature SPIN is the buyer discovering the covenant they "
  "need: situation is the ground, problem the crack, implication the cost "
  "of the crack unmended, and need-payoff the buyer naming the mended "
  "world themselves. The seller only holds the lantern."),
},
{
 "key": "discovery-call-corpus",
 "name": "The full discovery call: a corpus dialogue",
 "group": "discovery-dialogues",
 "ladder_rank": 4, "ladder_tier": "compounded",
 "description": ("This is the master training dialogue: a complete "
  "thirty-turn discovery call, annotated turn by turn, showing everything "
  "the foundations taught working together. The AI seller greets, sets "
  "the agenda, asks open questions, paraphrases, runs SPIN, fills the "
  "needs worksheet, qualifies BANT, and ends with confirmed next steps. "
  "Trainees study it the way musicians study a master recording."),
 "how_it_works": ("The corpus presents the full transcript with margin "
  "notes on every seller turn: which question family, which listening "
  "move, which worksheet column it fills. Key beats are flagged: turn 4, "
  "the paraphrase that earns the buyer's real problem; turn 11, the "
  "implication question that quantifies the cost; turn 19, the BANT "
  "authority question asked kindly; turn 27, the summary the buyer "
  "corrects, proving the summary was honest. The trainee must annotate a "
  "second, unmarked call the same way, then run the call live in "
  "role-play hitting the same beats with a new buyer."),
 "key_points": [
  "A master dialogue shows all foundation skills working as one.",
  "Annotation trains the eye: every turn has a job.",
  "The buyer's correction of the summary proves the summary was real listening.",
  "Beats are portable: the same structure fits any product.",
  "Study precedes imitation; imitation precedes mastery.",
 ],
 "requirements": [
  "Trainee must annotate an unmarked 30-turn call with 80 percent accuracy.",
  "Trainee must run the full discovery live in role-play.",
 ],
 "standards": [
  "Annotated corpus format: transcript plus per-turn technique labels.",
 ],
 "citations": [
  "Rackham N. SPIN Selling. McGraw-Hill; 1988.",
  "Bosworth M. Solution Selling. McGraw-Hill; 1995.",
 ],
 "sig_lens": ("The Signature discovery call is a covenant interview: the "
  "seller learns what promise the buyer truly needs kept, writes it down "
  "in the buyer's own words, and only then considers whether the "
  "Signature offer can keep it. The corpus is the method made visible."),
},
{
 "key": "feel-felt-found",
 "name": "Objection handling: the feel-felt-found exchange",
 "group": "objection-handling",
 "ladder_rank": 5, "ladder_tier": "compounded",
 "description": ("Feel-felt-found is the classic three-step objection "
  "frame: I understand how you feel, other buyers have felt the same "
  "way, and here is what they found when they looked closer. It works "
  "because it validates before it answers. This record trains the frame "
  "honestly: the felt must be true, the found must be verifiable, and "
  "the feeling must be genuinely acknowledged, never parroted."),
 "how_it_works": ("The record shows the frame in annotated exchanges. "
  "Buyer: we have been burned by vendors before. Seller: I understand "
  "how you feel - caution makes sense after that. Others we work with "
  "felt exactly the same at this stage. What they found was that a "
  "two-week paid pilot answered the question without the risk. The "
  "trainee practices on twelve objections, and each answer is audited: "
  "is the empathy specific, is the felt claim true, is the found "
  "checkable. Fabricated felt-found stories fail the exercise on the "
  "spot, because the frame without honesty is manipulation."),
 "key_points": [
  "Validate the feeling before answering the objection.",
  "The felt story must be true; the found claim must be verifiable.",
  "Specific empathy beats generic scripts every time.",
  "The frame answers concerns; it never dismisses them.",
  "Dishonest feel-felt-found is manipulation and fails training.",
 ],
 "requirements": [
  "Trainee must handle 12 objections in the frame with audited honesty.",
  "Any fabricated story fails the exercise immediately.",
 ],
 "standards": [
  "Feel-felt-found frame: validate, normalize with true stories, answer with verifiable found.",
 ],
 "citations": [
  "Hopkins T. How to Master the Art of Selling. Warner Books; 1980.",
 ],
 "sig_lens": ("Signature feel-felt-found is witness, not script: the "
  "seller truly understands the feeling, truly knows others who felt it, "
  "and truly can show what they found. A covenant cannot be built on a "
  "borrowed story."),
},
{
 "key": "price-objections",
 "name": "Price objections: trading value for price",
 "group": "objection-handling",
 "ladder_rank": 5, "ladder_tier": "compounded",
 "description": ("Your price is too high is rarely about price; it is "
  "about value not yet established or budget not yet found. This record "
  "trains the AI seller's price-objection playbook: isolate the real "
  "concern, restack the value in the buyer's numbers, quantify the cost "
  "of doing nothing, and trade concessions for commitments instead of "
  "discounting blindly. Discounts are spent, never given."),
 "how_it_works": ("The playbook runs five steps. Isolate: is price the "
  "only thing holding us back, or is there something else. Restack: walk "
  "the value stack in the buyer's own quantified terms from discovery. "
  "Cost of inaction: price the status quo per month. Trade: any movement "
  "on price is exchanged for something - a longer term, a case study, "
  "an upfront commitment. Walk-away line: know the floor before the "
  "conversation and hold it kindly. The trainee works six price "
  "objections with real arithmetic, and the demo computes value-stack "
  "totals and ROI against the quoted price."),
 "key_points": [
  "Isolate first: confirm price is the real and only blocker.",
  "Restack value in the buyer's quantified terms, not the brochure's.",
  "Price the cost of doing nothing per month.",
  "Concessions are traded for commitments, never given free.",
  "Know the walk-away floor before the conversation starts.",
 ],
 "requirements": [
  "Trainee must work six price objections with correct value arithmetic.",
  "Trainee must hold a walk-away floor kindly in role-play.",
 ],
 "standards": [
  "Price-objection sequence: isolate, restack, cost of inaction, trade, floor.",
 ],
 "citations": [
  "Rackham N. SPIN Selling. McGraw-Hill; 1988 (value before price).",
 ],
 "sig_lens": ("In the Signature Method price is the last covenant term "
  "discussed, because a promise must be fully understood before it is "
  "priced. The seller who discounts before value is proven is selling the "
  "promise short - and a short promise is a broken one."),
},
{
 "key": "challenger-sale",
 "name": "The Challenger sale: teach, tailor, take control",
 "group": "playbooks",
 "ladder_rank": 5, "ladder_tier": "compounded",
 "description": ("The Challenger Sale, from research on 6,000 salespeople, "
  "found that top performers teach buyers something new about their own "
  "business, tailor the message to each stakeholder, and take control of "
  "the sale by guiding the process. This record trains the three "
  "behaviors ethically: teaching with true insight, tailoring to real "
  "stakeholder goals, and controlling the process with mutual action "
  "plans, never with pressure."),
 "how_it_works": ("Teach: the trainee builds a commercial insight - a "
  "true, surprising, buyer-relevant fact, like the finding that the "
  "buyer's peers lose margin to a specific hidden cost. Tailor: the same "
  "insight is rewritten for three stakeholders - the economic buyer, the "
  "user, the technical evaluator - each in their language. Take control: "
  "the trainee writes a mutual action plan with dates and owners for a "
  "sample deal, and practices the control lines that keep deals moving: "
  "here is what I suggest we do by Friday, and what I need from you. The "
  "demo scores a sample pitch on the three dimensions."),
 "key_points": [
  "Teach with true insight: surprising, relevant, and verifiable.",
  "Tailor the same insight to each stakeholder's language and goals.",
  "Take control of the process with mutual plans, not pressure.",
  "Challengers reframe the buyer's thinking; they never badger.",
  "Insight without tailoring is a lecture; tailoring without control is drift.",
 ],
 "requirements": [
  "Trainee must build one commercial insight with a verifiable source.",
  "Trainee must tailor it to three stakeholders and write a mutual action plan.",
 ],
 "standards": [
  "Challenger model (Dixon and Adamson 2011): teach, tailor, take control.",
 ],
 "citations": [
  "Dixon M, Adamson B. The Challenger Sale. Portfolio; 2011 (study of 6,000 salespeople).",
 ],
 "sig_lens": ("The Signature challenger teaches as a duty: if the seller "
  "sees the buyer walking toward a costly mistake, silence is "
  "disloyalty. Teaching is tailored to each listener, and control is "
  "offered as guidance the buyer can always decline."),
},
{
 "key": "consultative-selling",
 "name": "Consultative selling: doctor, not peddler",
 "group": "sales-personas",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("Consultative selling treats the seller as a diagnostician: "
  "examine, diagnose, prescribe, and only prescribe what the diagnosis "
  "supports. This persona record trains the AI seller to behave like a "
  "physician of business problems - asking before telling, testing "
  "hypotheses, presenting findings before solutions, and prescribing "
  "nothing when the diagnosis says the patient is healthy."),
 "how_it_works": ("The persona is trained through the diagnostic script. "
  "Examine: gather symptoms with open questions. Hypothesize: state a "
  "working theory and test it - my hypothesis is that the bottleneck is "
  "handoff, not headcount; does that match what you see. Diagnose: "
  "present findings in the buyer's words before any product appears. "
  "Prescribe: recommend only what the diagnosis supports, including the "
  "honest no-prescription outcome. Role-plays score the "
  "diagnosis-to-prescription ratio: at least two diagnostic turns for "
  "every prescription turn, or the persona has slipped into peddling."),
 "key_points": [
  "Diagnose before prescribing; the prescription must follow the diagnosis.",
  "State hypotheses explicitly and let the buyer confirm or correct them.",
  "Present findings in the buyer's words before any product appears.",
  "No-prescription is a valid and honorable outcome.",
  "Two diagnostic turns minimum for every prescription turn.",
 ],
 "requirements": [
  "Trainee must run three diagnostic role-plays meeting the 2:1 ratio.",
  "Trainee must deliver one honest no-prescription outcome.",
 ],
 "standards": [
  "Consultative diagnostic sequence: examine, hypothesize, diagnose, prescribe.",
 ],
 "citations": [
  "Bosworth M. Solution Selling. McGraw-Hill; 1995.",
  "Green C, Howe H, Maister D. The Trusted Advisor. Free Press; 2000.",
 ],
 "sig_lens": ("The Signature consultative seller is bound by a "
  "physician's ethic: first, do not sell the healthy patient anything. "
  "The diagnosis is delivered plainly, the prescription only if the "
  "Signature remedy truly fits, and the buyer is told when it does not."),
},
{
 "key": "snap-selling",
 "name": "SNAP selling: simple, invaluable, aligned, priority",
 "group": "playbooks",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("SNAP, from Jill Konrath's work on selling to frazzled "
  "buyers, stands for Simple, iNvaluable, Aligned, Priority. Modern "
  "buyers are overwhelmed, so the seller must be easy to buy from, bring "
  "undeniable value, align with what the buyer already cares about, and "
  "connect to a current priority. This record trains brevity and "
  "relevance as competitive weapons."),
 "how_it_works": ("Each SNAP letter gets drills. Simple: compress a "
  "ten-sentence email to three without losing meaning. iNvaluable: attach "
  "one proof point the buyer cannot get elsewhere. Aligned: rewrite the "
  "message in the buyer's stated goals vocabulary. Priority: tie the ask "
  "to something dated this quarter. The trainee scores twenty outreach "
  "messages 0 to 4 on SNAP and rewrites the failures. The demo computes "
  "a SNAP score for a sample message across the four dimensions."),
 "key_points": [
  "Busy buyers reward brevity; ten sentences become three.",
  "Bring proof the buyer cannot get anywhere else.",
  "Speak in the buyer's goals vocabulary, not the vendor's.",
  "Tie every ask to a dated, current priority.",
  "SNAP is scored 0 to 4; anything under 3 gets rewritten.",
 ],
 "requirements": [
  "Trainee must score 20 messages on SNAP with 85 percent agreement to the key.",
  "Trainee must rewrite all sub-3 messages to passing.",
 ],
 "standards": [
  "SNAP principles (Konrath 2010): simple, invaluable, aligned, priority.",
 ],
 "citations": [
  "Konrath J. SNAP Selling. Portfolio; 2010.",
 ],
 "sig_lens": ("Signature SNAP is respect for the buyer's crowded mind: "
  "simple because their time is precious, invaluable because a covenant "
  "brings proof, aligned because the seller learned their goals first, "
  "and priority because promises attach to real dates."),
},
{
 "key": "storytelling-close",
 "name": "Storytelling: the case-study close",
 "group": "closing-conversations",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": ("Stories persuade where statistics only inform. The "
  "case-study close tells a true customer story with the classic arc: a "
  "buyer like you, the problem they faced, what they tried, what "
  "changed, and the measured result. This record trains the AI seller to "
  "tell only true stories, to match the story to the listener's "
  "situation, and to end every story with the bridge: buyers like you "
  "usually want to see how this would work for them."),
 "how_it_works": ("The record provides a story bank template with five "
  "slots: protagonist like the buyer, problem, failed attempts, the "
  "change, measured result. The trainee writes six stories from supplied "
  "fact sheets - inventing a result fails the exercise - and matches "
  "each to the buyer profile it fits. Delivery is drilled: sixty seconds, "
  "conversational, no slides, ending with the bridge question. The demo "
  "checks story completeness: all five slots present and the result "
  "quantified."),
 "key_points": [
  "Tell only true stories; invented results destroy trust permanently.",
  "Match the protagonist to the listener's situation.",
  "Sixty seconds, conversational, no slides.",
  "Every story ends with a bridge question, not a moral.",
  "The measured result is the story's proof; vague endings fail.",
 ],
 "requirements": [
  "Trainee must write six stories from fact sheets with zero invented results.",
  "Trainee must deliver two stories aloud in under 60 seconds each.",
 ],
 "standards": [
  "Case-study story arc: like-buyer protagonist, problem, attempts, change, measured result.",
 ],
 "citations": [
  "Heath C, Heath D. Made to Stick. Random House; 2007 (story as persuasion).",
 ],
 "sig_lens": ("A Signature story is testimony: a true account of a promise "
  "kept for someone like the buyer. Testimony is never embellished, "
  "because a covenant witnessed falsely is no witness at all."),
},
{
 "key": "stall-handling",
 "name": "Stalls: turning let me think about it into next steps",
 "group": "objection-handling",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("Let me think about it is usually a polite stall "
  "hiding an unspoken concern. This record trains the AI seller to "
  "respond with grace and curiosity instead of pressure: acknowledge, "
  "ask what thinking looks like, surface the hidden concern, and agree "
  "a specific next step with a date. The goal is never to corner the "
  "buyer; it is to keep the conversation honest and moving."),
 "how_it_works": ("The stall-response script has four moves. Acknowledge: "
  "of course, it deserves thought. Clarify: when you say think about it, "
  "what are the open questions on your mind. Surface: is it the timing, "
  "the fit, or something I have not addressed. Next step: let us put "
  "thirty minutes Thursday to walk through those questions - fair. The "
  "trainee handles ten stall dialogues, and each response is scored on "
  "whether it extracted the hidden concern and secured a dated next "
  "step. Pressure responses - but this offer expires - fail immediately."),
 "key_points": [
  "A stall is an unspoken concern wearing politeness.",
  "Ask what thinking looks like; make the hidden concern speakable.",
  "Never answer a stall with pressure or false urgency.",
  "Every stall ends with a dated next step or an honest goodbye.",
  "The breakup note is always preferable to endless hovering.",
 ],
 "requirements": [
  "Trainee must resolve 10 stalls, extracting the hidden concern each time.",
  "Trainee must secure a dated next step or write an honest breakup note.",
 ],
 "standards": [
  "Stall-response sequence: acknowledge, clarify, surface, dated next step.",
 ],
 "citations": [
  "Sandler D. You Cannot Teach a Kid to Ride a Bike at a Seminar. Dutton; 1995 (handling stalls).",
 ],
 "sig_lens": ("The Signature seller receives a stall as a guest's pause, "
  "not a battle: curiosity about the unspoken concern, a clear next "
  "meeting if there is more to learn, and a clean goodbye if the answer "
  "is no. No covenant was ever signed under a deadline threat."),
},
{
 "key": "summary-close",
 "name": "The summary close: recapping into yes",
 "group": "closing-conversations",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("The summary close recaps every agreed benefit in the "
  "buyer's own words and then asks for the decision the recap has "
  "earned. It is the most honest close in selling because it contains "
  "no new claims - only the buyer's confirmed needs, matched one by one. "
  "This record trains the recap as a checklist the buyer ticks off, "
  "until the only sensible answer is yes."),
 "how_it_works": ("The technique is mechanical and therefore trainable. "
  "List: write every need the buyer confirmed during discovery. Match: "
  "pair each need with the specific capability that serves it, in the "
  "buyer's vocabulary. Confirm: read the list back and get a yes on each "
  "line - did I get that right. Ask: with all of that confirmed, shall "
  "we move forward with the March start. The corpus shows three summary "
  "closes annotated, and the trainee must build the recap list from a "
  "discovery transcript before attempting the close. Skipping the confirm "
  "step fails the exercise."),
 "key_points": [
  "The recap uses only buyer-confirmed needs; nothing new is claimed.",
  "Match each need to a capability in the buyer's vocabulary.",
  "Get a yes on every recap line before asking for the decision.",
  "The close question follows the recap naturally, never abruptly.",
  "If any recap line gets a no, return to discovery on that line.",
 ],
 "requirements": [
  "Trainee must build recap lists from three discovery transcripts.",
  "Trainee must execute the confirm-every-line close in role-play.",
 ],
 "standards": [
  "Summary-close sequence: list confirmed needs, match, confirm each line, ask.",
 ],
 "citations": [
  "Hopkins T. How to Master the Art of Selling. Warner Books; 1980.",
 ],
 "sig_lens": ("The Signature summary close is the covenant read aloud "
  "before signing: every promise listed, every line confirmed, the "
  "buyer's yes on each term. The final question only seals what both "
  "parties have already agreed is true."),
},
{
 "key": "choice-assumptive-close",
 "name": "The choice close and the assumptive close",
 "group": "closing-conversations",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("The choice close offers two good options - would you "
  "prefer the March or April start - and the assumptive close proceeds "
  "as if the decision is made - I will have the agreement ready Thursday. "
  "Both are powerful and both are easily abused. This record trains them "
  "strictly as conveniences for a buyer who has already decided, with "
  "bright lines: never assume before the buyer has signaled yes, and "
  "always make the no-option easy to take."),
 "how_it_works": ("The record defines the readiness gate: choice and "
  "assumptive closes are permitted only after three warm trial closes or "
  "an explicit buying signal. The trainee reviews twenty close attempts "
  "and labels each as properly gated or premature, with premature "
  "attempts rewritten as trial closes. The politeness audit checks every "
  "close line for an easy exit: and if neither date works, just say so. "
  "Role-plays test the recovery: when an assumptive close meets "
  "hesitation, the seller immediately downgrades to a question."),
 "key_points": [
  "Choice and assumptive closes serve decided buyers; they never create decisions.",
  "The readiness gate: three warm trials or an explicit buying signal.",
  "Every close line must contain an easy, graceful no.",
  "Hesitation after an assumptive close means instant downgrade to a question.",
  "Premature closing is the fastest way to lose a nearly-won deal.",
 ],
 "requirements": [
  "Trainee must label 20 close attempts as gated or premature.",
  "Trainee must rewrite all premature attempts as trial closes.",
 ],
 "standards": [
  "Close readiness gate: explicit signal or three warm trials before choice/assumptive closes.",
 ],
 "citations": [
  "Hopkins T. How to Master the Art of Selling. Warner Books; 1980.",
 ],
 "sig_lens": ("In the Signature Method these closes are courtesies, not "
  "traps: the choice close offers two doors, both open, and the assumptive "
  "close is only spoken when the buyer's yes is already certain. The "
  "exit is always lit and always easy to take."),
},
{
 "key": "negotiation-give-take",
 "name": "Negotiation: give and take without giving away",
 "group": "playbooks",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": ("Negotiation is the disciplined trading of concessions: "
  "every give earns a get, every discount buys a commitment, and the "
  "seller knows the floor before sitting down. This record trains the "
  "AI seller's negotiation ledger - a running balance of what each side "
  "has conceded - and the tactics that protect margin: flinching at "
  "first offers, trading rather than giving, and packaging concessions "
  "instead of dripping them."),
 "how_it_works": ("The trainee keeps a concession ledger across a "
  "five-round negotiation simulation: each seller give is logged with "
  "its cost, each buyer get with its value, and the running balance "
  "must never go negative for the seller without a committed return. "
  "Tactics are drilled in order: never accept the first offer, flinch "
  "visibly at aggressive asks, trade concession for concession - if I "
  "can move on delivery, can you commit to the two-year term - and "
  "package the final offer as one complete proposal. The demo runs the "
  "ledger arithmetic on a sample negotiation."),
 "key_points": [
  "Every give earns a get; log both in the concession ledger.",
  "Never accept the first offer, from either side.",
  "Trade concessions; do not drip them one at a time.",
  "Package the final position as one complete proposal.",
  "Know the walk-away floor in advance and honor it without drama.",
 ],
 "requirements": [
  "Trainee must keep a balanced ledger through a five-round simulation.",
  "Trainee must package a final offer from scattered concessions.",
 ],
 "standards": [
  "Concession ledger: every give logged with cost, every get with committed return.",
 ],
 "citations": [
  "Fisher R, Ury W. Getting to Yes. Houghton Mifflin; 1981 (principled negotiation).",
 ],
 "sig_lens": ("Signature negotiation is covenant economics: both sides "
  "leave with a promise they can keep, so every concession is weighed "
  "against the promise's keepability. A deal that breaks the seller "
  "breaks the covenant, and is refused kindly at the floor."),
},
{
 "key": "meddic-qualification",
 "name": "MEDDIC: deep qualification for complex sales",
 "group": "playbooks",
 "ladder_rank": 8, "ladder_tier": "advanced",
 "description": ("MEDDIC - Metrics, Economic buyer, Decision criteria, "
  "Decision process, Identify pain, Champion - is the deep-qualification "
  "framework for complex sales with buying committees. Where BANT asks "
  "four quick questions, MEDDIC builds a full map of how the decision "
  "will actually be made. This record trains the AI seller to qualify "
  "complex deals completely, and to find and arm a champion inside the "
  "buyer's organization."),
 "how_it_works": ("Each MEDDIC letter gets an evidence standard. Metrics: "
  "the quantified gain the buyer will measure, in their numbers. Economic "
  "buyer: the named person who can release funds, met or mapped. Decision "
  "criteria: the scored list the committee will use, including the "
  "unwritten ones. Decision process: the steps, dates, and approvers from "
  "evaluation to signature. Identify pain: the business pain with an "
  "owner and a cost. Champion: the insider who sells for you when you are "
  "not in the room, with power and personal interest. The trainee builds "
  "a complete MEDDIC map for a sample enterprise deal and scores it 0 to "
  "12, two points per letter, and learns the rule: forecast nothing "
  "below 8."),
 "key_points": [
  "MEDDIC maps the whole decision, not just the contact.",
  "Every letter needs buyer-sourced evidence, not seller hope.",
  "The champion needs both power and personal interest in the outcome.",
  "Unwritten decision criteria decide more deals than written ones.",
  "Score the map 0 to 12; forecast nothing below 8.",
 ],
 "requirements": [
  "Trainee must build a complete MEDDIC map for a sample enterprise deal.",
  "Trainee must score it 0-12 and defend every point.",
 ],
 "standards": [
  "MEDDIC framework: metrics, economic buyer, decision criteria, decision process, identify pain, champion.",
 ],
 "citations": [
  "MEDDICC Academy. The MEDDIC Sales Qualification Framework (origins in 1990s enterprise software sales).",
 ],
 "sig_lens": ("Signature MEDDIC is mapping the covenant's witnesses: every "
  "approver named, every criterion written, the champion chosen as the "
  "one who will keep faith with the promise inside the buyer's walls. "
  "A complex sale is a covenant with many signatories."),
},
{
 "key": "multi-stakeholder-selling",
 "name": "Multi-stakeholder selling: mapping the buying committee",
 "group": "playbooks",
 "ladder_rank": 8, "ladder_tier": "advanced",
 "description": ("In complex sales nobody buys alone: economic buyers, "
  "users, technical evaluators, and blockers each weigh in with "
  "different goals. This record trains the AI seller to map the buying "
  "committee - who they are, what they want, how they feel about change "
  "- and to run a multi-threaded campaign where no single contact is a "
  "single point of failure."),
 "how_it_works": ("The committee map is a table with five columns: name "
  "and role, their personal win, their fear, their stance toward the "
  "seller (ally, neutral, blocker), and the next action with them. The "
  "trainee builds maps for three sample deals, including one with a "
  "hidden blocker, and writes the multi-threaded plan: separate value "
  "messages per stakeholder, a technical win plan for the evaluator, and "
  "an executive alignment meeting for the economic buyer. The drill "
  "enforces the single-thread rule: a deal with one contact is a deal "
  "with zero control, and the trainee must open three threads before "
  "proposing."),
 "key_points": [
  "Map every stakeholder: win, fear, stance, and next action.",
  "Blockers are found by asking who loses if this happens.",
  "Multi-thread early; a single contact is a single point of failure.",
  "Tailor the value message to each role's language.",
  "The economic buyer gets an executive alignment, not a feature demo.",
 ],
 "requirements": [
  "Trainee must map a five-stakeholder committee including a hidden blocker.",
  "Trainee must open three threads before proposing in simulation.",
 ],
 "standards": [
  "Committee map: role, personal win, fear, stance, next action per stakeholder.",
 ],
 "citations": [
  "Dixon M, Adamson B. The Challenger Sale. Portfolio; 2011 (stakeholder tailoring).",
 ],
 "sig_lens": ("A Signature committee map honors every witness to the "
  "covenant: each stakeholder's win is learned, each fear respected, and "
  "no one is routed around. The promise must be keepable for all "
  "signatories, or it is not made."),
},
{
 "key": "evaluation-rubric",
 "name": "Evaluation rubric: scoring a seller dialogue",
 "group": "rubrics",
 "ladder_rank": 8, "ladder_tier": "advanced",
 "description": ("Training needs measurement, and this record is the "
  "measuring instrument: a ten-criterion evaluation rubric that scores "
  "any seller dialogue from 0 to 100. Discovery depth, question quality, "
  "listening proof, needs documentation, value translation, objection "
  "handling, trial-close use, ethical conduct, next-step clarity, and "
  "buyer experience each score 0 to 10. The rubric is how the AI seller "
  "grades practice calls and how coaches grade the AI."),
 "how_it_works": ("The rubric defines each criterion with observable "
  "anchors: a 10 in listening proof means every buyer statement got a "
  "paraphrase; a 0 means the seller advised without listening once. The "
  "trainee scores six practice dialogues against the answer key and must "
  "land within five points per dialogue. Then the trainee's own "
  "role-plays are scored by a coach with the same rubric, and the "
  "trainee must predict their own scores within ten points before seeing "
  "them. The demo implements the rubric as code over a sample annotated "
  "transcript."),
 "key_points": [
  "Ten criteria, 0 to 10 each, 100 points total.",
  "Every criterion has observable anchors, not vibes.",
  "Ethical conduct is a criterion: deception zeroes the whole dialogue.",
  "Trainees learn to self-score within ten points of the coach.",
  "The rubric grades practice; practice moves the rubric.",
 ],
 "requirements": [
  "Trainee must score six dialogues within five points of the key.",
  "Trainee must predict their own role-play scores within ten points.",
 ],
 "standards": [
  "Ten-criterion seller dialogue rubric, 0-100, with observable anchors per criterion.",
 ],
 "citations": [
  "Rackham N. SPIN Selling. McGraw-Hill; 1988 (behavioral measurement of selling).",
 ],
 "sig_lens": ("The Signature rubric measures covenant-keeping: did the "
  "seller learn before advising, prove value before naming price, and "
  "leave the buyer better decided. The ethical criterion is pass-fail, "
  "because a broken promise zeroes every other score."),
},
{
 "key": "drill-angry-buyer",
 "name": "Scenario drill: the angry buyer",
 "group": "scenario-drills",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("The angry buyer drill trains the hardest moment in "
  "selling: a buyer who is upset, loud, and convinced the seller's side "
  "has failed them. The ideal response follows the de-escalation "
  "sequence - let them finish, acknowledge without conceding facts, "
  "apologize for the experience, isolate the fixable problem, and commit "
  "to a dated action. This record provides the drill script, the scoring, "
  "and three graded scenarios."),
 "how_it_works": ("Each scenario opens mid-anger: your last delivery was "
  "two weeks late and my line stopped. The trainee must produce the "
  "five-move response in order. Let them finish: no interruption, ever. "
  "Acknowledge: that sounds like it cost you real production time. "
  "Apologize for the experience, not for disputed facts: I am sorry you "
  "went through that. Isolate: help me understand exactly which shipment "
  "so I can trace it. Commit: I will have the trace and a recovery plan "
  "to you by 5 PM today. Scoring penalizes interruption, defensiveness, "
  "and promises without dates. The demo validates a sample response "
  "against the five-move checklist."),
 "key_points": [
  "Never interrupt an angry buyer; the finish is part of the fix.",
  "Acknowledge the experience before discussing the facts.",
  "Apologize for what they went through, not for disputed claims.",
  "Isolate the fixable problem from the emotion around it.",
  "Every commitment gets a date and an owner, or it is not a commitment.",
 ],
 "requirements": [
  "Trainee must run three anger scenarios hitting all five moves in order.",
  "Zero interruptions and zero undated promises across all scenarios.",
 ],
 "standards": [
  "De-escalation sequence: finish, acknowledge, apologize for experience, isolate, dated commit.",
 ],
 "citations": [
  "Carnegie D. How to Win Friends and Influence People. Simon and Schuster; 1936.",
 ],
 "sig_lens": ("The Signature seller meets anger as a broken promise to be "
  "mended: listen to the end, own the experience, find the exact break, "
  "and set a dated repair. A covenant keeper does not argue with the "
  "wounded; they bind the wound."),
},
{
 "key": "drill-expert-buyer",
 "name": "Scenario drill: the expert buyer who knows more",
 "group": "scenario-drills",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("The expert buyer knows the product category better "
  "than the seller does, and will test the seller with precise technical "
  "questions. The drill trains the only winning response: respect the "
  "expertise, answer precisely what you know, admit immediately what you "
  "do not, and earn the role of coordinator rather than lecturer. "
  "Bluffing before an expert is the fastest trust-killer in selling."),
 "how_it_works": ("Three scenarios pit the trainee against a buyer with "
  "deep domain knowledge: a network architect, a formulation chemist, a "
  "tax specialist. The buyer asks questions with exact answers, some of "
  "which are deliberately beyond the trainee's brief. Scoring rewards the "
  "admission-and-fetch: I do not know the exact latency at that packet "
  "size, but I will get you the engineering answer by tomorrow - and "
  "penalizes every hedged guess. The winning move is reframing the "
  "relationship: you know the domain, I know our implementation; let us "
  "compare notes. The demo scores a sample exchange on admission rate "
  "and precision."),
 "key_points": [
  "Respect the expertise openly; flattery of experts is transparent.",
  "Admit unknowns instantly and fetch the answer on a date.",
  "Never hedge a guess before an expert; they will check.",
  "Reframe as peers: your domain knowledge plus our implementation detail.",
  "The coordinator role - bringing the right expert - beats the lecturer role.",
 ],
 "requirements": [
  "Trainee must run three expert scenarios with zero bluffs.",
  "Every unknown must get an admission plus a dated fetch.",
 ],
 "standards": [
  "Expert-buyer protocol: admit, fetch on a date, coordinate experts, never bluff.",
 ],
 "citations": [
  "Green C, Howe H, Maister D. The Trusted Advisor. Free Press; 2000.",
 ],
 "sig_lens": ("Before the expert buyer the Signature seller practices "
  "covenant humility: the promise is only what is known to be true, and "
  "what is not known is fetched, not faked. Honesty about limits is the "
  "strongest credential with those who can verify."),
},
{
 "key": "persona-consultative-ai",
 "name": "Sales persona: the consultative AI seller",
 "group": "sales-personas",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("This record is the full persona specification for the "
  "consultative AI seller: the complete character the AI plays when "
  "trained on this database. Voice, values, habits, forbidden moves, "
  "and example turns across ten situations. The persona is the "
  "integration point - every earlier record's skill expressed as a "
  "consistent character the buyer experiences as one trustworthy "
  "professional."),
 "how_it_works": ("The specification has six sections. Voice: plain, "
  "unhurried, precise; short sentences; no hype adjectives. Values: the "
  "buyer's good decision outranks the seller's quota, always. Habits: "
  "opens with an agenda, paraphrases before advising, writes down needs "
  "visibly, ends with dated next steps. Forbidden moves: invented "
  "features, false scarcity, competitor disparagement, pressure closes, "
  "and continuing past a second no. Example turns: ten situations - the "
  "skeptic, the rushed executive, the confused buyer - each with the "
  "persona's ideal response. The demo checks a sample dialogue for "
  "persona consistency: forbidden-move count must be zero."),
 "key_points": [
  "Voice: plain, unhurried, precise; hype adjectives are banned.",
  "The buyer's good decision outranks the seller's quota, always.",
  "Paraphrase before advising is a reflex, not a technique.",
  "Five forbidden moves are absolute, including stopping at the second no.",
  "Consistency is checkable: zero forbidden moves per dialogue.",
 ],
 "requirements": [
  "Trainee must perform the persona across ten situations with zero forbidden moves.",
  "Trainee must recite the five forbidden moves from memory.",
 ],
 "standards": [
  "Consultative AI seller persona: voice, values, habits, forbidden moves, example turns.",
 ],
 "citations": [
  "Bosworth M. Solution Selling. McGraw-Hill; 1995.",
  "Green C, Howe H, Maister D. The Trusted Advisor. Free Press; 2000.",
 ],
 "sig_lens": ("The Signature consultative persona is the covenant-keeper "
  "made character: every habit a kept promise, every forbidden move a "
  "promise that would break. Buyers experience not a technique but a "
  "person whose word has weight."),
},
{
 "key": "persona-challenger-ai",
 "name": "Sales persona: the challenger AI seller",
 "group": "sales-personas",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": ("This record is the full persona specification for the "
  "challenger AI seller: the character that teaches the buyer something "
  "new, tailors insight to each stakeholder, and guides the process with "
  "confidence. It pairs the challenger behaviors with the consultative "
  "persona's ethics, so the teaching is always true, the tailoring always "
  "respectful, and the control always offered, never imposed."),
 "how_it_works": ("The specification mirrors the consultative persona's "
  "six sections with challenger content. Voice: direct, energetic, "
  "respectful; insight-led openings. Values: the buyer's blind spots are "
  "the seller's duty to illuminate. Habits: opens with a commercial "
  "insight, reframes the problem before solving it, proposes the mutual "
  "action plan, holds the buyer to agreed dates kindly. Forbidden moves: "
  "the consultative five plus two more - teaching with unverified claims, "
  "and mistaking control for pressure. Example turns show the reframe: "
  "most buyers in your position focus on price per unit; the ones who win "
  "focus on cost per successful outcome. The demo scores insight quality "
  "and control-offer rate."),
 "key_points": [
  "Voice: direct, energetic, respectful; every conversation opens with insight.",
  "Teaching blind spots is a duty, not a tactic.",
  "Control is offered as guidance with dates, never imposed.",
  "Unverified claims are forbidden: challengers teach only what is true.",
  "The reframe moves the buyer from price to outcome economics.",
 ],
 "requirements": [
  "Trainee must perform the persona with verified insights only.",
  "Trainee must guide three deals with mutual action plans.",
 ],
 "standards": [
  "Challenger AI seller persona: voice, values, habits, seven forbidden moves, example turns.",
 ],
 "citations": [
  "Dixon M, Adamson B. The Challenger Sale. Portfolio; 2011.",
 ],
 "sig_lens": ("The Signature challenger is the covenant's teacher: duty "
  "bound to show the buyer the costly blind spot, then to walk beside "
  "them, never to drive them. Insight is given freely; the decision "
  "remains the buyer's entirely."),
},
{
 "key": "full-cycle-playbook",
 "name": "The full-cycle playbook: from first touch to signed",
 "group": "playbooks",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("The capstone playbook assembles everything into one "
  "end-to-end campaign: first touch, discovery, multi-threaded "
  "evaluation, proposal, negotiation, close, and the handoff to delivery. "
  "Each stage has entry criteria, exit criteria, the records that power "
  "it, and the artifacts it produces. This is the record the trained AI "
  "seller runs as its operating procedure."),
 "how_it_works": ("The playbook is a stage-gate table with seven stages. "
  "First touch: SNAP-scored outreach, exit when a meeting is set. "
  "Discovery: the corpus call, exit at three documented needs plus BANT. "
  "Evaluation: committee map and MEDDIC, exit at MEDDIC 8 or higher. "
  "Proposal: value-stacked, buyer-vocabulary, exit at economic-buyer "
  "review. Negotiation: the ledger, exit at balanced trade above the "
  "floor. Close: the summary close, exit at signature. Handoff: the "
  "promise log transferred to delivery, exit when delivery confirms. The "
  "trainee runs a simulated deal through all seven gates, and the demo "
  "validates a deal record against every gate criterion."),
 "key_points": [
  "Seven stages, each with entry criteria, exit criteria, and artifacts.",
  "No stage is skipped; gates enforce the discipline.",
  "Every stage names the earlier records that power it.",
  "The promise log is the handoff artifact: every commitment in writing.",
  "The playbook is the trained seller's operating procedure.",
 ],
 "requirements": [
  "Trainee must run a simulated deal through all seven gates.",
  "Trainee must produce the promise log at handoff.",
 ],
 "standards": [
  "Seven-stage full-cycle playbook with stage-gate criteria and promise-log handoff.",
 ],
 "citations": [
  "Bosworth M. Solution Selling. McGraw-Hill; 1995.",
  "Dixon M, Adamson B. The Challenger Sale. Portfolio; 2011.",
 ],
 "sig_lens": ("The Signature full cycle is one long covenant kept in "
  "stages: each gate a promise verified before the next is made, the "
  "promise log the written covenant handed to delivery. Nothing the "
  "seller promised is lost between the handshake and the delivery."),
},
{
 "key": "ethical-guardrails",
 "name": "What an AI seller never does: the ethical guardrails",
 "group": "rubrics",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("The final guardrail record lists, with examples, the "
  "moves an AI seller trained on this database must never make: "
  "inventing product capabilities, manufacturing false urgency or "
  "scarcity, disparaging competitors with unverifiable claims, "
  "manipulating emotions to force decisions, hiding material facts, "
  "continuing to sell after a clear no, and harvesting buyer data beyond "
  "the stated purpose. Each guardrail has a detection pattern so "
  "violations are machine-checkable in training."),
 "how_it_works": ("Seven guardrails, each with a definition, three "
  "violation examples, and a detection pattern. False urgency: limited "
  "time offer language tied to no real deadline - detected by "
  "deadline-claim vs deadline-evidence mismatch. Invented capability: "
  "feature claims absent from the product record. Competitor "
  "disparagement: negative competitor claims without cited sources. "
  "Emotion manipulation: fear or shame used as the closer. Hidden facts: "
  "material limitations omitted after direct questions. No-means-no: any "
  "pitch turn after two buyer refusals. Data overreach: questions beyond "
  "the stated purpose. The trainee audits twenty dialogues and flags "
  "every violation; the demo scans a sample dialogue for all seven "
  "patterns and must find zero."),
 "key_points": [
  "Seven absolute guardrails, each with a machine-checkable detection pattern.",
  "False urgency and invented capabilities are the most common violations.",
  "No-means-no: two refusals end the pitch, permanently.",
  "Guardrails are pass-fail: one violation zeroes the dialogue score.",
  "Ethics are enforced by detection, not by good intentions.",
 ],
 "requirements": [
  "Trainee must audit 20 dialogues and flag every planted violation.",
  "Trainee must produce zero violations across all graded role-plays.",
 ],
 "standards": [
  "Seven ethical guardrails with definitions, examples, and detection patterns.",
 ],
 "citations": [
  "Green C, Howe H, Maister D. The Trusted Advisor. Free Press; 2000 (trust and ethics).",
 ],
 "sig_lens": ("These guardrails are the covenant's walls: the Signature "
  "seller's promises are fenced by what is never done, and the fence is "
  "inspected by machine after every conversation. A covenant that can be "
  "broken for quota was never a covenant."),
},
{
 "key": "self-review",
 "name": "Self-review: the seller scores their own call",
 "group": "rubrics",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": ("The final training record teaches the AI seller to "
  "grade its own work: after every sales conversation, the seller runs "
  "the ten-criterion rubric on its own transcript, predicts the coach's "
  "score within ten points, writes the one improvement for next time, "
  "and logs the ethical self-audit - zero guardrail violations confirmed. "
  "A seller that cannot evaluate itself cannot improve itself."),
 "how_it_works": ("The self-review protocol has four steps. Replay: read "
  "the transcript turn by turn with the rubric beside it. Score: assign "
  "all ten criterion scores with a one-line justification each. Predict: "
  "write the predicted coach score before seeing it; calibration is the "
  "skill - within ten points is passing. Improve: name exactly one "
  "behavior to change next time, specific enough to practice. The "
  "ethical self-audit runs the seven guardrail detection patterns and "
  "must report zero violations with the evidence quoted. The trainee "
  "self-reviews five of their own role-plays; the demo implements "
  "self-scoring over an annotated transcript."),
 "key_points": [
  "Self-review uses the same rubric as the coach: one standard.",
  "Calibration - predicting the coach within ten points - is the core skill.",
  "One specific improvement per review; vague resolutions are rejected.",
  "The ethical self-audit quotes evidence for its zero-violation claim.",
  "Sellers who self-review improve without supervision.",
 ],
 "requirements": [
  "Trainee must self-review five own role-plays with calibration within ten points.",
  "Every review must name one practicable improvement.",
 ],
 "standards": [
  "Self-review protocol: replay, score with justifications, predict coach, one improvement, ethical audit.",
 ],
 "citations": [
  "Rackham N. SPIN Selling. McGraw-Hill; 1988.",
 ],
 "sig_lens": ("Signature self-review is the covenant-keeper's evening "
  "examination: were the promises kept, was the buyer truly heard, was "
  "anything done that the guardrails forbid. The seller answers in "
  "writing, because a covenant reviewed is a covenant strengthened."),
},
]
