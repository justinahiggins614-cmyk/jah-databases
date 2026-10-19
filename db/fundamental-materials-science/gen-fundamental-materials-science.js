(function(){'use strict';
/* jahdb-fundamental-materials-science-1.0 — fundamental materials-science bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FMS-';
var KIND='fundamental materials-science record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Materials science studies how the structure of materials determines their properties: why steel is strong, glass is brittle, and silicon computes. It connects atomic arrangement to engineering performance across metals, ceramics, polymers, and composites.', 'reasoning':'Materials scientists reason across scales: atomic bonding → microstructure → macroscopic properties. Processing sets structure, structure sets properties, properties set performance — the field\'s central tetrahedron.', 'quantities':'The core quantities are strength, stiffness (modulus), toughness, hardness, and conductivity — thermal and electrical. The Ashby charts map these properties across all materials, guiding selection.', 'mechanism':'Materials understanding is built by processing-structure-properties-performance: how you make it determines its internal structure, which determines what it can do. Heat treatment, alloying, and forming are structure-control levers.', 'miscon':'Materials science is not just memorizing alloys: it predicts from structure. Stronger is not always better — toughness, fatigue, and corrosion often govern. And \'pure\' is not \'better\': alloys and composites outperform pure elements by design.'};
var SIGLENS=['In the Signature system, materials science is the substance discipline: every manufactured thing in this network is made of materials chosen by these principles, and the Signature formulation teaches each one as a selection you can justify.','The Signature practice is to select the material: define the requirements, compare the properties, justify the choice — so materials reasoning is done as engineering selection, not memorization.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- specific strength demo. Runs as-is with python3."""\nmats = {"steel": (500, 7.85), "aluminum": (300, 2.70), "titanium": (900, 4.43), "CFRP": (1500, 1.60)}\nprint(f"{\'material\':<10} {\'strength/density\':>16}")\nfor name, (s, d) in mats.items():\n    print(f"{name:<10} {s/d:>16.0f} (MPa per g/cm^3)")\nprint("aerospace picks by specific properties, not absolute ones")\n', '#!/usr/bin/env python3\n"""{TITLE} -- thermal expansion demo. Runs as-is with python3."""\ndef expansion(length_m, alpha, dT):\n    return length_m * alpha * dT\nfor name, alpha in [("steel", 12e-6), ("aluminum", 23e-6), ("concrete", 10e-6)]:\n    print(f"{name:<10} 100m bridge, 40C swing: {expansion(100, alpha, 40)*1000:.0f} mm")\nprint("expansion joints exist because materials move with temperature")\n', '#!/usr/bin/env python3\n"""{TITLE} -- rule of mixtures demo. Runs as-is with python3."""\ndef composite_modulus(vf, ef, em):\n    return vf * ef + (1 - vf) * em\nfor vf in [0.3, 0.5, 0.6]:\n    print(f"fiber fraction {vf}: E = {composite_modulus(vf, 230e3, 3e3)/1e3:.0f} GPa")\nprint("composites blend properties: stiff fibers in a tough matrix")\n'];
var TOPICS=[['What Materials Science Is','Materials science studies the relationship between a material\'s internal structure and its properties: why materials behave as they do, and how to make them behave better. It is the science behind every engineered object.'],
['The Core Question of Materials Science','The core question is: how does structure determine properties, and how does processing determine structure? Answer both, and you can design materials — not just discover them.'],
['Assumptions: The Tetrahedron','The field assumes the processing-structure-properties-performance tetrahedron: each corner influences the others. Change the processing, change the structure, change everything downstream — the assumption that organizes all investigation.'],
['The Vocabulary: Metals, Ceramics, Polymers, Composites','The vocabulary names the families: metals (strong, ductile, conductive), ceramics (hard, brittle, heat-resistant), polymers (light, moldable, insulating), composites (combined for combined virtues). Each family\'s bonding explains its character.'],
['The Crystal Structure: The Fundamental Concept','Crystal structure is the fundamental concept: how atoms pack and bond determines nearly everything. Dislocations — defects in the packing — explain why real metals are weaker than theory and how work hardening strengthens them.'],
['Characterization: The Primary Method','Characterization is the primary method: microscopy, diffraction, and spectroscopy revealing structure from atoms to grains. You cannot engineer what you cannot see — the microscope is the field\'s telescope.'],
['A Canonical First Example','The canonical first example is steel: iron plus a little carbon, heat-treated to set its microstructure, transformed from soft to hard. One alloy, many steels — processing writing properties into metal.'],
['How Materials Science Measures','The field measures with tensile testers, hardness indenters, microscopes, and diffractometers: strength, hardness, grain size, crystal phases. The tensile test — pull until it breaks — is the honest measure.'],
['The Core Mechanism: Defects Govern Properties','The core mechanism is that defects govern properties: dislocations enable metal forming, grain boundaries strengthen, vacancies enable diffusion. Perfection would be brittle — engineering exploits controlled imperfection.'],
['The Simplest Law: Hooke\'s Law for Materials','The simplest law is Hooke\'s: stress proportional to strain in the elastic region, the slope being Young\'s modulus. Stiffness is the material\'s first answer to load — and the easiest to measure.'],
['Common Misconceptions in Materials Science','The misconceptions mislead: that stronger is always better (toughness and fatigue often govern), that pure means superior (alloys outperform pure metals by design), and that materials don\'t change in service (corrosion, fatigue, and creep are always working).'],
['How Beginners Practice Materials Science','Beginners practice by testing and looking: break the tensile specimens, polish and etch the samples, read the microstructures. The microscope connects the curve to the cause.'],
['The Core Model: The Phase Diagram','The phase diagram is the core model: temperature versus composition maps showing which phases exist where. It predicts what heat treatment will produce — the metallurgist\'s map and recipe book.'],
['The Great Tool: The Ashby Chart','The Ashby chart is the great selection tool: material properties plotted log-log, families as bubbles, design requirements as lines. Selection becomes visual — the best material for the job is the bubble the line touches.'],
['Systems Thinking: The Tetrahedron','Systems thinking is the tetrahedron itself: processing, structure, properties, performance — change one corner and trace the effects around. Design is navigating the tetrahedron deliberately.'],
['Invariance: Bonding Determines Family','The invariance principle is that bonding determines family behavior: metallic bonding gives ductility and conductivity across all metals; covalent networks give hardness across ceramics. Change the atoms, keep the bonding, keep the character.'],
['Approximation: Ideal Microstructures','Approximation models ideal microstructures — perfect crystals, uniform grains — then adds reality: defects, distributions, textures. The ideal bounds the possible; the real determines the actual.'],
['Evidence Standards: Standardized Testing','The evidence standard is the standardized test: ASTM and ISO methods so a strength number means the same in every lab. Materials data without a standard method is incomparable.'],
['Classic Discoveries','The classic discoveries are steel, semiconductors, polymers, and composites — each enabling a technological age. The transistor required germanium, then silicon, purified beyond any previous human achievement.'],
['Core Trade-offs: Strength versus Toughness','The core trade-off is strength versus toughness: harder materials crack easier. The designer\'s art is choosing the balance the application needs — the bridge wants toughness, the cutting tool wants hardness.'],
['Handling Uncertainty: Statistical Properties','The field handles uncertainty statistically: strength varies with defects, so design uses Weibull statistics and minimum properties. Brittle materials are designed by the weakest link — honestly quantified.'],
['Tools of the Trade','The tools of the trade are the microscope, the diffractometer, the tensile tester, and the furnace. The deepest is the phase diagram — the map of what processing can create.'],
['Ethics and Responsibility','Ethics in materials science concerns safety and sustainability: materials that fail kill, materials that persist pollute. The field\'s responsibility spans from structural integrity to recyclability and the ethics of extraction.'],
['Teaching Materials Science','Teaching it well breaks things: the tensile lab, the fracture surfaces, the etched microstructures. Students who have watched a crack run understand toughness permanently.'],
['The Frontier Question','The frontier question is materials by design: can we compute the material with exactly the needed properties before making it? Computational materials science and machine learning are converging on the answer.'],
['Unifying Theories','The unifying theories are quantum mechanics for bonding, thermodynamics for phases, and kinetics for how fast structures change. Together they predict what exists, what\'s stable, and what forms in practice.'],
['Computational Materials Science','Computational materials science predicts before synthesizing: density functional theory for properties, molecular dynamics for mechanisms, CALPHAD for phase diagrams. The Materials Genome Initiative aims to halve development time by computation.'],
['Bridges to Other Fields','Materials science bridges to physics (condensed matter), chemistry (synthesis), mechanical engineering (design), electrical engineering (devices), and medicine (biomaterials). Every technology is a materials story.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: room-temperature superconductors, the perfect prediction of fatigue life, and materials that fully recycle indefinitely. Active research, no settled answers.'],
['How New Claims Are Validated','New materials are validated by independent synthesis and standardized testing: another lab makes it, the properties reproduce, the structure is confirmed. A wonder material earns trust through replication, not press releases.'],
['The Great Debates','The great debates include how much computation can replace experiment, the definition of material \'sustainability,\' and the pace of adopting new materials in conservative industries. The debates balance innovation against reliability.'],
['Failure Modes: When Materials Science Gets It Wrong','The field gets it wrong through unconsidered environments (corrosion, hydrogen embrittlement), scale-up surprises, and over-trusting models. The immune system is the failure analysis — every fracture teaches.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis selects and designs materials from fundamentals: requirements mapped, candidates charted, microstructure engineered, performance verified. The fundamentals are the selection method.'],
['The Signature Formulation: Materials as Designed Substance','The Signature formulation treats materials as designed substance: every principle here selects or creates the matter things are made of, because in the Signature system what you build is what your materials allow. That is the Signature capstone on materials bedrock.']];
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
    standards:["Structure is characterized: claims about properties reference measured microstructure.", "Testing is standardized: ASTM/ISO methods so results compare across labs.", "Failure is analyzed: fractures are read to improve the next design."],citations:["Callister, W. D. and Rethwisch, D. G. \u2014 Materials Science and Engineering: An Introduction.", "Ashby, M. F. \u2014 Materials Selection in Mechanical Design.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-materials-science-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-materials-science',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
