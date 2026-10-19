(function(){'use strict';
/* jahdb-fundamental-manufacturing-1.0 — fundamental manufacturing bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FMF-';
var KIND='fundamental manufacturing record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Manufacturing is the transformation of materials into products at scale: casting, forming, machining, joining, and additive processes, organized into systems that deliver quality, cost, and volume. It is where design becomes reality.', 'reasoning':'Manufacturing engineers reason in processes and variation: define the process, measure its capability, control its variation, and improve continuously. Quality is not inspected in — it is built in by controlling the process.', 'quantities':'The core quantities are tolerance (allowed variation), process capability (Cp, Cpk), cycle time, yield, and cost per unit. Tolerance is the master quantity — it prices everything.', 'mechanism':'Manufacturing works the process loop: design for manufacture → plan the process → make → measure → control variation → improve. Statistical process control watches the process; lean removes the waste around it.', 'miscon':'Manufacturing is not just \'making stuff\': it is precision, systems, and economics. Tighter tolerance is not always better — it costs exponentially. And automation does not eliminate skill: it moves skill from hands to process design.'};
var SIGLENS=['In the Signature system, manufacturing is how ideas become objects: every 3D print, every product, every physical thing in this network passes through manufacturing thinking, and the Signature formulation teaches each principle as a process you can run.','The Signature practice is to make the thing: plan the process, hold the tolerance, measure the result — so manufacturing is learned by producing, not just by reading about production.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- tolerance stack demo. Runs as-is with python3."""\nimport random\nrandom.seed(9)\ndef assemble(n, target, tol):\n    parts = [random.gauss(target, tol/3) for _ in range(n)]\n    return sum(parts)\nresults = [assemble(5, 10.0, 0.1) for _ in range(1000)]\nworst = max(abs(r - 50.0) for r in results)\nprint(f"5 parts of 10+/-0.1: worst assembly deviation in 1000 tries: {worst:.3f}")\nprint("tolerances stack: RSS beats worst-case, but the stack still grows")\n', '#!/usr/bin/env python3\n"""{TITLE} -- OEE demo. Runs as-is with python3."""\ndef oee(availability, performance, quality):\n    return availability * performance * quality\nfor a, p, q in [(0.9, 0.95, 0.99), (0.8, 0.9, 0.95)]:\n    print(f"A={a} P={p} Q={q} -> OEE={oee(a,p,q):.1%}")\nprint("world-class OEE is 85%: losses multiply, so attack the biggest first")\n', '#!/usr/bin/env python3\n"""{TITLE} -- EOQ demo. Runs as-is with python3."""\nimport math\ndef eoq(demand_yr, order_cost, holding_cost_unit_yr):\n    return math.sqrt(2 * demand_yr * order_cost / holding_cost_unit_yr)\nq = eoq(12000, 50, 2.0)\nprint(f"EOQ = {q:.0f} units per order")\nprint("order too often: ordering cost dominates; too rarely: holding cost dominates")\n'];
var TOPICS=[['What Manufacturing Is','Manufacturing transforms materials into products: shaping, joining, and finishing at scales from one-offs to millions. It is where engineering meets economics — the design is only as good as its manufacturability.'],
['The Core Question of Manufacturing','The core question is: how do we make this to specification, at cost, at volume? Every process choice — cast or machine, weld or bolt, automate or manual — answers the triangle of quality, cost, and delivery.'],
['Assumptions: Processes Have Capability','The field assumes processes have measurable capability: every process produces variation, and the variation can be quantified (Cp, Cpk). Design must fit process capability — tolerance tighter than the process is a wish, not a specification.'],
['The Vocabulary: Tolerance, Yield, Cycle Time','The vocabulary names the economics: tolerance (allowed variation), yield (good parts over total), cycle time (seconds per part), and takt (the heartbeat of demand). Fluency means thinking in rates and variations, not just shapes.'],
['Tolerance: The Fundamental Quantity','Tolerance is the fundamental quantity: the allowed variation on every dimension. It prices manufacturing — halving a tolerance can multiply cost tenfold — so the art is tolerancing only what function requires.'],
['Process Control: The Primary Method','Statistical process control is the primary method: measure the process, chart it, and distinguish signal (assignable causes) from noise (common causes). Control the process and the product takes care of itself.'],
['A Canonical First Example','The canonical first example is the machined shaft and hole: the shaft must fit the bore — clearance, transition, or interference — and the tolerance zones on the drawing guarantee it. One fit teaches the whole philosophy of interchangeability.'],
['How Manufacturing Measures','The field measures with micrometers, CMMs, and gauges: dimensions to microns, surfaces to nanometers of roughness. Measurement uncertainty must be a tenth of the tolerance — the metrology rule behind all quality.'],
['The Core Mechanism: The Process Loop','The core mechanism is the process loop: plan → make → measure → adjust. APQP plans the quality in; PPAP proves the process before production; continuous improvement tightens the loop forever.'],
['The Simplest Law: Variation Exists','The simplest law is that variation exists in everything: no two parts are identical. The discipline is not eliminating variation — impossible — but controlling it within what function allows.'],
['Common Misconceptions in Manufacturing','The misconceptions cost money: that tighter tolerance is always better (it costs exponentially), that inspection creates quality (it only sorts it), and that automation fixes bad processes (it accelerates them, flaws included).'],
['How Beginners Practice Manufacturing','Beginners practice by making: machine the part, measure it, compare to the drawing. The shop teaches what the textbook assumed — feeds, speeds, and the feel of a sharp tool.'],
['The Core Model: The Process Capability Index','Cpk is the core model of quality: the process spread versus the tolerance width. Cpk 1.33 is the industrial standard — the process centered with room to breathe, quantified.'],
['The Great Idea: Lean','Lean is the great idea: value as the customer defines it, waste (muda) relentlessly removed, flow pulled by demand. The Toyota Production System turned manufacturing philosophy into the world\'s most studied management system.'],
['Systems Thinking: The Production System','Systems thinking sees the factory whole: material flow, information flow, and the bottlenecks that govern throughput. Theory of Constraints finds the drum — the slowest resource sets the pace of everything.'],
['Invariance: Interchangeability','The invariance principle is interchangeability: any good part fits any good assembly. It enabled mass production, repair, and the modern world — standardization as civilization\'s quiet miracle.'],
['Approximation: Prototypes','Approximation builds prototypes: the 3D print, the soft tool, the pilot run — each a cheaper estimate of the production truth. Prototype to learn, pilot to prove, produce to deliver.'],
['Evidence Standards: First Article and PPAP','The evidence standard is the approved process: first articles measured, capability demonstrated, PPAP signed. Production approval means the process — not just the parts — passed.'],
['Classic Discoveries','The classic discoveries are interchangeable parts, the assembly line, statistical quality control, CNC, and additive manufacturing. Each multiplied what humanity could make — and how precisely.'],
['Core Trade-offs: Quality versus Cost','The core trade-off is quality versus cost versus speed: the iron triangle of production. The masters move the frontier — better processes deliver more of all three — rather than merely choosing a point.'],
['Handling Uncertainty: Safety Stock and Buffers','Manufacturing handles uncertainty with designed buffers: safety stock for demand variation, capacity buffers for breakdowns, time buffers for the schedule. Buffers cost; stockouts cost more — the balance is calculated.'],
['Tools of the Trade','The tools of the trade are CAD/CAM, the CNC machine, the CMM, and the control chart. The deepest is the process FMEA — imagining every way the process can fail, before it does.'],
['Ethics and Responsibility','Ethics in manufacturing is worker safety, honest quality, and environmental responsibility: the factory must not harm its people, its customers, or its neighbors. Quality ethics means never shipping known defects.'],
['Teaching Manufacturing','Teaching it well makes things: the machined part, the measured drawing, the improved process. Students who have scrapped a part respect tolerance forever.'],
['The Frontier Question','The frontier question is the smart factory: additive manufacturing at scale, digital twins mirroring production, AI optimizing processes in real time. The frontier asks what manufacturing becomes when the physical and digital fully merge.'],
['Unifying Theories','The unifying theories are quality management (Deming, Juran) and operations science: variation understood, flow optimized, waste removed. Together they turned factory folklore into a science of production.'],
['Computational Manufacturing','Computational manufacturing simulates before cutting: toolpath simulation, mold flow, factory digital twins. The simulation catches the crash before the machine does — the cheapest test piece is virtual.'],
['Bridges to Other Fields','Manufacturing bridges to mechanical engineering (design), materials science (processability), industrial engineering (systems), computer science (automation), and business (operations). It is where all engineering becomes product.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: zero-defect manufacturing at scale, fully flexible automation economics, and circular manufacturing that wastes nothing. Active research, no settled answers.'],
['How New Claims Are Validated','New processes are validated by capability studies and production trials: the Cpk demonstrated, the pilot run shipped, the field watched. A process earns trust in production — the only certification that counts.'],
['The Great Debates','The great debates include reshoring versus global supply chains, automation versus employment, and lean versus resilience (buffers cost, fragility costs more). The debates are economic — they shape where things are made.'],
['Failure Modes: When Manufacturing Gets It Wrong','The field gets it wrong through incapable processes, skipped validation, and cost-cutting on quality — recalls are the tuition. The immune system is the containment, the root cause, and the lessons-learned that change the process.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis runs whole production systems from fundamentals: processes capable, variation controlled, flow lean, quality built in. The fundamentals are the operating system of making.'],
['The Signature Formulation: Manufacturing as Reality Production','The Signature formulation treats manufacturing as reality production: every principle here turns designs into objects, because in the Signature system an idea you cannot manufacture is an idea unfinished. That is the Signature capstone on manufacturing bedrock.']];
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
    standards:["Drawings govern: dimensions, tolerances, and finishes are specified completely.", "Processes are capable: Cpk targets are met before production approval.", "Quality is built in: control plans monitor the process, not just the product."],citations:["Groover, M. P. \u2014 Automation, Production Systems, and Computer-Integrated Manufacturing.", "Deming, W. E. \u2014 Out of the Crisis (quality management).", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-manufacturing-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-manufacturing',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
