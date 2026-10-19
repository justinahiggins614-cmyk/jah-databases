#!/usr/bin/env python3
"""Entries 13-24 (Compounded tier) for the Unsolved Neuroscience databases."""

ENTRIES_B = [
{
 "key": "full_function_of_sleep",
 "name": "What the Full Function of Sleep Is",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": ("Every animal with a nervous system sleeps, and humans who go "
             "without it for days develop hallucinations, immune failure, "
             "and eventually death in animal models. Sleep is one of the "
             "most universal and most expensive behaviors in biology — "
             "eight hours a day of vulnerability — yet no single account "
             "explains all of what sleep does. Memory, metabolism, "
             "immunity, emotion, and brain cleaning all claim a piece, but "
             "the full function of sleep, the reason it is worth the "
             "enormous cost, remains unsolved."),
 "background": ("The modern science of sleep began with the "
                "electroencephalogram and the discovery of REM sleep in "
                "1953. Allan Rechtschaffen and colleagues showed that total "
                "sleep deprivation kills rats within weeks, proving sleep "
                "is not optional. The memory camp, led by researchers like "
                "Jan Born, showed sleep replays and consolidates memories; "
                "the synaptic homeostasis hypothesis of Giulio Tononi and "
                "Chiara Cirelli proposed sleep globally downscales synapses "
                "to keep the brain's energy budget balanced. In 2013 Maiken "
                "Nedergaard's team discovered the glymphatic system: during "
                "sleep, cerebrospinal fluid washes through the brain, "
                "clearing metabolic waste including the amyloid proteins "
                "linked to Alzheimer's. Matthew Walker's synthesis ties "
                "sleep to emotion, immunity, and learning. Each function is "
                "real; the unsolved question is whether they are separate "
                "jobs sharing one state, or facets of one deeper function — "
                "and why evolution never found a cheaper way."),
 "why_it_matters": ("A third of human life is spent asleep, and modern "
                    "society is chronically short of it. If sleep's core "
                    "function were known, we could design around it: "
                    "protect the essential part, treat insomnia at its "
                    "root, and understand why sleep loss predicts "
                    "everything from Alzheimer's to depression. It is the "
                    "highest-leverage unsolved problem in daily human "
                    "biology."),
 "sig_lens": ("Signature lens: sleep is the brain's maintenance shift — "
              "the Signature view treats the sleeping brain as a facility "
              "that cannot serve customers and repair itself at the same "
              "time."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The waking brain accumulates three kinds of debt: "
  "informational (unconsolidated learning), metabolic (waste products), "
  "and synaptic (runaway potentiation raising energy costs). (2) All "
  "three can only be serviced when the brain is decoupled from the "
  "world. (3) Evolution bundled the servicing into one state because the "
  "decoupling itself is the expensive part. "
  "REASONING PATH. The Signature approach proposes that sleep is not one "
  "function but one decoupling event with three mandatory service "
  "routines — and the reason they share a state is that each requires "
  "the others' silence. Memory replay needs the sensory stream off; "
  "glymphatic washing needs the interstitial space expanded, which "
  "requires reduced neural firing; synaptic downscaling needs a global "
  "signal that would corrupt waking perception. The 'core function' "
  "debate dissolves: asking which routine is the real purpose of sleep "
  "is like asking which chore is the real purpose of closing a shop. "
  "REM and non-REM are two different service modes — non-REM runs the "
  "physical maintenance (washing, downscaling), REM runs the "
  "informational maintenance (replay, emotional reprocessing) — and the "
  "nightly cycling between them is the service schedule. "
  "PROPOSED MECHANISM. Sleep onset is triggered when any of the three "
  "debt meters crosses threshold; the brain then cycles through "
  "service modes in order of urgency, which is why deep sleep "
  "dominates early night (physical debt is most urgent) and REM "
  "dominates late night. Dreaming is the informational routine's "
  "visible exhaust. "
  "WHAT WOULD CONFIRM IT. If the three debt meters could be measured "
  "independently and shown to each gate specific sleep stages — with "
  "selective debt in one domain shifting only its corresponding stage — "
  "the bundled-service proposal gains support. "
  "WHAT WOULD REFUTE IT. If one routine proved fully serviceable "
  "during waking with no decoupling cost, or if a sleepless animal "
  "showed zero accumulation on all three debts, the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the three debts are "
  "exhaustive, it does not offer medical advice about sleep, and it "
  "does not claim proof."),
 "key_points": [
  "Total sleep deprivation is lethal in animal models; sleep is biologically mandatory.",
  "Memory replay, synaptic downscaling, and glymphatic waste clearance are all real sleep functions.",
  "The unsolved question is whether they are separate jobs or facets of one deeper function.",
  "The Signature proposal: sleep is one decoupling event with three mandatory service routines; the decoupling is the expensive part they must share.",
  "Independent debt meters gating specific sleep stages would confirm it; a fully waking-serviceable routine would refute it."],
 "requirements": [
  "Accept three debt types: informational, metabolic, and synaptic.",
  "Require decoupling from the world for all three service routines.",
  "Treat REM and non-REM as informational versus physical service modes.",
  "Require debt meters to gate their corresponding sleep stages.",
  "Keep the account descriptive; no medical advice."],
 "standards": [
  "Polysomnographic sleep staging (AASM).",
  "Glymphatic clearance imaging methods.",
  "Sleep-deprivation and selective-stage-deprivation designs."],
 "citations": [
  "Tononi G, Cirelli C. Sleep and the price of plasticity. Neuron; 2014.",
  "Xie L, et al. Sleep drives metabolite clearance from the adult brain. Science; 2013.",
  "Walker M. Why We Sleep. Scribner; 2017."],
},
{
 "key": "the_neural_code",
 "name": "How Information Is Encoded in Spike Trains",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": ("Neurons communicate in spikes — brief electrical pulses — "
             "and everything the brain knows, perceives, and decides is "
             "carried by patterns of these pulses across billions of "
             "cells. The neural code is the mapping between spike patterns "
             "and the information they carry. After seventy years of "
             "recording spikes, the field still cannot say how the brain "
             "reads its own code: does it count spikes, measure their "
             "timing, listen to populations, or use all of these at once?"),
 "background": ("Edgar Adrian showed in the 1920s that stronger stimuli "
                "produce higher spike rates — the rate code, the first and "
                "simplest proposal. But recordings soon showed spike timing "
                "carries information rate alone cannot: in the auditory "
                "system, microsecond timing differences locate sound; in "
                "the visual system, the relative timing of first spikes "
                "encodes stimuli faster than rates could. The population "
                "code emerged from Georgopoulos's 1980s work on arm "
                "movements, where each neuron votes with its preferred "
                "direction and the population vector points the way. "
                "Information theory entered through Rieke, Warland, and "
                "Bialek's 'Spikes' (1997), quantifying bits per spike. "
                "Synchrony codes, phase codes, and rank-order codes each "
                "have their champions. The deepest problem is the "
                "readout: whatever code theorists propose, some downstream "
                "neuron must decode it with only synapses and spikes — "
                "and no experiment has yet shown which code the brain's "
                "own readers actually use."),
 "why_it_matters": ("The neural code is the brain's language. Cracking it "
                    "would unlock brain-computer interfaces that read "
                    "intentions directly, prosthetics that speak the "
                    "nervous system's native tongue, and artificial "
                    "networks built on the brain's actual coding "
                    "principles rather than guesses. It is the key to "
                    "everything downstream."),
 "sig_lens": ("Signature lens: the code is whatever the reader can read — "
              "the Signature view treats the neural code as defined by "
              "the decoder, not by the theorist."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) There is no single neural code; different circuits "
  "use different codes. (2) The code in each circuit is whatever its "
  "downstream readers can decode with spikes and synapses. (3) The brain "
  "is redundant: the same information is carried in rate, timing, and "
  "population patterns simultaneously. "
  "REASONING PATH. The Signature approach dissolves the rate-versus-"
  "timing war by proposing the brain is multilingual by design. Fast "
  "circuits that must act in milliseconds — like the auditory "
  "brainstem — use timing codes, because rates are too slow. Slow "
  "integrative circuits — like prefrontal cortex — use rate codes, "
  "because they have time to count. Population codes are the "
  "error-correcting layer: single neurons are noisy, so information is "
  "spread across many, and the reader pools them. The redundancy is "
  "the point: if one channel degrades, the others carry the message. "
  "Theorists arguing for one true code are like linguists arguing for "
  "one true human language — the brain speaks several, each fit to its "
  "circuit's speed and noise. "
  "PROPOSED MECHANISM. Each circuit's code is set by its reader's "
  "integration window: readers with short windows decode timing, "
  "readers with long windows decode rate, and convergent readers "
  "decode populations. The code can be read off the anatomy — window "
  "lengths, convergence ratios, and noise levels predict which code a "
  "circuit uses. "
  "WHAT WOULD CONFIRM IT. If a circuit's empirically measured code "
  "matched the code predicted from its readers' biophysics — with "
  "mismatches (timing code into a slow reader) failing to transmit "
  "information — the reader-defined proposal gains support. "
  "WHAT WOULD REFUTE IT. If a single universal code were found used "
  "identically across fast and slow circuits regardless of reader "
  "biophysics, the multilingual proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the full codebook of any "
  "circuit is known, it does not claim redundancy is always present, "
  "and it does not claim proof."),
 "key_points": [
  "Adrian (1920s) established the rate code; timing codes later proved essential in audition and fast vision.",
  "Georgopoulos's population vector showed information spread across many noisy neurons.",
  "Information theory (Rieke et al., 1997) quantified bits per spike, but the brain's own readout remains unknown.",
  "The Signature proposal: the brain is multilingual — the code in each circuit is whatever its downstream readers can decode, with redundancy across rate, timing, and population.",
  "Matching measured codes to reader biophysics would confirm it; a single universal code would refute it."],
 "requirements": [
  "Abandon the search for one true neural code.",
  "Define each circuit's code by its readers' integration windows and convergence.",
  "Treat redundancy across rate, timing, and population as the design, not a puzzle.",
  "Require reader biophysics to predict the observed code.",
  "Demand a falsifiable mismatch experiment."],
 "standards": [
  "Single-unit and multi-unit recording analysis methods.",
  "Information-theoretic spike-train analysis.",
  "Population decoding and reader-modeling techniques."],
 "citations": [
  "Adrian ED. The Basis of Sensation. 1928.",
  "Rieke F, Warland D, de Ruyter van Steveninck R, Bialek W. Spikes: Exploring the Neural Code. MIT Press; 1997.",
  "Georgopoulos AP, et al. On the relations between the direction of two-dimensional arm movements and cell discharge in primate motor cortex. Journal of Neuroscience; 1982."],
},
{
 "key": "binding_problem",
 "name": "The Binding Problem",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": ("Your visual cortex processes color in one area, motion in "
             "another, and shape in a third — yet you see a single red "
             "ball rolling, not a floating redness, a separate roundness, "
             "and a detached motion. The binding problem asks how the "
             "brain's distributed feature detectors are recombined into "
             "unified objects and a single coherent experience. It is "
             "arguably the most basic question about perception, and it "
             "has no agreed answer."),
 "background": ("Anne Treisman's feature-integration theory (1980) made "
                "the problem famous: features are processed separately "
                "and bound by attention, with illusory conjunctions — "
                "misbound features — occurring when attention is "
                "overloaded. Christoph von der Malsburg proposed in 1981 "
                "that binding is achieved by temporal synchrony: neurons "
                "coding features of the same object fire in sync, "
                "tagging them as belonging together. Wolf Singer's group "
                "found such synchrony in cat visual cortex, launching a "
                "decade of excitement — until critics noted synchrony "
                "also occurs without binding and binding without "
                "synchrony. Alternative proposals include binding by "
                "convergence (all features project to a 'grandmother' "
                "object neuron), binding by attention-indexed pointers "
                "(FINSTs), and the radical suggestion that there is no "
                "binding problem because there is no unified experience "
                "— only the illusion of one. The field remains split "
                "between synchrony, convergence, and dissolution."),
 "why_it_matters": ("Binding is where the brain's distributed machinery "
                    "becomes the seamless world we inhabit. Solving it "
                    "would explain the unity of consciousness, guide the "
                    "design of artificial perception systems that must "
                    "also fuse features into objects, and clarify "
                    "disorders where binding breaks, from visual agnosias "
                    "to the fragmented perception reported in psychosis."),
 "sig_lens": ("Signature lens: binding is a labeling system — the "
              "Signature view treats the brain as tagging each feature "
              "with its object's identity, using whatever tag the "
              "circuit can read."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain processes features in parallel across "
  "specialized areas. (2) Downstream areas need to know which features "
  "belong together. (3) The brain uses multiple tagging schemes in "
  "different circuits, not one universal glue. "
  "REASONING PATH. The Signature approach proposes that 'binding' is "
  "three different operations wearing one name. Spatial binding — which "
  "features share a location — is solved by overlapping receptive "
  "fields and topographic maps: features processed at the same map "
  "position are bound by anatomy. Temporal binding — which features "
  "change together — uses synchrony as a tag, exactly as von der "
  "Malsburg proposed, but only in circuits with readers fast enough to "
  "detect it. Object binding — which features belong to the same "
  "thing across time — is solved by attention-indexed pointers that "
  "track objects through change. The synchrony debate dissolves: "
  "synchrony is real binding in fast circuits and irrelevant in slow "
  "ones, which is why the evidence looked contradictory. Illusory "
  "conjunctions happen when the spatial tag is degraded and the system "
  "falls back on weaker temporal tags. "
  "PROPOSED MECHANISM. Each visual area carries a spatial tag by "
  "topography; fast local circuits add a synchrony tag readable by "
  "coincidence-detecting downstream neurons; attentional pointers in "
  "parietal cortex maintain object identity across time. The conscious "
  "unity of the scene is the readout of all three tags agreeing. "
  "WHAT WOULD CONFIRM IT. If disrupting synchrony selectively broke "
  "temporal binding while sparing spatial binding — and disrupting "
  "topographic alignment broke spatial binding while sparing temporal — "
  "the three-operation proposal gains support. "
  "WHAT WOULD REFUTE IT. If a single manipulation broke all binding "
  "types identically, or if binding survived the removal of all three "
  "tagging schemes, the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the tags are the "
  "experience of unity, it does not claim all three are fully mapped, "
  "and it does not claim proof."),
 "key_points": [
  "Treisman (1980) showed features bind via attention; overload produces illusory conjunctions.",
  "Von der Malsburg (1981) proposed binding by temporal synchrony; evidence since has been mixed.",
  "Alternatives include convergence onto object neurons, attentional pointers, and dissolving the problem.",
  "The Signature proposal: binding is three operations — spatial (topography), temporal (synchrony), object (attentional pointers) — each used where its readers can read it.",
  "Selective double dissociation of the binding types would confirm it; a single universal glue would refute it."],
 "requirements": [
  "Split binding into spatial, temporal, and object operations.",
  "Assign each a tagging scheme matched to its readers.",
  "Explain the synchrony debate as circuit-dependent tag use.",
  "Require double dissociation of the binding types.",
  "Demand a falsifiable selective-disruption experiment."],
 "standards": [
  "Illusory-conjunction and feature-search paradigms.",
  "Multi-unit synchrony measurement methods.",
  "Attentional-tracking (FINST) task designs."],
 "citations": [
  "Treisman A, Gelade G. A feature-integration theory of attention. Cognitive Psychology; 1980.",
  "Von der Malsburg C. The correlation theory of brain function. 1981.",
  "Singer W, Gray CM. Visual feature integration and the temporal correlation hypothesis. Annual Review of Neuroscience; 1995."],
},
{
 "key": "physical_basis_of_memory",
 "name": "The Physical Basis of Memory",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": ("Where is a memory, physically? Not which brain region is "
             "involved — but what is the actual physical thing that a "
             "memory is. Is it a pattern of synaptic strengths, a set of "
             "molecules inside cells, a dynamic pattern of activity, or "
             "something else? The engram — the physical trace of a memory "
             "— was postulated a century ago and has been partially found, "
             "yet the complete physical account of what stores a lifetime "
             "of experience remains unsolved."),
 "background": ("Richard Semon coined 'engram' in 1904 for the hypothesized "
                "physical memory trace. Karl Lashley spent decades "
                "searching for it in rat cortex and concluded in 1950 "
                "that memory is distributed, not localized — the engram "
                "was nowhere and everywhere. The modern era began with "
                "long-term potentiation (Bliss and Lomo, 1973), a lasting "
                "strengthening of synapses, and the molecular cascade "
                "behind it (Kandel, CREB, protein synthesis). Susumu "
                "Tonegawa's group then did what Lashley could not: using "
                "optogenetics, they tagged the neurons active during "
                "fear learning and later reactivated them to trigger the "
                "memory — then created false memories by reactivating "
                "the tags in new contexts. The engram, as a set of "
                "neurons, was found. But the deeper question survived: "
                "the tagged neurons are the address, not the content. "
                "What physically encodes the content — the synaptic "
                "weights, the molecular states, the connectivity pattern "
                "— and how a lifetime of engrams coexist without "
                "interference is still unknown."),
 "why_it_matters": ("The physical basis of memory is the physical basis of "
                    "identity: we are, in large part, our stored past. "
                    "Understanding the storage medium would transform "
                    "treatment of memory disorders, settle how much of a "
                    "person could in principle be preserved or restored, "
                    "and reveal the brain's densest information-storage "
                    "technology — one that outperforms every human-built "
                    "system by orders of magnitude."),
 "sig_lens": ("Signature lens: a memory is a reconstructable pattern — "
              "the Signature view treats the engram as an address plus a "
              "recipe, stored across synapses, molecules, and connectivity."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) Memory content is stored in the pattern of synaptic "
  "strengths across the engram neurons, not in any single molecule. (2) "
  "Molecules (receptors, kinases, epigenetic marks) are the maintenance "
  "crew that keep the pattern stable, not the pattern itself. (3) "
  "Retrieval is pattern completion: a partial cue reactivates the full "
  "pattern through recurrent connectivity. "
  "REASONING PATH. The Signature approach resolves the address-versus-"
  "content puzzle with a layered account. The engram neurons Tonegawa "
  "tagged are the index — they say which memory, not what it contains. "
  "The content lives one level down, in the synaptic weight matrix "
  "among and around those neurons: the strengths encode the pattern, "
  "the way the weights of a trained network encode its function. "
  "Molecules are the third layer: they implement and protect the "
  "weights over time, like the error-correction on a disk. This "
  "explains why blocking protein synthesis erases recent memories (the "
  "weights were never written) but spares old ones (the weights are "
  "maintained by deeper mechanisms), and why memories survive "
  "considerable neural turnover — the pattern is redundantly encoded "
  "across many synapses, so losing some synapses degrades but does not "
  "destroy it. "
  "PROPOSED MECHANISM. A memory is a triple: an index (the engram cell "
  "ensemble), a weight pattern (the content, distributed across "
  "synapses), and a maintenance state (molecular locks holding the "
  "pattern). Recall is index-triggered pattern completion; forgetting "
  "is maintenance failure or index decay. "
  "WHAT WOULD CONFIRM IT. If the weight pattern among engram neurons "
  "could be read out and shown to predict the specific content of the "
  "memory — with content changing when the pattern is rewritten and "
  "the index left intact — the proposal gains support. "
  "WHAT WOULD REFUTE IT. If content proved fully determined by "
  "molecular states independent of synaptic weights, or if memories "
  "survived complete erasure of their weight patterns, the proposal "
  "fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the weight pattern of any "
  "real memory has been read, it does not claim to explain how "
  "patterns avoid interference at scale, and it does not claim proof."),
 "key_points": [
  "Semon (1904) postulated the engram; Lashley (1950) concluded memory is distributed.",
  "Bliss and Lomo (1973) discovered long-term potentiation; Kandel mapped its molecular cascade.",
  "Tonegawa's group tagged engram neurons optogenetically and created false memories by reactivating them.",
  "The Signature proposal: a memory is a triple — index (engram cells), content (synaptic weight pattern), maintenance (molecular locks).",
  "Reading content from the weight pattern with the index intact would confirm it; content without weights would refute it."],
 "requirements": [
  "Separate the engram index from the memory content.",
  "Store content in distributed synaptic weight patterns.",
  "Assign molecules the maintenance role, not the content role.",
  "Explain protein-synthesis blockade and neural turnover within the triple.",
  "Demand a falsifiable content-readout experiment."],
 "standards": [
  "Optogenetic engram tagging and reactivation protocols.",
  "Long-term potentiation induction and maintenance assays.",
  "Protein-synthesis-inhibition memory paradigms."],
 "citations": [
  "Semon R. Die Mneme. 1904.",
  "Bliss TVP, Lomo T. Long-lasting potentiation of synaptic transmission. Journal of Physiology; 1973.",
  "Josselyn SA, Tonegawa S. Memory engrams: recalling the past and imagining the future. Science; 2020."],
},
{
 "key": "rules_of_neuroplasticity",
 "name": "The Rules of Neuroplasticity",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": ("The brain rewires itself constantly — synapses strengthen "
             "and weaken, maps reorganize, new neurons are born in some "
             "regions. This neuroplasticity underlies all learning. Yet "
             "the rules are strangely elusive: the same stimulation can "
             "strengthen a synapse in one context and weaken it in "
             "another; plasticity is exuberant in childhood and gated in "
             "adulthood; and nobody knows the complete rulebook the brain "
             "uses to decide what changes, when, and in which direction."),
 "background": ("Donald Hebb's 1949 postulate — cells that fire together "
                "wire together — gave the field its first rule. Bliss and "
                "Lomo's LTP (1973) and the later discovery of LTD (long-"
                "term depression) gave it mechanisms. Then the rules "
                "multiplied: spike-timing-dependent plasticity (Markram, "
                "Bi and Poo, 1997-98) made the order of spikes decisive; "
                "the BCM rule (Bienenstock, Cooper, Munro, 1982) made the "
                "threshold slide with history; heterosynaptic and "
                "homeostatic plasticity showed synapses also change to "
                "keep the network stable. Critical periods — windows of "
                "heightened plasticity in development, studied by Wiesel "
                "and Hubel — showed the rules themselves change with age, "
                "gated by inhibition and molecular brakes like perineuronal "
                "nets. The field now has a catalog of plasticity "
                "phenomena but no unified rulebook: it cannot predict, "
                "for an arbitrary synapse in an arbitrary state, what a "
                "given pattern of activity will do."),
 "why_it_matters": ("Plasticity rules are the brain's learning algorithm. "
                    "Knowing them would let medicine reopen critical "
                    "periods after stroke, guide rehabilitation, treat "
                    "disorders of maladaptive plasticity like chronic "
                    "pain and addiction, and give artificial intelligence "
                    "the brain's actual learning rule instead of "
                    "backpropagation's shadow."),
 "sig_lens": ("Signature lens: plasticity is gated optimization — the "
              "Signature view treats every plasticity rule as the brain "
              "solving stability versus adaptability under an energy "
              "budget."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain optimizes a single objective: accurate "
  "prediction at sustainable energy cost. (2) Every plasticity "
  "phenomenon is this optimization running under different constraints. "
  "(3) The rules are gated: the brain adjusts its own learning rate by "
  "context. "
  "REASONING PATH. The Signature approach unifies the catalog. Hebbian "
  "LTP is the optimization taking a step that reduces prediction error; "
  "LTD is the same optimization pruning weights that increase error. "
  "Spike-timing dependence falls out of causality: pre-before-post "
  "means the presynaptic neuron predicted the postsynaptic one, so "
  "strengthen; the reverse means it mispredicted, so weaken. The "
  "sliding BCM threshold is the stability guard — it rises when the "
  "neuron is overactive, preventing runaway potentiation. Homeostatic "
  "plasticity is the energy budget enforcer. Critical periods are the "
  "gates opened wide: in development the brain accepts instability to "
  "learn fast, then molecular brakes (perineuronal nets, inhibition) "
  "close the gates to protect what was learned. Adult plasticity is "
  "not absent but gated — reopened locally by attention, surprise, and "
  "neuromodulators that signal 'this matters, learn now.' "
  "PROPOSED MECHANISM. A three-factor rule at every synapse: "
  "coincidence sets the candidate change, the local prediction error "
  "sets its sign, and a global gate (neuromodulators, inhibition "
  "state, developmental brakes) sets whether change is allowed at all. "
  "All documented plasticity phenomena are parameter settings of this "
  "one rule. "
  "WHAT WOULD CONFIRM IT. If an arbitrary synapse's response to a "
  "stimulation pattern could be predicted from the three factors — "
  "with the gate state measured, not assumed — across LTP, LTD, STDP, "
  "and homeostatic protocols, the proposal gains support. "
  "WHAT WOULD REFUTE IT. If a major plasticity phenomenon proved "
  "irreducible to the three factors — changing with no change in "
  "coincidence, error, or gate — the unified proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the gate signals are "
  "fully mapped, it does not claim to reopen critical periods safely, "
  "and it does not claim proof."),
 "key_points": [
  "Hebb (1949) proposed fire-together-wire-together; LTP (1973) and LTD gave mechanisms.",
  "STDP made spike order decisive; the BCM rule made the threshold slide with history.",
  "Critical periods show the rules themselves change with age, gated by inhibition and molecular brakes.",
  "The Signature proposal: one three-factor rule — coincidence sets the candidate, local error sets the sign, a global gate sets permission — with every phenomenon as a parameter setting.",
  "Predicting arbitrary synaptic responses from the three measured factors would confirm it; an irreducible phenomenon would refute it."],
 "requirements": [
  "Unify LTP, LTD, STDP, BCM, and homeostatic plasticity under one objective.",
  "Derive timing dependence from causality in prediction.",
  "Treat critical periods as scheduled gate openings, not separate rules.",
  "Require the three factors to predict responses across protocols.",
  "Demand a falsifiable irreducible-phenomenon test."],
 "standards": [
  "STDP induction protocols in slice physiology.",
  "Critical-period plasticity assays (ocular dominance).",
  "Neuromodulator-gated plasticity paradigms."],
 "citations": [
  "Hebb DO. The Organization of Behavior. 1949.",
  "Bienenstock EL, Cooper LN, Munro PW. Theory for the development of neuron selectivity. Journal of Neuroscience; 1982.",
  "Markram H, et al. Regulation of synaptic efficacy by coincidence of postsynaptic APs and EPSPs. Science; 1997."],
},
{
 "key": "neural_basis_of_decision",
 "name": "How the Brain Decides",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": ("Every day you make thousands of decisions — what to eat, "
             "which route to take, whether to trust a stranger — and most "
             "feel instantaneous and obvious. Beneath that ease, the brain "
             "must convert noisy, incomplete evidence into a single "
             "committed action, trading speed against accuracy. How neural "
             "circuits actually implement this conversion, where the "
             "decision happens, and how value, habit, and deliberation "
             "combine remain unsolved."),
 "background": ("The drift-diffusion model, developed by Ratcliff in the "
                "1970s, describes decisions as noisy evidence accumulating "
                "to a bound — and it fits reaction times and accuracy "
                "across species and tasks with uncanny precision. Shadlen "
                "and Newsome found neurons in monkey parietal cortex whose "
                "firing ramps exactly like the model's accumulator during "
                "motion-discrimination decisions. Value-based decisions "
                "added the orbitofrontal cortex and striatum, where "
                "Padoa-Schioppa and others found neurons encoding the "
                "value of options. Kahneman and Tversky's prospect theory "
                "showed human choice systematically violates rationality, "
                "and the field split decisions into fast habitual systems "
                "and slow deliberative ones. But the beautiful accumulator "
                "story covers only simple perceptual choices; for real "
                "decisions — multi-attribute, value-laden, made over days "
                "— the field has models but no agreed neural mechanism, "
                "and how the brain sets the bound (its speed-accuracy "
                "tradeoff) adaptively is still mysterious."),
 "why_it_matters": ("Decision-making is the final common path of the "
                    "brain: perception, memory, emotion, and value all "
                    "converge on choice. Understanding it would improve "
                    "treatments for addiction, impulsivity, and "
                    "compulsive disorders, sharpen economic and policy "
                    "models, and show artificial agents how to decide "
                    "under uncertainty the way brains do."),
 "sig_lens": ("Signature lens: deciding is betting under uncertainty — "
              "the Signature view treats every choice as the brain "
              "placing a bet with evidence as its stake and time as its "
              "cost."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) All decisions are evidence accumulation to a bound, "
  "from the simplest perceptual choice to the most deliberative. (2) "
  "The bound is set adaptively by the cost of time and the cost of "
  "error. (3) Value, habit, and deliberation are three evidence streams "
  "feeding one accumulator. "
  "REASONING PATH. The Signature approach extends the drift-diffusion "
  "account to all decisions. Perceptual decisions accumulate sensory "
  "evidence; value decisions accumulate value signals from "
  "orbitofrontal and striatal circuits; deliberative decisions "
  "accumulate internally generated evidence — retrieved memories, "
  "simulated outcomes — over longer timescales. The 'two systems' of "
  "fast and slow choice are not two mechanisms but two parameter "
  "regimes of one accumulator: habits are accumulators with "
  "pre-loaded evidence and low bounds (fast, cheap, inflexible), "
  "deliberation is the same circuit with the bound raised and the "
  "evidence stream switched to internal simulation. Prospect-theory "
  "biases — loss aversion, framing — are not bugs but features of the "
  "value stream, which encodes fitness-relevant asymmetries. The bound "
  "is set by a meta-controller tracking the opportunity cost of time: "
  "urgency lowers the bound, importance raises it. "
  "PROPOSED MECHANISM. Cortical-basal ganglia loops implement the "
  "accumulator; dopamine and norepinephrine set the bound by signaling "
  "urgency and value; the three evidence streams (sensory, value, "
  "simulated) converge on shared integrator circuits. Choice is the "
  "first bound crossed. "
  "WHAT WOULD CONFIRM IT. If the bound could be read out neurally and "
  "shown to track opportunity cost trial by trial — with habits, "
  "deliberation, and perceptual choices all fitting one accumulator "
  "with different parameters — the proposal gains support. "
  "WHAT WOULD REFUTE IT. If a major decision type proved to use no "
  "accumulation-to-bound dynamics at all, or if the bound showed no "
  "adaptive tracking of time and error costs, the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim all biases are adaptive, "
  "it does not claim the meta-controller is identified, and it does "
  "not claim proof."),
 "key_points": [
  "Ratcliff's drift-diffusion model fits decision speed and accuracy across species and tasks.",
  "Shadlen and Newsome found parietal neurons ramping like the model's accumulator.",
  "Value decisions engage orbitofrontal and striatal circuits; prospect theory documents systematic deviations from rationality.",
  "The Signature proposal: one accumulator for all decisions — habits are low-bound pre-loaded regimes, deliberation is high-bound internal simulation, and a meta-controller sets the bound from time and error costs.",
  "Neural readout of the bound tracking opportunity cost would confirm it; a decision type with no accumulation dynamics would refute it."],
 "requirements": [
  "Extend accumulation-to-bound from perception to value and deliberative choice.",
  "Treat fast and slow systems as parameter regimes of one mechanism.",
  "Explain prospect-theory biases as features of the value stream.",
  "Require the bound to track opportunity cost adaptively.",
  "Demand a falsifiable no-accumulation test."],
 "standards": [
  "Random-dot motion discrimination paradigms.",
  "Value-based choice and intertemporal-choice tasks.",
  "Single-unit accumulator recording protocols."],
 "citations": [
  "Ratcliff R. A theory of memory retrieval. Psychological Review; 1978.",
  "Shadlen MN, Newsome WT. Neural basis of a perceptual decision in the parietal cortex. Journal of Neuroscience; 2001.",
  "Kahneman D, Tversky A. Prospect theory. Econometrica; 1979."],
},
{
 "key": "neural_basis_of_emotion",
 "name": "The Neural Basis of Emotion",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": ("Fear, joy, anger, grief — emotions are the most vivid part "
             "of mental life, yet neuroscience cannot say what an emotion "
             "is. Are emotions built-in circuits, one per feeling, or are "
             "they constructed by the brain from simpler ingredients? The "
             "question has split the field for decades, and the answer "
             "determines how we understand mood, treat emotional "
             "disorders, and build machines that interact with feeling "
             "humans."),
 "background": ("The classic view descends from Darwin (1872) and was "
                "formalized by Paul Ekman: a small set of basic emotions "
                "— fear, anger, disgust, sadness, joy, surprise — each "
                "with a dedicated circuit (fear in the amygdala, per "
                "LeDoux) and a universal facial expression. Jaak "
                "Panksepp proposed seven primary emotional systems wired "
                "into the mammalian brain. The constructionist challenge, "
                "led by Lisa Feldman Barrett, argues the opposite: the "
                "brain has only core affect (valence and arousal) plus "
                "concepts, and emotions are constructed predictions — "
                "the brain categorizing its own bodily state using "
                "emotion concepts learned from culture. Meta-analyses "
                "show the amygdala responds to salience and novelty, not "
                "fear specifically, undermining the one-circuit-per-"
                "emotion map. Both camps have mountains of evidence; "
                "neither has produced the experiment that settles it."),
 "why_it_matters": ("Emotion drives decision, memory, health, and social "
                    "life; emotional disorders are among the leading "
                    "causes of disability worldwide. Whether emotions are "
                    "circuits or constructions changes treatment — tune "
                    "the circuit, or retrain the concepts — and it "
                    "changes what it would mean to build an artificial "
                    "system that truly feels."),
 "sig_lens": ("Signature lens: emotions are the brain's action "
              "preparation — the Signature view treats feelings as the "
              "conscious readout of the body being readied for what "
              "comes next."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain must prepare the body for action before "
  "knowing exactly what is happening — speed demands it. (2) Emotions "
  "are the control states that configure the body and the brain for "
  "classes of situations. (3) The conscious feeling is the readout of "
  "the control state, categorized by learned concepts. "
  "REASONING PATH. The Signature approach synthesizes the two camps. "
  "Panksepp is right that evolution built a small set of ancient "
  "control circuits — fight, flight, freeze, seek, care, play, grieve "
  "— because these situations recurred for hundreds of millions of "
  "years. Barrett is right that the felt emotion is constructed: the "
  "control state is subcortical and fast, while the conscious "
  "experience is the cortex categorizing the bodily changes with "
  "emotion concepts. Fear the circuit (amygdala-driven defense "
  "mobilization) is universal; fear the feeling (the categorized "
  "experience) varies by culture and learning. This explains why "
  "amygdala damage impairs defense responses but not all fear "
  "experience, and why emotion words shape what people feel. The "
  "circuits are the instruments; the concepts are the music played on "
  "them. "
  "PROPOSED MECHANISM. Subcortical control circuits set bodily "
  "parameters (autonomic tone, muscle readiness, attention bias) for "
  "situation classes; interoceptive cortex reads the resulting bodily "
  "state; conceptual circuits categorize the state as an emotion. "
  "Disorders can arise at any level — misfiring circuits, misread "
  "bodies, or miscategorizing concepts. "
  "WHAT WOULD CONFIRM IT. If the control state could be dissociated "
  "from the categorized feeling — same bodily mobilization, different "
  "reported emotion under different concept primes, with the "
  "mobilization predicting action but the categorization predicting "
  "experience — the synthesis gains support. "
  "WHAT WOULD REFUTE IT. If felt emotions proved fully determined by "
  "subcortical circuits with no conceptual contribution, or fully "
  "constructed with no dedicated control circuitry, the synthesis "
  "fails. "
  "WHAT IT DOES NOT CLAIM. It does not diagnose or treat any person's "
  "emotional condition, it does not claim the circuit list is final, "
  "and it does not claim proof — it is a descriptive frame only."),
 "key_points": [
  "Ekman's basic-emotion view proposes dedicated circuits and universal expressions; LeDoux mapped fear to the amygdala.",
  "Panksepp proposed seven primary emotional systems in the mammalian brain.",
  "Barrett's constructionism argues emotions are categorized core affect, built with learned concepts.",
  "The Signature proposal: ancient control circuits prepare the body for situation classes; the felt emotion is the cortex categorizing that preparation — instruments and music.",
  "Dissociating mobilization (predicting action) from categorization (predicting experience) would confirm it; either extreme alone would refute it."],
 "requirements": [
  "Grant evolution a small set of ancient control circuits.",
  "Grant the cortex a categorizing role in felt experience.",
  "Explain amygdala findings as defense mobilization, not fear itself.",
  "Require dissociation of control state from categorized feeling.",
  "Keep the account descriptive; no diagnosis or treatment of any person."],
 "standards": [
  "Affective neuroscience lesion and stimulation paradigms.",
  "Emotion-categorization and concept-priming experiments.",
  "Interoceptive accuracy measurement methods."],
 "citations": [
  "Panksepp J. Affective Neuroscience. Oxford University Press; 1998.",
  "Barrett LF. How Emotions Are Made. Houghton Mifflin Harcourt; 2017.",
  "LeDoux JE. The Emotional Brain. Simon and Schuster; 1996."],
},
{
 "key": "language_comprehension",
 "name": "The Neural Basis of Language Comprehension",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": ("A string of sounds hits your ears and, in a fraction of a "
             "second, becomes meaning — you understand sentences you have "
             "never heard before, instantly. Language comprehension is the "
             "most complex computation the brain performs routinely, "
             "combining sound, grammar, meaning, and context at speed. "
             "How neural circuits transform acoustic waves into understood "
             "thought, and where meaning itself lives in the brain, "
             "remains unsolved."),
 "background": ("The classic map began with Broca (1861) and Wernicke "
                "(1874), localizing production and comprehension to left "
                "frontal and temporal areas. The Wernicke-Lichtheim model "
                "ruled for a century until imaging complicated it: "
                "language activates a broad left-lateralized network, and "
                "meaning seems distributed across the cortex. Noam "
                "Chomsky's universal grammar proposed innate syntactic "
                "machinery; connectionists countered that statistics "
                "suffice. Event-related potentials revealed the N400 "
                "(Kutas and Hillyard, 1980), a brain wave tracking "
                "meaning violations, and the P600 tracking syntactic "
                "ones. Modern work shows the brain predicts upcoming "
                "words constantly, integrates context within hundreds of "
                "milliseconds, and represents word meaning in distributed "
                "patterns spanning sensory and motor areas. Yet no model "
                "explains the central miracle: infinite meaningful "
                "sentences from finite means, computed in real time by "
                "wet tissue."),
 "why_it_matters": ("Language is the medium of human thought and culture. "
                    "Understanding its neural basis would transform "
                    "treatment of aphasia and language disorders, guide "
                    "education, and answer whether machines that process "
                    "language the statistical way are missing the brain's "
                    "core trick. It is the highest cognitive function we "
                    "can study in the lab."),
 "sig_lens": ("Signature lens: comprehension is prediction all the way "
              "down — the Signature view treats understanding as the "
              "brain predicting the speaker's meaning before the "
              "sentence ends."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain processes language predictively at every "
  "level: sound, word, grammar, meaning. (2) Meaning is not stored in a "
  "dictionary area but in the pattern of connections between word forms "
  "and the sensory, motor, and emotional systems they refer to. (3) "
  "Comprehension is the convergence of these predictions on a single "
  "coherent interpretation. "
  "REASONING PATH. The Signature approach proposes that understanding a "
  "sentence is hierarchical prediction converging. As each word arrives, "
  "the brain predicts the next sound (auditory cortex), the next word "
  "(lexical networks), the syntactic structure (frontal-temporal "
  "circuits), and the unfolding meaning (distributed semantic systems) "
  "— simultaneously. The N400 is the semantic prediction error; the "
  "P600 is the syntactic prediction error. Meaning 'lives' nowhere "
  "single because it is the convergence state itself: a word's meaning "
  "is the full set of predictions it licenses across all systems. "
  "Novel sentences are understood because prediction is compositional — "
  "the brain predicts the meaning of the whole from the predicted "
  "meanings of the parts, exactly as fast as the words arrive. "
  "Broca's and Wernicke's areas are hubs in this predictive hierarchy, "
  "not containers of grammar or words. "
  "PROPOSED MECHANISM. A left-lateralized predictive hierarchy: each "
  "level predicts the input to the level below and receives prediction "
  "errors back; meaning emerges as the top-level state that best "
  "explains the whole sentence. Context tunes the predictions, which "
  "is why the same sentence means different things in different "
  "conversations. "
  "WHAT WOULD CONFIRM IT. If trial-by-trial prediction errors at each "
  "level (sound, word, syntax, meaning) independently predicted the "
  "N400, P600, and comprehension speed — with comprehension failing "
  "exactly when the errors cannot be resolved — the proposal gains "
  "support. "
  "WHAT WOULD REFUTE IT. If comprehension proved non-predictive — "
  "meaning computed only after the sentence ends, with no anticipatory "
  "activity — or if meaning localized to a single dictionary area, the "
  "proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the innate-versus-learned "
  "debate is settled, it does not claim a complete circuit map, and it "
  "does not claim proof."),
 "key_points": [
  "Broca (1861) and Wernicke (1874) founded the classic localization map; imaging later showed a broad left-lateralized network.",
  "The N400 (Kutas and Hillyard, 1980) tracks meaning violations; the P600 tracks syntactic ones.",
  "The brain predicts upcoming words constantly; meaning appears distributed across sensory and motor systems.",
  "The Signature proposal: comprehension is hierarchical prediction converging — a word's meaning is the full set of predictions it licenses, and understanding is the convergence state.",
  "Level-by-level prediction errors predicting comprehension measures would confirm it; non-predictive comprehension would refute it."],
 "requirements": [
  "Process language predictively at sound, word, grammar, and meaning levels.",
  "Distribute meaning across connected sensory, motor, and emotional systems.",
  "Identify the N400 and P600 as semantic and syntactic prediction errors.",
  "Explain novel-sentence understanding through compositional prediction.",
  "Demand a falsifiable level-by-level error prediction."],
 "standards": [
  "ERP language paradigms (N400/P600).",
  "Predictive-processing sentence experiments.",
  "Lesion-symptom mapping in aphasia."],
 "citations": [
  "Kutas M, Hillyard SA. Reading senseless sentences. Science; 1980.",
  "Friederici AD. The brain basis of language processing. Physiological Reviews; 2011.",
  "Hagoort P. MUC (memory, unification, control). Trends in Cognitive Sciences; 2013."],
},
{
 "key": "neural_basis_of_creativity",
 "name": "The Neural Basis of Creativity",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": ("Beethoven composed deaf; Einstein imagined riding a light "
             "beam; a child invents a game no one taught. Creativity — "
             "the generation of novel, valuable ideas — is the most "
             "celebrated human capacity and the least understood. What "
             "neural events distinguish a creative thought from an "
             "ordinary one, and can the creative process be described "
             "mechanistically at all?"),
 "background": ("Early work treated creativity as divergent thinking, "
                "measurable by tests like the Torrance Tests and the "
                "Alternative Uses Task. Imaging studies converged on a "
                "surprising pattern: creative thought engages the default "
                "mode network (imagination, memory, simulation) together "
                "with the executive control network (evaluation, focus) — "
                "two systems usually opposed. Rex Jung, Oshin Vartanian, "
                "and others mapped this coupling; the 'blind variation "
                "and selective retention' model of Campbell and Simonton "
                "framed creativity as Darwinian search among ideas. The "
                "neurochemistry implicates dopamine (novelty seeking) and "
                "reduced latent inhibition (more raw material reaching "
                "awareness). But correlation is not mechanism: the field "
                "can say which networks are active during creative tasks "
                "without being able to say what computation makes an "
                "idea creative, why insights arrive suddenly, or why "
                "creative ability varies so wildly between people and "
                "within a person across a lifetime."),
 "why_it_matters": ("Creativity drives science, art, technology, and "
                    "culture — it is the engine of everything new. A "
                    "mechanistic account would change education (teaching "
                    "creativity, not just knowledge), help creative "
                    "blocks and decline, and tell us whether artificial "
                    "systems can genuinely create or only remix."),
 "sig_lens": ("Signature lens: creativity is controlled surprise — the "
              "Signature view treats the creative brain as a generator "
              "running hot and a critic running sharp, in alternation."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) Idea generation and idea evaluation are separable "
  "processes using different networks. (2) Creativity requires both: "
  "generation without evaluation is noise, evaluation without "
  "generation is sterility. (3) The creative act is the timed "
  "alternation between them. "
  "REASONING PATH. The Signature approach proposes that creativity is "
  "an annealing process. In the generation phase, the default mode "
  "network runs hot — association thresholds drop, distant memories "
  "and concepts activate together, and the brain samples unusual "
  "combinations (the 'blind variation'). In the evaluation phase, "
  "executive networks cool the system — testing combinations against "
  "goals, constraints, and taste (the 'selective retention'). Insight "
  "'aha' moments are phase transitions: the cooled system suddenly "
  "recognizing a high-value combination the hot system produced. This "
  "explains why creativity needs both networks coupled, why incubation "
  "(stepping away) helps — it extends the hot phase — and why "
  "creativity varies: people differ in their hot-phase temperature "
  "(dopamine, latent inhibition) and their cool-phase judgment "
  "(expertise, taste). Madness and genius share the hot phase; they "
  "differ in the cool one. "
  "PROPOSED MECHANISM. Neuromodulators set the annealing schedule: "
  "dopamine raises generation temperature, norepinephrine sharpens "
  "evaluation; the cycle between default-mode and executive dominance "
  "is the algorithm. Training creativity means training the schedule "
  "— longer hot phases for novelty, stricter cool phases for value. "
  "WHAT WOULD CONFIRM IT. If the hot-cool cycle could be tracked in "
  "real time and shown to predict creative output — with output "
  "quality depending on the match between phase timing and task "
  "demands — the annealing proposal gains support. "
  "WHAT WOULD REFUTE IT. If creative output proved independent of "
  "any generation-evaluation alternation, or if the coupled networks "
  "showed no phase structure during creative work, the proposal "
  "fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim creativity can be "
  "manufactured on demand, it does not reduce art to temperature "
  "settings, and it does not claim proof."),
 "key_points": [
  "Creative thought couples the default mode network with the executive control network — systems usually opposed.",
  "Campbell and Simonton framed creativity as blind variation and selective retention.",
  "Dopamine and reduced latent inhibition supply raw material; expertise supplies judgment.",
  "The Signature proposal: creativity is annealing — a hot generation phase alternating with a cool evaluation phase, with insight as the phase transition.",
  "Real-time phase tracking predicting creative output would confirm it; phaseless coupled activity would refute it."],
 "requirements": [
  "Separate idea generation from idea evaluation as distinct processes.",
  "Treat their alternation as the creative algorithm.",
  "Explain insight as a phase transition in the annealing schedule.",
  "Require phase timing to predict creative output quality.",
  "Demand a falsifiable real-time tracking experiment."],
 "standards": [
  "Alternative Uses and Torrance creativity task protocols.",
  "Default-mode/executive coupling fMRI analysis.",
  "Insight (aha) moment experimental paradigms."],
 "citations": [
  "Jung RE, et al. The structure of creative cognition in the human brain. Frontiers in Human Neuroscience; 2013.",
  "Simonton DK. Creativity and discovery as blind variation. Psychological Bulletin; 2011.",
  "Beaty RE, et al. Robust prediction of individual creative ability from brain functional connectivity. PNAS; 2018."],
},
{
 "key": "lifelong_learning_no_forgetting",
 "name": "How the Brain Learns for a Lifetime Without Catastrophic Forgetting",
 "group": "Compounded", "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": ("An artificial neural network trained on a new task tends to "
             "destroy what it learned before — catastrophic forgetting. "
             "The human brain learns thousands of skills across a lifetime "
             "without this collapse: you can learn Spanish at forty "
             "without forgetting how to ride a bike. How the brain adds "
             "new knowledge indefinitely while preserving the old — the "
             "stability-plasticity dilemma in its fullest form — remains "
             "unsolved."),
 "background": ("McCloskey and Cohen demonstrated catastrophic forgetting "
                "in artificial networks in 1989, and the problem has "
                "haunted machine learning since. The brain's solution was "
                "partly sketched by the complementary learning systems "
                "theory (McClelland, McNaughton, O'Reilly, 1995): the "
                "hippocampus learns fast and the cortex learns slow, with "
                "interleaved replay protecting old knowledge. But that "
                "account covers episodic memory, not the full lifetime "
                "of skills, languages, and expertise. Proposed mechanisms "
                "include synaptic consolidation (important synapses are "
                "molecularly protected — the basis of AI's elastic weight "
                "consolidation, Kirkpatrick et al., 2017), sparse coding "
                "(new learning uses fresh neurons, minimizing overlap), "
                "neurogenesis (new neurons for new memories), and "
                "modular organization (different tasks use different "
                "circuits). Each helps; the complete account of how they "
                "combine to give a lifetime of stable, cumulative "
                "learning does not exist."),
 "why_it_matters": ("Lifelong learning is the difference between a tool "
                    "and a mind. Understanding the brain's solution would "
                    "give artificial intelligence true continual learning, "
                    "transform education across the lifespan, and explain "
                    "how expertise accumulates — and why it sometimes "
                    "doesn't, as in age-related decline."),
 "sig_lens": ("Signature lens: the brain writes in pencil and ink — the "
              "Signature view treats important synapses as progressively "
              "locked, so new learning flows around the old."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) Not all synapses are equal: some carry critical "
  "knowledge, others are free. (2) The brain tracks synapse importance "
  "and protects important ones. (3) New learning is routed preferentially "
  "through unprotected synapses and fresh neurons. "
  "REASONING PATH. The Signature approach proposes a protection-and-"
  "routing system. When a skill is mastered, its critical synapses are "
  "tagged — molecularly locked via the same cascades that maintain "
  "long-term memory — raising their resistance to change. New learning "
  "then flows around the locked synapses, using the remaining plastic "
  "capacity plus newly generated neurons. This is why experts can add "
  "skills without losing old ones: the old skills are literally "
  "hardened. Interference happens when two tasks need the same "
  "unprotected synapses — the classic explanation for why similar "
  "tasks interfere most. Sleep replay serves as the auditor: it "
  "reactivates old skills, re-measures which synapses matter, and "
  "refreshes their locks. Aging degrades the system not by losing "
  "plasticity but by losing lock maintenance — old knowledge slowly "
  "unlocks and gets overwritten. "
  "PROPOSED MECHANISM. Importance-weighted protection: each synapse "
  "carries a protection level set by its contribution to mastered "
  "skills; plasticity is gated by (1 - protection); neurogenesis "
  "supplies fresh unprotected capacity; replay maintains the locks. "
  "Catastrophic forgetting is what happens with protection set to "
  "zero — the artificial-network condition. "
  "WHAT WOULD CONFIRM IT. If synapse protection levels could be "
  "measured and shown to predict which synapses change during new "
  "learning — with protection blockade causing catastrophic-like "
  "forgetting in animals — the proposal gains support. "
  "WHAT WOULD REFUTE IT. If new learning were found to change "
  "synapses independently of any importance measure, or if "
  "protection blockade left old skills fully intact, the proposal "
  "fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the importance signal is "
  "fully identified, it does not claim aging is only lock failure, "
  "and it does not claim proof."),
 "key_points": [
  "McCloskey and Cohen (1989) demonstrated catastrophic forgetting in artificial networks.",
  "Complementary learning systems (1995) proposed fast hippocampal and slow cortical learners with replay.",
  "Candidate protections: synaptic tagging, sparse coding, neurogenesis, modular organization.",
  "The Signature proposal: importance-weighted synaptic protection — mastered skills lock their synapses, new learning routes around them, replay maintains the locks.",
  "Measured protection predicting synaptic change would confirm it; importance-independent change would refute it."],
 "requirements": [
  "Track per-synapse importance for mastered skills.",
  "Gate plasticity by (1 - protection).",
  "Route new learning through unprotected synapses and fresh neurons.",
  "Use replay as the lock-maintenance auditor.",
  "Demand a falsifiable protection-blockade experiment."],
 "standards": [
  "Continual-learning benchmark paradigms.",
  "Synaptic tagging and capture protocols.",
  "Adult neurogenesis manipulation assays."],
 "citations": [
  "McCloskey M, Cohen NJ. Catastrophic interference in connectionist networks. Psychology of Learning and Motivation; 1989.",
  "Kirkpatrick J, et al. Overcoming catastrophic forgetting in neural networks. PNAS; 2017.",
  "McClelland JL, McNaughton BL, O'Reilly RC. Why there are complementary learning systems. Psychological Review; 1995."],
},
{
 "key": "anesthesia_consciousness_switch",
 "name": "How General Anesthesia Switches Consciousness Off and On",
 "group": "Compounded", "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": ("Every day, millions of people have their consciousness "
             "switched off by general anesthetics and switched back on "
             "again — safely, reversibly, routinely. It is the most "
             "dramatic manipulation of consciousness in medicine, and "
             "after 170 years nobody fully understands how it works. "
             "Anesthetics act on molecules we can name, but how those "
             "molecular actions extinguish subjective experience — and "
             "why the switch is so clean — remains unsolved."),
 "background": ("Ether anesthesia was demonstrated in 1846; the Meyer-"
                "Overton rule soon linked anesthetic potency to lipid "
                "solubility, suggesting a membrane target. Modern work "
                "identified protein targets: most anesthetics enhance "
                "GABA-A inhibition and block NMDA excitation, among "
                "other actions. But the molecular story never reached "
                "the experience: why does boosting inhibition abolish "
                "consciousness rather than just sedate? Theories "
                "proliferated: Mashour's 'cognitive unbinding' (anesthetics "
                "disrupt frontoparietal feedback), Alkire's thalamic "
                "switch (the thalamus gates consciousness), and the "
                "integrated-information account (anesthetics collapse the "
                "brain's capacity to integrate information, measurable as "
                "the perturbational complexity index, which drops in "
                "sleep, anesthesia, and disorders of consciousness "
                "alike). Each explains part; none derives the clean "
                "on-off switch from the molecules."),
 "why_it_matters": ("Understanding the switch would make anesthesia safer "
                    "(preventing the rare but devastating awareness under "
                    "anesthesia), provide the cleanest test of every "
                    "theory of consciousness, and potentially reveal a "
                    "general principle: what physical property must be "
                    "present for experience to exist. It is consciousness "
                    "research with a control knob."),
 "sig_lens": ("Signature lens: anesthesia breaks the loop — the Signature "
              "view treats consciousness as requiring recurrent feedback, "
              "and anesthetics as cutting the feedback while leaving the "
              "feedforward intact."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) Consciousness requires recurrent processing: "
  "feedforward sweeps alone are unconscious. (2) Anesthetics "
  "preferentially disrupt feedback connectivity over feedforward. (3) "
  "The molecular actions (GABA enhancement, NMDA blockade) implement "
  "this disruption. "
  "REASONING PATH. The Signature approach proposes that the clean "
  "switch is a network phase transition. The conscious brain is a "
  "recurrent network balanced near criticality, with feedback "
  "connections sustaining integrated states. Anesthetics tilt the "
  "balance: enhanced inhibition and reduced excitation preferentially "
  "silence the long-range feedback projections (which are more "
  "vulnerable, being longer and more NMDA-dependent) while sparing "
  "local feedforward processing. Below a critical feedback density, "
  "the network cannot sustain integrated states — consciousness "
  "winks out all at once, like a percolation threshold. This "
  "explains the binary character of the switch, why primary sensory "
  "responses persist under anesthesia (feedforward survives), why "
  "dreams can occur in light anesthesia (partial feedback), and why "
  "the perturbational complexity index tracks the state: it measures "
  "exactly the feedback-driven integration. Emergence is the "
  "threshold crossed in reverse. "
  "PROPOSED MECHANISM. Molecular actions reduce feedback gain; when "
  "recurrent gain falls below the critical value, integrated states "
  "collapse — a phase transition, not a dimmer. Different "
  "anesthetics reach the threshold by different molecular routes, "
  "which is why their profiles differ while the endpoint is the "
  "same. "
  "WHAT WOULD CONFIRM IT. If feedback connectivity could be measured "
  "in real time and shown to cross a sharp threshold exactly at loss "
  "and return of consciousness — across different anesthetic agents "
  "— the phase-transition proposal gains support. "
  "WHAT WOULD REFUTE IT. If consciousness were lost with feedback "
  "fully intact, or if the transition proved gradual with no "
  "threshold across careful measurement, the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the critical value is "
  "known, it does not offer medical guidance on anesthesia, and it "
  "does not claim proof — it is a descriptive frame only."),
 "key_points": [
  "Ether anesthesia dates to 1846; the Meyer-Overton rule linked potency to lipid solubility.",
  "Modern targets: GABA-A enhancement and NMDA blockade, among others.",
  "Leading accounts: cognitive unbinding, the thalamic switch, and integrated-information collapse.",
  "The Signature proposal: the switch is a phase transition — anesthetics cut long-range feedback below a critical density, collapsing integrated states all at once while feedforward survives.",
  "A sharp feedback threshold crossed at loss and return of consciousness, across agents, would confirm it; loss with intact feedback would refute it."],
 "requirements": [
  "Require recurrent feedback for consciousness; feedforward alone is unconscious.",
  "Show anesthetics preferentially disrupting feedback over feedforward.",
  "Treat the switch as a percolation-like phase transition.",
  "Explain the binary character and the persistence of sensory responses.",
  "Keep the account descriptive; no medical guidance."],
 "standards": [
  "Perturbational complexity index (PCI) measurement.",
  "Loss/return of consciousness timing paradigms.",
  "Thalamocortical connectivity imaging under anesthesia."],
 "citations": [
  "Mashour GA. Cognitive unbinding in anesthesia and autism. Frontiers in Neuroscience; 2013.",
  "Alkire MT, Hudetz AG, Tononi G. Consciousness and anesthesia. Science; 2008.",
  "Casali AG, et al. Stratification of unresponsive patients by an independent perturbational measure. Science Translational Medicine; 2013."],
},
{
 "key": "volition_libet",
 "name": "The Neural Correlates of Volition",
 "group": "Compounded", "ladder_rank": 24, "ladder_tier": "compounded",
 "problem": ("In the 1980s Benjamin Libet found that the brain's "
             "'readiness potential' begins about half a second before "
             "people report deciding to move — suggesting the brain "
             "decides before 'you' do. The result ignited a decades-long "
             "war over free will. But the deeper neuroscience question "
             "remains unsolved: what neural events constitute a voluntary "
             "decision, how do intentions form in the brain, and what — "
             "if anything — does conscious will add to the process?"),
 "background": ("Libet's 1983 experiments asked subjects to flick a "
                "wrist whenever they felt like it and note when they "
                "decided; the readiness potential (a slow buildup found "
                "by Kornhuber and Deecke in 1965) preceded the reported "
                "decision by ~500 milliseconds. Soon et al. (2008) pushed "
                "further, decoding choices from brain activity up to "
                "seconds before awareness. Critics countered: the "
                "readiness potential may reflect general preparation, not "
                "the decision; Schurger's 2012 model showed it can emerge "
                "from random neural noise crossing a threshold; and "
                "reporting decision times is notoriously unreliable. "
                "Meanwhile, stimulation studies (Desmurget) can trigger "
                "the feeling of intending to move, and the sense of "
                "agency can be manipulated independently of action. The "
                "field now distinguishes the intention, the decision, the "
                "action, and the feeling of willing — four things that "
                "can come apart — without agreeing on how they normally "
                "combine."),
 "why_it_matters": ("Volition is the foundation of moral responsibility, "
                    "law, and our self-conception as agents. A neural "
                    "account of intention would clarify what conscious "
                    "will does — commander, vetoer, or narrator — and "
                    "would reshape debates about addiction, compulsion, "
                    "and criminal responsibility. It is the point where "
                    "neuroscience meets the deepest human questions."),
 "sig_lens": ("Signature lens: will is the veto, not the spark — the "
              "Signature view treats conscious intention as the brain's "
              "late-arriving approval stamp on processes already in "
              "motion."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) Action preparation begins unconsciously; this is "
  "settled by the evidence. (2) Conscious intention is a real neural "
  "event with causal powers, not an epiphenomenal glow. (3) Its power "
  "is veto and selection among prepared options, not initiation from "
  "nothing. "
  "REASONING PATH. The Signature approach proposes a two-stage will. "
  "Stage one is unconscious preparation: multiple action plans "
  "accumulate evidence in parallel, exactly like the decision "
  "accumulators, and the readiness potential is this preparation "
  "becoming visible — Schurger is right that it need not be 'the "
  "decision.' Stage two is conscious endorsement: when a plan nears "
  "threshold, it is broadcast to the global workspace, and the "
  "conscious system can veto it, delay it, or let it through — Libet's "
  "'free won't.' The feeling of willing is the readout of endorsement, "
  "which is why stimulation can fabricate it and why it can be "
  "manipulated apart from action. Soon et al.'s early decoding reads "
  "stage-one biases, not the final choice; the choice is made when "
  "endorsement meets threshold. This preserves both findings: the "
  "brain prepares before awareness AND conscious will does real work — "
  "as the gate, not the generator. "
  "PROPOSED MECHANISM. Parallel unconscious accumulators prepare "
  "actions; the leading candidate is broadcast; prefrontal circuits "
  "apply the veto-or-endorse decision within a ~200ms window before "
  "execution. Responsibility tracks the endorsement stage: actions "
  "endorsed are owned; actions that bypass it (reflexes, compulsions) "
  "are not. "
  "WHAT WOULD CONFIRM IT. If the veto window could be isolated — with "
  "disruption of prefrontal activity in that window selectively "
  "abolishing the ability to withhold prepared actions while leaving "
  "initiation intact — the two-stage proposal gains support. "
  "WHAT WOULD REFUTE IT. If conscious intention proved to have zero "
  "causal effect under all manipulations — vetoes never changing "
  "outcomes — or if initiation itself proved consciously controlled "
  "with no unconscious preparation, the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not settle the philosophical free-"
  "will debate, it does not assign legal responsibility, and it does "
  "not claim proof."),
 "key_points": [
  "Libet (1983) found the readiness potential precedes reported decisions by about half a second.",
  "Soon et al. (2008) decoded choices seconds before awareness; Schurger (2012) modeled the readiness potential as noise crossing threshold.",
  "Intention, decision, action, and the feeling of willing can be dissociated experimentally.",
  "The Signature proposal: two-stage will — unconscious parallel preparation, then conscious endorsement-or-veto in a late window; will is the gate, not the generator.",
  "Selective veto-window disruption abolishing withholding but sparing initiation would confirm it; zero causal effect of intention would refute it."],
 "requirements": [
  "Accept unconscious preparation as established.",
  "Grant conscious intention real causal power as veto/selection.",
  "Reinterpret the readiness potential as preparation, not decision.",
  "Locate responsibility at the endorsement stage.",
  "Demand a falsifiable veto-window experiment."],
 "standards": [
  "Libet clock-paradigm intention timing.",
  "Pre-movement decoding protocols.",
  "Agency-manipulation experimental designs."],
 "citations": [
  "Libet B, et al. Time of conscious intention to act. Brain; 1983.",
  "Soon CS, et al. Unconscious determinants of free decisions in the human brain. Nature Neuroscience; 2008.",
  "Schurger A, et al. An accumulator model for spontaneous neural activity prior to self-initiated movement. PNAS; 2012."],
},
]
