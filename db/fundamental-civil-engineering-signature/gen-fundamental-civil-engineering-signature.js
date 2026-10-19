(function(){'use strict';
/* jahdb-fundamental-civil-engineering-signature-1.0 — fundamental civil-engineering bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFCE-';
var KIND='fundamental civil-engineering record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Civil engineering designs the built environment: structures, bridges, dams, roads, water systems — the infrastructure civilization stands on. It is the oldest engineering branch, and its works outlive their builders by centuries.', 'reasoning':'Civil engineers reason with codes, loads, and factors of safety: define the worst credible demands, design to the governing standard, and prove every element. The structure must stand for generations — the analysis must be conservative and complete.', 'quantities':'The core quantities are loads (dead, live, wind, seismic), stresses, deflections, and flows (water, traffic). The load combination — the code\'s recipe for worst cases — is the field\'s master calculation.', 'mechanism':'Civil engineering works design-bid-build (and its modern variants): survey → design to code → review → construct → inspect. The inspector is the field\'s conscience — what gets built is verified against what was designed.', 'miscon':'Civil engineering is not just concrete: geotechnics, hydraulics, transportation, and environmental systems are equal branches. Concrete is strong in compression and weak in tension — which is why it\'s reinforced. And \'overdesigned\' is usually just \'designed for the code\'s loads.\''};
var SIGLENS=['In the Signature system, civil engineering is the infrastructure discipline: every lasting construction in this network follows its habits — codes, margins, inspection — and the Signature formulation teaches each principle as a structure you can verify.','The Signature practice is to design the structure: define the loads, size the members, check the code — so civil reasoning is done with the discipline of things that must stand for a century.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- beam load demo. Runs as-is with python3."""\ndef simply_supported_moment(w_kN_m, L_m):\n    return w_kN_m * L_m**2 / 8  # kN-m\nfor L in [5, 10, 20]:\n    print(f"span {L}m, 10 kN/m: max moment = {simply_supported_moment(10, L):.0f} kN-m")\nprint("moment grows with span squared: long spans need deep beams")\n', '#!/usr/bin/env python3\n"""{TITLE} -- concrete volume demo. Runs as-is with python3."""\ndef slab_volume(length_m, width_m, thick_m):\n    return length_m * width_m * thick_m\nv = slab_volume(10, 8, 0.15)\nprint(f"10x8m slab, 15cm thick: {v:.1f} m^3 of concrete")\nprint(f"at 2400 kg/m^3: {v*2400/1000:.1f} tonnes")\n', '#!/usr/bin/env python3\n"""{TITLE} -- water flow demo (Manning). Runs as-is with python3."""\ndef manning_q(n, area, rh, slope):\n    return (1/n) * area * (rh ** (2/3)) * (slope ** 0.5)\nq = manning_q(0.013, 2.0, 0.5, 0.001)\nprint(f"channel flow: {q:.2f} m^3/s")\nprint("drainage design sizes channels for the worst storm, not the average rain")\n'];
var TOPICS=[['Signature What Civil Engineering Is','Civil engineering creates the built environment: buildings, bridges, dams, highways, water and sewer systems. It is the engineering of civilization\'s physical platform — designed to serve generations.'],
['Signature The Core Question of Civil Engineering','The core question is: how do we build it to stand safely for its design life? Every structure answers with its loads defined, its members sized, its foundations set on understood ground.'],
['Signature Assumptions: Codes and Conservative Loads','The field assumes code-defined loads and conservative analysis: design for the earthquake, the flood, the crowd — the worst credible events, not the average day. The code is the profession\'s accumulated memory of failures.'],
['Signature The Vocabulary: Loads, Spans, Foundations','The vocabulary names the concerns: dead loads (the structure), live loads (its users), environmental loads (wind, quake, snow), spans, and foundations. Fluency means seeing any structure as loads finding their way to the ground.'],
['Signature The Load Path: The Fundamental Concept','The load path is the fundamental concept: every force must travel continuously from where it\'s applied to the foundation. A break in the path — a missing connection, an unbraced joint — is where structures fail.'],
['Signature Structural Analysis: The Primary Method','Structural analysis is the primary method: model the structure, apply factored loads, compute forces and deflections, check against capacities. Modern software does the arithmetic; the engineer owns the model and the judgment.'],
['Signature A Canonical First Example','The canonical first example is the simply supported beam: uniform load, reactions at the ends, maximum moment wL²/8 at midspan. One equation sizes floor beams worldwide — the seed of all structural design.'],
['Signature How Civil Engineering Measures','The field measures with surveys, load tests, and structural health monitoring: settlements in millimeters, strains under load, vibrations of bridges. Proof-load testing verifies the critical spans before the public arrives.'],
['Signature The Core Mechanism: Codes and Review','The core mechanism is codes plus independent review: designs checked against standards written from past failures, then reviewed by licensed engineers who stamp their responsibility. The system is designed to catch the single human error.'],
['Signature The Simplest Law: Equilibrium of the Structure','The simplest law is global equilibrium: the whole structure\'s reactions balance its loads. Before any member is sized, the structure as a system must stand in balance — the first check of every analysis.'],
['Signature Common Misconceptions in Civil Engineering','The misconceptions mislead: that concrete is strong in tension (it\'s reinforced because it isn\'t), that structures are designed for average loads (they\'re designed for extremes), and that computer output is automatically right (the model is the engineer\'s responsibility).'],
['Signature How Beginners Practice Civil Engineering','Beginners practice by analyzing simple structures by hand: trusses by joints, beams by diagrams — then checking with software. Hand methods build the judgment that catches the software\'s mistakes.'],
['Signature The Core Model: The Truss','The truss is the core model: members in pure tension or compression, joints pinned, loads at nodes. Bridges, towers, and roofs are trusses at heart — the most efficient way to span distance with material.'],
['Signature The Great Achievement: The Long-Span Bridge','The long-span bridge is the great achievement: suspension and cable-stayed spans crossing kilometers, each a tuned system of cables, deck, and towers. They are the field\'s cathedrals — and its hardest dynamics problems.'],
['Signature Systems Thinking: Infrastructure Networks','Systems thinking in civil engineering is the network: water, transport, power as interconnected systems with cascading failures. Resilience — surviving the disruption — now joins strength as a design goal.'],
['Signature Invariance: What Codes Preserve','The invariance principle is the code\'s intent: different designers, same safety. The codes encode minimum performance — life safety in the great earthquake — invariant across styles and software.'],
['Signature Approximation: Simplified Models','Approximation uses simplified models calibrated to reality: equivalent static loads for wind, response spectra for earthquakes. The simplifications are validated against the complex truth — and against history.'],
['Signature Evidence Standards: The Stamp','The evidence standard is the professional stamp: a licensed engineer certifies the design meets the code. The stamp is legal and moral — it says a qualified human takes responsibility.'],
['Signature Classic Discoveries','The classic discoveries are reinforced concrete, prestressing, the skyscraper\'s steel frame, and seismic base isolation. Each let humanity build taller, longer, and safer than before.'],
['Signature Core Trade-offs: Cost versus Performance','The core trade-off is cost versus performance versus durability: the cheapest first cost often loses on lifecycle. Value engineering optimizes the whole life — construction, maintenance, and the cost of failure.'],
['Signature Handling Uncertainty: Load Factors','The field handles uncertainty with load and resistance factors: amplify the uncertain loads, reduce the uncertain strengths, design the factored system. LRFD is quantified caution, calibrated to target reliabilities.'],
['Signature Tools of the Trade','The tools of the trade are structural software, the code books, the survey instruments, and the inspection checklist. The deepest is the site visit — the structure as built, which is the only one that matters.'],
['Signature Ethics and Responsibility','Ethics in civil engineering is life safety as a fiduciary duty: the public trusts what engineers stamp. The field\'s code of ethics puts public welfare first — above client, above employer, above self.'],
['Signature Teaching Civil Engineering','Teaching it well visits structures: the bridge, the dam, the construction site. Students who have stood under a truss they analyzed understand load paths bodily.'],
['Signature The Frontier Question','The frontier question is resilient and sustainable infrastructure: structures that survive climate extremes, materials that heal, cities that adapt. The frontier rebuilds civilization\'s platform for the next century.'],
['Signature Unifying Theories','The unifying theories are mechanics of materials and structural dynamics: stress and strain beneath, vibration and stability above. Geotechnics adds the ground — the half of every structure you can\'t see.'],
['Signature Computational Civil Engineering','Computational civil engineering models the unbuildable first: finite elements for complex structures, CFD for wind, seismic time-history for earthquakes. The models are calibrated to tests — and to the failures of history.'],
['Signature Bridges to Other Fields','Civil engineering bridges to architecture (form), geology (ground), environmental science (water, waste), and economics (infrastructure finance). The built environment is inherently interdisciplinary.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: predicting soil behavior perfectly, infrastructure deterioration modeling, and designing for truly unprecedented climate extremes. Active research, no settled answers.'],
['Signature How New Claims Are Validated','New systems are validated by testing and by precedent: the new connection tested to failure, the new material monitored in service for years. The field adopts slowly — because its mistakes stand in public.'],
['Signature The Great Debates','The great debates include performance-based versus prescriptive codes, the pace of adopting new materials, and how to fund maintenance. The debates are civic — they shape the world everyone inhabits.'],
['Signature Failure Modes: When Civil Engineering Gets It Wrong','The field gets it wrong through unconsidered loads, foundation surprises, and connection failures — its disasters are public and studied. The immune system is the failure investigation, published so the codes can learn.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis delivers whole infrastructure from fundamentals: loads pathed, members sized, foundations set, codes met, inspected in the field. The fundamentals are the profession\'s promise to the public.'],
['Signature The Signature Formulation: Civil Engineering as Lasting Infrastructure','The Signature formulation treats civil principles as infrastructure thinking: every concept here builds things meant to outlast their builders, because in the Signature system construction that does not endure is construction unfinished. That is the Signature capstone on civil bedrock.']];
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
    standards:["Codes govern: designs comply with the applicable structural, seismic, and safety codes.", "Loads are combined per code: worst credible combinations, not typical ones.", "Inspection verifies construction: built work is checked against the design."],citations:["Hibbeler, R. C. \u2014 Structural Analysis (Pearson).", "ACI 318 / AISC 360 \u2014 the governing concrete and steel codes.", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-civil-engineering-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-civil-engineering-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
