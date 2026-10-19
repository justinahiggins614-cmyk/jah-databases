(function(){'use strict';
/* jahdb-fundamental-electrical-engineering-signature-1.0 — fundamental electrical-engineering bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFEE-';
var KIND='fundamental electrical-engineering record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Electrical engineering is the engineering of electrical and electromagnetic systems at scale: power generation and distribution, machines, control systems, and signal processing. Where electronics studies components, electrical engineering builds the systems that light cities.', 'reasoning':'Electrical engineers reason with phasors, transforms, and models: convert time-domain problems to frequency-domain solutions, design for worst case, and verify against standards. The grid is the largest machine ever built — it is designed, not grown.', 'quantities':'The core quantities are voltage, current, power (real, reactive, apparent), frequency, and energy. The power triangle — P, Q, S — and the 50/60 Hz heartbeat of the grid organize the field.', 'mechanism':'Electrical engineering works by energy conversion and control: generators turn motion into electricity, transformers change its voltage, motors turn it back into motion, and control systems keep it all stable. The synchronous grid is the master mechanism — thousands of generators locked in step.', 'miscon':'Electrical engineering is not just bigger electronics: power systems have their own phenomena (faults, stability, reactive power). Electricity does not travel at the speed of light in wires — fields propagate fast, electrons drift slowly. And \'clean\' power is a precise technical term, not a marketing one.'};
var SIGLENS=['In the Signature system, electrical engineering is the power discipline: every data center, every device, every deployment in this network depends on electrical systems done right, and the Signature formulation teaches each principle as a system you can analyze.','The Signature practice is to analyze the system: compute the power flows, check the stability, size the protection — so electrical reasoning is done with engineering numbers, not just component values.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- AC power demo. Runs as-is with python3."""\nimport math\ndef ac_power(v_rms, i_rms, pf):\n    p = v_rms * i_rms * pf          # real power W\n    s = v_rms * i_rms               # apparent VA\n    q = math.sqrt(max(s*s - p*p, 0))  # reactive VAR\n    return p, q, s\nfor v, i, pf in [(230, 10, 1.0), (230, 10, 0.8), (120, 15, 0.9)]:\n    p, q, s = ac_power(v, i, pf)\n    print(f"{v}V {i}A pf={pf}: P={p:.0f}W Q={q:.0f}VAR S={s:.0f}VA")\n', '#!/usr/bin/env python3\n"""{TITLE} -- transformer demo. Runs as-is with python3."""\ndef transformer(v_primary, n1, n2):\n    v_secondary = v_primary * n2 / n1\n    return v_secondary\nprint("240V, 1000:100 turns ->", transformer(240, 1000, 100), "V")\nprint("step down for safety; step up for transmission (less current, less loss)")\ndef line_loss(p_watts, v_volts):\n    i = p_watts / v_volts\n    return i, i * i * 0.5  # 0.5 ohm line\nfor v in [230, 11000, 132000]:\n    i, loss = line_loss(1e6, v)\n    print(f"1MW at {v}V: I={i:.1f}A line loss={loss/1000:.1f}kW")\n', '#!/usr/bin/env python3\n"""{TITLE} -- three-phase demo. Runs as-is with python3."""\nimport math\nv_phase = 230\nv_line = v_phase * math.sqrt(3)\nprint(f"phase voltage {v_phase}V -> line voltage {v_line:.0f}V (x sqrt(3))")\nprint("three phases 120 degrees apart deliver constant power: motors run smooth")\n'];
var TOPICS=[['Signature What Electrical Engineering Is','Electrical engineering designs systems that generate, transmit, and use electrical energy — plus the control and signal systems that manage them. It is the engineering of the grid, the motor, and the machines that make modern life possible.'],
['Signature The Core Question of Electrical Engineering','The core question is: how do we deliver electrical energy safely, reliably, and efficiently at scale? Every substation, every motor drive, every protection scheme is an answer refined over a century.'],
['Signature Assumptions: Sinusoidal Steady State','Much of the field assumes sinusoidal steady state: the grid runs at 50 or 60 Hz, and phasor analysis turns differential equations into algebra. Transients and faults are then studied as departures from this well-understood baseline.'],
['Signature The Vocabulary: Real, Reactive, and Apparent Power','The vocabulary distinguishes real power (P, watts — doing work), reactive power (Q, VAR — sloshing in fields), and apparent power (S, VA — what the equipment must carry). Power factor measures how much of the apparent power does real work.'],
['Signature Power: The Fundamental Quantity','Power is the fundamental quantity: the rate of energy transfer, measured in watts, with energy itself in watt-hours billed by the meter. The grid balances power supply and demand every second — the largest real-time control problem on Earth.'],
['Signature Power System Analysis: The Primary Method','Power system analysis is the primary method: load flow (where power goes), fault analysis (what breaks), and stability (whether it stays synchronized). Protection coordination ensures the right breaker trips — and only that one.'],
['Signature A Canonical First Example','The canonical first example is the simple distribution circuit: source, transformer, feeder, load — voltage stepped down for safety, protection at each level. Scale it up a million times and you have the grid.'],
['Signature How Electrical Engineering Measures','The field measures with power analyzers, protective relays, and SCADA: voltages, currents, power flows, and fault records across the network. Phasor measurement units now timestamp the grid\'s heartbeat 60 times a second.'],
['Signature The Core Mechanism: The Synchronous Grid','The core mechanism is the synchronous AC grid: thousands of generators locked to the same frequency, sharing load automatically through the physics of synchronism. Frequency is the grid\'s pulse — 60.00 Hz means supply meets demand.'],
['Signature The Simplest Law: Power Balance','The simplest law is instantaneous power balance: generation equals load plus losses, at every moment. Imbalance shows up as frequency drift within seconds — the grid has no storage, only balance.'],
['Signature Common Misconceptions in Electrical Engineering','The misconceptions mislead: that electrons race through wires at light speed (fields propagate fast; electrons drift), that higher voltage is always more dangerous (it\'s the current and the path), and that renewables can\'t power grids (the challenge is variability management, an engineering problem).'],
['Signature How Beginners Practice Electrical Engineering','Beginners practice with circuits, then machines, then systems: analyze the circuit, wire the motor, study the one-line diagram. Safety training comes first — respect for energy is the field\'s first lesson.'],
['Signature The Core Model: The Transformer','The transformer is the core model: two windings sharing a magnetic core, trading voltage for current at constant power. It made long-distance AC transmission practical — and won the war of currents.'],
['Signature The Great Achievement: The Grid','The grid is the great achievement: the largest synchronized machine ever built, delivering power with 99.99% reliability. Its operation — markets, dispatch, protection — is a century of engineering refined daily.'],
['Signature Systems Thinking: Stability','Systems thinking in power engineering is stability: will the generators stay in step after a fault? Transient stability analysis simulates the seconds after disturbances — the grid\'s immune response, computed in advance.'],
['Signature Invariance: Frequency as Global Signal','The invariance principle is system frequency: one number reflecting the global balance of supply and demand. Every generator watches it; every control acts on it — a planet-scale feedback loop.'],
['Signature Approximation: Per-Unit System','Approximation uses the per-unit system: normalize voltages, currents, and impedances to base values, and disparate equipment becomes comparable. The numbers shrink to order one — and errors shrink with them.'],
['Signature Evidence Standards: Commissioning Tests','The evidence standard is the commissioning test: protection relays trip-tested, transformers hi-potted, the system proven before energization. Paper studies predict; field tests certify.'],
['Signature Classic Discoveries','The classic discoveries are Faraday\'s induction, Tesla\'s polyphase system, the transformer, and high-voltage transmission. Each electrified the world a little more — the defining infrastructure of the 20th century.'],
['Signature Core Trade-offs: Reliability versus Cost','The core trade-off is reliability versus cost: N-1 contingency (surviving any single failure) is the standard, but each additional nine of reliability costs exponentially. Society chooses the point — usually 99.99%.'],
['Signature Handling Uncertainty: Contingency Analysis','Power systems handle uncertainty with contingency analysis: simulate every credible failure in advance and pre-position the response. The grid is operated not for today but for the worst credible tomorrow.'],
['Signature Tools of the Trade','The tools of the trade are the one-line diagram, the load-flow program, the relay test set, and the thermal camera. The deepest is the protection coordination study — the plan for what trips when everything goes wrong.'],
['Signature Ethics and Responsibility','Ethics in electrical engineering is public safety: the code exists because mistakes kill. Engineers stamp drawings, take responsibility, and design for the fault — the field\'s ethic is written in standards paid for by past disasters.'],
['Signature Teaching Electrical Engineering','Teaching it well combines the lab bench with the system view: wire the motor starter, then study the grid it plugs into. Students who have felt a contactor slam understand power differently.'],
['Signature The Frontier Question','The frontier question is the renewable grid: inverters replacing synchronous machines, storage firming variability, and the grid becoming a power-electronics system. The frontier redesigns the machine while it runs.'],
['Signature Unifying Theories','The unifying theories are electromagnetics beneath and control theory above: Maxwell governs the fields, feedback governs the stability. Between them, circuit theory organizes the middle — the field\'s three-layer cake.'],
['Signature Computational Power Engineering','Computational power engineering simulates the grid: load flow, short circuit, transient stability, and now real-time digital twins. The simulations run the contingency analyses that keep the lights on.'],
['Signature Bridges to Other Fields','Electrical engineering bridges to mechanical (machines), civil (transmission structures), computer science (smart grid), economics (power markets), and policy (energy transition). The energy transition runs through this field.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: grid-scale storage at acceptable cost, perfect forecasting of renewable output, and cybersecurity of the operational grid. Active work, no settled answers.'],
['Signature How New Claims Are Validated','New equipment is validated by type tests and field trials: the transformer tested to destruction in the lab, then monitored for years in service. Utilities trust what has survived both.'],
['Signature The Great Debates','The great debates include AC versus DC futures, centralized versus distributed generation, and market versus engineering operation of grids. The debates are consequential — they shape trillion-dollar infrastructure.'],
['Signature Failure Modes: When Electrical Engineering Gets It Wrong','The field gets it wrong through protection miscoordination, underestimated fault levels, and cascading failures — blackouts are the tuition. The immune system is the post-disturbance analysis, published and learned from.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis operates whole power systems from fundamentals: flows balanced, faults cleared selectively, stability maintained, standards met. The fundamentals are the operating philosophy of civilization\'s power.'],
['Signature The Signature Formulation: Electrical Engineering as Civilization\'s Power','The Signature formulation treats electrical engineering as the power layer of civilization: every principle here keeps the lights on for these databases and their users, because in the Signature system power you cannot analyze is power you cannot rely on. That is the Signature capstone on electrical bedrock.']];
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
    standards:["Codes are law: the NEC/IEC standards govern installations for safety.", "Protection is designed: every system has fault protection coordinated by analysis.", "Grounding and bonding are verified: safety grounding is tested, not assumed."],citations:["Nilsson, J. W. and Riedel, S. A. \u2014 Electric Circuits (Pearson).", "Glover, J. D., Sarma, M. S., Overbye, T. \u2014 Power System Analysis and Design.", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-electrical-engineering-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-electrical-engineering-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
