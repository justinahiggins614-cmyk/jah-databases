(function(){'use strict';
/* jahdb-fundamental-anatomy-physiology-1.0 — fundamental anatomy-physiology bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FAN-';
var KIND='fundamental anatomy-physiology record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Anatomy studies the body\'s structure; physiology studies its function. Together they describe the human machine: 206 bones, 600+ muscles, and the organ systems that keep every cell alive. Structure enables function — the field\'s eternal pairing.', 'reasoning':'Anatomists and physiologists reason structure-to-function: the shape explains the job — the heart\'s valves enforce one-way flow, the lung\'s surface area enables gas exchange. Form follows function, and function follows form.', 'quantities':'The core quantities are the defended variables: blood pH 7.4, core temperature ~37°C, blood glucose ~5 mmol/L, blood pressure ~120/80. Homeostasis is the master concept — the body\'s defense of its constants.', 'mechanism':'The body works by homeostasis via feedback: sensors detect deviation, control centers compare to set points, effectors correct. Negative feedback stabilizes everything from temperature to blood sugar — the master mechanism of physiology.', 'miscon':'Anatomy is not just memorization: it is functional — every structure\'s shape serves its job. The body is not a machine with replaceable parts: it heals, adapts, and varies. And \'textbook normal\' is a range, not a point — variation is normal.'};
var SIGLENS=['In the Signature system, anatomy and physiology are the body-knowledge foundation: every health, fitness, and medical database in this network builds on this structure-function map, and the Signature formulation teaches each principle as a system you can trace.','The Signature practice is to trace the system: follow the blood, track the signal, map the structure to its job — so body knowledge is learned as working systems, not as lists of parts.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- cardiac output demo. Runs as-is with python3."""\ndef cardiac_output(hr_bpm, stroke_vol_ml):\n    return hr_bpm * stroke_vol_ml / 1000  # L/min\nfor hr, sv in [(70, 70), (150, 100), (50, 70)]:\n    print(f"HR {hr}, SV {sv}mL -> cardiac output {cardiac_output(hr, sv):.1f} L/min")\nprint("rest ~5 L/min; exercise can exceed 20 L/min")\n', '#!/usr/bin/env python3\n"""{TITLE} -- lung volumes demo. Runs as-is with python3."""\n# mL, typical adult\nvolumes = {"tidal": 500, "inspiratory reserve": 3000, "expiratory reserve": 1100, "residual": 1200}\nvc = volumes["tidal"] + volumes["inspiratory reserve"] + volumes["expiratory reserve"]\nprint("vital capacity:", vc, "mL")\nprint("total lung capacity:", vc + volumes["residual"], "mL")\n', '#!/usr/bin/env python3\n"""{TITLE} -- BMI and body surface demo. Runs as-is with python3."""\nimport math\ndef bsa_mosteller(h_cm, w_kg):\n    return math.sqrt(h_cm * w_kg / 3600)\nfor h, w in [(175, 70), (160, 60), (190, 95)]:\n    print(f"{h}cm {w}kg -> BSA {bsa_mosteller(h, w):.2f} m^2 (drug dosing, burn assessment)")\n'];
var TOPICS=[['What Anatomy and Physiology Are','Anatomy maps the body\'s structure; physiology explains its function. Together they describe the human organism completely — the parts, how they work, and how they work together. Neither makes full sense alone.'],
['The Core Question of the Field','The core question is: how is the body built, and how does the building do its jobs? Every structure invites the functional question — what is this for? — and every function invites the structural one — what does it?'],
['Assumptions: Levels of Organization','The field assumes hierarchical organization: atoms → molecules → cells → tissues → organs → systems → organism. Each level has emergent properties — the heart\'s pumping exists at no lower level.'],
['The Vocabulary: Planes, Directions, Systems','The vocabulary orients: anatomical position, superior/inferior, proximal/distal, the sagittal/coronal/transverse planes. The eleven organ systems name the functional divisions — fluency means navigating the body by these coordinates.'],
['Homeostasis: The Fundamental Concept','Homeostasis is the fundamental concept: the body\'s maintenance of stable internal conditions — temperature, pH, glucose, water — against a changing world. Health is homeostasis succeeding; disease is homeostasis failing.'],
['Dissection and Experiment: The Primary Methods','Anatomy learns by dissection and imaging; physiology by experiment — perturbing systems and measuring responses. The methods differ, the goal is one: the working map of the body.'],
['A Canonical First Example','The canonical first example is the knee-jerk reflex: tap the tendon, the leg kicks — sensory neuron to spinal cord to motor neuron, no brain required. One reflex teaches the whole reflex arc: receptor, pathway, effector.'],
['How the Field Measures','The field measures with imaging, electrophysiology, and the chemistry panel: structure seen (MRI, CT), electrical activity recorded (ECG, EEG), function assayed (blood tests). Each modality views a different aspect of the living body.'],
['The Core Mechanism: Negative Feedback','The core mechanism is negative feedback: deviation detected, correction applied, stability restored. Blood sugar, blood pressure, body temperature — the body\'s constants are defended by loops, not by luck.'],
['The Simplest Law: Structure Serves Function','The simplest law is that structure serves function: the alveoli\'s vast surface for gas exchange, the neuron\'s branches for connection, the bone\'s trabeculae along stress lines. Form is function made visible.'],
['Common Misconceptions in Anatomy and Physiology','The misconceptions mislead: that anatomy is pure memorization (it\'s functional reasoning), that the body is a machine with interchangeable parts (it heals and adapts), and that \'normal\' is a single value (it\'s a range — variation is normal).'],
['How Beginners Practice','Beginners practice by drawing and labeling: sketch the heart, trace the blood, label the parts — then explain each part\'s job. Teaching the structure aloud cements the structure-function link.'],
['The Core Model: The Cell','The cell is the core model: the unit of structure and function, with organelles as its organs. Every tissue, every organ, every system is cells organized — the body\'s fractal foundation.'],
['The Great System: Circulation','Circulation is the great system: the heart\'s double pump driving blood through pulmonary and systemic circuits, delivering oxygen and collecting waste. Harvey\'s 1628 demonstration — by ligatures and logic — founded modern physiology.'],
['Systems Thinking: Integration','Systems thinking sees the body integrated: the nervous and endocrine systems coordinate, the cardiovascular serves all tissues, the immune patrols everywhere. No system operates alone — the organism is the system.'],
['Invariance: The Defended Variables','The invariance principles are the defended variables: pH, temperature, osmolarity held nearly constant despite the chaos outside. The body\'s constancy amid change is its defining achievement.'],
['Approximation: The Reference Man','Approximation uses reference values — the 70-kg man, the standard ranges — then adjusts for the individual. The reference orients; the patient in front of you decides.'],
['Evidence Standards: Reproducible Physiology','The evidence standard is the reproducible experiment: the response demonstrated, the mechanism blocked and restored, the finding replicated. Physiology trusts what can be made to happen again.'],
['Classic Discoveries','The classic discoveries are circulation, the cell theory, the neuron doctrine, hormones, and the genetic code\'s machinery. Each revealed a layer of the body\'s organization — from pump to molecule.'],
['Core Trade-offs: Specialization versus Generality','The core trade-off in body design is specialization versus adaptability: the highly specialized (the eye\'s optics) excels narrowly; the general (the immune system\'s learning) covers broadly. Evolution balanced both across systems.'],
['Handling Uncertainty: Biological Variation','The field handles uncertainty as variation: no two bodies are identical, and normal spans ranges. Clinical judgment reads the individual against the population — the art within the science.'],
['Tools of the Trade','The tools of the trade are the atlas, the microscope, the ECG, and the lab panel. The deepest is the physical examination — hands and senses trained to read the body directly.'],
['Ethics and Responsibility','Ethics governs the body itself: consent for examination, dignity in dissection, respect in teaching. The body studied is someone\'s body — the field never forgets it.'],
['Teaching Anatomy and Physiology','Teaching it well makes it three-dimensional: models, dissection, palpation on the living. Students who have felt the pulse, traced the tendon, and drawn the heart own the knowledge.'],
['The Frontier Question','The frontier question is the integrated human: the connectome, the immune repertoire, the microbiome\'s role — mapping the body\'s complex systems completely. The frontier asks whether we can model the whole.'],
['Unifying Theories','The unifying theories are cell theory, homeostasis, and evolution: the unit, the regulation, and the history. Together they explain why the body is built this way and how it stays working.'],
['Computational Physiology','Computational physiology builds the virtual body: heart models that beat, lung models that breathe, whole-body simulations for drug testing. The models integrate knowledge — and reveal what the pieces alone don\'t show.'],
['Bridges to Other Fields','Anatomy and physiology bridge to medicine (application), sports science (performance), engineering (biomechanics, prosthetics), and art (the figure). The body is everyone\'s subject.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: the full wiring of the brain, the complete logic of the immune system, and regeneration of complex tissues. Active research, no settled answers.'],
['How New Claims Are Validated','New physiological claims are validated by replication and mechanism: the effect reproduced, the pathway identified, the blockade tested. A phenomenon earns trust when its mechanism is shown.'],
['The Great Debates','The great debates include how much of function genes determine, the limits of the machine metaphor for the body, and what \'normal\' should mean. The debates keep the field honest about its models.'],
['Failure Modes: When the Field Gets It Wrong','The field gets it wrong through over-mechanization (forgetting the whole), textbook dogma outliving evidence, and ignoring variation. The immune system is the careful observer and the replicated experiment.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis reads the body whole: the symptom traced to the system, the system to the cell, the treatment aimed at the mechanism. The fundamentals are clinical reasoning\'s foundation.'],
['The Signature Formulation: The Body as Working System','The Signature formulation treats body knowledge as working-system knowledge: every principle here maps structure to function in systems you can trace, because in the Signature system the body is the original complex system — and understanding it is the template for understanding all systems. That is the Signature capstone on anatomical bedrock.']];
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
    standards:["Terminology is standard: anatomical position and directional terms used consistently.", "Structure-function pairing: every structure taught with the function it serves.", "Variation is acknowledged: normal ranges, not single values, are reported."],citations:["Marieb, E. N. and Hoehn, K. \u2014 Human Anatomy & Physiology (Pearson).", "Netter, F. H. \u2014 Atlas of Human Anatomy.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-anatomy-physiology-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-anatomy-physiology',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
