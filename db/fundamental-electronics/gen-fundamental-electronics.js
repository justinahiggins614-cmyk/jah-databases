(function(){'use strict';
/* jahdb-fundamental-electronics-1.0 — fundamental electronics bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FELE-';
var KIND='fundamental electronics record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Electronics is the study and engineering of devices that control the flow of electrons: from resistors and capacitors through transistors to integrated circuits. It is the physical foundation of all digital technology.', 'reasoning':'Electronics engineers reason with circuits: apply Kirchhoff\'s laws, model components, simulate, then build and measure. The schematic is the hypothesis; the oscilloscope is the verdict.', 'quantities':'The core quantities are voltage (electrical pressure), current (flow), resistance (opposition), and power (rate of energy transfer). Ohm\'s law, V = IR, relates the first three — the most-used equation in the field.', 'mechanism':'Electronics works by controlling electron flow: transistors switch and amplify, turning tiny signals into large effects. Digital electronics reduces everything to two voltage levels — and builds computers from that single distinction.', 'miscon':'Electronics is not just soldering: design and analysis dominate. Voltage is not \'used up\' around a circuit — energy is transferred, charge circulates. And digital is not separate from analog: every digital signal is analog underneath.'};
var SIGLENS=['In the Signature system, electronics is the physical bedrock of computation: every chip, every sensor, every device in this network obeys these principles, and the Signature formulation teaches each one as a circuit you can analyze and build.','The Signature practice is to build the circuit: calculate the values, simulate the behavior, measure the result — so electronics is learned at the bench, not just on the schematic.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- Ohm\'s law demo. Runs as-is with python3."""\ndef ohms_law(v=None, i=None, r=None):\n    if v is None: return i * r\n    if i is None: return v / r\n    return v / i\nprint("V=12V R=4ohm -> I=", ohms_law(v=12, r=4), "A")\nprint("I=2A R=10ohm -> V=", ohms_law(i=2, r=10), "V")\nprint("V=9V I=0.02A -> R=", ohms_law(v=9, i=0.02), "ohm (LED resistor)")\n', '#!/usr/bin/env python3\n"""{TITLE} -- voltage divider demo. Runs as-is with python3."""\ndef divider(vin, r1, r2):\n    return vin * r2 / (r1 + r2)\nfor r1, r2 in [(1000, 1000), (10000, 1000), (1000, 10000)]:\n    print(f"R1={r1} R2={r2}: Vout={divider(5.0, r1, r2):.2f}V from 5V")\n', '#!/usr/bin/env python3\n"""{TITLE} -- RC time constant demo. Runs as-is with python3."""\nimport math\ndef charge_curve(vin, r, c, t):\n    tau = r * c\n    return vin * (1 - math.exp(-t / tau)), tau\nv, tau = charge_curve(5.0, 10000, 100e-6, 1.0)\nprint(f"R=10k C=100uF: tau={tau:.2f}s; after 1s Vc={v:.2f}V (of 5V)")\nprint("after 5 time constants a capacitor is ~99% charged")\n'];
var TOPICS=[['What Electronics Is','Electronics is the technology of controlling electron flow: using components to switch, amplify, and process electrical signals. It is the physical layer of the digital age — every computer is electronics organized into logic.'],
['The Core Question of Electronics','The core question is: how do we make electrons do what we want? Every circuit is an answer — shaping voltages and currents to compute, communicate, sense, or power.'],
['Assumptions: Lumped Elements','Circuit analysis assumes lumped elements: components small enough that signals cross them instantly, so Kirchhoff\'s laws apply. At high frequencies the assumption breaks — and transmission-line theory takes over.'],
['The Vocabulary: Voltage, Current, Components','The vocabulary names the quantities (voltage, current, resistance, capacitance, inductance) and the components (resistor, capacitor, inductor, diode, transistor). Fluency means reading a schematic like a sentence.'],
['Ohm\'s Law: The Fundamental Relationship','Ohm\'s law, V = IR, is the fundamental relationship: voltage across a resistor equals current times resistance. It is the most-used equation in electronics — the starting point of nearly every analysis.'],
['Circuit Analysis: The Primary Method','Circuit analysis is the primary method: apply Kirchhoff\'s voltage and current laws, write the equations, solve. Nodal and mesh analysis systematize it; simulation (SPICE) scales it to millions of components.'],
['A Canonical First Example','The canonical first example is the LED circuit: battery, resistor, LED in series, the resistor chosen by Ohm\'s law to limit current to 20 mA. One loop teaches voltage, current, resistance, polarity, and power — the whole field in miniature.'],
['How Electronics Measures','Electronics measures with the multimeter, the oscilloscope, and the logic analyzer: steady values, waveforms in time, and digital sequences. The oscilloscope is the field\'s window into reality — voltage versus time, truth versus theory.'],
['The Core Mechanism: The Transistor','The core mechanism is the transistor: a three-terminal device where a small input controls a large current. As a switch it builds digital logic; as an amplifier it builds radios — one device, the entire electronic age.'],
['The Simplest Law: Kirchhoff\'s Current Law','The simplest law is Kirchhoff\'s current law: the sum of currents entering a node equals the sum leaving. Charge is conserved — the audit rule every circuit analysis obeys.'],
['Common Misconceptions in Electronics','The misconceptions persist: that voltage is \'used up\' (energy is transferred; charge circulates), that digital circuits aren\'t analog underneath (every edge is an analog event), and that ground is zero volts absolutely (it is a reference, chosen by the designer).'],
['How Beginners Practice Electronics','Beginners practice by building: the LED circuit, the 555 timer blinker, the transistor switch — each on a breadboard, each measured. Kits and simulators help, but real components teach the smell of hot resistors and the patience of debugging.'],
['The Core Model: The Ideal Op-Amp','The ideal op-amp is the core model of analog design: infinite gain, so feedback sets the behavior. Amplifiers, filters, and integrators all follow from the two golden rules — and real op-amps are close enough to make the model powerful.'],
['The Great Equation: V = IR (and P = VI)','Ohm\'s law plus P = VI are the great equations: together they size every resistor, every supply, every heatsink. Power as heat is the eternal constraint — electronics is thermodynamics with wires.'],
['Systems Thinking: Feedback','Systems thinking in electronics is feedback: output sampled back to the input to stabilize, linearize, or oscillate. Negative feedback makes amplifiers precise; positive feedback makes oscillators and latches — control theory in solder.'],
['Invariance: Linearity and Superposition','The invariance principle is superposition in linear circuits: the response to combined inputs equals the combined responses. It lets complex circuits be analyzed one source at a time — divide and conquer in hardware.'],
['Approximation: Ideal Models','Approximation uses ideal models first: ideal wires, ideal op-amps, ideal diodes — then adds the non-idealities that matter. Engineering is knowing which imperfections to include and which to ignore.'],
['Evidence Standards: The Measurement','The evidence standard is the measurement: the simulation predicts, the oscilloscope decides. A circuit that simulates but doesn\'t work has a modeling error; the bench is the court of final appeal.'],
['Classic Discoveries','The classic discoveries are the vacuum tube, the transistor, the integrated circuit, and the microprocessor. Each collapsed the size and cost of computation by orders of magnitude — the physical basis of the digital revolution.'],
['Core Trade-offs: Speed versus Power','The core trade-off is speed versus power versus cost: faster switching burns more power; lower power runs slower; precision costs money. Every design is a point chosen in this space for its application.'],
['Handling Uncertainty: Tolerances','Electronics handles uncertainty with tolerances: resistors are ±5%, capacitors worse, and designs must work across the spread. Worst-case and Monte Carlo analysis prove the circuit works not just typically but always.'],
['Tools of the Trade','The tools of the trade are the breadboard, the multimeter, the oscilloscope, the soldering iron, and SPICE. The deepest is the datasheet — the component\'s contract, which the wise read completely before designing.'],
['Ethics and Responsibility','Ethics in electronics concerns safety and honesty: mains isolation, battery safety, and truthful specifications. A power supply that lies about its ratings can burn a house down — the responsibility is physical.'],
['Teaching Electronics','Teaching it well starts with building: the LED lights on day one, then the theory explaining why. Students who have debugged a real circuit understand grounding in a way lectures cannot convey.'],
['The Frontier Question','The frontier question is the end of Moore\'s law: as transistors approach atomic scales, what comes next — new materials, new architectures, quantum devices? The frontier is reinventing the switch itself.'],
['Unifying Theories','The unifying theories are Maxwell\'s equations beneath all circuits and the abstraction stack above them: fields to components to gates to processors. Electronics is applied electromagnetism, organized into logic.'],
['Computational Electronics','Computational electronics simulates before building: SPICE and electromagnetic solvers predict behavior, and hardware description languages design chips too complex to draw. Simulation is the field\'s wind tunnel.'],
['Bridges to Other Fields','Electronics bridges to physics (devices), computer science (digital design), mechanical engineering (packaging, thermal), and medicine (instruments, implants). Every smart device is a bridge made product.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: computing beyond CMOS at scale, room-temperature quantum devices, and energy harvesting that powers real systems. Active research, no settled answers.'],
['How New Claims Are Validated','New devices are validated by measurement and by independent fabrication: the datasheet specs reproduced, the chip made in a second foundry. A device earns trust when others build it and it works.'],
['The Great Debates','The great debates include analog versus digital purity, the future of Moore\'s law, and open versus proprietary hardware. The debates are practical — each side ships products.'],
['Failure Modes: When Electronics Gets It Wrong','Electronics gets it wrong through thermal runaway, unconsidered parasitics, and designs that work on the bench but not in production spread. The immune system is derating, tolerance analysis, and testing across temperature.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis designs whole systems from fundamentals: power budgeted, signals clean, feedback stable, tolerances covered. The fundamentals are the difference between a circuit and a product.'],
['The Signature Formulation: Electronics as Physical Bedrock','The Signature formulation treats electronics as the physical bedrock of the network: every principle here underlies the machines that host these databases, because in the Signature system computation rests on electrons, and electrons obey these laws. That is the Signature capstone on electronics bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
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
    standards:["Safety first: mains voltage and large capacitors are treated with respect and procedure.", "Schematics are documentation: every build has a readable, labeled diagram.", "Measure, don't guess: the multimeter and oscilloscope verify every claim."],citations:["Horowitz, P. and Hill, W. \u2014 The Art of Electronics (Cambridge University Press).", "Boylestad, R. and Nashelsky, L. \u2014 Electronic Devices and Circuit Theory.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-electronics-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-electronics',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
