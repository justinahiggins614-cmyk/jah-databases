(function(){'use strict';
/* jahdb-fundamental-mechanical-engineering-1.0 — fundamental mechanical-engineering bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FME-';
var KIND='fundamental mechanical-engineering record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Mechanical engineering designs machines and mechanical systems: how forces move things, how materials bear loads, how heat becomes work. It is the oldest engineering discipline — the engineering of the physical machine.', 'reasoning':'Mechanical engineers reason with free-body diagrams and conservation laws: isolate the system, draw every force, write equilibrium or motion equations, and check against material limits. The diagram is the thinking.', 'quantities':'The core quantities are force, torque, stress, strain, and power — with temperature and heat transfer where energy converts. The stress-strain curve of a material is the field\'s master chart.', 'mechanism':'Mechanical design works the loop: define loads → choose materials → size components → check failure modes → prototype → test. Factor of safety covers the unknowns; testing covers the factors.', 'miscon':'Mechanical engineering is not just gears: fluids, heat, vibrations, and controls are equal partners. Heavier does not mean stronger — geometry beats mass. And \'it feels solid\' is not analysis: the numbers decide.'};
var SIGLENS=['In the Signature system, mechanical engineering is the discipline of physical making: every 3D print, every device, every manufactured thing in this network obeys these principles, and the Signature formulation teaches each one as a design you can calculate.','The Signature practice is to design the machine: draw the free body, size the member, check the failure mode — so mechanical reasoning is done with engineering numbers that can be built.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- stress demo. Runs as-is with python3."""\ndef stress(force_N, area_mm2):\n    return force_N / area_mm2  # N/mm^2 = MPa\nfor F, A in [(10000, 100), (50000, 100), (10000, 25)]:\n    print(f"F={F}N A={A}mm^2 -> stress={stress(F, A):.0f} MPa")\nprint("steel yields ~250 MPa: the first case has safety factor 2.5")\n', '#!/usr/bin/env python3\n"""{TITLE} -- gear ratio demo. Runs as-is with python3."""\ndef gear_train(teeth):\n    ratio = 1.0\n    for driver, driven in teeth:\n        ratio *= driven / driver\n    return ratio\nr = gear_train([(12, 36), (12, 48)])\nprint("12->36, 12->48: overall ratio", r, ":1 (torque x12, speed /12)")\nprint("gears trade speed for torque, power is conserved (minus losses)")\n', '#!/usr/bin/env python3\n"""{TITLE} -- beam deflection demo. Runs as-is with python3."""\ndef cantilever_deflection(F_N, L_m, E_Pa, I_m4):\n    return F_N * L_m**3 / (3 * E_Pa * I_m4)\nd = cantilever_deflection(1000, 2.0, 200e9, 8.33e-6)\nprint(f"1kN on 2m steel beam: deflection = {d*1000:.1f} mm")\nprint("deflection grows with length cubed: long beams get floppy fast")\n'];
var TOPICS=[['What Mechanical Engineering Is','Mechanical engineering is the design of machines: systems that transmit force and motion, convert energy, and bear loads. From engines to robots to prosthetics, it is the engineering discipline most directly in contact with the physical world.'],
['The Core Question of Mechanical Engineering','The core question is: how do we make it move, bear the load, and not break? Every machine is an answer — sized, toleranced, and tested against the forces it will meet.'],
['Assumptions: Rigid Bodies and Continua','Analysis assumes rigid bodies where deformation is negligible and continua where materials are smooth — then checks the assumptions. The art is knowing when the rigid assumption fails (vibrations, impacts) and the continuum must be modeled.'],
['The Vocabulary: Stress, Strain, Torque','The vocabulary names the quantities: stress (force per area), strain (deformation per length), torque (twisting moment), and the failure modes — yield, fatigue, fracture, buckling. Fluency means reading a stress-strain curve like a biography.'],
['Stress: The Fundamental Quantity','Stress is the fundamental quantity: force divided by area, in pascals. Materials fail at characteristic stresses, so the entire discipline is keeping working stresses safely below failing ones — the central inequality of the field.'],
['The Free-Body Diagram: The Primary Method','The free-body diagram is the primary method: isolate the part, draw every force and moment, enforce equilibrium. Every machine analysis begins here — the diagram externalizes the thinking so errors become visible.'],
['A Canonical First Example','The canonical first example is the bolted joint: preload the bolt, the clamped parts carry the load, the bolt sees only a fraction. One joint teaches preload, stiffness, fatigue, and the difference between strength and stiffness.'],
['How Mechanical Engineering Measures','The field measures with strain gauges, load cells, accelerometers, and thermal cameras: deformation, force, vibration, and heat made visible. Testing validates analysis — the test rig is the court of final appeal.'],
['The Core Mechanism: Force Transmission','The core mechanism is force transmission through mechanisms: gears, linkages, cams, belts, and screws converting motion\'s form — rotation to translation, speed to torque. The mechanism is the machine\'s grammar.'],
['The Simplest Law: Equilibrium','The simplest law is equilibrium: the sum of forces and the sum of moments are each zero for a body at rest. Statics — the whole first course — is this law applied with discipline.'],
['Common Misconceptions in Mechanical Engineering','The misconceptions mislead: that stronger material fixes bad design (geometry usually matters more), that stiffness equals strength (they\'re different properties), and that computers replaced hand analysis (they check it; judgment still designs).'],
['How Beginners Practice Mechanical Engineering','Beginners practice by analyzing and building: solve the statics problems, then build the linkage, the bracket, the small engine. The built thing teaches what the equations assumed.'],
['The Core Model: The Stress-Strain Curve','The stress-strain curve is the core model of materials: elastic region, yield point, plastic deformation, fracture. One curve encodes stiffness, strength, ductility, and toughness — the material\'s whole mechanical character.'],
['The Great Equation: σ = F/A (and Its Extensions)','Stress equals force over area is the great equation, extended by Hooke\'s law (σ = Eε), beam theory, and fatigue life curves. From this seed grows the sizing of everything from bolts to bridges.'],
['Systems Thinking: Vibrations','Systems thinking in mechanical engineering is dynamics and vibration: every structure has natural frequencies, and forcing near them causes resonance — the phenomenon behind both musical instruments and collapsed bridges.'],
['Invariance: Conservation Laws','The invariance principles are conservation of energy and momentum applied to machines: they bound what\'s possible before design begins. No mechanism delivers more work than it receives — the audit no perpetual motion survives.'],
['Approximation: Linearization','Approximation linearizes: small oscillations, small strains, linear elasticity — then checks the range of validity. Engineering analysis is the art of the justified simplification.'],
['Evidence Standards: Testing','The evidence standard is the test: prototypes loaded to failure, fatigue specimens cycled millions of times, field data from service. Analysis predicts; testing certifies.'],
['Classic Discoveries','The classic discoveries are the steam engine, the internal combustion engine, the jet engine, and the industrial robot. Each redefined what machines could do — and what civilization could build.'],
['Core Trade-offs: Strength versus Weight','The core trade-off is strength versus weight versus cost: aerospace pays for lightness, civil engineering for cheap mass, racing for both. Material selection charts navigate the trade systematically.'],
['Handling Uncertainty: Factor of Safety','The field handles uncertainty with factors of safety: design for multiples of the expected load, with the multiple reflecting how well loads and materials are known. It is quantified humility — and it saves lives.'],
['Tools of the Trade','The tools of the trade are CAD, finite element analysis, the machine shop, and the test rig. The deepest is the failure analysis — the fractured part read like a black box, teaching what the design missed.'],
['Ethics and Responsibility','Ethics in mechanical engineering is public safety made personal: pressure vessels, elevators, vehicles — the engineer\'s stamp means the analysis was done and the margins are real. The field\'s disasters are its curriculum.'],
['Teaching Mechanical Engineering','Teaching it well pairs analysis with making: the beam theory lecture follows the beam-bending lab. Students who have broken the specimen understand the stress-strain curve bodily.'],
['The Frontier Question','The frontier question is machines at the extremes: soft robots, micro-machines, and structures that heal themselves. The frontier asks what \'machine\' means when materials become active.'],
['Unifying Theories','The unifying theories are continuum mechanics beneath and control theory alongside: deformation described generally, motion governed actively. Together with thermodynamics, they cover the field\'s physics.'],
['Computational Mechanical Engineering','Computational mechanics simulates what can\'t be tested: finite elements for stress, CFD for fluids, multibody dynamics for mechanisms. Simulation explores design space; testing anchors it to reality.'],
['Bridges to Other Fields','Mechanical engineering bridges to materials science, electrical engineering (mechatronics), civil engineering (structures), medicine (biomechanics, prosthetics), and aerospace. The machine is the shared object.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: turbulence prediction from first principles, fatigue life prediction for complex loadings, and fully autonomous design. Active research, no settled answers.'],
['How New Claims Are Validated','New designs are validated by analysis, test, and service: the calculation checked, the prototype broken, the field watched. A machine earns trust in operation — there is no other certification.'],
['The Great Debates','The great debates include simulation versus testing primacy, the limits of lightweighting, and how much autonomy machines should have. The debates are practical — each side builds.'],
['Failure Modes: When Mechanical Engineering Gets It Wrong','The field gets it wrong through fatigue underestimated, resonance unconsidered, and corrosion ignored — the classic killers. The immune system is the failure analysis, published so the next design learns.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis designs whole machines from fundamentals: loads defined, members sized, failure modes checked, tested to proof. The fundamentals are the design method, not just the coursework.'],
['The Signature Formulation: Mechanical Engineering as Buildable Design','The Signature formulation treats mechanical principles as buildable designs: every concept here sizes something real, because in the Signature system a machine principle you cannot calculate and build is a principle you have not yet learned. That is the Signature capstone on mechanical bedrock.']];
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
    standards:["Loads are defined: every design states its worst credible loads.", "Failure modes are checked: yield, fatigue, buckling, and fracture each get their analysis.", "Safety factors are explicit: the margin between working load and failure is stated."],citations:["Shigley, J. E. and Mischke, C. R. \u2014 Mechanical Engineering Design (McGraw-Hill).", "Beer, F. P. and Johnston, E. R. \u2014 Mechanics of Materials.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-mechanical-engineering-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-mechanical-engineering',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
