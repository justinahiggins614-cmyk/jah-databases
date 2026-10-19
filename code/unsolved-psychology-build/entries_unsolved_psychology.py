#!/usr/bin/env python3
"""Entries for the Unsolved Psychology databases (Manon 2026-10-17 16:15
Unsolved Problems Solved series, batch 1 — Psychology).

Two databases, 34 ladder-ordered records each:

  unsolved-psychology             - The Unsolved Psychology Database
                                    (public-harvest: real, fact-checked
                                    unsolved problems of psychology —
                                    dream function, yawning, laughter,
                                    tears, deja vu, sleep function, the
                                    placebo effect, the nature of emotion,
                                    forgetting, motivation, cognitive
                                    bias persistence, language
                                    acquisition, creativity, linguistic
                                    relativity, stress and trauma, moral
                                    judgment origins, altruism, attention
                                    selection, the binding problem, the
                                    self, decision timing, memory
                                    consolidation, nature and nurture,
                                    the full picture of intelligence,
                                    the Flynn effect, the replication
                                    crisis, the unconscious, the causes
                                    of depression, the causes of
                                    schizophrenia, measuring
                                    consciousness, the hard problem, the
                                    problem of other minds, matter and
                                    experience, the full architecture of
                                    mind; standard references: Freud
                                    1900, James 1890, Ebbinghaus 1885,
                                    Spearman 1904, Maslow 1943, Chomsky
                                    1959, Tversky and Kahneman 1974,
                                    Treisman 1980, Libet 1983, Chalmers
                                    1995, Open Science Collaboration
                                    2015, and the other landmarks cited
                                    per record)
  unsolved-psychology-signature   - The Unsolved Psychology Signature
                                    Database
                                    (his original Signature reading:
                                    every open problem a locked door in
                                    the mind, the Signature method the
                                    key cut from first principles —
                                    each record the same problem seen
                                    through the Signature lens with a
                                    proposed solution approach; src
                                    signature, titles suffixed
                                    " (Signature Edition)", never
                                    presented as authentic public
                                    record)

34 records each, ordered by the teaching ladder (ladder_rank 1-34:
foundations 1-12, compounded 13-24, advanced 25-34); the shard index is
written in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-USPS- (public) and JAH-USPSS- (signature), verified free
2026-10-17 in the manifest id_prefix values and in all 872 shard index
files of jah-databases-data-1 (zero hits for "JAH-USPS-" anywhere; the
USPSS- form adds the series signature S before the trailing dash).

Record schema (per the unsolved series spec):
  id, t, g, name, title, problem, background, why_it_matters,
  signature_solution, src, ladder_rank, ladder_tier, demo

The signature_solution opens with the exact label
"Signature-generated proposed solution — not established science".
The public half carries a short pointer to the signature companion
record; the signature half carries the full treatment. Honesty rule
throughout: no claim of proof, no implied peer acceptance, no
speculation presented as settled. Descriptive and educational only —
no diagnosing of real people, no religious talk.

Numerical cores: demo weights hand-set 2026-10-17 per entry; expected
net scores are machine-computed from those weights and machine-verified
by the demos (see demos_unsolved_psychology.py). Every demo prints its
real computed values, walks five explorer steps with confirm and
refute panels, accepts adjustable assumption weights on the command
line, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before any
files are written.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

LABEL = "Signature-generated proposed solution — not established science"

ENTRIES = [
# ------------------------------------------------------------------ 1-9
{
 "key": "dream-function",
 "name": "Why Do We Dream?",
 "group": "Sleep and Dreams",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": ("Every human dreams, most nights, and nobody knows for certain "
             "why. The unsolved problem is the function of dreaming: is it "
             "memory work, emotional rehearsal, random noise, or something "
             "else entirely?"),
 "background": ("Dreaming has been studied since Freud published The "
                "Interpretation of Dreams in 1900, proposing dreams as "
                "disguised wish fulfillment. In 1953 Aserinsky and Kleitman "
                "discovered REM sleep, tying vivid dreaming to a measurable "
                "brain state. Hobson and McCarley countered Freud in 1977 "
                "with the activation-synthesis hypothesis: dreams are the "
                "forebrain making stories out of random brainstem noise. "
                "Revonsuo later proposed threat simulation, arguing dreams "
                "rehearse survival responses. Modern work links dreaming to "
                "memory consolidation and emotional regulation, and lucid "
                "dreaming research shows dreamers can sometimes steer the "
                "dream. None of these accounts has won; the field still "
                "holds several live rival theories."),
 "why_it_matters": ("A settled answer would reveal what sleep is actually "
                    "for and open new treatments for nightmares, PTSD "
                    "flashbacks, and sleep disorders. It would also settle "
                    "whether the sleeping brain is doing essential "
                    "computation or idling — a question that reaches into "
                    "consciousness itself."),
 "assumptions": [
   "Dream content carries information about waking concerns, not pure noise.",
   "REM physiology constrains which theories can be true.",
   "A function can be inferred from what breaks when dreaming is disrupted."],
 "confirm": [
   ("REM-sleep correlation", "Vivid narrative dreams track REM physiology, matching the rehearsal account.", 0.30),
   ("Threat rehearsal", "Dream content skews toward threats and social conflict, as threat simulation predicts.", 0.25),
   ("Memory linkage", "Learning tasks alter subsequent dream content, tying dreams to consolidation.", 0.20)],
 "refute": [
   ("Non-REM dreaming", "Structured dreams occur outside REM, weakening any REM-only mechanism.", 0.25),
   ("Bizarre content", "Much dream content is surreal and useless for any rehearsal.", 0.20),
   ("No deficit", "People deprived of dreaming show no clean, specific cognitive deficit.", 0.20)],
 "sig_body": (
   "The Signature reading treats the dream as the mind running its simulator off the leash: by day the simulator is clamped to sensory input, by night it free-runs on the day's unresolved material. "
   "Step one, assume the sleeping brain is still a prediction machine, minimizing surprise even with no input. "
   "Step two, the prediction errors of the day — threats noticed, tasks unfinished, emotions unprocessed — become the training set the simulator replays. "
   "Step three, the bizarreness is a feature: the simulator stress-tests predictions against scrambled inputs, the way engineers fuzz-test software. "
   "Step four, memory consolidation is then a side effect of simulator replay, not the purpose. "
   "What would confirm it: Confirm C1 — REM-sleep correlation: vivid narrative dreams track REM physiology, matching the rehearsal account. "
   "Confirm C2 — Threat rehearsal: dream content skews toward threats and social conflict, as threat simulation predicts. "
   "Confirm C3 — Memory linkage: learning tasks alter subsequent dream content, tying dreams to consolidation. "
   "What would refute it: Refute R1 — Non-REM dreaming: structured dreams occur outside REM, weakening any REM-only mechanism. "
   "Refute R2 — Bizarre content: much dream content is surreal and useless for any rehearsal. "
   "Refute R3 — No deficit: people deprived of dreaming show no clean, specific cognitive deficit. "
   "What it does NOT claim: it does not claim dreams predict the future, carry messages, or can be decoded by any fixed symbol dictionary. "
   "Honest status: a proposal only — the function of dreaming remains open in established science."),
},
{
 "key": "yawning-function",
 "name": "Why Do We Yawn?",
 "group": "Sleep and Dreams",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": ("Yawning is one of the most common human behaviors and one of "
             "the least understood. The unsolved problem is what yawning is "
             "for: cooling the brain, raising alertness, signaling state — "
             "or nothing at all?"),
 "background": ("Yawning happens in the womb, across species, and spreads "
                "contagiously between people. Old textbook claims — that "
                "yawning tops up oxygen — were disproven when experiments "
                "showed oxygen and carbon dioxide levels do not trigger it. "
                "Andrew Gallup proposed the brain-cooling hypothesis: the "
                "deep inhale and jaw stretch move warm blood and cool the "
                "brain, with supporting evidence that yawning frequency "
                "tracks ambient temperature. Others link yawning to arousal "
                "shifts and social signaling, since contagious yawning is "
                "stronger among socially bonded individuals. The empathy "
                "link was once popular but later studies weakened it. No "
                "single account explains all the data."),
 "why_it_matters": ("Settling it would clarify a basic brain-regulation "
                    "loop and the biology behind contagious behavior. "
                    "Abnormal yawning patterns also appear in some "
                    "neurological conditions, so a mechanism could become "
                    "a diagnostic clue."),
 "assumptions": [
   "A behavior this conserved across species likely serves a function.",
   "Ambient temperature effects point at a thermoregulatory role.",
   "Contagiousness and physiology may have separate explanations."],
 "confirm": [
   ("Temperature tracking", "Yawning rate follows ambient and brain temperature as the cooling account predicts.", 0.30),
   ("Arousal shifts", "Yawns cluster at wake-sleep transitions, matching an alertness function.", 0.20),
   ("Stretch mechanics", "Jaw stretch and deep inhale measurably move blood and air as cooling requires.", 0.20)],
 "refute": [
   ("No cooling deficit", "Blocking the cooling pathway does not cleanly abolish yawning.", 0.25),
   ("Contagiousness unexplained", "Brain cooling says nothing about why yawns spread person to person.", 0.25),
   ("Empathy link weakened", "Later studies failed to firmly tie contagious yawning to empathy scores.", 0.15)],
 "sig_body": (
   "The Signature reading splits the mystery in two instead of forcing one answer: the yawn and the contagion are different mechanisms wearing the same face. "
   "Step one, treat the solitary yawn as a thermal and arousal reset — a combined stretch, inhale, and circulation pulse that nudges brain temperature and vigilance together. "
   "Step two, treat contagious yawning as a separate social channel: a low-cost synchrony signal that aligns group arousal states, like a flock adjusting formation. "
   "Step three, the reason one behavior shows both patterns is evolutionary thrift — the same motor program got recruited twice. "
   "What would confirm it: Confirm C1 — Temperature tracking: yawning rate follows ambient and brain temperature as the cooling account predicts. "
   "Confirm C2 — Arousal shifts: yawns cluster at wake-sleep transitions, matching an alertness function. "
   "Confirm C3 — Stretch mechanics: jaw stretch and deep inhale measurably move blood and air as cooling requires. "
   "What would refute it: Refute R1 — No cooling deficit: blocking the cooling pathway does not cleanly abolish yawning. "
   "Refute R2 — Contagiousness unexplained: brain cooling says nothing about why yawns spread person to person. "
   "Refute R3 — Empathy link weakened: later studies failed to firmly tie contagious yawning to empathy scores. "
   "What it does NOT claim: it does not claim yawning diagnoses empathy, intelligence, or any condition in any person. "
   "Honest status: a proposal only — yawning's function remains open in established science."),
},
{
 "key": "laughter-mechanism",
 "name": "Why Do We Laugh?",
 "group": "Emotion",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": ("Laughter is universal, appears in infants before speech, and "
             "yet its mechanism is unsolved. The problem: what exactly is "
             "the brain computing when something is funny, and why does "
             "that computation trigger spasmodic vocalization?"),
 "background": ("Three classical theories compete: incongruity (Kant, "
                "Schopenhauer) says laughter resolves violated "
                "expectations; relief theory (Freud, Spencer) says it "
                "vents built-up tension; superiority theory (Hobbes) says "
                "it marks sudden triumph over others. Robert Provine showed "
                "laughter is overwhelmingly social — people laugh far more "
                "with others, and most laughter follows unfunny remarks. "
                "Robin Dunbar linked laughter to social bonding via "
                "endorphins, like primate grooming. Gelotology, the study "
                "of laughter, documents real health correlates but no "
                "agreed causal mechanism. Tickling, humor, and nervous "
                "laughter may not even share one circuit."),
 "why_it_matters": ("Laughter sits at the junction of cognition, emotion, "
                    "and social bonding. A mechanism would illuminate how "
                    "the brain detects surprise and rewards social "
                    "coordination, with applications from therapy to "
                    "human-computer interaction."),
 "assumptions": [
   "Different laugh triggers may share a core surprise-detection circuit.",
   "Social context modulates a physiological, not purely cognitive, event.",
   "The vocal pattern is ancient and conserved, hinting at a deep function."],
 "confirm": [
   ("Incongruity timing", "Brain signals of violated expectation reliably precede laughter onset.", 0.30),
   ("Social amplification", "Group settings multiply laughter, matching the bonding account.", 0.25),
   ("Endorphin release", "Laughter measurably raises pain thresholds via endorphins.", 0.20)],
 "refute": [
   ("Tickling gap", "Ticklish laughter bypasses humor entirely, breaking single-circuit accounts.", 0.25),
   ("Unfunny laughter", "Most real-world laughter follows remarks nobody rates as funny.", 0.20),
   ("Pathological laughter", "Brain lesions can trigger laughter with no humor content at all.", 0.20)],
 "sig_body": (
   "The Signature reading treats laughter as the sound of a prediction error being safely discharged: the brain detects a violated expectation, checks for threat, finds none, and dumps the mobilized energy as rhythmic vocalization. "
   "Step one, every laugh begins with surprise — a model of the world briefly breaks. "
   "Step two, a fast safety check runs: no predator, no social danger, the break is benign. "
   "Step three, the arousal already mobilized for the surprise has nowhere to go, so the ancient vocal circuit vents it in bursts — the ha-ha pattern is the shape of a safe alarm. "
   "Step four, the social contagion layer turns a private discharge into group glue: shared safe-surprise synchronizes the group. "
   "What would confirm it: Confirm C1 — Incongruity timing: brain signals of violated expectation reliably precede laughter onset. "
   "Confirm C2 — Social amplification: group settings multiply laughter, matching the bonding account. "
   "Confirm C3 — Endorphin release: laughter measurably raises pain thresholds via endorphins. "
   "What would refute it: Refute R1 — Tickling gap: ticklish laughter bypasses humor entirely, breaking single-circuit accounts. "
   "Refute R2 — Unfunny laughter: most real-world laughter follows remarks nobody rates as funny. "
   "Refute R3 — Pathological laughter: brain lesions can trigger laughter with no humor content at all. "
   "What it does NOT claim: it does not claim to predict what any individual will find funny, or that laughter therapy cures disease. "
   "Honest status: a proposal only — laughter's mechanism remains open in established science."),
},
{
 "key": "crying-function",
 "name": "Why Do We Cry?",
 "group": "Emotion",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": ("Humans are the only animals that shed emotional tears, and "
             "the function of crying is unsolved. Is it chemical catharsis, "
             "a social signal, self-soothing — or an evolutionary "
             "accident?"),
 "background": ("William Frey proposed in the 1980s that emotional tears "
                "carry stress hormones and proteins out of the body — a "
                "chemical catharsis idea that later work largely failed to "
                "support. Hasson argued tears are a social signal: they "
                "blur vision to signal vulnerability and elicit care. "
                "Research shows criers are rated as warmer but also as "
                "less competent, and observers offer more support to "
                "visible criers. The catharsis belief is widespread yet "
                "studies of mood after crying are mixed — many people feel "
                "worse, not better. Tear composition differs between "
                "irritant and emotional tears, but no agreed function "
                "explains the difference."),
 "why_it_matters": ("Crying is central to grief, empathy, and emotional "
                    "regulation. A real mechanism would reshape therapy "
                    "for grief and depression and clarify how humans "
                    "signal need without words."),
 "assumptions": [
   "A costly, conspicuous signal is unlikely to be functionless.",
   "Social effects of tears are measurable and real.",
   "Self-reported relief may mislead about actual function."],
 "confirm": [
   ("Care elicitation", "Visible tears reliably increase helping behavior in observers.", 0.30),
   ("Vulnerability signal", "Tears blur vision and broadcast helplessness, matching signal theory.", 0.25),
   ("Bonding effects", "Shared crying episodes strengthen reported social bonds.", 0.15)],
 "refute": [
   ("Catharsis unproven", "Controlled studies do not consistently show mood improvement after crying.", 0.30),
   ("Solitary crying", "People often cry alone, where no signal receiver exists.", 0.20),
   ("Chemical claims weak", "Tear-chemistry detox claims failed to replicate convincingly.", 0.20)],
 "sig_body": (
   "The Signature reading treats tears as a two-channel broadcast: one channel aimed outward at the group, one aimed inward at the self. "
   "Step one, the outward channel is honest signaling — tears are hard to fake and visible at distance, so they credibly advertise need and recruit care. "
   "Step two, the inward channel is a physiological gear-shift: the act of crying engages the parasympathetic system, nudging the body from alarm toward recovery. "
   "Step three, the mixed mood data follows: the signal can fail (no one responds, or the context is unsafe), leaving the crier worse — catharsis was never the mechanism, recovery-attempt was. "
   "What would confirm it: Confirm C1 — Care elicitation: visible tears reliably increase helping behavior in observers. "
   "Confirm C2 — Vulnerability signal: tears blur vision and broadcast helplessness, matching signal theory. "
   "Confirm C3 — Bonding effects: shared crying episodes strengthen reported social bonds. "
   "What would refute it: Refute R1 — Catharsis unproven: controlled studies do not consistently show mood improvement after crying. "
   "Refute R2 — Solitary crying: people often cry alone, where no signal receiver exists. "
   "Refute R3 — Chemical claims weak: tear-chemistry detox claims failed to replicate convincingly. "
   "What it does NOT claim: it does not claim crying heals trauma, detoxifies the body, or that anyone should or should not cry. "
   "Honest status: a proposal only — crying's function remains open in established science."),
},
{
 "key": "deja-vu-cause",
 "name": "What Causes Deja Vu?",
 "group": "Memory",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": ("Deja vu — the eerie feeling of having lived a moment before "
             "while knowing you have not — is common and unexplained. The "
             "unsolved problem is what neural event produces a false "
             "feeling of familiarity."),
 "background": ("Alan Brown's 2004 review catalogued decades of speculation "
                "and found the phenomenon oddly under-researched given how "
                "common it is. The leading scientific account is a "
                "familiarity-without-recollection glitch: the rhinal "
                "memory-familiarity system fires while the hippocampal "
                "recollection system finds nothing, and the brain reads "
                "that mismatch as 'I have been here.' Gloor's 1990 work "
                "showed electrical stimulation of rhinal cortex can evoke "
                "deja vu in epilepsy patients. Cleary's experiments found "
                "that unnoticed perceptual overlap with past scenes "
                "increases deja vu reports. Yet none of this explains why "
                "it strikes particular moments, why it fades with age, or "
                "why some people never experience it."),
 "why_it_matters": ("Deja vu is a clean window into how the brain tags "
                    "experience as familiar — the same tagging that fails "
                    "in false memories and some dementias. Understanding "
                    "the glitch would illuminate normal memory monitoring."),
 "assumptions": [
   "Deja vu is a monitoring error, not a memory retrieval.",
   "Familiarity and recollection are separable signals.",
   "Trigger conditions can be studied experimentally."],
 "confirm": [
   ("Rhinal stimulation", "Direct stimulation of familiarity circuitry evokes the exact sensation.", 0.30),
   ("Perceptual overlap", "Hidden similarity to past scenes raises deja vu rates in the lab.", 0.25),
   ("Age curve", "Deja vu peaks in young adulthood when monitoring systems are most active.", 0.15)],
 "refute": [
   ("No recollection", "No actual prior episode is ever recovered, straining memory accounts.", 0.25),
   ("Never-experiencers", "A minority never get deja vu, unexplained by any single mechanism.", 0.20),
   ("Moment selection", "No theory predicts which moments trigger it.", 0.20)],
 "sig_body": (
   "The Signature reading treats deja vu as a timestamp collision in the brain's filing system: two processes stamp the same moment and the discrepancy reads as prior experience. "
   "Step one, perception and familiarity-tagging run on slightly different clocks; normally the tags agree. "
   "Step two, a small delay or double-processing — a scene processed twice in quick succession, or a familiarity signal arriving before its recollection check — stamps the moment twice. "
   "Step three, the conscious mind receives 'familiar' plus 'no source found' and the only coherent story is: this happened before. "
   "Step four, the age curve follows: young adult brains run the fastest, most aggressive tagging, producing the most collisions. "
   "What would confirm it: Confirm C1 — Rhinal stimulation: direct stimulation of familiarity circuitry evokes the exact sensation. "
   "Confirm C2 — Perceptual overlap: hidden similarity to past scenes raises deja vu rates in the lab. "
   "Confirm C3 — Age curve: deja vu peaks in young adulthood when monitoring systems are most active. "
   "What would refute it: Refute R1 — No recollection: no actual prior episode is ever recovered, straining memory accounts. "
   "Refute R2 — Never-experiencers: a minority never get deja vu, unexplained by any single mechanism. "
   "Refute R3 — Moment selection: no theory predicts which moments trigger it. "
   "What it does NOT claim: it does not claim deja vu is precognition, past-life memory, or evidence of anything supernatural. "
   "Honest status: a proposal only — deja vu's cause remains open in established science."),
},
{
 "key": "sleep-function",
 "name": "Why Do We Sleep?",
 "group": "Sleep and Dreams",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": ("Every animal with a nervous system sleeps, and prolonged "
             "wakefulness kills — yet the core function of sleep is still "
             "unsolved. What is sleep actually doing that nothing else "
             "can do?"),
 "background": ("Theories abound: restoration of the body, energy "
                "conservation, memory consolidation, and Tononi and "
                "Cirelli's synaptic homeostasis hypothesis — sleep "
                "downscales synapses strengthened during waking. In 2013 "
                "Nedergaard's team discovered the glymphatic system, which "
                "clears metabolic waste including amyloid from the brain "
                "mainly during sleep. Fatal familial insomnia shows that "
                "total sleep loss is lethal in humans. Yet hibernating "
                "animals still need sleep, migratory birds sleep with half "
                "a brain, and no single theory covers every species' "
                "pattern. The deepest question persists: why must the "
                "brain go offline at all?"),
 "why_it_matters": ("Sleep loss costs lives through accidents and disease. "
                    "A true mechanism would transform treatment of "
                    "insomnia, neurodegeneration, and shift-work damage — "
                    "and answer why consciousness must periodically "
                    "shut down."),
 "assumptions": [
   "Sleep's universality implies a non-negotiable biological function.",
   "Multiple real processes (clearance, consolidation, scaling) occur in sleep.",
   "The offline requirement itself is the deepest part of the mystery."],
 "confirm": [
   ("Waste clearance", "The glymphatic system clears brain metabolites chiefly during sleep.", 0.30),
   ("Lethality", "Total sleep loss is fatal, proving a non-optional function.", 0.25),
   ("Synaptic scaling", "Sleep measurably downscales synaptic strength built up in waking.", 0.20)],
 "refute": [
   ("Hibernation paradox", "Hibernators still need sleep, against simple restoration accounts.", 0.25),
   ("Half-brain sleep", "Some birds and marine mammals sleep with half the brain awake.", 0.20),
   ("No single theory", "No one function explains sleep across all species.", 0.20)],
 "sig_body": (
   "The Signature reading treats sleep as the brain's maintenance window — the one time the system can take itself offline for repairs that cannot run while it is serving traffic. "
   "Step one, waking cognition is expensive: it builds metabolic waste, strengthens synapses indiscriminately, and accumulates prediction errors. "
   "Step two, three maintenance jobs need exclusive access: waste clearance through the glymphatic system, synaptic downscaling to keep the network plastic, and memory triage that decides what survives. "
   "Step three, consciousness is the casualty of maintenance, not its purpose — the lights go out because the crew is rewiring the theater. "
   "Step four, the hibernation paradox resolves: hibernation is low-power idling, not maintenance; the jobs still queue up and still demand their window. "
   "What would confirm it: Confirm C1 — Waste clearance: the glymphatic system clears brain metabolites chiefly during sleep. "
   "Confirm C2 — Lethality: total sleep loss is fatal, proving a non-optional function. "
   "Confirm C3 — Synaptic scaling: sleep measurably downscales synaptic strength built up in waking. "
   "What would refute it: Refute R1 — Hibernation paradox: hibernators still need sleep, against simple restoration accounts. "
   "Refute R2 — Half-brain sleep: some birds and marine mammals sleep with half the brain awake. "
   "Refute R3 — No single theory: no one function explains sleep across all species. "
   "What it does NOT claim: it does not claim any sleep schedule, supplement, or device is optimal, or that less sleep is safe. "
   "Honest status: a proposal only — sleep's core function remains open in established science."),
},
{
 "key": "placebo-mechanism",
 "name": "How Does the Placebo Effect Work?",
 "group": "Mind and Body",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": ("Sugar pills and sham treatments can produce real, "
             "measurable healing — less pain, better movement in "
             "Parkinson's, even objective physiological change. The "
             "unsolved problem is the mechanism: how does belief move "
             "biology?"),
 "background": ("Henry Beecher's 1955 paper 'The Powerful Placebo' claimed "
                "about a third of patients improve on placebo, though "
                "later critics showed he had mixed in natural recovery. "
                "Levine demonstrated in 1978 that placebo pain relief is "
                "blocked by naloxone, implicating the brain's own opioids. "
                "Conditioning matters too: prior drug pairings can train "
                "placebo responses. Kaptchuk's 2010 open-label placebo "
                "trial — patients told the pill was inert still improved — "
                "showed deception is not required. Brain imaging reveals "
                "real dopamine and opioid release during placebo response. "
                "Still unsolved: why it varies wildly between people and "
                "conditions, and how expectation physically rewires "
                "symptom circuits."),
 "why_it_matters": ("Every drug trial must beat placebo, so the mechanism "
                    "is a multi-billion-dollar scientific question. "
                    "Harnessing it ethically could add a real, side-effect-"
                    "free layer to medicine."),
 "assumptions": [
   "Placebo effects are genuine neurobiology, not reporting bias alone.",
   "Expectation and conditioning are distinct, measurable pathways.",
   "Individual variation is data, not noise."],
 "confirm": [
   ("Opioid blockade", "Naloxone blocks placebo analgesia, proving endogenous opioid involvement.", 0.30),
   ("Open-label effect", "Placebos work even when patients know they are placebos.", 0.25),
   ("Dopamine imaging", "Brain scans show real neurotransmitter release during placebo response.", 0.25)],
 "refute": [
   ("Wild variability", "Effect sizes swing enormously across people and conditions.", 0.25),
   ("Natural history", "Much apparent placebo response is just regression to the mean.", 0.25),
   ("Nocebo mirror", "Negative expectation harms, complicating any purely positive mechanism.", 0.15)],
 "sig_body": (
   "The Signature reading treats the placebo response as the brain's pharmacy responding to a work order: expectation is not magic, it is a control signal that releases the body's own compounds. "
   "Step one, the brain maintains an internal dispensary — endogenous opioids, dopamine, cannabinoids — normally released on evidence of healing. "
   "Step two, expectation and conditioned cues can pre-authorize release: the ritual of treatment is the paperwork that opens the dispensary early. "
   "Step three, open-label placebos still work because the ritual and the clinical context, not the deception, file the paperwork. "
   "Step four, variability follows from learning history: a brain with rich conditioning opens the dispensary easily; a naive one does not. "
   "What would confirm it: Confirm C1 — Opioid blockade: naloxone blocks placebo analgesia, proving endogenous opioid involvement. "
   "Confirm C2 — Open-label effect: placebos work even when patients know they are placebos. "
   "Confirm C3 — Dopamine imaging: brain scans show real neurotransmitter release during placebo response. "
   "What would refute it: Refute R1 — Wild variability: effect sizes swing enormously across people and conditions. "
   "Refute R2 — Natural history: much apparent placebo response is just regression to the mean. "
   "Refute R3 — Nocebo mirror: negative expectation harms, complicating any purely positive mechanism. "
   "What it does NOT claim: it does not claim placebos cure disease, replace treatment, or that any condition is 'all in the mind.' "
   "Honest status: a proposal only — the placebo mechanism remains open in established science."),
},
{
 "key": "emotion-nature",
 "name": "What Is an Emotion?",
 "group": "Emotion",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": ("Everyone feels emotions, but psychology cannot agree on what "
             "an emotion is. Are emotions hardwired programs, bodily "
             "perceptions, or concepts the brain constructs? The nature of "
             "emotion is unsolved."),
 "background": ("William James proposed in 1884 that emotion is the "
                "perception of bodily changes — we feel afraid because we "
                "tremble. Cannon and Bard countered that bodily feedback is "
                "too slow and undifferentiated. Schachter and Singer's "
                "1962 two-factor theory split emotion into arousal plus a "
                "cognitive label. Ekman argued for a set of basic, "
                "universal, hardwired emotions with distinct facial "
                "signals. Lisa Feldman Barrett's constructed-emotion "
                "theory (2017) argues the brain builds each emotion from "
                "interoception, past experience, and concepts — there are "
                "no fingerprint patterns for anger or fear. Meta-analyses "
                "of physiology and brain imaging keep failing to find "
                "consistent emotion fingerprints, yet the basic-emotions "
                "view persists."),
 "why_it_matters": ("Emotion theory underlies therapy, affective computing, "
                    "and law. If emotions are constructed rather than "
                    "triggered, everything from lie detection to emotional "
                    "intelligence testing needs rebuilding."),
 "assumptions": [
   "Emotion reports are real data about brain states.",
   "Bodily signals contribute but do not fully determine emotion.",
   "Categories like anger may be concepts, not natural kinds."],
 "confirm": [
   ("No fingerprints", "Large meta-analyses find no consistent bodily signature per emotion.", 0.30),
   ("Label effects", "The words available change what people feel and report.", 0.25),
   ("Prediction success", "Constructionist models predict emotion reports from interoception plus context.", 0.20)],
 "refute": [
   ("Universal faces", "Cross-cultural recognition of core expressions supports hardwired programs.", 0.25),
   ("Infant emotions", "Newborns show organized emotional responses before concepts exist.", 0.20),
   ("Animal affect", "Other mammals show emotion-like states without human concepts.", 0.20)],
 "sig_body": (
   "The Signature reading treats an emotion as a situated prediction: the brain's best current guess about what the body's signals mean, assembled from interoception, context, and learned concepts. "
   "Step one, the body continuously reports its state — heart rate, gut tension, temperature — a noisy interoceptive stream. "
   "Step two, the brain must explain that stream fast, so it reaches for the nearest fitting concept learned across a lifetime: racing heart plus dark alley becomes fear; racing heart plus finish line becomes triumph. "
   "Step three, the felt emotion is the prediction, not the raw signal — which is why the same arousal wears different emotional names in different contexts. "
   "Step four, this explains both camps: the bodily machinery is universal (James was half right) while the categories are constructed (Barrett's half). "
   "What would confirm it: Confirm C1 — No fingerprints: large meta-analyses find no consistent bodily signature per emotion. "
   "Confirm C2 — Label effects: the words available change what people feel and report. "
   "Confirm C3 — Prediction success: constructionist models predict emotion reports from interoception plus context. "
   "What would refute it: Refute R1 — Universal faces: cross-cultural recognition of core expressions supports hardwired programs. "
   "Refute R2 — Infant emotions: newborns show organized emotional responses before concepts exist. "
   "Refute R3 — Animal affect: other mammals show emotion-like states without human concepts. "
   "What it does NOT claim: it does not claim emotions are unreal, voluntary, or that anyone can simply relabel away genuine distress. "
   "Honest status: a proposal only — the nature of emotion remains open in established science."),
},
{
 "key": "forgetting-mechanism",
 "name": "Why Do Memories Fade?",
 "group": "Memory",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": ("Forgetting is as fundamental as remembering, and its "
             "mechanism is unsolved. Do memories decay like fading "
             "photographs, get overwritten by interference, or simply "
             "become unretrievable while intact?"),
 "background": ("Ebbinghaus mapped the forgetting curve in 1885, showing "
                "rapid early loss that levels off. Jenkins and Dallenbach "
                "in 1924 argued interference — new learning disrupting old "
                "— beats simple decay, since sleep (with less interference) "
                "protects memory. Tulving later proposed retrieval failure: "
                "the trace survives but its cues are lost, which is why a "
                "smell can resurrect a 'forgotten' childhood scene. Modern "
                "neuroscience adds active forgetting: the brain deliberately "
                "prunes via mechanisms like dopamine-driven forgetting in "
                "fruit flies. Reconsolidation research shows recalled "
                "memories become fragile again. The field still cannot say "
                "which of these dominates human forgetting, or whether "
                "forgetting is failure or design."),
 "why_it_matters": ("The answer decides whether memory loss in aging and "
                    "dementia is erasure or access failure — with totally "
                    "different treatment paths. It also decides whether "
                    "forgetting is a bug to fix or a feature that keeps "
                    "minds flexible."),
 "assumptions": [
   "Different kinds of forgetting may have different mechanisms.",
   "Retrieval success is not the same as trace survival.",
   "The brain likely forgets on purpose, at least sometimes."],
 "confirm": [
   ("Cue revival", "Lost memories return with the right cue, proving traces can outlive access.", 0.30),
   ("Sleep protection", "Less interference during sleep preserves memory, favoring interference accounts.", 0.25),
   ("Active pruning", "Dedicated molecular pathways actively erase memories in animals.", 0.20)],
 "refute": [
   ("Trace loss", "Some memories never return under any cue, suggesting true erasure.", 0.25),
   ("Decay evidence", "Time alone degrades some memory types even without interference.", 0.20),
   ("Reconsolidation fragility", "Recalled memories can be damaged, blurring storage and retrieval.", 0.15)],
 "sig_body": (
   "The Signature reading treats forgetting as triage, not decay: the brain runs a retention market where memories compete for limited consolidation budget and most are deliberately delisted. "
   "Step one, encoding is cheap and promiscuous — the brain records far more than it can keep. "
   "Step two, a value signal (emotion, repetition, relevance, sleep replay) bids for each trace's survival; low-bid traces are pruned to keep the index fast and the generalizations clean. "
   "Step three, 'lost' memories are usually delisted, not deleted — the trace persists in cold storage but its index entry is dropped, which is why the right cue can still find it. "
   "Step four, true erasure happens too, but it is the exception: interference overwrites and reconsolidation edits are the market's write-offs. "
   "What would confirm it: Confirm C1 — Cue revival: lost memories return with the right cue, proving traces can outlive access. "
   "Confirm C2 — Sleep protection: less interference during sleep preserves memory, favoring interference accounts. "
   "Confirm C3 — Active pruning: dedicated molecular pathways actively erase memories in animals. "
   "What would refute it: Refute R1 — Trace loss: some memories never return under any cue, suggesting true erasure. "
   "Refute R2 — Decay evidence: time alone degrades some memory types even without interference. "
   "Refute R3 — Reconsolidation fragility: recalled memories can be damaged, blurring storage and retrieval. "
   "What it does NOT claim: it does not claim forgotten memories can always be recovered, or that memory training prevents dementia. "
   "Honest status: a proposal only — forgetting's mechanism remains open in established science."),
},
]

ENTRIES += [
# --------------------------------------------------------------- 10-18
{
 "key": "motivation-drivers",
 "name": "What Really Motivates People?",
 "group": "Motivation and Behavior",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": ("Psychology can list motivators but cannot settle what "
             "fundamentally drives human behavior. Is it needs, rewards, "
             "autonomy, meaning — and why do external rewards sometimes "
             "kill the very motivation they were meant to boost?"),
 "background": ("Maslow's 1943 hierarchy of needs ordered motives from "
                "physiological to self-actualization, though evidence for "
                "the strict ordering is weak. Deci and Ryan's "
                "self-determination theory argues autonomy, competence, "
                "and relatedness are the core nutrients of motivation. The "
                "overjustification effect shows paying people for "
                "intrinsically enjoyable tasks can reduce their interest — "
                "rewards backfire. Behavioral economics adds loss aversion "
                "and social comparison. Neuroscience points to dopamine "
                "prediction-error circuits, yet dopamine tracks wanting, "
                "not liking. No unified account predicts when a reward "
                "will motivate, demotivate, or do nothing."),
 "why_it_matters": ("Schools, workplaces, and health programs run on "
                    "motivation theory. A true account would end "
                    "billion-dollar incentive schemes that backfire and "
                    "show how to sustain effort without burning people "
                    "out."),
 "assumptions": [
   "Motivation is multi-system, not a single drive.",
   "Reward effects depend on how the reward is interpreted.",
   "Wanting and liking are separable circuits."],
 "confirm": [
   ("Overjustification", "External rewards measurably reduce intrinsic interest in controlled studies.", 0.30),
   ("Autonomy effects", "Autonomy-supportive contexts raise sustained effort across domains.", 0.25),
   ("Prediction errors", "Dopamine tracks reward prediction error, a computable drive signal.", 0.20)],
 "refute": [
   ("Reward works", "Well-designed incentives reliably raise performance in many settings.", 0.25),
   ("Cultural variance", "What motivates varies sharply across cultures, against universal drives.", 0.20),
   ("Maslow weak", "The famous hierarchy lacks strong empirical support as an ordering.", 0.15)],
 "sig_body": (
   "The Signature reading treats motivation as a control system with three nested loops: a fast loop that chases predicted reward, a middle loop that protects autonomy and competence, and a slow loop that asks whether the game is worth playing. "
   "Step one, the fast loop is pure prediction-error machinery — dopamine marks the gap between expected and received, and behavior climbs the gradient. "
   "Step two, the middle loop monitors the terms of engagement: a reward framed as control (do this, get that) trips an autonomy threat that subtracts more than the reward adds — the overjustification effect falls out naturally. "
   "Step three, the slow loop tracks meaning and identity fit; when it goes negative, no fast-loop reward compensates, which is why well-paid people quit meaningless work. "
   "Step four, interventions work when they feed all three loops at once and backfire when they feed one while starving another. "
   "What would confirm it: Confirm C1 — Overjustification: external rewards measurably reduce intrinsic interest in controlled studies. "
   "Confirm C2 — Autonomy effects: autonomy-supportive contexts raise sustained effort across domains. "
   "Confirm C3 — Prediction errors: dopamine tracks reward prediction error, a computable drive signal. "
   "What would refute it: Refute R1 — Reward works: well-designed incentives reliably raise performance in many settings. "
   "Refute R2 — Cultural variance: what motivates varies sharply across cultures, against universal drives. "
   "Refute R3 — Maslow weak: the famous hierarchy lacks strong empirical support as an ordering. "
   "What it does NOT claim: it does not claim money never motivates, or prescribe any management or parenting method. "
   "Honest status: a proposal only — the drivers of motivation remain open in established science."),
},
{
 "key": "bias-persistence",
 "name": "Why Do Cognitive Biases Persist?",
 "group": "Thinking and Judgment",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": ("Decades of research catalogued our reasoning biases, and "
             "knowing about them barely helps. The unsolved problem: why "
             "do cognitive biases survive awareness, education, and "
             "intelligence itself?"),
 "background": ("Tversky and Kahneman's 1974 heuristics-and-biases program "
                "showed judgment under uncertainty leans on mental "
                "shortcuts that systematically err. Gigerenzer countered "
                "that many 'biases' are ecologically rational — fast "
                "frugal rules tuned to ancestral environments. "
                "Stanovich showed smarter people are not reliably less "
                "biased; some biases grow with cognitive ability. "
                "Debiasing interventions mostly produce small, fleeting "
                "effects. The field cannot agree whether biases are design "
                "flaws, features, or artifacts of artificial lab tasks — "
                "and cannot reliably remove them either way."),
 "why_it_matters": ("Biases shape medicine, law, finance, and democracy. "
                    "If they are irremovable features, institutions must "
                    "be designed around them; if they are fixable bugs, "
                    "training should work. The answer decides the "
                    "strategy."),
 "assumptions": [
   "Biases reflect real computational trade-offs, not mere stupidity.",
   "Lab demonstrations may exaggerate real-world error rates.",
   "Persistence across interventions is itself evidence about architecture."],
 "confirm": [
   ("Smart and biased", "Higher cognitive ability does not reliably reduce bias.", 0.30),
   ("Debiasing fails", "Awareness and training produce only small temporary gains.", 0.25),
   ("Speed-accuracy trade", "Biases buy speed; removing them costs decision time.", 0.20)],
 "refute": [
   ("Ecological rationality", "Many biases vanish when tasks match natural formats.", 0.25),
   ("Expertise reduces", "Domain experts show smaller biases in their own domain.", 0.20),
   ("Incentives help", "Real stakes and accountability measurably shrink some biases.", 0.15)],
 "sig_body": (
   "The Signature reading treats biases as the visible seams of a layered mind: fast ancestral heuristics run underneath, slow deliberation on top, and the seams show whenever the layers disagree about the task. "
   "Step one, the fast layer is a library of gamble-tested shortcuts — good enough for survival decisions under time pressure, wrong in the statistician's seminar room. "
   "Step two, the slow layer knows the right answer in principle but is expensive and lazy; it endorses the fast layer's output unless something flags a conflict. "
   "Step three, intelligence amplifies rather than removes bias because smarter minds are better at rationalizing the fast layer's first draft — motivated reasoning is a feature of a good lawyer-brain, not a defect. "
   "Step four, debiasing fails because it lectures the slow layer while the fast layer keeps answering first. "
   "What would confirm it: Confirm C1 — Smart and biased: higher cognitive ability does not reliably reduce bias. "
   "Confirm C2 — Debiasing fails: awareness and training produce only small temporary gains. "
   "Confirm C3 — Speed-accuracy trade: biases buy speed; removing them costs decision time. "
   "What would refute it: Refute R1 — Ecological rationality: many biases vanish when tasks match natural formats. "
   "Refute R2 — Expertise reduces: domain experts show smaller biases in their own domain. "
   "Refute R3 — Incentives help: real stakes and accountability measurably shrink some biases. "
   "What it does NOT claim: it does not claim reasoning is hopeless, or that any group's judgments are invalid. "
   "Honest status: a proposal only — bias persistence remains open in established science."),
},
{
 "key": "language-acquisition",
 "name": "How Do Children Learn Language?",
 "group": "Language",
 "ladder_rank": 12, "ladder_tier": "foundations",
 "problem": ("Toddlers master the most complex system humans produce with "
             "no instruction, while adults struggle for years. The "
             "unsolved problem is how: built-in grammar, statistical "
             "learning, social imitation — or what combination?"),
 "background": ("Chomsky argued in 1959 that children could not learn "
                "language from the sparse input they hear — the poverty "
                "of the stimulus — so a universal grammar must be innate. "
                "Saffran showed infants are powerful statistical learners, "
                "tracking sound patterns in minutes. Tomasello's "
                "usage-based account stresses social intention-reading: "
                "children learn language as a tool for shared goals. "
                "Lenneberg's critical period hypothesis notes language "
                "learning degrades after puberty, supported by cases of "
                "deprived children. Yet no account fully explains the "
                "speed, the uniformity across cultures, or why machines "
                "with vast data still learn differently than a three-year-"
                "old with a fraction of the input."),
 "why_it_matters": ("The answer reveals the architecture of the human "
                    "mind — how much is prewired versus learned. It "
                    "matters for language disorders, deaf education, and "
                    "building machines that learn like children."),
 "assumptions": [
   "Input alone looks too sparse for pure imitation accounts.",
   "Social interaction is doing real computational work.",
   "The child's brain and the adult's differ in learning machinery."],
 "confirm": [
   ("Statistical power", "Infants extract word boundaries from raw sound statistics in minutes.", 0.25),
   ("Critical period", "Late first-language exposure yields permanently limited grammar.", 0.30),
   ("Social gating", "Language learning collapses without live social interaction.", 0.20)],
 "refute": [
   ("No grammar gene", "No dedicated universal-grammar module has been found in the brain.", 0.25),
   ("Input richer", "Child-directed speech may be richer in structure than early estimates.", 0.15),
   ("Machine counterpoint", "Statistical models learn language from data alone, weakening innateness claims.", 0.20)],
 "sig_body": (
   "The Signature reading treats the child as running three learners in parallel on the same stream: a statistician counting patterns, a mind-reader inferring intentions, and a body mapping sounds to muscles — and language is what falls out of their intersection. "
   "Step one, the statistician segments the sound stream and finds its regularities, exactly as Saffran's infants do. "
   "Step two, the mind-reader anchors those patterns to shared intentions — words are learned as tools for getting joint attention, which is why social isolation breaks learning that tapes and screens cannot fix. "
   "Step three, the body closes the loop: babbling is motor calibration, and production locks in perception. "
   "Step four, the 'poverty of the stimulus' dissolves because the stimulus was never just sound — it was sound plus minds plus bodies in interaction, a far richer dataset. "
   "What would confirm it: Confirm C1 — Statistical power: infants extract word boundaries from raw sound statistics in minutes. "
   "Confirm C2 — Critical period: late first-language exposure yields permanently limited grammar. "
   "Confirm C3 — Social gating: language learning collapses without live social interaction. "
   "What would refute it: Refute R1 — No grammar gene: no dedicated universal-grammar module has been found in the brain. "
   "Refute R2 — Input richer: child-directed speech may be richer in structure than early estimates. "
   "Refute R3 — Machine counterpoint: statistical models learn language from data alone, weakening innateness claims. "
   "What it does NOT claim: it does not claim any parenting method produces smarter children, or that bilingualism confuses children. "
   "Honest status: a proposal only — language acquisition remains open in established science."),
},
{
 "key": "creativity-mechanism",
 "name": "What Is Creativity?",
 "group": "Thinking and Judgment",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": ("Creativity drives science, art, and technology, yet "
             "psychology cannot say what it is mechanically. The unsolved "
             "problem: what does the brain do differently in a creative "
             "moment versus an ordinary one?"),
 "background": ("Guilford distinguished divergent thinking — generating "
                "many solutions — from convergent single-answer thinking, "
                "but divergent tests predict real creative achievement "
                "only weakly. Campbell proposed blind variation and "
                "selective retention: the mind generates variants and "
                "keeps the fit ones. Brain imaging implicates the default "
                "mode network in idea generation and executive networks in "
                "evaluation, with creativity linked to their cooperation. "
                "Csikszentmihalyi's flow research describes the "
                "phenomenology but not the mechanism. Incubation effects — "
                "solutions arriving after rest — are real but poorly "
                "understood. The field still lacks a process model that "
                "predicts when a novel, useful idea will appear."),
 "why_it_matters": ("A mechanism would let education and organizations "
                    "reliably cultivate creativity instead of hoping for "
                    "it, and clarify whether machines can be genuinely "
                    "creative or only combinatorial."),
 "assumptions": [
   "Generation and evaluation are separable phases.",
   "Novelty plus usefulness is the right operational definition.",
   "Brain network cooperation patterns are real clues."],
 "confirm": [
   ("Network cooperation", "Creative performance tracks default-mode plus executive network coupling.", 0.30),
   ("Incubation real", "Breaks measurably improve creative problem solving.", 0.20),
   ("Variation-selection", "Creative output looks like generate-then-prune in process studies.", 0.20)],
 "refute": [
   ("Tests weak", "Divergent-thinking scores predict real achievement only modestly.", 0.25),
   ("No creative spot", "No dedicated creativity center exists in the brain.", 0.20),
   ("Domain specificity", "Creativity in one domain rarely transfers to others.", 0.15)],
 "sig_body": (
   "The Signature reading treats creativity as controlled disinhibition: the brain temporarily loosens the filters that normally keep thought on track, samples widely, then re-applies evaluation to the haul. "
   "Step one, generation is the default mode network free-associating — distant concepts collide because the usual relevance gate is lowered. "
   "Step two, evaluation is the executive network scoring the catch for novelty and usefulness; the creative person is not the one with the wildest generator but the one with the best coupling between generator and judge. "
   "Step three, incubation is the generator running offline while the judge rests — solutions 'arrive' when background sampling crosses a threshold and interrupts. "
   "Step four, domain specificity follows: the generator draws on a stocked pantry, so expertise in the domain is the fuel, not the enemy, of novelty. "
   "What would confirm it: Confirm C1 — Network cooperation: creative performance tracks default-mode plus executive network coupling. "
   "Confirm C2 — Incubation real: breaks measurably improve creative problem solving. "
   "Confirm C3 — Variation-selection: creative output looks like generate-then-prune in process studies. "
   "What would refute it: Refute R1 — Tests weak: divergent-thinking scores predict real achievement only modestly. "
   "Refute R2 — No creative spot: no dedicated creativity center exists in the brain. "
   "Refute R3 — Domain specificity: creativity in one domain rarely transfers to others. "
   "What it does NOT claim: it does not claim creativity can be installed by any technique, or that psychedelics or any substance reliably enhance it. "
   "Honest status: a proposal only — creativity's mechanism remains open in established science."),
},
{
 "key": "linguistic-relativity",
 "name": "Does Language Shape Thought?",
 "group": "Language",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": ("The Sapir-Whorf question will not die: does the language you "
             "speak shape what you can think? After a century of debate, "
             "the scope and reality of linguistic relativity remain "
             "unsolved."),
 "background": ("Whorf claimed Hopi and English speakers inhabit different "
                "thought worlds, though his Hopi data were later "
                "challenged. Berlin and Kay found color naming follows "
                "near-universal stages, a blow to strong relativity. "
                "Boroditsky revived the question with experiments: "
                "grammatical gender nudges object descriptions, and "
                "languages with absolute direction terms produce better "
                "navigators. Critics reply these are thinking-for-speaking "
                "effects — habits of verbalization, not deep cognitive "
                "limits. Bilingual studies show thought patterns shifting "
                "with the active language, but the mechanism and the "
                "boundary between language effects and culture effects "
                "remain contested."),
 "why_it_matters": ("The answer defines the relationship between our "
                    "oldest technology — language — and cognition itself. "
                    "It bears on translation, education, and whether some "
                    "thoughts are truly unthinkable in some tongues."),
 "assumptions": [
   "Language effects, if real, are probabilistic nudges not prison walls.",
   "Habitual verbalization can be separated from underlying competence.",
   "Bilingual minds are natural experiments."],
 "confirm": [
   ("Gender nudges", "Grammatical gender measurably shifts object descriptions.", 0.25),
   ("Direction languages", "Absolute-direction speakers navigate better without instruments.", 0.25),
   ("Bilingual shifts", "Reasoning patterns change with the language in use.", 0.20)],
 "refute": [
   ("Color universals", "Color naming follows universal stages across languages.", 0.25),
   ("Speaking effects", "Many findings vanish when verbalization is blocked.", 0.20),
   ("Culture confound", "Language and culture travel together and are hard to separate.", 0.20)],
 "sig_body": (
   "The Signature reading treats language as a cognitive toolkit that stocks the mind's workbench: it does not build the walls of thought, but it decides which tools are within reach. "
   "Step one, every language lexicalizes some distinctions and not others — having a ready word for a distinction lowers the cost of noticing and using it. "
   "Step two, grammar is a habit engine: obligatory categories like gender or evidentiality force the speaker to track those dimensions constantly, training attention the way a sport trains muscle. "
   "Step three, the effects are therefore real but soft — they show up in speed, likelihood, and default framing, not in hard limits on what can be conceived. "
   "Step four, bilingual shifts follow naturally: switching languages swaps the workbench layout, so different tools come to hand. "
   "What would confirm it: Confirm C1 — Gender nudges: grammatical gender measurably shifts object descriptions. "
   "Confirm C2 — Direction languages: absolute-direction speakers navigate better without instruments. "
   "Confirm C3 — Bilingual shifts: reasoning patterns change with the language in use. "
   "What would refute it: Refute R1 — Color universals: color naming follows universal stages across languages. "
   "Refute R2 — Speaking effects: many findings vanish when verbalization is blocked. "
   "Refute R3 — Culture confound: language and culture travel together and are hard to separate. "
   "What it does NOT claim: it does not claim any language is superior, or that speakers of any language cannot grasp any concept. "
   "Honest status: a proposal only — linguistic relativity remains open in established science."),
},
{
 "key": "stress-trauma-transition",
 "name": "Why Does Stress Sometimes Become Trauma?",
 "group": "Mental Health Science",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": ("Most people survive terrible events without lasting damage; "
             "a minority develop PTSD. The unsolved problem is the "
             "transition: what turns survivable stress into persistent "
             "trauma in one brain and not another?"),
 "background": ("PTSD entered the DSM in 1980 after the Vietnam War forced "
                "psychiatry to face it. Fear conditioning is the core "
                "animal model: a neutral cue paired with shock later "
                "triggers fear alone. Human work implicates an "
                "overreactive amygdala, a smaller or less active "
                "hippocampus, and weakened prefrontal regulation. Yet "
                "most exposed people recover — known risk factors "
                "(prior trauma, low support, dissociation during the "
                "event) predict only modestly. Twin studies suggest "
                "genetic influence on vulnerability. Memory research "
                "shows trauma memories are fragmented and "
                "sensory-heavy. No account yet predicts, for a given "
                "person, whether stress will resolve or crystallize."),
 "why_it_matters": ("An answer would enable prevention — intervening in "
                    "the hours after trauma — instead of treating "
                    "established PTSD. It would also destigmatize the "
                    "disorder by showing it is a learning process, not "
                    "weakness. This record is educational only and does "
                    "not diagnose or advise any person."),
 "assumptions": [
   "Trauma is a memory-formation outcome, not a character outcome.",
   "Timing of intervention matters because consolidation has a window.",
   "Vulnerability is dimensional, not a binary trait."],
 "confirm": [
   ("Fear conditioning", "Trauma responses follow the rules of associative fear learning.", 0.30),
   ("Consolidation window", "Early post-event interventions alter later symptom trajectories.", 0.20),
   ("Circuit pattern", "Amygdala hyperactivity with prefrontal under-regulation marks PTSD.", 0.25)],
 "refute": [
   ("Resilience majority", "Most exposed people recover, against simple conditioning accounts.", 0.25),
   ("Weak prediction", "Known risk factors predict individual outcomes only modestly.", 0.25),
   ("Delayed onset", "Some cases emerge months later, straining event-locked models.", 0.15)],
 "sig_body": (
   "The Signature reading treats trauma as a memory that gets filed wrong: under extreme arousal the brain stamps a sensory fragment as 'happening now' instead of 'happened then,' and every reminder replays it as present danger. "
   "Step one, normal memory files events with time and place tags via the hippocampus; extreme stress hormones disrupt that tagging while supercharging the amygdala's alarm trace. "
   "Step two, the result is a tagless fragment — vivid sensory data with no 'past' marker — so retrieval feels like recurrence. "
   "Step three, avoidance then protects the fragment from the corrective replays that would retag it; the system never gets the update that the danger ended. "
   "Step four, individual differences follow from tagging capacity under load — prior load, sleep, support, and genetics all set how much disruption the filing system can absorb before it misfiles. "
   "What would confirm it: Confirm C1 — Fear conditioning: trauma responses follow the rules of associative fear learning. "
   "Confirm C2 — Consolidation window: early post-event interventions alter later symptom trajectories. "
   "Confirm C3 — Circuit pattern: amygdala hyperactivity with prefrontal under-regulation marks PTSD. "
   "What would refute it: Refute R1 — Resilience majority: most exposed people recover, against simple conditioning accounts. "
   "Refute R2 — Weak prediction: known risk factors predict individual outcomes only modestly. "
   "Refute R3 — Delayed onset: some cases emerge months later, straining event-locked models. "
   "What it does NOT claim: it does not diagnose anyone, prescribe treatment, or imply trauma is a choice or a failure of character. Anyone affected should consult qualified professionals. "
   "Honest status: a proposal only — the stress-to-trauma transition remains open in established science."),
},
{
 "key": "moral-judgment-origins",
 "name": "Where Do Moral Judgments Come From?",
 "group": "Social Mind",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": ("People make instant moral judgments and then invent "
             "reasons for them. The unsolved problem is the source: "
             "are moral judgments reasoned conclusions, gut intuitions "
             "with press-release reasoning, or something else?"),
 "background": ("Kohlberg proposed stages of moral reasoning developing "
                "through childhood, but his stages track Western educated "
                "samples best. Haidt's 2001 social intuitionist model "
                "argued moral judgment is rapid intuition followed by "
                "slow rationalization — reasoning is the press secretary, "
                "not the president. The trolley problem (Foot 1967, "
                "Thomson) shows people distinguish pushing from flipping "
                "a switch while struggling to say why. Greene's fMRI work "
                "found emotional circuits engaged in 'personal' dilemmas "
                "and reasoning circuits in 'impersonal' ones. "
                "Cross-cultural work finds moral foundations vary — care, "
                "fairness, loyalty, authority, purity weighted "
                "differently. The causal arrow between intuition and "
                "reason is still disputed."),
 "why_it_matters": ("Moral psychology underlies law, politics, and AI "
                    "alignment. If judgments are post-hoc rationalizations "
                    "of intuition, persuasion and policy must target the "
                    "intuition, not the argument."),
 "assumptions": [
   "Judgment speed is evidence about process order.",
   "Intuitions are trainable, not fixed.",
   "Cultural variation constrains universalist claims."],
 "confirm": [
   ("Dumbfounding", "People hold judgments they cannot justify when reasons are removed.", 0.30),
   ("Trolley split", "Emotionally personal dilemmas recruit different circuits than impersonal ones.", 0.25),
   ("Speed data", "Moral verdicts arrive faster than any deliberation could produce.", 0.20)],
 "refute": [
   ("Reason shifts", "Deliberation and argument do change moral views over time.", 0.25),
   ("Expert convergence", "Trained ethicists converge more than intuition-only accounts predict.", 0.15),
   ("Cultural learning", "Moral norms are clearly learned, not just triggered.", 0.20)],
 "sig_body": (
   "The Signature reading treats moral judgment as a two-pass compiler: a fast intuition pass emits a verdict from trained pattern-matchers, then a slow reasoning pass generates the justification — and crucially, the second pass can patch the first on the next run. "
   "Step one, intuitions are compressed experience: thousands of social feedback episodes distilled into instant evaluative reflexes. "
   "Step two, reasoning's real job is not just press-release work but debugging — when justifications fail publicly, the embarrassment retrains the intuition, which is why moral dumbfounding stings. "
   "Step three, the trolley split follows: personal dilemmas hit the fast alarm circuits, impersonal ones route to the slow simulator, and the verdict differs because different hardware voted. "
   "Step four, cultural variation is the training set differing — same compiler, different codebases. "
   "What would confirm it: Confirm C1 — Dumbfounding: people hold judgments they cannot justify when reasons are removed. "
   "Confirm C2 — Trolley split: emotionally personal dilemmas recruit different circuits than impersonal ones. "
   "Confirm C3 — Speed data: moral verdicts arrive faster than any deliberation could produce. "
   "What would refute it: Refute R1 — Reason shifts: deliberation and argument do change moral views over time. "
   "Refute R2 — Expert convergence: trained ethicists converge more than intuition-only accounts predict. "
   "Refute R3 — Cultural learning: moral norms are clearly learned, not just triggered. "
   "What it does NOT claim: it does not claim any moral view is correct, or that reasoning about ethics is pointless. "
   "Honest status: a proposal only — the source of moral judgment remains open in established science."),
},
{
 "key": "altruism-origins",
 "name": "Why Are Humans Altruistic?",
 "group": "Social Mind",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": ("Humans routinely help strangers at real cost — donating "
             "blood, jumping into rivers, giving to distant famine "
             "victims. The unsolved problem is why natural selection, "
             "which rewards selfish genes, built a generous ape."),
 "background": ("Hamilton's 1964 kin selection showed helping relatives "
                "spreads shared genes. Trivers (1971) added reciprocal "
                "altruism: help now, get help later — enforced by memory "
                "and reputation. Costly signaling theory says generosity "
                "advertises quality to mates and allies. Batson's "
                "empathy-altruism hypothesis argues empathic concern "
                "produces genuinely selfless motivation. Yet anonymous "
                "one-shot giving in lab games persists beyond what these "
                "accounts cleanly predict, and human cooperation scales to "
                "millions of strangers — far beyond any ancestral band. "
                "The field debates whether true selflessness exists or "
                "every gift hides a payoff."),
 "why_it_matters": ("The answer shapes economics, charity design, and "
                    "whether large-scale cooperation — climate action, "
                    "public health — can be sustained or must be coerced."),
 "assumptions": [
   "Costly helping needs an evolutionary account.",
   "Lab games reveal tendencies but simplify real stakes.",
   "Reputation systems scale cooperation beyond kin."],
 "confirm": [
   ("Kin patterns", "Helping tracks genetic relatedness across species.", 0.25),
   ("Reputation effects", "Observed generosity rises when reputations are at stake.", 0.30),
   ("Punishment sustains", "Costly punishment of free-riders stabilizes cooperation.", 0.20)],
 "refute": [
   ("Anonymous giving", "One-shot anonymous gifts persist beyond payoff accounts.", 0.25),
   ("Scale puzzle", "Cooperation among millions of strangers exceeds ancestral mechanisms.", 0.25),
   ("Empathy evidence", "Empathic concern predicts helping even with no reward possible.", 0.15)],
 "sig_body": (
   "The Signature reading treats altruism as cooperation hardware running on modern software: ancient kin-and-reciprocity circuits got re-targeted by culture onto strangers, and the retargeting mostly works. "
   "Step one, the base layer is Hamilton and Trivers machinery — help kin, trade favors, track cheaters — built for bands of dozens. "
   "Step two, culture installed a patch: moral norms, religions, and institutions tag strangers as honorary in-group members, and the old circuits fire on the new targets. "
   "Step three, reputation is the scaling technology — from village gossip to online ratings, being seen to help pays, so the circuits that evolved for small groups scale to millions. "
   "Step four, the residual anonymous giving is misfire plus empathy overflow: circuits firing on cues (a face, a story) that the ancestral environment always meant 'someone real.' "
   "What would confirm it: Confirm C1 — Kin patterns: helping tracks genetic relatedness across species. "
   "Confirm C2 — Reputation effects: observed generosity rises when reputations are at stake. "
   "Confirm C3 — Punishment sustains: costly punishment of free-riders stabilizes cooperation. "
   "What would refute it: Refute R1 — Anonymous giving: one-shot anonymous gifts persist beyond payoff accounts. "
   "Refute R2 — Scale puzzle: cooperation among millions of strangers exceeds ancestral mechanisms. "
   "Refute R3 — Empathy evidence: empathic concern predicts helping even with no reward possible. "
   "What it does NOT claim: it does not claim generosity is secretly selfish in any individual case, or that people should not give. "
   "Honest status: a proposal only — altruism's origins remain open in established science."),
},
{
 "key": "attention-selection",
 "name": "How Does Attention Select?",
 "group": "Mind and Brain",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": ("The world floods the senses; the mind sips through a "
             "straw. The unsolved problem is the selection mechanism: "
             "how does attention choose one signal from millions, and "
             "what happens to everything it does not choose?"),
 "background": ("Cherry's 1953 cocktail-party experiments showed people "
                "track one voice among many. Broadbent (1958) proposed an "
                "early filter: unattended input is blocked before meaning "
                "is processed. Treisman's attenuation theory softened it: "
                "unattended input is turned down, not off — your name "
                "still breaks through. Posner's spotlight model gave "
                "attention a spatial beam; later work added a zoom lens. "
                "Neuroscience finds attention modulates sensory cortex "
                "like a gain knob, but the controller — what sets the "
                "gain, moment to moment — is unidentified. Inattentional "
                "blindness shows unselected input can vanish entirely "
                "from awareness."),
 "why_it_matters": ("Attention gates learning, memory, and safety — from "
                    "classrooms to cockpits to car dashboards. A real "
                    "mechanism would let us design for the brain's "
                    "bottleneck instead of against it."),
 "assumptions": [
   "Selection is a limited resource with a controller.",
   "Unattended processing continues below awareness.",
   "Gain modulation in sensory cortex is a real mechanism."],
 "confirm": [
   ("Gain modulation", "Attention measurably turns up sensory cortex responses.", 0.30),
   ("Cocktail party", "One stream is tracked while others are suppressed.", 0.25),
   ("Breakthrough effects", "Salient unattended items still capture attention.", 0.20)],
 "refute": [
   ("No controller", "No single brain area commands the gain settings.", 0.25),
   ("Blindness puzzle", "Unattended input can vanish completely, against attenuation.", 0.20),
   ("Split limits", "Divided attention costs resist simple spotlight models.", 0.15)],
 "sig_body": (
   "The Signature reading treats attention as a bidding market for a single broadcast channel: sensory processors bid for access to the global workspace, and the winner gets amplified while losers are suppressed. "
   "Step one, every processor continuously computes a salience bid — bottom-up novelty plus top-down relevance — in parallel and unconsciously. "
   "Step two, a winner-take-all circuit (likely involving the pulvinar and parietal cortex) awards the channel to the highest bidder and applies gain to its signal. "
   "Step three, the 'controller' is not a homunculus but the bid-weighting policy itself, set by goals, habits, and recent rewards — which is why your name outbids a stranger's sentence. "
   "Step four, inattentional blindness is the market working as designed: the gorilla's bid simply lost, so it never reached the broadcast. "
   "What would confirm it: Confirm C1 — Gain modulation: attention measurably turns up sensory cortex responses. "
   "Confirm C2 — Cocktail party: one stream is tracked while others are suppressed. "
   "Confirm C3 — Breakthrough effects: salient unattended items still capture attention. "
   "What would refute it: Refute R1 — No controller: no single brain area commands the gain settings. "
   "Refute R2 — Blindness puzzle: unattended input can vanish completely, against attenuation. "
   "Refute R3 — Split limits: divided attention costs resist simple spotlight models. "
   "What it does NOT claim: it does not claim attention can be infinitely expanded by training, or diagnose attention disorders. "
   "Honest status: a proposal only — attention's selection mechanism remains open in established science."),
},
]

ENTRIES += [
# --------------------------------------------------------------- 19-27
{
 "key": "binding-problem",
 "name": "The Binding Problem",
 "group": "Mind and Brain",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": ("Vision splits the world into color, shape, motion, and "
             "location processed in separate brain areas — yet you see "
             "one unified red ball rolling. The unsolved problem is "
             "binding: how does the brain reassemble the fragments into "
             "a single coherent object?"),
 "background": ("Treisman's 1980 feature integration theory proposed "
                "attention as the glue: focused attention binds features "
                "at a location, and without it illusory conjunctions "
                "occur — people miscombine colors and shapes. Singer and "
                "Gray proposed temporal binding: neurons for one object "
                "fire in synchrony, tagging themselves as a group. "
                "Decades of hunting for the synchrony code found "
                "correlations but no proof it causes binding. "
                "Alternative accounts invoke recurrent feedback loops or "
                "deny the problem — arguing there is no inner screen "
                "needing assembly. Meanwhile binding failures appear in "
                "schizophrenia, autism, and Balint's syndrome, showing "
                "the glue is real and breakable."),
 "why_it_matters": ("Binding is the construction of perceived reality "
                    "itself. Solving it would explain how a unified "
                    "conscious scene arises from distributed processing — "
                    "the central trick of the brain."),
 "assumptions": [
   "Features are processed in anatomically separate areas.",
   "Binding failures in disorders prove a real mechanism exists.",
   "Timing information is available to neural circuits."],
 "confirm": [
   ("Illusory conjunctions", "Divided attention produces feature misbinding, implicating attention as glue.", 0.30),
   ("Synchrony correlates", "Neurons for one object show correlated firing in many studies.", 0.20),
   ("Disorder evidence", "Binding breaks down in specific neurological conditions.", 0.25)],
 "refute": [
   ("No causal proof", "Synchrony correlates with binding but causation is unproven.", 0.25),
   ("Feedback alternative", "Recurrent loops could bind without any synchrony code.", 0.20),
   ("Problem denied", "Some argue there is no assembly needing explanation.", 0.15)],
 "sig_body": (
   "The Signature reading treats binding as address-by-time: the brain tags 'these features belong together' not with a place but with a shared rhythm, and attention is the conductor that hands out the rhythms. "
   "Step one, separate feature maps each propose candidates — red here, round there, moving left. "
   "Step two, the attentional conductor assigns one temporal slot (a gamma-cycle phase) per object; all features of that object fire in that slot. "
   "Step three, downstream areas read coincidence as co-membership — 'fired together in slot 3' means 'same object' — no inner screen required, just a time-division protocol. "
   "Step four, illusory conjunctions are slot collisions under divided attention: the conductor double-books, and features get misfiled. "
   "What would confirm it: Confirm C1 — Illusory conjunctions: divided attention produces feature misbinding, implicating attention as glue. "
   "Confirm C2 — Synchrony correlates: neurons for one object show correlated firing in many studies. "
   "Confirm C3 — Disorder evidence: binding breaks down in specific neurological conditions. "
   "What would refute it: Refute R1 — No causal proof: synchrony correlates with binding but causation is unproven. "
   "Refute R2 — Feedback alternative: recurrent loops could bind without any synchrony code. "
   "Refute R3 — Problem denied: some argue there is no assembly needing explanation. "
   "What it does NOT claim: it does not claim the synchrony code is proven, or that timing is the only binding mechanism. "
   "Honest status: a proposal only — the binding problem remains open in established science."),
},
{
 "key": "self-nature",
 "name": "What Is the Self?",
 "group": "Self and Identity",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": ("You feel like a continuous 'I' persisting through time, "
             "yet psychology and neuroscience keep failing to find it. "
             "The unsolved problem is what the self is: a thing, a "
             "process, a story — or an illusion?"),
 "background": ("William James split the self into the 'I' (the knower) "
                "and the 'Me' (the known) in 1890. Split-brain research "
                "by Sperry and Gazzaniga showed the two hemispheres can "
                "hold separate awarenesses, with the left hemisphere "
                "inventing explanations for actions it did not choose. "
                "Gallagher distinguishes the minimal self — the bare "
                "sense of ownership and agency — from the narrative self, "
                "the life story. The default mode network lights up for "
                "self-referential thought, but damage and meditation can "
                "dissolve the sense of self while cognition continues. "
                "Buddhist psychology and modern neuroscience converge on "
                "the no-self finding, yet the feeling of being someone "
                "persists every waking moment."),
 "why_it_matters": ("The self anchors responsibility, identity, and "
                    "mental health — disorders from depersonalization to "
                    "narcissism are disorders of selfhood. A real account "
                    "would reshape therapy, law, and our understanding of "
                    "what a person is."),
 "assumptions": [
   "The feeling of self is data needing explanation.",
   "Dissociation and split-brain cases reveal architecture.",
   "Ownership and agency are separable components."],
 "confirm": [
   ("Split-brain duality", "Severed hemispheres show separable awareness streams.", 0.25),
   ("Self dissolution", "Meditation and lesions can dissolve selfhood while cognition continues.", 0.30),
   ("Interpreter confabulation", "The left hemisphere invents explanations for actions it did not initiate.", 0.20)],
 "refute": [
   ("Persistence feeling", "The sense of continuity resists all debunking in daily life.", 0.20),
   ("Infant self", "Self-recognition emerges early and universally.", 0.20),
   ("Agency reality", "Voluntary action control is measurably real, not illusory.", 0.20)],
 "sig_body": (
   "The Signature reading treats the self as a control interface, not an entity: the brain builds a simplified user-avatar of the organism so that planning, social prediction, and error-correction have something to point at. "
   "Step one, the minimal self is the avatar's live dashboard — ownership tags ('my hand') and agency tags ('I moved it') computed from sensorimotor prediction matches. "
   "Step two, the narrative self is the avatar's log file — a compressed, edited story that lets the system predict its own future behavior and explain its past. "
   "Step three, the 'I' that feels irreducible is what it is like to be the interface from the inside; there is no little person behind the dashboard, just as there is no little person behind a car's instrument panel. "
   "Step four, split brains run two dashboards, meditation dims the dashboard's brightness, and depersonalization is a dashboard fault — all consistent with interface, not entity. "
   "What would confirm it: Confirm C1 — Split-brain duality: severed hemispheres show separable awareness streams. "
   "Confirm C2 — Self dissolution: meditation and lesions can dissolve selfhood while cognition continues. "
   "Confirm C3 — Interpreter confabulation: the left hemisphere invents explanations for actions it did not initiate. "
   "What would refute it: Refute R1 — Persistence feeling: the sense of continuity resists all debunking in daily life. "
   "Refute R2 — Infant self: self-recognition emerges early and universally. "
   "Refute R3 — Agency reality: voluntary action control is measurably real, not illusory. "
   "What it does NOT claim: it does not claim you do not exist, that responsibility is meaningless, or that any person's identity is invalid. "
   "Honest status: a proposal only — the nature of the self remains open in established science."),
},
{
 "key": "decision-timing",
 "name": "Do Our Brains Decide Before We Do?",
 "group": "Free Will and Choice",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": ("Libet's experiments found brain activity predicting a "
             "'free' choice seconds before subjects felt they decided. "
             "The unsolved problem is what this means: does the brain "
             "decide before the mind, and is conscious will real or a "
             "story told afterward?"),
 "background": ("In 1983 Libet reported the readiness potential — brain "
                "activity ramping up about half a second before subjects "
                "reported deciding to move. Soon and colleagues (2008) "
                "pushed prediction to seconds ahead using fMRI patterns. "
                "Wegner argued conscious will is an illusion: the mind "
                "infers authorship from timing, like inferring one "
                "billiard ball caused another's motion. Critics note the "
                "tasks are trivial finger-movements, the readiness "
                "potential may reflect general preparation not decision, "
                "and subjects retain a 'free won't' — the power to veto. "
                "Philosophers split between compatibilists, who redefine "
                "freedom, and those who say the experiments miss the "
                "real phenomenon of deliberation entirely."),
 "why_it_matters": ("Free will grounds moral responsibility, law, and "
                    "human dignity. If conscious choice is epiphenomenal, "
                    "retribution-based justice and the very idea of "
                    "'deciding' need rethinking."),
 "assumptions": [
   "Brain activity preceding reported decision is a real finding.",
   "Trivial lab choices may not generalize to deliberation.",
   "Veto power is itself a decision needing explanation."],
 "confirm": [
   ("Readiness potential", "Brain activity ramps before reported decision time.", 0.30),
   ("fMRI prediction", "Choice patterns are decodable seconds before awareness.", 0.25),
   ("Authorship illusions", "People claim authorship of actions they did not cause.", 0.20)],
 "refute": [
   ("Trivial tasks", "Findings come from meaningless finger movements, not real decisions.", 0.25),
   ("Preparation not choice", "Early activity may be general readiness, not the decision itself.", 0.25),
   ("Free wont", "Subjects can veto the prepared action, preserving a role for will.", 0.15)],
 "sig_body": (
   "The Signature reading treats the will as a layered system where 'deciding' happens at multiple depths, and the feeling of deciding marks only the top layer's endorsement. "
   "Step one, lower layers continuously prepare candidate actions and their predicted outcomes — the readiness potential is this preparation, not a secret dictator. "
   "Step two, the conscious layer's job is veto and selection among prepared options, operating on a slower clock; its 'decision moment' is when it signs off, which naturally lags preparation. "
   "Step three, the fMRI predictions work because preparation leaks information about which option the lower layers favor — predicting the favorite is not the same as bypassing the chooser. "
   "Step four, deliberation about important choices engages the top layer for extended cycles, which is why finger-twitch studies generalize poorly to life decisions. "
   "What would confirm it: Confirm C1 — Readiness potential: brain activity ramps before reported decision time. "
   "Confirm C2 — fMRI prediction: choice patterns are decodable seconds before awareness. "
   "Confirm C3 — Authorship illusions: people claim authorship of actions they did not cause. "
   "What would refute it: Refute R1 — Trivial tasks: findings come from meaningless finger movements, not real decisions. "
   "Refute R2 — Preparation not choice: early activity may be general readiness, not the decision itself. "
   "Refute R3 — Free wont: subjects can veto the prepared action, preserving a role for will. "
   "What it does NOT claim: it does not claim free will is proven or disproven, or that anyone is not responsible for their actions. "
   "Honest status: a proposal only — the timing of decision remains open in established science."),
},
{
 "key": "memory-consolidation",
 "name": "How Is Long-Term Memory Formed?",
 "group": "Memory",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": ("A moment becomes a memory that lasts decades, but the "
             "transformation is unsolved. How does the brain convert "
             "fragile new experience into durable long-term memory — "
             "and why does it take sleep, time, and the hippocampus?"),
 "background": ("Muller and Pilzecker coined 'consolidation' in 1900. "
                "Patient H.M., studied by Scoville and Milner from 1957, "
                "lost the ability to form new long-term memories after "
                "hippocampal removal while old memories survived — "
                "pinpointing the hippocampus as the converter. Bliss and "
                "Lomo discovered long-term potentiation in 1973, the "
                "synaptic strengthening believed to encode traces. The "
                "standard model says memories transfer from hippocampus "
                "to cortex over weeks; newer work shows the cortex learns "
                "alongside from the start. Sleep replay — the hippocampus "
                "replaying the day's patterns — is observed but its causal "
                "role is still debated. Reconsolidation findings show even "
                "'finished' memories destabilize on recall."),
 "why_it_matters": ("Consolidation is the gateway to lasting knowledge — "
                    "education, skill, identity. Cracking it would open "
                    "treatments for amnesia, PTSD, and age-related memory "
                    "loss, and settle how experiences become a self."),
 "assumptions": [
   "H.M. and LTP findings constrain any true account.",
   "Systems consolidation takes time for a reason.",
   "Sleep replay is doing work, not just correlating."],
 "confirm": [
   ("H.M. lesion", "Hippocampal loss blocks new long-term memory formation.", 0.30),
   ("LTP mechanism", "Synaptic strengthening provides a plausible storage substrate.", 0.25),
   ("Sleep replay", "The hippocampus replays waking patterns during sleep.", 0.20)],
 "refute": [
   ("Cortex early", "Cortical traces form alongside hippocampal ones, against slow transfer.", 0.20),
   ("Reconsolidation", "Recalled memories destabilize, against finished-storage models.", 0.20),
   ("Replay causality", "Disrupting replay impairs memory inconsistently.", 0.20)],
 "sig_body": (
   "The Signature reading treats consolidation as a two-copy backup protocol: the hippocampus is fast, fragile RAM and the cortex is slow, durable disk, and sleep is the nightly backup job. "
   "Step one, waking experience writes first to hippocampal RAM — quick to store, quick to fade, indexed for immediate use. "
   "Step two, during sleep the hippocampus replays the day's index entries to the cortex, which trains slowly over many replays — this is why consolidation takes weeks and why sleep loss corrupts the backup. "
   "Step three, the cortex does not wait passively; it pre-builds schemas (frameworks of prior knowledge) that catch compatible new entries fast, explaining rapid learning when something 'fits.' "
   "Step four, reconsolidation is the protocol's edit function: recalling a memory checks it out of the archive, and it must be re-saved — which is also why it can be updated or corrupted on recall. "
   "What would confirm it: Confirm C1 — H.M. lesion: hippocampal loss blocks new long-term memory formation. "
   "Confirm C2 — LTP mechanism: synaptic strengthening provides a plausible storage substrate. "
   "Confirm C3 — Sleep replay: the hippocampus replays waking patterns during sleep. "
   "What would refute it: Refute R1 — Cortex early: cortical traces form alongside hippocampal ones, against slow transfer. "
   "Refute R2 — Reconsolidation: recalled memories destabilize, against finished-storage models. "
   "Refute R3 — Replay causality: disrupting replay impairs memory inconsistently. "
   "What it does NOT claim: it does not claim memories can be downloaded, transferred, or perfectly preserved by any technique. "
   "Honest status: a proposal only — consolidation's mechanism remains open in established science."),
},
{
 "key": "nature-nurture-personality",
 "name": "Nature vs Nurture: What Shapes Personality?",
 "group": "Development",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": ("Twin studies say genes explain about half of personality — "
             "but which genes, and what explains the rest? The unsolved "
             "problem is the partition: how nature and nurture actually "
             "divide the work of building a person."),
 "background": ("Bouchard's Minnesota twin studies found identical twins "
                "raised apart strikingly similar, estimating Big Five "
                "heritability around 40 to 60 percent. Yet genome-wide "
                "studies find individual gene variants with tiny effects "
                "— the 'missing heritability' gap. Stranger still, the "
                "shared family environment — parenting style, home, "
                "neighborhood — shows near-zero effect on adult "
                "personality in behavioral genetics. The non-shared "
                "environment (unique experiences, peers, chance) carries "
                "the rest but resists specification. Epigenetics and "
                "gene-environment interplay promise answers but have "
                "delivered few firm ones. The partition everyone quotes "
                "rests on statistical models whose assumptions are "
                "increasingly questioned."),
 "why_it_matters": ("The partition decides what parenting, schooling, "
                    "and policy can actually change. If shared "
                    "environment barely matters and genes are diffuse, "
                    "interventions must target the unique experiences "
                    "that actually move the needle."),
 "assumptions": [
   "Heritability estimates are population statistics, not individual recipes.",
   "The near-zero shared-environment finding is real and needs explaining.",
   "Gene-environment correlation confounds simple partitions."],
 "confirm": [
   ("Twin similarity", "Identical twins raised apart show substantial personality similarity.", 0.30),
   ("Shared environment zero", "Adoption studies find little lasting shared-family effect.", 0.25),
   ("Polygenic signal", "Thousands of tiny genetic variants collectively predict traits.", 0.20)],
 "refute": [
   ("Missing heritability", "Found genes explain far less than twin studies imply.", 0.25),
   ("Assumption critiques", "Twin-study assumptions (equal environments) are disputed.", 0.20),
   ("Non-shared mystery", "The supposed big environmental share cannot be pinned down.", 0.20)],
 "sig_body": (
   "The Signature reading treats personality as a developmental cascade where genes set reaction ranges and unrepeatable micro-experiences pick the point in the range — and 'nurture' was always the wrong word for the second part. "
   "Step one, genes do not code for traits; they code for response curves — how strongly a nervous system reacts to novelty, threat, reward — which is why heritability is real but no 'personality genes' exist. "
   "Step two, the shared family environment washes out because siblings inhabit different micro-worlds: different peers, different birth-order niches, different random events — the 'non-shared environment' is mostly chance plus peer culture, not parenting. "
   "Step three, development amplifies small differences: a slightly bolder child elicits bolder responses, which trains bolder habits — gene-environment correlation doing the heavy lifting the partition misattributes. "
   "Step four, missing heritability is then expected: thousands of variants shape reaction curves, and their effects only appear through lived cascades no genome scan can see. "
   "What would confirm it: Confirm C1 — Twin similarity: identical twins raised apart show substantial personality similarity. "
   "Confirm C2 — Shared environment zero: adoption studies find little lasting shared-family effect. "
   "Confirm C3 — Polygenic signal: thousands of tiny genetic variants collectively predict traits. "
   "What would refute it: Refute R1 — Missing heritability: found genes explain far less than twin studies imply. "
   "Refute R2 — Assumption critiques: twin-study assumptions (equal environments) are disputed. "
   "Refute R3 — Non-shared mystery: the supposed big environmental share cannot be pinned down. "
   "What it does NOT claim: it does not claim parenting is irrelevant, that traits are fixed, or predict any individual's personality from genes. "
   "Honest status: a proposal only — the nature-nurture partition remains open in established science."),
},
{
 "key": "intelligence-full-picture",
 "name": "What Is Intelligence, in Full?",
 "group": "Intelligence",
 "ladder_rank": 24, "ladder_tier": "compounded",
 "problem": ("IQ tests predict life outcomes yet nobody agrees what they "
             "measure. The unsolved problem is the full picture of "
             "intelligence: one general factor, many independent "
             "abilities, or something the tests miss entirely?"),
 "background": ("Spearman discovered in 1904 that all cognitive tests "
                "correlate — the positive manifold — and proposed g, "
                "general intelligence. Thurstone countered with primary "
                "mental abilities. Gardner (1983) proposed multiple "
                "intelligences including musical and interpersonal; "
                "Sternberg added practical and creative. The CHC model "
                "now dominates psychometrics with stratified abilities "
                "under a general factor. IQ predicts school, work, and "
                "health outcomes, yet critics note it misses creativity, "
                "wisdom, and social skill. The Flynn effect — rising "
                "scores — shows whatever IQ measures is environmentally "
                "movable. Neuroscience hunts g in brain networks with "
                "only partial success."),
 "why_it_matters": ("Intelligence tests gate education, hiring, and "
                    "immigration worldwide. A full picture would make "
                    "assessment fairer and reveal which abilities are "
                    "trainable versus fixed."),
 "assumptions": [
   "The positive manifold is a real phenomenon needing explanation.",
   "Tests measure developed abilities, not raw potential.",
   "Multiple theories can each capture part of the truth."],
 "confirm": [
   ("Positive manifold", "All cognitive tests intercorrelate, implying a common factor.", 0.30),
   ("Predictive power", "IQ scores predict real-world outcomes across domains.", 0.25),
   ("CHC synthesis", "The stratified model organizes a century of findings coherently.", 0.20)],
 "refute": [
   ("Misses creativity", "Tests barely capture creative or practical achievement.", 0.20),
   ("Flynn mobility", "Rapid score rises undermine fixed-capacity readings.", 0.20),
   ("Cultural loading", "Test content favors specific cultural backgrounds.", 0.20)],
 "sig_body": (
   "The Signature reading treats intelligence as the efficiency of a prediction engine running on good models: g is real, but it is a system property — processing speed times model quality times working-memory bandwidth — not a single thing in the head. "
   "Step one, the positive manifold falls out naturally: a faster, better-supplied engine does better on every task that needs prediction, which is nearly every cognitive test. "
   "Step two, the 'multiple intelligences' are domain model-libraries — music, people, space — built by the same engine on different training data; Gardner catalogued libraries, Spearman measured the engine. "
   "Step three, creativity and wisdom sit partly outside IQ because tests sample the engine under time pressure on abstract models, missing slow model-building and value judgment. "
   "Step four, the Flynn effect is the engine getting better fuel — nutrition, schooling, cognitive complexity of environments — which raises measured output without changing the architecture. "
   "What would confirm it: Confirm C1 — Positive manifold: all cognitive tests intercorrelate, implying a common factor. "
   "Confirm C2 — Predictive power: IQ scores predict real-world outcomes across domains. "
   "Confirm C3 — CHC synthesis: the stratified model organizes a century of findings coherently. "
   "What would refute it: Refute R1 — Misses creativity: tests barely capture creative or practical achievement. "
   "Refute R2 — Flynn mobility: rapid score rises undermine fixed-capacity readings. "
   "Refute R3 — Cultural loading: test content favors specific cultural backgrounds. "
   "What it does NOT claim: it does not claim any person's worth or potential from a test score, or that intelligence is fixed. "
   "Honest status: a proposal only — intelligence's full picture remains open in established science."),
},
{
 "key": "flynn-effect",
 "name": "The Flynn Effect: Why Do IQ Scores Keep Rising?",
 "group": "Intelligence",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": ("IQ scores rose about three points per decade across the "
             "20th century — too fast for genes. The unsolved problem is "
             "the cause of the Flynn effect, and why it is now stalling "
             "or reversing in some countries."),
 "background": ("James Flynn documented the rise in the 1980s: massive, "
                "worldwide, concentrated in fluid reasoning rather than "
                "crystallized knowledge. Proposed causes include better "
                "nutrition, more schooling, smaller families, the "
                "cognitive demands of modern life — even video games. "
                "Dickens and Flynn modeled a social multiplier: small "
                "individual gains cascade through increasingly demanding "
                "environments. Then came the twist: since the 1990s, "
                "several Scandinavian countries show the effect stalling "
                "or reversing, with proposed explanations from "
                "immigration patterns to schooling changes to "
                "dysgenic fertility — all contested. No single cause "
                "explains the rise, its fluid-reasoning concentration, "
                "and the reversal together."),
 "why_it_matters": ("The Flynn effect is the largest natural experiment "
                    "in cognitive enhancement ever observed. Its cause "
                    "would reveal exactly which environments raise human "
                    "reasoning — and the reversal warns the gains are not "
                    "guaranteed."),
 "assumptions": [
   "The rise is too fast for genetic change.",
   "Fluid-reasoning concentration is a diagnostic clue.",
   "The reversal is real data, not measurement artifact."],
 "confirm": [
   ("Speed of rise", "Three points per decade rules out genetic explanations.", 0.30),
   ("Fluid concentration", "Gains center on abstract reasoning, pointing at environmental complexity.", 0.25),
   ("Multiplier models", "Social-multiplier mathematics reproduces the curve shape.", 0.20)],
 "refute": [
   ("No single cause", "No one factor tracks the rise across all countries.", 0.25),
   ("Reversal puzzle", "Stalling in rich countries strains nutrition and schooling accounts.", 0.25),
   ("Test artifact", "Changing test composition could mimic real gains.", 0.15)],
 "sig_body": (
   "The Signature reading treats the Flynn effect as the cognitive equivalent of rising heights: environments got richer in abstract-demand calories, and brains — like bodies — grew on the better diet. "
   "Step one, the 20th century industrialized abstraction: schooling expanded, jobs demanded symbolic reasoning, media saturated life with puzzles of representation — the daily cognitive diet changed more than genes ever could. "
   "Step two, fluid reasoning gained most because it is the most diet-sensitive: it measures on-the-spot pattern handling, exactly what complex environments train, while crystallized knowledge was already being taught. "
   "Step three, the Dickens-Flynn multiplier closes the loop: slightly sharper individuals build slightly more demanding environments (better schools, harder games), which sharpen the next cohort — a feedback loop, not a single cause. "
   "Step four, the reversal is the loop saturating or shifting diet: where schooling quality slipped or the cognitive diet moved from abstraction to passive consumption, the multiplier runs in reverse. "
   "What would confirm it: Confirm C1 — Speed of rise: three points per decade rules out genetic explanations. "
   "Confirm C2 — Fluid concentration: gains center on abstract reasoning, pointing at environmental complexity. "
   "Confirm C3 — Multiplier models: social-multiplier mathematics reproduces the curve shape. "
   "What would refute it: Refute R1 — No single cause: no one factor tracks the rise across all countries. "
   "Refute R2 — Reversal puzzle: stalling in rich countries strains nutrition and schooling accounts. "
   "Refute R3 — Test artifact: changing test composition could mimic real gains. "
   "What it does NOT claim: it does not claim any population is inherently more or less intelligent, or that the reversal proves decline. "
   "Honest status: a proposal only — the Flynn effect's cause remains open in established science."),
},
{
 "key": "replication-crisis-causes",
 "name": "Why Do Psychological Effects Fail to Replicate?",
 "group": "Science of Psychology",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": ("In 2015 a massive effort found only about a third of "
             "psychology studies replicated. The unsolved problem is the "
             "deep cause: is psychology studying fragile phenomena, "
             "broken methods, or a reward system that manufactures "
             "false positives?"),
 "background": ("Ioannidis argued in 2005 that most published findings "
                "are false, given low power and publication bias. The "
                "Open Science Collaboration (2015) replicated 100 "
                "studies and succeeded on roughly 36 percent by "
                "significance criteria, with smaller effect sizes. "
                "Explanations compete: p-hacking and researcher degrees "
                "of freedom, underpowered designs, publication bias "
                "burying nulls, and hidden moderators — effects real but "
                "context-sensitive. Reforms followed: preregistration, "
                "registered reports, larger samples, open data. Yet "
                "replication rates improved only partially, and some "
                "argue psychology studies moving targets — human "
                "behavior in changing cultures — so exact replication is "
                "the wrong standard. The deep cause is still disputed."),
 "why_it_matters": ("Trillions in policy, medicine, and business rest on "
                    "psychological findings. Knowing whether the crisis is "
                    "method, phenomenon, or incentive decides whether the "
                    "science can be fixed — and how."),
 "assumptions": [
   "The 2015 low replication rate is roughly accurate.",
   "Multiple causes operate simultaneously.",
   "Context-sensitivity is a hypothesis, not an excuse."],
 "confirm": [
   ("Shrunken effects", "Replications find systematically smaller effects, signaling bias.", 0.30),
   ("Power failures", "Original studies were chronically underpowered.", 0.25),
   ("Reform gains", "Preregistered replications replicate better.", 0.20)],
 "refute": [
   ("Hidden moderators", "Failed replications may miss real context conditions.", 0.25),
   ("Standard too strict", "Exact replication may be the wrong bar for human science.", 0.20),
   ("Field differences", "Some subfields replicate well, against blanket crisis claims.", 0.15)],
 "sig_body": (
   "The Signature reading treats the crisis as an incentive-structure artifact amplified by a real feature of the subject matter: the reward system selected for surprising positives, and human behavior genuinely varies by context — both are true at once. "
   "Step one, journals rewarded novelty and significance, so the published record is a filtered sample — p-hacking and publication bias are the filter's mechanics, and shrunken replication effects are the filter's fingerprint. "
   "Step two, low power plus many researcher degrees of freedom made the filter efficient: with small samples and flexible analyses, noise reliably produces publishable 'findings.' "
   "Step three, the context-sensitivity defense has a kernel of truth — social priming effects really do depend on cultural moment — but it cannot explain why the failures concentrate in exactly the subfields with the weakest methods. "
   "Step four, the fix is therefore two-layered: reform the incentives (preregistration, registered reports) and right-size the claims (estimate effect distributions across contexts instead of chasing universal effects). "
   "What would confirm it: Confirm C1 — Shrunken effects: replications find systematically smaller effects, signaling bias. "
   "Confirm C2 — Power failures: original studies were chronically underpowered. "
   "Confirm C3 — Reform gains: preregistered replications replicate better. "
   "What would refute it: Refute R1 — Hidden moderators: failed replications may miss real context conditions. "
   "Refute R2 — Standard too strict: exact replication may be the wrong bar for human science. "
   "Refute R3 — Field differences: some subfields replicate well, against blanket crisis claims. "
   "What it does NOT claim: it does not claim psychology is worthless, or that any specific finding is false. "
   "Honest status: a proposal only — the crisis's deep causes remain open in established science."),
},
{
 "key": "unconscious-depth",
 "name": "What Is the Unconscious?",
 "group": "Mind and Brain",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": ("Freud made the unconscious famous; modern science made it "
             "respectable, then messy. The unsolved problem is its true "
             "extent and structure: how much of mental life runs without "
             "awareness, and how is it organized?"),
 "background": ("Freud's dynamic unconscious held repressed wishes "
                "shaping behavior. Cognitive science replaced it with "
                "the 'new unconscious': implicit memory, automatic "
                "skills, blindsight (Weiskrantz) where cortically blind "
                "patients respond to unseen stimuli. Priming research "
                "claimed subtle cues steer behavior, but the flagship "
                "social-priming findings largely failed to replicate. "
                "Dijksterhuis's unconscious thought theory — that "
                "unconscious deliberation beats conscious thought on "
                "complex choices — also faltered under replication. What "
                "survives firmly: massive unconscious processing in "
                "perception, motor control, and learning. What does not: "
                "a coherent map of its limits, or whether it reasons, "
                "wants, and decides in any meaningful sense."),
 "why_it_matters": ("The unconscious question is the free-will question "
                    "writ large: if most of the mind runs dark, what "
                    "exactly is the conscious part for? The answer "
                    "redefines agency itself."),
 "assumptions": [
   "Unconscious processing is massive and real.",
   "Failed replications bound the grand claims.",
   "Different unconscious systems need separate theories."],
 "confirm": [
   ("Blindsight", "Unseen stimuli guide behavior without awareness.", 0.30),
   ("Implicit learning", "People learn patterns they cannot articulate.", 0.25),
   ("Automaticity", "Skills run unconsciously after practice.", 0.20)],
 "refute": [
   ("Priming collapse", "Flagship social-priming effects failed to replicate.", 0.30),
   ("UTT failure", "Unconscious-thought advantages did not hold up.", 0.20),
   ("No central executive", "No evidence of unified unconscious deliberation.", 0.20)],
 "sig_body": (
   "The Signature reading treats the unconscious not as one hidden mind but as the whole factory floor: dozens of specialized processors running dark, with consciousness as the small lit office upstairs that receives summaries and issues occasional directives. "
   "Step one, perception, motor control, habit, and associative learning all run unconsciously because they must be fast — awareness is too slow a medium for catching a ball. "
   "Step two, the grand Freudian claims failed because they projected office-style reasoning (wishes, plots, deliberation) onto the factory floor, which does pattern-matching, not plotting. "
   "Step three, blindsight and implicit learning are the floor working normally with the office's windows boarded up — the machinery never needed the lights. "
   "Step four, consciousness's real job is then narrow but crucial: handling novelty, conflict, and long-range planning — the cases where no dark processor has a ready routine. "
   "What would confirm it: Confirm C1 — Blindsight: unseen stimuli guide behavior without awareness. "
   "Confirm C2 — Implicit learning: people learn patterns they cannot articulate. "
   "Confirm C3 — Automaticity: skills run unconsciously after practice. "
   "What would refute it: Refute R1 — Priming collapse: flagship social-priming effects failed to replicate. "
   "Refute R2 — UTT failure: unconscious-thought advantages did not hold up. "
   "Refute R3 — No central executive: no evidence of unified unconscious deliberation. "
   "What it does NOT claim: it does not claim hidden messages control behavior, or that unconscious motives can be decoded from dreams or slips. "
   "Honest status: a proposal only — the unconscious's extent remains open in established science."),
},
]

ENTRIES += [
# --------------------------------------------------------------- 28-34
{
 "key": "depression-causes",
 "name": "What Causes Depression?",
 "group": "Mental Health Science",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": ("Depression disables more people worldwide than almost any "
             "other condition, yet its fundamental cause is unsolved. Is "
             "it a chemical imbalance, a circuit disorder, an "
             "inflammatory state, a cognitive pattern — or all of these "
             "at once?"),
 "background": ("The monoamine hypothesis — depression as serotonin or "
                "norepinephrine deficiency — guided decades of drug "
                "development, but Moncrieff's 2022 umbrella review found "
                "no consistent evidence linking serotonin to depression. "
                "Antidepressants help many patients, yet so do exercise, "
                "therapy, and placebo, and drugs take weeks to work. "
                "Newer accounts invoke impaired neuroplasticity and BDNF, "
                "chronic inflammation, HPA-axis dysregulation, and "
                "disrupted reward circuits. Beck's cognitive theory "
                "targets negative thought patterns with real therapeutic "
                "success. Genetics contributes modestly; life stress "
                "contributes strongly. The field increasingly suspects "
                "'depression' labels several different disorders sharing "
                "symptoms — which would explain why no single cause has "
                "been found."),
 "why_it_matters": ("A causal account would turn trial-and-error "
                    "treatment into targeted medicine and could prevent "
                    "episodes instead of chasing them. This record is "
                    "educational only: it does not diagnose, treat, or "
                    "advise any person. Anyone affected should consult "
                    "qualified professionals."),
 "assumptions": [
   "Depression is biologically real and heterogeneous.",
   "Treatment response is evidence about mechanism.",
   "Single-cause accounts have failed repeatedly."],
 "confirm": [
   ("Serotonin unproven", "Umbrella reviews find no consistent serotonin-depression link.", 0.25),
   ("Plural mechanisms", "Inflammation, plasticity, and circuit findings each replicate partially.", 0.30),
   ("Stress linkage", "Life stress robustly predicts onset across studies.", 0.20)],
 "refute": [
   ("Drugs work", "Monoamine drugs help millions, implying the system is involved.", 0.25),
   ("Heterogeneity defense", "Mixed results may reflect multiple disorders under one label.", 0.20),
   ("Cognitive success", "Therapy targeting thoughts works, against purely chemical accounts.", 0.20)],
 "sig_body": (
   "The Signature reading treats depression as a system stuck in a defensive shutdown mode: the brain's cost-benefit controller concludes — rightly or wrongly — that engagement is not worth the energy, and throttles motivation, pleasure, and plasticity accordingly. "
   "Step one, the controller integrates real signals: chronic stress, inflammation, social defeat, energy debt — all legitimate inputs that in the ancestral world meant 'conserve and withdraw.' "
   "Step two, the shutdown is implemented across levels at once: monoamines, BDNF-driven plasticity, HPA-axis tone, and reward-circuit gain all turn down together, which is why single-chemical theories each capture a slice. "
   "Step three, the trap is the controller's own feedback: withdrawal reduces the rewarding experiences that would update the cost-benefit estimate, so the shutdown self-confirms — the cognitive patterns Beck described are the controller's bookkeeping, not the root cause. "
   "Step four, heterogeneity follows: different people arrive at shutdown via different input mixes (inflammation-heavy, stress-heavy, loss-heavy), which is why one label holds several disorders and no single treatment works for all. "
   "What would confirm it: Confirm C1 — Serotonin unproven: umbrella reviews find no consistent serotonin-depression link. "
   "Confirm C2 — Plural mechanisms: inflammation, plasticity, and circuit findings each replicate partially. "
   "Confirm C3 — Stress linkage: life stress robustly predicts onset across studies. "
   "What would refute it: Refute R1 — Drugs work: monoamine drugs help millions, implying the system is involved. "
   "Refute R2 — Heterogeneity defense: mixed results may reflect multiple disorders under one label. "
   "Refute R3 — Cognitive success: therapy targeting thoughts works, against purely chemical accounts. "
   "What it does NOT claim: it does not diagnose or explain any person's condition, recommend any treatment, or suggest depression is a choice. This is educational description of open science only; anyone affected should consult qualified professionals. "
   "Honest status: a proposal only — depression's causes remain open in established science."),
},
{
 "key": "schizophrenia-causes",
 "name": "What Causes Schizophrenia?",
 "group": "Mental Health Science",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": ("Schizophrenia profoundly alters perception, thought, and "
             "selfhood, and its mechanism is unsolved. Genes explain "
             "most of the risk, yet no gene causes it; dopamine drugs "
             "treat symptoms, yet dopamine is not the whole story. What "
             "actually goes wrong?"),
 "background": ("Heritability estimates reach around 80 percent, but "
                "genome studies implicate hundreds of variants plus "
                "rare copy-number changes — no single cause. The "
                "dopamine hypothesis arose because antipsychotics block "
                "dopamine and amphetamines can induce psychosis, yet "
                "many patients respond partially and dopamine measures "
                "are inconsistent. The neurodevelopmental view points to "
                "prenatal infection, obstetric complications, and "
                "adolescent synaptic pruning gone awry. Recent work adds "
                "glutamate dysfunction and immune/microglial involvement. "
                "Onset in late adolescence, urban upbringing, and "
                "migration raise risk for reasons still unclear. The "
                "field has risk factors and treatments but no agreed "
                "causal chain."),
 "why_it_matters": ("Current drugs blunt symptoms with heavy side "
                    "effects and leave cognitive symptoms largely "
                    "untouched. A causal mechanism would enable "
                    "prevention and genuinely targeted treatment. This "
                    "record is educational only and does not diagnose or "
                    "advise any person."),
 "assumptions": [
   "High heritability with diffuse genetics implies developmental pathways.",
   "Adolescent onset timing is a mechanistic clue.",
   "Symptom treatment success partially constrains causes."],
 "confirm": [
   ("Diffuse genetics", "Hundreds of variants implicate neurodevelopmental pathways.", 0.30),
   ("Pruning timing", "Onset aligns with adolescent synaptic pruning schedules.", 0.20),
   ("Glutamate evidence", "NMDA dysfunction models reproduce psychosis-like states.", 0.25)],
 "refute": [
   ("Dopamine partial", "Dopamine blockade helps but leaves much unexplained.", 0.25),
   ("Risk not destiny", "Most high-risk individuals never develop the condition.", 0.20),
   ("Urban mystery", "Urban upbringing raises risk for unknown reasons.", 0.15)],
 "sig_body": (
   "The Signature reading treats schizophrenia as a prediction-system disorder: the brain's reality-testing machinery — the circuits that tag perceptions as self-generated versus world-generated — miscalibrates during adolescent rewiring, and the miscalibration compounds. "
   "Step one, the brain constantly predicts its own sensory consequences and cancels them (which is why you cannot tickle yourself); psychosis begins when this cancellation fails, so inner speech arrives tagged as external voice. "
   "Step two, adolescent synaptic pruning is when the prediction machinery gets its final calibration — diffuse genetic variants that slightly alter pruning, plus prenatal and immune hits, push the calibration off in vulnerable brains. "
   "Step three, dopamine's role is gain control on the error signal: too much gain and every coincidence feels significant, which is why dopamine blockade quiets positive symptoms without fixing the underlying miscalibration. "
   "Step four, delusions are the system's attempt to explain the faulty data — a rational response to irrational inputs, which is why arguing against them rarely works. "
   "What would confirm it: Confirm C1 — Diffuse genetics: hundreds of variants implicate neurodevelopmental pathways. "
   "Confirm C2 — Pruning timing: onset aligns with adolescent synaptic pruning schedules. "
   "Confirm C3 — Glutamate evidence: NMDA dysfunction models reproduce psychosis-like states. "
   "What would refute it: Refute R1 — Dopamine partial: dopamine blockade helps but leaves much unexplained. "
   "Refute R2 — Risk not destiny: most high-risk individuals never develop the condition. "
   "Refute R3 — Urban mystery: urban upbringing raises risk for unknown reasons. "
   "What it does NOT claim: it does not diagnose or explain any person's condition, recommend any treatment, or assign blame to families or individuals. Educational description of open science only. "
   "Honest status: a proposal only — schizophrenia's causes remain open in established science."),
},
{
 "key": "consciousness-measurement",
 "name": "How Can Consciousness Be Measured?",
 "group": "Consciousness",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": ("Doctors must judge consciousness in unresponsive patients, "
             "and science must detect it in animals and machines — yet "
             "there is no agreed meter for consciousness. The unsolved "
             "problem is measurement: what observable quantity tracks "
             "the presence of experience?"),
 "background": ("Tononi's Integrated Information Theory proposes Phi, a "
                "measure of a system's integrated information, as the "
                "quantity of consciousness — mathematically precise but "
                "uncomputable for real brains and contested as a "
                "criterion. The Global Neuronal Workspace theory "
                "(Dehaene, Changeux) ties consciousness to ignition of a "
                "brain-wide broadcast network. Massimini's perturbational "
                "complexity index (PCI) zaps the cortex with magnetic "
                "pulses and measures the EEG echo's complexity — it "
                "distinguishes conscious from unconscious patients "
                "better than behavior. Yet PCI measures responsiveness "
                "complexity, and critics ask whether that is "
                "consciousness or just complex processing. Anesthesia, "
                "sleep, and locked-in states each challenge every "
                "proposed meter differently."),
 "why_it_matters": ("A valid meter would transform care for coma and "
                    "locked-in patients, settle animal sentience debates, "
                    "and tell us whether any machine could be conscious — "
                    "one of the century's defining questions."),
 "assumptions": [
   "Consciousness comes in degrees and kinds, not a single on-off.",
   "Behavioral unresponsiveness does not equal unconsciousness.",
   "Any meter must survive anesthesia, sleep, and seizure counterexamples."],
 "confirm": [
   ("PCI discrimination", "Perturbational complexity separates conscious from unconscious patients.", 0.30),
   ("Anesthesia tracking", "Proposed measures fall reliably under anesthesia.", 0.20),
   ("Covert awareness", "Some unresponsive patients show command-following in scanners.", 0.25)],
 "refute": [
   ("Phi uncomputable", "Integrated information cannot be computed for real brains.", 0.25),
   ("Complexity ambiguity", "Complex responses may reflect processing, not experience.", 0.25),
   ("Theory split", "Leading theories disagree on what to measure.", 0.20)],
 "sig_body": (
   "The Signature reading treats consciousness as graded broadcast depth: what can be measured is not experience itself but how widely and richly information is shared across the brain — and that quantity tracks experience closely enough to serve as a meter. "
   "Step one, define the observable: the spatiotemporal complexity of the brain's response to a standard perturbation — PCI's core idea — because a conscious brain answers a knock with a symphony and an unconscious one with an echo or silence. "
   "Step two, calibrate the meter on the clear cases: wakefulness high, deep sleep and anesthesia low, seizures paradoxically low despite high activity — which rules out mere 'brain activity' meters. "
   "Step three, apply to the gray zones: covert awareness in unresponsive patients shows intermediate complexity, matching the clinical reality that consciousness fades in degrees. "
   "Step four, accept the principled limit: the meter tracks the broadcast, and the identification of broadcast with experience remains a theoretical bridge — honest meters report their bridge assumptions. "
   "What would confirm it: Confirm C1 — PCI discrimination: perturbational complexity separates conscious from unconscious patients. "
   "Confirm C2 — Anesthesia tracking: proposed measures fall reliably under anesthesia. "
   "Confirm C3 — Covert awareness: some unresponsive patients show command-following in scanners. "
   "What would refute it: Refute R1 — Phi uncomputable: integrated information cannot be computed for real brains. "
   "Refute R2 — Complexity ambiguity: complex responses may reflect processing, not experience. "
   "Refute R3 — Theory split: leading theories disagree on what to measure. "
   "What it does NOT claim: it does not claim any current meter is validated, or that machines are or are not conscious. "
   "Honest status: a proposal only — measuring consciousness remains open in established science."),
},
{
 "key": "hard-problem-consciousness",
 "name": "The Hard Problem of Consciousness",
 "group": "Consciousness",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": ("Science can map every neuron firing when you see red — and "
             "still not explain why there is something it is like to see "
             "red. Chalmers named this the hard problem in 1995: why is "
             "any physical process accompanied by experience at all?"),
 "background": ("Levine (1983) identified the explanatory gap: no "
                "physical description entails the feel of experience. "
                "Chalmers distinguished the 'easy problems' — explaining "
                "discrimination, report, attention — from the hard one: "
                "why these functions feel like anything. The zombie "
                "argument asks us to conceive a physically identical "
                "being with no inner life, suggesting experience is an "
                "extra fact. Responses range from illusionism (Dennett, "
                "Frankish: we are wrong that there is a hard problem) to "
                "panpsychism (Strawson, Goff: experience is fundamental) "
                "to mysterianism (McGinn: our minds cannot grasp the "
                "answer). Neuroscience's neural correlates program maps "
                "experience's footprints without explaining why "
                "footprints feel like anything."),
 "why_it_matters": ("The hard problem is the deepest question about "
                    "ourselves: whether a complete science of the brain "
                    "leaves out the very thing it is like to be us. Its "
                    "resolution decides the limits of physical explanation."),
 "assumptions": [
   "The easy/hard distinction marks a real explanatory gap.",
   "First-person reports are data, not illusions to dismiss lightly.",
   "Any solution must handle the zombie conceivability argument."],
 "confirm": [
   ("Explanatory gap", "No physical account entails subjective feel.", 0.30),
   ("Zombie conceivability", "A non-conscious duplicate seems conceivable.", 0.20),
   ("Correlates not causes", "Neural correlates map experience without explaining it.", 0.25)],
 "refute": [
   ("Illusionist reply", "The hard problem may dissolve under careful analysis.", 0.25),
   ("Conceivability weak", "Conceivability does not prove metaphysical possibility.", 0.20),
   ("Progress reply", "Easy-problem progress keeps shrinking the gap.", 0.15)],
 "sig_body": (
   "The Signature reading treats the hard problem as a category error made by a good instinct: we ask why processing 'feels like' something because we are the processing, and being a process from the inside is what feeling is. "
   "Step one, separate two questions the hard problem fuses: (a) why does information processing have the functional profile of awareness, and (b) why is there 'something it is like' — the Signature answer is that (b) is what (a) is like from the inside, not an extra fact. "
   "Step two, the zombie argument then asks us to conceive the functional profile without the inside view — but conceiving a system 'from the outside' while stipulating no inside view begs the question, since the inside view is not an add-on property but the system's own perspective. "
   "Step three, illusionism gets half credit: we are indeed wrong about experience being a separate inner glow — but wrong in a way that still needs explaining, because the systematic misdescription is itself data. "
   "Step four, what remains genuinely hard is not a metaphysical extra but an epistemic limit: a system cannot fully model itself modeling, so the feeling of irreducibility is exactly what self-modeling systems should report. "
   "What would confirm it: Confirm C1 — Explanatory gap: no physical account entails subjective feel. "
   "Confirm C2 — Zombie conceivability: a non-conscious duplicate seems conceivable. "
   "Confirm C3 — Correlates not causes: neural correlates map experience without explaining it. "
   "What would refute it: Refute R1 — Illusionist reply: the hard problem may dissolve under careful analysis. "
   "Refute R2 — Conceivability weak: conceivability does not prove metaphysical possibility. "
   "Refute R3 — Progress reply: easy-problem progress keeps shrinking the gap. "
   "What it does NOT claim: it does not claim the hard problem is solved, or that any position in the debate is refuted. "
   "Honest status: a proposal only — the hard problem remains open in established science."),
},
{
 "key": "other-minds-problem",
 "name": "The Problem of Other Minds",
 "group": "Consciousness",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": ("You know you are conscious from the inside; everyone else "
             "you know only from the outside. The unsolved problem: how "
             "can we ever know that other beings — people, animals, "
             "machines — actually experience anything?"),
 "background": ("Philosophers have pressed the problem for centuries: "
                "behavior underdetermines inner life, and analogy ('they "
                "act like me, so they feel like me') is inference, not "
                "knowledge. Developmental psychology found theory of mind "
                "— the ability to attribute mental states — emerging "
                "around age four, measured by false-belief tasks (Wimmer "
                "and Perner 1983). Premack and Woodruff (1978) asked "
                "whether chimpanzees have a theory of mind, opening "
                "decades of animal-cognition debate. Mirror neurons were "
                "briefly hailed as the neural basis of mind-reading, "
                "then the hype collapsed under scrutiny. Autism research "
                "reframed mind-blindness accounts. With AI systems now "
                "mimicking conscious behavior fluently, the problem has "
                "moved from seminar room to engineering lab — still "
                "unsolved."),
 "why_it_matters": ("The answer sets the moral circle: which beings "
                    "count as experiencers deserving consideration. It "
                    "also decides whether we will recognize machine "
                    "consciousness if we ever build it — or falsely "
                    "attribute it long before."),
 "assumptions": [
   "Behavior alone cannot settle the question.",
   "Theory of mind is a real cognitive capacity with limits.",
   "The problem applies symmetrically to animals and machines."],
 "confirm": [
   ("False-belief marker", "Mind-attribution capacity emerges measurably in development.", 0.20),
   ("Animal debate", "Decades of experiments leave animal experience contested.", 0.25),
   ("AI mimicry", "Fluent behavior without settled inner life is now demonstrable.", 0.30)],
 "refute": [
   ("Analogy strength", "Shared biology makes human-to-human inference extremely reliable.", 0.25),
   ("Neuroscience bridge", "Shared neural mechanisms support shared experience claims.", 0.20),
   ("Practical success", "Mind-reading works well enough for social life.", 0.15)],
 "sig_body": (
   "The Signature reading treats other-minds knowledge as structural inference, not analogy: we do not guess others feel because they act like us — we infer it because the same causal architecture that produces our experience produces their behavior. "
   "Step one, analogy is indeed weak for strangers and machines; what is strong is mechanism: when neuroscience shows the same broadcast architecture, the same pain circuitry, the same global-workspace dynamics, the inference is to shared structure, not similar acting. "
   "Step two, this dissolves the false symmetry between humans, animals, and AI: the question is never 'does it behave consciously' but 'does it run the architecture that constitutes experiencing' — a question about wiring, answerable in principle. "
   "Step three, theory of mind is then revealed as the brain's built-in structural-inference engine, evolved for predicting kin — useful, biased, and extendable by science beyond its native range. "
   "Step four, the residual uncertainty is honest and permanent for exotic cases, but it shrinks with mechanistic knowledge rather than growing with behavioral mimicry. "
   "What would confirm it: Confirm C1 — False-belief marker: mind-attribution capacity emerges measurably in development. "
   "Confirm C2 — Animal debate: decades of experiments leave animal experience contested. "
   "Confirm C3 — AI mimicry: fluent behavior without settled inner life is now demonstrable. "
   "What would refute it: Refute R1 — Analogy strength: shared biology makes human-to-human inference extremely reliable. "
   "Refute R2 — Neuroscience bridge: shared neural mechanisms support shared experience claims. "
   "Refute R3 — Practical success: mind-reading works well enough for social life. "
   "What it does NOT claim: it does not claim any animal or machine is or is not conscious, or settle anyone's moral status. "
   "Honest status: a proposal only — the problem of other minds remains open in established science."),
},
{
 "key": "matter-to-experience",
 "name": "How Does Matter Become Experience?",
 "group": "Mind and Body",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": ("The mind-body problem is philosophy's oldest unsolved "
             "question and neuroscience's deepest: how does three "
             "pounds of electrochemical tissue generate the taste of "
             "coffee, the sting of grief, the sense of self?"),
 "background": ("Descartes split mind and body into separate substances, "
                "leaving interaction mysterious. Physicalism answers "
                "that mind is what brain does, but the emergence step — "
                "how — is unspecified. Crick and Koch launched the "
                "modern neural-correlates program in 1990, mapping "
                "experience's neural footprints with growing precision. "
                "Emergentists argue experience is a higher-level "
                "property like wetness from H2O molecules; critics reply "
                "wetness is still publicly observable while experience "
                "is private. Panpsychists propose experience as "
                "fundamental, merely combined in brains. "
                "Neuroscientists increasingly bracket the metaphysics "
                "and map correlates — progress without resolution."),
 "why_it_matters": ("This is the question beneath every other question "
                    "in this database. Its answer would complete the "
                    "scientific worldview — or reveal its permanent "
                    "boundary."),
 "assumptions": [
   "Correlates are real progress even without metaphysical settlement.",
   "Emergence analogies must be tested, not assumed.",
   "Privacy of experience is a datum, not a confusion."],
 "confirm": [
   ("Correlate mapping", "Specific experiences map to specific neural patterns ever more precisely.", 0.30),
   ("Intervention works", "Stimulating or lesioning brain tissue changes experience predictably.", 0.25),
   ("No extra ingredient", "No non-physical signal has ever been detected in the brain.", 0.20)],
 "refute": [
   ("Emergence gap", "Wetness analogies fail on the privacy of experience.", 0.25),
   ("Combination problem", "Panpsychism cannot explain how micro-experiences combine.", 0.20),
   ("Hard remainder", "Correlate maps leave the why-of-feel untouched.", 0.20)],
 "sig_body": (
   "The Signature reading treats experience as what integrated information processing is like from the inside when the processing includes a self-model: matter 'becomes' experience at the point where a physical system models itself as an experiencer. "
   "Step one, start with the uncontroversial: brains integrate information across senses, memory, and goals into a unified control model — the correlates program maps this integration faithfully. "
   "Step two, add the self-model: the system does not just integrate the world, it integrates a model of itself integrating — and that recursive loop is the structural signature of subjectivity, the point at which there is 'something it is like' to be the system. "
   "Step three, privacy follows from architecture, not magic: the self-model's contents are encoded in the system's own idiosyncratic format, accessible to its control processes but not to outside observers — private the way a compiled binary is private to its source. "
   "Step four, this predicts a graded, testable boundary: systems with richer integration plus self-modeling should show richer experience-correlates, which is exactly the research program consciousness science is already running. "
   "What would confirm it: Confirm C1 — Correlate mapping: specific experiences map to specific neural patterns ever more precisely. "
   "Confirm C2 — Intervention works: stimulating or lesioning brain tissue changes experience predictably. "
   "Confirm C3 — No extra ingredient: no non-physical signal has ever been detected in the brain. "
   "What would refute it: Refute R1 — Emergence gap: wetness analogies fail on the privacy of experience. "
   "Refute R2 — Combination problem: panpsychism cannot explain how micro-experiences combine. "
   "Refute R3 — Hard remainder: correlate maps leave the why-of-feel untouched. "
   "What it does NOT claim: it does not claim the mind-body problem is solved, or that materialism or any rival is proven. "
   "Honest status: a proposal only — how matter becomes experience remains open in established science."),
},
{
 "key": "mind-architecture",
 "name": "The Full Architecture of Mind",
 "group": "Mind and Brain",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": ("Psychology has theories of perception, memory, emotion, "
             "and consciousness — but no unified architecture showing "
             "how they fit together in one working mind. The unsolved "
             "problem is the whole: what is the complete functional "
             "blueprint of a human mind?"),
 "background": ("Cognitive architectures like ACT-R and Soar model "
                "unified cognition and match human data on specific "
                "tasks, but cover only slices of mental life. Global "
                "Workspace Theory offers a blackboard all specialists "
                "read and write, with growing neural evidence. Friston's "
                "predictive processing proposes the whole cortex as a "
                "hierarchy minimizing prediction error — elegant, "
                "ambitious, and still short of a complete working "
                "model. Each subfield's theory works locally; the "
                "interfaces between them — how emotion reshapes memory "
                "consolidation, how attention gates conscious broadcast "
                "— are sketched, not specified. No architecture yet "
                "runs the full human repertoire: perceiving, remembering, "
                "feeling, choosing, and being aware, all at once."),
 "why_it_matters": ("A complete architecture would unify psychology's "
                    "fragments, guide brain-inspired AI, and finally "
                    "show how the 33 problems in this database are 33 "
                    "views of one machine."),
 "assumptions": [
   "Local theories are largely correct and must be preserved.",
   "The interfaces between systems are where the mystery lives.",
   "A real architecture must run, not just describe."],
 "confirm": [
   ("Architecture models", "ACT-R and Soar reproduce human performance on modeled tasks.", 0.25),
   ("Workspace evidence", "Brain-wide broadcast dynamics match global workspace predictions.", 0.25),
   ("Predictive fit", "Prediction-error signals appear throughout cortical hierarchies.", 0.25)],
 "refute": [
   ("Slice coverage", "No architecture covers the full mental repertoire.", 0.30),
   ("Interface gaps", "Interactions between emotion, memory, and attention are underspecified.", 0.25),
   ("Scale shortfall", "Working models are toy-sized beside a real brain.", 0.20)],
 "sig_body": (
   "The Signature reading proposes the mind as a prediction hierarchy with a broadcast summit: layered predictors handle perception, memory, and action, and a global workspace broadcasts the winners — with emotion as the value-weighting on every bid and the self-model as the summit's standing agenda item. "
   "Step one, the base is predictive processing all the way down: each cortical layer predicts the layer below and reports only errors upward — perception, motor control, and much of thought are one error-minimizing stack. "
   "Step two, the summit is the global workspace: winning predictions get broadcast brain-wide, which is why attention, working memory, and conscious access travel together — they are three names for winning the broadcast. "
   "Step three, emotion is not a separate module but the bid-weighting: value signals from the body and from learned goals set the salience of every prediction, which is why feelings color perception, memory, and choice simultaneously. "
   "Step four, memory systems are the hierarchy's training logs at different timescales — hippocampal RAM, cortical disk — and the self is the summit's persistent model of the bidder, explaining why all 33 preceding problems are views of one machine. "
   "What would confirm it: Confirm C1 — Architecture models: ACT-R and Soar reproduce human performance on modeled tasks. "
   "Confirm C2 — Workspace evidence: brain-wide broadcast dynamics match global workspace predictions. "
   "Confirm C3 — Predictive fit: prediction-error signals appear throughout cortical hierarchies. "
   "What would refute it: Refute R1 — Slice coverage: no architecture covers the full mental repertoire. "
   "Refute R2 — Interface gaps: interactions between emotion, memory, and attention are underspecified. "
   "Refute R3 — Scale shortfall: working models are toy-sized beside a real brain. "
   "What it does NOT claim: it does not claim a complete working model exists, or that building one is near. "
   "Honest status: a proposal only — the full architecture of mind remains open in established science."),
},
]

POINTER_TMPL = (
  "This record presents the problem as established science knows it — the "
  "facts, the history, and where the field stands today. The Signature "
  "system's proposed solution approach is published as the companion "
  "record in The Unsolved Psychology Signature Database: see record %s "
  "in that archive. That companion solution is labeled Signature-generated "
  "throughout; it is a proposal, not established science, and it claims "
  "no proof and no peer acceptance.")

def public_solution(companion_id):
    return LABEL + " " + (POINTER_TMPL % companion_id)

def signature_solution(entry):
    return LABEL + "\n\n" + entry["sig_body"]

def expected_net(entry):
    c = sum(w for _, _, w in entry["confirm"])
    r = sum(w for _, _, w in entry["refute"])
    return (c - r) / (c + r)
