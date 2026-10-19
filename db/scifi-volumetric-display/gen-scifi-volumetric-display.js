(function(){'use strict';
/* JAH Volumetric Display Database generator - jahdb-scifi-volumetric-display-1.0.
   Property of Justin Addam Higgins (JAH).
   SPECULATIVE CONCEPT TECHNOLOGY: Signature-generated concept-tech for study,
   imagination, and design exploration. Not established real-world fact.
   Deterministic: same seed, same record. Seeds 1..N return the archive
   records; higher seeds generate boundless variants. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
var SLUG='scifi-volumetric-display';
var PREFIX='JAH-VOLUMETRICDISPLAY-';
var SHORT='Volumetric Display';
var FULLNAME='JAH Volumetric Display Database';
var TAGLINE='True 3D images in thin air.';
var GROUPS=['overview','model-v1','model-v2','model-v3','specifications','code-demos','applications','safety'];
var DISCLAIMER='Speculative concept technology. Signature-generated for study, imagination, and design exploration. Not established real-world fact; not instructions for building weapons or hazardous devices. Nothing herein is medical, legal, or engineering advice.';
var TECH={"name": "Volumetric Display", "specs": [{"p": "Capability index", "u": "/100", "v1": "35", "v2": "72", "v3": "97"}, {"p": "Efficiency", "u": "%", "v1": "42", "v2": "76", "v3": "95"}, {"p": "Reliability", "u": "%", "v1": "80", "v2": "96", "v3": "99.9"}, {"p": "Ease of use", "u": "/10", "v1": "3", "v2": "7", "v3": "10"}, {"p": "Cost index", "u": "/100", "v1": "85", "v2": "45", "v3": "12"}, {"p": "Safety index", "u": "/100", "v1": "60", "v2": "88", "v3": "99"}], "models": {"v1": "Mark I proves the principle: it works under lab conditions with expert operators and generous power.", "v2": "Mark II is the practical generation: reliable, efficient, and usable by trained professionals.", "v3": "Mark III is the mature form: superb capability, effortless operation, and safety engineered into every layer."}, "concept": "Volumetric Display is a speculative concept-technology: an imagined device for stories, design study, and inspiration. Signature concept-tech, not established fact.", "principle": "Concept technologies mature along a familiar arc: prove the principle, refine it for real use, then master it. The three models below trace that arc.", "note": "Volumetric displays render images in true three-dimensional space without headsets.", "apps": ["Science-fiction storytelling and worldbuilding", "Engineering design inspiration", "Education about speculative technology"], "safety": "Every speculative technology is studied with safety first: each model documents hazards, interlocks, and responsible-use guidelines.", "subsystems": ["Core effector", "Power supply", "Control system", "Safety interlocks", "User interface", "Maintenance access"]};
var BLUEPRINTS=[{"t": "Volumetric Display: Concept Definition", "g": "overview", "ladder": 1, "angle": "definition"}, {"t": "Volumetric Display: Principles and Idea Lineage", "g": "overview", "ladder": 1, "angle": "lineage"}, {"t": "Volumetric Display Mark 1: Model Card", "g": "model-v1", "ladder": 2, "angle": "model-card"}, {"t": "Volumetric Display Mark 1: Specification Sheet", "g": "model-v1", "ladder": 2, "angle": "spec-sheet"}, {"t": "Volumetric Display Mark 1: Demo Program", "g": "model-v1", "ladder": 2, "angle": "demo-program", "scenario": "Mark 1 demonstration run"}, {"t": "Volumetric Display Mark 1: Field Notes", "g": "model-v1", "ladder": 2, "angle": "field-notes"}, {"t": "Volumetric Display Mark 2: Model Card", "g": "model-v2", "ladder": 2, "angle": "model-card"}, {"t": "Volumetric Display Mark 2: Specification Sheet", "g": "model-v2", "ladder": 2, "angle": "spec-sheet"}, {"t": "Volumetric Display Mark 2: Demo Program", "g": "model-v2", "ladder": 2, "angle": "demo-program", "scenario": "Mark 2 demonstration run"}, {"t": "Volumetric Display Mark 2: Field Notes", "g": "model-v2", "ladder": 2, "angle": "field-notes"}, {"t": "Volumetric Display Mark 3: Model Card", "g": "model-v3", "ladder": 3, "angle": "model-card"}, {"t": "Volumetric Display Mark 3: Specification Sheet", "g": "model-v3", "ladder": 3, "angle": "spec-sheet"}, {"t": "Volumetric Display Mark 3: Demo Program", "g": "model-v3", "ladder": 3, "angle": "demo-program", "scenario": "Mark 3 demonstration run"}, {"t": "Volumetric Display Mark 3: Field Notes", "g": "model-v3", "ladder": 3, "angle": "field-notes"}, {"t": "Volumetric Display: Full Specification Sheet", "g": "specifications", "ladder": 2, "angle": "full-spec"}, {"t": "Volumetric Display: Subsystem Breakdown", "g": "specifications", "ladder": 2, "angle": "subsystem"}, {"t": "Volumetric Display: Performance Envelope", "g": "specifications", "ladder": 3, "angle": "envelope"}, {"t": "Volumetric Display: Interfaces and Compatibility", "g": "specifications", "ladder": 2, "angle": "interfaces"}, {"t": "Volumetric Display: Demo - Basic capability calculator", "g": "code-demos", "ladder": 2, "angle": "demo-scenario", "scenario": "Basic capability calculator"}, {"t": "Volumetric Display: Demo - Mark I vs II vs III comparison", "g": "code-demos", "ladder": 3, "angle": "demo-scenario", "scenario": "Mark I vs II vs III comparison"}, {"t": "Volumetric Display: Demo - Edge cases and limits", "g": "code-demos", "ladder": 2, "angle": "demo-scenario", "scenario": "Edge cases and limits"}, {"t": "Volumetric Display: Demo - Interactive playground", "g": "code-demos", "ladder": 3, "angle": "demo-scenario", "scenario": "Interactive playground"}, {"t": "Volumetric Display in Science-Fiction Storytelling And", "g": "applications", "ladder": 1, "angle": "application", "app": "Science-fiction storytelling and worldbuilding"}, {"t": "Volumetric Display in Engineering Design Inspiration", "g": "applications", "ladder": 2, "angle": "application", "app": "Engineering design inspiration"}, {"t": "Volumetric Display in Education About Speculative", "g": "applications", "ladder": 2, "angle": "application", "app": "Education about speculative technology"}, {"t": "Volumetric Display: Safety Engineering", "g": "safety", "ladder": 1, "angle": "safety"}, {"t": "Volumetric Display: Ethics and Governance", "g": "safety", "ladder": 2, "angle": "ethics"}, {"t": "Volumetric Display: Development Roadmap", "g": "safety", "ladder": 2, "angle": "roadmap"}];
var DEMOFN=function(tech, scenario){
var S=tech.specs, n=tech.name;
var L=[];
L.push('// '+n+' - specification comparison ('+scenario+')');
L.push('// Run with: node demo.js');
L.push("'use strict';");
L.push('var specs='+JSON.stringify(tech.specs)+';');
L.push('console.log("'+n+' - v1 vs v2 vs v3");');
L.push('console.log("==================================================");');
L.push('specs.forEach(function(s){');
L.push('  console.log(s.p+": Mark I "+s.v1+" "+s.u+" | Mark II "+s.v2+" "+s.u+" | Mark III "+s.v3+" "+s.u);');
L.push('});');
L.push('console.log("Each generation compounds: better on every axis, never a trade-off disguised as progress.");');
return L.join('\n');
};
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function pnum(v){var x=parseFloat(String(v).replace(/,/g,''));return isFinite(x)?x:null;}
function para(){return Array.prototype.slice.call(arguments).join('\n\n');}
function genOf(bp){
  if(bp.g==='model-v1')return 'v1';
  if(bp.g==='model-v2')return 'v2';
  if(bp.g==='model-v3')return 'v3';
  return null;
}
function ord(g){return g==='v1'?'first':g==='v2'?'second':'third';}
function specVals(T,g){return T.specs.map(function(s){return s.p+': '+s[g]+' '+s.u;}).join('; ');}
function gainSummary(T,from,to){
  var best=null,bestP='';
  T.specs.forEach(function(s){
    var a=pnum(s[from]),b=pnum(s[to]);
    if(a&&b&&a>0&&b>0){var r=b/a;if(r>1&&(!best||r>best)){best=r;bestP=s.p;}}
  });
  if(best)return 'up to '+best.toFixed(best<10?1:0)+'x improvement on '+bestP+' ('+from.toUpperCase()+' to '+to.toUpperCase()+')';
  return 'improved on every specification axis';
}
function descFor(bp,seed){
  var T=TECH,n=SHORT,g=genOf(bp);
  switch(bp.angle){
  case 'definition':return para(
    T.concept,
    T.note,
    'This database is the permanent archive for '+n+': its definition, three compounding model generations (Mark I, Mark II, Mark III - each better than the last), full specifications, runnable code demonstrations, applications, and safety framing. '+TAGLINE,
    DISCLAIMER);
  case 'lineage':return para(
    'Principles of the '+n+'. '+T.principle,
    'The idea lineage: early speculation imagined the effect; bench prototypes proved the principle; refinement generations compounded performance; the mature form in this archive represents the best understood version of the concept.',
    'How to read this database: start with the concept definition (ladder 1), study each Mark generation in order (ladder 2-3), run the code demonstrations, then review applications and safety.',
    DISCLAIMER);
  case 'model-card':{
    var prev=g==='v1'?null:(g==='v2'?'v1':'v2');
    return para(
      n+' Mark '+g.charAt(1)+' - the '+ord(g)+' compounding generation.',
      T.models[g],
      'Key specifications: '+specVals(T,g)+'.',
      prev?('Compounding gain over Mark '+prev.charAt(1)+': '+gainSummary(T,prev,g)+', with no regression on any axis.'):('The baseline generation. It proves the principle that Mark II and Mark III compound upon.'),
      DISCLAIMER);}
  case 'spec-sheet':{
    var rows=T.specs.map(function(s){return s.p+' ('+s.u+'): Mark I '+s.v1+' | Mark II '+s.v2+' | Mark III '+s.v3;});
    return para(
      n+' - '+g.toUpperCase()+' specification sheet.',
      'Full parameter table:\n'+rows.join('\n'),
      'Reading the table: every parameter improves or holds steady from Mark I to Mark III. That compounding - better on all axes at once - is the signature of a maturing concept generation.',
      DISCLAIMER);}
  case 'demo-program':
    return para(
      n+' Mark '+g.charAt(1)+' - runnable demonstration program.',
      'The program below simulates this generation using its specification values. It runs as-is with node: save it as demo.js and run "node demo.js".',
      'Scenario: '+bp.scenario+'. The simulation compares all three generations so the compounding improvement is visible in the numbers.',
      DISCLAIMER);
  case 'field-notes':
    return para(
      n+' Mark '+g.charAt(1)+' - simulated field notes (concept exercise).',
      'Trial 1: baseline performance matches the specification sheet within expected simulation tolerance. Trial 2: sustained operation confirms the headline parameters. Trial 3: edge-case handling reviewed against the safety interlocks.',
      'Engineer note: the compounding from the previous generation is most visible in sustained operation, where '+g.toUpperCase()+' holds its specification values under load that degraded earlier marks.',
      'These notes describe a simulated concept exercise, not a real device test. '+DISCLAIMER);
  case 'variant':
    return para(
      n+' '+g.toUpperCase()+' '+bp.variant+' - boundless concept variant.',
      T.models[g||'v3'],
      'This variant explores the same compounding generation adapted for a specialized role. All specification values derive from the '+ (g?g.toUpperCase():'Mark III') +' baseline, adjusted for the variant mission profile.',
      'Boundless variants are generated, validated concept studies - each one checked against the archive for drift before acceptance. '+DISCLAIMER);
  case 'full-spec':{
    var r2=T.specs.map(function(s){return s.p+' ('+s.u+'): '+s.v1+' / '+s.v2+' / '+s.v3;});
    return para(
      n+' - complete specification record.',
      T.concept,
      'Mark I: '+T.models.v1,
      'Mark II: '+T.models.v2,
      'Mark III: '+T.models.v3,
      'Parameter table (Mark I / Mark II / Mark III):\n'+r2.join('\n'),
      DISCLAIMER);}
  case 'subsystem':
    return para(
      n+' - subsystem breakdown.',
      T.subsystems.map(function(s,i){return (i+1)+'. '+s+': engineered to the '+n+' specification with generation-appropriate margins.';}).join('\n'),
      'Integration: subsystems connect through published interfaces so any generation of one subsystem works with any generation of the others.',
      DISCLAIMER);
  case 'envelope':
    return para(
      n+' - performance envelope.',
      'Nominal operation holds all specification values at their Mark III ratings. Peak operation reaches the best demonstrated values across the parameter table with reduced margins.',
      'Degraded operation: the design fails gracefully, shedding non-essential functions while preserving safety interlocks and core capability.',
      'Envelope limits are simulated concept values for design study. '+DISCLAIMER);
  case 'interfaces':
    return para(
      n+' - interfaces and compatibility.',
      'Power interface: standardized bus with generation-negotiated voltage and conditioning. Data interface: open telemetry schema shared across all three marks. Mechanical interface: common mounting geometry so generations are field-interchangeable.',
      'Compatibility promise: a Mark III subsystem plugs into a Mark I installation and negotiates down safely; a Mark I subsystem in a Mark III installation is carried at its own rated limits.',
      DISCLAIMER);
  case 'demo-scenario':
    return para(
      n+' - code demonstration: '+bp.scenario+'.',
      'The program below is runnable with node (save as demo.js, run "node demo.js"). It exercises the '+n+' specification values in the "'+bp.scenario+'" scenario and prints the results.',
      'Try varying the inputs: the simulation is parameterized so students can explore how each specification value shapes the outcome.',
      DISCLAIMER);
  case 'application':
    return para(
      n+' in '+bp.app.toLowerCase()+'.',
      'Applied here, the compounding generations matter directly: Mark I makes the application conceivable, Mark II makes it practical, and Mark III makes it routine.',
      'Deployment notes: start with the mature generation where available; specify interfaces so earlier generations can substitute during supply constraints.',
      DISCLAIMER);
  case 'safety':
    return para(
      n+' - safety engineering. '+T.safety,
      'Hazard analysis covers the full lifecycle: construction, operation, maintenance, and decommissioning. Each generation reduces residual risk while adding capability.',
      'Safety case: interlocks are independent of control systems, failures default to the safe state, and operators can always command a safe stop.',
      DISCLAIMER);
  case 'ethics':
    return para(
      n+' - ethics and governance (concept framework).',
      'Who decides deployment: the concept framework requires review by domain experts, affected communities, and independent safety boards before any real-world program begins.',
      'Consent, reversibility, and equitable access are designed in from Mark I - they are not retrofits. Dual-use potential is assessed for every subsystem.',
      'This is a speculative ethics framework for a fictional technology, offered for study and discussion. '+DISCLAIMER);
  case 'roadmap':
    return para(
      n+' - development roadmap (concept plan).',
      'Phase 1 (Mark I): prove the principle with instrumented prototypes and publish everything. Phase 2 (Mark II): refine to practical reliability with independent safety review. Phase 3 (Mark III): mature to routine operation with full lifecycle support.',
      'Each phase gates on the previous: no phase begins until the prior phase meets its safety and performance criteria in open review.',
      DISCLAIMER);
  default:
    return para(n+' - '+bp.t+'.',T.concept,DISCLAIMER);
  }
}
function buildRecord(bp,seed){
  var g=genOf(bp);
  var r={
    id:PREFIX+pad(seed),
    title:bp.t,t:bp.t,g:bp.g,ladder:bp.ladder,
    description:descFor(bp,seed),
    specs:{},models:{mark1:TECH.models.v1,mark2:TECH.models.v2,mark3:TECH.models.v3},
    src:'signature-generated',disclaimer:DISCLAIMER,last_verified:'2026-10-19'
  };
  TECH.specs.forEach(function(s){r.specs[s.p]={unit:s.u,mark1:s.v1,mark2:s.v2,mark3:s.v3};});
  if(bp.angle==='demo-program'||bp.angle==='demo-scenario'){
    r.program=DEMOFN(TECH,bp.scenario||('Mark '+(g?g.charAt(1):'III')+' demonstration'));
    r.run_hint='Save the program field as demo.js and run: node demo.js';
  }
  return r;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>=1&&seed<=BLUEPRINTS.length){
    var bp=JSON.parse(JSON.stringify(BLUEPRINTS[seed-1]));
    var g=opts.group&&GROUPS.indexOf(opts.group)>=0?opts.group:null;
    if(g)bp.g=g;
    return buildRecord(bp,seed);
  }
  var variants=['Arctic variant','Deep-space variant','Miniaturized variant','Heavy-duty variant','Stealth variant','Rapid-deployment variant','Long-endurance variant','High-precision variant'];
  var gens=['v1','v2','v3'];
  var gg=pick(rnd,gens);
  var bp2={t:SHORT+' Mark '+gg.charAt(1)+' '+pick(rnd,variants)+': concept study',g:pick(rnd,GROUPS),ladder:gg==='v3'?3:2,angle:'variant',variant:'boundless study'};
  return buildRecord(bp2,seed);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(GROUPS.indexOf(r.g)<0)e.push('group');
  if(typeof r.description!=='string'||r.description.length<300)e.push('description');
  if(r.src!=='signature-generated')e.push('src');
  if(typeof r.disclaimer!=='string'||!r.disclaimer.length)e.push('disclaimer');
  if(!(r.ladder>=1&&r.ladder<=3))e.push('ladder');
  if(r.program&&typeof r.program!=='string')e.push('program');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-scifi-volumetric-display-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:GROUPS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
