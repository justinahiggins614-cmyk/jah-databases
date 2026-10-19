#!/usr/bin/env python3
"""34 ladder-ordered unsolved neuroscience problems (public) + Signature editions.
The Unsolved Neuroscience Database / The Unsolved Neuroscience Signature Database.
Manon 2026-10-17 16:15 orders, Unsolved Problems Solved series batch 1.
Every signature_solution opens with the exact honesty label. Descriptive and
educational only: no diagnosing real people, no medical claims, nothing
presented as established science that is not.
"""

POINTER = ("Signature-generated proposed solution — not established science. "
           "This public record states the problem exactly as the field knows "
           "it today. The Signature edition of this same record develops the "
           "full Signature proposed solution approach: the assumptions, the "
           "reasoning path, the proposed mechanism, what evidence would "
           "confirm it and what would refute it, and what it does not claim. "
           "The problem itself remains open in established science.")

ENTRIES = [
# ---------------------------------------------------------------- 1-12 Foundations
{
 "key": "why_we_dream",
 "name": "Why We Dream",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": ("Every night the human brain spends roughly two hours generating "
             "vivid hallucinations that we call dreams, mostly during REM "
             "sleep, while the body lies paralyzed and the outside world is "
             "shut out. Nobody knows why. The brain consumes about a fifth of "
             "the body's energy at rest; spending that energy on elaborate "
             "fictions every night for a lifetime is enormously expensive, so "
             "evolution must be buying something with it — but after a "
             "century of research there is no agreed answer about what."),
 "background": ("Sigmund Freud's 1899 Interpretation of Dreams proposed dreams "
                "as disguised wish fulfillment, the first famous theory, but "
                "modern neuroscience treats it as largely untestable. The "
                "discovery of REM sleep in 1953 by Aserinsky and Kleitman gave "
                "the problem a physiological anchor: dreams cluster in REM, "
                "when the brainstem fires in PGO waves and the visual cortex "
                "is active while the prefrontal cortex — the seat of logic "
                "and self-monitoring — is suppressed. J. Allan Hobson and "
                "Robert McCarley's 1977 activation-synthesis hypothesis "
                "argued the dreaming brain is just the forebrain trying to "
                "make sense of random brainstem noise. Competing accounts "
                "include the threat-simulation theory of Antti Revonsuo "
                "(dreams rehearse survival), the memory-consolidation view "
                "(dreams replay and integrate the day), and the emotional "
                "regulation view of Matthew Walker (REM strips the emotional "
                "charge from painful memories). All have supporting evidence; "
                "none commands consensus, and some researchers argue dreams "
                "may be a spandrel — a side effect of offline brain activity "
                "with no function at all."),
 "why_it_matters": ("If dreaming serves memory, emotion, or threat rehearsal, "
                    "understanding it would change how we treat trauma, "
                    "learning, and sleep disorders, and it would tell us "
                    "whether artificial systems need an offline dream phase "
                    "too. If dreams are functionless, that tells us something "
                    "equally deep: the most vivid experiences of our lives "
                    "are an accident of the machinery. Either answer "
                    "reshapes the science of the mind."),
 "sig_lens": ("Signature lens: dreams are the brain running its generator "
              "with the world disconnected — the Signature view treats the "
              "dream as a nightly training run of the brain's world model."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain is a prediction machine: it maintains a "
  "generative model of the world and constantly predicts its own sensory "
  "input. (2) During REM sleep, sensory input is gated off but the "
  "generator keeps running, producing the brain's best guesses with no "
  "correction from reality. (3) Nightly offline runs are cheaper than "
  "waking rehearsal because the body is still. "
  "REASONING PATH. The Signature approach starts from the known fact that "
  "the dreaming brain is highly active in sensory and emotional regions "
  "while logic and self-monitoring regions are suppressed — exactly the "
  "configuration a world-model would need for uncorrected generative "
  "rehearsal. It proposes that dreams are the brain stress-testing its "
  "own model: each dream is a counterfactual rollout — what would happen "
  "if — and the emotional charge of dreams is the model's loss function "
  "being computed on simulated outcomes. Threat scenarios recur not "
  "because dreams evolved to rehearse tigers, but because high-stakes "
  "counterfactuals are where the model's errors are costliest. "
  "PROPOSED MECHANISM. During waking, the model updates on prediction "
  "error. During REM, the model runs free rollouts and updates on "
  "internally generated surprise: the mismatch between the dream's "
  "predicted arc and its actual simulated arc. This is why dreams feel "
  "real while lasting and absurd in hindsight — no error signal arrives "
  "to correct them. "
  "WHAT WOULD CONFIRM IT. A controlled experiment where subjects learn a "
  "new skill, then dream content is decoded from sleep brain activity: if "
  "the decoded dream rollouts systematically precede next-day performance "
  "gains on exactly the simulated subtasks, the proposal gains support. "
  "WHAT WOULD REFUTE IT. If suppressing dream generation entirely (in a "
  "way that leaves sleep architecture intact) leaves learning, emotional "
  "regulation, and model accuracy completely unchanged across large "
  "samples, the generative-rehearsal proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim dreams have hidden meanings "
  "about the dreamer's life, it does not claim the brain literally "
  "simulates physics during dreams, and it does not claim proof — it is "
  "a proposed frame, offered for testing, not a settled answer."),
 "key_points": [
  "Dreams cluster in REM sleep, when the brainstem fires PGO waves, visual cortex is active, and the prefrontal cortex is suppressed.",
  "Freud (1899) proposed wish fulfillment; Hobson and McCarley (1977) proposed activation-synthesis; Revonsuo proposed threat simulation.",
  "Competing functions on the table: memory consolidation, emotional regulation, threat rehearsal, or no function at all.",
  "The Signature proposal: dreams are uncorrected generative rollouts — the brain stress-testing its own world model offline.",
  "Confirming evidence would link decoded dream content to next-day performance gains; a clean refutation would be zero learning cost from dream suppression."],
 "requirements": [
  "Accept the prediction-machine premise: the brain maintains a generative model of the world.",
  "Accept that REM gates sensory input while the generator keeps running.",
  "Treat dream emotion as the model's internally computed loss on simulated outcomes.",
  "Require that any proposed mechanism predict which dream contents aid next-day performance.",
  "Demand a falsifiable test: selective dream suppression with intact sleep architecture."],
 "standards": [
  "Polysomnography and REM staging standards (AASM manual).",
  "Dream-report collection and blind content scoring methods.",
  "Sleep-deprivation and selective REM-deprivation experimental designs."],
 "citations": [
  "Freud S. The Interpretation of Dreams. 1899.",
  "Hobson JA, McCarley RW. The brain as a dream state generator. American Journal of Psychiatry; 1977.",
  "Walker M. Why We Sleep. Scribner; 2017."],
},
{
 "key": "what_attention_is",
 "name": "What Attention Is",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": ("At every moment your senses deliver far more information than "
             "your brain can process, yet you experience a single coherent "
             "scene and can deliberately pick out one voice in a crowded "
             "room. Attention is the brain's selection mechanism, and "
             "although its effects are among the most replicated findings in "
             "psychology, nobody knows what attention actually is at the "
             "neural level. Is it a spotlight, a filter, a gain control, a "
             "competition, or something else entirely? The mechanism that "
             "decides what gets processed and what gets ignored remains "
             "unresolved."),
 "background": ("William James wrote in 1890 that attention is the taking "
                "possession by the mind of one out of several possible "
                "objects — and the field has been refining that sentence "
                "ever since. Donald Broadbent's 1958 filter theory proposed "
                "an early bottleneck; Anne Treisman's attenuation and "
                "feature-integration work moved selection later and showed "
                "features bind only when attended. In the 1990s the "
                "biased-competition model of Desimone and Duncan reframed "
                "attention as a competition among neural representations, "
                "biased by goals and salience. Michael Posner's attention "
                "networks, Stanislas Dehaene's global workspace, and the "
                "predictive-coding accounts of Karl Friston each place "
                "attention somewhere different: network, workspace "
                "ignition, or precision-weighting of prediction errors. "
                "Single-neuron recordings show attention multiplies firing "
                "rates and sharpens tuning, EEG shows rhythmic sampling at "
                "theta frequencies, but no experiment has yet shown which "
                "of these descriptions is the mechanism and which are "
                "its shadows."),
 "why_it_matters": ("Attention gates learning, memory, and consciousness "
                    "itself — you cannot remember what you never attended. "
                    "Disorders of attention shape millions of lives, and "
                    "every artificial intelligence that selects among inputs "
                    "is implicitly betting on a theory of attention. "
                    "Settling what attention is would unify psychology, "
                    "neuroscience, and machine intelligence around a single "
                    "selection principle."),
 "sig_lens": ("Signature lens: attention is the brain's precision dial — the "
              "Signature view treats attending as turning up the gain on "
              "the prediction errors that matter and turning it down on "
              "the rest."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain minimizes prediction error across a "
  "hierarchy of models. (2) Not all errors are equally trustworthy, so the "
  "brain must weight them — this weighting IS attention. (3) Weighting is "
  "implemented as gain control on error-carrying neurons, adjustable in "
  "milliseconds. "
  "REASONING PATH. The Signature approach dissolves the spotlight-versus-"
  "filter debate by proposing both are views of one operation: precision "
  "weighting. The spotlight is what precision looks like from the outside "
  "(a region of boosted gain); the filter is what it looks like from the "
  "inside (suppressed errors never reach the model). Rhythmic theta "
  "sampling is the signature of the weighting being recomputed — the "
  "brain re-asking, several times a second, which errors deserve trust. "
  "Biased competition falls out naturally: representations compete "
  "through mutually inhibitory error units, and the winner is the one "
  "whose errors the current precision map trusts most. "
  "PROPOSED MECHANISM. Precision is set by a fast control loop running "
  "through the pulvinar and frontal eye fields: salience and goals write "
  "a precision map, the map multiplies error signals, and the multiplied "
  "errors drive both perception and learning. Attentional blink, "
  "inattentional blindness, and the cocktail-party effect are all "
  "predictions of the same loop hitting its limits. "
  "WHAT WOULD CONFIRM IT. Simultaneous recordings showing that the "
  "precision map (in pulvinar/frontal circuits) predicts, trial by "
  "trial, which sensory errors get amplified downstream — with attention "
  "effects vanishing when the map is held fixed while goals change. "
  "WHAT WOULD REFUTE IT. If attention effects persist with zero change in "
  "any precision-like signal, or if a clean attentional selection occurs "
  "with no error-weighting anywhere in the circuit, the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim precision weighting explains "
  "consciousness, it does not claim the pulvinar is the only controller, "
  "and it does not claim proof — only a testable unification of the "
  "competing descriptions."),
 "key_points": [
  "William James (1890) framed attention as taking possession of one object among many; the definition still stands.",
  "Broadbent (1958) proposed an early filter; Treisman moved selection later and showed binding needs attention.",
  "The biased-competition model (Desimone and Duncan) reframes attention as competition among representations.",
  "The Signature proposal: attention is precision-weighting of prediction errors — spotlight and filter are two views of one gain operation.",
  "Confirming evidence would show a precision map predicting trial-by-trial amplification; absence of any precision signal would refute it."],
 "requirements": [
  "Accept the prediction-error premise: perception and learning run on error signals.",
  "Accept that error signals must be weighted by trustworthiness.",
  "Identify weighting with measurable gain control on error-carrying neurons.",
  "Require the precision map to precede and predict downstream attention effects.",
  "Demand a falsifiable circuit: attention without precision change kills the proposal."],
 "standards": [
  "Posner cueing and attentional-network task designs.",
  "Single-unit attention paradigms in visual cortex.",
  "EEG/MEG time-frequency analysis of theta rhythmic sampling."],
 "citations": [
  "James W. The Principles of Psychology. 1890.",
  "Desimone R, Duncan J. Neural mechanisms of selective visual attention. Annual Review of Neuroscience; 1995.",
  "Friston K. The free-energy principle. Nature Reviews Neuroscience; 2010."],
},
{
 "key": "why_we_forget",
 "name": "Why We Forget",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": ("The average person forgets the majority of what they "
             "experience within days, and most of what remains within "
             "years. Forgetting feels like a defect — a leaky memory system "
             "— but the leak is so systematic, so consistent across people "
             "and cultures, that it looks designed. The unsolved question "
             "is whether forgetting is a bug, a feature, or both: does the "
             "brain actively erase, passively decay, or strategically "
             "suppress, and what exactly is the function of losing "
             "information?"),
 "background": ("Hermann Ebbinghaus quantified the forgetting curve in 1885: "
                "retention drops steeply within the first day, then levels "
                "off — a curve replicated thousands of times since. Early "
                "theories blamed decay (traces fade with time) or "
                "interference (new memories overwrite old ones), and the "
                "two fought for a century. Modern work added active "
                "mechanisms: the hippocampus continually generates new "
                "neurons in a process called neurogenesis, and Frankland, "
                "Josselyn and colleagues showed this neurogenesis actively "
                "promotes forgetting — young animals with more neurogenesis "
                "forget faster. Molecular studies identified active erasure "
                "pathways, including dopamine-driven forgetting circuits in "
                "fruit flies and Rac1-dependent actin remodeling. Sleep "
                "research added another layer: the brain appears to "
                "downscale synapses globally during sleep, per the synaptic "
                "homeostasis hypothesis of Tononi and Cirelli. Yet the field "
                "still cannot say which forgetting is active erasure, "
                "which is interference, and which serves a computational "
                "purpose versus being mere capacity overflow."),
 "why_it_matters": ("If forgetting is designed, then memory disorders might "
                    "be disorders of forgetting rather than of remembering, "
                    "and treatments would target erasure, not storage. "
                    "Education, trauma therapy, and artificial intelligence "
                    "all depend on knowing what should be kept and what "
                    "should be lost. A theory of forgetting is half of a "
                    "theory of memory."),
 "sig_lens": ("Signature lens: forgetting is the brain's compression "
              "algorithm — the Signature view treats memory not as a "
              "recording but as a model, and forgetting as the model's "
              "regularization."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) Memory is not a recording; it is a generative model "
  "that must generalize, and generalization requires discarding detail. "
  "(2) The brain has finite synaptic resources, so some forgetting is "
  "forced. (3) The brain can distinguish predictive detail (worth keeping) "
  "from non-predictive detail (safe to drop). "
  "REASONING PATH. The Signature approach treats the Ebbinghaus curve as "
  "the visible trace of a regularization process. Just as a statistical "
  "model that memorizes every data point overfits and predicts poorly, a "
  "brain that kept every detail would drown in interference. Forgetting "
  "is the brain applying the equivalent of weight decay: traces that stop "
  "being retrieved stop being reinforced, and their synaptic weights "
  "relax toward the population mean. Active erasure — neurogenesis, "
  "dopamine-driven forgetting, sleep downscaling — is the same operation "
  "run deliberately on traces tagged as low-value. This explains why "
  "forgetting is steepest early (unretrieved traces decay fastest) and "
  "why emotional memories resist it (high predicted value keeps the "
  "weights up). "
  "PROPOSED MECHANISM. Each memory trace carries a value estimate updated "
  "by retrieval success and emotional salience. Traces below a dynamic "
  "threshold are released to decay; traces above it are consolidated. "
  "Sleep performs a global pass, multiplying all weights by a factor less "
  "than one — exactly the synaptic homeostasis finding — which "
  "preferentially erases the weak. "
  "WHAT WOULD CONFIRM IT. If memories could be scored for future "
  "predictive value and low-value memories were found to be "
  "preferentially erased by the known active mechanisms — with the "
  "Ebbinghaus curve's shape derivable from the value distribution — the "
  "proposal gains support. "
  "WHAT WOULD REFUTE IT. If active erasure mechanisms were blocked and "
  "memory capacity, generalization, and interference were all unchanged, "
  "or if high-value memories were found to decay at exactly the same "
  "rate as trivial ones, the regularization proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim all forgetting is useful "
  "(some is plain capacity overflow), it does not claim the value tag "
  "mechanism is identified, and it does not claim proof."),
 "key_points": [
  "Ebbinghaus (1885) measured the forgetting curve: steep early loss, then a long tail.",
  "Decay versus interference debated for a century; modern work adds active erasure via neurogenesis and dopamine-driven circuits.",
  "Tononi and Cirelli's synaptic homeostasis hypothesis proposes global synaptic downscaling during sleep.",
  "The Signature proposal: forgetting is regularization — the brain discarding non-predictive detail so the memory model generalizes.",
  "Value-tagged erasure would confirm it; equal decay for high- and low-value memories would refute it."],
 "requirements": [
  "Treat memory as a generative model, not a recording.",
  "Accept that generalization mathematically requires discarding detail.",
  "Map the Ebbinghaus curve onto weight decay with a value threshold.",
  "Require active erasure mechanisms to preferentially target low-value traces.",
  "Demand a falsifiable prediction about which memories survive."],
 "standards": [
  "Ebbinghaus savings-method retention paradigms.",
  "Directed-forgetting and retrieval-induced-forgetting task designs.",
  "Rodent neurogenesis-manipulation memory assays."],
 "citations": [
  "Ebbinghaus H. Memory: A Contribution to Experimental Psychology. 1885.",
  "Frankland PW, Josselyn SA, et al. Neurogenesis and forgetting. Trends in Neurosciences; 2013.",
  "Tononi G, Cirelli C. Sleep and the price of plasticity. Neuron; 2014."],
},
{
 "key": "memory_consolidation",
 "name": "How Memories Are Consolidated",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": ("A new experience is fragile: a blow to the head, a seizure, "
             "or even an interruption minutes afterward can erase it "
             "entirely. Yet weeks later the same memory can survive "
             "anything. Somewhere between minutes and months, memories are "
             "transformed from fragile to durable in a process called "
             "consolidation — and the full mechanism, the schedule, and "
             "the question of what exactly is being transferred from where "
             "to where remain unsolved."),
 "background": ("The standard model grew from patient H.M., studied by "
                "Brenda Milner from 1957: after hippocampal removal he "
                "could not form new long-term memories, proving the "
                "hippocampus is needed for consolidation while old "
                "memories survived without it. The model says the "
                "hippocampus rapidly encodes new episodes and then "
                "gradually teaches the cortex over weeks, through replay "
                "during sleep — a view supported by the discovery of "
                "hippocampal replay in rodents by Wilson, McNaughton, and "
                "later by the identification of sharp-wave ripples as the "
                "replay events. But the multiple-trace theory of Nadel and "
                "Moscovitch countered that the hippocampus is always "
                "needed for vivid episodic memory, and recent work shows "
                "some memories consolidate in hours, others never fully "
                "leave the hippocampus, and schema-consistent memories can "
                "consolidate almost immediately. The field now juggles "
                "synaptic consolidation (minutes to hours, protein "
                "synthesis), systems consolidation (weeks to years, "
                "hippocampus to cortex), and reconsolidation (recalled "
                "memories become fragile again) — three processes whose "
                "relationship is still disputed."),
 "why_it_matters": ("Consolidation is the bottleneck between experience and "
                    "lasting knowledge. Understanding it would transform "
                    "education schedules, trauma treatment (blocking "
                    "consolidation of traumatic memories), and dementia "
                    "care. Every learning machine also faces the same "
                    "problem — how to make fast learning durable without "
                    "breaking old knowledge."),
 "sig_lens": ("Signature lens: consolidation is a two-timescale handshake — "
              "the Signature view treats the hippocampus as the brain's "
              "fast scratchpad and the cortex as its slow library, with "
              "sleep as the nightly librarian."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) Fast learning and stable knowledge conflict: one "
  "network cannot do both well. (2) The brain solves this with two "
  "learners: a fast, high-plasticity hippocampal system and a slow, "
  "low-plasticity cortical system. (3) Transfer happens by replay: the "
  "fast system replays experiences to the slow system during offline "
  "periods. "
  "REASONING PATH. The Signature approach formalizes the classic "
  "complementary-learning-systems idea and resolves its puzzles. "
  "Schema-consistent memories consolidate fast because the slow system "
  "needs only a small update — the knowledge nearly fits already. "
  "Reconsolidation exists because retrieval returns a memory to the fast "
  "system for re-encoding, making it fragile again until re-transferred. "
  "The multiple-trace objection is absorbed: vivid episodic detail stays "
  "hippocampal because the cortex stores compressed gist, not because "
  "transfer failed — the system keeps two formats by design, like keeping "
  "both a photo and its caption. "
  "PROPOSED MECHANISM. Sharp-wave ripples during sleep are the transfer "
  "protocol: each ripple is a compressed replay packet, and cortical "
  "plasticity during the ripple writes the packet into slow weights. The "
  "transfer rate is set by prediction error — surprising experiences get "
  "more replay packets, which is why novelty consolidates faster. "
  "WHAT WOULD CONFIRM IT. If ripple-triggered disruption selectively "
  "blocks transfer of exactly the replayed content — decoded in advance "
  "from the ripple — while leaving other memories intact, the packet "
  "model gains support. "
  "WHAT WOULD REFUTE IT. If memories were found to consolidate fully "
  "with zero replay events detected across all offline periods, or if "
  "cortical learning proved to be as fast as hippocampal learning with "
  "no interference cost, the two-learner proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim every memory type uses this "
  "path (skills and habits use different circuits), it does not claim the "
  "transfer protocol is fully decoded, and it does not claim proof."),
 "key_points": [
  "Patient H.M. (Milner, 1957) showed the hippocampus is needed to form new long-term memories.",
  "Hippocampal replay during sleep, carried by sharp-wave ripples, is the leading transfer mechanism.",
  "Synaptic consolidation takes minutes to hours; systems consolidation takes weeks to years; reconsolidation re-opens memories on recall.",
  "The Signature proposal: a two-learner handshake — fast hippocampal scratchpad teaches the slow cortical library via replay packets, prioritized by surprise.",
  "Ripple-triggered disruption of decoded content would confirm it; consolidation with zero replay would refute it."],
 "requirements": [
  "Accept the fast-versus-stable conflict as the core design problem.",
  "Assign fast learning to the hippocampus and slow learning to the cortex.",
  "Treat sharp-wave ripples as compressed replay packets.",
  "Require transfer priority to track prediction error.",
  "Demand a falsifiable replay-blocking experiment."],
 "standards": [
  "Sharp-wave ripple detection and closed-loop disruption methods.",
  "Rodent replay decoding from place-cell sequences.",
  "Human sleep targeted-memory-reactivation paradigms."],
 "citations": [
  "Milner B. Psychological defects produced by temporal lobe excision. 1957.",
  "McClelland JL, McNaughton BL, O'Reilly RC. Why there are complementary learning systems. Psychological Review; 1995.",
  "Nadel L, Moscovitch M. Memory consolidation, retrograde amnesia and the hippocampal complex. Current Opinion in Neurobiology; 1997."],
},
{
 "key": "deja_vu",
 "name": "What Causes Deja Vu",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": ("Roughly two out of three people have felt it: a new scene "
             "arrives wrapped in an eerie certainty that it has happened "
             "before. Deja vu is one of the most common strange experiences "
             "in human life, it is brief, it cannot be summoned on demand, "
             "and it leaves no trace to study afterward. The result is a "
             "famous unsolved problem: what neural event manufactures a "
             "false feeling of familiarity for something genuinely new?"),
 "background": ("Explanations have ranged from the paranormal (past lives, "
                "precognition) to the neurological. The serious science "
                "began with the observation that deja vu can be triggered "
                "by temporal-lobe seizures — Hughlings Jackson noted in "
                "the 19th century that epileptic auras sometimes include "
                "dreamy states of false familiarity, implicating the "
                "medial temporal lobe. Modern theories cluster around "
                "three ideas: a timing glitch (the familiarity signal fires "
                "milliseconds before the perceptual details arrive), a "
                "memory-mismatch (the scene matches a stored fragment — a "
                "similar doorway, a similar light — and the match is "
                "misattributed to the whole), and a source-monitoring error "
                "(the brain correctly detects familiarity but mislabels "
                "its source). Laboratory analogues exist: Anne Cleary's "
                "work shows that scenes sharing spatial layout with "
                "previously seen scenes trigger deja vu-like familiarity, "
                "and subliminal priming can manufacture it. But no theory "
                "has been caught in the act during a spontaneous episode, "
                "because spontaneous episodes cannot be scheduled inside a "
                "scanner."),
 "why_it_matters": ("Deja vu is a natural experiment in how the brain tags "
                    "experience as familiar or new — and that tag underlies "
                    "recognition, false memory, eyewitness reliability, and "
                    "the feeling of knowing. Understanding the glitch would "
                    "illuminate the normal machinery, and it would settle "
                    "whether some of our most uncanny experiences are "
                    "features or misfires."),
 "sig_lens": ("Signature lens: deja vu is a misdated receipt — the "
              "Signature view treats familiarity as a separate signal from "
              "recollection, and deja vu as the signal arriving without "
              "its paperwork."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain computes two separable outputs for every "
  "scene: a familiarity signal (have I processed something like this) "
  "and a recollection signal (what exactly, and when). (2) The two "
  "signals travel different paths with different latencies. (3) The "
  "conscious feeling of 'I have been here before' is constructed after "
  "both arrive, by attributing the familiarity to the current scene. "
  "REASONING PATH. The Signature approach proposes that deja vu is a "
  "race condition: the fast familiarity pathway — which responds to "
  "partial matches like spatial layout or gist — occasionally fires "
  "ahead of, or stronger than, the slower recollection pathway that "
  "would normally veto it by reporting 'similar, but new.' In ordinary "
  "perception the veto arrives in time and the scene feels merely "
  "reminiscent. In deja vu the familiarity signal wins the race, and the "
  "brain, finding a strong familiarity tag with no source attached, does "
  "what it always does with unexplained signals: it attributes them to "
  "the present moment. The eeriness is the residue of the failed veto — "
  "the system's own error flag, felt as strangeness. "
  "PROPOSED MECHANISM. Perirhinal familiarity computations complete "
  "roughly tens of milliseconds before hippocampal pattern-completion "
  "verdicts. Fatigue, stress, or a slightly over-excitable temporal lobe "
  "widens that window; when the window exceeds the veto latency, deja vu "
  "occurs. This predicts deja vu peaks in the teens and twenties (peak "
  "temporal-lobe excitability) and under exhaustion. "
  "WHAT WOULD CONFIRM IT. High-temporal-resolution recordings catching a "
  "spontaneous episode and showing the familiarity response preceding "
  "the recollection verdict by an abnormal margin, with the veto "
  "arriving late — a direct observation of the lost race. "
  "WHAT WOULD REFUTE IT. If spontaneous episodes showed no timing "
  "anomaly and no familiarity-recollection dissociation — the two "
  "signals arriving together and correctly — the race-condition proposal "
  "fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim precognition or past lives, "
  "it does not claim every episode shares one mechanism, and it does not "
  "claim proof — spontaneous episodes remain unobserved in the act."),
 "key_points": [
  "About two-thirds of people experience deja vu; it is brief, unschedulable, and leaves no trace.",
  "Temporal-lobe seizure auras can include false familiarity, implicating the medial temporal lobe.",
  "Leading theories: timing glitch, memory-mismatch misattribution, and source-monitoring error.",
  "The Signature proposal: a race condition — the fast familiarity signal beats the slower recollection veto, and the brain attributes the orphan signal to the present.",
  "Catching an episode with the familiarity response abnormally preceding the verdict would confirm it; no timing anomaly would refute it."],
 "requirements": [
  "Separate familiarity from recollection as distinct computed signals.",
  "Accept that the two signals travel paths with different latencies.",
  "Treat the feeling of familiarity as constructed after both signals arrive.",
  "Predict the age and fatigue distribution from excitability and window width.",
  "Demand a falsifiable in-the-act recording of the lost race."],
 "standards": [
  "Deja vu laboratory analogues (Cleary spatial-layout paradigms).",
  "Intracranial EEG timing of perirhinal versus hippocampal responses.",
  "Temporal-lobe epilepsy aura documentation standards."],
 "citations": [
  "Cleary AM. Recognition memory, familiarity, and deja vu experiences. Current Directions in Psychological Science; 2008.",
  "Brown AS. The Deja Vu Experience. Psychology Press; 2004.",
  "Jackson JH. Selected Writings on epilepsy and epileptiform convulsions; 1931."],
},
{
 "key": "prediction_error_learning",
 "name": "How the Brain Learns From Prediction Errors",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": ("When reality surprises you — the light turns green but no "
             "cars move, the expected reward never arrives — your brain "
             "updates its model of the world within seconds. Somewhere a "
             "difference is computed between what was predicted and what "
             "happened, and that difference rewrites synapses. The "
             "existence of prediction-error learning is well established, "
             "but how the brain computes the error, where the subtraction "
             "happens, and how a single error signal can correctly assign "
             "credit to the millions of synapses that caused it remain "
             "unsolved."),
 "background": ("The story began with the Rescorla-Wagner model of 1972, "
                "which described animal conditioning as driven by the "
                "difference between expected and received reward. In 1997 "
                "Wolfram Schultz recorded from monkey dopamine neurons and "
                "found them firing exactly like a reward-prediction error: "
                "bursting for unexpected reward, silent for fully predicted "
                "reward, dipping when expected reward was omitted — one of "
                "the cleanest matches between a psychological model and a "
                "neural signal ever found. Temporal-difference learning, "
                "formalized by Sutton and Barto, gave the mathematics; "
                "human fMRI found prediction-error signals in the striatum "
                "and beyond. But the clean story frays at the edges: "
                "dopamine also responds to novelty, movement, and threat; "
                "the brain must compute errors for vision, motor control, "
                "and abstract beliefs, not just reward; and the credit-"
                "assignment problem — how the error reaches the right "
                "synapses — has no agreed biological solution. The field "
                "knows the brain learns from surprise; it does not know "
                "the wiring."),
 "why_it_matters": ("Prediction-error learning is the engine of adaptive "
                    "behavior — it is how habits form, how addictions take "
                    "hold, how children learn cause and effect. Disorders "
                    "from addiction to schizophrenia have been reframed as "
                    "disorders of prediction. And every reinforcement-"
                    "learning AI is built on this principle — understanding "
                    "the brain's version would improve both medicine and "
                    "machines."),
 "sig_lens": ("Signature lens: surprise is the brain's currency — the "
              "Signature view treats every prediction error as a payment "
              "that buys a precise, local synaptic update."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain computes prediction errors locally, at every "
  "level of every hierarchy, not in one central dopamine office. (2) "
  "Dopamine broadcasts a global modulatory signal — roughly, how "
  "surprising things are overall — while local circuits compute their own "
  "signed errors. (3) Credit assignment is solved by eligibility traces: "
  "synapses tag themselves when active, and the global signal later "
  "decides which tagged synapses change. "
  "REASONING PATH. The Signature approach resolves the dopamine debate by "
  "splitting the error into two parts. Local error units — found "
  "throughout cortex as neurons that fire to mismatch — compute the "
  "signed difference for their own patch of the world. Dopamine is not "
  "the error; it is the volume knob on plasticity, turned by aggregate "
  "surprise. This explains why dopamine responds to novelty and movement "
  "too: anything surprising turns up the knob. Credit assignment then "
  "needs no miracle: a synapse that was recently active carries a "
  "decaying eligibility tag, and when the global surprise signal arrives, "
  "only tagged synapses update, in the direction of their local error. "
  "The Rescorla-Wagner and temporal-difference equations emerge as the "
  "average behavior of this two-part system. "
  "PROPOSED MECHANISM. Three-factor plasticity: presynaptic activity "
  "times postsynaptic activity sets the tag; the local error sets the "
  "sign; the diffuse modulatory signal sets the rate. All three are "
  "biologically documented pieces; the proposal is that together they "
  "are the complete learning rule. "
  "WHAT WOULD CONFIRM IT. An experiment showing that blocking local "
  "error signals abolishes learning even when dopamine is intact, while "
  "blocking dopamine only slows learning without changing what is "
  "learned — separating the sign from the volume. "
  "WHAT WOULD REFUTE IT. If learning were found to require no local "
  "error computation anywhere — pure global-signal learning with correct "
  "credit assignment — or if eligibility tags proved absent at the "
  "relevant synapses, the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim dopamine has no error "
  "content, it does not claim the three factors are sufficient for "
  "abstract belief learning, and it does not claim proof."),
 "key_points": [
  "Rescorla and Wagner (1972) modeled conditioning as driven by expectation minus outcome.",
  "Schultz (1997) found monkey dopamine neurons firing exactly like a reward-prediction error.",
  "Temporal-difference learning (Sutton and Barto) gave the mathematics; fMRI found error signals in human striatum.",
  "The Signature proposal: local circuits compute signed errors, dopamine is the global plasticity volume knob, and eligibility tags solve credit assignment.",
  "Separating the sign (local error) from the volume (dopamine) experimentally would confirm it; pure global-signal learning would refute it."],
 "requirements": [
  "Split prediction error into local signed errors and a global modulatory signal.",
  "Accept eligibility traces as the biological credit-assignment mechanism.",
  "Recover Rescorla-Wagner and temporal-difference as average behavior.",
  "Require that blocking local errors abolishes learning while blocking dopamine only slows it.",
  "Demand a falsifiable dissociation of sign from volume."],
 "standards": [
  "Schultz-style reward-prediction-error recording paradigms.",
  "Three-factor plasticity slice-physiology protocols.",
  "Human computational-modeling of trial-by-trial learning."],
 "citations": [
  "Rescorla RA, Wagner AR. A theory of Pavlovian conditioning. 1972.",
  "Schultz W, Dayan P, Montague PR. A neural substrate of prediction and reward. Science; 1997.",
  "Sutton RS, Barto AG. Reinforcement Learning. MIT Press; 1998."],
},
{
 "key": "pain_in_the_brain",
 "name": "What Pain Is in the Brain",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": ("Pain is the most common reason people seek medical care, yet "
             "there is no pain meter — no scan, no blood test, no "
             "objective measure of how much pain anyone is in. Two people "
             "with identical injuries can report wildly different pain, "
             "and people can feel agony in limbs that no longer exist. "
             "The unsolved problem is the gap between nociception (the "
             "neural detection of tissue damage) and pain (the conscious "
             "experience): where, and how, does a damage signal become "
             "suffering?"),
 "background": ("The specificity theory of the 19th century treated pain as "
                "a dedicated labeled line from skin to brain. Ronald "
                "Melzack and Patrick Wall's 1965 gate-control theory "
                "revolutionized the field: the spinal cord contains a "
                "'gate' where non-painful input can inhibit pain signals, "
                "explaining why rubbing a bump helps. Melzack later "
                "proposed the neuromatrix — pain as an output of a "
                "distributed brain network, not a readout of a sensor. "
                "Modern imaging finds no single 'pain center'; instead a "
                "network including insula, anterior cingulate, and "
                "somatosensory cortex tracks pain, but these regions also "
                "track salience, attention, and emotion. Tor Wager's "
                "neurologic pain signature can predict pain reports from "
                "brain patterns above chance, yet it still cannot tell "
                "pain from intense non-painful salience with certainty. "
                "Phantom-limb pain and placebo analgesia prove the brain "
                "generates pain top-down — but the transformation from "
                "signal to experience remains unmapped."),
 "why_it_matters": ("Chronic pain disables more people than any other "
                    "condition, and the opioid crisis was born of treating "
                    "pain we cannot measure. An objective account of how "
                    "damage becomes suffering would change diagnosis, "
                    "drug development, and the ethics of pain care. It "
                    "would also answer a deep question: is pain a "
                    "perception like vision, constructed by the brain, "
                    "rather than a sensation delivered by the body?"),
 "sig_lens": ("Signature lens: pain is the brain's protected alarm — the "
              "Signature view treats pain not as a measurement of damage "
              "but as the brain's decision that protection is needed."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) Nociception and pain are different things: the first "
  "is data, the second is a decision. (2) The brain maintains a model of "
  "the body's integrity and computes a protection policy from it. (3) "
  "Pain is the conscious readout of that policy, not of the raw data. "
  "REASONING PATH. The Signature approach explains every classic puzzle "
  "with one move. Phantom-limb pain: the body's integrity model still "
  "contains the limb, and the policy still protects it. Placebo "
  "analgesia: belief updates the model's threat estimate, so the policy "
  "relaxes. Why identical injuries hurt differently: the policy weighs "
  "context — a soldier's wound in battle gets a low protection setting "
  "because action is needed; the same wound at home gets a high one. "
  "The gate in the spinal cord is the policy's first actuator, and the "
  "insula-cingulate network is where the policy's output becomes "
  "conscious. Pain is to nociception what a fire alarm is to a smoke "
  "sensor: the sensor reports particles, the alarm decides whether to "
  "ring, and the decision depends on the building's state. "
  "PROPOSED MECHANISM. A threat-estimation circuit integrates nociceptive "
  "input, contextual cues, prior injury history, and attentional state "
  "into a single protection variable; when the variable crosses a "
  "dynamic threshold, the pain experience is generated and descending "
  "modulation adjusts the spinal gate. Chronic pain is the threshold "
  "stuck low after the model learns that protection 'worked.' "
  "WHAT WOULD CONFIRM IT. If the protection variable could be read out — "
  "a neural pattern that predicts pain reports better than nociceptive "
  "input does, across contexts including placebo and phantom cases — the "
  "proposal gains support. "
  "WHAT WOULD REFUTE IT. If pain reports tracked nociceptive input "
  "perfectly across all contexts with no top-down modulation measurable "
  "anywhere, the decision-model proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim anyone's pain is imaginary "
  "(the alarm is real even when the smoke is not), it does not offer "
  "medical advice, it does not diagnose or treat any person, and it does "
  "not claim proof — it is a descriptive frame only."),
 "key_points": [
  "Melzack and Wall (1965) proposed gate control: the spinal cord can inhibit pain signals.",
  "No single pain center exists; a distributed network tracks pain but also salience and emotion.",
  "Phantom-limb pain and placebo analgesia prove top-down generation of pain.",
  "The Signature proposal: nociception is data, pain is a protection decision — the brain's alarm policy, not a damage meter.",
  "A neural protection variable predicting reports better than raw input would confirm it; perfect tracking of input would refute it."],
 "requirements": [
  "Separate nociception (data) from pain (decision).",
  "Model the body's integrity and a protection policy computed from it.",
  "Explain phantom pain, placebo, and context effects as policy outputs.",
  "Require a readable protection variable that beats raw input at predicting reports.",
  "Keep the account descriptive and educational; no medical claims, no diagnosis."],
 "standards": [
  "Quantitative sensory testing protocols.",
  "Wager neurologic pain signature validation methods.",
  "Placebo analgesia experimental designs."],
 "citations": [
  "Melzack R, Wall PD. Pain mechanisms: a new theory. Science; 1965.",
  "Melzack R. From the gate to the neuromatrix. Pain; 1999.",
  "Wager TD, et al. An fMRI-based neurologic signature of physical pain. New England Journal of Medicine; 2013."],
},
{
 "key": "body_ownership",
 "name": "How the Brain Feels Its Own Body",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": ("You feel your body from the inside — you know where your "
             "hands are with your eyes closed, and you feel that your body "
             "is yours. This sense of embodiment seems so basic it is "
             "barely noticed, yet it is a construction: the brain fuses "
             "vision, touch, proprioception, and balance into a single "
             "feeling of 'this is me.' How the brain builds and maintains "
             "this body model — and why it can be so easily fooled — is "
             "unsolved."),
 "background": ("The rubber-hand illusion, discovered by Botvinick and "
                "Cohen in 1998, showed the trick in its simplest form: "
                "stroke a visible rubber hand in synchrony with a "
                "subject's hidden real hand, and the subject starts to "
                "feel the rubber hand as their own, with proprioception "
                "drifting toward it. Henrik Ehrsson extended this to full-"
                "body illusions, swapping subjects' perceived bodies with "
                "mannequins using virtual reality. The temporoparietal "
                "junction and premotor cortex emerged as key nodes, and "
                "interoception — sensing the internal body, mapped in the "
                "insula by researchers like Bud Craig — turned out to be "
                "deeply tied to the sense of self. Predictive-coding "
                "accounts now frame body ownership as inference: the brain "
                "decides which body is mine by finding the hypothesis that "
                "best explains the multisensory evidence. But the "
                "computation — how conflicting signals are weighted, what "
                "sets the 'mine' boundary, why the illusion breaks with "
                "asynchronous stroking — has no agreed mechanistic "
                "account."),
 "why_it_matters": ("Body ownership underlies everything from tool use (a "
                    "blind person's cane becomes part of the body schema) "
                    "to phantom limbs, eating disorders, and the design of "
                    "prosthetics and virtual reality. If we knew the "
                    "brain's ownership rule, we could build prosthetics "
                    "the brain accepts as self and virtual worlds it "
                    "inhabits fully."),
 "sig_lens": ("Signature lens: the body is a hypothesis — the Signature "
              "view treats 'this is mine' as the brain's best explanation "
              "of correlated multisensory evidence, recomputed continuously."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain never senses the body directly; it infers "
  "it from multisensory correlations. (2) Ownership is the winning "
  "hypothesis in a continuous Bayesian model comparison. (3) The prior "
  "favors a single, roughly human-shaped body — but the prior can be "
  "overridden by strong evidence. "
  "REASONING PATH. The Signature approach treats the rubber-hand "
  "illusion as model selection in action. Synchronous stroking makes the "
  "'rubber hand is mine' hypothesis explain the visual-tactile "
  "correlation far better than the 'my hand is hidden' hypothesis, so "
  "the brain switches winners — and proprioception, now serving the new "
  "winner, drifts toward the rubber hand. Asynchronous stroking breaks "
  "the correlation, the old hypothesis wins, and the illusion dies. "
  "Tool embodiment, phantom limbs, and full-body swaps are the same "
  "computation with different evidence: the cane's tip correlates with "
  "touch, so the body model extends; the amputated limb's model persists "
  "because no contradictory evidence arrives. The 'mine' boundary is "
  "wherever the winning hypothesis draws it. "
  "PROPOSED MECHANISM. Premotor and temporoparietal circuits run the "
  "comparison: each candidate body hypothesis predicts the incoming "
  "multisensory stream, prediction errors accumulate per hypothesis, and "
  "the lowest-error hypothesis captures ownership and proprioceptive "
  "calibration. The insula contributes interoceptive evidence — the "
  "heartbeat-synced component that makes the owned body feel alive from "
  "the inside. "
  "WHAT WOULD CONFIRM IT. If ownership switches could be predicted, "
  "trial by trial, from measured multisensory prediction errors per "
  "hypothesis — with the switch occurring exactly when the error "
  "crossover happens — the proposal gains support. "
  "WHAT WOULD REFUTE IT. If ownership changed with no change in the "
  "multisensory evidence or error signals, or if the prior proved "
  "un-overridable (illusions impossible under any evidence), the "
  "proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the computation is "
  "conscious, it does not claim a complete circuit map, and it does not "
  "claim proof."),
 "key_points": [
  "The rubber-hand illusion (Botvinick and Cohen, 1998) shows synchronous stroking transfers ownership to a fake hand.",
  "Full-body illusions extend ownership to mannequins and avatars; interoception in the insula ties ownership to the sense of self.",
  "Predictive-coding accounts frame ownership as Bayesian inference over multisensory evidence.",
  "The Signature proposal: ownership is continuous model selection — the lowest-error body hypothesis wins, and proprioception serves the winner.",
  "Trial-by-trial prediction of ownership switches from error crossovers would confirm it; evidence-free switches would refute it."],
 "requirements": [
  "Treat the body as inferred, never directly sensed.",
  "Run ownership as Bayesian model comparison over body hypotheses.",
  "Explain synchrony dependence as correlation evidence for the winning hypothesis.",
  "Require error-crossover to precede ownership switches.",
  "Demand a falsifiable prediction about when illusions must fail."],
 "standards": [
  "Rubber-hand and full-body illusion induction protocols.",
  "Proprioceptive-drift measurement methods.",
  "Multisensory temporal-binding window paradigms."],
 "citations": [
  "Botvinick M, Cohen J. Rubber hands feel touch. Nature; 1998.",
  "Ehrsson HH. The experimental induction of out-of-body experiences. Science; 2007.",
  "Craig AD. How Do You Feel? Princeton University Press; 2015."],
},
{
 "key": "few_shot_learning",
 "name": "How the Brain Learns From Very Few Examples",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": ("A child sees a zebra once and recognizes zebras forever. A "
             "machine-learning system typically needs thousands of labeled "
             "zebras. The human brain learns new concepts, words, and "
             "skills from one or a handful of examples — few-shot learning "
             "— and does it routinely. How the brain achieves this data "
             "efficiency, when its synapses change slowly and its neurons "
             "are noisy, is one of the great unsolved puzzles of learning."),
 "background": ("The puzzle sharpened as deep learning rose: artificial "
                "networks are data-hungry, yet humans are data-efficient, "
                "which suggests the brain is doing something structurally "
                "different. Candidate explanations include strong priors "
                "(the brain brings powerful assumptions to each new "
                "example, per the Bayesian program-learning work of Lake, "
                "Salakhutdinov, and Tenenbaum), compositionality (new "
                "concepts are built from known parts — a zebra is a horse "
                "plus stripes), hippocampal one-shot encoding (the fast "
                "learner of complementary learning systems stores the "
                "single episode immediately), and meta-learning (the brain "
                "has learned how to learn, so each new task starts from a "
                "good initialization). Sleep replay may then consolidate "
                "the single example into cortical structure. Each account "
                "has evidence; none explains the full phenomenon, and the "
                "field cannot yet say which combination the brain actually "
                "uses, or how the pieces fit together in one system."),
 "why_it_matters": ("Data efficiency is the central gap between human and "
                    "artificial intelligence. Understanding the brain's "
                    "few-shot trick would transform machine learning, "
                    "education (teaching so that one example suffices), "
                    "and our understanding of what makes human cognition "
                    "special. It is also a window into priors: what the "
                    "brain already knows before the first example."),
 "sig_lens": ("Signature lens: one example is enough when the scaffolding "
              "is ready — the Signature view treats few-shot learning as "
              "the fast learner filing a single episode into a deeply "
              "prepared prior."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain arrives at every new example with a rich "
  "generative prior built over a lifetime. (2) New concepts are encoded "
  "compositionally — as programs assembled from known parts. (3) A fast "
  "hippocampal store captures the single episode; slow cortical "
  "learning then distills it. "
  "REASONING PATH. The Signature approach proposes that few-shot "
  "learning is inference, not training. When the child sees the zebra, "
  "the brain does not adjust millions of weights from scratch; it runs "
  "program induction — searching its library of parts (horse shape, "
  "stripe pattern, four legs) for the shortest program that generates "
  "the observed animal. One example suffices because the hypothesis "
  "space is already carved by the prior: the search starts near the "
  "answer. The hippocampus stores the raw episode as an anchor, and "
  "sleep replay then trains the cortical network on variations sampled "
  "from the induced program — the brain generating its own training "
  "data from one example. This explains why few-shot learning fails for "
  "truly alien concepts (no parts, no prior) and succeeds for "
  "compositional ones. "
  "PROPOSED MECHANISM. Concept learning is Bayesian program induction "
  "over a part library; the hippocampus holds the episode; offline "
  "replay performs self-distillation, sampling synthetic variations "
  "from the induced program to train slow weights. "
  "WHAT WOULD CONFIRM IT. If disrupting sleep replay after a single-"
  "example learning trial selectively destroyed the generalization "
  "while sparing recall of the episode itself, the self-distillation "
  "proposal gains support. "
  "WHAT WOULD REFUTE IT. If one-shot generalization survived complete "
  "replay blockade with no loss, or if concept learning proved "
  "non-compositional at the neural level (no part-based encoding "
  "detectable), the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the part library is fully "
  "mapped, it does not claim program induction is the whole story for "
  "motor skills, and it does not claim proof."),
 "key_points": [
  "Humans learn concepts from one example; typical machine systems need thousands.",
  "Candidate accounts: strong priors, compositionality, hippocampal one-shot encoding, meta-learning.",
  "Lake, Salakhutdinov, and Tenenbaum showed Bayesian program learning can match human one-shot performance.",
  "The Signature proposal: few-shot learning is program induction over a part library, anchored by the hippocampus and distilled by sleep replay.",
  "Replay blockade sparing recall but killing generalization would confirm it; generalization without replay would refute it."],
 "requirements": [
  "Treat new-concept learning as inference over a prepared prior, not training from scratch.",
  "Require compositionality: new concepts assemble from known parts.",
  "Assign the single episode to the fast hippocampal store.",
  "Require sleep replay to self-distill variations for the slow system.",
  "Demand a falsifiable replay-blockade prediction."],
 "standards": [
  "One-shot categorization task designs.",
  "Bayesian program-learning evaluation benchmarks.",
  "Targeted memory reactivation during sleep."],
 "citations": [
  "Lake BM, Salakhutdinov R, Tenenbaum JB. Human-level concept learning through probabilistic program induction. Science; 2015.",
  "Tenenbaum JB, et al. How to grow a mind. Science; 2011.",
  "Kumaran D, Hassabis D, McClelland JL. What learning systems do intelligent agents need? Nature Reviews Neuroscience; 2016."],
},
{
 "key": "spatial_representation",
 "name": "How the Brain Represents Space",
 "group": "Foundations", "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": ("You can walk through your home in the dark, take a shortcut "
             "you have never taken, and point to the kitchen from the "
             "bedroom. Somewhere in the brain there is a map — a "
             "representation of space that supports navigation, memory, "
             "and imagination. The discovery of place cells and grid cells "
             "revealed pieces of this map, but how the pieces combine into "
             "a usable cognitive map, how the map handles three "
             "dimensions, and how it is reused for non-spatial thinking "
             "remain unsolved."),
 "background": ("John O'Keefe discovered place cells in the rat hippocampus "
                "in 1971: neurons that fire when the animal is in a "
                "specific location. In 2005 May-Britt and Edvard Moser "
                "discovered grid cells in the entorhinal cortex, firing in "
                "a hexagonal lattice across space — a coordinate system. "
                "The trio shared the 2014 Nobel Prize. Head-direction "
                "cells, border cells, and speed cells completed the "
                "navigation toolkit. Then came the surprises: grid cells "
                "remap and distort, the same circuits activate during "
                "non-spatial tasks like organizing concepts and memories, "
                "and human navigation relies heavily on landmarks and "
                "language, not just path integration. The field now asks "
                "whether the cognitive map is really a map of space at "
                "all, or a general relational memory system that space "
                "happens to use — and how a hexagonal lattice in a flat "
                "sheet of cortex represents the three-dimensional world."),
 "why_it_matters": ("The spatial system is the best-understood circuit in "
                    "the mammalian brain and the template for how "
                    "representation might work everywhere else. If the "
                    "cognitive map is general-purpose, understanding it "
                    "unlocks memory, planning, and abstract thought. It "
                    "also matters practically: navigation fails early in "
                    "Alzheimer's disease, and the spatial circuits are "
                    "among the first affected."),
 "sig_lens": ("Signature lens: space is the brain's first coordinate "
              "system — the Signature view treats the cognitive map as "
              "the prototype that all abstract thought reuses."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain needs a reusable coordinate framework, not "
  "just a record of places. (2) Grid cells provide that framework: a "
  "metric, path-integration-based coordinate system. (3) The hippocampus "
  "binds coordinates to content — what happened where — and the same "
  "binding machinery is reused for non-spatial relations. "
  "REASONING PATH. The Signature approach proposes that the entorhinal-"
  "hippocampal system is a general relational engine wearing a spatial "
  "costume. Grid cells compute position in an abstract state space by "
  "path integration; place cells are conjunctions of position and "
  "sensory content; and the hippocampus stores episodes as positions in "
  "this space plus their content. When the task is navigation, the state "
  "space is physical; when the task is organizing bird species or social "
  "hierarchies, the same grid-like code maps the conceptual space — "
  "which is why grid-like signals appear in non-spatial tasks. Three-"
  "dimensional navigation works because the lattice is a 2D projection "
  "of a higher-dimensional code, sufficient for animals that mostly move "
  "on surfaces. Shortcuts and pointing work because the map supports "
  "vector computations between any two positions. "
  "PROPOSED MECHANISM. Continuous-attractor networks in entorhinal "
  "cortex maintain the grid phase by integrating velocity; hippocampal "
  "place cells read out conjunctions; downstream circuits compute "
  "vectors between positions for planning. Non-spatial reuse is the "
  "same circuit with non-spatial velocity inputs. "
  "WHAT WOULD CONFIRM IT. If disrupting grid-cell periodicity "
  "selectively impaired relational inference in non-spatial tasks while "
  "sparing simple recognition, the general-engine proposal gains "
  "support. "
  "WHAT WOULD REFUTE IT. If grid-like codes in conceptual tasks proved "
  "to be a different, unrelated signal, or if navigation survived "
  "complete grid disruption with no deficit, the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the map is the only "
  "navigation system (landmarks and habits run in parallel), it does not "
  "claim the 3D code is fully characterized, and it does not claim "
  "proof."),
 "key_points": [
  "O'Keefe (1971) discovered place cells; the Mosers (2005) discovered grid cells; Nobel Prize 2014.",
  "Head-direction, border, and speed cells complete the navigation toolkit.",
  "Grid-like codes appear in non-spatial tasks, suggesting a general relational engine.",
  "The Signature proposal: the entorhinal-hippocampal system is a general state-space mapper; space is its first and clearest use.",
  "Selective loss of relational inference with grid disruption would confirm it; unrelated conceptual codes would refute it."],
 "requirements": [
  "Treat grid cells as a reusable coordinate framework, not a place list.",
  "Bind coordinates to content in the hippocampus.",
  "Explain non-spatial grid signals as reuse with non-spatial velocity inputs.",
  "Require vector computation between positions for shortcuts and pointing.",
  "Demand a falsifiable disruption experiment on relational inference."],
 "standards": [
  "Rodent place-cell and grid-cell recording protocols.",
  "Human fMRI grid-like signal analysis methods.",
  "Virtual-reality navigation task designs."],
 "citations": [
  "O'Keefe J, Dostrovsky J. The hippocampus as a spatial map. Brain Research; 1971.",
  "Hafting T, Fyhn M, Molden S, Moser MB, Moser EI. Microstructure of a spatial map in the entorhinal cortex. Nature; 2005.",
  "Behrens TEJ, et al. What is a cognitive map? Neuron; 2018."],
},
{
 "key": "working_memory_limits",
 "name": "How Working Memory Holds So Little",
 "group": "Foundations", "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": ("You can hold a phone number in mind just long enough to dial "
             "it — about seven digits, fewer if distracted. Working memory, "
             "the brain's mental scratchpad, holds only three to four "
             "items at once, a limit so severe it shapes all of human "
             "thought. The puzzle is why the limit exists at all: the "
             "brain has 86 billion neurons, yet it can juggle only a "
             "handful of items. What sets the capacity, and what is an "
             "'item'?"),
 "background": ("George Miller's famous 1956 paper proposed seven plus or "
                "minus two; Alan Baddeley's multicomponent model (1974, "
                "with Hitch) divided working memory into the phonological "
                "loop, visuospatial sketchpad, and central executive. "
                "Nelson Cowan's careful experiments revised capacity down "
                "to about four chunks. Neural theories followed: "
                "persistent firing in prefrontal cortex (Goldman-Rakic), "
                "synaptic models where memories are held in transient "
                "weight changes, and oscillatory models where items are "
                "multiplexed in gamma cycles nested in theta — the "
                "Lisman-Idiart proposal that capacity equals the number of "
                "gamma cycles per theta cycle, about seven, later refined "
                "toward four. Recent work shows the limit is flexible: "
                "chunking expands it, expertise expands it, and the limit "
                "may be on precision rather than item count — a resource "
                "model where more items means noisier memories. The field "
                "still cannot say what physically enforces the limit."),
 "why_it_matters": ("Working memory capacity predicts reasoning ability, "
                    "learning speed, and academic achievement better than "
                    "almost any other single measure. Understanding the "
                    "limit would change education, interface design, and "
                    "the treatment of disorders where working memory fails. "
                    "It is also the sharpest known constraint on human "
                    "thought — the bottleneck everything intelligent must "
                    "pass through."),
 "sig_lens": ("Signature lens: the scratchpad is a broadcast channel — the "
              "Signature view treats working memory as the narrow stage "
              "where the brain's parallel processes take turns."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) The brain's unconscious processes are massively "
  "parallel, but flexible reasoning needs a serial workspace. (2) The "
  "workspace is implemented as a globally broadcast representation — "
  "whatever is in working memory is available to all processes. (3) "
  "Broadcast requires a shared code, and the shared code has limited "
  "bandwidth. "
  "REASONING PATH. The Signature approach proposes that the capacity "
  "limit is a bandwidth limit on the broadcast channel. Unconscious "
  "modules process vast information in parallel, but to cooperate on a "
  "novel problem they must communicate through the global workspace, "
  "and the workspace can only carry a few high-precision items at once "
  "— like a meeting where everyone can talk but only one presentation "
  "fits on the screen. Chunking works because a chunk is one broadcast "
  "item pointing to a rich unconscious structure. The gamma-theta "
  "nesting is the channel's time-division multiplexing: each gamma "
  "cycle is a time slot, each theta cycle a frame, and the number of "
  "slots per frame is the capacity. Precision trades against count "
  "because the channel's total bit rate is fixed. "
  "PROPOSED MECHANISM. Prefrontal-parietal circuits maintain the "
  "broadcast items via rhythmic multiplexing; the bit rate of the "
  "channel — set by oscillation frequencies and neural noise — fixes "
  "capacity at three to four high-precision items. Training expands "
  "effective capacity by building better chunks, never by widening the "
  "channel. "
  "WHAT WOULD CONFIRM IT. If the channel's bit rate could be measured "
  "independently (from oscillation parameters and noise) and predicted "
  "each individual's capacity — with capacity changing when the rate is "
  "experimentally altered — the proposal gains support. "
  "WHAT WOULD REFUTE IT. If capacity proved independent of any "
  "broadcast-like mechanism — for example, if items were maintained "
  "with zero global availability yet still counted against the limit — "
  "the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not claim the channel is the only "
  "memory store, it does not claim capacity cannot be improved by "
  "chunking, and it does not claim proof."),
 "key_points": [
  "Miller (1956) proposed seven plus or minus two; Cowan revised capacity to about four chunks.",
  "Baddeley and Hitch (1974) divided working memory into loop, sketchpad, and executive.",
  "Oscillatory models propose items are multiplexed in gamma cycles nested in theta cycles.",
  "The Signature proposal: capacity is the bit rate of a global broadcast channel — a few high-precision items, with precision trading against count.",
  "Predicting individual capacity from measured channel parameters would confirm it; capacity without broadcast would refute it."],
 "requirements": [
  "Treat working memory as a serial global workspace over parallel unconscious processes.",
  "Identify the capacity limit with the broadcast channel's bit rate.",
  "Explain chunking as one broadcast item pointing to rich structure.",
  "Require oscillation parameters to predict individual capacity.",
  "Demand a falsifiable channel-rate manipulation."],
 "standards": [
  "Change-detection and complex-span capacity paradigms.",
  "EEG/MEG cross-frequency coupling analysis.",
  "Prefrontal persistent-activity recording protocols."],
 "citations": [
  "Miller GA. The magical number seven, plus or minus two. Psychological Review; 1956.",
  "Baddeley AD, Hitch G. Working memory. Psychology of Learning and Motivation; 1974.",
  "Cowan N. The magical number 4 in short-term memory. Behavioral and Brain Sciences; 2001."],
},
{
 "key": "sensory_cancellation",
 "name": "How the Brain Predicts and Cancels Its Own Sensations",
 "group": "Foundations", "ladder_rank": 12, "ladder_tier": "foundations",
 "problem": ("You cannot tickle yourself. When you speak, your auditory "
             "cortex dampens its response to your own voice; when you move "
             "your eyes, the world does not smear. The brain constantly "
             "predicts the sensory consequences of its own actions and "
             "subtracts them — a trick called sensory cancellation or "
             "corollary discharge. The phenomenon is clear, but the full "
             "circuit, the precision of the prediction, and what happens "
             "when cancellation fails remain unsolved."),
 "background": ("The concept of corollary discharge dates to von Holst and "
                "Mittelstaedt in 1950 and Roger Sperry's work on fish eye "
                "movements: a copy of the motor command (efference copy) is "
                "sent to sensory areas to cancel the expected sensation. "
                "In primates, the superior colliculus pathway through the "
                "thalamus provides the eye-movement copy that keeps vision "
                "stable across saccades. Human studies show auditory cortex "
                "suppresses responses to self-produced speech, and the "
                "cerebellum is the leading candidate for the comparator "
                "that predicts sensory consequences of movement. The "
                "clinical stakes rose when researchers proposed that "
                "failures of cancellation explain psychotic symptoms: if "
                "inner speech is not tagged as self-produced, it may be "
                "experienced as an alien voice. But the complete pathway — "
                "from motor command to precise sensory prediction to "
                "subtraction — has never been traced end to end in any "
                "system, and the brain's prediction is far more precise "
                "than current models explain."),
 "why_it_matters": ("Sensory cancellation is the brain's solution to the "
                    "self-versus-world problem: without it, every action "
                    "would feel like the world attacking you. Understanding "
                    "it illuminates the sense of agency, the stability of "
                    "perception, and possibly the origins of psychotic "
                    "symptoms. Every robot and virtual-reality system faces "
                    "the same problem and currently solves it worse than "
                    "the brain does."),
 "sig_lens": ("Signature lens: the brain signs its own work — the "
              "Signature view treats cancellation as the brain stamping "
              "self-produced sensations so the world model is never "
              "confused by its own actions."),
 "signature_solution_full": ("Signature-generated proposed solution — not "
  "established science. "
  "ASSUMPTIONS. (1) Every motor command generates an efference copy "
  "routed to sensory areas. (2) A forward model transforms the copy "
  "into a precise sensory prediction. (3) The prediction is subtracted "
  "from incoming sensation; the remainder is attributed to the world. "
  "REASONING PATH. The Signature approach proposes that cancellation is "
  "not a single subtraction but a signature-verification system. The "
  "forward model — likely cerebellar — does not merely predict what the "
  "sensation will be; it computes a confidence interval around the "
  "prediction. Sensation inside the interval is canceled and tagged "
  "self; sensation outside it passes through as world. This explains the "
  "precision puzzle: the system is accurate because it only cancels what "
  "it predicts confidently, and lets the rest through. Tickle fails on "
  "oneself because the prediction is near-perfect; a delayed or altered "
  "touch (as in classic experiments with delayed self-tickle devices) "
  "escapes cancellation and becomes ticklish. When the forward model "
  "degrades, self-produced signals leak into the world channel — the "
  "proposed basis for certain psychotic experiences, framed here as a "
  "hypothesis, not a diagnosis. "
  "PROPOSED MECHANISM. Cerebellar circuits learn the forward model by "
  "comparing efference copies with actual sensory outcomes; the "
  "prediction plus its uncertainty travels via thalamic pathways to "
  "sensory cortex, where a subtraction circuit cancels the predicted "
  "component. The residual — the unpredicted part — is what we perceive. "
  "WHAT WOULD CONFIRM IT. If the uncertainty interval could be measured "
  "neuraly and shown to set the cancellation boundary — with "
  "manipulations of predicted precision shifting exactly which "
  "self-produced sensations get through — the proposal gains support. "
  "WHAT WOULD REFUTE IT. If cancellation proved all-or-none with no "
  "precision grading, or if precise cancellation persisted with the "
  "forward model fully lesioned, the proposal fails. "
  "WHAT IT DOES NOT CLAIM. It does not diagnose any person or condition, "
  "it does not claim the cerebellum is the only forward model, and it "
  "does not claim proof — it is a descriptive frame only."),
 "key_points": [
  "Von Holst, Mittelstaedt, and Sperry established corollary discharge: motor copies cancel expected sensation.",
  "You cannot tickle yourself because the touch is precisely predicted; delaying it restores ticklishness.",
  "The cerebellum is the leading candidate for the forward model; thalamic pathways carry the copy.",
  "The Signature proposal: cancellation is signature-verification — predictions carry uncertainty intervals, and only confident predictions are canceled and tagged self.",
  "Measuring the uncertainty interval setting the cancellation boundary would confirm it; all-or-none cancellation would refute it."],
 "requirements": [
  "Route an efference copy of every motor command to sensory areas.",
  "Compute a forward-model prediction with a confidence interval.",
  "Subtract only the confidently predicted component; pass the residual as world.",
  "Explain self-tickle immunity and its breakdown under delay.",
  "Keep the account descriptive; no diagnosis of any person or condition."],
 "standards": [
  "Self-tickle and delayed-tactile-feedback paradigms.",
  "Saccadic suppression measurement protocols.",
  "Cerebellar forward-model learning assays."],
 "citations": [
  "Von Holst E, Mittelstaedt H. Das Reafferenzprinzip. 1950.",
  "Sperry RW. Neural basis of the spontaneous optokinetic response. Journal of Comparative Physiology; 1950.",
  "Blakemore SJ, Wolpert DM, Frith CD. Central cancellation of self-produced tickle sensation. Nature Neuroscience; 1998."],
},
]
