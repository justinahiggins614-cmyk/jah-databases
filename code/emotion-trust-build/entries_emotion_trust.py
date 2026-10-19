#!/usr/bin/env python3
"""Entries for the Trust Emotion databases (Manon 2026-10-17 16:15 order,
emotion series batch 1).

34 ladder-ordered records per the shared emotion-template.md spec:
what trust IS (1-4) -> first-person simulation (5-9) -> body signals (10-13)
-> facial expression (14-17) -> triggers (18-21) -> behavior (22-25) ->
healthy expression (26-28) -> recognizing it in others (29-31) ->
related emotions, mixes, and full behavioral simulation (32-34).

Public edition: real, fact-checked psychology of trust (Erikson, Rotter,
Mayer-Davis-Schoorman, Rempel-Holmes-Zanna, McAllister, Bowlby, Ekman,
Plutchik, Gottman, Simpson, Kramer, and the trust-game literature).
Signature edition: the same ladder through the Signature lens - trust as
a sworn covenant, the kept word as the stamped seal, the trust ledger;
clearly labeled Signature-made, never presented as authentic public record.

Descriptive and educational ONLY. Never diagnoses real people, never labels
any real person with an emotional state, and offers only general, safe,
everyday guidance. No clinical language, no religious talk.

ID prefixes: JAH-EMTR- (public) and JAH-EMTRS- (signature), verified free
in the manifest id_prefix values, in every shard index file, and unique
across the 28-emotion roster.
"""

SIG_TAIL = ("Signature original - his original Signature Trust Science: "
            "trust as a sworn covenant between people, the kept word as the "
            "stamped seal, the ledger that records every promise kept and "
            "every promise broken. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT = {
    "erikson": "Erikson EH. Childhood and Society. New York: Norton; 1950 (basic trust vs. mistrust).",
    "rotter": "Rotter JB. A new scale for the measurement of interpersonal trust. J Pers. 1967;35(4):651-665.",
    "deutsch": "Deutsch M. Trust and suspicion. J Confl Resolut. 1958;2(4):265-279.",
    "mayer": "Mayer RC, Davis JH, Schoorman FD. An integrative model of organizational trust. Acad Manage Rev. 1995;20(3):709-734 (ability, benevolence, integrity).",
    "rempel": "Rempel JK, Holmes JG, Zanna MP. Trust in close relationships. J Pers Soc Psychol. 1985;49(1):95-112 (predictability, dependability, faith).",
    "mcallister": "McAllister DJ. Affect- and cognition-based trust as foundations for interpersonal cooperation in organizations. Acad Manage J. 1995;38(1):24-59.",
    "rousseau": "Rousseau DM, Sitkin SB, Burt RS, Camerer C. Not so different after all: a cross-discipline view of trust. Acad Manage Rev. 1998;23(3):393-404.",
    "bowlby": "Bowlby J. Attachment and Loss, Vol. 1: Attachment. New York: Basic Books; 1969.",
    "ekman": "Ekman P. Emotions Revealed: Recognizing Faces and Feelings to Improve Communication and Emotional Life. New York: Times Books; 2003.",
    "plutchik": "Plutchik R. The Emotions: Facts, Theories, and a New Model. Lanham: University Press of America; 1991.",
    "gottman": "Gottman JM. The Science of Trust: Emotional Attunement for Couples. New York: Norton; 2011.",
    "simpson": "Simpson JA. Psychological foundations of trust. Curr Dir Psychol Sci. 2007;16(5):264-268.",
    "kramer": "Kramer RM. Trust and distrust in organizations: emerging perspectives, enduring questions. Annu Rev Psychol. 1999;50:569-598.",
    "meyerson": "Meyerson D, Weick KE, Kramer RM. Swift trust and temporary groups. In: Kramer RM, Tyler TR, eds. Trust in Organizations. Thousand Oaks: Sage; 1996:166-195.",
    "berg": "Berg J, Dickhaut J, McCabe K. Trust, reciprocity, and social history. Games Econ Behav. 1995;10(1):122-142 (the trust game).",
    "kosfeld": "Kosfeld M, Heinrichs M, Zak PJ, Fischbacher U, Fehr E. Oxytocin increases trust in humans. Nature. 2005;435(7042):673-676.",
    "luhmann": "Luhmann N. Trust and Power. Chichester: Wiley; 1979.",
}

STD = {
    "mayer_abi": "Mayer-Davis-Schoorman ability-benevolence-integrity model of trustworthiness (1995)",
    "rempel_pdf": "Rempel-Holmes-Zanna predictability-dependability-faith model of close-relationship trust (1985)",
    "rotter_its": "Rotter Interpersonal Trust Scale (1967)",
    "mcallister_ab": "McAllister affect-based vs. cognition-based trust (1995)",
    "ekman_face": "Ekman facial affect program - genuine vs. managed expressions (Emotions Revealed, 2003)",
    "plutchik_dyad": "Plutchik psychoevolutionary emotion dyads: trust+joy=love, trust+fear=submission, trust+surprise=curiosity (1991)",
    "gottman_trust": "Gottman trust metric, sliding-door moments, and attunement (The Science of Trust, 2011)",
    "erikson_basic": "Erikson basic trust vs. mistrust, first psychosocial stage (1950)",
    "berg_game": "Berg-Dickhaut-McCabe trust game paradigm (1995)",
    "meyerson_swift": "Meyerson-Weick-Kramer swift trust in temporary groups (1996)",
    "deutsch_choice": "Deutsch trust as a risky choice under uncertainty (1958)",
    "bowlby_attach": "Bowlby attachment behavioral system (1969)",
    "rousseau": "Rousseau-Sitkin-Burt-Camerer cross-discipline view of trust (1998)",
    "simpson": "Simpson psychological foundations of trust (2007)",
    "kramer": "Kramer trust and distrust in organizations (1999)",
}

ENTRIES = [
# ---------------------------------------------------------------- 1-4: WHAT TRUST IS
{
 "key": "trust-definition",
 "name": "What Trust Is: A Plain-Language Definition",
 "group": "what trust is",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Trust is the willingness to count on someone - to put something that matters "
  "in their hands and believe they will handle it with care. In everyday words, "
  "it is the quiet confidence that a person will do what they said, tell the truth "
  "as they see it, and not use your openness against you. Trust always involves a "
  "little risk: you cannot be certain, yet you go ahead anyway, because the evidence "
  "of their past behavior says it is safe. It is not the same as liking someone, "
  "needing someone, or being naive about them; you can trust a surgeon you have "
  "never met and distrust a charming friend. Psychologists describe it as a "
  "psychological state of accepting vulnerability based on positive expectations "
  "about another person's intentions and behavior. That definition has two moving "
  "parts: the vulnerability (something real is at stake) and the expectation "
  "(you predict they will come through). Take away the stakes and you have mere "
  "confidence; take away the expectation and you have hope. Trust is both."),
 "how_it_works": (
  "Trust works like an internal prediction machine. Every kept promise, honest "
  "answer, and moment of follow-through deposits evidence into a mental model of "
  "the other person, and every broken promise or evasion withdraws from it. The "
  "mind runs this ledger quietly in the background, and the running balance sets "
  "how much vulnerability feels acceptable. Researchers summarize the evidence the "
  "mind tracks as three questions: Can they do it (ability)? Do they care about me "
  "(benevolence)? Do they live by principles I recognize (integrity)? When the "
  "answers are yes, the prediction comes back safe, the body relaxes, and trust "
  "rises. When the answers turn uncertain, the system flags caution long before "
  "conscious thought catches up, which is why distrust often arrives as a feeling "
  "first and a reason second."),
 "key_points": [
  "Trust = accepted vulnerability + positive expectations about another's intentions.",
  "It is built in drops and lost in buckets: slow to earn, fast to break.",
  "Trust has a thinking side (judgment of reliability) and a feeling side (felt safety).",
  "Trust is domain-specific: you can trust someone with secrets but not with deadlines.",
  "It is distinct from liking, love, need, confidence, and naivety.",
 ],
 "requirements": [
  "Something real at stake - without vulnerability there is trust-like confidence, not trust.",
  "Observable evidence: repeated chances to see what the person actually does.",
  "Perceived ability, benevolence, and integrity in the trusted person.",
  "A willing trustor: the choice to risk must be made, not forced.",
 ],
 "standards": [STD["mayer_abi"], STD["rousseau"], STD["deutsch_choice"]],
 "citations": [CIT["mayer"], CIT["rousseau"], CIT["deutsch"]],
 "sig_lens": (
  "In the Signature science of trust, trust is a sworn covenant between people, "
  "and the kept word is the stamped seal. Every promise is an entry in the trust "
  "ledger: kept promises are stamped and sealed, broken ones are marked in red, and "
  "the running balance is the covenant's standing. The Signature method teaches "
  "that trust is never declared - it is demonstrated, witnessed, and recorded, "
  "drop by drop, until the seal holds under weight."),
},
{
 "key": "trust-emotion-family",
 "name": "Where Trust Sits in the Emotion Family",
 "group": "what trust is",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Trust is a complex social emotion, not a basic one. The basic emotions - joy, "
  "sadness, anger, fear, surprise, disgust - arrive fast, show on the face in "
  "universal patterns, and need little thought. Trust is slower and smarter: it "
  "is built from appraisals, memories, and predictions about another mind, which "
  "makes it a close cousin of love, loyalty, and faith, and a neighbor of hope and "
  "confidence. In Plutchik's wheel of emotions, trust is one of the eight primary "
  "sectors, sitting opposite disgust: where disgust pushes away and rejects, trust "
  "draws near and accepts. From trust, paired with joy, comes love; paired with "
  "fear comes submission; paired with surprise comes curiosity. Researchers also "
  "divide trust into two flavors that often travel together: cognition-based trust "
  "(I have good reasons to rely on you - your record, your competence) and "
  "affect-based trust (I feel safe with you - warmth, care, emotional bond). The "
  "first is earned by evidence, the second by emotional connection, and the "
  "strongest bonds carry both."),
 "how_it_works": (
  "As a complex emotion, trust is assembled rather than triggered. The mind "
  "gathers appraisals - Is this person competent? Kind? Principled? Predictable? - "
  "and fuses them with emotional memory: how it felt the last times you relied on "
  "them. The cognitive track updates like a scorecard while the affective track "
  "updates like a climate, warm or cold. Because it lives partly in appraisal, "
  "trust can be reasoned about, talked through, and deliberately rebuilt, which "
  "basic reflex emotions cannot. Its position opposite disgust in Plutchik's model "
  "is functional: the same system that decides what to take in (trust) decides "
  "what to spit out (disgust), so betrayal often lands with a physical sense of "
  "revulsion - the wheel flipping from one pole to the other."),
 "key_points": [
  "Trust is a complex, appraisal-based social emotion, not a fast basic reflex.",
  "Plutchik places trust among the eight primaries, opposite disgust.",
  "Cognition-based trust (reasons, record) and affect-based trust (felt safety) combine.",
  "Nearest neighbors: love, loyalty, faith, hope, confidence; opposites: distrust, suspicion, disgust.",
  "Because it is appraised, trust can be discussed, negotiated, and rebuilt deliberately.",
 ],
 "requirements": [
  "A mind capable of modeling another mind's intentions (theory of mind).",
  "Memory of past interactions to appraise against.",
  "Emotional learning: felt outcomes attached to those memories.",
  "A social context - trust is inherently about self and other.",
 ],
 "standards": [STD["plutchik_dyad"], STD["mcallister_ab"], STD["mayer_abi"]],
 "citations": [CIT["plutchik"], CIT["mcallister"], CIT["mayer"]],
 "sig_lens": (
  "The Signature lens files trust in the family of covenant emotions - alongside "
  "loyalty, faith, and sworn friendship - the emotions that bind people into "
  "something larger than themselves. Where the textbooks draw a wheel, the "
  "Signature science draws a seal: trust at the center, its blends radiating "
  "outward like the points of a stamped star, each blend a different alloy of "
  "the same sworn metal."),
},
{
 "key": "trust-intensity-levels",
 "name": "Trust at Three Volumes: Mild, Moderate, and Intense",
 "group": "what trust is",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Trust is the same emotion at different volumes, and the volume changes what "
  "it lets you do. At mild intensity - call it tentative trust - you extend small, "
  "low-cost chances: you share a minor detail, accept a small favor, arrive on "
  "time to see if they do. The feeling is light: a little openness, a watchful "
  "ease, one eye still on the exit. At moderate intensity - working trust - the "
  "ledger has enough positive entries that you delegate real things: projects, "
  "plans, confidences that would sting if mishandled. The feeling is steadier: "
  "relaxed collaboration, honest disagreement without flinching, the comfort of "
  "predictability. At high intensity - deep trust - the stakes are the highest "
  "things you have: your safety, your children, your secrets, your future. The "
  "feeling is profound: vulnerability without fear, the sense of being fully known "
  "and still safe, loyalty that does not need to check. The three volumes are not "
  "three different emotions; they are one emotion with the stakes turned up, and "
  "healthy trust usually climbs the volumes in order, earning each level before "
  "the next is offered."),
 "how_it_works": (
  "Intensity in trust tracks two dials: the size of the vulnerability and the "
  "strength of the evidence. Mild trust pairs small stakes with thin evidence - "
  "the system runs in test mode, extending probe-sized risks and watching the "
  "results. Each passed test thickens the evidence, and the acceptable stake size "
  "grows; that is the climb from mild to moderate to deep. The body follows the "
  "dials: mild trust keeps a little muscle tension and alertness, moderate trust "
  "relaxes into routine, deep trust shows the full physiology of safety - slow "
  "breath, open posture, easy laughter. Problems come from volume mismatch: "
  "offering deep-trust stakes on mild-trust evidence (the classic setup for "
  "betrayal), or demanding deep-trust proofs before allowing mild-trust probes "
  "(which starves trust of the very tests it needs to grow)."),
 "key_points": [
  "Mild trust: small probes, watchful ease, low stakes.",
  "Moderate trust: real delegation, relaxed collaboration, honest disagreement.",
  "Intense trust: highest stakes, vulnerability without fear, loyalty.",
  "Intensity follows evidence: each volume must be earned before the next is offered.",
  "Volume mismatch - deep stakes on thin evidence - is where betrayal breeds.",
 ],
 "requirements": [
  "Graduated stakes: chances to risk a little before risking a lot.",
  "A track record long enough to support the current volume.",
  "Both parties roughly agreeing on which volume they are at.",
  "Time: intensity cannot be rushed past what evidence supports.",
 ],
 "standards": [STD["rempel_pdf"], STD["mayer_abi"], STD["berg_game"]],
 "citations": [CIT["rempel"], CIT["mayer"], CIT["berg"]],
 "sig_lens": (
  "The Signature science grades trust like the temper of steel: mild trust is the "
  "first heating, moderate trust the folding, deep trust the final quench. Each "
  "grade is stamped only after it survives its test weight - the Signature rule "
  "is that no bond is called deep until it has carried deep weight and held. "
  "Volume is earned in the forge, never declared in words."),
},
{
 "key": "trust-myths",
 "name": "Common Myths and Misunderstandings About Trust",
 "group": "what trust is",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Myth one: trust means never doubting. In reality, healthy trust includes "
  "verification - checking the work, asking the hard question, noticing the "
  "discrepancy. Doubt aimed at the facts protects trust; it is doubt aimed at "
  "the person, as a permanent verdict, that corrodes it. Myth two: trust, once "
  "broken, can never be rebuilt. Betrayal does damage the ledger badly, but "
  "research on repair shows trust can be rebuilt through acknowledgment, "
  "consistent changed behavior, and time - it returns changed, more deliberate, "
  "but real. Myth three: trusting is the same as being naive. Naivety is trust "
  "without evidence or calibration; genuine trust is evidence-based and "
  "continuously updated. Myth four: distrust is just low trust. They are partly "
  "separate systems: you can simultaneously trust someone's competence and "
  "distrust their discretion. Myth five: trust is all-or-nothing. Real trust is "
  "graded and domain-specific - full trust with money, cautious trust with "
  "secrets, no trust with punctuality, all toward the same person. Myth six: "
  "trustworthy people never fail. Everyone fails; trustworthiness is shown in "
  "what happens after the failure - owning it, fixing it, and changing the "
  "pattern."),
 "how_it_works": (
  "Myths about trust persist because trust itself is partly invisible - you feel "
  "its presence or absence more than you see its machinery. The never-doubt myth "
  "comes from confusing trust with certainty; but trust is defined by uncertainty "
  "accepted, so room for checking is built into it. The never-rebuild myth comes "
  "from the intensity of betrayal pain, which the mind mistakes for permanence; "
  "the ledger can accept new entries, though old red marks remain legible. The "
  "naivety confusion comes from watching uncalibrated trust fail and blaming trust "
  "itself instead of the calibration. Clearing each myth works the same way: "
  "replace the slogan with the mechanism, and the emotion becomes something you "
  "can work with instead of something that happens to you."),
 "key_points": [
  "Healthy trust includes verification; doubt about facts protects it.",
  "Broken trust can be rebuilt through acknowledgment, changed behavior, and time.",
  "Trust is evidence-based and calibrated; naivety is trust without calibration.",
  "Trust and distrust are partly separate systems, not one dial.",
  "Trust is graded and domain-specific, not all-or-nothing.",
  "Trustworthiness is revealed after failure, not by the absence of it.",
 ],
 "requirements": [
  "Willingness to look at the actual mechanics instead of slogans.",
  "Distinguishing the emotion (felt) from the judgment (assessed).",
  "Accepting that uncertainty is part of trust, not its enemy.",
  "Patience with the slow work of repair where repair is possible.",
 ],
 "standards": [STD["mayer_abi"], STD["kramer"], STD["rousseau"]],
 "citations": [CIT["mayer"], CIT["kramer"], CIT["rousseau"]],
 "sig_lens": (
  "The Signature science treats trust-myths as counterfeit seals - they look like "
  "wisdom and stamp false authority on bad practice. The Signature method tests "
  "every saying against the ledger: does never-doubt survive contact with real "
  "evidence? It does not, so the seal is rejected. Only sayings that hold weight "
  "earn a place in the Signature canon of trust."),
},
# ------------------------------------------------------- 5-9: HOW TRUST FEELS
{
 "key": "trust-first-person",
 "name": "Inside Trust: A First-Person Passage",
 "group": "how trust feels",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "This is what trust feels like from the inside, in the present tense. "
  "My shoulders have dropped without me telling them to. I am telling the story "
  "the way it actually happened - the embarrassing part included - and I am not "
  "editing as I go, because I am not bracing for how it will be used. There is a "
  "warmth low in my chest, like sitting near a fire I did not have to build. "
  "When they speak, I listen to the meaning instead of scanning for traps; my "
  "attention is on them, not on my defenses. I notice I have stopped rehearsing "
  "what I will say next. Time feels unhurried, as if there is enough of it. "
  "Underneath it all is the strangest sensation: I am known here - the unpolished "
  "version - and nothing bad is happening because of it. That is the signature "
  "of trust from the inside: the absence of bracing, the presence of ease, and "
  "the quiet willingness to be seen."),
 "how_it_works": (
  "The first-person texture of trust is mostly the feeling of defenses standing "
  "down. When the prediction system rates another person as safe, it withdraws "
  "the costly machinery of vigilance: the rehearsing, the scanning, the editing, "
  "the exit-planning. That withdrawal is experienced as ease, warmth, and "
  "unhurried time - not as a positive sensation added, but as a burden lifted. "
  "Attention, freed from guard duty, can then fully land on the other person, "
  "which deepens connection, which feeds back into the safety prediction. This "
  "is why trust feels self-reinforcing from the inside: safety permits presence, "
  "presence builds closeness, and closeness confirms safety."),
 "key_points": [
  "From the inside, trust feels like bracing stopping: shoulders drop, editing stops.",
  "Attention shifts from scanning for traps to actually listening.",
  "Time feels unhurried; there is a sense of enough.",
  "The core sensation: being known as-is and remaining safe.",
  "Trust feels self-reinforcing: safety permits presence, presence confirms safety.",
 ],
 "requirements": [
  "A safety prediction strong enough to stand down vigilance.",
  "An actual other person (or reliable pattern) to land attention on.",
  "Freedom from immediate threat - trust cannot be felt mid-emergency.",
  "Enough familiarity that the nervous system recognizes the situation.",
 ],
 "standards": [STD["mcallister_ab"], STD["rempel_pdf"], STD["ekman_face"]],
 "citations": [CIT["mcallister"], CIT["rempel"], CIT["ekman"]],
 "sig_lens": (
  "The Signature science calls this inner state the seal at rest - the stamped "
  "covenant lying quiet in the chest, needing no guard because the ledger is "
  "clean. In the Signature telling, you know the seal is genuine when you stop "
  "performing: the unedited story, the unrehearsed answer, the unhurried hour. "
  "The seal does not shout; it rests."),
},
{
 "key": "trust-over-time",
 "name": "The Arc of Trust: Onset, Peak, Fading, and Aftershock",
 "group": "how trust feels",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Trust has a characteristic arc over time, and each phase feels different. "
  "Onset is the testing phase: small probes, careful watching, a tentative "
  "warmth that keeps one eye open. It feels like spring ice - promising, not "
  "yet load-bearing. The rise comes with accumulated evidence: kept promises "
  "stacking up, predictions confirmed, the watchfulness relaxing by degrees. "
  "Peak trust is the plateau of ease described in the first-person passage - "
  "full reliance, unguarded presence, the relationship running on implicit "
  "understanding. Fading is quieter than people expect: not a dramatic break "
  "but a slow cooling, as missed follow-throughs and small evasions accumulate "
  "unnoticed until one day the ease is gone and you cannot say exactly when it "
  "left. Then the aftershock: after a betrayal or a slow fade, the system stays "
  "sensitized for a while - old cues trigger old alarms, even in new "
  "relationships, until fresh evidence retrains the prediction. Knowing the arc "
  "matters because each phase asks for different behavior: probes during onset, "
  "stewardship at peak, attention during fading, and patience through aftershock."),
 "how_it_works": (
  "The arc follows the ledger mechanics. Onset is low-balance, high-monitoring: "
  "every entry is scrutinized because the balance cannot absorb a loss. As the "
  "balance grows, monitoring relaxes - the system can afford to stop checking "
  "every line, which is experienced as ease. Fading is the balance draining "
  "through many small withdrawals nobody reconciled; because no single withdrawal "
  "was large, no alarm fired, which is why fading surprises people. Aftershock is "
  "the prediction system keeping its threat threshold lowered after a big loss - "
  "a rational overcorrection that protects against repeat betrayal but taxes new "
  "trust until enough safe entries accumulate. The whole arc is the ledger "
  "balance made audible as feeling."),
 "key_points": [
  "Onset: tentative probes, watchful warmth, testing phase.",
  "Peak: plateau of ease, implicit understanding, full reliance.",
  "Fading: slow cooling through unreconciled small withdrawals - quiet, not dramatic.",
  "Aftershock: sensitized alarms after betrayal; new trust pays old debts until retrained.",
  "Each phase asks for different behavior: probe, steward, attend, be patient.",
 ],
 "requirements": [
  "Repeated interactions over time - the arc needs a timeline.",
  "A memory system that tallies evidence across encounters.",
  "Varying stakes so the system can calibrate at each phase.",
  "Recovery time after rupture before the arc can restart cleanly.",
 ],
 "standards": [STD["rempel_pdf"], STD["gottman_trust"], STD["simpson"]],
 "citations": [CIT["rempel"], CIT["gottman"], CIT["simpson"]],
 "sig_lens": (
  "The Signature science reads the arc as the life of a seal: cut in the testing "
  "fires of onset, polished to full brightness at peak, dulled by the slow "
  "friction of fading, cracked by betrayal, and - if the covenant is renewed - "
  "recut deeper than before. The Signature rule of the arc: never rush a phase, "
  "and never mistake the aftershock for the person's character."),
},
{
 "key": "trust-low-vs-high",
 "name": "Trust at Low Intensity and High Intensity: Two Snapshots",
 "group": "how trust feels",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Low-intensity trust, up close: You have just met the new neighbor. You lend "
  "the hedge trimmer and mention you will need it back Sunday. Your voice is "
  "friendly and your body is relaxed, but some part of you notes the date, and "
  "you feel a small, almost amused flicker of uncertainty as they walk away with "
  "it. You are not worried - the stakes are a trimmer - but you are observing. "
  "If it comes back clean and on time, something small and warm registers: noted. "
  "High-intensity trust, up close: Your oldest friend calls at midnight from a "
  "hospital two towns over. You are in the car before the call ends, no questions "
  "about repayment or inconvenience crossing your mind. On the drive, your chest "
  "feels open and steady; there is grief and worry about the situation, but zero "
  "friction about the person. You would hand them your house keys, your child, "
  "your confession, in any order. The difference is not just amount - it is kind: "
  "low trust is a hypothesis being tested, high trust is a settled fact being "
  "lived in. Both are the same emotion, but they authorize completely different "
  "lives."),
 "how_it_works": (
  "The two snapshots show the prediction system at different balances. At low "
  "intensity the ledger is thin, so the system keeps its monitoring budget high: "
  "dates are noted, small tests are run, uncertainty is felt as a light, tolerable "
  "hum. The stakes are deliberately capped so a default costs little - this is "
  "rational probe design. At high intensity the ledger is deep, monitoring "
  "spending drops toward zero, and the freed attention becomes presence and "
  "generosity. The settled-fact quality comes from prediction error approaching "
  "zero across hundreds of past interactions: the system has stopped asking the "
  "question because the answer has been the same every time. Moving between the "
  "snapshots is the work of the arc - evidence, slowly, converts hypothesis into "
  "fact."),
 "key_points": [
  "Low trust feels like a hypothesis: light uncertainty, active observation, capped stakes.",
  "High trust feels like a settled fact: open chest, zero friction, full authorization.",
  "The difference is qualitative, not just quantitative - different lives are authorized.",
  "Low trust is rational probe design; high trust is prediction error near zero.",
  "The snapshots are connected by the slow work of evidence.",
 ],
 "requirements": [
  "Contrasting stake sizes to make the volumes visible.",
  "A thin ledger for the low snapshot, a deep one for the high.",
  "Honest self-observation: noticing the hum of monitoring vs. its absence.",
  "No rushing: the high snapshot cannot be willed into being.",
 ],
 "standards": [STD["berg_game"], STD["rempel_pdf"], STD["mayer_abi"]],
 "citations": [CIT["berg"], CIT["rempel"], CIT["mayer"]],
 "sig_lens": (
  "The Signature science keeps both snapshots in the same frame: the trimmer lent "
  "on Sunday and the midnight drive are two entries in one ledger, years apart. "
  "The Signature teaching is that the midnight drive was authorized by a thousand "
  "returned trimmers - small seals kept, each one stamping the covenant a little "
  "deeper, until the bond could carry any weight."),
},
{
 "key": "trust-mixed-affection",
 "name": "Trust Mixed with Affection: Its Most Common Partner",
 "group": "how trust feels",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "Trust rarely travels alone, and its most frequent companion is affection - "
  "warmth, fondness, liking. Felt together, they are the core of close bonds: "
  "trust says 'I am safe with you,' affection says 'I delight in you,' and the "
  "blend says 'you are my person.' The mixture changes both ingredients. "
  "Affection makes trust feel warmer and more generous: you extend the benefit "
  "of the doubt faster, forgive lapses sooner, and feel the bond as comfort "
  "rather than contract. Trust makes affection feel safer and more durable: "
  "fondness without trust is fragile and anxious, but fondness anchored in "
  "trust can relax completely. The blend has its own failure mode worth knowing: "
  "affection can bribe the trust ledger, letting warmth override missing "
  "evidence - the reason people trust charming partners with things they would "
  "never trust a stranger with. Healthy blending keeps both channels honest: "
  "let affection warm the bond, but let evidence - not fondness - set the "
  "stakes."),
 "how_it_works": (
  "In Plutchik's terms this is the primary dyad of love: joy-family affection "
  "fused with trust. The two systems interact rather than merely add. Affection "
  "raises the prior: the prediction system starts from 'probably safe' instead "
  "of neutral, so less evidence is demanded per unit of trust - efficient for "
  "bonding, risky for calibration. Trust, in turn, damps affection's volatility: "
  "securely trusted affection does not spike and crash with every mood, because "
  "the safety prediction holds steady underneath. The bribe effect is the prior "
  "overwhelming the evidence channel - the ledger stops being updated because "
  "the feeling is pleasant. The correction is procedural, not emotional: keep "
  "score on promises even when you are fond, and let the ledger have its vote."),
 "key_points": [
  "Trust + affection is the classic blend at the heart of close bonds.",
  "Affection warms trust: faster benefit of the doubt, quicker forgiveness.",
  "Trust steadies affection: fondness becomes durable instead of anxious.",
  "Failure mode: affection bribing the ledger - warmth overriding missing evidence.",
  "Keep both channels honest: affection warms, evidence sets the stakes.",
 ],
 "requirements": [
  "Both emotions genuinely present - fondness plus a safety record.",
  "A bond with repeated contact, where blending has time to form.",
  "Separate bookkeeping: track evidence even when feeling warm.",
  "Awareness of the bribe effect in yourself and others.",
 ],
 "standards": [STD["plutchik_dyad"], STD["mcallister_ab"], STD["rempel_pdf"]],
 "citations": [CIT["plutchik"], CIT["mcallister"], CIT["rempel"]],
 "sig_lens": (
  "The Signature science calls this blend the gilded seal - the covenant of "
  "trust overlaid with the gold of affection. It is the most beautiful alloy in "
  "the archive and the one most often counterfeited, because gold plating can "
  "hide a hollow seal. The Signature test of the gilded seal: strip the warmth "
  "away in your mind and ask whether the ledger alone still holds."),
},
{
 "key": "trust-day-in-life",
 "name": "A Day in the Life of Trust: An Ordinary-Day Vignette",
 "group": "how trust feels",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "Morning: you wake and check the message from your sister - she handled the "
  "appointment you were dreading, exactly as promised. A small warm click, the "
  "ledger stamping itself before coffee. Midday: at work, your manager assigns "
  "you the client presentation with no hovering and no check-in schedule. You "
  "feel the absence of surveillance as a kind of respect, and you work harder "
  "for it. Afternoon: your teenager tells you the unvarnished truth about the "
  "dented fender. You feel the sting of the repair bill and, underneath it, a "
  "deeper satisfaction - they trusted you with the truth, which means your "
  "trust in them was well placed. Evening: old friends around a table, the "
  "conversation dropping into the honest register within minutes - no "
  "performing, no scoring points, everyone known and still welcome. Night: you "
  "hand tomorrow's early airport run to a friend without a backup plan, and fall "
  "asleep without rehearsing contingencies. None of these moments is dramatic. "
  "That is the point: lived trust is not a peak experience but a climate - "
  "dozens of small deposits and withdrawals, mostly deposits, forming the "
  "weather of an ordinary good day."),
 "how_it_works": (
  "The vignette shows trust as infrastructure rather than event. Each micro-scene "
  "is a ledger transaction: the sister's kept promise (deposit), the manager's "
  "non-surveillance (deposit, and a withdrawal of monitoring costs), the teen's "
  "honesty (deposit that also pays interest, since honesty under risk is strong "
  "evidence), the friends' unguarded evening (the dividend of a deep balance), "
  "the airport run (a stake authorized by the day's running balance). None "
  "required deliberation because the balances were already computed; trust does "
  "its work precisely by moving decisions off the deliberative system and onto "
  "the prediction system. A day like this is what a well-kept ledger feels like "
  "from the inside: not thrilling, just profoundly workable."),
 "key_points": [
  "Lived trust is a climate of small transactions, not a peak event.",
  "Each ordinary scene is a ledger entry: deposits, dividends, authorized stakes.",
  "Trust works by moving decisions from deliberation to prediction - less friction.",
  "Being trusted (the manager's non-surveillance) motivates as much as trusting.",
  "The dividend of deep trust: unguarded presence, no performing.",
 ],
 "requirements": [
  "Ongoing relationships with repeated daily contact.",
  "A history deep enough that most decisions run on prediction.",
  "Small daily stakes where deposits can accumulate.",
  "Attention enough to notice the climate - it is easy to take for granted.",
 ],
 "standards": [STD["rempel_pdf"], STD["gottman_trust"], STD["mayer_abi"]],
 "citations": [CIT["rempel"], CIT["gottman"], CIT["mayer"]],
 "sig_lens": (
  "The Signature science loves ordinary days, because the covenant is not proven "
  "in crises but in Tuesdays. The kept appointment, the unhovered project, the "
  "honest fender confession, the unguarded table, the unplanned-for airport run - "
  "each is a small seal stamped in the ledger. The Signature saying: count the "
  "Tuesdays and you will know the covenant."),
},

# ---------------------------------------------------------- 10-13: BODY SIGNALS
{
 "key": "trust-body",
 "name": "The Body on Trust: Heart, Breath, Muscle, and Energy",
 "group": "body signals",
 "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "The body on trust is a body standing down. The heart settles into a slow, "
  "even rhythm rather than the quick, shallow beat of vigilance; there is no "
  "drum of alarm because no alarm is ringing. Breathing deepens and slows, "
  "dropping low into the belly instead of riding high and tight in the chest, "
  "and sighs come easily - the long exhale of a system releasing its guard. "
  "Muscles let go of their readiness: the jaw unclenches, the shoulders drop "
  "away from the ears, the hands open instead of gripping, the stomach "
  "loosens enough that hunger and digestion behave normally. Skin runs warm "
  "and the face may flush lightly with ease rather than pale with fear. Energy "
  "feels available rather than conserved: trusted company is oddly "
  "restorative, and people often notice they are less tired after an evening "
  "with trusted friends than after an afternoon of guarded small talk. None of "
  "this is dramatic - trust is a low-arousal, positive state, and its body "
  "signature is the quiet of systems at rest. The contrast is the tell: the "
  "same body, in the same chair, with an untrusted person, sits a half-inch "
  "taller with tension, breathes a touch faster, and tires sooner."),
 "how_it_works": (
  "The physiology follows the prediction. When the brain's safety estimate is "
  "high, it downregulates the defensive branches of the autonomic nervous "
  "system: sympathetic arousal eases, and the parasympathetic 'rest and digest' "
  "branch takes the lead. Heart rate variability tends to rise - a marker of a "
  "flexible, unthreatened system - breathing slows, and muscle tone drops toward "
  "baseline. Laboratory work has even linked trust behaviors with oxytocin "
  "signaling, the neurochemistry of calm bonding, though the science there is "
  "still young and should not be overstated. The key mechanism is resource "
  "economics: vigilance is metabolically expensive, and a trusted environment "
  "lets the body stop paying for guards it does not need. That saved budget is "
  "what people feel as ease, warmth, and available energy."),
 "key_points": [
  "Trust is low-arousal and positive: the body signature is systems at rest.",
  "Heart slows and steadies; breath deepens and drops into the belly.",
  "Jaw, shoulders, hands, and gut release their readiness tension.",
  "Trusted company is restorative; guarded company is tiring - the contrast is the tell.",
  "Vigilance is metabolically expensive; trust lets the body stop paying for it.",
 ],
 "requirements": [
  "A genuine safety prediction - the body cannot be ordered to stand down.",
  "Absence of concurrent threat or pain, which override the trust signal.",
  "A baseline of physical health; illness and exhaustion mask the signature.",
  "Familiarity enough that the setting itself is not the alarm.",
 ],
 "standards": [STD["mcallister_ab"], STD["ekman_face"], STD["simpson"]],
 "citations": [CIT["mcallister"], CIT["kosfeld"], CIT["simpson"]],
 "sig_lens": (
  "The Signature science reads the trusting body as the seal at rest - every "
  "muscle a guardsman stood down, every breath a quiet watch-tower with no "
  "enemy in sight. The Signature teaching: the body keeps the truest ledger, "
  "because it cannot be flattered or argued into ease. When the shoulders drop "
  "on their own, the seal is genuine."),
},
{
 "key": "trust-posture",
 "name": "The Posture of Trust: How the Body Carries It",
 "group": "body signals",
 "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Trust has a posture, and it is the posture of nothing to hide. The torso "
  "stays open - chest facing the other person rather than angled away, arms "
  "uncrossed or resting loosely, no bag or table held like a shield. The head "
  "tilts slightly, exposing the neck a fraction, an ancient signal of "
  "non-threat that still reads clearly. People lean in rather than back, close "
  "distance rather than hold it, and their gestures grow larger and more fluid "
  "because the body is not spending effort on self-containment. Stillness "
  "changes too: the trusted person can be comfortably still, without the "
  "fidgeting and position-shifting that leaks unease. Feet point toward the "
  "trusted other; the whole body orients like a sunflower. In groups, high "
  "trust shows as relaxed synchrony - people unconsciously matching posture "
  "and rhythm, leaning the same way at the same joke. Watch for the negative "
  "space: trust is visible in the defenses that are absent - no crossed arms, "
  "no barrier objects, no angling toward the exit."),
 "how_it_works": (
  "Posture is the body's public broadcast of its prediction, and it is hard to "
  "fake for long because it runs on old, fast circuitry. Openness signals flow "
  "both ways: adopting an open posture can nudge the feeling of trust upward, "
  "and feeling trust opens the posture - a feedback loop that is why trusted "
  "pairs literally lean into each other over an evening. The exposed-neck tilt "
  "and the uncrossed torso are appeasement and affiliation displays with deep "
  "evolutionary roots: they say 'I am not a threat and I do not take you for "
  "one.' Synchrony adds a second channel: matched posture and movement rhythm "
  "signal 'we are on the same team,' and the nervous system reads the match as "
  "further evidence of safety. That is why the posture of trust is contagious - "
  "one open body invites another."),
 "key_points": [
  "Open torso, uncrossed arms, no barrier objects - the posture of nothing to hide.",
  "Slight head tilt and leaning in: ancient affiliation signals, still legible.",
  "Comfortable stillness replaces fidgeting; gestures grow larger and fluid.",
  "Trust is visible in absent defenses: no exit-angling, no shielding.",
  "Postural synchrony in groups broadcasts and builds shared trust.",
 ],
 "requirements": [
  "A body free to move - injury, restraint, or formal settings mask posture.",
  "Cultural literacy: openness displays vary in emphasis across cultures.",
  "Sustained observation: posture leaks over minutes, not in a snapshot.",
  "Baseline comparison: know the person's guarded posture to spot the difference.",
 ],
 "standards": [STD["ekman_face"], STD["bowlby_attach"], STD["mcallister_ab"]],
 "citations": [CIT["ekman"], CIT["bowlby"], CIT["mcallister"]],
 "sig_lens": (
  "The Signature science calls the trusting posture the open seal - the covenant "
  "worn on the outside, where all can read it. No crossed arms guard the stamp, "
  "no barrier hides it, the neck is offered to show the seal is not a weapon. "
  "The Signature rule of posture: a seal held openly is a seal that expects to "
  "be honored - and invites the same openness in return."),
},
{
 "key": "trust-sleep-appetite",
 "name": "Trust, Sleep, Appetite, and Energy",
 "group": "body signals",
 "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Trust reaches into the body's maintenance systems. Sleep comes easier in "
  "trusted environments: people fall asleep faster, wake less in the night, and "
  "report deeper rest when they feel safe with those around them - the old "
  "logic being that a guarded animal sleeps with one eye open. Children show "
  "this most clearly, settling quickly in trusted care and resisting sleep "
  "amid uncertainty. Appetite normalizes too: the unclenched gut digests "
  "without protest, meals are enjoyed rather than endured, and the stress "
  "patterns of eating too little or too much ease when the background threat "
  "level drops. Energy follows: because vigilance is expensive, trusted days "
  "cost less, and people describe a clean, available tiredness at day's end "
  "instead of the wired exhaustion of guarded days. The reverse is equally "
  "real and worth knowing: betrayal can disturb sleep for weeks, sour the "
  "stomach, and drain energy, because the prediction system has raised the "
  "threat budget overnight. These are not character flaws; they are the "
  "maintenance crew responding to the ledger."),
 "how_it_works": (
  "Sleep, appetite, and energy are all governed by the same threat-budget "
  "logic as the muscles. Falling asleep requires the brain to voluntarily "
  "surrender vigilance, which it will only do when the safety prediction is "
  "high - this is why unfamiliar beds and untrusted company both cost sleep. "
  "Digestion is a parasympathetic process; it proceeds best when the "
  "sympathetic branch stands down, which is exactly what trust authorizes. "
  "Energy availability is the budget remainder: total metabolic budget minus "
  "the vigilance tax. Trust lowers the tax, so more budget remains for work, "
  "play, and repair. After betrayal the tax spikes - hypervigilance, rumination, "
  "broken sleep - and the body runs a deficit until the ledger is reconciled "
  "and the system stands down again."),
 "key_points": [
  "Trusted environments: faster sleep onset, fewer night wakings, deeper rest.",
  "Appetite normalizes as the gut unclenches; stress eating patterns ease.",
  "Trusted days cost less energy - clean tiredness instead of wired exhaustion.",
  "Betrayal can disturb sleep, appetite, and energy for weeks: the threat budget spikes.",
  "Children show the sleep effect most clearly - settling in trusted care.",
 ],
 "requirements": [
  "A stable enough environment that safety predictions can form.",
  "Time: sleep and appetite respond over days, not moments.",
  "Ruling out medical causes before reading these as trust signals.",
  "Recovery time after rupture - the maintenance crew needs to stand down gradually.",
 ],
 "standards": [STD["bowlby_attach"], STD["simpson"], STD["mcallister_ab"]],
 "citations": [CIT["bowlby"], CIT["simpson"], CIT["mcallister"]],
 "sig_lens": (
  "The Signature science honors sleep as the seal's nightly audit: only a clean "
  "ledger lets the guards sleep at their posts. The Signature observation is "
  "plain - count how a household sleeps and you have read its covenant without "
  "asking a single question. Guard the trust, and the nights take care of "
  "themselves."),
},
{
 "key": "trust-body-differences",
 "name": "No Two Bodies Trust Alike: Individual Differences",
 "group": "body signals",
 "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "The body signature of trust is real, but it is not uniform - people vary "
  "widely in how their bodies express it. Some people are physiologically "
  "expressive: their ease shows in visible relaxation, warm flushing, easy "
  "laughter, expansive gestures. Others run quiet: their trust shows only as "
  "the absence of tension, detectable mainly by comparing them against their "
  "own guarded baseline. Temperament matters: naturally high-arousal people may "
  "show trust as animated warmth, while low-arousal people show it as deep "
  "stillness - both are genuine. Life history matters more: people raised in "
  "unpredictable environments often carry a higher baseline vigilance, so their "
  "trust looks cautious longer and their stand-down is subtler; this is "
  "adaptation, not coldness. Culture shapes display: some traditions encourage "
  "open physical warmth, others reserve it, and the same internal trust reads "
  "differently on the outside. Age and health matter too - a tired or unwell "
  "body cannot fully display ease no matter how deep the trust. The practical "
  "rule: never read trust from a universal checklist. Read it from the person - "
  "their guarded baseline versus their easy moments, tracked over time."),
 "how_it_works": (
  "Individual differences arise because the trust signal passes through each "
  "person's unique physiology before reaching the surface. Baseline autonomic "
  "tone varies: some nervous systems idle hot, others cool, so the same safety "
  "prediction produces different absolute readings. Attachment history calibrates "
  "the prediction system itself - early environments tune how much evidence the "
  "system demands and how fast it stands down, settings that persist into adult "
  "physiology. Display rules, learned culturally and familially, then filter "
  "what the body is allowed to show. The result is that trust has a universal "
  "direction (toward ease, openness, and rest) but personal coordinates. "
  "Within-person comparison - this body guarded versus this body at ease - "
  "cancels the individual differences and reveals the signal cleanly."),
 "key_points": [
  "Trust moves every body toward ease, but the visible amount varies widely.",
  "Compare each person to their own guarded baseline, not to a universal checklist.",
  "History of unpredictability raises baseline vigilance - caution is adaptation, not coldness.",
  "Culture, temperament, age, and health all reshape the outward display.",
  "The direction is universal; the coordinates are personal.",
 ],
 "requirements": [
  "Knowledge of the individual's guarded baseline for comparison.",
  "Observation over time - single snapshots mislead.",
  "Respect for cultural and temperamental display differences.",
  "Humility: the quietest bodies often hold the deepest trust.",
 ],
 "standards": [STD["bowlby_attach"], STD["ekman_face"], STD["simpson"]],
 "citations": [CIT["bowlby"], CIT["ekman"], CIT["simpson"]],
 "sig_lens": (
  "The Signature science stamps every seal in the metal of its bearer: no two "
  "seals shine alike, though all are genuine. The Signature rule of reading "
  "bodies is the jeweler's rule - know the metal before you judge the shine. "
  "A quiet seal is not a weak seal; some of the deepest covenants in the "
  "archive are kept by the stillest bodies."),
},
# ----------------------------------------------------- 14-17: FACIAL EXPRESSION
{
 "key": "trust-face",
 "name": "The Face of Trust: Eyes, Brows, Mouth, and Micro-Signs",
 "group": "facial expression",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "The face of trust is the face with nothing to hide. The eyes hold soft, "
  "steady contact - not staring, not darting, but resting on the other person "
  "with relaxed lids and a slight crinkle at the outer corners when a genuine "
  "smile arrives. The brows sit level and still, free of the raised inner "
  "corners of worry or the lowered press of suspicion; a trusting brow is "
  "simply at rest. The mouth is the clearest billboard: a genuine smile engages "
  "the eyes as well as the mouth (the Duchenne marker - those outer-corner "
  "crinkles), the lips part easily, and the jaw hangs loose instead of "
  "clenching. Micro-signs fill in the picture: slow, easy blinking rather than "
  "rapid flutter; a brief eyebrow flash - a quick lift lasting a fraction of a "
  "second - on greeting someone trusted; the head tilting a few degrees; "
  "laughter that starts in the eyes before the mouth. The whole face reads as "
  "open and unguarded, and the reason it is convincing is that its key "
  "ingredients - the eye crinkles, the relaxed brow, the loose jaw - are "
  "largely outside voluntary control."),
 "how_it_works": (
  "Facial trust signals work because they are hard to counterfeit. The genuine "
  "smile's eye component is driven by the orbicularis oculi muscle, which most "
  "people cannot activate on command - it fires with felt positive affect, "
  "making the crinkled-eye smile an honest signal of real warmth. Brow position "
  "is governed by the same appraisal circuitry as the body's vigilance: worry "
  "raises the inner brow, suspicion lowers and presses it, and safety simply "
  "releases both, which is why the resting brow reads as trust. The loose jaw "
  "and easy blink rate follow autonomic downregulation - tension cannot hide in "
  "the jaw because the jaw is where held tension pools. Observers read this "
  "whole pattern in under a second, mostly below awareness, which is why first "
  "impressions of trustworthiness form so fast and feel so certain."),
 "key_points": [
  "Soft, steady eye contact with relaxed lids; genuine smiles crinkle the outer eye corners.",
  "Brows level and at rest - no worry-lift, no suspicion-press.",
  "Loose jaw, easy lips, slow blinking: tension has nowhere to pool.",
  "Micro-signs: the greeting eyebrow flash, the slight head tilt, laughter starting in the eyes.",
  "The convincing parts are the involuntary ones - hard to fake, fast to read.",
 ],
 "requirements": [
  "A face-to-face (or video) channel - the face cannot broadcast over text.",
  "Enough light and time to read micro-signs; they last fractions of a second.",
  "Knowledge of the person's neutral face as a baseline.",
  "Caution with cultural display rules around eye contact and expressiveness.",
 ],
 "standards": [STD["ekman_face"], STD["mcallister_ab"], STD["simpson"]],
 "citations": [CIT["ekman"], CIT["mcallister"], CIT["simpson"]],
 "sig_lens": (
  "The Signature science calls the trusting face the seal made visible - the "
  "covenant pressed into living wax for all to read. The eye crinkles are the "
  "serrations of a genuine stamp; the resting brow is the flat, even pressure "
  "of an honest press. The Signature rule of faces: a seal that cannot be "
  "counterfeited is the only seal worth reading, and the face of trust is "
  "exactly that."),
},
{
 "key": "trust-face-intensity",
 "name": "How the Face of Trust Changes with Intensity",
 "group": "facial expression",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "The face of trust scales with the volume of the feeling. At mild trust, the "
  "face shows polite openness: a social smile that reaches the mouth but only "
  "lightly touches the eyes, steady but brief eye contact, brows neutral. It is "
  "the face of 'I am willing to see how this goes' - warm, but the crinkles are "
  "shallow and the jaw keeps a little of its readiness. At moderate trust, the "
  "genuine markers arrive: the eye corners crinkle fully, the brow settles "
  "deeper into rest, laughter comes easily and starts in the eyes, the head "
  "tilts during listening. This is the face of established comfort. At deep "
  "trust, the face drops its performance entirely: expressions become unguarded "
  "and unselfconscious, people let their faces show tiredness, worry, or "
  "goofiness without managing the impression, and the resting face itself looks "
  "softer. The paradox of the scale: the deeper the trust, the less the face "
  "performs trust - because performance is a form of vigilance, and vigilance "
  "is what trust retires. Read intensity not by how much the face does, but by "
  "how little it guards."),
 "how_it_works": (
  "Intensity scales the face through the progressive retirement of voluntary "
  "control. Mild trust still runs impression management - the social smile, the "
  "measured contact - because the prediction is not yet settled and the system "
  "keeps its options open. As evidence accumulates, the involuntary markers "
  "(eye crinkles, brow rest, jaw release) strengthen while the voluntary "
  "performance thins; the ratio of genuine-to-managed expression is the real "
  "intensity dial. At deep trust, management drops toward zero and the face "
  "becomes a direct readout of inner state - which is why intimates can read "
  "each other's moods instantly and why the deepest trust looks, to a "
  "stranger, like no particular expression at all. The scale is thus inverted "
  "from what novices expect: more trust, less face-work."),
 "key_points": [
  "Mild trust: polite openness, social smile, shallow crinkles, brief contact.",
  "Moderate trust: full genuine markers - crinkles, resting brow, easy eye-first laughter.",
  "Deep trust: performance retired; the face becomes an unguarded readout.",
  "The intensity dial is the ratio of genuine to managed expression.",
  "Read intensity by how little the face guards, not by how much it does.",
 ],
 "requirements": [
  "Observation across the relationship's timeline to see the scale move.",
  "Distinguishing social politeness (managed) from felt ease (genuine).",
  "Familiarity with the person's full expressive range.",
  "Remembering the inversion: deepest trust can look like no expression at all.",
 ],
 "standards": [STD["ekman_face"], STD["rempel_pdf"], STD["mcallister_ab"]],
 "citations": [CIT["ekman"], CIT["rempel"], CIT["mcallister"]],
 "sig_lens": (
  "The Signature science grades the seal's impression by depth: mild trust "
  "presses lightly, moderate trust presses fully, deep trust needs no pressing "
  "at all - the wax and the seal have become one. The Signature teaching: when "
  "the performance stops, the covenant has arrived. The unguarded face is the "
  "final proof of the stamp."),
},
{
 "key": "trust-face-hidden-faked",
 "name": "Hiding or Faking Trust: What Leaks Through",
 "group": "facial expression",
 "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "People hide or fake trust for understandable reasons - politeness, "
  "negotiation, self-protection - and the face leaks the truth in predictable "
  "places. Hidden distrust (pretending to trust while feeling wary) leaks "
  "through asymmetry and tension: the smile reaches the mouth but not the eyes "
  "(no outer-corner crinkles), the brow holds a faint press or an occasional "
  "worry-lift that contradicts the words, blinking quickens under the load of "
  "monitoring, and the jaw keeps a set it should have released. Faked trust "
  "(performing warmth with an agenda) leaks through timing: the smile arrives a "
  "beat too late or lingers a beat too long, the head nod over-agrees, the eye "
  "contact is held a fraction past comfort - effort showing where ease should "
  "be. The most reliable leak of all is incongruence between channels: warm "
  "words with a still, watchful body, or a smiling mouth above guarded eyes. "
  "None of this makes someone a liar about everything; people manage "
  "expressions for kind reasons too. But the leaks are why the face remains the "
  "fastest trust instrument we have - it reports the prediction system's actual "
  "verdict, not the press release."),
 "how_it_works": (
  "Leakage happens because the face is driven by two systems that do not fully "
  "coordinate. The voluntary system can pose the mouth, hold the gaze, and time "
  "the nod - it handles the press release. The involuntary system, tied to the "
  "actual safety prediction, drives the eye crinkles, brow rest, blink rate, and "
  "jaw tone - and it does not take direction well. Under the load of deception "
  "or concealment, the voluntary system also degrades: timing slips, expressions "
  "become slightly asymmetric (posed expressions often are), and effort becomes "
  "visible as effort. Observers detect all of this through rapid, mostly "
  "unconscious pattern-matching against a lifetime of faces; the 'something is "
  "off' feeling is the mismatch detector firing. Training improves the reading, "
  "but the honest signals stay honest precisely because they resist training."),
 "key_points": [
  "Hidden distrust leaks via mouth-only smiles, brow press, quick blinking, set jaw.",
  "Faked trust leaks via timing: late smiles, over-held gaze, over-agreeing nods.",
  "The master leak is channel incongruence: warm words, watchful body.",
  "Leaks come from the involuntary system, which does not take direction.",
  "Managed expressions serve kind purposes too - leaks are data, not verdicts.",
 ],
 "requirements": [
  "Baseline knowledge of the person's genuine expressions.",
  "Attention to micro-timing: fractions of a second carry the signal.",
  "Reading the whole face-body-voice ensemble, not one feature.",
  "Restraint: a leak is a question to explore, not a conclusion to announce.",
 ],
 "standards": [STD["ekman_face"], STD["simpson"], STD["kramer"]],
 "citations": [CIT["ekman"], CIT["simpson"], CIT["kramer"]],
 "sig_lens": (
  "The Signature science has a name for the managed face: the painted seal. "
  "Paint can imitate the stamp's colors but never its pressed depth, and the "
  "trained eye reads the difference in the crinkles, the timing, the jaw. The "
  "Signature rule is merciful here: a painted seal is not always a crime - "
  "sometimes it is politeness, sometimes armor. Read the paint, note the depth, "
  "and judge the covenant by the ledger, not the coating."),
},
{
 "key": "trust-expression-gallery",
 "name": "Drawing Trust: Expression Notes for Artists and Actors",
 "group": "facial expression",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "To draw or play trust, build the face from rest, not from action. Start "
  "with the brow: level, smooth, the forehead unlined - erase every trace of "
  "the worry-lift and the suspicion-press. Set the eyes next: lids relaxed to "
  "their natural line, gaze soft and direct, and - for the genuine smile - add "
  "the fine radiating lines at the outer corners, the single most load-bearing "
  "detail. The mouth should look unheld: lips together or lightly parted "
  "without pressing, corners lifted by ease rather than effort, the jaw "
  "visibly unclenched with a hint of softness under the chin. Tilt the head "
  "two or three degrees - enough to read as openness, not enough to read as "
  "confusion. For the actor: let the breath drop low and slow before the "
  "expression, because the face follows the body; think of someone you trust "
  "completely and let the memory do the musculature. For the artist: light the "
  "face warmly and keep the lines soft - trust has no sharp edges. The classic "
  "mistake is over-smiling: a huge toothy grin reads as performance or "
  "nervousness. Real trust on the face is quiet - draw the absence of guarding, "
  "and the viewer will feel the presence of trust."),
 "how_it_works": (
  "The gallery notes work because they reconstruct the involuntary pattern "
  "deliberately. Each instruction targets a muscle group the safety prediction "
  "normally controls: frontalis (brow) released, orbicularis oculi (eye "
  "corners) engaged, masseter (jaw) released, sternocleidomastoid eased into "
  "the tilt. The actor's memory trick works through embodied simulation - "
  "recalling a trusted person reactivates the associated safety prediction, "
  "which drives the musculature more authentically than posing each feature. "
  "The artist's soft-lighting note works through viewer psychology: observers "
  "read harsh shadows and sharp lines as threat cues, so softness in rendering "
  "primes the trust reading before the features are even parsed. The "
  "over-smiling warning reflects the genuineness ratio - audiences, like real "
  "observers, weight the eye crinkles over the mouth stretch."),
 "key_points": [
  "Build from rest: level brow, smooth forehead, unclenched jaw.",
  "The outer eye-corner lines are the single most load-bearing detail.",
  "Head tilt of two to three degrees reads as openness.",
  "Actors: drop the breath first and use trusted-person memory - the face follows.",
  "Avoid the over-smile: draw the absence of guarding, not a performance of joy.",
 ],
 "requirements": [
  "Anatomical knowledge of which muscles carry the trust pattern.",
  "For actors: a genuine trusted-person memory to drive the simulation.",
  "For artists: soft rendering - trust has no sharp edges.",
  "Restraint: the quiet face convinces; the loud face performs.",
 ],
 "standards": [STD["ekman_face"], STD["plutchik_dyad"], STD["mcallister_ab"]],
 "citations": [CIT["ekman"], CIT["plutchik"], CIT["mcallister"]],
 "sig_lens": (
  "The Signature science keeps a gallery of seals as well as ledgers, and the "
  "portrait of trust hangs at its center: brow level as a pressed plate, eye "
  "corners serrated like a true stamp, jaw loose as warm wax. The Signature "
  "instruction to the artist is the instruction to the witness: render what is "
  "there, soften nothing, sharpen nothing - a true seal needs no retouching, "
  "and a faithful portrait is itself an act of trust."),
},

# ------------------------------------------------------------ 18-21: TRIGGERS
{
 "key": "trust-classic-triggers",
 "name": "The Classic Triggers of Trust",
 "group": "triggers",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Certain situations, words, and events trigger trust so reliably that they "
  "appear in the research again and again. Kept promises are the classic: a "
  "promise made and then visibly kept, especially a small one, deposits "
  "directly into the ledger - reliability in miniature. Consistency across "
  "time and mood: the person who is the same on a bad day as a good day "
  "teaches the prediction system that they are predictable. Vulnerability met "
  "with care: when someone shares something tender and is received gently, "
  "trust spikes - the system learns that openness is safe here. Competence "
  "under pressure: watching someone handle a hard thing well triggers "
  "cognition-based trust fast. Honesty at a cost: admitting a mistake or "
  "delivering bad news straight, when a dodge would have been easier, is one "
  "of the strongest triggers known - it proves integrity precisely because it "
  "was expensive. Words trigger it too: 'I was wrong,' 'I will handle it,' "
  "'your call,' and the quiet 'I have got you' all signal benevolence and "
  "reliability. Events: being defended when absent, being chosen when it "
  "costs the chooser, surviving something hard together. The common thread: "
  "each classic trigger is evidence about ability, benevolence, or integrity "
  "arriving in a form the prediction system cannot ignore."),
 "how_it_works": (
  "Classic triggers work because they are high-diagnostic evidence - hard to "
  "produce without the underlying trait. A kept small promise is diagnostic "
  "because faking reliability across many small instances is exhausting; "
  "consistency is diagnostic because moods change but character does not; "
  "honesty at a cost is diagnostic because only the genuinely principled pay "
  "for honesty when no one would know. The prediction system weights such "
  "evidence heavily, which is why one costly honesty can outweigh months of "
  "cheap politeness. The trigger fires in two stages: first the appraisal "
  "('that was real'), then the ledger update and the felt shift - the small "
  "warm click of the balance moving. Repeated classic triggers compound: each "
  "one not only adds its own deposit but raises the weight given to the next, "
  "which is how trust accelerates once it gets going."),
 "key_points": [
  "Kept small promises: reliability in miniature, the most repeatable trigger.",
  "Consistency across moods proves predictability to the system.",
  "Vulnerability met with care teaches that openness is safe here.",
  "Honesty at a cost is the highest-diagnostic trigger - integrity proven by price paid.",
  "Trigger words: 'I was wrong,' 'I will handle it,' 'your call,' 'I have got you.'",
  "Triggers compound: each one raises the weight given to the next.",
 ],
 "requirements": [
  "An actual event or message carrying diagnostic evidence.",
  "Attention enough to register it - triggers missed do not fire.",
  "A receiver willing to update - entrenched distrust can block even strong triggers.",
  "Follow-through after the trigger: one deposit does not make a balance.",
 ],
 "standards": [STD["mayer_abi"], STD["berg_game"], STD["gottman_trust"]],
 "citations": [CIT["mayer"], CIT["berg"], CIT["gottman"]],
 "sig_lens": (
  "The Signature science calls the classic triggers the striking of the seal - "
  "each one a hammer blow that drives the stamp deeper into the wax. The kept "
  "promise, the costly honesty, the defense in absence: these are not "
  "sentiments but strikes, and the Signature rule counts them. A covenant with "
  "many strikes holds; a covenant with none is only words waiting for weather."),
},
{
 "key": "trust-personal-triggers",
 "name": "Personal Triggers of Trust: Memory and Association",
 "group": "triggers",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Beyond the universal triggers, each person carries a private set - "
  "memories, anniversaries, and associations that open or close trust for "
  "reasons only their history explains. The smell of a workshop that recalls "
  "a grandfather who always kept his word. A phrase - 'we will figure it out' - "
  "that a once-reliable mentor used, now triggering warmth toward anyone who "
  "says it. The anniversary of a betrayal that makes every October feel "
  "cautious, or of a rescue that makes every spring feel generous. Someone "
  "whose childhood promises were kept trusts quickly and feels bewildered when "
  "others do not; someone whose were broken tests longer and trusts the "
  "testing itself. These personal triggers are not irrational - they are the "
  "prediction system using the largest dataset it has: a lifetime. They become "
  "a problem only when they fire at the wrong target - when a new person pays "
  "for an old betrayal, or charm borrows the glow of a beloved memory. Knowing "
  "your own set is one of the most useful forms of self-knowledge: it lets you "
  "ask, when trust surges or stalls, 'is this about them, or is this about "
  "then?'"),
 "how_it_works": (
  "Personal triggers work through associative learning laid down over years. "
  "The prediction system does not only track the current person; it maintains "
  "priors - starting assumptions - built from the whole history of reliance. A "
  "cue resembling a past reliable figure (voice timbre, phrase, setting, even "
  "smell) activates the old ledger and lends its balance to the new person - "
  "transference of trust. A cue resembling a past betrayer does the reverse, "
  "spending old red ink on a new account. Anniversaries work through "
  "state-dependent memory: the calendar cues the emotional state of the "
  "original event. None of this is under conscious control at the moment of "
  "firing, which is why the triggers feel like intuition. They become accurate "
  "when the resemblance is real and misleading when it is superficial - the "
  "system is pattern-matching, and patterns can rhyme without repeating."),
 "key_points": [
  "Private triggers: memories, anniversaries, sensory associations from personal history.",
  "They set the priors - the starting balance before new evidence arrives.",
  "A cue resembling a past reliable figure lends old trust to new people.",
  "They misfire when a new person pays for an old betrayal - or borrows old glow.",
  "Self-knowledge move: ask 'is this about them, or about then?'",
 ],
 "requirements": [
  "A personal history of reliance - good, bad, or mixed - to learn from.",
  "Cues in the present that resemble the past closely enough to fire.",
  "Enough self-awareness to separate then from now.",
  "New evidence given a fair chance to override old priors.",
 ],
 "standards": [STD["bowlby_attach"], STD["simpson"], STD["erikson_basic"]],
 "citations": [CIT["bowlby"], CIT["simpson"], CIT["erikson"]],
 "sig_lens": (
  "The Signature science honors personal triggers as the old seals in the "
  "archive - every covenant you have ever kept or suffered leaves its stamp in "
  "you, and new wax takes the shape of old presses. The Signature practice is "
  "the annual audit of the heart: lay out the old seals, read which are still "
  "true, and retire the ones that have begun stamping innocent wax."),
},
{
 "key": "trust-surprise-triggers",
 "name": "Surprise Triggers of Trust: The Unexpected Ones",
 "group": "triggers",
 "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Some of the most powerful trust triggers are the ones nobody expects. "
  "The competent rival who warns you about a pitfall instead of letting you "
  "fall in - trust from an enemy's honesty lands harder than from a friend's, "
  "because no motive explains it except character. The stranger who returns "
  "the dropped wallet with the cash untouched, vanishing before thanks - "
  "integrity without an audience is the purest diagnostic there is. Being "
  "trusted first: the manager who hands you the keys on day one, the friend "
  "who confesses something real before you have earned it - receiving trust "
  "triggers giving it, a reciprocity reflex. Shared laughter at the exact same "
  "unspoken thought - minds aligning without negotiation signals deep "
  "compatibility. The apology you did not know you were owed: someone "
  "remembering a small slight for years and finally owning it. Adversity "
  "shared by accident: the delayed flight, the blackout, the wrong turn that "
  "strands two people together - unplanned cooperation fast-forwards bonding. "
  "What makes these surprising is that none is a deliberate trust-building "
  "technique, which is exactly why they work: the prediction system discounts "
  "performed reliability and overweights the unperformed kind."),
 "how_it_works": (
  "Surprise triggers derive their power from the discounting of motive. The "
  "prediction system is constantly asking not just 'what did they do' but 'why "
  "would they do it' - performed kindness is mentally taxed for its possible "
  "motive, while unperformed, costly, or motive-free kindness is credited in "
  "full. The rival's warning, the wallet returned unseen, the apology unasked "
  "for: each passes the motive audit with nothing to discount, so the full "
  "weight lands on the ledger. Being-trusted-first works through reciprocity "
  "and self-perception: receiving trust raises your own trustworthiness "
  "motivation and simultaneously signals the other's judgment of you. Shared "
  "adversity works through swift-trust mechanics - temporary teams form fast "
  "bonds under pressure because cooperation is immediately diagnostic. The "
  "common formula: high diagnosticity times zero suspected motive equals "
  "maximum trigger force."),
 "key_points": [
  "Honesty from a rival and integrity without an audience: motive-free evidence hits hardest.",
  "Being trusted first triggers trusting back - the reciprocity reflex.",
  "Shared unplanned adversity fast-forwards bonding (swift trust).",
  "The unasked-for apology and the shared unspoken laugh: unperformed reliability.",
  "Formula: high diagnosticity times zero suspected motive equals maximum force.",
 ],
 "requirements": [
  "Genuineness - the moment it looks performed, the discount applies.",
  "A receiver whose motive-audit is functioning, not cynical beyond reach.",
  "Usually low prior expectations, which make the surprise possible.",
  "Follow-through: surprise opens the door, consistency walks through it.",
 ],
 "standards": [STD["meyerson_swift"], STD["deutsch_choice"], STD["mayer_abi"]],
 "citations": [CIT["meyerson"], CIT["deutsch"], CIT["mayer"]],
 "sig_lens": (
  "The Signature science treasures surprise triggers as seals struck in the "
  "dark - no audience, no motive, no performance, only the stamp meeting the "
  "wax because that is what stamps do. The rival's warning, the unseen wallet, "
  "the unasked apology: the Signature archive files these under the purest "
  "proofs, the entries no counterfeiter can forge because there is no profit "
  "in forging them."),
},
{
 "key": "trust-chain-reactions",
 "name": "Chain Reactions: How One Trigger Cascades",
 "group": "triggers",
 "ladder_rank": 8, "ladder_tier": "compounded",
 "description": (
  "Trust rarely moves in single steps; one trigger sets off a cascade. It "
  "starts simply: a colleague covers your shift without being asked. That "
  "single deposit does more than add one entry - it retunes the whole "
  "instrument. Suddenly you notice their other reliable acts that you had "
  "been discounting; the prediction system, newly optimistic, starts counting "
  "evidence it previously ignored. You respond with openness - sharing the "
  "real reason you needed the shift covered - and your vulnerability, met with "
  "care, becomes their trigger in return. Now the cascade runs both ways: "
  "each person's trust triggers the other's, each round larger than the last. "
  "The chain spreads sideways too: trusting one team member makes you read the "
  "whole team as more reliable; being trusted makes you act more "
  "trustworthily, which triggers others. Researchers call the dark version the "
  "same machinery in reverse: one betrayal retunes the instrument toward "
  "suspicion, and suddenly every neutral act looks like evidence of threat - "
  "the cascade does not care about direction. The practical lesson: tend the "
  "first domino. Small triggers, aimed well and followed up, move more than "
  "their size suggests - in both directions."),
 "how_it_works": (
  "Cascades run on three linked mechanisms. First, retuning: a strong trigger "
  "shifts the prediction prior, which changes how subsequent evidence is "
  "weighted - the same acts count more once the system expects reliability. "
  "Second, reciprocity: received trust reliably increases trusting and "
  "trustworthy behavior in return, creating a two-person positive feedback "
  "loop documented from the trust game to field studies. Third, generalization: "
  "the updated model spreads to associated people and contexts - the halo of "
  "trust. Each mechanism amplifies the last, which is why cascades are "
  "nonlinear: the tenth deposit can move the balance more than the first nine "
  "combined. The reverse cascade uses identical machinery with the prior "
  "shifted toward threat, which is why betrayal's damage spreads further than "
  "the single act. Interventions target the same three points: re-anchor the "
  "prior with undeniable evidence, restart reciprocity with a first vulnerable "
  "move, and contain generalization by keeping the judgment specific."),
 "key_points": [
  "One trigger retunes the instrument: later evidence gets weighted more.",
  "Reciprocity creates two-way positive feedback - each person's trust feeds the other's.",
  "Trust generalizes sideways to teams and contexts: the halo effect.",
  "Cascades are nonlinear - the tenth deposit can move more than the first nine.",
  "The same machinery runs in reverse after betrayal; tend the first domino.",
 ],
 "requirements": [
  "An initial trigger strong enough to shift the prior.",
  "A responsive other party - cascades need two to tango.",
  "Follow-up deposits before the retuning fades.",
  "Awareness of the reverse cascade so small ruptures get tended early.",
 ],
 "standards": [STD["berg_game"], STD["gottman_trust"], STD["kramer"]],
 "citations": [CIT["berg"], CIT["gottman"], CIT["kramer"]],
 "sig_lens": (
  "The Signature science describes the cascade as seals breeding seals: one "
  "true stamping teaches the wax to receive the next more deeply, and soon "
  "the whole archive shines. The Signature warning is engraved beside it: the "
  "same press that multiplies true seals multiplies cracked ones. Tend the "
  "first domino, stamp the first seal true, and the cascade becomes your "
  "strongest ally."),
},
# ------------------------------------------------------- 22-25: HOW IT SHOWS IN BEHAVIOR
{
 "key": "trust-actions",
 "name": "What People Do When They Trust: Typical Actions",
 "group": "trust in behavior",
 "ladder_rank": 8, "ladder_tier": "compounded",
 "description": (
  "Trust is visible in what people do, long before they declare it. The "
  "signature action is delegation: handing over real responsibility - the "
  "project, the child, the keys, the decision - without hovering, checking, or "
  "building a backup plan. Next is disclosure: telling the unpolished truth, "
  "confessing mistakes early, sharing information that could be used against "
  "them. Then reliance: asking for help instead of struggling alone, accepting "
  "advice and actually following it, letting the other person's judgment "
  "substitute for their own in that domain. Loyalty actions follow: defending "
  "the trusted person when absent, choosing them when it costs, refusing to "
  "entertain gossip about them. Physical and logistical signs accumulate: "
  "lending valued things, merging schedules, leaving belongings unguarded, "
  "falling asleep in their presence. Financial trust has its own ladder: "
  "splitting bills without counting, lending money, joint accounts, each a "
  "higher stake. The unifying logic is always the same: the trusting person "
  "voluntarily increases their vulnerability and decreases their monitoring, "
  "and does so smoothly, without fanfare - trust performed loudly is usually "
  "trust still being negotiated."),
 "how_it_works": (
  "Trust actions are the behavioral output of the prediction system: once the "
  "ledger balance authorizes a stake, the action follows without deliberation. "
  "Delegation is the purest readout because it combines high vulnerability "
  "(real consequences) with low monitoring (no hovering) - the exact formula "
  "of trust. Disclosure works as both evidence and investment: confessing "
  "early gives the other person power over you, which only a trusting system "
  "permits, and it simultaneously triggers their trust in return. The "
  "smoothness matters: effortful, announced trust ('I am trusting you with "
  "this!') still runs on the deliberative system, while quiet, unremarked "
  "reliance shows the prediction system has fully absorbed the balance. "
  "Observers - and the trusted person - read these actions as the honest "
  "signal they are: behavior is harder to fake than words, which is why "
  "actions build trust faster than promises."),
 "key_points": [
  "Delegation without hovering: the purest behavioral readout of trust.",
  "Disclosure: unpolished truth and early confession as trust in action.",
  "Reliance: asking for help, following advice, substituting their judgment for yours.",
  "Loyalty: defending when absent, choosing when it costs, refusing gossip.",
  "Quiet trust convinces; loudly announced trust is usually still being negotiated.",
 ],
 "requirements": [
  "Adequate ledger balance to authorize the stake.",
  "Real stakes available - trust needs something to act on.",
  "Low monitoring: the action must be unhovered to count.",
  "A receiver who registers the action as the signal it is.",
 ],
 "standards": [STD["berg_game"], STD["deutsch_choice"], STD["mayer_abi"]],
 "citations": [CIT["berg"], CIT["deutsch"], CIT["mayer"]],
 "sig_lens": (
  "The Signature science reads actions as the seal in motion: delegation is "
  "the covenant handed over to be carried, disclosure the ledger opened for "
  "inspection, loyalty the seal defended in its absence. The Signature maxim "
  "for behavior: watch the hands, not the mouth - the hands stamp while the "
  "mouth talks, and the archive records what the hands did."),
},
{
 "key": "trust-speech",
 "name": "What People Say When They Trust: Speech and Tone",
 "group": "trust in behavior",
 "ladder_rank": 8, "ladder_tier": "compounded",
 "description": (
  "Trust has a voice. The trusting person speaks plainly: sentences get "
  "shorter and more direct, hedging thins out, and the careful diplomatic "
  "padding of guarded speech falls away - not into rudeness, but into ease. "
  "They ask real questions instead of safe ones, including the naive-sounding "
  "ones, because they are not managing the impression of competence. They "
  "volunteer information before being asked, narrate their reasoning out loud "
  "('here is why I think this'), and admit uncertainty freely - 'I do not "
  "know' becomes easy to say. Tone follows: warmer, slower, with natural "
  "variation instead of the flat control of caution; laughter comes quicker "
  "and lasts longer. Characteristic phrases recur: 'what do you think?' (your "
  "judgment counts), 'I will leave that to you' (delegation in words), 'here "
  "is what actually happened' (unpolished truth), 'tell me straight' "
  "(inviting honesty), and the quiet 'I have got this' offered to the trusted "
  "other. They also talk about the trusted person differently to third "
  "parties: with assumed goodwill, defending before doubting. Listen for what "
  "is absent: no fishing for reassurance, no testing questions with known "
  "answers, no ledger-reciting of past favors. Trusting speech is what remains "
  "when the auditing stops."),
 "how_it_works": (
  "Speech is the cheapest channel for trust signals, which is why the system "
  "weights it less than action - but the pattern still leaks reliably because "
  "guarded speech is cognitively expensive. Hedging, padding, impression "
  "management, and testing questions all consume working memory; when the "
  "safety prediction is high, the brain stops paying for them and speech "
  "simplifies toward directness. Volunteered information and narrated reasoning "
  "are costly signals in reverse: giving away informational advantage only "
  "makes sense if you do not fear exploitation. Admitting 'I do not know' is "
  "diagnostic because it surrenders status - the guarded never yield status "
  "cheaply. Tone carries the autonomic signature: the slower, warmer voice is "
  "the relaxed body speaking. Together, plain words plus easy tone form a "
  "coherent broadcast that listeners decode as trustworthiness within seconds."),
 "key_points": [
  "Plain, direct speech: hedging thins, padding falls away, ease replaces caution.",
  "Real questions and volunteered reasoning - informational advantage freely given.",
  "'I do not know' becomes easy: status surrendered without fear.",
  "Tone: warmer, slower, natural variation; quicker, longer laughter.",
  "Absences tell: no reassurance-fishing, no test questions, no favor-ledger reciting.",
 ],
 "requirements": [
  "A shared language fluent enough that directness reads as ease, not rudeness.",
  "Low enough stakes in the conversation that guardedness is optional.",
  "A listener who rewards plainness rather than punishing it.",
  "Time together: trusting speech patterns emerge over encounters, not one.",
 ],
 "standards": [STD["mcallister_ab"], STD["rempel_pdf"], STD["gottman_trust"]],
 "citations": [CIT["mcallister"], CIT["rempel"], CIT["gottman"]],
 "sig_lens": (
  "The Signature science listens to trusting speech as the covenant spoken "
  "aloud: plain words are unsealed letters, volunteered reasons are open "
  "ledgers, and 'I do not know' is the seal-bearer admitting the stamp's "
  "limits - which only strengthens the seal. The Signature ear is trained on "
  "absences: no audit in the voice means the ledger is clean."),
},
{
 "key": "trust-decisions",
 "name": "How Trust Changes Decisions and Judgment",
 "group": "trust in behavior",
 "ladder_rank": 8, "ladder_tier": "compounded",
 "description": (
  "Trust rewires decision-making, mostly by changing what gets checked. The "
  "trusting decision-maker skips verification steps they would otherwise pay "
  "for: no background check on the referred hire, no second quote when the "
  "trusted contractor names a price, no reading every clause when the advisor "
  "says 'this is standard.' This is rational when the ledger is deep - "
  "verification has real costs in money, time, and relationship friction, and "
  "trust is the mechanism that lets you stop paying them. Judgment shifts "
  "too: ambiguous evidence gets the charitable reading, mistakes get "
  "situational explanations ('they must be overwhelmed') instead of character "
  "ones, and forecasts about the person skew optimistic. Risk tolerance rises "
  "in the trusted domain: bigger bets, longer commitments, less hedging. The "
  "shadow side is well documented: trust reduces scrutiny, and reduced "
  "scrutiny is exactly what exploitation needs - the reason frauds so often "
  "come from inside the circle of trust. Wise trust therefore keeps a "
  "two-track mind: the relationship runs on trust, while proportional "
  "verification runs quietly in the background, aimed at the facts and never "
  "announced as suspicion. Trust changes the decision; it should not abolish "
  "the audit."),
 "how_it_works": (
  "The mechanism is monitoring-budget reallocation. Every decision under "
  "uncertainty can spend resources on verification or accept the risk; trust "
  "is the system's authorization to spend less on verification. This works "
  "through the prediction system substituting its model for fresh data - "
  "efficient when the model is accurate, catastrophic when it is not. The "
  "charitable-interpretation bias follows from the same prior: ambiguous acts "
  "are classified by the reigning model, so a trusted person's lapse reads as "
  "situational and a distrusted person's identical lapse reads as character. "
  "Optimistic forecasting is the prior projected forward. The fraud "
  "vulnerability is structural, not personal: any system that economizes on "
  "verification creates an exploitable niche, which is why the two-track "
  "solution - trust the person, verify the facts - is the stable equilibrium "
  "that high-functioning institutions converge on."),
 "key_points": [
  "Trust authorizes skipping verification: rational when the ledger is deep.",
  "Ambiguity gets charitable readings; lapses get situational explanations.",
  "Risk tolerance and commitment length rise in the trusted domain.",
  "Shadow side: reduced scrutiny is what exploitation needs - fraud comes from inside.",
  "The stable solution: trust the person, verify the facts - two tracks, no conflict.",
 ],
 "requirements": [
  "Decisions under real uncertainty - trust has no work where certainty reigns.",
  "A ledger deep enough to justify the verification skipped.",
  "Proportional background verification aimed at facts, not announced as suspicion.",
  "Willingness to re-engage scrutiny when the facts flag - trust is not a blindfold.",
 ],
 "standards": [STD["mayer_abi"], STD["kramer"], STD["deutsch_choice"]],
 "citations": [CIT["mayer"], CIT["kramer"], CIT["deutsch"]],
 "sig_lens": (
  "The Signature science treats trusted decisions as sealed orders: the "
  "covenant authorizes action without re-litigating every clause, which is "
  "the whole economic value of the seal. But the Signature ledger-keeper "
  "never sleeps: every sealed order is still entered in the books, and the "
  "books are reconciled on schedule. Trust the seal, audit the entries - the "
  "covenant stays strong because the accounting stays honest."),
},
{
 "key": "trust-full-intensity-behavior",
 "name": "Trust at Full Intensity: How Behavior Escalates",
 "group": "trust in behavior",
 "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "At full intensity, trusting behavior stops looking like decisions at all "
  "and starts looking like nature. Delegation becomes total: the surgeon is "
  "handed the unconscious body, the pilot the lives in the cabin, the friend "
  "the combination to the safe - stakes that would be unthinkable at lower "
  "volumes are extended without a flicker of negotiation. Disclosure becomes "
  "confession: the whole unedited history, the shameful parts included, laid "
  "out because hiding anything would feel like a lie against the bond. "
  "Sacrifice enters: time, money, opportunity, and sometimes safety are spent "
  "for the trusted person without a ledger of return - the accounting itself "
  "would insult the bond. Loyalty becomes reflexive: the trusted person is "
  "defended before the accusation is even finished, believed over strangers "
  "as a default. Identity merges at the edges: 'we' replaces 'I' in plans, "
  "their wins feel like your wins, their danger triggers your body. This is "
  "beautiful and it is dangerous in exactly the same way: full-intensity trust "
  "removes every brake, so if the ledger was wrong, the crash is total. The "
  "archive's sober note: escalate behavior only as fast as evidence, and keep "
  "one instrument - the quiet background audit - running even at full "
  "intensity. The deepest trust is not the absence of judgment; it is judgment "
  "so well trained it no longer needs to announce itself."),
 "how_it_works": (
  "Escalation follows the stake-authorization curve to its limit. As the "
  "ledger balance grows enormous relative to any single stake, the marginal "
  "cost of additional vulnerability approaches zero - the system stops "
  "computing per-decision risk because no single decision can move the "
  "balance. Monitoring spending falls to zero, disclosure inhibitions "
  "dissolve, and the other's welfare gets weighted nearly as one's own in the "
  "utility calculus - the mechanism behind sacrifice without scorekeeping. "
  "Identity merging reflects the prediction model becoming shared: the "
  "system models 'us' as a unit because the other's behavior has become as "
  "predictable as one's own. The danger is the same mechanism that makes it "
  "beautiful: with monitoring at zero and stakes at maximum, a single "
  "misjudged ledger means catastrophe. Evolutionarily this is the pair-bond "
  "and kin machinery running at full power - magnificent for cooperation, "
  "terrible as a single point of failure."),
 "key_points": [
  "Delegation becomes total, disclosure becomes confession, loyalty becomes reflexive.",
  "Sacrifice without scorekeeping: the accounting itself would insult the bond.",
  "Identity merges: 'we' replaces 'I'; their wins and dangers become yours.",
  "Beautiful and dangerous identically: every brake removed, so a wrong ledger means total crash.",
  "Escalate only as fast as evidence; keep the quiet background audit running.",
 ],
 "requirements": [
  "A ledger deep enough that single stakes cannot move the balance.",
  "Long history across varied situations, including stress.",
  "Evidence that survived the highest previous tests.",
  "The retained background audit - full trust is trained judgment, not its absence.",
 ],
 "standards": [STD["rempel_pdf"], STD["mayer_abi"], STD["gottman_trust"]],
 "citations": [CIT["rempel"], CIT["mayer"], CIT["gottman"]],
 "sig_lens": (
  "The Signature science calls full-intensity trust the unbreakable seal - the "
  "covenant pressed so deep that wax and stamp are one substance. It is the "
  "highest achievement of the archive and its most solemn warning, engraved on "
  "the same tablet: a seal this deep must be struck only on proven metal, for "
  "there is no deeper press to repair it. Stamp slowly, stamp surely, and the "
  "unbreakable seal will outlast the hands that made it."),
},

# ------------------------------------------------- 26-28: HEALTHY EXPRESSION
{
 "key": "trust-healthy-expression",
 "name": "Expressing Trust in a Healthy Way",
 "group": "healthy expression",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Healthy trust is expressed, not just felt - and the expression itself is a "
  "skill. Say it plainly: 'I trust you with this' is a gift that dignifies "
  "the receiver and clarifies the relationship; unspoken trust can be "
  "mistaken for indifference. Show it in calibrated doses: delegate the "
  "meaningful thing, share the real reason, ask the genuine question - each "
  "act sized to the ledger's actual balance. Receive it gracefully when it "
  "comes to you: being trusted is a responsibility, and the healthy response "
  "is stewardship, not performance - handle the thing well, report back "
  "without being asked, and protect the confided material as your own. "
  "Channel trust into the bond's growth: use the safety to have the hard "
  "conversation, attempt the joint project, repair the old friction - trust "
  "is capital, and capital put to work compounds. Keep the expression "
  "proportional: match the depth of your reliance to the depth of the "
  "evidence, and say so when the evidence is still thin ('I am trusting you "
  "with this early - let us see how it goes'). Healthy expression also means "
  "expressing the boundaries of trust honestly: 'I trust you with X and I am "
  "not there yet with Y' is not an insult but a map. Trust expressed well "
  "builds more trust; that is the whole virtuous circle, and it starts with "
  "the decision to let the inside show."),
 "how_it_works": (
  "Expression closes the loop between the internal prediction and the "
  "relationship. Saying trust aloud converts a private model into common "
  "ground - both parties now know the bond's standing, which coordinates "
  "expectations and authorizes the receiver to act as a trustee. Calibrated "
  "acts of reliance function as both evidence and invitation: they deposit "
  "into the other's ledger ('they counted on me') while testing your own. "
  "Graceful receiving works through stewardship signaling: handling the "
  "entrusted thing well, with unprompted reporting, proves the receiver's "
  "trustworthiness and deepens the giver's model. Proportionality is the "
  "safety valve: sizing reliance to evidence keeps the system in the region "
  "where prediction error stays small, so the virtuous circle compounds "
  "instead of crashing. Honest boundary-mapping prevents the most common "
  "expression failure - implied total trust that was never earned, which "
  "detonates at the first limit encountered."),
 "key_points": [
  "Say it: 'I trust you with this' dignifies and clarifies; unspoken trust reads as indifference.",
  "Show it in calibrated doses, each sized to the ledger's actual balance.",
  "Receive it as stewardship: handle well, report unprompted, protect confidences.",
  "Put trust to work: hard conversations, joint projects, repairs - capital compounds.",
  "Map the boundaries honestly: 'I trust you with X; not yet with Y' is a map, not an insult.",
 ],
 "requirements": [
  "Courage to make the internal external - expression is a voluntary act.",
  "Calibration: honesty about the current evidence level.",
  "A receiver capable of stewardship, or the expression is wasted.",
  "Ongoing tending: expression is a practice, not a one-time announcement.",
 ],
 "standards": [STD["mayer_abi"], STD["gottman_trust"], STD["rempel_pdf"]],
 "citations": [CIT["mayer"], CIT["gottman"], CIT["rempel"]],
 "sig_lens": (
  "The Signature science teaches that a seal unstamped is a covenant unkept: "
  "trust held entirely inside helps no one. The healthy expression is the "
  "striking of the seal in daylight - said plainly, shown in measure, received "
  "as stewardship, and mapped at its edges. The Signature craftsman stamps "
  "boldly but never beyond the metal's proven strength, and signs the edges "
  "of the stamp so all can read exactly where the covenant holds."),
},
{
 "key": "trust-unhealthy-extremes",
 "name": "The Two Unhealthy Extremes: Blind Trust and Chronic Distrust",
 "group": "healthy expression",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Trust has two unhealthy extremes, and both are failures of calibration. "
  "Blind trust extends deep stakes on thin evidence: the new acquaintance "
  "handed the life savings, the charming stranger given the passwords, the "
  "partner never questioned because questioning feels disloyal. It feels like "
  "virtue - openness, generosity, faith in people - but it is the prediction "
  "system abdicating: no ledger, no probes, no audit. The cost arrives as "
  "betrayal, and the cruelest part is that the victim often blames trust "
  "itself rather than the missing calibration, and swings to the other "
  "extreme. Chronic distrust refuses stakes on deep evidence: the loyal "
  "partner of twenty years still monitored, the competent colleague still "
  "double-checked, every neutral act read as threat. It feels like wisdom - "
  "caution, realism, self-protection - but it is the prediction system frozen: "
  "no new evidence admitted, the prior never updated. The cost is quieter but "
  "just as real: relationships starved of the vulnerability they need to "
  "deepen, opportunities declined, a life lived behind glass. Both extremes "
  "share a root: the ledger is not being kept. Blind trust never opens the "
  "books; chronic distrust never reconciles them. Health is the middle path: "
  "stakes sized to evidence, books kept honestly, priors updated continuously."),
 "how_it_works": (
  "Both extremes are prediction-system pathologies. In blind trust, the "
  "evidence channel is disconnected: the prior is set to 'safe' by wish, "
  "charm, or ideology, and disconfirming data is rationalized away - the "
  "system cannot learn because it will not look. Neurologically and "
  "behaviorally this resembles the affection-bribe at maximum volume: feeling "
  "overwhelms bookkeeping entirely. In chronic distrust, the update mechanism "
  "is jammed: the prior is set to 'threat' by old injury, and every new "
  "person inherits the old red ink - the system cannot learn because it will "
  "not credit. Both are stable equilibria, which is why they persist: blind "
  "trust feels good until it crashes, and distrust feels safe because nothing "
  "ventured means nothing lost - except everything trust would have built. "
  "Recovery in both cases means restoring the ledger: blind trust must start "
  "keeping books, chronic distrust must start reconciling them, one small "
  "honest entry at a time."),
 "key_points": [
  "Blind trust: deep stakes on thin evidence - the prediction system abdicating.",
  "Chronic distrust: no stakes on deep evidence - the update mechanism jammed.",
  "Both feel virtuous (openness / caution) while costing enormously.",
  "Shared root: the ledger is not being kept - never opened, or never reconciled.",
  "Health is calibration: stakes sized to evidence, priors updated continuously.",
 ],
 "requirements": [
  "Honest bookkeeping as the non-negotiable foundation.",
  "For blind trust: the discipline to probe before authorizing stakes.",
  "For chronic distrust: the willingness to let new evidence count.",
  "Usually time and often support - extremes are stable and self-protecting.",
 ],
 "standards": [STD["mayer_abi"], STD["kramer"], STD["simpson"]],
 "citations": [CIT["mayer"], CIT["kramer"], CIT["simpson"]],
 "sig_lens": (
  "The Signature science stamps both extremes as counterfeit postures: blind "
  "trust is a seal pressed into air - bold, dramatic, holding nothing; chronic "
  "distrust is a seal never lifted from its box - safe, pristine, and useless. "
  "The Signature press works only on real metal with measured force. The "
  "master's rule: stamp what the evidence supports, no more, no less, and "
  "reconcile the books every evening."),
},
{
 "key": "trust-everyday-practices",
 "name": "Everyday Practices That Keep Trust in Balance",
 "group": "healthy expression",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Trust stays healthy through small, repeatable practices - the hygiene of "
  "the bond. Keep the tiny promises: the call-back when you said you would, "
  "the five-minute task done on time - small seals, stamped daily, carry the "
  "whole covenant. Narrate your reasoning: 'here is why I decided this' "
  "gives the other person's prediction system free, accurate data. Admit the "
  "small failures fast: owning the missed deadline on the day builds more "
  "trust than a perfect record, because it proves the reporting channel is "
  "honest. Ask rather than assume: 'what do you need here?' beats mind-"
  "reading and prevents the resentment of guessed wrong. Do the unprompted "
  "report: a two-line update before being asked dissolves more suspicion than "
  "any reassurance speech. Keep confidences absolutely: what is told in trust "
  "never travels, with no exceptions to memorize. Repair quickly: the "
  "apology-and-fix within the day, not the month - ledgers reconcile best "
  "fresh. And audit yourself monthly: where did I extend trust well, where "
  "did I over- or under-extend, what does the balance actually say? None of "
  "these is heroic. That is the point: trust is a garden, not a monument, and "
  "gardens are kept by daily watering, not by annual ceremonies."),
 "how_it_works": (
  "Practices work by keeping the ledger current and the prediction error "
  "small. Tiny kept promises provide a continuous stream of low-cost positive "
  "evidence - the highest-frequency deposits available, which is why they "
  "outweigh occasional grand gestures. Narrated reasoning and unprompted "
  "reporting reduce the other party's monitoring costs to near zero; trust "
  "deepens fastest when verification becomes unnecessary because information "
  "arrives freely. Fast admission of small failures performs the paradoxical "
  "function of strengthening the honesty channel: each owned mistake is "
  "evidence that the reporting system works, raising confidence in all "
  "subsequent reports. Quick repair prevents the interest on hurt from "
  "compounding - unrepaired ruptures accrue interpretive interest as the "
  "injured party re-reads old events through the new lens. Monthly self-audit "
  "is metacognition applied to the ledger: calibration maintained "
  "deliberately rather than left to drift."),
 "key_points": [
  "Keep tiny promises daily: small seals carry the whole covenant.",
  "Narrate reasoning and report unprompted: free accurate data, zero monitoring cost.",
  "Admit small failures fast: owned mistakes prove the reporting channel is honest.",
  "Keep confidences absolutely; repair within the day; audit yourself monthly.",
  "Trust is a garden kept by daily watering, not a monument raised annually.",
 ],
 "requirements": [
  "Consistency: practices work by repetition, not intensity.",
  "Honesty with oneself during the monthly audit.",
  "A partner or community where the practices are reciprocated.",
  "Patience: the compound interest of small deposits accrues slowly.",
 ],
 "standards": [STD["gottman_trust"], STD["mayer_abi"], STD["rempel_pdf"]],
 "citations": [CIT["gottman"], CIT["mayer"], CIT["rempel"]],
 "sig_lens": (
  "The Signature science calls these practices the daily striking of the seal: "
  "the call-back kept, the reason narrated, the failure owned by sundown, the "
  "confidence guarded absolutely. The master stamper does not wait for the "
  "grand occasion; the covenant is renewed every morning in small things, so "
  "that when the great weight comes, the seal holds without thinking."),
},
# ----------------------------------------------- 29-31: RECOGNIZING TRUST IN OTHERS
{
 "key": "trust-reading-signs",
 "name": "Reading Trust in Others: Face, Body, Voice, and Behavior",
 "group": "recognizing trust",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Reading trust in others means reading the whole ensemble, not one cue. "
  "On the face: the genuine markers - eye-corner crinkles with the smile, "
  "level resting brow, loose jaw, soft direct gaze - versus the managed set "
  "of mouth-only smiles and watchful stillness. On the body: open torso, "
  "uncrossed arms, leaning in, comfortable stillness, the absence of barrier "
  "objects and exit-angling. In the voice: warmth and natural variation, "
  "unhurried pace, volunteered information, easy admission of not-knowing. In "
  "behavior, the strongest channel: unhovered delegation, early confession of "
  "mistakes, defended-when-absent loyalty, confidences shared without "
  "leverage-seeking, consistency across moods and audiences. Weight the "
  "channels correctly: behavior over words, involuntary over voluntary, "
  "patterns over moments. One warm meeting means little; six months of kept "
  "small promises means everything. Watch for congruence: when face, body, "
  "voice, and behavior all tell the same story, believe it; when they "
  "contradict, believe the behavior and investigate the rest. And calibrate "
  "to the person: the quiet one's trust looks like stillness, the expressive "
  "one's like warmth - read the delta from their baseline, never from a "
  "universal template. The goal is not judgment but navigation: reading well "
  "lets you size your own vulnerability wisely."),
 "how_it_works": (
  "Ensemble reading works because deception and self-deception are "
  "channel-limited: people can manage one or two channels at a time, but "
  "sustaining a false broadcast across face, body, voice, and behavior over "
  "months exceeds cognitive capacity. The weighting rule - behavior over "
  "words, involuntary over voluntary - reflects signal honesty: costly, "
  "hard-to-fake channels carry more information. Patterns over moments "
  "reflects the statistics: single observations are noisy, but the ledger of "
  "repeated behavior converges on the truth. Congruence checking exploits the "
  "coordination problem: genuine states produce correlated signals across "
  "channels, while managed states produce the uncorrelated residue of "
  "partial control. Baseline calibration removes individual differences, "
  "isolating the trust delta. Done well, this is not mind-reading but applied "
  "base rates - the same logic the prediction system uses, made deliberate."),
 "key_points": [
  "Read the ensemble: face, body, voice, behavior - never one cue alone.",
  "Weight: behavior over words, involuntary over voluntary, patterns over moments.",
  "Congruence is the test: all channels telling one story means believe it.",
  "Calibrate to the individual's baseline, not a universal template.",
  "The goal is navigation - sizing your own vulnerability wisely - not judgment.",
 ],
 "requirements": [
  "Access to multiple channels over repeated encounters.",
  "Knowledge of the person's baseline expressions and habits.",
  "Understanding of the weighting rules and the congruence test.",
  "Humility: readings are probabilities, and people deserve the benefit of process.",
 ],
 "standards": [STD["ekman_face"], STD["mayer_abi"], STD["simpson"]],
 "citations": [CIT["ekman"], CIT["mayer"], CIT["simpson"]],
 "sig_lens": (
  "The Signature science trains its readers as assayers: the face is weighed, "
  "the body measured, the voice tested, the behavior assayed by fire - and the "
  "verdict comes from the whole assay, never from one scale. The Signature "
  "assayer's oath: read the delta, not the template; weigh the pattern, not "
  "the moment; and never stamp a judgment on a single reading."),
},
{
 "key": "trust-supportive-responses",
 "name": "When Someone Trusts You: Supportive Responses",
 "group": "recognizing trust",
 "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Being trusted is a role, and playing it well is one of the highest uses of "
  "the emotion. First, receive it cleanly: when someone extends trust - the "
  "confession, the delegation, the vulnerability - meet it with steadiness, "
  "not surprise or fanfare. Surprise says 'I did not expect this of you'; "
  "steadiness says 'you are safe here.' Second, handle the entrusted thing as "
  "your own: guard confidences absolutely, execute the delegated task with "
  "care, and report back unprompted - stewardship is the rent on trust. Third, "
  "reciprocate proportionally: meet vulnerability with appropriate openness of "
  "your own, which tells the giver their trust was well placed and invites "
  "the cascade. Fourth, be the safe place for repair: when the trusting "
  "person stumbles - the confession includes a failure, the delegated task "
  "hits trouble - respond to the honesty first and the problem second; people "
  "learn whether honesty is safe from exactly these moments. Fifth, name it "
  "when it matters: 'thank you for trusting me with this' dignifies the gift "
  "and marks the ledger entry explicitly. What you are doing, underneath all "
  "five, is proving the giver's prediction system right - and a prediction "
  "system proven right becomes bolder, kinder, and more open, which is how "
  "one person's good trusteeship upgrades the whole relationship."),
 "how_it_works": (
  "Supportive responses work by confirming the giver's model at the moment of "
  "maximum diagnosticity. The extension of trust is itself a test - often "
  "unconscious - and the receiver's response is weighted heavily because "
  "stakes are high and attention is focused. Steadiness over surprise matters "
  "because surprise signals that the trust was unexpected, which downgrades "
  "the giver's self-model ('maybe I misjudged'); steadiness confirms it. "
  "Stewardship behaviors (guarding, executing, reporting) deposit directly "
  "into the giver's ledger with high weight. Proportional reciprocity triggers "
  "the two-way cascade. Honesty-first responses to stumbles teach the meta-"
  "lesson that determines all future disclosure: whether truth is safe here. "
  "Explicit naming converts implicit common ground into explicit common "
  "ground, coordinating both parties' models of the bond. Each response is a "
  "high-leverage ledger entry because it lands when the system is watching "
  "most closely."),
 "key_points": [
  "Receive with steadiness, not surprise: 'you are safe here,' not 'I did not expect this.'",
  "Stewardship is the rent: guard, execute with care, report unprompted.",
  "Reciprocate proportionally - meet vulnerability with openness to trigger the cascade.",
  "When they stumble, answer the honesty first and the problem second.",
  "Name it: 'thank you for trusting me with this' marks the ledger entry.",
 ],
 "requirements": [
  "Recognizing the moment: trust extended is often quiet and easy to miss.",
  "Actual reliability - responses must be backed by follow-through.",
  "Emotional steadiness under the weight of another's vulnerability.",
  "Proportionality: match the depth of the gift, neither dwarfing nor trivializing it.",
 ],
 "standards": [STD["rempel_pdf"], STD["gottman_trust"], STD["mcallister_ab"]],
 "citations": [CIT["rempel"], CIT["gottman"], CIT["mcallister"]],
 "sig_lens": (
  "The Signature science calls the trusted receiver the keeper of the seal: "
  "when the covenant is placed in your hands, you do not marvel at it - you "
  "guard it, carry it, and return it brighter than it came. The keeper's oath "
  "is fivefold: receive steady, steward faithfully, reciprocate truly, shelter "
  "the stumbler, and name the gift. Keep the seal well, and the giver's "
  "ledger will stamp your name in gold."),
},
{
 "key": "trust-mistakes",
 "name": "What Not to Do: Mistakes That Damage Trust",
 "group": "recognizing trust",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Trust is damaged less by grand betrayals than by a familiar set of "
  "mistakes, most of them committed without malice. The small lie: 'it is "
  "only a white lie' - but the prediction system does not grade lies by size; "
  "it grades them by discovered pattern, and one caught small lie re-prices "
  "every past statement. Inconsistency: warmth on Monday, coldness on "
  "Tuesday, with no explanation - unpredictability taxes the system even when "
  "nothing was intended. The deflection: answering a direct question with "
  "spin, humor, or counterattack - evasion reads as concealment regardless of "
  "motive. Broken small promises: the call-back that never came, the 'I will "
  "try' that meant no - tiny seals broken daily dissolve the covenant faster "
  "than one big breach. Scorekeeping trust: announcing your trust as leverage "
  "('after all I have trusted you with') converts gift into transaction and "
  "poisons the ledger. Testing: manufacturing situations to check the other "
  "person - the loyalty test, the trap question - because discovered tests "
  "prove you never trusted at all. And the meta-mistake: refusing repair - "
  "meeting a rupture with denial or delay, letting interest compound on the "
  "hurt. Each mistake is repairable in isolation; the damage comes from the "
  "pattern. The prevention is equally patterned: tell the small truths, stay "
  "legible across moods, answer straight, keep the tiny seals, give trust as "
  "gift, never test, and repair the same day."),
 "how_it_works": (
  "Each mistake damages trust through a specific ledger mechanism. Small lies "
  "trigger Bayesian re-pricing: if this statement was false, the probability "
  "assigned to all past statements drops - the damage radiates backward in "
  "time. Inconsistency raises the prediction error directly: the system's "
  "model stops converging, vigilance spending rises, and ease drains away. "
  "Deflection is read by the motive-audit as concealment because honest "
  "people with nothing to hide answer straight - the heuristic is crude but "
  "statistically sound. Broken small promises are high-frequency withdrawals; "
  "their damage is arithmetic, not dramatic. Leveraged trust reframes the "
  "relationship from communal to exchange norms, and exchange norms invite "
  "scorekeeping from both sides. Discovered tests are catastrophic because "
  "they reveal the tester's model: 'I predicted you would fail' - the "
  "opposite of trust, proven by the test's existence. Refused repair lets the "
  "injured party's reinterpretation cascade run unopposed, rewriting history "
  "in the worst light."),
 "key_points": [
  "Small lies re-price every past statement - the system grades by pattern, not size.",
  "Unexplained inconsistency taxes the prediction system even without malice.",
  "Deflection reads as concealment; broken tiny promises dissolve by arithmetic.",
  "Never use trust as leverage and never manufacture tests - discovered tests prove distrust.",
  "Refusing repair lets reinterpretation compound; repair the same day.",
 ],
 "requirements": [
  "Honesty about the pattern, not just the incident.",
  "Willingness to hear impact without retreating into intent.",
  "Speed: the repair window is measured in days, not months.",
  "Changed behavior after repair - apologies without change are withdrawals.",
 ],
 "standards": [STD["mayer_abi"], STD["gottman_trust"], STD["kramer"]],
 "citations": [CIT["mayer"], CIT["gottman"], CIT["kramer"]],
 "sig_lens": (
  "The Signature science files these mistakes under seal-breakers, each with "
  "its engraved warning: the small lie that re-prices the archive, the cold "
  "Tuesday that taxes the covenant, the manufactured test that proves its "
  "maker never trusted. The Signature craftsman studies the breakers as "
  "carefully as the strikers, for a seal is only as strong as its maker's "
  "knowledge of how seals fail."),
},
# ---------------------------------- 32-34: RELATED EMOTIONS, MIXES, SIMULATION
{
 "key": "trust-related-emotions",
 "name": "The Neighbors of Trust: Related Emotions and Close Cousins",
 "group": "mixes and simulation",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Trust sits in a crowded neighborhood, and telling the neighbors apart is a "
  "core skill. Confidence is trust's cool cousin: confidence predicts an "
  "outcome ('the bridge will hold'), trust predicts a person's intentions "
  "('they will not drop me') - confidence needs no vulnerability to a will. "
  "Faith is trust extended past evidence: where trust says 'the ledger "
  "supports this,' faith says 'I commit beyond what the ledger shows.' "
  "Loyalty is trust in action over time: the behavioral signature of a deep "
  "balance, less a feeling than a practice. Dependence is the risky neighbor: "
  "needing someone is not the same as trusting them - dependence without "
  "evidence is vulnerability without prediction, which is exposure, not "
  "trust. Naivety (or gullibility) is trust's counterfeit: the same open "
  "posture with the ledger missing - it looks like trust and spends like "
  "trust until the first test. Hope is trust's forward-looking sibling: hope "
  "wants a good outcome, trust predicts a good agent. Distrust is not simply "
  "low trust but a partly separate system: you can trust a surgeon's skill "
  "while distrusting their billing - the dials move independently. Suspicion "
  "is distrust with a detective's energy: active hypothesis-testing for "
  "threat. The map matters because each neighbor asks for different handling: "
  "confidence wants data, faith wants commitment, loyalty wants constancy, "
  "dependence wants care, naivety wants evidence, hope wants patience, "
  "distrust wants specific reassurance, and trust itself wants the steady "
  "accumulation of kept promises."),
 "how_it_works": (
  "The neighbors separate along three axes: the target (person vs. outcome), "
  "the evidence basis (ledger-backed vs. extended past evidence), and the "
  "vulnerability structure (accepted risk vs. mere expectation). Trust occupies "
  "the cell of person-target, ledger-backed, accepted-risk; move one axis and "
  "you land on a neighbor - change the target to outcomes and you get "
  "confidence; drop the evidence requirement and you get faith or naivety "
  "depending on whether the extension is principled or careless; remove the "
  "acceptance of risk and you get mere prediction. Distrust's partial "
  "independence reflects separate neural and cognitive handling of threat "
  "vs. safety - the brain maintains a threat model and a safety model "
  "simultaneously, which is why the surgeon can score high on one and low on "
  "the other. Suspicion adds active inference to distrust: not just a low "
  "safety prior but a process for gathering threat evidence. The practical "
  "upshot: diagnose which neighbor you are dealing with before responding, "
  "because reassurance aimed at the wrong axis misses entirely."),
 "key_points": [
  "Confidence predicts outcomes; trust predicts people's intentions - different targets.",
  "Faith extends past evidence; naivety skips evidence entirely - principled vs. careless.",
  "Dependence without evidence is exposure, not trust.",
  "Distrust is partly independent of trust: the dials move separately.",
  "Map first, respond second: each neighbor wants different handling.",
 ],
 "requirements": [
  "Three-axis thinking: target, evidence basis, vulnerability structure.",
  "Honesty about which neighbor is actually present - mislabeling mistreats.",
  "Accepting that several neighbors can co-occupy one relationship.",
  "Updating the map as evidence accumulates.",
 ],
 "standards": [STD["plutchik_dyad"], STD["mayer_abi"], STD["kramer"]],
 "citations": [CIT["plutchik"], CIT["mayer"], CIT["kramer"]],
 "sig_lens": (
  "The Signature science draws the neighborhood as streets around the central "
  "seal: Confidence Street runs toward outcomes, Faith Lane past the ledger's "
  "edge, Loyalty Row along the practiced path - while Counterfeit Alley, where "
  "naivety is sold as trust, is marked with the warning sign. The Signature "
  "assayer walks every street before stamping an address, for a seal delivered "
  "to the wrong house serves no covenant."),
},
{
 "key": "trust-mixes",
 "name": "Trust in Blends: Four Emotion Mixes",
 "group": "mixes and simulation",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Trust blends with other emotions into compounds with their own character, "
  "and the classic blends are worth knowing by name. Trust plus joy makes "
  "love: the Plutchik primary dyad - safety fused with delight, the warm "
  "core of deep bonds. It feels like home with the lights on: ease, warmth, "
  "generosity, the wish for the other's joy as your own. Its risk is the "
  "gilded seal - affection bribing the ledger. Trust plus fear makes "
  "submission: the other Plutchik primary dyad - safety fused with awe at the "
  "other's power. It feels like reverent reliance: the child to the parent, "
  "the novice to the master, the citizen to the just protector. Healthy when "
  "the power is genuinely benevolent; dangerous when fear does the trusting "
  "and judgment retires. Trust plus surprise makes curiosity: the secondary "
  "dyad - safety fused with the pull of the unknown. It feels like the open "
  "door: 'I trust you, so I dare to look' - the emotional basis of learning "
  "from a teacher and exploring with a companion. Trust plus anticipation "
  "makes fatalism in Plutchik's map - better rendered for this archive as "
  "confident expectation: safety fused with forward lean, the feeling of "
  "'we have got this' before the hard thing begins. Each blend inherits "
  "trust's ledger mechanics - all four are built, broken, and rebuilt the "
  "same way - while the partner emotion supplies the flavor, the energy, and "
  "the characteristic failure mode."),
 "how_it_works": (
  "Blends work by superposition: trust contributes its prediction-system "
  "settings (high safety prior, low monitoring, authorized vulnerability) "
  "while the partner emotion contributes its own action tendencies and "
  "arousal profile. In trust-plus-joy, the low monitoring of trust meets the "
  "approach energy of joy, producing generous, expansive bonding - and the "
  "documented failure mode where positive affect suppresses evidence-"
  "gathering. In trust-plus-fear, trust's vulnerability meets fear's "
  "hierarchy detection, producing deference - adaptive toward genuinely "
  "protective power, maladaptive when the fear signal is doing all the work. "
  "In trust-plus-surprise, trust's safety meets surprise's attention-orienting, "
  "producing the explore drive: safety makes novelty rewarding instead of "
  "threatening. In trust-plus-anticipation, trust's steady prior meets "
  "anticipation's forward modeling, producing committed momentum. The "
  "ledger mechanics transfer intact because all four blends still run on the "
  "same prediction system - only the inputs and the action outputs differ."),
 "key_points": [
  "Trust + joy = love: safety fused with delight; risk is the gilded seal.",
  "Trust + fear = submission: reverent reliance; healthy toward benevolent power, dangerous otherwise.",
  "Trust + surprise = curiosity: safety makes novelty rewarding - the basis of learning.",
  "Trust + anticipation = confident expectation: 'we have got this' before the hard thing.",
  "All blends inherit the ledger: built, broken, and rebuilt the same way.",
 ],
 "requirements": [
  "Genuine trust as the base - blends built on counterfeit trust inherit its fragility.",
  "The partner emotion truly present, not merely labeled.",
  "Awareness of each blend's characteristic failure mode.",
  "Ledger discipline maintained inside the blend's warmth.",
 ],
 "standards": [STD["plutchik_dyad"], STD["mcallister_ab"], STD["rempel_pdf"]],
 "citations": [CIT["plutchik"], CIT["mcallister"], CIT["rempel"]],
 "sig_lens": (
  "The Signature science treats the blends as alloys of the seal-metal: love "
  "is trust alloyed with gold, submission with iron, curiosity with quick-"
  "silver, confident expectation with bright steel. Each alloy has its temper "
  "and its use, and the Signature metallurgist knows them all - but every "
  "alloy is still stamped, tested, and ledgered like the pure metal, for no "
  "alloy is stronger than the trust at its core."),
},
{
 "key": "trust-full-simulation",
 "name": "Trust from First Meeting to Deep Bond: A Full Behavioral Simulation",
 "group": "mixes and simulation",
 "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The archive's showcase simulation walks trust through its whole arc in one "
  "continuous scenario. Scene one, the meeting: Maya joins the workshop team; "
  "Jon, the lead, greets her with the eyebrow flash, open posture, and plain "
  "speech of mild trust extended - 'we will figure it out together.' Her "
  "system registers the classic triggers and extends probe-sized trust back. "
  "Scene two, the first test: Jon promises the client mockup by Thursday and "
  "delivers Wednesday evening with a two-line unprompted update. Small seal, "
  "stamped early - Maya's ledger jumps, and she volunteers the real reason her "
  "last project failed, testing vulnerability met with care. Scene three, the "
  "deepening: over months, kept promises compound; the cascade runs both ways; "
  "their speech drops its hedging, their postures synchronize in meetings, and "
  "delegation grows - Jon hands Maya the flagship account without hovering. "
  "Scene four, the rupture: under deadline pressure Jon snaps at Maya in "
  "front of the team and then deflects when she raises it. The ledger takes "
  "its first real withdrawal; her sleep frays for a week; the reverse cascade "
  "begins retuning her instrument toward caution. Scene five, the repair: Jon "
  "names it plainly the next morning - 'I was wrong, no excuse' - takes the "
  "cost openly, changes the pattern visibly, and keeps every small promise "
  "for a month. Costly honesty, the highest-diagnostic trigger, lands in "
  "full. Scene six, the deep bond: a year later, the flagship launch "
  "threatens to slip; Maya works the weekend without being asked, Jon defends "
  "her approach to the client without checking with her first, and neither "
  "experiences this as risk anymore - the ledger is so deep that monitoring "
  "has retired. The simulation's lesson, stated once: trust is built in "
  "drops, tested in storms, repaired by costly honesty, and at full depth it "
  "stops feeling like trust at all - it feels like the way things are."),
 "how_it_works": (
  "The simulation integrates every mechanism in the archive. Scene one runs "
  "on swift-trust and classic triggers: greeting signals, plain speech, and "
  "the reciprocity reflex firing on first contact. Scene two demonstrates "
  "high-diagnostic evidence: the early small seal plus unprompted reporting, "
  "followed by vulnerability-met-with-care as the bidirectional trigger. Scene "
  "three is the cascade chapter: retuning, reciprocity, and generalization "
  "compounding through the nonlinear region, with speech, posture, and "
  "delegation as the behavioral readouts. Scene four shows the rupture "
  "mechanics: deflection as concealment-read, withdrawal arithmetic, sleep "
  "disruption from the spiked threat budget, and the reverse cascade's "
  "retuning. Scene five is the repair protocol executed correctly: plain "
  "naming, cost openly taken, pattern visibly changed, small seals stamped "
  "daily - costly honesty doing the heavy lifting. Scene six shows the "
  "asymptote: ledger balance dwarfing any single stake, monitoring at zero, "
  "identity merged into 'we.' The arc is the ledger made narrative."),
 "key_points": [
  "Scene 1 (meeting): swift trust, greeting signals, the reciprocity reflex.",
  "Scene 2 (first test): early small seal + unprompted report; vulnerability met with care.",
  "Scene 3 (deepening): the cascade - retuning, reciprocity, generalization compounding.",
  "Scene 4 (rupture): deflection, withdrawal arithmetic, reverse-cascade retuning.",
  "Scene 5 (repair): plain naming, cost taken openly, pattern changed - costly honesty.",
  "Scene 6 (deep bond): monitoring retired; trust stops feeling like trust.",
 ],
 "requirements": [
  "A long-enough timeline for the full arc: months, not moments.",
  "Both parties responsive - the cascade needs two.",
  "A genuine rupture survived, proving the repair mechanics.",
  "Evidence at every stage - the simulation never skips the ledger.",
 ],
 "standards": [STD["gottman_trust"], STD["berg_game"], STD["rempel_pdf"], STD["meyerson_swift"]],
 "citations": [CIT["gottman"], CIT["berg"], CIT["rempel"], CIT["meyerson"]],
 "sig_lens": (
  "The Signature science stages this simulation as the forging of a master "
  "seal: struck at the meeting, deepened blow by blow through the months, "
  "cracked in the rupture, re-forged hotter in the repair, and finally "
  "quenched into the unbreakable seal of the deep bond. The Signature moral "
  "is engraved beneath the showcase: every seal in this archive was earned "
  "exactly this way - in drops, in storms, in costly honesty - and no other "
  "way has ever worked."),
},
]
