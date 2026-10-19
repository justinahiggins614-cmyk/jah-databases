#!/usr/bin/env python3
"""Entries for the Unsolved Biology databases (Manon's 16:15 orders, Unsolved Problems Solved batch 1).

34 famous unsolved biology problems, ladder-ordered by accessibility (rank 1 = most
approachable, rank 34 = most complex). Public half: JAH-USBI- (real, fact-checked problems
as the world knows them). Signature half: JAH-USBIS- (same 34 problems through the
Signature lens; titles suffixed " (Signature Edition)", src signature, clearly labeled
Signature-made, never presented as authentic public record).

ID prefixes JAH-USBI- / JAH-USBIS- verified free 2026-10-17: zero hits in the manifest
id_prefix values (2,442 databases) and zero hits in every shard index file of
jah-databases-data-1 (full zgrep sweep over data/*/index.jsonl.gz).

The Signature solution in every record opens with the EXACT label
"Signature-generated proposed solution - not established science."
Public halves carry a short pointer; signature halves carry the full treatment.
Honesty rule: no claims of proof, no implied peer acceptance, speculation never
presented as settled.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. All records human-readable sentences/paragraphs.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature original - his original Signature Method applied to biology: "
            "every unsolved problem a covenant question, the solution explorer the "
            "Signature system's walkthrough, confirm-and-refute panels the oath of "
            "honesty. Clearly labeled Signature-made, never presented as established "
            "science or authentic public record.")

CIT_SLEEP = ("Borbely AA. Human sleep: the two-process model. Hum Neurobiol. 1982;1:195-204; "
             "Tononi G, Cirelli C. Sleep and the price of plasticity: from synaptic homeostasis "
             "to memory consolidation and integration. Neuron. 2014;81:12-34.")
CIT_DREAM = ("Hobson JA, Friston KJ. Waking and dreaming consciousness: neurobiological and "
             "functional considerations. Prog Neurobiol. 2012;98:82-98; Walker MP. Why We "
             "Sleep. Scribner; 2017.")
CIT_MEMORY = ("Kandel ER. The molecular biology of memory storage: a dialogue between genes "
              "and synapses. Science. 2001;294:1030-1038; Josselyn SA, Tonegawa S. Memory "
              "engrams: recalling the past and imagining the future. Science. 2020;367:eaaw4325.")
CIT_PAIN = ("Basbaum AI et al. Cellular and molecular mechanisms of pain. Cell. 2009;139:267-284; "
            "Woolf CJ. Central sensitization: implications for the diagnosis and treatment of "
            "pain. Pain. 2011;152:S2-S15.")
CIT_AGING = ("Lopez-Otin C et al. Hallmarks of aging: an expanding universe. Cell. 2023;186:243-278; "
             "Kennedy BK et al. Geroscience: linking aging to chronic disease. Cell. 2014;159:709-713.")
CIT_LIFESPAN = ("Speakman JR. Body size, energy metabolism and lifespan. J Exp Biol. 2005;208:1717-1730; "
               "de Magalhaes JP, Costa J, Church GM. An analysis of the relationship between metabolism, "
               "developmental schedules, and longevity using phylogenetic independent contrasts. "
               "J Gerontol A. 2007;62:149-160.")
CIT_REGEN = ("Brockes JP, Kumar A. Comparative aspects of animal regeneration. Annu Rev Cell Dev "
             "Biol. 2008;24:525-549; Tanaka EM, Reddien PW. The cellular basis for animal "
             "regeneration. Dev Cell. 2011;21:172-185.")
CIT_IMMUNITY = ("Janeway CA Jr. Approaching the asymptote? Evolution and revolution in immunology. "
                "Cold Spring Harb Symp Quant Biol. 1989;54:1-13; Medzhitov R, Janeway C Jr. Innate "
                "immunity. N Engl J Med. 2000;343:338-344.")
CIT_CELLFATE = ("Waddington CH. The Strategy of the Genes. Allen and Unwin; 1957; Takahashi K, "
                "Yamanaka S. Induction of pluripotent stem cells from mouse embryonic and adult "
                "fibroblast cultures by defined factors. Cell. 2006;126:663-676.")

ENTRIES = [
 {
  "key": "sleep",
  "name": "Why We Sleep",
  "group": "Mind and Brain",
  "ladder_rank": 1, "ladder_tier": "foundations",
  "description": ("Every animal with a nervous system sleeps, yet after a century of research "
                  "no single function of sleep commands consensus. Sleep is the most familiar "
                  "unsolved problem in biology: we spend a third of our lives doing it, it is "
                  "actively enforced by the brain, and total deprivation kills laboratory animals "
                  "within weeks, yet why the brain must go offline remains debated."),
  "problem": "What is sleep for - what function makes nightly unconsciousness worth a third of every life?",
  "background": ("Sleep was first recorded electrically by Hans Berger in the 1920s, and rapid-eye-movement "
                 "sleep was discovered by Aserinsky and Kleitman in 1953. Alexander Borbely's two-process model "
                 "in 1982 described sleep pressure building during wakefulness and discharging during sleep, "
                 "gated by the circadian clock. Proposed functions multiplied: memory consolidation, synaptic "
                 "downscaling to save energy (Tononi and Cirelli's synaptic homeostasis hypothesis), metabolic "
                 "clearance via the glymphatic system, immune regulation, and emotional processing. Yet animals "
                 "deprived of sleep die of no single clear cause, and no experiment has cleanly separated sleep's "
                 "many correlates from its core purpose. The field agrees sleep is essential; it does not agree why."),
  "why_it_matters": ("A real answer would reshape medicine: insomnia, sleep apnea, and shift-work disorder cost "
                      "economies hundreds of billions yearly and raise risks of dementia, heart disease, and "
                      "diabetes. It would also settle whether the brain can ever be engineered to need less sleep, "
                      "a question with consequences for every human schedule."),
  "sig_lens": ("The Signature lens treats sleep as a covenant the brain keeps with its own wiring: a nightly "
               "audit where the day's ledger is reconciled before the next day can be written."),
  "sol_public": ("The Signature system proposes sleep is the brain's mandatory audit cycle - a nightly "
                 "reconciliation in which synaptic weights earned during the day are settled, tested, and "
                 "pruned against a fixed energy budget, and no animal can skip the audit because the ledger "
                 "compounds. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the brain runs on a strict daily energy budget it cannot exceed; "
              "(2) waking experience writes synaptic changes that are locally useful but globally incoherent; "
              "(3) offline replay is the only time the network can test those changes against the whole system. "
              "Reasoning path: treat the brain as a ledger. Every waking hour posts debits (energy spent, synapses "
              "strengthened). If the ledger is never reconciled, debits compound until the network saturates - "
              "this matches the observed rise in sleep pressure with time awake and the cognitive collapse of "
              "total deprivation. Proposed mechanism: sleep stages are audit phases - deep sleep settles metabolic "
              "and synaptic accounts (downscaling), REM sleep stress-tests the reconciled model against imagined "
              "scenarios (dreams as audit simulations). What would confirm it: a measurable ledger variable - e.g., "
              "total synaptic weight or a metabolic byproduct - that rises monotonically with wakefulness, falls "
              "monotonically with sleep, and predicts cognitive performance better than hours slept. What would "
              "kill it: an animal or human that maintains full cognition with zero sleep and no compensating "
              "mechanism, or proof that synaptic weights do not systematically change across the sleep-wake cycle. "
              "What it does NOT claim: that this is proven, that dreams have individual meaning, or that any "
              "pill can safely replace the audit. Where the honest answer is unknown - why sleep pressure "
              "resets at the observed rate - we say so: the reset-rate constant is the missing measurement."),
  "key_points": [
   "Every studied animal with a nervous system sleeps; total sleep deprivation is lethal in lab animals.",
   "Borbely's two-process model (1982): sleep pressure rises in wakefulness, falls in sleep, gated by circadian rhythm.",
   "Leading candidate functions: memory consolidation, synaptic downscaling, glymphatic clearance, immune and emotional regulation.",
   "No single function has won consensus; correlates of sleep are hard to separate from its cause.",
   "Sleep disorders cost hundreds of billions yearly and raise dementia, cardiovascular, and metabolic risk."],
  "requirements": [
   "Identify a ledger variable that tracks sleep pressure monotonically and predicts performance.",
   "Confirm: synaptic or metabolic accounts systematically settle across sleep stages in vivo.",
   "Refute: find sustained full cognition with zero sleep and no compensating mechanism.",
   "Refute: show synaptic weights do not change systematically across the sleep-wake cycle."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim dreams carry messages or that sleep can be safely engineered away.",
   "It must survive the reset-rate question: the model needs a measured constant, not a fitted one."],
  "citations": [CIT_SLEEP],
 },
 {
  "key": "dream",
  "name": "Why We Dream",
  "group": "Mind and Brain",
  "ladder_rank": 2, "ladder_tier": "foundations",
  "description": ("We all dream several times a night, mostly in REM sleep, yet whether dreams do anything "
                  "at all is still open. The activation-synthesis hypothesis says dreams are the forebrain's "
                  "attempt to make sense of random brainstem noise; threat-simulation and memory theories say "
                  "dreams are functional rehearsals. A century of dream research has not settled which is true."),
  "problem": "Do dreams serve a function, or are they a by-product the brain merely narrates?",
  "background": ("Freud's 1900 Interpretation of Dreams made dreams culturally central but scientifically "
                 "marginal for decades. The 1953 discovery of REM sleep gave dreams a physiology: vivid dreaming "
                 "clusters in REM, when the brainstem fires in bursts (PGO waves) and the prefrontal cortex goes "
                 "quiet. Hobson and McCarley's 1977 activation-synthesis theory argued dreams are the cortex "
                 "weaving stories from random activation - functionless. Revonsuo's threat-simulation theory "
                 "(2000) countered that dreams rehearse dangers, an evolved simulator. Modern work ties dreaming "
                 "to emotional memory processing and creativity, but no experiment has shown that a creature "
                 "deprived specifically of dreams - with sleep otherwise intact - suffers a defined deficit. "
                 "The function, if any, remains unproven."),
  "why_it_matters": ("If dreams are a simulator, understanding them unlocks new treatments for PTSD nightmares, "
                      "anxiety, and depression, and a working model of offline learning that AI could borrow. "
                      "If they are noise, that too matters: it would end a century of over-interpretation."),
  "sig_lens": ("The Signature lens treats dreaming as the audit's test bench: the reconciled brain running "
               "itself against imagined cases before the next day's real ones arrive."),
  "sol_public": ("The Signature system proposes dreams are the brain's overnight test suite - structured "
                 "simulations run against the day's reconciled model to find its failures before reality does. "
                 "Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the sleeping brain has a freshly reconciled world-model each night; "
              "(2) a model can only be trusted after adversarial testing; (3) REM physiology - paralyzed body, "
              "active sensory cortex, quiet prefrontal evaluator - is exactly the rig a test suite needs. "
              "Reasoning path: engineers never ship an updated model without running tests; evolution, which "
              "punishes untested updates with death, should do the same. The bizarre content of dreams is not "
              "noise but coverage: the test generator sampling edge cases - falling, being chased, social "
              "exposure - because edge cases are where untested models fail. Proposed mechanism: the day's "
              "memory updates are loaded into a generative simulator during REM; threat and social scenarios "
              "dominate because those are the historically lethal failure modes; emotional charge tags the "
              "scenarios the model handled worst, prioritizing them for the next day's attention. What would "
              "confirm it: dream content statistically matching the individual's recent prediction errors, and "
              "selective dream deprivation (REM kept fragmented but sleep preserved) producing measurably worse "
              "next-day performance specifically on recently learned threats or skills. What would kill it: "
              "dreams that are pure replay with no novel recombination, or dream deprivation with zero "
              "cognitive cost. What it does NOT claim: that any single dream can be decoded into a message, "
              "that lucid dreaming grants control of the process, or that this is established. The honest "
              "unknown: whether the test suite improves the model or merely exercises it."),
  "key_points": [
   "Vivid dreaming concentrates in REM sleep, discovered 1953; the body is paralyzed while the cortex is active.",
   "Activation-synthesis (1977): dreams are stories woven from random brainstem activation - functionless.",
   "Threat-simulation (2000): dreams rehearse dangers - an evolved simulator.",
   "No experiment has isolated dream deprivation from sleep deprivation with a clean deficit.",
   "Dream content is emotional, social, and threat-heavy across cultures."],
  "requirements": [
   "Confirm: dream content correlates with the dreamer's recent prediction errors, not random replay.",
   "Confirm: selective dream disruption impairs next-day threat learning with sleep otherwise intact.",
   "Refute: dreams shown to be pure replay with no novel recombination.",
   "Refute: dream deprivation with zero measurable cognitive cost."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim individual dreams are decodable messages.",
   "Must answer whether the test suite improves the model or only exercises it - currently unknown."],
  "citations": [CIT_DREAM],
 },
 {
  "key": "memory",
  "name": "How Memories Are Stored",
  "group": "Mind and Brain",
  "ladder_rank": 3, "ladder_tier": "foundations",
  "description": ("We know memories live in the brain, and we know synapses change with experience, but how "
                  "a lifetime of episodes is written, kept for decades, and read back on demand is still "
                  "unsolved. The engram - the physical trace of a memory - can be found and even artificially "
                  "reactivated in mice, yet the code that turns a pattern of synaptic weights into a recalled "
                  "afternoon from childhood remains unknown."),
  "problem": "What is the physical code of a memory, and how does the brain write, keep, and read it for a lifetime?",
  "background": ("Lashley's decades-long hunt for the engram (1920s-1950s) ended in failure and the quip that "
                 "memory seemed everywhere and nowhere. Kandel's work on the sea slug Aplysia from the 1960s on "
                 "proved that learning changes synapses through defined molecular cascades - work that won the "
                 "2000 Nobel Prize. In the 2010s, Tonegawa's group labeled the actual neurons of a mouse fear "
                 "memory and reactivated them with light to trigger recall - the engram made visible. Yet the "
                 "code is missing: we can find which cells hold a memory but not how their activity pattern "
                 "encodes its content; we know consolidation moves memories from hippocampus to cortex over weeks "
                 "but not the transfer protocol; and we cannot explain how decades-old memories survive the "
                 "complete turnover of the molecules that supposedly store them."),
  "why_it_matters": ("Cracking the memory code would transform Alzheimer's treatment, education, and brain-machine "
                      "interfaces - and settle whether memories could ever be read out or backed up. Every therapy "
                      "for dementia today works blind, without knowing what it is trying to preserve."),
  "sig_lens": ("The Signature lens treats a memory as a covenant between a moment and the future: written in "
               "synapses, countersigned by systems, and honored across the turnover of every molecule."),
  "sol_public": ("The Signature system proposes memories are stored as multi-signed contracts - the same event "
                 "written in several brain systems at several timescales, so no single molecule's turnover can "
                 "void it. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) every molecule in a synapse is replaced within weeks to months; "
              "(2) some memories last a century; (3) therefore the code cannot be molecular identity - it must "
              "be pattern, and the pattern must be re-signed across substrates. Reasoning path: think of a "
              "covenant renewed by successive witnesses. The hippocampus writes the first signature (fast, "
              "detailed, fragile). During sleep, the signature is countersigned by cortical networks (slow, "
              "schematic, durable). Each countersigning re-encodes the pattern in fresh molecules, so molecular "
              "turnover becomes the renewal mechanism rather than the erasure mechanism. Forgetting is then not "
              "decay but unsigned contracts - traces never countersigned, or countersignatures overwritten by "
              "newer ones. Proposed mechanism: systems consolidation is a scheduled re-signing protocol gated "
              "by sleep; emotional charge (amygdala) sets signing priority; retrieval re-opens the contract for "
              "amendment, which is why recalled memories become temporarily fragile (reconsolidation). What "
              "would confirm it: tracking one memory's trace and showing its physical substrate migrating "
              "across systems on a schedule, with each migration refreshing - not merely copying - the code, "
              "and showing that blocking a scheduled re-signing erases the memory while blocking replay alone "
              "does not. What would kill it: a memory proven to persist for years with zero systems-level "
              "change, or molecular turnover shown to preserve information without any re-encoding step. "
              "What it does NOT claim: that memories can be read out like files, that this is established, or "
              "that every memory follows the same schedule. Honest unknown: the actual code - how a pattern "
              "of weights becomes the taste of a childhood meal - remains unmapped."),
  "key_points": [
   "Kandel proved learning changes synapses molecularly (Nobel 2000); Tonegawa's group reactivated labeled mouse engrams with light.",
   "The engram's cells are known; the code - how activity encodes content - is not.",
   "Consolidation moves memories from hippocampus to cortex over weeks by an unknown protocol.",
   "Synaptic molecules turn over in weeks; some memories last a lifetime - the paradox of persistence.",
   "Retrieval makes memories temporarily fragile (reconsolidation)."],
  "requirements": [
   "Confirm: a single memory's substrate migrating across systems on a re-signing schedule.",
   "Confirm: blocking scheduled re-signing erases the trace while blocking replay alone does not.",
   "Refute: a years-long memory with zero systems-level change of substrate.",
   "Refute: molecular turnover preserving information with no re-encoding step."],
  "standards": [
   "Proposed path only; the actual memory code is honestly unmapped.",
   "Does not claim memories are readable like files or that one schedule fits all.",
   "Must not present the covenant model as established neuroscience."],
  "citations": [CIT_MEMORY],
 },
 {
  "key": "pain",
  "name": "Why Pain Lingers",
  "group": "Mind and Brain",
  "ladder_rank": 4, "ladder_tier": "foundations",
  "description": ("Pain is supposed to be an alarm: tissue damage triggers nerves, the brain registers it, "
                  "the tissue heals, the alarm stops. But chronic pain - pain that persists months or years "
                  "after healing - afflicts roughly one in five adults, and its biology is still unsolved. "
                  "The alarm keeps ringing with nothing left to warn about, and medicine still cannot reliably "
                  "silence it."),
  "problem": "Why does pain persist after tissues heal, and what keeps the alarm ringing with nothing to warn about?",
  "background": ("Melzack and Wall's 1965 gate control theory first showed pain is not a simple wire from "
                 "injury to brain - the spinal cord gates the signal. In the 1990s-2000s, Woolf and others "
                 "demonstrated central sensitization: after injury, spinal and brain circuits amplify their own "
                 "gain, so gentle touch registers as pain (allodynia) long after healing. Brain imaging then "
                 "showed chronic pain rewiring emotional and memory circuits - the suffering outliving the "
                 "signal. Yet the field cannot answer the core question: why does sensitization resolve in some "
                 "people and lock in permanently in others, and what molecular switch would flip a sensitized "
                 "circuit back? Opioids dull the alarm without fixing the wiring, which is why the crisis of "
                 "addiction grew out of the mystery of pain."),
  "why_it_matters": ("Chronic pain is among the largest causes of disability and lost work worldwide, and the "
                      "opioid epidemic was born from treating a wiring problem with a volume knob. Solving the "
                      "persistence mechanism would mean real cures - resetting the circuit instead of sedating "
                      "the patient."),
  "sig_lens": ("The Signature lens treats chronic pain as an unsigned alarm: a covenant of protection whose "
               "cancellation notice was never delivered, so the guard keeps shouting at an empty gate."),
  "sol_public": ("The Signature system proposes chronic pain is a stuck gain-control loop - the nervous system "
                 "raised its own amplifier during injury and lost the reset signal, so normal input now reads "
                 "as damage. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) acute pain is a gain-control system, not a wire - spinal and brain "
              "circuits set amplification dynamically; (2) injury raises gain deliberately to protect healing "
              "tissue; (3) a separate reset signal is supposed to lower gain after healing. Reasoning path: "
              "every alarm system needs both a trigger and a stand-down order. Central sensitization is the "
              "trigger side working as designed; chronic pain is the missing stand-down. The reset signal is "
              "probably a slow, activity-dependent process - descending inhibition from the brainstem plus "
              "glial signaling - that verifies 'no damage for X weeks' before lowering gain. In chronic pain, "
              "the verification never completes: either the damage report keeps arriving (ectopic firing from "
              "damaged nerves), the descending brake is weak (genetics, stress, sleep loss), or the circuit "
              "learned the high-gain state as its new normal (long-term potentiation of pain pathways). "
              "Proposed mechanism: treat chronic pain as three stuck loops - peripheral ectopic drive, failed "
              "descending inhibition, and learned spinal amplification - each needing its own reset: silence "
              "ectopic firing, strengthen descending control (which is why exercise, sleep, and some "
              "antidepressants help), and depotentiate the sensitized synapses. What would confirm it: a "
              "measurable gain variable in patients that predicts who transitions from acute to chronic pain, "
              "and targeted resets of each loop producing durable - not merely sedated - relief. What would "
              "kill it: chronic pain with provably normal gain at every level of the neuraxis, or a single "
              "molecular switch that flips all chronic pain off regardless of loop. What it does NOT claim: "
              "that pain is 'all in the head', that any reset protocol is proven, or that this replaces the "
              "need for new non-addictive analgesics. Honest unknown: the identity and timing of the natural "
              "stand-down signal."),
  "key_points": [
   "Gate control theory (1965): the spinal cord gates pain signals; pain is not a simple wire.",
   "Central sensitization: injury raises circuit gain; gentle touch can register as pain after healing.",
   "Chronic pain rewires emotional and memory circuits; suffering outlives the original signal.",
   "Opioids lower perceived volume without resetting the wiring - the root of the addiction crisis.",
   "Core unknown: why sensitization resolves in some people and locks in permanently in others."],
  "requirements": [
   "Confirm: a measurable gain variable predicting acute-to-chronic transition in patients.",
   "Confirm: loop-specific resets producing durable relief, not sedation.",
   "Refute: chronic pain with provably normal gain at every level of the neuraxis.",
   "Refute: a single molecular switch flipping all chronic pain off regardless of loop."],
  "standards": [
   "Proposed path only; no proven reset protocol is claimed.",
   "Never implies pain is imaginary - the gain is physically real in the circuits.",
   "The natural stand-down signal is honestly unidentified."],
  "citations": [CIT_PAIN],
 },
 {
  "key": "aging",
  "name": "Why We Age",
  "group": "The Cell",
  "ladder_rank": 5, "ladder_tier": "foundations",
  "description": ("Aging is the single biggest risk factor for nearly every disease that kills us - cancer, "
                  "heart disease, dementia - yet biology still cannot say why we age. Two camps have argued "
                  "for a century: aging as accumulated damage the body cannot fully repair, versus aging as a "
                  "program, a scheduled decline written into our genes. The 2023 hallmarks of aging list "
                  "twelve mechanisms, but which are causes, which are consequences, and whether any master "
                  "switch exists remain open."),
  "problem": "Why do we age - is aging accumulated damage, a genetic program, or something else entirely?",
  "background": ("Weismann proposed in the 1880s that aging exists to clear generations for evolution's sake. "
                 "Medawar (1952), Williams (1957), and Kirkwood (1977) built the modern evolutionary theories: "
                 "mutation accumulation, antagonistic pleiotropy (genes good early, bad late), and the disposable "
                 "soma theory (the body under-invests in repair because evolution favors reproduction). "
                 "Molecular work then found the hallmarks: genomic instability, telomere shortening, epigenetic "
                 "alterations, loss of proteostasis, disabled macroautophagy, deregulated nutrient sensing, "
                 "mitochondrial dysfunction, cellular senescence, stem cell exhaustion, altered intercellular "
                 "communication, chronic inflammation, and dysbiosis - twelve as of the 2023 update. Interventions "
                 "like rapamycin and senolytics extend mouse lifespan, proving aging is malleable, but no "
                 "intervention has been shown to slow human aging itself, and the field still argues whether the "
                 "hallmarks are twelve separate problems or symptoms of one."),
  "why_it_matters": ("Aging underlies most mortality and most healthcare spending; even a partial answer - a "
                      "way to slow the process rather than treat each disease - would be the largest medical "
                      "advance in history. It is also the gateway question: every longevity claim stands or "
                      "falls on the mechanism of aging."),
  "sig_lens": ("The Signature lens treats aging as a ledger kept in two columns - damage accrued and repair "
               "budgeted - with the body settling the account on evolution's schedule, not ours."),
  "sol_public": ("The Signature system proposes aging is a repair-budget deficit: the body can afford full "
                 "repair only through the reproductive window, after which it pays interest on unrepaired "
                 "damage in twelve compounding currencies. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) repair is energetically expensive and the body has a finite lifetime "
              "energy budget; (2) evolution allocates that budget to maximize reproductive success, not "
              "lifespan; (3) the twelve hallmarks are not twelve diseases but twelve ledgers of the same "
              "unpaid balance. Reasoning path: the disposable soma theory is the skeleton - but it needs "
              "quantitative flesh. Model the body as settling accounts daily: each day posts damage (DNA "
              "lesions, protein misfolds, senescent cells) and spends repair budget (autophagy, DNA repair, "
              "immune clearance). Through the reproductive years the budget covers the damage; afterward, "
              "evolution stops topping up the account, and the unpaid balance compounds across hallmarks - "
              "senescent cells secrete inflammatory signals that damage neighbors, which creates more "
              "senescent cells. This explains why aging looks both programmed (the budget schedule is genetic) "
              "and stochastic (which ledger fails first is chance). Proposed mechanism: interventions work by "
              "either increasing the budget (dietary restriction, exercise) or clearing arrears (senolytics, "
              "autophagy inducers); none reset the schedule itself. What would confirm it: a unified "
              "accounting - a single 'unrepaired damage' metric across hallmarks that predicts mortality "
              "better than chronological age and moves coherently with every lifespan-extending intervention. "
              "What would kill it: a hallmark that progresses independently of all others and of the repair "
              "budget, or a species that ages with zero measurable damage accumulation. What it does NOT claim: "
              "that aging is programmed to kill us on purpose, that any intervention is proven in humans, or "
              "that the ledger can be balanced forever. Honest unknown: the exchange rates between the twelve "
              "ledgers - how much senescence equals how much epigenetic drift."),
  "key_points": [
   "Aging is the top risk factor for cancer, heart disease, and dementia; its mechanism is still debated.",
   "Evolutionary theories: mutation accumulation, antagonistic pleiotropy, disposable soma.",
   "Twelve hallmarks of aging listed as of 2023 - causes vs consequences still argued.",
   "Rapamycin and senolytics extend mouse lifespan; no intervention proven to slow human aging.",
   "Programmed vs damage: the field is split, and both camps have real evidence."],
  "requirements": [
   "Confirm: a unified unrepaired-damage metric predicting mortality better than chronological age.",
   "Confirm: the metric moving coherently with every lifespan-extending intervention.",
   "Refute: a hallmark progressing independently of all others and of repair budget.",
   "Refute: a species aging with zero measurable damage accumulation."],
  "standards": [
   "Proposed path only; no human anti-aging intervention is claimed proven.",
   "Does not claim aging is deliberately programmed death.",
   "Exchange rates between hallmarks are honestly unknown."],
  "citations": [CIT_AGING],
 },
 {
  "key": "lifespan",
  "name": "Why Species Live Different Lengths",
  "group": "Evolution",
  "ladder_rank": 6, "ladder_tier": "foundations",
  "description": ("A mouse lives two years, a bowhead whale over two hundred, and a Greenland shark perhaps "
                  "five hundred - yet all are mammals built from the same basic cells. Biology can describe "
                  "the pattern: bigger animals tend to live longer, and lifespan scales roughly with body mass "
                  "to the quarter power. But why evolution set each species' clock where it did, and what "
                  "mechanism enforces the limit, remains unsolved."),
  "problem": "What sets each species' lifespan - why two years for a mouse and two centuries for a whale?",
  "background": ("The pattern was noted as early as Aristotle; modern scaling work in the 20th century showed "
                 "lifespan scaling with mass to roughly the 1/4 power across mammals. Evolutionary theory says "
                 "lifespan matches the ecological niche: high-predation species like mice cannot afford slow "
                 "aging because few survive to old age anyway, so evolution invests in early reproduction "
                 "instead. The whale poses the famous counter-puzzle - Peto's paradox: with a thousand times "
                 "more cells than a mouse and two centuries to mutate them, whales should drown in cancer, yet "
                 "they do not, implying superior repair or suppression. Bowhead whales carry duplicated DNA "
                 "repair genes; elephants carry extra copies of the tumor suppressor p53. But no one has "
                 "identified the master mechanism that converts 'elephant genome' into 'seventy-year elephant' "
                 "rather than 'two-year elephant', and lifespan has proven stubbornly hard to extend by single "
                 "gene changes."),
  "why_it_matters": ("Species lifespan is nature's own longevity experiment, run billions of times: whatever "
                      "whales and sharks do differently is a working blueprint for slow aging. Reading it would "
                      "give medicine targets no lab could invent from scratch."),
  "sig_lens": ("The Signature lens treats each species' lifespan as a covenant term: evolution signs a "
               "maintenance contract whose length matches the niche, and the genome is the fine print."),
  "sol_public": ("The Signature system proposes lifespan is a maintenance contract priced by predation: "
                 "species pay for exactly as much repair as their niche lets them collect on, and whales are "
                 "rich because their niche is safe. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) every species has a maintenance budget set by its genes; "
              "(2) the budget's length is priced by extrinsic mortality - predation, starvation, accident; "
              "(3) cancer suppression scales with the contract because more cells over more years means more "
              "lottery tickets. Reasoning path: a mouse that will probably be eaten within a year gains nothing "
              "from a fifty-year repair budget, so evolution spends the mouse's energy on early litters. A "
              "whale with almost no predators can collect on a two-century contract, so evolution pays for "
              "duplicated repair genes and extra p53 copies - the premium is worth it. Peto's paradox dissolves: "
              "whales are not lucky, they are insured, and the insurance (repair redundancy) is exactly what "
              "their long contract requires. Body-mass scaling falls out naturally: larger animals tend to have "
              "lower predation, hence longer affordable contracts. Proposed mechanism: lifespan equals the "
              "longest maintenance contract the niche's mortality curve makes profitable; the genome implements "
              "it through repair-gene copy number and redundancy, not a clock. What would confirm it: "
              "transplanting a long-contract repair suite (e.g., whale-like repair redundancy) into a "
              "short-lived mammal and watching lifespan extend proportionally to the redundancy added, and "
              "showing that repair investment across species tracks extrinsic mortality better than it tracks "
              "body mass alone. What would kill it: a high-predation species with lavish repair redundancy, or "
              "a predator-free species that ages fast despite cheap available repair. What it does NOT claim: "
              "that lifespan is consciously 'decided', that humans can simply buy the whale contract, or that "
              "this is established. Honest unknown: the currency conversion - how many extra repair-gene "
              "copies buy how many extra years."),
  "key_points": [
   "Mouse ~2 years, bowhead whale 200+, Greenland shark possibly ~500: same mammalian toolkit, wildly different clocks.",
   "Lifespan scales roughly with body mass to the 1/4 power across mammals.",
   "Peto's paradox: whales should get far more cancer than mice but do not - implying superior suppression.",
   "Elephants carry extra p53 copies; bowheads carry duplicated DNA repair genes.",
   "No single gene change has been shown to set a species' whole lifespan."],
  "requirements": [
   "Confirm: transplanted repair redundancy extending a short-lived mammal's lifespan proportionally.",
   "Confirm: repair investment tracking extrinsic mortality better than body mass alone.",
   "Refute: a high-predation species with lavish repair redundancy.",
   "Refute: a predator-free species aging fast despite cheap available repair."],
  "standards": [
   "Proposed path only; the whale contract cannot simply be bought for humans.",
   "Does not claim lifespan is deliberately decided by any agent.",
   "The repair-copy-to-years conversion rate is honestly unknown."],
  "citations": [CIT_LIFESPAN],
 },
 {
  "key": "regeneration",
  "name": "Why Humans Cannot Regrow Limbs",
  "group": "The Cell",
  "ladder_rank": 7, "ladder_tier": "foundations",
  "description": ("An axolotl can regrow a perfect leg - bone, muscle, nerves, skin - in weeks. A human child "
                  "can regrow a fingertip, but an adult human who loses an arm gets a scar, not a limb. "
                  "Mammals retain the genes for regeneration; salamanders use them and we do not. Why the "
                  "program runs in one vertebrate and stalls in another is one of biology's most practical "
                  "unsolved problems."),
  "problem": "Why can salamanders regrow whole limbs while adult mammals heal the same wound with a scar?",
  "background": ("Regeneration was studied by Spallanzani in the 1700s; the modern era began when researchers "
                 "found that the salamander limb forms a blastema - a mound of dedifferentiated cells at the "
                 "wound that replays embryonic development. Brockes and Kumar's comparative work showed mammals "
                 "possess most of the same signaling pathways (FGF, Wnt, BMP) but deploy them toward fibrosis "
                 "instead. Key differences found so far: salamander immune response is muted and pro-regenerative "
                 "(macrophages required; deplete them and regeneration fails), their cells readily dedifferentiate, "
                 "and they avoid the scar-forming fibroblast program. Mouse digit tips regenerate in neonates "
                 "but lose the ability within weeks of birth. The field has the parts list but not the "
                 "switch: what tells a mammalian wound 'scar' instead of 'rebuild'?"),
  "why_it_matters": ("The answer is regenerative medicine itself: regrowing limbs, spinal cords, and hearts "
                      "instead of transplanting or prosthetizing them. Every year of delay is measured in "
                      "amputations and organ waiting lists."),
  "sig_lens": ("The Signature lens treats regeneration as a covenant the salamander kept and mammals broke: "
               "the wound signs either a rebuilding contract or a scarring contract, and mammals default to "
               "the cheaper one."),
  "sol_public": ("The Signature system proposes mammals chose the scarring contract for speed: a fast scar "
                 "seals a wound before infection in a microbe-rich world, and the price is the lost limb - "
                 "while salamanders, in cleaner water, could afford the slow rebuilding contract. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) wound healing is a race between sealing (scar) and rebuilding "
              "(blastema); (2) infection risk sets the deadline - an open wound in a microbe-rich environment "
              "must close fast; (3) mammals and salamanders face different deadlines. Reasoning path: mammals "
              "evolved as warm, microbe-laden animals where an open limb wound invites lethal infection within "
              "days; the scarring program closes the wound in hours. Salamanders live in cool water with lower "
              "microbial pressure and slower metabolism, so they can afford the weeks-long blastema program. "
              "The mammalian 'switch' is therefore not a missing gene but a triage decision: fibroblasts are "
              "recruited first and lay down collagen before dedifferentiation can organize, and the immune "
              "system - tuned for aggressive pathogen clearance - actively suppresses the pro-regenerative "
              "macrophage state. This explains why neonate mammals (sterile-ish womb, immature immunity) can "
              "still regenerate digit tips and lose the ability as immunity matures. Proposed mechanism: "
              "regeneration fails in mammals because of a three-lock sequence - fast fibroblast sealing, "
              "inflammatory macrophage dominance, and epigenetic locking of differentiated state - and unlocking "
              "requires all three addressed in order: delay the scar, retune the macrophages, then supply the "
              "developmental signals. What would confirm it: a mammalian wound protocol that sequentially "
              "delays fibrosis, shifts macrophages to the pro-regenerative state, and applies FGF/Wnt patterning "
              "producing jointed regrowth rather than scar. What would kill it: a mammal regenerating a limb "
              "with full aggressive scarring intact, or a salamander failing to regenerate in sterile conditions "
              "despite an open wound window. What it does NOT claim: that limb regrowth in humans is around the "
              "corner, that any protocol is proven, or that infection risk is the whole story. Honest unknown: "
              "the exact molecular identity of the triage signal that commits a wound to scar."),
  "key_points": [
   "Axolotls regrow complete limbs in weeks via a blastema that replays development.",
   "Mammals use the same pathways (FGF, Wnt, BMP) but deploy them toward scar-forming fibrosis.",
   "Salamander macrophages are required for regeneration; depleting them blocks it.",
   "Neonate mice regenerate digit tips but lose the ability within weeks as immunity matures.",
   "The field has the parts list but not the switch: scar versus rebuild."],
  "requirements": [
   "Confirm: a sequential mammalian protocol (delay scar, retune macrophages, pattern signals) yielding jointed regrowth.",
   "Confirm: the triage signal's molecular identity and its timing in wound healing.",
   "Refute: mammalian limb regrowth with full aggressive scarring left intact.",
   "Refute: salamander regeneration failing in sterile conditions despite an open wound window."],
  "standards": [
   "Proposed path only; no human limb-regrowth protocol is claimed or near.",
   "Does not claim infection pressure is the entire explanation.",
   "The triage signal's identity is honestly unknown."],
  "citations": [CIT_REGEN],
 },
 {
  "key": "immunity",
  "name": "How Immunity Tells Friend From Foe",
  "group": "Immunity and Microbes",
  "ladder_rank": 8, "ladder_tier": "foundations",
  "description": ("The immune system faces an impossible classification problem: among trillions of molecules, "
                  "attack the pathogens and the cancers while sparing every healthy cell of the body - and it "
                  "gets it right almost every time. When it fails, the result is autoimmune disease or "
                  "unchecked infection. How a system with no central commander achieves near-perfect "
                  "self/non-self discrimination is still not fully understood."),
  "problem": "How does the immune system reliably distinguish self from non-self with no central commander?",
  "background": ("Burnet's clonal selection theory (1957) gave the framework: each lymphocyte carries one "
                 "receptor, and self-reactive ones are deleted during development. Janeway's 1989 insight added "
                 "the innate system: pattern-recognition receptors detect conserved microbial features "
                 "(PAMPs) and damage signals, giving the adaptive system its context. Matzinger's danger model "
                 "(1994) argued the real distinction is not self/non-self but damage/non-damage. Central "
                 "tolerance in the thymus deletes most self-reactive T cells, and regulatory T cells suppress "
                 "the escapees. Yet puzzles persist: the gut hosts trillions of foreign microbes unmolested, "
                 "pregnancy tolerates a half-foreign fetus, and autoimmune diseases strike when discrimination "
                 "slips for reasons still unclear. The system has overlapping theories but no unified account "
                 "of how the decision is computed in real tissue."),
  "why_it_matters": ("Autoimmune diseases afflict roughly one in ten people, and every vaccine, transplant, "
                      "and cancer immunotherapy is an attempt to steer this discrimination. A unified theory "
                      "would mean designing tolerance and attack on demand."),
  "sig_lens": ("The Signature lens treats immunity as a border covenant: every cell must present its papers "
               "continuously, and the guards are trained by seeing the citizenry first."),
  "sol_public": ("The Signature system proposes discrimination is continuous re-authentication, not a "
                 "one-time passport check: cells constantly present identity papers, and attack requires "
                 "multiple independent alarms agreeing. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) no single signal is trustworthy - pathogens mimic self and damaged "
              "self mimics danger; (2) the system therefore requires coincidence: several weak signals must "
              "agree before attack; (3) the threshold for agreement is set during development by exposure to "
              "the body's own molecules. Reasoning path: a border guard who shoots on one suspicious paper "
              "will kill citizens; a guard who requires three independent alarms will rarely err. The immune "
              "system is the second kind: T cells need antigen plus co-stimulation plus cytokine context; "
              "innate sensors need microbial patterns plus damage signals. Self-tolerance is then not a list "
              "of forbidden targets but a calibration - the thymus shows developing T cells the full citizenry "
              "so their activation thresholds are set above the background of self. The gut and the fetus are "
              "not exceptions but special jurisdictions where the alarm threshold is deliberately raised "
              "(regulatory T cells, placental barriers) because the cost of false attack exceeds the cost of "
              "missed detection. Autoimmunity is threshold drift: chronic damage signals or molecular mimicry "
              "pushing the coincidence detector past its set point. Proposed mechanism: discrimination equals "
              "calibrated coincidence detection with tissue-specific thresholds, continuously re-set by "
              "regulatory networks. What would confirm it: measuring per-tissue activation thresholds in vivo "
              "and showing autoimmune onset coinciding with measurable threshold drift before any tissue "
              "damage, plus therapies that re-calibrate thresholds producing durable tolerance. What would "
              "kill it: a proven single-signal discriminator that alone decides attack versus tolerance, or "
              "autoimmunity arising with provably intact thresholds and coincidence logic. What it does NOT "
              "claim: that the danger model or self/non-self model is wrong - both describe parts of the "
              "coincidence logic - or that threshold therapy exists today. Honest unknown: how thresholds are "
              "encoded and inherited across immune cell generations."),
  "key_points": [
   "Clonal selection (1957): one receptor per lymphocyte; self-reactive clones deleted in development.",
   "Innate pattern recognition (Janeway) and the danger model (Matzinger) added context to the decision.",
   "Thymic central tolerance plus regulatory T cells suppress most self-attack.",
   "The gut microbiome and the fetus are tolerated despite being foreign - thresholds vary by tissue.",
   "No unified account yet of how the attack/tolerate decision is computed in real tissue."],
  "requirements": [
   "Confirm: per-tissue activation thresholds measurable in vivo, drifting before autoimmune onset.",
   "Confirm: threshold re-calibration therapies producing durable tolerance.",
   "Refute: a single signal proven to decide attack versus tolerance alone.",
   "Refute: autoimmunity arising with provably intact thresholds and coincidence logic."],
  "standards": [
   "Proposed path only; it absorbs rather than replaces existing models.",
   "No threshold therapy is claimed to exist today.",
   "Threshold encoding across cell generations is honestly unknown."],
  "citations": [CIT_IMMUNITY],
 },
 {
  "key": "cellfate",
  "name": "How Cells Choose Their Fate",
  "group": "The Cell",
  "ladder_rank": 9, "ladder_tier": "foundations",
  "description": ("Every cell in your body carries the same genome, yet a neuron and a skin cell read it as "
                  "entirely different instruction books. During development, identical stem cells commit to "
                  "hundreds of fates - irreversibly, in the right place, at the right time. Yamanaka showed "
                  "in 2006 that four factors can reverse the choice, proving fate is a state, not a destiny. "
                  "But what computes the choice, and what locks it in, is still unsolved."),
  "problem": "How does a cell with the full genome choose one fate out of hundreds - and what locks the choice?",
  "background": ("Waddington's 1957 epigenetic landscape pictured development as a ball rolling down branching "
                 "valleys - fate as a landscape of attractors. Molecular biology filled in transcription "
                 "factors: master regulators like MyoD can convert fibroblasts to muscle, and the Yamanaka "
                 "factors (Oct4, Sox2, Klf4, c-Myc) reprogram adult cells to pluripotency, winning the 2012 "
                 "Nobel Prize. Single-cell sequencing now maps the valleys in exquisite detail, showing fate "
                 "decisions as bifurcations in gene-expression space. Yet the computation remains mysterious: "
                 "how does a cell integrate dozens of noisy signals into one crisp, irreversible decision, and "
                 "why do some fates reprogram easily while others resist? The landscape is mapped; the "
                 "dynamics that roll the ball are still being worked out."),
  "why_it_matters": ("Every regenerative therapy - growing insulin cells for diabetics, dopamine neurons for "
                      "Parkinson's - is an attempt to command cell fate on demand. Reliable fate control would "
                      "turn transplantation from donor-limited surgery into manufacturing."),
  "sig_lens": ("The Signature lens treats cell fate as a covenant signed in chromatin: the cell swears to one "
               "reading of the genome, and the signature is written in chemical marks that outlast the moment."),
  "sol_public": ("The Signature system proposes fate is a locked attractor: gene-regulatory circuits with "
                 "positive feedback create stable valleys, and chromatin marks are the padlocks that keep the "
                 "cell from climbing out. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) fate decisions are made by small gene-regulatory circuits with "
              "positive feedback (toggle switches), not by the whole genome at once; (2) feedback creates "
              "attractors - stable states the cell falls into and cannot easily leave; (3) chromatin "
              "modifications are the lock, not the decision. Reasoning path: a toggle switch of two mutually "
              "repressing transcription factors has exactly two stable states - this is the valley's floor. "
              "Noisy developmental signals tilt the switch; once flipped, positive feedback holds it flipped "
              "even after the signal fades - this is irreversibility. Chromatin marks (methylation, histone "
              "modifications) then padlock the losing genes shut, which is why differentiated cells resist "
              "reprogramming: the Yamanaka factors must pick four specific locks. Fate hierarchies are "
              "cascades of such switches, each narrowing the options - Waddington's valleys as circuits. "
              "Proposed mechanism: differentiation equals sequential toggle-flipping with chromatin padlocking; "
              "reprogramming equals lock-picking in reverse order. What would confirm it: predicting a cell's "
              "reprogramming difficulty purely from its chromatin-lock inventory, and flipping fates at will "
              "by targeting the specific toggle circuits rather than brute-force factor cocktails. What would "
              "kill it: fate decisions with no identifiable toggle circuit and no feedback stabilization, or "
              "cells that hold fate with zero chromatin change. What it does NOT claim: that every fate is "
              "fully mapped, that reprogramming is safe (c-Myc is oncogenic), or that this is established. "
              "Honest unknown: the full wiring diagram - which toggles, in which order, for most of the "
              "hundreds of human cell types."),
  "key_points": [
   "Same genome, hundreds of fates: fate is a regulatory state, not a different genome.",
   "Waddington (1957): development as a ball rolling down branching valleys - attractors.",
   "Yamanaka factors (2006) reprogram adult cells to pluripotency (Nobel 2012) - fate is reversible in principle.",
   "Master regulators (e.g., MyoD) can switch fates; single-cell sequencing maps the valleys.",
   "Open: how noisy signals integrate into one crisp irreversible decision."],
  "requirements": [
   "Confirm: reprogramming difficulty predicted purely from a cell's chromatin-lock inventory.",
   "Confirm: on-demand fate flips by targeting specific toggle circuits.",
   "Refute: fate decisions with no toggle circuit and no feedback stabilization.",
   "Refute: cells holding fate with zero chromatin change."],
  "standards": [
   "Proposed path only; most human fate circuits are unmapped.",
   "Does not claim reprogramming is safe - oncogenic risk is real.",
   "The full toggle wiring diagram is honestly unknown."],
  "citations": [CIT_CELLFATE],
 },
]

CIT_DEVO = ("Wolpert L. Positional information and the spatial pattern of cellular differentiation. "
            "J Theor Biol. 1969;25:1-47; Nusslein-Volhard C, Wieschaus E. Mutations affecting segment "
            "number and polarity in Drosophila. Nature. 1980;287:795-801.")
CIT_MICROBIOME = ("Turnbaugh PJ et al. The human microbiome project. Nature. 2007;449:804-810; "
                  "Gilbert JA et al. Current understanding of the human microbiome. Nat Med. "
                  "2018;24:392-400.")
CIT_PREGNANCY = ("Medawar PB. Some immunological and endocrinological problems raised by the evolution "
                 "of viviparity in vertebrates. Symp Soc Exp Biol. 1953;7:320-338; Erlebacher A. "
                 "Immunology of the maternal-fetal interface. Annu Rev Immunol. 2013;31:387-411.")
CIT_CANCER = ("Hanahan D, Weinberg RA. Hallmarks of cancer: the next generation. Cell. "
              "2011;144:646-674; Hanahan D. Hallmarks of cancer: new dimensions. Cancer Discov. "
              "2022;12:31-46.")
CIT_REJUV = ("Ocampo A et al. In vivo amelioration of age-associated hallmarks by partial "
             "reprogramming. Cell. 2016;167:1719-1733; Horvath S. DNA methylation age of human "
             "tissues and cell types. Genome Biol. 2013;14:R115.")
CIT_CONSC = ("Crick F, Koch C. Towards a neurobiological theory of consciousness. Semin Neurosci. "
             "1990;2:263-275; Tononi G et al. Integrated information theory: from consciousness to "
             "its physical substrate. Nat Rev Neurosci. 2016;17:450-461.")
CIT_NEURALCODE = ("Adrian ED. The Basis of Sensation. Christophers; 1928; Rieke F et al. Spikes: "
                  "Exploring the Neural Code. MIT Press; 1997.")
CIT_FOLDING = ("Anfinsen CB. Principles that govern the folding of protein chains. Science. "
               "1973;181:223-230; Jumper J et al. Highly accurate protein structure prediction with "
               "AlphaFold. Nature. 2021;596:583-589.")
CIT_DARKGENOME = ("ENCODE Project Consortium. An integrated encyclopedia of DNA elements in the human "
                  "genome. Nature. 2012;489:57-74; Doolittle WF. Is junk DNA bunk? A critique of ENCODE. "
                  "Proc Natl Acad Sci USA. 2013;110:5294-5300.")

ENTRIES += [
 {
  "key": "embryo",
  "name": "How Embryos Build Bodies",
  "group": "Development",
  "ladder_rank": 10, "ladder_tier": "foundations",
  "description": ("A fertilized egg - one cell, no map, no architect - divides into trillions of cells that "
                  "arrange themselves into a brain, a heart, fingers, and eyes, in the right places, at the "
                  "right time, with near-perfect reliability. Developmental biology has named many of the "
                  "signals, but how local cells with only local information build a global body plan remains "
                  "unsolved."),
  "problem": "How do cells with only local information reliably build a complete, correctly proportioned body?",
  "background": ("Wolpert's 1969 French flag model proposed the answer: cells read their position from "
                 "morphogen gradients - chemical concentrations that tell each cell where it is. "
                 "Nusslein-Volhard and Wieschaus (Nobel 1995) found the genes that stripe the fly embryo, "
                 "proving patterning is genetic and decipherable. Turing's 1952 reaction-diffusion mathematics "
                 "showed how spots and stripes self-organize from uniformity. Modern imaging watches gradients "
                 "form in living embryos with stunning precision. Yet the deep puzzles persist: gradients are "
                 "noisy, but bodies are precise - how is the noise filtered? Embryos scale patterns to size "
                 "(a half embryo makes a half-size whole), which simple gradient-reading cannot explain. And "
                 "nobody knows how the genome's one-dimensional code unfolds into reliable three-dimensional "
                 "construction without a supervisor."),
  "why_it_matters": ("Birth defects are patterning errors; understanding the program means preventing and "
                      "repairing them, and it is the prerequisite for growing organs - construction without a "
                      "foreman is the most advanced manufacturing on Earth."),
  "sig_lens": ("The Signature lens treats the embryo as a covenant of construction: every cell swears to "
               "read its position honestly, and the body is what honest local readings add up to."),
  "sol_public": ("The Signature system proposes embryos build by error-corrected consensus: cells do not "
                 "just read gradients, they compare notes with neighbors and average out the noise, and "
                 "scaling comes from feedback that re-zeros the map to the embryo's actual size. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) no cell sees the whole embryo - all information is local; "
              "(2) morphogen gradients are noisy readouts; (3) the final body is precise, so error correction "
              "must exist. Reasoning path: a single cell reading a noisy gradient is like one witness guessing "
              "a distance - unreliable. But cells talk: gap junctions and contact signaling let neighborhoods "
              "average their readings, and averaging N noisy measurements cuts error by the square root of N. "
              "Precision is therefore a collective achievement, not an individual one. Scaling is solved by "
              "feedback: downstream pattern genes report back to the gradient source, re-zeroing the map until "
              "it matches the embryo's real size - a control loop, not a fixed ruler. Robustness comes from "
              "redundancy: multiple overlapping gradients vote, so no single failure misplaces an organ. "
              "Proposed mechanism: patterning equals noisy gradient reading plus neighbor-averaging plus "
              "feedback re-zeroing plus redundant voting. What would confirm it: measuring gradient noise and "
              "neighbor-coupling in a living embryo and showing the final pattern is precisely as accurate as "
              "the averaging math predicts - no more, no less - and breaking the feedback loop destroying "
              "size-scaling while leaving gradient reading intact. What would kill it: embryos achieving "
              "precision with provably no cell-cell averaging, or scaling without any feedback from pattern "
              "to gradient. What it does NOT claim: that the full program is decoded, that this is "
              "established, or that noise is the only problem. Honest unknown: the complete parts list of "
              "the averaging and feedback circuits in any vertebrate."),
  "key_points": [
   "One cell with no map reliably builds trillions of cells into a correct body.",
   "Wolpert (1969): cells read position from morphogen gradients - the French flag model.",
   "Fly patterning genes found (Nobel 1995); Turing (1952) showed self-organizing patterns mathematically.",
   "Gradients are noisy but bodies are precise; embryos scale patterns to their size.",
   "Open: how noise is filtered and how one-dimensional code becomes 3D construction."],
  "requirements": [
   "Confirm: final pattern accuracy matching neighbor-averaging math exactly in a living embryo.",
   "Confirm: breaking pattern-to-gradient feedback destroying size-scaling specifically.",
   "Refute: embryonic precision with provably no cell-cell averaging.",
   "Refute: size-scaling with provably no feedback from pattern to gradient."],
  "standards": [
   "Proposed path only; the full vertebrate circuit list is unmapped.",
   "Does not claim the program is decoded or that noise is the only problem.",
   "Averaging and feedback circuits are honestly incomplete."],
  "citations": [CIT_DEVO],
 },
 {
  "key": "microbiome",
  "name": "How the Microbiome Shapes Health",
  "group": "Immunity and Microbes",
  "ladder_rank": 11, "ladder_tier": "foundations",
  "description": ("Your body carries roughly as many microbial cells as human cells, and their genes outnumber "
                  "yours a hundred to one. The microbiome is linked to obesity, diabetes, depression, autism, "
                  "and immunity - yet almost every link is a correlation. Whether microbes cause disease, "
                  "merely reflect it, or both, is the great unsolved causal question of modern medicine."),
  "problem": "Does the microbiome cause disease and health, or does it merely reflect them?",
  "background": ("The Human Microbiome Project (2007) and cheap sequencing revealed the body's microbial "
                 "ecosystems in full: gut, skin, mouth, each a rainforest. Study after study then linked "
                 "microbial patterns to conditions - obese versus lean microbiomes, depressed versus healthy "
                 "ones. Fecal transplants curing Clostridioides difficile infection proved microbes can be "
                 "medicine. But the causal arrow stays blurry: diet, drugs, and disease all reshape the "
                 "microbiome, so a 'disease microbiome' may be the disease's shadow. Germ-free mouse "
                 "experiments show microbial effects on immunity and behavior, yet translating any of it into "
                 "reliable human therapy has largely failed. The field has magnificent correlations and "
                 "almost no settled causal chains from microbe to mechanism to disease."),
  "why_it_matters": ("If causality is real and mappable, the microbiome becomes a programmable organ: "
                      "treatments for metabolic, immune, and mental conditions made of living ecosystems "
                      "rather than single molecules. If it is mostly reflection, billions in probiotic hype "
                      "need redirecting."),
  "sig_lens": ("The Signature lens treats the microbiome as a covenant partner: a second genome the body "
               "did not write but signed a treaty with, and health is the treaty holding."),
  "sol_public": ("The Signature system proposes the microbiome is a treaty ecosystem: health is the stable "
                 "contract between host and microbes, disease is treaty breakdown, and causation runs both "
                 "ways through the treaty's terms. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) host and microbes co-evolved a negotiated peace, not a conquest; "
              "(2) the terms are chemical - metabolites, immune signals, barrier integrity; (3) correlation "
              "dominates because most studies photograph the treaty after it broke. Reasoning path: stop "
              "asking 'which microbe causes which disease' and ask 'which treaty term broke'. A healthy gut "
              "treaty has terms: microbes get fiber, host gets short-chain fatty acids and immune training, "
              "both maintain the mucus barrier. Antibiotics, low-fiber diets, or inflammation break terms; "
              "the ecosystem re-stabilizes at a new, worse equilibrium - dysbiosis. The new equilibrium then "
              "actively maintains disease (inflammatory metabolites, leaky barrier), which is why causation "
              "looks bidirectional: the treaty broke first (correlation), then the new treaty enforces "
              "disease (causation). Fecal transplant works because it re-signs the original treaty wholesale. "
              "Proposed mechanism: health equals treaty stability; therapy equals treaty renegotiation - "
              "identify the broken term (missing metabolite, breached barrier, lost keystone species) and "
              "restore that term rather than adding random microbes. What would confirm it: longitudinal "
              "tracking showing specific treaty terms breaking before disease onset, and term-targeted "
              "restoration preventing disease while generic probiotics fail. What would kill it: diseases "
              "with fully healthy treaty terms by every measure, or term restoration that never changes "
              "outcomes. What it does NOT claim: that any specific probiotic works, that the treaty is fully "
              "mapped, or that this is established. Honest unknown: the complete text of the treaty - most "
              "microbial metabolites and their host receptors are unidentified."),
  "key_points": [
   "Microbial cells roughly equal human cells; microbial genes outnumber human genes ~100 to 1.",
   "Microbiome linked to obesity, diabetes, depression, immunity - nearly all links correlational.",
   "Fecal transplant cures C. difficile: proof microbes can be medicine.",
   "Diet, drugs, and disease reshape the microbiome - the causal arrow is blurry.",
   "Germ-free mice show real microbial effects; human translation has largely failed."],
  "requirements": [
   "Confirm: specific treaty terms breaking before disease onset in longitudinal tracking.",
   "Confirm: term-targeted restoration preventing disease where generic probiotics fail.",
   "Refute: disease with fully healthy treaty terms by every measure.",
   "Refute: term restoration that never changes outcomes."],
  "standards": [
   "Proposed path only; no specific probiotic efficacy is claimed.",
   "The treaty's full text is honestly unmapped.",
   "Correlation is not dismissed - it is explained as post-breakdown photography."],
  "citations": [CIT_MICROBIOME],
 },
 {
  "key": "pregnancy",
  "name": "Why Pregnancy Is Not Rejected",
  "group": "Immunity and Microbes",
  "ladder_rank": 12, "ladder_tier": "foundations",
  "description": ("A fetus is half foreign - it carries the father's genes, which the mother's immune system "
                  "should recognize as non-self and attack, exactly as it attacks a transplanted organ. Yet "
                  "pregnancy normally proceeds for nine months without rejection. Medawar called it the "
                  "immunological paradox of pregnancy in 1953, and it is still not fully resolved."),
  "problem": "Why does the mother's immune system tolerate a half-foreign fetus for nine months?",
  "background": ("Medawar's 1953 lecture framed the paradox and proposed three explanations: the fetus is "
                 "antigenically immature, the mother is immunosuppressed, or the placenta is a barrier. All "
                 "three proved partly wrong: the placenta expresses foreign antigens, the mother is not "
                 "globally immunosuppressed, and the barrier leaks fetal cells routinely. Modern work found a "
                 "specialized local truce: placental trophoblast cells display unusual HLA-G instead of "
                 "classical HLA, regulatory T cells expand massively, and the decidua is packed with unusual "
                 "natural killer cells that help build blood vessels instead of killing. Yet no one can fully "
                 "explain why the truce holds in most pregnancies and fails in preeclampsia or miscarriage, or "
                 "how tolerance is switched off after birth so the mother regains full immune function."),
  "why_it_matters": ("Preeclampsia and recurrent miscarriage devastate millions of families yearly with no "
                      "real treatment; the placenta's trick, once decoded, is also the blueprint for "
                      "transplant tolerance without lifelong immunosuppression."),
  "sig_lens": ("The Signature lens treats pregnancy as a nine-month covenant: two immune systems signing a "
               "temporary treaty with an expiration date, honored locally and dissolved on schedule."),
  "sol_public": ("The Signature system proposes the placenta is a special jurisdiction: tolerance is not "
                 "global immunosuppression but a locally negotiated treaty with a built-in expiry, enforced "
                 "by dedicated regulatory cells. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the immune system can set different thresholds in different "
              "tissues; (2) pregnancy exploits this by declaring the placenta a special jurisdiction; "
              "(3) the treaty must self-dissolve at birth. Reasoning path: Medawar's three ideas each failed "
              "because they were global; the answer is local. The placenta negotiates its own terms: "
              "trophoblasts present HLA-G, a 'do not attack' dialect the mother's NK cells are trained to "
              "respect; regulatory T cells specific to paternal antigens expand and patrol the decidua; "
              "tryptophan-catabolizing enzymes starve would-be attacker T cells locally. The rest of the "
              "mother's body stays fully defended - she fights infections normally. The expiry is hormonal: "
              "the same signals that initiate labor dismantle the regulatory infrastructure, so tolerance "
              "ends on schedule. Preeclampsia and miscarriage are treaty failures - shallow trophoblast "
              "invasion means the jurisdiction was never properly established. Proposed mechanism: tolerance "
              "equals a locally negotiated, hormonally expiring immune treaty, not systemic suppression. What "
              "would confirm it: mapping the full treaty terms (signals, cell types, timing) and showing "
              "treaty-establishment metrics in the first trimester predicting preeclampsia, plus inducing an "
              "analogous local treaty around a transplanted organ. What would kill it: rejection-free "
              "pregnancy with provably no local regulatory specialization, or systemic immunosuppression "
              "proven necessary. What it does NOT claim: that every miscarriage is immune-mediated, that a "
              "transplant treaty exists today, or that this is established. Honest unknown: the complete "
              "signal inventory of the treaty and what first breaks in preeclampsia."),
  "key_points": [
   "The fetus is half foreign; the mother's immune system should reject it like a transplant - Medawar's paradox (1953).",
   "Medawar's three global explanations all proved partly wrong; the answer is local.",
   "Placental cells display unusual HLA-G; regulatory T cells expand; decidual NK cells build vessels instead of killing.",
   "The mother is not globally immunosuppressed - she fights infections normally.",
   "Open: why the truce fails in preeclampsia and miscarriage, and how it dissolves after birth."],
  "requirements": [
   "Confirm: first-trimester treaty-establishment metrics predicting preeclampsia.",
   "Confirm: an analogous local treaty induced around a transplanted organ.",
   "Refute: rejection-free pregnancy with provably no local regulatory specialization.",
   "Refute: systemic immunosuppression proven necessary for fetal survival."],
  "standards": [
   "Proposed path only; no transplant treaty exists today.",
   "Does not claim every miscarriage is immune-mediated.",
   "The treaty's full signal inventory is honestly unmapped."],
  "citations": [CIT_PREGNANCY],
 },
 {
  "key": "cancer",
  "name": "What Cancer Really Is",
  "group": "The Cell",
  "ladder_rank": 13, "ladder_tier": "compounded",
  "description": ("We have named cancer's hallmarks, sequenced its genomes, and built immunotherapies - yet "
                  "cancer still kills ten million people a year, and the deepest questions are open. Why do "
                  "some tissues get cancer constantly and others almost never? Why do metastases home to "
                  "specific organs? Is cancer a genetic disease, a tissue-organization disease, or an "
                  "evolutionary process wearing a disease's mask? The full picture is still missing."),
  "problem": "What is cancer, fundamentally - and why does the full picture of its origin, spread, and resistance still elude us?",
  "background": ("The somatic mutation theory - cancer as accumulated mutations - dominated since the 1970s "
                 "and was codified in Hanahan and Weinberg's hallmarks papers (2000, 2011, 2022): sustaining "
                 "proliferation, evading suppressors, resisting death, enabling immortality, inducing blood "
                 "vessels, activating invasion, reprogramming metabolism, avoiding immunity. Trillion-dollar "
                 "sequencing confirmed mutations but also embarrassed the theory: healthy tissues carry "
                 "thousands of 'cancer' mutations without becoming cancer, and some tumors have few mutations. "
                 "The tissue organization field theory counters that cancer is a breakdown of tissue "
                 "architecture, with mutations as passengers. Meanwhile therapy keeps meeting evolution: "
                 "tumors are heterogeneous populations that evolve resistance to nearly everything, and "
                 "metastasis - the actual killer in 90 percent of cases - remains the least understood step."),
  "why_it_matters": ("Ten million deaths a year, and most therapies still fail against metastatic, resistant "
                      "disease. The right fundamental picture decides whether the next fifty years bring "
                      "incremental drugs or actual cures."),
  "sig_lens": ("The Signature lens treats cancer as a broken covenant of the multicellular contract: cells "
               "that stop paying the cooperation tax and start running their own ledger."),
  "sol_public": ("The Signature system proposes cancer is defection from the multicellular contract: "
                 "mutations are the excuse, but the crime is a cell abandoning cooperation - and the "
                 "contract's enforcers (tissue architecture, immunity) are the real battleground. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) multicellularity is a cooperation contract - cells surrender "
              "independent reproduction for the body's benefit; (2) defection is always tempting and always "
              "arising; (3) the body therefore runs layered enforcement, not just mutation prevention. "
              "Reasoning path: view tissues as societies. Mutations happen constantly (healthy skin carries "
              "them by the thousand) - they are failed defections, suppressed by enforcement: tissue "
              "architecture that denies rogue cells space and signals, immune surveillance that kills "
              "defectors, and programmed cell death as the honorable exit. Cancer begins when enforcement "
              "fails at multiple layers simultaneously - which is why it takes decades and multiple hits, and "
              "why tissues with high turnover and strong architecture (small intestine) resist while others "
              "succumb. Metastasis is defection going mobile: cells that learn to survive without their "
              "tissue's permission, homing to organs whose enforcement is weakest. Therapy resistance is "
              "evolution doing its job: treatment is a selection pressure, and heterogeneous tumors always "
              "contain a defector that survives it. Proposed mechanism: prevent and treat cancer by "
              "reinforcing the contract's enforcers - restore tissue architecture, re-arm immune "
              "surveillance, close the ecological niches defectors exploit - rather than only hunting "
              "mutations. What would confirm it: interventions that strengthen tissue-level enforcement "
              "reducing cancer incidence without touching mutation rates, and metastasis predicted by "
              "enforcement weakness of target organs better than by tumor genetics. What would kill it: "
              "cancers arising and progressing with provably intact enforcement at every layer, or mutation "
              "profiles alone fully predicting behavior. What it does NOT claim: that mutations do not "
              "matter, that any enforcement therapy is proven, or that this is established. Honest unknown: "
              "the complete inventory of enforcement layers and which fails first in each cancer type."),
  "key_points": [
   "Ten million cancer deaths yearly; metastasis causes ~90 percent of them and is the least understood step.",
   "Hallmarks papers (2000/2011/2022) codified the mutation-centered view.",
   "Healthy tissues carry thousands of cancer-associated mutations without becoming cancer.",
   "Tissue organization theory: cancer as architecture breakdown, mutations as passengers.",
   "Therapy resistance is evolution: heterogeneous tumors always contain a surviving defector."],
  "requirements": [
   "Confirm: enforcement-strengthening interventions cutting incidence without changing mutation rates.",
   "Confirm: metastasis sites predicted by target-organ enforcement weakness over tumor genetics.",
   "Refute: cancers arising with provably intact enforcement at every layer.",
   "Refute: mutation profiles alone fully predicting tumor behavior."],
  "standards": [
   "Proposed path only; no enforcement therapy is claimed proven.",
   "Does not dismiss the role of mutations.",
   "The enforcement-layer inventory is honestly incomplete."],
  "citations": [CIT_CANCER],
 },
 {
  "key": "rejuvenation",
  "name": "Whether Aging Can Be Reversed",
  "group": "The Cell",
  "ladder_rank": 14, "ladder_tier": "compounded",
  "description": ("In 2006 Yamanaka showed adult cells could be reprogrammed to youth; in 2016 partial "
                  "reprogramming extended lifespan in prematurely aging mice. Blood from young mice seems to "
                  "rejuvenate old tissues. Yet no intervention has been shown to reverse human aging, and every "
                  "rejuvenation trick flirts with cancer - the same pathways that renew also unleash. Whether "
                  "aging can actually be turned back, rather than merely slowed, is wide open."),
  "problem": "Can aging be reversed - not just slowed - without unleashing cancer?",
  "background": ("Heterochronic parabiosis - joining young and old mouse circulations - has suggested "
                 "rejuvenating blood factors since the 1970s, revived in the 2000s by Conboy and Rando. "
                 "Horvath's 2013 epigenetic clock gave aging a measurable dial: DNA methylation patterns that "
                 "predict biological age. Ocampo's 2016 partial reprogramming - briefly expressing Yamanaka "
                 "factors without full dedifferentiation - rolled back epigenetic age and extended lifespan in "
                 "progeria mice, launching the rejuvenation industry. But full reprogramming causes teratomas; "
                 "partial reprogramming's safety window is unproven; young-blood factors (GDF11 and others) "
                 "have seesawed between miracle and artifact; and the epigenetic clock can be fooled - "
                 "changing the readout is not the same as changing aging. The field has dials it can move and "
                 "no proof any of them is the aging process itself."),
  "why_it_matters": ("Reversal versus slowing is the difference between managing decline and restoring youth: "
                      "trillions in healthcare, and the entire longevity industry's credibility, hang on which "
                      "is real."),
  "sig_lens": ("The Signature lens treats rejuvenation as re-signing the covenant of youth: the cell's "
               "original signature is still on file in the epigenome, and the question is whether it can be "
               "re-authenticated without forging it."),
  "sol_public": ("The Signature system proposes aging's information is not lost but misfiled: the youthful "
                 "epigenetic signature persists underneath, and partial reprogramming works by re-authenticating "
                 "it - the danger is re-signing too aggressively and authenticating cancer instead. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the genome is unchanged by aging - only its reading changes; "
              "(2) the youthful reading pattern is therefore still encodable; (3) cancer is what happens "
              "when reprogramming overshoots into uncontrolled plasticity. Reasoning path: Sinclair's "
              "information theory of aging frames this precisely - aging is loss of epigenetic information, "
              "not genetic damage. If the information is merely misfiled rather than destroyed, reversal is "
              "a restoration problem: re-present the youthful filing system and the cell re-files itself. "
              "Partial reprogramming is a controlled re-filing: brief Yamanaka expression loosens the "
              "epigenetic locks just enough for the cell to re-settle into its youthful pattern, then stops "
              "before pluripotency. The cancer risk is the overshoot: full loosening lets cells settle "
              "anywhere, including malignancy. The safety window is therefore a dosing problem - pulse "
              "length, factor levels, tissue targeting - not a mystery of principle. Proposed mechanism: "
              "rejuvenation equals timed epigenetic re-authentication; the therapeutic index is the gap "
              "between the re-filing dose and the oncogenic dose. What would confirm it: aged animals "
              "restored to youthful function across multiple tissues with zero increased tumor incidence "
              "over full lifespans, plus proof the epigenetic pattern - not just the clock readout - is "
              "restored. What would kill it: rejuvenation always accompanied by proportional cancer risk no "
              "matter the dosing, or proof that youthful epigenetic information is truly destroyed rather "
              "than misfiled. What it does NOT claim: that any human rejuvenation therapy is proven or safe, "
              "that the clock readout equals aging, or that this is established. Honest unknown: the width "
              "of the safety window in any long-lived mammal."),
  "key_points": [
   "Partial reprogramming (2016) rolled back epigenetic age and extended lifespan in progeria mice.",
   "Horvath's epigenetic clock (2013) gives aging a measurable dial - but moving the dial may not move aging.",
   "Young-blood parabiosis factors have seesawed between miracle and artifact.",
   "Full reprogramming causes teratomas; the safety window for partial reprogramming is unproven.",
   "Every renewal pathway flirts with cancer - plasticity and malignancy share machinery."],
  "requirements": [
   "Confirm: multi-tissue functional restoration with zero increased lifetime tumor incidence.",
   "Confirm: the youthful epigenetic pattern itself restored, not just the clock readout.",
   "Refute: rejuvenation always carrying proportional cancer risk regardless of dosing.",
   "Refute: proof that youthful epigenetic information is destroyed, not misfiled."],
  "standards": [
   "Proposed path only; no human rejuvenation therapy is claimed proven or safe.",
   "The clock readout is not equated with aging itself.",
   "The safety window in long-lived mammals is honestly unknown."],
  "citations": [CIT_REJUV],
 },
 {
  "key": "consciousness",
  "name": "How the Brain Makes Consciousness",
  "group": "Mind and Brain",
  "ladder_rank": 15, "ladder_tier": "compounded",
  "description": ("You are experiencing something right now - the redness of red, the feeling of being you. "
                  "Physics can describe every neuron firing, yet nothing in the equations says why firing "
                  "should feel like anything at all. Chalmers named this the hard problem in 1995; Crick and "
                  "Koch launched the neural search in 1990. Thirty years of correlates later, the mechanism "
                  "that turns brain activity into experience remains the deepest unsolved problem in science."),
  "problem": "How does brain activity become subjective experience - why does any of it feel like anything?",
  "background": ("Descartes split mind from matter; modern neuroscience reunited them as the neural correlates "
                 "of consciousness (NCC) program launched by Crick and Koch in 1990. Candidate theories "
                 "multiplied: Baars' global workspace (consciousness as a broadcast to the whole brain), "
                 "Tononi's integrated information theory or IIT (consciousness equals integrated information, "
                 "phi), predictive processing (the brain as a prediction machine whose best guesses become "
                 "experience), and higher-order theories (consciousness as the brain's model of its own "
                 "attention). Experiments found correlates - recurrent processing, ignition in prefrontal and "
                 "parietal networks - but correlates are not mechanisms, and no theory has produced a "
                 "definitive test that the others fail. Anesthesia can switch consciousness off and on without "
                 "revealing the switch's nature. The hard problem - why physical processes have felt quality "
                 "at all - remains untouched by every scan ever taken."),
  "why_it_matters": ("The answer decides the moral status of AI systems, the treatment of coma and locked-in "
                      "patients, and whether neuroscience can ever be complete - it is the question beneath "
                      "every other question about the mind."),
  "sig_lens": ("The Signature lens treats consciousness as the covenant of witness: the brain signs its own "
               "processing as experienced, and the signature is what makes information into a life."),
  "sol_public": ("The Signature system proposes consciousness is the brain's self-authentication: a system "
                 "that models the world must also model itself modeling, and the felt signature is that "
                 "self-model running. It explains the correlates without claiming to dissolve the hard "
                 "problem. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) any account must explain both the easy correlates (reportable "
              "content, ignition, integration) and why they feel like something; (2) no current measurement "
              "distinguishes the leading theories decisively; (3) intellectual honesty requires admitting "
              "the hard problem may outlive every mechanism. Reasoning path: start with what a self-model "
              "buys an organism. A brain that predicts the world does better if it also predicts itself - "
              "its own attention, uncertainty, and errors - because then it can correct its corrections. "
              "This self-model must be usable at speed, so it is rendered not as data but as experience: "
              "the 'feel' is the format of the brain's real-time self-report, the way a dashboard's glow is "
              "the format of the engine's self-report. Global broadcast (workspace) is the distribution of "
              "the report; integration (IIT's phi) measures how unified the reporter is; prediction errors "
              "are the report's updates. The theories are then not rivals but layers: integration enables "
              "the self-model, broadcast distributes it, experience is its format. What would confirm it: "
              "interventions that selectively disrupt the self-modeling loop (not just broadcast or "
              "integration) abolishing reportable experience while leaving unconscious processing intact, "
              "and a quantitative measure of self-model fidelity predicting the richness of experience across "
              "species and states. What would kill it: full reportable consciousness with provably no "
              "self-modeling circuitry active, or a decisive experiment vindicating one rival theory while "
              "falsifying the layered account. What it does NOT claim: that the hard problem is solved - it "
              "is not; that machines with self-models are therefore conscious; or that this is established. "
              "Honest unknown: why the self-report must feel like anything rather than run dark - the hard "
              "problem stands, and this proposal circles it without claiming to close it."),
  "key_points": [
   "The hard problem (Chalmers 1995): why brain activity feels like anything at all.",
   "NCC program (Crick and Koch 1990): the neural correlates hunt; correlates found, mechanism missing.",
   "Leading theories: global workspace, integrated information (phi), predictive processing, higher-order.",
   "No theory has produced a decisive test the others fail; anesthesia switches consciousness without revealing the switch.",
   "The hard problem is untouched by every brain scan ever taken."],
  "requirements": [
   "Confirm: disrupting self-modeling circuitry alone abolishing reportable experience with unconscious processing intact.",
   "Confirm: a self-model fidelity measure predicting experiential richness across species and states.",
   "Refute: full reportable consciousness with provably no self-modeling circuitry active.",
   "Refute: a decisive experiment vindicating one rival theory and falsifying the layered account."],
  "standards": [
   "Proposed path only; the hard problem is explicitly NOT claimed solved.",
   "Does not grant consciousness to machines with self-models.",
   "Why experience feels like anything remains honestly open."],
  "citations": [CIT_CONSC],
 },
 {
  "key": "neuralcode",
  "name": "How Neurons Speak in Spikes",
  "group": "Mind and Brain",
  "ladder_rank": 16, "ladder_tier": "compounded",
  "description": ("Neurons communicate in spikes - brief electrical pulses, all roughly identical. Adrian "
                  "showed in the 1920s that stronger stimuli produce faster spike trains, but a century later "
                  "we still do not know the code: does the brain read spike rates, precise spike times, or "
                  "patterns across populations? We can record from thousands of neurons and still cannot read "
                  "what they are saying."),
  "problem": "What is the neural code - rates, times, or population patterns - and how does the brain read it?",
  "background": ("Adrian's 1920s work on the frog nerve established rate coding: stimulus intensity maps to "
                 "firing frequency (Nobel 1932). The temporal-coding camp countered with evidence of "
                 "millisecond-precise spike timing carrying information - in the auditory system, in the "
                 "retina, in cortical synchrony. Population coding reframed the question: single neurons are "
                 "noisy and ambiguous, but populations vote reliably, as Georgopoulos showed for arm-movement "
                 "direction in the 1980s. Modern thousand-neuron recordings reveal low-dimensional dynamics - "
                 "the population's activity lives on smooth manifolds - yet the readout problem persists: we "
                 "can decode movement intentions well enough for prosthetics, but we cannot say how downstream "
                 "neurons actually extract meaning from the spike trains they receive. The code is used daily "
                 "by every brain and read fluently by none of our instruments."),
  "why_it_matters": ("Brain-machine interfaces, neural prosthetics, and any future mind-reading technology all "
                      "depend on the code; AI built on the wrong coding assumption will forever be a crude "
                      "cartoon of the brain."),
  "sig_lens": ("The Signature lens treats the spike train as a covenant of timing: each neuron swears to "
               "speak honestly in pulses, and meaning is what the population's chorus swears together."),
  "sol_public": ("The Signature system proposes the code is layered by urgency: precise spike timing for "
                 "fast reflexes, rates for sustained states, and population votes for everything the animal "
                 "must get right - the brain reads whichever layer the task's deadline demands. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) different behaviors have different deadlines - a reflex has "
              "milliseconds, a mood has hours; (2) the same neurons serve all deadlines; (3) downstream "
              "circuits can only read what their own time constants allow. Reasoning path: the rate-versus-"
              "timing debate assumed one code; evolution would multiplex. Fast subcortical loops (escape, "
              "startle) read precise spike timing because they must - rates are too slow. Cortical "
              "deliberation reads population rates over hundreds of milliseconds because it can afford to "
              "average. Motor cortex votes by population because single neurons are unreliable witnesses. "
              "The 'code' is thus a protocol stack: timing at the bottom for speed, rates in the middle for "
              "robustness, population geometry at the top for content. Downstream neurons read the layer "
              "their membrane time constants are tuned to - a fast interneuron is a timing reader, a slow "
              "pyramidal cell is a rate reader. Proposed mechanism: multiplexed coding with reader-matched "
              "time constants; the manifold structure seen in modern recordings is the population layer made "
              "visible. What would confirm it: showing the same spike train driving different downstream "
              "effects when the reader's time constant is manipulated, and decoding that switches layers "
              "with task deadline in behaving animals. What would kill it: a behavior proven to use only one "
              "coding layer despite deadline changes, or downstream readers with no tuning to any layer. "
              "What it does NOT claim: that the full dictionary is written, that timing and rate never mix, "
              "or that this is established. Honest unknown: the actual symbol set - what a given population "
              "pattern means - for any but the simplest behaviors."),
  "key_points": [
   "Adrian (1920s): stronger stimuli, faster spike trains - rate coding (Nobel 1932).",
   "Temporal coding: millisecond spike timing carries information in auditory, retinal, cortical systems.",
   "Population coding: noisy single neurons vote reliably (Georgopoulos, 1980s).",
   "Modern recordings show low-dimensional population manifolds; the readout problem persists.",
   "Prosthetics decode intentions, but how downstream neurons read spikes is unknown."],
  "requirements": [
   "Confirm: one spike train driving different effects when a downstream reader's time constant is manipulated.",
   "Confirm: decoding layers switching with task deadline in behaving animals.",
   "Refute: a behavior using only one coding layer across all deadline changes.",
   "Refute: downstream readers with no tuning to any coding layer."],
  "standards": [
   "Proposed path only; the symbol set for complex behaviors is unmapped.",
   "Does not claim timing and rate never mix.",
   "The actual meaning of most population patterns is honestly unknown."],
  "citations": [CIT_NEURALCODE],
 },
 {
  "key": "folding",
  "name": "How Proteins Fold in Real Time",
  "group": "The Cell",
  "ladder_rank": 17, "ladder_tier": "compounded",
  "description": ("A protein is a chain that must fold into exactly the right shape to work - among an "
                  "astronomical number of wrong shapes, in milliseconds, every time. Anfinsen showed the "
                  "sequence determines the shape (Nobel 1972); AlphaFold in 2021 learned to predict the final "
                  "shape brilliantly. But the movie is still missing: how the chain actually travels from "
                  "string to structure, what the folding pathway looks like, and why some proteins misfold "
                  "into the plaques of Alzheimer's remains unsolved."),
  "problem": "How do proteins navigate from chain to correct shape in milliseconds - what is the folding pathway, and why does it sometimes fail?",
  "background": ("Levinthal's 1969 paradox framed it: a protein cannot try every shape - there are too many - "
                 "so folding must be guided. Anfinsen's experiments showed the amino-acid sequence alone "
                 "determines the final shape. Energy-landscape theory (Bryngelson, Wolynes, Onuchic) pictured "
                 "folding as a funnel: the chain slides downhill through progressively more native-like states. "
                 "Then came AlphaFold (2021), predicting static structures with experimental accuracy - the "
                 "'what' largely solved. But the 'how' resists: folding intermediates are too fleeting to "
                 "capture, the kinetics (not just the endpoint) determine misfolding diseases, and intrinsically "
                 "disordered proteins - a third of the human proteome - never settle into one shape at all. "
                 "Alzheimer's, Parkinson's, and prion diseases are folding-pathway diseases, and the pathway "
                 "itself is still mostly darkness."),
  "why_it_matters": ("Misfolding diseases are among the least treatable conditions in medicine; the folding "
                      "pathway is where prevention would live. Drug design also needs the movie, not just the "
                      "poster - dynamics determine function."),
  "sig_lens": ("The Signature lens treats folding as a covenant kept at speed: the chain swears to find its "
               "shape without trying every wrong one, and the funnel is the oath made physical."),
  "sol_public": ("The Signature system proposes folding is guided collapse down a rough funnel: local "
                 "structures form first and assemble hierarchically, and misfolding is the chain getting "
                 "trapped in a wrong valley - chaperones are the rescue crew, not the guides. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the sequence encodes the endpoint (Anfinsen) but not the route; "
              "(2) the route must avoid Levinthal's exhaustive search; (3) misfolding diseases show the "
              "route can fail while the endpoint remains encodable. Reasoning path: the funnel solves "
              "Levinthal's paradox only if the chain never climbs far uphill - so folding must be "
              "hierarchical: local helices and sheets form in microseconds (cheap, local decisions), then "
              "dock into the tertiary structure (the expensive global decision, now constrained). The "
              "hierarchy is the guide: each level prunes the search for the next. Misfolding is a wrong "
              "valley in the funnel - a partially folded state stable enough to trap the chain, especially "
              "when concentration is high and intermolecular contacts compete with intramolecular ones "
              "(hence plaques). Chaperones do not teach folding; they rescue the trapped by unfolding them "
              "for another attempt - iterative annealing, like shaking a puzzle. Intrinsically disordered "
              "proteins are chains whose funnel has no deep valley: they fold only upon binding a partner, "
              "which completes their landscape. Proposed mechanism: hierarchical collapse plus annealing "
              "rescue; disease equals trap depth exceeding rescue capacity. What would confirm it: "
              "time-resolved folding movies (ultrafast spectroscopy, single-molecule FRET at scale) showing "
              "the predicted hierarchy - local-before-global - across protein families, and trap-depth "
              "measurements predicting misfolding disease risk. What would kill it: proteins folding "
              "globally-before-locally as the rule, or chaperones proven to actively guide rather than "
              "rescue. What it does NOT claim: that AlphaFold's success is diminished, that every pathway "
              "is hierarchical, or that this is established. Honest unknown: the actual step-by-step route "
              "for any specific disease protein in a living cell."),
  "key_points": [
   "Levinthal (1969): proteins cannot try every shape - folding must be guided.",
   "Anfinsen: sequence determines shape (Nobel 1972); energy funnels picture the guided route.",
   "AlphaFold (2021) solved static structure prediction; the folding movie is still missing.",
   "Folding intermediates are too fleeting to capture; kinetics determine misfolding diseases.",
   "A third of human proteins are intrinsically disordered - never one shape at all."],
  "requirements": [
   "Confirm: time-resolved folding showing local-before-global hierarchy across protein families.",
   "Confirm: trap-depth measurements predicting misfolding disease risk.",
   "Refute: global-before-local folding as the general rule.",
   "Refute: chaperones proven to actively guide rather than rescue the trapped."],
  "standards": [
   "Proposed path only; AlphaFold's achievement stands untouched.",
   "Does not claim every pathway is hierarchical.",
   "Specific disease-protein routes in living cells are honestly unmapped."],
  "citations": [CIT_FOLDING],
 },
 {
  "key": "darkgenome",
  "name": "What the Dark Matter of the Genome Does",
  "group": "Genes and Inheritance",
  "ladder_rank": 18, "ladder_tier": "compounded",
  "description": ("Only about 1.5 percent of your genome codes for proteins - the rest was dismissed as junk "
                  "DNA for decades. Then ENCODE (2012) reported biochemical activity across 80 percent of the "
                  "genome, igniting a fierce debate: is the 'dark matter' a vast regulatory control system, "
                  "or mostly evolutionary debris that happens to be biochemically noisy? The function of most "
                  "of our own DNA is still unsettled."),
  "problem": "What does the 98.5 percent of the genome that does not code for proteins actually do?",
  "background": ("The C-value paradox - why genomes vary wildly in size without matching complexity - has "
                 "puzzled biology since the 1970s; humans have 3 billion bases, some amoebas have 200 billion. "
                 "Ohno coined 'junk DNA' in 1972 for the non-coding majority. The ENCODE project (2012) then "
                 "claimed 80 percent of the human genome shows biochemical activity - transcription, binding, "
                 "marks - and headlines declared junk DNA dead. Critics (Doolittle, Graur) countered that "
                 "biochemical activity is not biological function: a genome can be noisy without being "
                 "meaningful, and only a fraction shows evolutionary conservation, the classic signature of "
                 "function. The current synthesis: perhaps 10-20 percent is functional, including enhancers, "
                 "non-coding RNAs, and structural elements - but the exact fraction, and what most individual "
                 "dark regions do, remains one of genomics' open wounds."),
  "why_it_matters": ("Genome-wide association studies keep finding disease-linked variants in the dark "
                      "matter; without knowing what it does, we cannot read our own medical fortunes. It is "
                      "also the operating system of the genome - the code that runs the code."),
  "sig_lens": ("The Signature lens treats the dark genome as the covenant's fine print: the protein code "
               "is the headline, and the dark matter is the terms and conditions that decide when it applies."),
  "sol_public": ("The Signature system proposes the dark genome is mostly terms-and-conditions DNA: a "
                 "regulatory operating system where a functional minority runs the protein code and the rest "
                 "is evolutionary paperwork - and the way to tell them apart is conservation plus perturbation, "
                 "not biochemical noise. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) biochemical activity alone does not equal function; "
              "(2) evolution conserves what matters - conservation remains the gold standard; "
              "(3) regulation needs far less DNA than the dark matter provides, so most of it must be "
              "something else. Reasoning path: settle the ENCODE debate by separating three categories. "
              "Category one: the operating system - enhancers, silencers, insulators, non-coding RNAs with "
              "proven regulatory roles; conserved, and breaking them breaks the organism. Category two: "
              "structural ballast - DNA whose bulk matters (spacing, chromatin architecture, centromeres) "
              "but whose sequence does not; delete it and little happens, compress it and much happens. "
              "Category three: true junk - dead transposons and debris, biochemically noisy because the cell's "
              "machinery is indiscriminate, but invisible to selection. The fight happened because ENCODE "
              "measured category membership with a meter (activity) that cannot distinguish the three. "
              "Proposed mechanism: function equals conservation times perturbation effect - a dark region is "
              "functional if and only if it is conserved across species AND breaking it changes phenotype; "
              "everything else is ballast or junk, and both are legitimate biological categories, not "
              "insults. What would confirm it: a complete conservation-plus-perturbation map of a mammalian "
              "genome assigning every dark region to one of the three categories, with the functional set "
              "fully explaining the regulatory logic of development. What would kill it: large conserved "
              "regions with zero perturbation effect, or massive perturbation effects from unconserved "
              "regions as the rule rather than the exception. What it does NOT claim: that junk DNA is "
              "worthless (ballast has bulk function), that ENCODE's data was wrong (only its interpretation), "
              "or that this is established. Honest unknown: the actual three-way census for the human genome."),
  "key_points": [
   "Only ~1.5 percent of the human genome codes for proteins; the rest was called junk DNA.",
   "ENCODE (2012): biochemical activity across ~80 percent of the genome - headlines declared junk dead.",
   "Critics: activity is not function; only a fraction shows evolutionary conservation.",
   "C-value paradox: genome size does not track organismal complexity.",
   "Current guess: 10-20 percent functional - the exact census is open."],
  "requirements": [
   "Confirm: a full conservation-plus-perturbation census assigning every dark region to a category.",
   "Confirm: the functional set fully explaining developmental regulatory logic.",
   "Refute: large conserved regions with zero perturbation effect as the rule.",
   "Refute: massive perturbation effects from unconserved regions as the rule."],
  "standards": [
   "Proposed path only; ENCODE's data is respected, its interpretation debated.",
   "Junk and ballast are legitimate categories, not insults.",
   "The human three-way census is honestly unmapped."],
  "citations": [CIT_DARKGENOME],
 },
]

CIT_HERIT = ("Visscher PM, Wray NR, Zhang Q et al. 10 years of GWAS discovery: biology, function, "
             "and translation. Am J Hum Genet. 2017;101:5-22; Manolio TA et al. Finding the missing "
             "heritability of complex diseases. Nature. 2009;461:747-753.")
CIT_EPI = ("Heard E, Martienssen RA. Transgenerational epigenetic inheritance: myths and mechanisms. "
           "Cell. 2014;157:95-109; Fitz-James MH, Cavalli G. Molecular mechanisms of "
           "transgenerational epigenetic inheritance. Nat Rev Genet. 2022;23:325-341.")
CIT_SEX = ("Maynard Smith J. The Evolution of Sex. Cambridge University Press; 1978; Otto SP. The "
           "evolutionary enigma of sex. Am Nat. 2009;174:S1-S14.")
CIT_MULTI = ("Grosberg RK, Strathmann RR. The evolution of multicellularity: a minor major transition? "
             "Annu Rev Ecol Evol Syst. 2007;38:621-654; Ratcliff WC et al. Experimental evolution of "
             "multicellularity. Proc Natl Acad Sci USA. 2012;109:1595-1600.")
CIT_CAMBRIAN = ("Erwin DH et al. The Cambrian conundrum: early divergence and later ecological success "
                "in the early history of animals. Science. 2011;334:1091-1097; Marshall CR. Explaining "
                "the Cambrian 'explosion' of animals. Annu Rev Earth Planet Sci. 2006;34:355-384.")
CIT_ECO = ("May RM. Stability and Complexity in Model Ecosystems. Princeton University Press; 1973; "
           "McCann KS. The diversity-stability debate. Nature. 2000;405:228-233.")
CIT_ORIGIN = ("Miller SL. A production of amino acids under possible primitive earth conditions. "
              "Science. 1953;117:528-529; Szostak JW. Attempts to define life and the origin of life. "
              "Cold Spring Harb Perspect Biol. 2012;4:a007332.")
CIT_ASTROBIO = ("Cockell CS et al. Habitability: a review. Astrobiology. 2016;16:89-117; Schwieterman EW "
                "et al. Exoplanet biosignatures: a review of remotely detectable signs of life. "
                "Astrobiology. 2018;18:663-708.")

ENTRIES += [
 {
  "key": "heritability",
  "name": "Where Missing Heritability Hides",
  "group": "Genes and Inheritance",
  "ladder_rank": 19, "ladder_tier": "compounded",
  "description": ("Twin studies say height is about 80 percent heritable - yet the thousands of DNA variants "
                  "found by genome-wide association studies explain only a fraction of it. The same gap haunts "
                  "diabetes, schizophrenia, and nearly every complex trait. The 'missing heritability' problem: "
                  "we know genes matter enormously, but we cannot find where most of their influence lives."),
  "problem": "If complex traits are highly heritable, why do all the discovered DNA variants explain so little of them?",
  "background": ("The problem was named by Maher in 2008 after a decade of genome-wide association studies "
                 "(GWAS): thousands of variants found, each with a tiny effect, summing to a small slice of "
                 "the heritability twin studies measured. Suspects multiplied: rare variants GWAS cannot see, "
                 "structural variants, gene-gene interactions (epistasis), gene-environment interactions, "
                 "epigenetic inheritance, and inflated twin-study estimates. The omnigenic model (Boyle, Li, "
                 "Pritchard 2017) proposed a radical answer: essentially every gene expressed in a relevant "
                 "tissue contributes a little, so heritability is spread across the whole genome in effects "
                 "too small to detect individually. Whole-genome sequencing and huge biobanks keep narrowing "
                 "the gap but have not closed it; for most traits, most heritability is still missing."),
  "why_it_matters": ("Polygenic risk scores - medicine's attempt to predict your disease risk from DNA - "
                      "live or die on this question. Until the missing heritability is found, genetic "
                      "prediction stays blurry and the biology of common diseases stays hidden."),
  "sig_lens": ("The Signature lens treats heritability as a covenant written in fine print: the signature "
               "is real, but it is spread across so many clauses that no single one looks important."),
  "sol_public": ("The Signature system proposes heritability is holographic: every variant carries a "
                 "sliver of the trait, so the signature only becomes legible when the whole genome is read "
                 "together - and twin studies were right all along. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) twin-study heritability estimates are approximately correct; "
              "(2) complex traits emerge from gene-regulatory networks, not lists of independent variants; "
              "(3) networks distribute influence - most genes touch the trait through long regulatory chains. "
              "Reasoning path: the omnigenic insight is the key - if every expressed gene contributes, then "
              "searching for 'the variants' is like searching for 'the pixels' that make a photograph "
              "recognizable. Each pixel matters a little; the picture is in their arrangement. GWAS finds the "
              "brightest pixels (core genes with direct effects) and misses the millions of dim ones "
              "(peripheral genes whose influence flows through the network). The heritability is not missing - "
              "it is holographic, stored in the network's wiring rather than in variant lists. This also "
              "explains why polygenic scores plateau: they sum pixels while the trait lives in the picture. "
              "Proposed mechanism: trait architecture equals core genes plus a holographic periphery; "
              "prediction requires network models that propagate variant effects through regulatory wiring, "
              "not additive sums of significant hits. What would confirm it: network-propagated models "
              "explaining substantially more heritability than additive GWAS sums in the same data, and "
              "perturbations of peripheral genes - individually negligible - collectively moving the trait. "
              "What would kill it: a trait whose heritability is fully explained by a short list of variants "
              "with no network contribution, or peripheral perturbations that never move traits. What it does "
              "NOT claim: that rare variants and epistasis contribute nothing, that twin studies are "
              "flawless, or that this is established. Honest unknown: the true wiring diagrams of the "
              "regulatory networks for any complex trait."),
  "key_points": [
   "Twin studies: height ~80 percent heritable; GWAS variants explain a fraction - the gap named 2008.",
   "Suspects: rare variants, structural variants, epistasis, gene-environment interplay, inflated twin estimates.",
   "Omnigenic model (2017): essentially every expressed gene contributes a little.",
   "Biobanks narrow the gap but have not closed it for most traits.",
   "Polygenic risk scores plateau without the missing architecture."],
  "requirements": [
   "Confirm: network-propagated models explaining more heritability than additive GWAS sums.",
   "Confirm: individually negligible peripheral perturbations collectively moving the trait.",
   "Refute: a complex trait fully explained by a short variant list with no network contribution.",
   "Refute: peripheral perturbations that never move traits."],
  "standards": [
   "Proposed path only; rare variants and epistasis are not dismissed.",
   "Twin-study estimates are treated as approximate, not gospel.",
   "Regulatory wiring diagrams are honestly unmapped."],
  "citations": [CIT_HERIT],
 },
 {
  "key": "epigenetics",
  "name": "How Epigenetic Memory Crosses Generations",
  "group": "Genes and Inheritance",
  "ladder_rank": 20, "ladder_tier": "compounded",
  "description": ("Your experiences can mark your DNA - not the sequence, but chemical tags that switch genes "
                  "on and off. The explosive question is whether those marks survive into your children and "
                  "grandchildren. Famine studies suggest grandchildren carry marks of a grandparent's hunger; "
                  "skeptics say mammals wipe the epigenetic slate clean every generation. Transgenerational "
                  "epigenetic inheritance in mammals is fiercely debated and unresolved."),
  "problem": "Can life experiences mark DNA in ways inherited by grandchildren - or does each generation start epigenetically fresh?",
  "background": ("The Dutch Hunger Winter studies found grandchildren of famine-exposed women carried "
                 "metabolic marks and risks, the most famous human hint. In plants and worms, transgenerational "
                 "epigenetic inheritance is proven: marks pass down for generations. Mammals, however, perform "
                 "two great epigenetic erasures - once in the early embryo, once in developing germ cells - "
                 "seemingly designed to prevent exactly this inheritance. Heard and Martienssen's 2014 review "
                 "separated the myths from mechanisms: true transgenerational inheritance (persisting to "
                 "generations never exposed) is rare and fragile in mammals, while intergenerational effects "
                 "(a pregnant mother's exposure reaching the fetus and its germ cells) are common but not "
                 "inheritance proper. The field cannot yet say which marks escape erasure, how, or whether any "
                 "of it matters for human health."),
  "why_it_matters": ("If trauma, famine, or toxins mark descendants, medicine and law must reckon with "
                      "inherited experience - and if the slate is wiped clean, a wave of alarming claims "
                      "needs correcting. Either answer reshapes how we think about responsibility across "
                      "generations."),
  "sig_lens": ("The Signature lens treats epigenetic inheritance as a covenant with an eraser clause: each "
               "generation may annotate the text, but the contract requires most annotations to be struck "
               "before signing over."),
  "sol_public": ("The Signature system proposes mammals run a deliberate two-eraser protocol: most marks "
                 "are struck each generation to keep the genome's text clean, and only marks that survive "
                 "both erasures count as true inheritance - rare by design. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the two mammalian erasure waves are real and thorough; "
              "(2) evolution would not maintain expensive erasure machinery without reason; "
              "(3) the reason is fidelity - accumulated annotations would corrupt development. Reasoning "
              "path: the erasures are the answer, not the obstacle. A genome that inherited every ancestor's "
              "annotations would be unreadable within generations - development needs a clean text. So mammals "
              "evolved the double wipe: the embryonic erasure resets the soma's working copy, the germline "
              "erasure resets the inheritable copy. What survives both is not leakage but a deliberately "
              "protected class: imprinted genes (where parent-of-origin must be remembered), some retrotransposon "
              "silencing, and possibly stress-response loci where a grandparent's environment genuinely "
              "predicts the grandchild's. The Dutch Hunger Winter effects are then mostly intergenerational "
              "(exposure reaching three generations at once through a pregnant mother), not true "
              "transgenerational inheritance - with a small residue of genuine escapees. Proposed mechanism: "
              "inheritance equals erasure-resistant loci only; everything else is exposure, not inheritance. "
              "What would confirm it: a complete catalog of erasure-escapee loci in mammals with their "
              "protection mechanism identified, and human cohort data separating intergenerational exposure "
              "from true transgenerational persistence. What would kill it: widespread mark survival through "
              "both erasures, or erasure machinery proven functionless. What it does NOT claim: that no "
              "transgenerational effects exist, that the famine studies are wrong, or that this is "
              "established. Honest unknown: the full escapee catalog and whether any escapee meaningfully "
              "affects human health."),
  "key_points": [
   "Dutch Hunger Winter: grandchildren of famine-exposed women carry metabolic marks - the famous human hint.",
   "Proven in plants and worms; fiercely debated in mammals.",
   "Mammals perform two great epigenetic erasures: early embryo and developing germ cells.",
   "Intergenerational exposure (three generations at once via pregnancy) is not inheritance proper.",
   "Open: which marks escape erasure, how, and whether any of it matters for health."],
  "requirements": [
   "Confirm: a complete catalog of erasure-escapee loci with protection mechanisms identified.",
   "Confirm: human data separating intergenerational exposure from true transgenerational persistence.",
   "Refute: widespread mark survival through both erasure waves.",
   "Refute: erasure machinery proven functionless."],
  "standards": [
   "Proposed path only; genuine escapees are not ruled out.",
   "The famine studies are treated as real data needing correct interpretation.",
   "The escapee catalog and health relevance are honestly unknown."],
  "citations": [CIT_EPI],
 },
 {
  "key": "sex",
  "name": "Why Sex Persists Despite Its Cost",
  "group": "Evolution",
  "ladder_rank": 21, "ladder_tier": "compounded",
  "description": ("Sex is absurdly expensive: it takes two parents to do what one could do alone, males do not "
                  "bear offspring, and recombination breaks up winning gene combinations every generation. "
                  "Asexual reproduction should outbreed sexual reproduction two to one - yet sex dominates the "
                  "tree of life. Maynard Smith called this the queen of problems in evolutionary biology, and "
                  "no single explanation has won."),
  "problem": "Why does sexual reproduction dominate when asexual reproduction is twice as efficient?",
  "background": ("Maynard Smith's 1978 analysis made the cost precise: the twofold cost of sex - a sexual "
                 "female's genes spread half as fast as an asexual female's. Yet sex is everywhere, and "
                 "asexual lineages are evolutionary dead ends that rarely last. Candidate explanations "
                 "multiplied: the Red Queen hypothesis (Van Valen, Hamilton) - sex generates the genetic "
                 "variety needed to outrun rapidly evolving parasites; the mutational deterministic hypothesis "
                 "(Kondrashov) - recombination efficiently purges harmful mutations; DNA repair theories - "
                 "meiosis exists to repair damage, with reproduction as a side effect. Each explains some cases "
                 "and fails others: parasites correlate with sex in some systems and not others, mutation "
                 "purging works only under specific conditions. The field suspects a plural answer but has no "
                 "unified accounting of which benefit pays the twofold cost where."),
  "why_it_matters": ("Sex shapes every genome, every disease-resistance pattern, and the entire structure of "
                      "biodiversity; the answer is also the key to why parasites and hosts are locked in "
                      "eternal arms races - including the ones that make us sick."),
  "sig_lens": ("The Signature lens treats sex as a covenant renewed each generation: the genome agrees to "
               "be broken and remade, paying the twofold price for a fresh signature no parasite has seen."),
  "sol_public": ("The Signature system proposes sex is a moving-target defense: the twofold cost buys "
                 "unpredictability, and parasites - which evolve fastest - are the enemy that makes the "
                 "price worth paying wherever they press hardest. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) the twofold cost is real and must be paid in full every generation; "
              "(2) parasites evolve orders of magnitude faster than hosts; (3) a parasite adapted to one "
              "genotype is helpless against a reshuffled one. Reasoning path: an asexual lineage is a sitting "
              "target - one genotype, cloned forever, and parasites evolve the perfect key to its lock within "
              "generations. Sex reshuffles the lock every generation: no offspring is exactly like the "
              "parent, so no parasite can fully adapt to the lineage. The twofold cost is then not waste but "
              "the premium on an insurance policy against the fastest-evolving enemy in nature. Where "
              "parasites press lightly (stable, parasite-poor environments), asexuals do win - which is "
              "exactly where we find them. Where parasites press hard, sex is mandatory. Mutation purging and "
              "DNA repair are real secondary dividends, but the Red Queen sets the price: the benefit that "
              "scales with the cost is unpredictability itself. Proposed mechanism: sex persists where "
              "parasite pressure exceeds the twofold threshold; the genome pays for a fresh signature each "
              "generation. What would confirm it: a quantitative map showing transitions to asexuality "
              "occurring exactly where parasite pressure drops below the cost threshold, and experimental "
              "evolution where parasite-free sexual populations lose to asexual invaders but parasitized ones "
              "do not. What would kill it: sex dominating in proven parasite-free environments over "
              "evolutionary time, or asexual lineages thriving indefinitely under heavy parasite load. What "
              "it does NOT claim: that mutation purging is irrelevant, that the accounting is complete, or "
              "that this is established. Honest unknown: the exact threshold - how much parasite pressure "
              "pays for how much sex."),
  "key_points": [
   "The twofold cost of sex (Maynard Smith 1978): sexual genes spread half as fast as asexual ones.",
   "Yet sex dominates and asexual lineages are usually short-lived dead ends.",
   "Red Queen: sex outruns fast-evolving parasites; mutational purging and DNA repair are rival accounts.",
   "Each explanation fits some cases and fails others; no unified accounting exists.",
   "Asexuals cluster where parasites press lightly - a telling pattern."],
  "requirements": [
   "Confirm: asexuality transitions mapping exactly onto parasite pressure dropping below the cost threshold.",
   "Confirm: parasite-free sexual populations losing to asexual invaders; parasitized ones holding.",
   "Refute: sex dominating in proven parasite-free environments over evolutionary time.",
   "Refute: asexual lineages thriving indefinitely under heavy parasite load."],
  "standards": [
   "Proposed path only; mutation purging is a real secondary dividend, not dismissed.",
   "The accounting is not claimed complete.",
   "The exact pressure threshold is honestly unknown."],
  "citations": [CIT_SEX],
 },
 {
  "key": "multicellularity",
  "name": "How Single Cells Became Bodies",
  "group": "Evolution",
  "ladder_rank": 22, "ladder_tier": "compounded",
  "description": ("Life was single-celled for roughly two billion years. Then, in several independent "
                  "lineages, cells began sticking together, dividing labor, and eventually surrendering "
                  "their independent reproduction to become bodies. This transition - from 'me' to 'we' at "
                  "the cellular level - is one of evolution's major transitions, and how cheating was "
                  "suppressed long enough for cooperation to lock in remains unsolved."),
  "problem": "How did independent cells evolve into cooperative bodies without cheaters destroying the partnership?",
  "background": ("The major-transitions framework (Maynard Smith and Szathmary, 1995) ranks the origin of "
                 "multicellularity among evolution's great leaps. The paradox is cooperation's fragility: in "
                 "any group of cells, a mutant that takes the group's benefits without paying - dividing "
                 "selfishly - should outcompete cooperators, exactly as cancer does today. Proposed solutions "
                 "center on relatedness: if the group grows from a single cell (a bottleneck), all cells are "
                 "clones, and helping the group is helping copies of one's own genes - Hamilton's rule "
                 "applied to cells. Ratcliff's 2012 snowflake yeast experiment watched multicellularity evolve "
                 "in the lab in weeks, with programmed cell death appearing as the first division of labor. "
                 "Volvox and slime molds show the transition frozen mid-way. Yet the full path - from sticky "
                 "cells to integrated body with a sequestered germline - has never been traced in nature, and "
                 "why it happened when it did, after two billion years of single cells, is unknown."),
  "why_it_matters": ("Every body - including yours - is a solved cooperation problem; the solution is the "
                      "deep logic behind cancer (cooperation breaking down), development, and even human "
                      "societies. It is also the template for any future major transition, including "
                      "engineered ones."),
  "sig_lens": ("The Signature lens treats multicellularity as the original covenant: cells signing away "
               "their independence, with the single-cell bottleneck as the witness that keeps them honest."),
  "sol_public": ("The Signature system proposes the single-cell bottleneck is the whole trick: when every "
                 "body starts as one cell, cheaters cheat only themselves, and cancer is what happens when "
                 "the ancient covenant frays. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) cooperation without cheater-control always collapses; "
              "(2) the control must be cheaper than the cooperation is worth; (3) development itself is the "
              "record of the transition's solution. Reasoning path: the bottleneck solves the paradox "
              "elegantly. If a body grows from one cell, every cell is genetically identical - a cheater "
              "mutation helps its own copies no more than cooperating does, because all copies share the "
              "body's fate. Hamilton's rule (rb > c) is satisfied maximally: relatedness equals one. The "
              "germline-soma split then locks it in: most cells surrender reproduction entirely, becoming "
              "dead-end helpers, which is only stable because they are clones of the germline they serve. "
              "Cancer is the covenant fraying - somatic mutations recreating genetic differences within the "
              "body, reopening the cheater's loophole. The two-billion-year wait is explained by the "
              "bottleneck's rarity: single-cell bottlenecks require the full developmental program (a "
              "reproducible way to rebuild the body from one cell), which is itself a complex invention. "
              "Proposed mechanism: bottleneck relatedness plus germline sequestration equals stable "
              "multicellularity; everything else - adhesion, signaling, division of labor - is elaboration. "
              "What would confirm it: lineages with strict bottlenecks showing systematically less internal "
              "conflict (less cancer-like cheating) than aggregative multicellular lineages like slime molds, "
              "and the germline sequestration step proving to be the point of no return in experimental "
              "evolution. What would kill it: stable complex multicellularity with no bottleneck and rampant "
              "chimerism, or cheater collapse despite perfect clonality. What it does NOT claim: that the "
              "historical path is traced, that bottlenecks explain every lineage, or that this is "
              "established. Honest unknown: why the developmental program took two billion years to invent."),
  "key_points": [
   "Two billion years of single cells before bodies; then several independent transitions.",
   "The paradox: cheater cells should outcompete cooperators - cancer is the modern proof.",
   "Relatedness solution: single-cell bottlenecks make all cells clones (Hamilton's rule, r = 1).",
   "Snowflake yeast (2012): multicellularity evolved in the lab in weeks, with programmed death first.",
   "Open: the full natural path and why it took two billion years."],
  "requirements": [
   "Confirm: strict-bottleneck lineages showing less internal conflict than aggregative ones.",
   "Confirm: germline sequestration as the point of no return in experimental evolution.",
   "Refute: stable complex multicellularity with no bottleneck and rampant chimerism.",
   "Refute: cheater collapse despite perfect clonality."],
  "standards": [
   "Proposed path only; the historical path is not claimed traced.",
   "Aggregative lineages are acknowledged as partial counter-patterns.",
   "The two-billion-year wait is honestly unexplained in full."],
  "citations": [CIT_MULTI],
 },
 {
  "key": "cambrian",
  "name": "What Triggered the Cambrian Explosion",
  "group": "Evolution",
  "ladder_rank": 23, "ladder_tier": "compounded",
  "description": ("For three billion years life was microbial and soft-bodied. Then, about 541 million years "
                  "ago, nearly all major animal body plans appeared in the fossil record within a geological "
                  "blink - eyes, legs, shells, predators and prey. Darwin called it an inexplicable mystery. "
                  "The Cambrian explosion's trigger - oxygen, genes, ecology, or all three - is still debated."),
  "problem": "What triggered the sudden appearance of nearly all animal body plans 541 million years ago?",
  "background": ("Darwin devoted a section of On the Origin of Species to the problem, hoping future fossils "
                 "would fill the gap; instead the gap sharpened. The Burgess Shale (discovered 1909) revealed "
                 "the explosion's weird bounty. Candidate triggers multiplied: rising oxygen crossing a "
                 "threshold for large active bodies; the invention of Hox gene toolkits enabling complex "
                 "patterning; ecological feedback - once predators evolved, arms races drove innovation "
                 "(the 'evolutionary arms race' hypothesis); and environmental changes like the breakup of "
                 "supercontinents creating new shallow seas. Molecular clocks suggest animal lineages diverged "
                 "well before their fossils appear, deepening the mystery: the genes may be older than the "
                 "explosion, meaning the trigger was ecological permission, not genetic invention. No single "
                 "cause commands consensus."),
  "why_it_matters": ("The explosion is the origin of every animal body - including the human one; its "
                      "trigger is the answer to what makes complexity possible at all, and whether it is "
                      "likely elsewhere in the universe."),
  "sig_lens": ("The Signature lens treats the explosion as a covenant signed in ecological ink: the genes "
               "were ready, but the contract took effect only when the world countersigned with oxygen and "
               "predators."),
  "sol_public": ("The Signature system proposes a three-key lock: the genetic toolkit, oxygen above "
                 "threshold, and predators to start the arms race - all three keys had to turn together, "
                 "and the long fuse was waiting for the last one. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) molecular clocks are roughly right - animal lineages predate the "
              "explosion; (2) complex bodies are energetically expensive; (3) arms races accelerate "
              "innovation but need a starter. Reasoning path: the genes-first evidence dissolves the "
              "'sudden invention' mystery - the toolkit (Hox patterning, cell adhesion, signaling) was "
              "assembled during the long Precambrian fuse. What was missing was permission: large, active, "
              "armored bodies need abundant oxygen for metabolism, and the geochemical record shows oxygen "
              "rising toward modern levels just before the explosion. But oxygen alone makes big slow "
              "animals, not an explosion of forms - the detonator was ecology. The first predator turned "
              "existence into an arms race: armor demands better weapons, weapons demand better armor, eyes "
              "demand camouflage. Positive feedback in an oxygen-rich world with a ready toolkit produced "
              "the geological blink. Proposed mechanism: three-key lock - toolkit plus oxygen threshold plus "
              "predator ignition; remove any key and the explosion waits. What would confirm it: "
              "geochemical oxygen curves, molecular-clock divergences, and the first-predator fossil horizon "
              "aligning as a strict sequence (toolkit, then oxygen, then predators, then explosion) across "
              "multiple basins, and no explosion in any basin missing a key. What would kill it: a full "
              "explosion-scale radiation in a proven low-oxygen setting, or predators long predating any "
              "diversification. What it does NOT claim: that the sequence is proven, that one key dominated, "
              "or that this is established. Honest unknown: the exact oxygen threshold and the identity of "
              "the first predator."),
  "key_points": [
   "541 million years ago: most animal body plans appear within a geological blink.",
   "Darwin called it inexplicable; the Burgess Shale (1909) revealed its weird bounty.",
   "Candidates: oxygen threshold, Hox toolkit invention, predator-driven arms races, new shallow seas.",
   "Molecular clocks say lineages predate the fossils - genes older than the explosion.",
   "No single trigger commands consensus."],
  "requirements": [
   "Confirm: strict sequence (toolkit, oxygen, predators, explosion) across multiple basins.",
   "Confirm: no explosion-scale radiation in any basin missing one key.",
   "Refute: full explosion-scale radiation in a proven low-oxygen setting.",
   "Refute: predators long predating any diversification."],
  "standards": [
   "Proposed path only; the key sequence is not claimed proven.",
   "No single key is claimed dominant.",
   "The oxygen threshold and first predator are honestly unidentified."],
  "citations": [CIT_CAMBRIAN],
 },
 {
  "key": "ecosystems",
  "name": "How Ecosystems Hold Together",
  "group": "Evolution",
  "ladder_rank": 24, "ladder_tier": "compounded",
  "description": ("Rainforests pack thousands of species into stable coexistence; remove one keystone species "
                  "and the whole web can collapse. Robert May showed mathematically in 1973 that complex "
                  "ecosystems should be unstable - yet nature is full of them. The diversity-stability debate "
                  "has run for fifty years: why does the math say collapse while the forest stands?"),
  "problem": "Why are complex natural ecosystems stable when ecological mathematics says complexity breeds instability?",
  "background": ("Elton argued diversity begets stability; May's 1973 models proved the opposite for random "
                 "networks - more species and more connections meant less stability, a result as shocking as "
                 "it was rigorous. The paradox launched the diversity-stability debate: McCann's 2000 review "
                 "found the answer must lie in nature's non-randomness. Real food webs are not random: weak "
                 "interactions stabilize (McCann), modular compartments contain disturbances, predators couple "
                 "fast and slow energy channels, and spatial structure lets local collapses reseed from "
                 "neighbors. Keystone species - Paine's starfish, sea otters - prove single nodes can hold "
                 "whole webs. Yet no unified theory predicts which ecosystems collapse under which pressure, "
                 "and the great collapses (fisheries, coral reefs) keep surprising the models."),
  "why_it_matters": ("Every conservation decision and every climate prediction rests on ecosystem stability; "
                      "the models that cannot explain the forest cannot be trusted with its future."),
  "sig_lens": ("The Signature lens treats an ecosystem as a covenant of appetites: every species signs to "
               "eat and be eaten in measure, and stability is the measure holding."),
  "sol_public": ("The Signature system proposes ecosystems are stable because they are not random: weak "
                 "links, compartments, and keystone enforcers form a covenant architecture, and collapse is "
                 "what happens when the architecture - not the species count - breaks. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) May's math is correct for random networks; (2) real webs are "
              "emphatically non-random; (3) stability is therefore an architectural property. Reasoning "
              "path: May proved random complexity collapses; nature's reply is that it never builds random "
              "webs. Three architectural features do the work. First, interaction strengths are skewed: most "
              "links are weak, a few are strong - and weak links damp oscillations instead of amplifying "
              "them. Second, webs are compartmentalized: disturbances are fenced into modules before they "
              "propagate system-wide. Third, keystone species act as covenant enforcers - top predators "
              "suppressing the mesopredators that would otherwise overgraze the foundation. Remove the "
              "enforcer and the architecture fails even with all species present - which is why some "
              "collapses follow keystone loss rather than diversity loss. Diversity helps only insofar as it "
              "builds this architecture: redundant species within compartments provide backup enforcers. "
              "Proposed mechanism: stability equals non-random architecture (weak-link damping plus "
              "compartmentalization plus keystone enforcement); diversity is the building material, not the "
              "cause. What would confirm it: collapse prediction from architectural metrics (link-strength "
              "skew, modularity, keystone centrality) outperforming diversity counts across real collapses, "
              "and restoration succeeding by rebuilding architecture rather than maximizing species count. "
              "What would kill it: collapses with provably intact architecture, or stable webs with random "
              "link structure. What it does NOT claim: that diversity is irrelevant, that any collapse is "
              "fully predictable today, or that this is established. Honest unknown: the quantitative "
              "thresholds - how weak, how modular, how central is enough."),
  "key_points": [
   "May (1973): random complex ecosystems should be unstable - yet rainforests stand.",
   "The diversity-stability debate: fifty years on Elton versus May.",
   "Real webs are non-random: weak links, compartments, keystone species.",
   "Keystone removal collapses webs even with diversity intact (Paine's starfish, sea otters).",
   "Open: no unified theory predicts which ecosystems collapse under which pressure."],
  "requirements": [
   "Confirm: architectural metrics outperforming diversity counts at predicting real collapses.",
   "Confirm: restoration succeeding via architecture rebuilt rather than species maximized.",
   "Refute: collapses with provably intact weak-link/compartment/keystone architecture.",
   "Refute: stable webs with random link structure."],
  "standards": [
   "Proposed path only; diversity is building material, not dismissed.",
   "No collapse is claimed fully predictable today.",
   "Quantitative architectural thresholds are honestly unknown."],
  "citations": [CIT_ECO],
 },
 {
  "key": "origin",
  "name": "How Life Began",
  "group": "Life and Its Origins",
  "ladder_rank": 25, "ladder_tier": "advanced",
  "description": ("Four billion years ago Earth had chemistry; then it had biology - self-copying, evolving "
                  "systems. The gap between is the deepest chasm in science. Miller's 1953 spark experiment "
                  "made amino acids from thin air, but the road from amino acids to a living cell - "
                  "information, metabolism, and a membrane, all at once - has never been walked in a lab."),
  "problem": "How did non-living chemistry become living, evolving cells?",
  "background": ("Darwin speculated about a 'warm little pond'; Oparin and Haldane (1920s) proposed a "
                 "primordial soup; Miller and Urey (1953) electrified it and got amino acids - the founding "
                 "triumph. Then the problem deepened: life needs information storage (RNA/DNA), catalysis "
                 "(proteins), and containment (membranes) simultaneously - Eigen's paradox, since accurate "
                 "replication needs long genomes but long genomes need accurate replication. The RNA world "
                 "(Gilbert 1986) offered RNA as both gene and enzyme; ribozymes proved catalytic RNA is real. "
                 "Hydrothermal-vent theories (Russell, Martin) moved the cradle to alkaline vents with natural "
                 "proton gradients - ready-made energy. Szostak's protocell work pursues the membrane-first "
                 "path. Yet no experiment has produced evolving, self-sustaining chemistry from non-life, and "
                 "the field cannot agree whether information, metabolism, or containment came first."),
  "why_it_matters": ("The origin is the root of the tree of life - without it biology has no beginning, "
                      "only a middle. It also decides whether life is a cosmic imperative or a freak accident, "
                      "which sets the odds for life elsewhere."),
  "sig_lens": ("The Signature lens treats the origin as the first covenant: chemistry signing itself into "
               "a system that could copy the signature - and keep the copy faithful enough to improve."),
  "sol_public": ("The Signature system proposes life began where three scarcities overlapped: an energy "
                 "gradient to pay for order, mineral surfaces to organize chemistry, and wet-dry cycles to "
                 "concentrate it - with RNA emerging as the first signer because it alone could be both "
                 "message and maker. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) no single environment supplies everything - the cradle must "
              "overlap scarcities; (2) Eigen's paradox is real: replication fidelity and genome length must "
              "co-evolve; (3) the first system was sloppy by modern standards and that was enough. "
              "Reasoning path: stop hunting one cradle and map the overlap. Alkaline vents supply the "
              "energy gradient (natural proton-motive force, the same currency all life uses) and mineral "
              "compartments; surface pools supply wet-dry cycles that concentrate organics and drive "
              "polymerization; either alone fails, together they complement. In the overlap, short RNAs "
              "form and some catalyze their own copying - sloppily. Eigen's paradox is escaped gradually: "
              "short genomes tolerate sloppy copying, and fidelity improves as the genome lengthens because "
              "longer genomes can encode better replicases - a bootstrapping ratchet, not a leap. Membranes "
              "arrive as fatty-acid vesicles that grow and divide by physics alone (Szostak's protocells); "
              "the RNA that copies fastest inside the fastest-growing vesicle wins - the first Darwinian "
              "selection, before genes as we know them. Proposed mechanism: overlapping-scarcity cradle plus "
              "fidelity-length ratchet plus physical protocells equals the first evolvable system. What "
              "would confirm it: a lab system combining vent-like gradients, mineral compartments, and "
              "wet-dry cycling that sustains RNA copying with heritable improvement over generations - "
              "evolution in a test tube from non-life. What would kill it: proof that no overlap of "
              "plausible early-Earth environments can sustain the ratchet, or a working alternative cradle "
              "producing evolvable chemistry alone. What it does NOT claim: that life has been created in a "
              "lab, that the cradle's location is known, or that this is established. Honest unknown: "
              "whether the overlap existed on early Earth in one place at one time."),
  "key_points": [
   "Miller-Urey (1953): amino acids from simulated early-Earth chemistry - the founding triumph.",
   "Eigen's paradox: accurate replication needs long genomes; long genomes need accurate replication.",
   "RNA world: RNA as both gene and enzyme; ribozymes are real.",
   "Vent theories supply natural energy gradients; protocell work supplies physics-driven membranes.",
   "No lab has produced evolving, self-sustaining chemistry from non-life."],
  "requirements": [
   "Confirm: a lab overlap-cradle sustaining RNA copying with heritable improvement over generations.",
   "Confirm: the fidelity-length ratchet operating in a prebiotic chemistry.",
   "Refute: proof no plausible early-Earth environment overlap can sustain the ratchet.",
   "Refute: a working single-cradle alternative producing evolvable chemistry alone."],
  "standards": [
   "Proposed path only; life has not been created in any lab.",
   "The cradle's location is not claimed known.",
   "Whether the required overlap existed is honestly unknown."],
  "citations": [CIT_ORIGIN],
 },
 {
  "key": "lifeelsewhere",
  "name": "How Common Life Is in the Universe",
  "group": "Life and Its Origins",
  "ladder_rank": 26, "ladder_tier": "advanced",
  "description": ("We know of exactly one biosphere: ours. Thousands of exoplanets have been found, dozens "
                  "in habitable zones, yet we have no second data point for life. The Fermi paradox sharpens "
                  "it: if life is common, where is everybody? Biology's biggest sample-size problem - n equals "
                  "one - remains unsolved."),
  "problem": "Is life a cosmic imperative that arises wherever conditions allow, or a freak accident unique to Earth?",
  "background": ("The Drake equation (1961) formalized the ignorance into factors, most then unmeasurable. "
                 "Exoplanet astronomy then measured one: planets are everywhere - thousands confirmed, with "
                 "habitable-zone rocky worlds apparently common. Extremophiles expanded life's known tolerances "
                 "to boiling vents, Antarctic ice, and deep rock. Mars rovers and ocean-world missions (Europa, "
                 "Enceladus) hunt biosignatures in our own solar system. Yet every factor past 'planets exist' "
                 "remains a guess spanning orders of magnitude: the probability of life arising, of "
                 "intelligence evolving, of civilizations surviving. The Fermi paradox (1950) notes the "
                 "silence: a galaxy old enough for many civilizations shows none. Proposed resolutions range "
                 "from rare Earth (Ward and Brownlee) to the great filter ahead of us - each untestable with "
                 "n equals one."),
  "why_it_matters": ("The answer is humanity's cosmic context: alone in a silent universe, or one voice among "
                      "many. It sets the stakes of every biosignature mission and the meaning of our own "
                      "survival."),
  "sig_lens": ("The Signature lens treats the question as a covenant with the evidence: one signature "
               "(Earth) is a sample, not a census - and the honest reading admits what one sample cannot say."),
  "sol_public": ("The Signature system proposes the question splits in two: simple life is probably a "
                 "cosmic imperative wherever the overlapping scarcities occur, while technological "
                 "civilizations face a great filter - and the silence tells us about the filter, not about "
                 "life. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) n equals one - all conclusions are provisional; (2) chemistry is "
              "universal - the same elements and energy gradients exist everywhere; (3) the origin's "
              "difficulty is the dominant unknown. Reasoning path: separate the two questions the paradox "
              "conflates. Microbial life needs only the overlapping scarcities (energy gradient, "
              "organization, concentration) - conditions that astronomy finds common: habitable-zone planets "
              "are abundant, water is abundant, energy gradients are universal. If the origin is a ratchet "
              "rather than a miracle (see the origin record), simple life should be common wherever the "
              "overlap persists. Technological civilization is the harder step: it took four billion years "
              "on Earth, required a cascade of contingencies (oxygenation, the Cambrian toolkit, mammals "
              "surviving the asteroid), and may face a filter - nuclear, ecological, or AI-shaped - that "
              "most never pass. The silence is then expected: the galaxy may hum with microbes while "
              "broadcasting nothing. Proposed mechanism: two-rate model - high rate for simple life wherever "
              "cradle conditions persist, low and filtered rate for technosignatures. What would confirm it: "
              "a second independent biosphere (Mars subsurface, Europa ocean, or an exoplanet biosignature) "
              "proving the origin is easy, combined with continued technosignature silence proving the "
              "filter is real. What would kill it: a sterile solar system despite habitable worlds "
              "(suggesting the origin is the filter), or a confirmed technosignature (collapsing the "
              "two-rate split). What it does NOT claim: that aliens exist, that any biosignature is "
              "confirmed, or that this is established. Honest unknown: everything past the chemistry - the "
              "origin's true probability is the number the whole question hinges on."),
  "key_points": [
   "n equals 1: exactly one known biosphere; thousands of exoplanets, dozens in habitable zones.",
   "Planets are everywhere; every later Drake factor spans orders of magnitude of guesswork.",
   "Extremophiles expanded life's tolerances; ocean worlds are prime search targets.",
   "Fermi paradox (1950): the galaxy is old enough for many civilizations, yet silent.",
   "Resolutions range from rare Earth to a great filter - all untestable at n equals one."],
  "requirements": [
   "Confirm: a second independent biosphere proving the origin is easy.",
   "Confirm: continued technosignature silence consistent with a real filter.",
   "Refute: a sterile solar system despite genuinely habitable worlds.",
   "Refute: a confirmed technosignature collapsing the two-rate split."],
  "standards": [
   "Proposed path only; no aliens or biosignatures are claimed confirmed.",
   "All conclusions provisional at n equals one.",
   "The origin's true probability is honestly the hinge unknown."],
  "citations": [CIT_ASTROBIO],
 },
]

CIT_COLLECTIVE = ("Gordon DM. Ant Encounters: Interaction Networks and Colony Behavior. Princeton "
                  "University Press; 2010; Couzin ID. Collective cognition in animal groups. Trends "
                  "Cogn Sci. 2009;13:36-44.")
CIT_PLANT = ("Trewavas A. Aspects of Plant Intelligence. Ann Bot. 2003;92:1-20; Calvo P et al. "
             "Plants are intelligent, too. Nat Plants. 2020;6:1216-1217.")
CIT_VIRULENCE = ("Anderson RM, May RM. Coevolution of hosts and parasites. Parasitology. "
                 "1982;85:411-426; Alizon S et al. Virulence evolution and the trade-off hypothesis: "
                 "history, current state of affairs and the future. J Evol Biol. 2009;22:245-259.")
CIT_CHIRAL = ("Levin M. Left-right asymmetry in embryonic development: a comprehensive review. "
              "Mech Dev. 2005;122:3-25; Hirokawa N et al. Nodal flow and the generation of left-right "
              "asymmetry. Cell. 2006;125:33-45.")
CIT_VIRUS = ("Koonin EV, Starokadomskyy P. Are viruses alive? The replicator paradigm sheds decisive "
             "light on an old but misguided question. Stud Hist Philos Biol Biomed Sci. 2016;59:125-134; "
             "Forterre P. The virocell concept. Nat Rev Microbiol. 2013;11:652-653.")
CIT_CELLATLAS = ("Regev A et al. The Human Cell Atlas. eLife. 2017;6:e27041; Han X et al. Mapping the "
                 "mouse cell atlas by microwell-seq. Cell. 2018;172:1091-1107.")
CIT_LUCA = ("Weiss MC et al. The physiology and habitat of the last universal common ancestor. "
              "Nat Microbiol. 2016;1:16116; Moody ERR et al. The nature of the last universal common "
              "ancestor and its impact on the early Earth system. Nat Ecol Evol. 2024;8:1654-1666.")
CIT_THEORY = ("Koonin EV. The Logic of Chance: The Nature and Origin of Biological Evolution. FT Press; "
              "2011; Noble D. The Music of Life. Oxford University Press; 2006.")

ENTRIES += [
 {
  "key": "ants",
  "name": "How Ant Colonies Think",
  "group": "Mind and Brain",
  "ladder_rank": 27, "ladder_tier": "advanced",
  "description": ("An ant colony finds the shortest path to food, allocates workers among tasks, moves house, "
                  "and wages war - with no ant in charge and no ant understanding the plan. Gordon's harvester "
                  "ant work showed colony behavior emerging from simple interaction rules. How dumb units "
                  "compute smart outcomes - collective cognition - is still only partly understood."),
  "problem": "How do colonies of simple ants compute sophisticated decisions with no leader and no blueprint?",
  "background": ("The study of collective behavior grew from watching social insects: Deneubourg's "
                 "double-bridge experiments (1990) showed ants finding shortest paths via pheromone "
                 "reinforcement alone. Gordon's decades with harvester ants revealed task allocation emerging "
                 "from encounter rates - ants switch jobs based on whom they bump into, with no central "
                 "assignment. Couzin's models showed three simple rules (avoid collisions, align, stay close) "
                 "generating flocking, schooling, and swarming. Yet the deep questions persist: how does a "
                 "colony weigh trade-offs (speed versus accuracy in house-hunting), how is information "
                 "integrated across thousands of individuals without distortion, and where is the colony's "
                 "'memory' stored when no individual remembers? The algorithms are partially mapped; the "
                 "computational theory of the colony is not."),
  "why_it_matters": ("Colonies are existence proofs that leaderless systems can be brilliant - the design "
                      "pattern for swarm robotics, decentralized AI, and resilient organizations. Understanding "
                      "them is understanding intelligence without a brain."),
  "sig_lens": ("The Signature lens treats the colony as a covenant of encounters: no ant signs for the "
               "colony, yet every bump is a countersignature on a decision no individual made."),
  "sol_public": ("The Signature system proposes the colony is a liquid computer: information flows in "
                 "encounter rates, decisions crystallize as quorum thresholds, and memory lives in the "
                 "environment (pheromones, nest structure) rather than in any ant. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) individual ants follow simple local rules; (2) colony-level "
              "decisions are real and adaptive (shortest paths, quorum house-hunting); (3) no individual "
              "holds the colony's state. Reasoning path: the colony computes the way a liquid computes - "
              "through flow, not storage. Encounter rate is the colony's clock and census: an ant that bumps "
              "many foragers infers abundant food without any ant counting. Pheromone trails are external "
              "memory: the environment stores what no ant remembers, and evaporation is forgetting - old "
              "information literally dissipates. Quorum thresholds are the decision rule: scouts recruit to a "
              "candidate nest until a threshold number agree, then the colony commits - a distributed vote "
              "with no ballot box. Speed-accuracy trade-offs are tuned by threshold height: high thresholds "
              "wait for more evidence. The colony's 'thoughts' are thus spatiotemporal patterns of "
              "interaction, readable only at the colony scale. Proposed mechanism: liquid computation - "
              "encounter-rate sensing plus stigmergic (environment-stored) memory plus quorum thresholds. "
              "What would confirm it: predicting colony decisions purely from encounter-rate and pheromone "
              "dynamics with no individual-level parameters, and disrupting decisions by manipulating the "
              "environmental memory alone. What would kill it: colony decisions requiring individual ants to "
              "hold global state, or quorum behavior with no threshold mechanism. What it does NOT claim: "
              "that colonies are conscious, that every species uses the same algorithm, or that this is "
              "established. Honest unknown: the full algorithm catalog - how many distinct collective "
              "computations colonies run."),
  "key_points": [
   "Colonies find shortest paths, allocate labor, and choose nests with no leader.",
   "Double-bridge experiments (1990): shortest paths via pheromone reinforcement alone.",
   "Harvester ants allocate tasks by encounter rates - no central assignment.",
   "Quorum thresholds decide house-hunting: scouts recruit until enough agree.",
   "Open: trade-off tuning, distortion-free integration, and where colony memory lives."],
  "requirements": [
   "Confirm: colony decisions predicted purely from encounter-rate and pheromone dynamics.",
   "Confirm: decisions disrupted by manipulating environmental memory alone.",
   "Refute: colony decisions requiring individual ants to hold global state.",
   "Refute: quorum behavior with no threshold mechanism."],
  "standards": [
   "Proposed path only; colonies are not claimed conscious.",
   "No single algorithm is claimed for all species.",
   "The full collective algorithm catalog is honestly unmapped."],
  "citations": [CIT_COLLECTIVE],
 },
 {
  "key": "plants",
  "name": "How Plants Sense the World",
  "group": "The Cell",
  "ladder_rank": 28, "ladder_tier": "advanced",
  "description": ("Plants have no brain, no nerves, and no muscles - yet they track the sun, remember winter "
                  "to time their flowering, warn neighbors of caterpillars through the air, and a Venus "
                  "flytrap counts its prey's touches before snapping. How sessile organisms sense, remember, "
                  "and decide without a nervous system is an unsolved frontier."),
  "problem": "How do plants sense, remember, and make decisions with no brain and no nervous system?",
  "background": ("Darwin's 1880 work on plant movement launched the field; Bose's early-1900s electrical "
                 "measurements in plants were dismissed then vindicated. Modern work found the machinery: "
                 "photoreceptors tracking light direction and color, auxin gradients steering growth toward "
                 "or away from stimuli, calcium waves propagating wound signals, and volatile chemicals "
                 "warning neighbors of herbivores. Vernalization - plants 'remembering' winter via epigenetic "
                 "silencing of flowering genes - is molecular memory without neurons. The Venus flytrap counts "
                 "two touches before closing, a form of short-term memory. Yet the integration problem is "
                 "unsolved: how do distributed signals across a plant add up to coherent behavior, is there "
                 "anything like attention or choice, and the 'plant neurobiology' debate (is the vocabulary "
                 "of intelligence appropriate at all?) remains heated and unresolved."),
  "why_it_matters": ("Crops are plants; understanding their sensing means engineering drought responses, pest "
                      "warnings, and timing that could feed billions. It also redraws the map of what minds "
                      "require."),
  "sig_lens": ("The Signature lens treats the plant as a covenant of patience: rooted in place, it signs "
               "its decisions in growth - slow writing that outlasts the moment."),
  "sol_public": ("The Signature system proposes plants are slow computers: electrical and chemical waves "
                 "carry signals, growth itself is the memory, and decisions are the integration of "
                 "distributed votes across the body. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) plants sense light, gravity, touch, chemicals, and damage - "
              "proven; (2) responses are coordinated across the organism - proven; (3) coordination without "
              "a center requires distributed integration. Reasoning path: a plant is a computer that writes "
              "in growth. Signals propagate as calcium and electrical waves (fast, plant-scale) and as "
              "hormone gradients (slow, persistent). Memory is structural: vernalization stores winter as "
              "chromatin marks; a bent stem stores wind as wood. Decision is integration: the shoot grows "
              "toward the weighted sum of light, gravity, and neighbor-shade signals - a physical vote "
              "tallied in auxin. The flytrap's counting is a leaky integrator: two touches within the leak "
              "window trigger the trap, one touch decays - short-term memory without a neuron. There is no "
              "center because none is needed: the body is the integrator, and growth is the output "
              "register. Proposed mechanism: distributed sensing plus wave/gradient signaling plus growth-"
              "as-memory equals plant behavior. What would confirm it: predicting whole-plant decisions "
              "(flowering time, growth direction) purely from distributed signal integration with no "
              "central-structure parameters, and erasing plant 'memories' by reversing the growth or "
              "chromatin marks that store them. What would kill it: plant decisions requiring a "
              "centralized integrator structure, or memories with no physical storage found. What it does "
              "NOT claim: that plants are conscious, that plant intelligence equals animal intelligence, or "
              "that this is established. Honest unknown: whether anything in the plant corresponds to "
              "attention or preference rather than weighted integration."),
  "key_points": [
   "Plants track sun, remember winter (vernalization), warn neighbors of herbivores, count touches (flytrap).",
   "Machinery: photoreceptors, auxin gradients, calcium waves, volatile warning chemicals.",
   "Vernalization is molecular memory via epigenetic silencing - no neurons needed.",
   "The plant neurobiology debate: is intelligence vocabulary appropriate? Unresolved.",
   "Open: how distributed signals integrate into coherent behavior."],
  "requirements": [
   "Confirm: whole-plant decisions predicted purely from distributed signal integration.",
   "Confirm: plant memories erased by reversing their physical storage.",
   "Refute: plant decisions requiring a centralized integrator.",
   "Refute: memories with no physical storage found."],
  "standards": [
   "Proposed path only; plants are not claimed conscious.",
   "Plant intelligence is not equated with animal intelligence.",
   "Attention-like phenomena are honestly unresolved."],
  "citations": [CIT_PLANT],
 },
 {
  "key": "virulence",
  "name": "What Drives Virulence Evolution",
  "group": "Immunity and Microbes",
  "ladder_rank": 29, "ladder_tier": "advanced",
  "description": ("Why does Ebola kill most of its hosts while the common cold barely inconveniences them? "
                  "Killing your host looks like evolutionary suicide - a dead host cannot spread you. Yet "
                  "virulence varies enormously and evolves rapidly. The trade-off hypothesis says pathogens "
                  "balance transmission against host death, but reality keeps violating the neat curve."),
  "problem": "Why are some pathogens deadly and others mild - what sets and changes virulence?",
  "background": ("The conventional wisdom was once that pathogens evolve toward mildness (the 'avirulence' "
                 "myth). Anderson and May's 1982 models replaced it with the trade-off hypothesis: virulence "
                 "is the price of transmission - more replication means more spread but a sicker, possibly "
                 "dead host, so evolution tunes virulence to maximize the product. Myxoma virus in Australian "
                 "rabbits became the textbook case: extreme virulence attenuated over decades toward an "
                 "intermediate optimum. But exceptions abound: vector-borne diseases can afford high virulence "
                 "(the mosquito does the moving), virulence sometimes evolves upward with vaccination "
                 "(Marek's disease in chickens), and within-host competition can drive runaway virulence. The "
                 "trade-off curve's shape - the actual biology constraining each pathogen - is unknown for "
                 "most diseases, and predicting virulence evolution (the question behind every pandemic's "
                 "trajectory) remains unreliable."),
  "why_it_matters": ("Every emerging pathogen poses the virulence question: will it attenuate like myxoma "
                      "or escalate like Marek's? The answer shapes vaccine strategy, pandemic planning, and "
                      "whether interventions accidentally breed worse diseases."),
  "sig_lens": ("The Signature lens treats virulence as a covenant negotiated in transmission: the pathogen "
               "signs for as much replication as the host's mobility will underwrite."),
  "sol_public": ("The Signature system proposes virulence is priced by the transmission route: the pathogen "
                 "spends host health to buy spread, and the exchange rate is set by how the pathogen travels - "
                 "so virulence evolves toward whatever the route can afford. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) pathogens maximize lifetime transmission, not host survival; "
              "(2) transmission requires host mobility or a vector; (3) replication buys transmission at "
              "the price of host damage. Reasoning path: the trade-off is an exchange rate, and the route "
              "sets it. A directly transmitted pathogen needs its host walking around - killing quickly "
              "bankrupts transmission, so virulence settles low (common cold). A vector-borne pathogen "
              "outsources mobility to mosquitoes - the host can be bedridden or dying and transmission "
              "continues, so virulence settles high (malaria). A waterborne pathogen outsources to water "
              "itself - cholera's purging diarrhea is transmission, so extreme virulence pays. Vaccination "
              "changes the rate: leaky vaccines that prevent disease but not transmission let virulent "
              "strains spread from protected hosts - the Marek's disease escalation. Within-host competition "
              "is a bidding war: multiple strains in one host select for the fastest replicator regardless "
              "of host cost. Proposed mechanism: virulence equals the transmission route's affordable price, "
              "modulated by competition and intervention. What would confirm it: virulence optima shifting "
              "predictably when a pathogen's transmission route is experimentally altered, and intervention "
              "strategies designed from the route-price model preventing Marek's-style escalation. What "
              "would kill it: virulence optima indifferent to transmission route across many pathogens, or "
              "escalation under sterilizing (transmission-blocking) immunity. What it does NOT claim: that "
              "any specific pathogen's future virulence is predictable today, that attenuation is "
              "inevitable, or that this is established. Honest unknown: the quantitative exchange rates for "
              "most real pathogens."),
  "key_points": [
   "Ebola kills most hosts; common colds barely sicken - virulence varies enormously.",
   "The avirulence myth fell to Anderson and May (1982): virulence is priced by transmission.",
   "Myxoma virus attenuated toward an intermediate optimum - the textbook trade-off.",
   "Exceptions: vector-borne and waterborne routes afford high virulence; leaky vaccines drove Marek's escalation.",
   "Open: the trade-off curve's shape for most pathogens; predicting pandemic trajectories."],
  "requirements": [
   "Confirm: virulence optima shifting predictably with experimental transmission-route changes.",
   "Confirm: route-price-designed interventions preventing vaccine-driven escalation.",
   "Refute: virulence optima indifferent to transmission route across many pathogens.",
   "Refute: escalation under sterilizing transmission-blocking immunity."],
  "standards": [
   "Proposed path only; no specific pathogen's future is claimed predictable.",
   "Attenuation is not claimed inevitable.",
   "Quantitative exchange rates are honestly unknown for most pathogens."],
  "citations": [CIT_VIRULENCE],
 },
 {
  "key": "chirality",
  "name": "Why Bodies Mirror Left and Right",
  "group": "Development",
  "ladder_rank": 30, "ladder_tier": "advanced",
  "description": ("Your heart is on the left, your liver on the right - and in one person in ten thousand, "
                  "the arrangement is perfectly mirrored with no ill effects. Embryos start symmetric, then "
                  "reliably break symmetry the same way every time. How a ball of identical cells decides "
                  "left from right - consistently, across billions of births - was a mystery until 2006, and "
                  "parts of it still are."),
  "problem": "How does a symmetric embryo reliably break left-right symmetry the same way every time?",
  "background": ("For a century the mechanism was unknown; the heart's leftward looping was described but "
                 "unexplained. The breakthrough came from the mouse node: Hirokawa's group (2006) showed that "
                 "tiny rotating cilia at the embryo's midline drive a leftward fluid flow - nodal flow - and "
                 "this flow breaks symmetry. Levin's earlier work had implicated ion channels and serotonin "
                 "in chick embryos, suggesting multiple upstream inputs. Downstream, the Nodal signaling "
                 "cascade amplifies the initial tiny bias into the full left-right body plan. Yet puzzles "
                 "remain: how does fluid flow become asymmetric gene expression (the mechanosensor is still "
                 "debated), why do some species use cilia and others apparently do not, and how is the "
                 "initial bias so reliable when it starts from molecular noise? Situs inversus - complete "
                 "mirror reversal - shows the system has exactly two stable outcomes, a precision that "
                 "demands explanation."),
  "why_it_matters": ("Left-right patterning errors cause severe birth defects of the heart and organs; the "
                      "symmetry-breaking mechanism is also the simplest model of how noise becomes reliable "
                      "information - a principle with applications from development to nanotechnology."),
  "sig_lens": ("The Signature lens treats left-right as the covenant's first signature: the embryo signs "
               "its symmetry away exactly once, and every organ countersigns the choice."),
  "sol_public": ("The Signature system proposes symmetry breaks by amplified whisper: rotating cilia create "
                 "a barely-there leftward flow, sensors read the whisper, and a feedback cascade amplifies "
                 "it into an irreversible left-right decision. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the early embryo is truly symmetric - no hidden left-right "
              "information; (2) the break must be both reliable (same outcome every time) and binary "
              "(left or mirror, nothing between); (3) molecular chirality (rotating cilia) is the only "
              "available asymmetric input. Reasoning path: the problem is turning a whisper into a decree. "
              "Cilia rotate clockwise (viewed from above) because of their molecular handedness; tilted "
              "rotation drags fluid leftward - a tiny, consistent bias from the molecular scale. Immotile "
              "sensory cilia at the node's edge detect the flow (the mechanosensor, likely polycystin "
              "channels), converting fluid bias into a calcium signal slightly stronger on the left. Then "
              "the Nodal cascade does the amplification: Nodal activates its own expression (positive "
              "feedback) while inducing its inhibitor Lefty, which diffuses faster - a classic "
              "activator-inhibitor system that converts a slight left bias into all-or-nothing left-sided "
              "gene expression. Reliability comes from the cascade's bistability: intermediate states are "
              "unstable, so the embryo lands on left or mirror-left, never halfway. Proposed mechanism: "
              "ciliary flow plus flow sensing plus bistable amplification equals the left-right decision. "
              "What would confirm it: identifying the flow sensor definitively and showing sensor-gain "
              "manipulation tuning the reliability of the outcome, plus reconstituting the three-step "
              "chain in an engineered system. What would kill it: normal left-right patterning with "
              "provably no flow and no ciliary input in a mammal, or a non-bistable cascade producing "
              "reliable outcomes. What it does NOT claim: that every species uses cilia, that the sensor "
              "is identified, or that this is established. Honest unknown: the sensor's identity and how "
              "non-ciliary species break symmetry."),
  "key_points": [
   "Heart left, liver right - reliably, across billions of births; mirror reversal (situs inversus) is harmless.",
   "Nodal flow (Hirokawa 2006): rotating cilia drive leftward fluid flow at the mouse node.",
   "Nodal cascade amplifies the tiny bias via activator-inhibitor feedback into all-or-nothing asymmetry.",
   "Bistability explains reliability: left or mirror, never halfway.",
   "Open: the flow sensor's identity; how non-ciliary species break symmetry."],
  "requirements": [
   "Confirm: definitive flow-sensor identification with gain manipulation tuning outcome reliability.",
   "Confirm: the three-step chain reconstituted in an engineered system.",
   "Refute: normal mammalian left-right patterning with provably no flow or ciliary input.",
   "Refute: a non-bistable cascade producing reliable binary outcomes."],
  "standards": [
   "Proposed path only; ciliary universality is not claimed.",
   "The sensor is not claimed identified.",
   "Non-ciliary symmetry breaking is honestly unexplained."],
  "citations": [CIT_CHIRAL],
 },
 {
  "key": "viruses",
  "name": "What Viruses Really Are",
  "group": "Immunity and Microbes",
  "ladder_rank": 31, "ladder_tier": "advanced",
  "description": ("Viruses outnumber stars in the observable universe by ten orders of magnitude - an "
                  "estimated 10^31 on Earth alone. They have genes and evolve, but no metabolism, no cells, "
                  "and no independent reproduction. Are they alive? The question sounds philosophical, but it "
                  "is practical: viral 'dark matter' - the majority of viral genes with no known function - "
                  "may be biology's largest unexplored continent."),
  "problem": "What are viruses - living things, escaped genes, or something else - and what does their dark matter do?",
  "background": ("Viruses were discovered as filterable poisons (Ivanovsky 1892, Beijerinck 1898) before "
                 "anyone saw one. The living-or-not debate ran for a century: they evolve and have genes "
                 "(alive-like) but do nothing metabolically outside a host (not-alive-like). Koonin's "
                 "replicator paradigm reframed it: viruses are replicators, members of the same world as "
                 "cells, distinguished by their reproductive strategy rather than a life certificate. "
                 "Forterre's virocell concept argues the infected cell - not the virion - is the living form. "
                 "Giant viruses (Mimivirus, 2003) blurred every line, carrying genes once thought "
                 "cell-exclusive. Metagenomics then revealed viral dark matter: most viral sequences match "
                 "nothing known. Viruses also emerge as major evolutionary players - 8 percent of the human "
                 "genome is retroviral fossils, and placental mammals may owe a key gene (syncytin) to an "
                 "ancient virus."),
  "why_it_matters": ("Viral dark matter is the largest unexplored gene pool on Earth - new enzymes, new "
                      "defenses, possibly new biology. And the definition of life decides what we search for "
                      "on other worlds."),
  "sig_lens": ("The Signature lens treats viruses as covenants without a body: signatures that cannot "
               "sign for themselves, borrowing the cell's hand to write their name again."),
  "sol_public": ("The Signature system proposes viruses are the biosphere's gene couriers: stripped-down "
                 "replicators that trade independence for mobility, and their dark matter is the courier "
                 "network's working toolkit - mostly host-manipulation machinery we have not decoded. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the living-or-not question is a category error - replicator "
              "strategy is the real distinction; (2) viral dark matter's size implies function, not junk; "
              "(3) viruses and cells co-evolved from the start. Reasoning path: stop asking for a life "
              "certificate and ask what strategy the entity runs. Cells run the stay-and-metabolize strategy; "
              "viruses run the travel-light-and-borrow strategy - maximum genes per gram, zero metabolic "
              "overhead, reproduction outsourced to hosts. Both are replicators; the biosphere needs both, "
              "the way an economy needs both factories and couriers. The virocell - the infected cell "
              "reprogrammed into a virus factory - is then the virus's true living form, and the virion is "
              "its spore: dormancy and dispersal, not death. Viral dark matter is the courier's toolkit: "
              "genes for entering cells, evading immunity, reprogramming metabolism - host-manipulation "
              "machinery under intense selection to be unrecognizable, which is exactly why it matches "
              "nothing in our databases. Endogenous retroviruses (8 percent of us) are retired couriers "
              "whose tools the host kept - syncytin building the placenta is the proof of concept. Proposed "
              "mechanism: virus equals mobile replicator strategy; dark matter equals host-manipulation "
              "toolkit under diversifying selection. What would confirm it: functional screens assigning "
              "host-manipulation roles to a large fraction of dark-matter genes, and the virocell showing "
              "metabolic and evolutionary dynamics distinct from both uninfected cell and virion. What would "
              "kill it: dark matter proving to be mostly non-functional baggage, or viruses shown to be "
              "recent escaped genes with no ancient lineage. What it does NOT claim: that the debate is "
              "settled, that all dark matter is functional, or that this is established. Honest unknown: "
              "the actual functions of most dark-matter genes and the true age of the viral world."),
  "key_points": [
   "~10^31 viruses on Earth; most viral genes match nothing known - viral dark matter.",
   "Discovered as filterable agents (1890s); the living-or-not debate ran a century.",
   "Giant viruses (2003) carry cell-like genes, blurring every boundary.",
   "8 percent of the human genome is retroviral fossils; syncytin (placenta) came from a virus.",
   "Virocell concept: the infected cell, not the virion, is the living form."],
  "requirements": [
   "Confirm: functional screens assigning host-manipulation roles to much dark matter.",
   "Confirm: the virocell showing distinct metabolic and evolutionary dynamics.",
   "Refute: dark matter proving mostly non-functional baggage.",
   "Refute: viruses proven recent escaped genes with no ancient lineage."],
  "standards": [
   "Proposed path only; the definition debate is not claimed settled.",
   "Not all dark matter is claimed functional.",
   "Dark-matter functions and viral antiquity are honestly open."],
  "citations": [CIT_VIRUS],
 },
 {
  "key": "cellatlas",
  "name": "Can We Map Every Cell in the Human Body",
  "group": "The Cell",
  "ladder_rank": 32, "ladder_tier": "advanced",
  "description": ("Your body holds some 37 trillion cells in perhaps thousands of types - and until recently, "
                  "no one knew the full inventory. The Human Cell Atlas, launched in 2016, aims to map every "
                  "cell type, where it lives, and what it does. But is the map completable? Cell types blur "
                  "into continuous states, rare cells hide, and a cell's identity changes with context. The "
                  "complete parts list of a human being is still unwritten."),
  "problem": "Can we produce a complete map of every cell type in the human body - and is 'cell type' even a fixed category?",
  "background": ("Cell types were historically defined by shape and stain - a few hundred catalogued. "
                 "Single-cell RNA sequencing (2010s) exploded the count: the brain alone went from dozens to "
                 "thousands of transcriptomic types. The Human Cell Atlas (Regev et al., 2017) set the "
                 "moonshot goal: every cell, mapped. But the deeper the sequencing goes, the blurrier the "
                 "categories get: cells form continua rather than neat types, the same transcriptome behaves "
                 "differently in different tissues, and transient states (a cell mid-division, mid-response) "
                 "may outnumber stable types. Rare cells - one in a million - are statistically invisible to "
                 "current sampling. The field now debates whether the atlas will converge on a finite parts "
                 "list or reveal that 'cell type' is a useful fiction over a continuous landscape."),
  "why_it_matters": ("Every disease is a cell-type disease - cancer, autoimmunity, neurodegeneration all "
                      "strike specific cells. A complete atlas is the reference manual for all of medicine; "
                      "an impossible one means medicine must work with landscapes, not lists."),
  "sig_lens": ("The Signature lens treats the atlas as a census of covenants: every cell a signed role, "
               "but the signatures shade into one another like handwriting, not stamps."),
  "sol_public": ("The Signature system proposes the atlas converges as a landscape, not a list: cell "
                 "identity is a position on continuous terrain, stable types are the valleys, and the map "
                 "is completable as a terrain model rather than a stamp collection. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) single-cell data shows continua, not just clusters; "
              "(2) function constrains identity - a cell's job limits how far it can drift; "
              "(3) the atlas's value is medical reference, so completeness means clinical sufficiency. "
              "Reasoning path: the stamp-collection model (finite discrete types) fails because "
              "transcriptomes vary continuously; but the pure-continuum model fails too, because function "
              "quantizes - a cell either contracts or it does not, secretes insulin or does not. The "
              "resolution is Waddington's landscape again: stable types are attractor valleys, continua are "
              "the slopes between them, and transient states are cells caught mid-slope. The atlas is then "
              "completable as a terrain map: finite valleys, mapped slopes, with rare cells as small but "
              "real valleys found by targeted sampling. 'Cell type' survives as 'attractor basin' - a "
              "dynamical definition replacing the morphological one. Sampling math sets the strategy: common "
              "valleys from broad surveys, rare valleys from enriched hunts, slopes from trajectory "
              "inference. Proposed mechanism: the human cell census equals a finite attractor landscape; "
              "completeness is achieved valley by valley with slope interpolation. What would confirm it: "
              "the atlas converging - new surveys adding slopes and rare valleys but no new major valleys - "
              "and valley membership predicting cell function and disease vulnerability better than "
              "cluster labels. What would kill it: unbounded new major valleys with every deeper survey, or "
              "valley membership failing to predict function. What it does NOT claim: that the atlas is "
              "nearly done, that continua do not matter medically, or that this is established. Honest "
              "unknown: the true valley count and whether any tissue is pure slope."),
  "key_points": [
   "~37 trillion cells; the brain alone went from dozens to thousands of transcriptomic types.",
   "Human Cell Atlas (2016): the moonshot to map every cell.",
   "Cells form continua, not neat types; context changes identity; rare cells evade sampling.",
   "Transient states may outnumber stable types.",
   "Open: finite parts list or continuous landscape - is 'cell type' a fixed category?"],
  "requirements": [
   "Confirm: atlas convergence - new surveys adding only slopes and rare valleys.",
   "Confirm: valley membership predicting function and disease vulnerability over cluster labels.",
   "Refute: unbounded new major valleys with every deeper survey.",
   "Refute: valley membership failing to predict function."],
  "standards": [
   "Proposed path only; the atlas is not claimed nearly done.",
   "Continua are granted medical relevance.",
   "The valley count is honestly unknown."],
  "citations": [CIT_CELLATLAS],
 },
 {
  "key": "luca",
  "name": "What LUCA Was Really Like",
  "group": "Life and Its Origins",
  "ladder_rank": 33, "ladder_tier": "advanced",
  "description": ("Every living thing - you, the oak, the bacterium in the vent - descends from one population: "
                  "the Last Universal Common Ancestor, LUCA, roughly four billion years ago. Genomic "
                  "reconstructions say LUCA already had hundreds of genes, a DNA genome, and a sophisticated "
                  "metabolism. But was it a free-living cell or a community of replicators? Hot vent dweller or "
                  "surface pond native? The ancestor of everything remains a sketch."),
  "problem": "What was the Last Universal Common Ancestor actually like - cell, community, or something stranger?",
  "background": ("Woese's ribosomal RNA work (1970s-90s) proved the three domains of life and implied their "
                 "common ancestor. Gene-content reconstructions (Weiss et al. 2016) assigned LUCA 355 gene "
                 "families: a DNA genome, ATP synthesis, the genetic code, and enzymes for an anaerobic, "
                 "hydrogen-dependent metabolism suited to hydrothermal vents. A 2024 update pushed LUCA's "
                 "complexity higher and its age to ~4.2 billion years - astonishingly early and sophisticated. "
                 "But reconstructions disagree on fundamentals: whether LUCA had a membrane (some analyses "
                 "find no membrane-lipid genes in common), whether it was a single cell or a communal gene "
                 "pool swapping freely (Woese's progenote hypothesis), and whether the vent chemistry is "
                 "ancestral or a later adaptation. LUCA may have been less an organism than a process - and "
                 "the sketch keeps changing."),
  "why_it_matters": ("LUCA is the root of the tree: its nature constrains every origin-of-life theory (the "
                      "origin must produce something LUCA-like) and defines the minimal toolkit of life "
                      "itself."),
  "sig_lens": ("The Signature lens treats LUCA as the first signed covenant of life: not necessarily one "
               "cell, but the first system whose signature - the genetic code - every descendant still honors."),
  "sol_public": ("The Signature system proposes LUCA was a covenant community: a vent-bound gene-trading "
                 "collective whose members shared innovations freely, with the genetic code as the shared "
                 "signature that let the trading work - cellular individuality came later. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) gene-content reconstructions are broadly right about LUCA's "
              "metabolic sophistication; (2) early gene transfer was rampant (progenote era); "
              "(3) vent chemistry matches LUCA's reconstructed metabolism too well to be coincidence. "
              "Reasoning path: the reconstructions' paradox - sophisticated genes, possibly no membrane - "
              "dissolves if LUCA was not one cell but a community. In a vent's mineral compartments, "
              "replicator collectives trade genes freely; selection acts on the collective's shared toolkit. "
              "The genetic code's universality is the proof of the trading: a code can only become universal "
              "if everyone is swapping parts - once frozen, the code locks the community into compatibility. "
              "Cellular individuality (private membranes, vertical inheritance) evolved later, multiple times, "
              "as collectives privatized - which is why the three domains have different membrane lipids: "
              "they invented cellularity independently from the shared code. LUCA's age (~4.2 billion years) "
              "then means the code froze fast, while bodies took eons. Proposed mechanism: LUCA equals a "
              "vent-bound gene-trading collective with a frozen shared code; cells are the later "
              "privatization. What would confirm it: membrane-lipid genes proving non-universal (independent "
              "cellular inventions), and pre-cellular gene-trading signatures preserved in the deepest gene "
              "families. What would kill it: a LUCA reconstruction with a complete private membrane toolkit "
              "and no trading signal, or the code proving freezable without communal exchange. What it does "
              "NOT claim: that the vent location is proven, that LUCA's full gene set is known, or that "
              "this is established. Honest unknown: whether LUCA was one collective or many, and the true "
              "chronology of privatization."),
  "key_points": [
   "All life descends from LUCA, ~4 billion years ago; reconstructions credit it with 355+ gene families.",
   "2024 update: LUCA more complex and older (~4.2 billion years) than thought.",
   "Paradox: sophisticated metabolism but possibly no membrane-lipid genes in common.",
   "Three domains have different membrane lipids - hinting at independent cellularity.",
   "Open: single cell, gene-trading community (progenote), or something stranger."],
  "requirements": [
   "Confirm: membrane-lipid genes proving non-universal across domains.",
   "Confirm: pre-cellular gene-trading signatures in the deepest gene families.",
   "Refute: a LUCA with complete private membrane toolkit and no trading signal.",
   "Refute: the code proving freezable without communal exchange."],
  "standards": [
   "Proposed path only; vent location is not claimed proven.",
   "LUCA's full gene set is not claimed known.",
   "Collective count and privatization chronology are honestly open."],
  "citations": [CIT_LUCA],
 },
 {
  "key": "theory",
  "name": "What a Complete Theory of Biology Would Look Like",
  "group": "Life and Its Origins",
  "ladder_rank": 34, "ladder_tier": "advanced",
  "description": ("Physics has the Standard Model - a compact theory from which much follows. Biology has "
                  "evolution by natural selection, the closest thing to a universal law, and then a vast "
                  "archipelago of mechanisms with no bridge between them. Is a complete, unified theory of "
                  "biology possible, or is life too historically contingent - too frozen-accident - for "
                  "lawlike unity? The question caps every other unsolved problem in this database."),
  "problem": "Can biology have a complete unified theory like physics, or does life's historical contingency forbid it?",
  "background": ("The Modern Synthesis (1930s-40s) unified evolution and genetics - biology's greatest "
                 "unification. Since then, unification attempts kept coming: systems biology's network laws, "
                 "Kauffman's order-for-free, the extended evolutionary synthesis incorporating development "
                 "and epigenetics, attempts at universal scaling laws (West, Brown, Enquist). Each captured "
                 "something real and fell short of completeness. The contingency objection - Gould's 'replay "
                 "the tape of life' - argues biology is dominated by frozen accidents (the genetic code, "
                 "left-handed amino acids) that no law predicts. The counter-argument: convergence shows "
                 "the tape replays similarly - eyes evolved 40+ times, eusociality repeatedly - implying "
                 "lawlike attractors beneath the accidents. No framework yet derives the living world the "
                 "way statistical mechanics derives thermodynamics, and whether one can exist is itself "
                 "unsolved."),
  "why_it_matters": ("A complete theory would be biology's periodic table: the frame that turns a "
                      "collection of facts into a predictive science - and the test of whether life is "
                      "understandable in principle, not just describable in practice."),
  "sig_lens": ("The Signature lens treats the complete theory as the master covenant: every mechanism in "
               "this database a clause, evolution the consideration, and the whole archipelago one signed "
               "document."),
  "sol_public": ("The Signature system proposes the unified theory is a theory of the possible: not laws "
                 "predicting which accidents happened, but laws of the adjacent possible - the space of "
                 "forms life can reach - with contingency choosing the path and law governing the terrain. "
                 "Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) physics-style prediction of specific outcomes is impossible for "
              "historical systems; (2) convergence is real and demands explanation; (3) a theory can be "
              "complete without being predictive of accidents. Reasoning path: the contingency objection "
              "misidentifies what a biological theory must do. Thermodynamics does not predict which "
              "molecules collide; it governs the ensemble. A complete biology would likewise govern the "
              "ensemble of the possible: the adjacent possible (Kauffman) - the set of forms reachable from "
              "current life in one innovation step. Laws of the adjacent possible would state which "
              "innovations are accessible, which attractors (eyes, wings, eusociality) the terrain funnels "
              "toward, and what trade-offs (rate versus yield, robustness versus evolvability) bound every "
              "path. Contingency then chooses the path through law-governed terrain - the tape of life "
              "replays differently in detail but similarly in structure, which is exactly what convergence "
              "shows. Evolution by natural selection is the first such law (the law of the hill-climb); the "
              "complete theory adds the laws of the landscape: scaling laws, network motifs, the major "
              "transitions as terrain features. Proposed mechanism: biology's unification equals the laws "
              "of the adjacent possible plus selection's hill-climb - prediction of the reachable, not the "
              "actual. What would confirm it: a formalized adjacent-possible framework predicting which "
              "innovations evolve repeatedly (convergent attractors) versus once (frozen accidents) across "
              "independent lineages, with experimental evolution as the test bench. What would kill it: "
              "convergence proving illusory under rigorous analysis, or the reachable space proving "
              "unformalizable in principle. What it does NOT claim: that such a theory exists today, that "
              "contingency will ever be tamed into prediction, or that this is established. Honest "
              "unknown: whether the adjacent possible is formalizable at all - the question beneath the "
              "question."),
  "key_points": [
   "Physics has the Standard Model; biology has natural selection plus an archipelago of mechanisms.",
   "Modern Synthesis (1930s-40s): biology's greatest unification; nothing comparable since.",
   "Contingency objection (Gould): frozen accidents dominate; replay the tape, get a different world.",
   "Convergence counter: eyes 40+ times, eusociality repeatedly - lawlike attractors beneath accidents.",
   "Open: whether a complete predictive theory of biology can exist in principle."],
  "requirements": [
   "Confirm: a formalized adjacent-possible framework predicting convergent versus frozen outcomes.",
   "Confirm: experimental evolution validating attractor predictions across lineages.",
   "Refute: convergence proving illusory under rigorous analysis.",
   "Refute: the reachable space proving unformalizable in principle."],
  "standards": [
   "Proposed path only; no such theory is claimed to exist today.",
   "Contingency is not claimed tamed into prediction.",
   "Formalizability of the adjacent possible is honestly the deepest unknown."],
  "citations": [CIT_THEORY],
 },
]
