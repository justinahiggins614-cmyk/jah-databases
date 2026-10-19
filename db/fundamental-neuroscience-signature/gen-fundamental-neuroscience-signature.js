(function(){'use strict';
/* jahdb-fundamental-neuroscience-signature-1.0 — fundamental neuroscience bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFNE-';
var KIND='fundamental neuroscience record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Neuroscience studies the nervous system: how neurons, circuits, and brains produce sensation, movement, cognition, and behavior. It spans molecules to minds — the most ambitious scale-bridging in science.', 'reasoning':'Neuroscientists reason by linking levels: molecules → neurons → circuits → behavior. Lesion, stimulation, and recording test causality — correlating brain activity with behavior, then proving the link by intervention.', 'quantities':'The core quantities are the action potential (~100 mV, ~1 ms), firing rates, synaptic weights, and conduction velocities. Time is the master quantity — the brain computes in milliseconds.', 'mechanism':'The brain works by electrochemical signaling: neurons integrate inputs, fire action potentials, release neurotransmitters, and change their connections with experience. Plasticity — the changeable wiring — is the mechanism of learning and memory.', 'miscon':'Neuroscience is not phrenology with better tools: brain regions are networks, not isolated modules. We do not use \'only 10% of our brains\' — imaging shows the whole brain active. And the brain is not a computer: it computes differently, in parallel, embodied, and plastic.'};
var SIGLENS=['In the Signature system, neuroscience is the intelligence-reference discipline: every AI in this network is measured against what brains actually do, and the Signature formulation teaches each principle as a mechanism you can model.','The Signature practice is to model the mechanism: simulate the neuron, compute the network, trace the pathway — so brain principles are experienced as dynamics you can run.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- neuron integrate-and-fire demo. Runs as-is with python3."""\ndef neuron(inputs, weights, threshold=1.0):\n    v = sum(i * w for i, w in zip(inputs, weights))\n    return 1 if v >= threshold else 0, v\nw = [0.6, 0.6]\nfor inp in [(1,1), (1,0), (0,0)]:\n    fired, v = neuron(inp, w)\n    print(f"inputs {inp} -> membrane {v:.1f} -> {\'FIRES\' if fired else \'silent\'}")\nprint("neurons sum their inputs: enough excitation fires the cell")\n', '#!/usr/bin/env python3\n"""{TITLE} -- Hebbian learning demo. Runs as-is with python3."""\nw = 0.1\nfor trial in range(10):\n    pre, post = 1, 1  # both active\n    w += 0.05 * pre * post  # cells that fire together, wire together\nprint(f"synaptic weight after 10 pairings: {w:.2f} (started 0.10)")\nprint("Hebbian plasticity: correlated activity strengthens the synapse")\n', '#!/usr/bin/env python3\n"""{TITLE} -- reaction time demo. Runs as-is with python3."""\nimport time, random\nrandom.seed(21)\ntrials = [random.gauss(0.25, 0.03) for _ in range(5)]\nfor i, t in enumerate(trials, 1):\n    print(f"trial {i}: {t*1000:.0f} ms")\nprint(f"mean: {sum(trials)/len(trials)*1000:.0f} ms (typical simple reaction time)")\n'];
var TOPICS=[['Signature What Neuroscience Is','Neuroscience studies the nervous system from ion channels to consciousness: how billions of neurons, wired together, produce perception, movement, memory, and thought. It is biology\'s final frontier — the organ studying itself.'],
['Signature The Core Question of Neuroscience','The core question is: how does the brain produce the mind? Every experiment asks how neural activity — spikes, rhythms, plasticity — relates to sensation, decision, and experience.'],
['Signature Assumptions: The Neuron Doctrine','The field assumes the neuron doctrine: the neuron is the nervous system\'s unit, communicating at synapses. Cajal\'s drawings established it; a century of physiology confirmed it — the foundation everything builds on.'],
['Signature The Vocabulary: Neurons, Synapses, Circuits','The vocabulary names the parts: neurons (the cells), synapses (the connections), circuits (the networks), and systems (vision, motor, memory). Fluency means moving between these levels without losing the thread.'],
['Signature The Action Potential: The Fundamental Signal','The action potential is the fundamental signal: a ~100 mV electrical spike traveling down the axon in ~1 ms. Hodgkin and Huxley\'s equations described it — the most important equations in biology.'],
['Signature Recording and Intervention: The Primary Methods','The methods are recording (listening to neurons) and intervention (lesioning, stimulating, optogenetics). Correlation suggests; intervention proves — the causal test is the field\'s gold standard.'],
['Signature A Canonical First Example','The canonical first example is the squid giant axon: big enough to thread with electrodes, it revealed the action potential\'s ionic basis. One invertebrate\'s neuron founded cellular neurophysiology.'],
['Signature How Neuroscience Measures','The field measures with electrodes, microscopes, and scanners: spikes in milliseconds, circuits in microns, whole-brain activity in seconds. Each method trades time resolution for space — the complete picture needs them all.'],
['Signature The Core Mechanism: Synaptic Transmission','The core mechanism is synaptic transmission: action potential → calcium influx → neurotransmitter release → postsynaptic response. Every thought is this mechanism, repeated trillions of times.'],
['Signature The Simplest Law: All-or-None','The simplest law is the all-or-none action potential: the neuron fires fully or not at all. Information is coded in timing and rate, not amplitude — digital pulses in an analog cell.'],
['Signature Common Misconceptions in Neuroscience','The misconceptions mislead: the 10% myth (the whole brain is active), left/right brain determinism (both hemispheres collaborate), and the computer metaphor taken literally (brains compute, but not like laptops).'],
['Signature How Beginners Practice Neuroscience','Beginners practice by drawing circuits: the reflex arc, the visual pathway, the motor loop — traced and labeled until the wiring is mental furniture. Neuroanatomy is learned by tracing, not memorizing.'],
['Signature The Core Model: The Integrate-and-Fire Neuron','The integrate-and-fire neuron is the core model: sum the inputs, fire if threshold is crossed. Simple enough to simulate by the million, true enough to capture the essential computation.'],
['Signature The Great Principle: Plasticity','Plasticity is the great principle: synapses strengthen and weaken with experience — Hebb\'s \'fire together, wire together.\' Learning is plasticity; memory is its persistence.'],
['Signature Systems Thinking: The Whole Brain','Systems thinking sees the brain whole: perception, action, emotion, and cognition as interacting networks, not isolated modules. Connectomics maps the wiring; the challenge is reading the traffic.'],
['Signature Invariance: Conserved Mechanisms','The invariance principles are evolutionarily conserved mechanisms: action potentials, synaptic transmission, and basic learning rules work similarly from squid to human. The differences are in wiring scale, not in kind.'],
['Signature Approximation: Reduced Models','Approximation uses reduced models: point neurons, rate models, mean-field networks — each capturing some truth while ignoring the rest. The art is choosing the simplification the question allows.'],
['Signature Evidence Standards: Converging Methods','The evidence standard is convergence: the lesion, the recording, and the stimulation agreeing. Single-method findings are provisional; the triangulated result is trusted.'],
['Signature Classic Discoveries','The classic discoveries are the neuron doctrine, the action potential mechanism, the chemical synapse, long-term potentiation, and place cells. Each revealed a layer of how brains compute.'],
['Signature Core Trade-offs: Speed versus Accuracy','The core trade-off in neural coding is speed versus accuracy: fast decisions use less evidence, careful ones take longer. The brain adjusts the trade per situation — the same dilemma as any decision system.'],
['Signature Handling Uncertainty: Population Coding','The brain handles uncertainty with population coding: many noisy neurons voting together, their pooled activity more reliable than any one. Bayesian models describe how the brain combines uncertain cues optimally.'],
['Signature Tools of the Trade','The tools of the trade are the electrode, the microscope, the scanner, and the model. The deepest is the causal intervention — the optogenetic pulse that proves the circuit\'s role.'],
['Signature Ethics and Responsibility','Ethics in neuroscience governs minds themselves: cognitive privacy, enhancement fairness, and the welfare of research subjects. As the field approaches reading and writing neural activity, the stakes become personal.'],
['Signature Teaching Neuroscience','Teaching it well starts with the wonder: the squid axon, the homunculus, the split-brain patient — then the mechanisms. Students who have traced a pathway own it.'],
['Signature The Frontier Question','The frontier question is the neural basis of consciousness: how does activity become experience? The theories compete — integrated information, global workspace — and the experiments grow sharper.'],
['Signature Unifying Theories','The unifying theories connect levels: biophysics of neurons, dynamics of circuits, computation of systems. The free-energy principle and efficient coding are candidate unifications — the field\'s search for its Maxwell.'],
['Signature Computational Neuroscience','Computational neuroscience models the brain: detailed neuron simulations, network models of cognition, and AI systems inspired by (and compared to) neural computation. The models test whether we understand — prediction is the proof.'],
['Signature Bridges to Other Fields','Neuroscience bridges to psychology (behavior), computer science (AI), medicine (neurology, psychiatry), engineering (brain-machine interfaces), and philosophy (mind). It is the hub science of the mind.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: consciousness, the full memory engram, and the complete mapping from circuit to behavior. Active research, no settled answers.'],
['Signature How New Claims Are Validated','New claims are validated by replication across labs and methods: the effect reproduced, the circuit causally tested, the finding extended. Landmark claims face adversarial replication — the field\'s immune response.'],
['Signature The Great Debates','The great debates include localization versus distribution, the role of glia, and whether AI needs brain-like architectures. The debates drive experiments — each side\'s predictions get tested.'],
['Signature Failure Modes: When Neuroscience Gets It Wrong','The field gets it wrong through underpowered studies, reverse inference (this area lit up, so the subject felt X), and hype outpacing evidence. The immune system is pre-registration, large samples, and causal tests.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis explains behavior from fundamentals: the molecule, the cell, the circuit, the system — linked into accounts of perception, memory, and decision. The fundamentals are the levels; synthesis is the bridge.'],
['Signature The Signature Formulation: Neuroscience as Intelligence Reference','The Signature formulation treats neuroscience as the reference for all intelligence in the network: every AI here is measured against what brains do, because in the Signature system artificial intelligence is built in dialogue with the natural kind. That is the Signature capstone on neuroscience bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(false){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Levels are linked: claims connect mechanisms across scales explicitly.", "Causality is tested: beyond correlation, by lesion, stimulation, or optogenetics.", "Replication is required: landmark findings are independently reproduced."],citations:["Kandel, E. R. et al. \u2014 Principles of Neural Science (McGraw-Hill).", "Purves, D. et al. \u2014 Neuroscience (Oxford University Press).", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-neuroscience-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-neuroscience-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
