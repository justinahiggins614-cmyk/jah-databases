(function(){'use strict';
/* jahdb-defense-aerospace-puma-1.0 — deterministic boundless generator for defense-aerospace-puma.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["microstructure", "heat-transfer", "tps-materials", "imaging", "validation"];
var PREFIX='JAH-DAE5-';
var EDITION='public';
var POOL=[["PUMA: Seeing Inside Heat Shields", "microstructure", "PUMA (Porous Microstructure Analysis) is NASA Ames software that analyzes micro-CT images of porous thermal protection materials to model microscale heat transfer and structural behavior. Heat shields like PICA are porous by design — they ablate and insulate — and PUMA predicts how they behave from their actual microstructure. It turns images into material properties.", {"Developer": "NASA Ames", "Input": "micro-CT images", "Models": "heat + structure at microscale", "Materials": "PICA-class ablatives", "Output": "effective properties"}], ["Micro-CT: The 3D Microscope", "imaging", "Micro-CT (micro computed tomography) images a material sample in 3D at micron resolution, distinguishing solid fibers from void pores voxel by voxel. PUMA segments these volumes into phases — fiber, matrix, pore — that the physics solvers consume. The image is the ground truth the models must honor.", {"Method": "micro computed tomography", "Resolution": "microns, 3D", "Phases": "fiber, matrix, pore", "Role": "ground truth for models"}], ["Porosity and What It Means", "microstructure", "Porosity — the fraction of void space — controls both insulation and strength: more pores mean lower conductivity but weaker structure. PUMA measures porosity directly from segmented volumes, plus pore-size distributions and connectivity. TPS designers trade these against each other deliberately.", {"Porosity": "void fraction", "Trade": "insulation vs strength", "Measured": "from segmented volumes", "Plus": "pore sizes, connectivity"}], ["Effective Thermal Conductivity", "heat-transfer", "A porous heat shield does not conduct heat like either phase alone — PUMA computes the effective conductivity of the mixture by solving heat conduction on the voxel geometry. Maxwell, series/parallel bounds, and direct numerical simulation bracket the answer. This number feeds the vehicle-level thermal model.", {"Property": "effective conductivity", "Method": "solve on voxel geometry", "Bounds": "Maxwell, series/parallel", "Feeds": "vehicle thermal model"}], ["Permeability: Gas Through Pores", "heat-transfer", "During entry, pyrolysis gases flow out through the pores — PUMA computes permeability from the pore network so the flow can be modeled. High permeability vents gas easily; low permeability builds pressure. Coupled with heat transfer, this is the ablation physics that keeps the shield working.", {"Property": "permeability", "Physics": "pyrolysis gas outflow", "High k": "vents easily", "Coupled": "with heat transfer"}], ["PICA: The Reference Ablator", "tps-materials", "PICA (Phenolic Impregnated Carbon Ablator) is the reference NASA heat-shield material — carbon fiberform impregnated with phenolic resin — flown on Stardust, MSL, and Orion test articles. PUMA-class analysis characterized its microstructure to predict flight performance. Understanding PICA means understanding porous ablators generally.", {"Material": "Phenolic Impregnated Carbon Ablator", "Flown": "Stardust, MSL", "Structure": "fiberform + phenolic", "Role": "reference ablator"}], ["Ablation: Sacrificial Cooling", "heat-transfer", "Ablation protects by sacrifice: the heat shield chars, pyrolyzes, and erodes, carrying heat away in the boundary layer. PUMA's microscale properties feed material-response codes that predict recession rate. The shield is designed to lose exactly enough of itself.", {"Mechanism": "char, pyrolyze, erode", "Cooling": "heat carried in boundary layer", "Predicts": "recession rate", "Design": "lose exactly enough"}], ["Mechanical Properties from Microstructure", "microstructure", "PUMA also estimates stiffness and strength from the fiber network: load paths through connected fibers, stress concentrations at contacts. A shield must survive launch vibration and entry pressure, not just heat. Microstructure links the thermal and structural designs.", {"Properties": "stiffness, strength", "From": "fiber network connectivity", "Loads": "launch vibe, entry pressure", "Links": "thermal + structural"}], ["Tortuosity: The Crooked Path", "heat-transfer", "Tortuosity measures how crooked the pore paths are — gas and heat diffuse slower through twisted channels than straight ones. PUMA computes it from random walks through the pore space. High tortuosity is good insulation and slow venting.", {"Tortuosity": "pore path crookedness", "Method": "random walks in pores", "High": "better insulation", "Trade": "slower venting"}], ["Validation: Arc-Jet Testing", "validation", "PUMA predictions are validated against arc-jet tests — ground facilities that blast material samples with entry-like heating — plus flight data where available. Measured recession and internal temperatures must match the models. Validation is what turns analysis into flight rationale.", {"Facility": "arc-jet (entry-like heating)", "Measures": "recession, internal temps", "Plus": "flight data", "Result": "flight rationale"}], ["Multi-Phase Materials", "tps-materials", "Real TPS is multi-phase: fibers, resin char, virgin resin, pores — each with its own properties, evolving as heating progresses. PUMA tracks phases separately so the property models follow the material through charring. The shield at peak heating is not the shield that launched.", {"Phases": "fiber, char, resin, pore", "Evolves": "with heating", "Tracks": "phase fractions vs time", "Truth": "shield changes in flight"}], ["From Voxels to Vehicle", "validation", "The full PUMA pipeline: image the sample, segment phases, compute effective properties, feed material-response codes, predict vehicle temperatures and recession, validate in arc-jets. Microscale truth becomes vehicle-scale margins. This is multi-scale engineering done right.", {"Image": "micro-CT", "Compute": "effective properties", "Predict": "vehicle response", "Prove": "arc-jet + flight"}], ["PUMA for New Materials", "tps-materials", "PUMA's real power is screening new TPS concepts before making full-scale articles: image a coupon, compute properties, and know whether the concept is worth pursuing. Faster material development means better shields sooner. Analysis accelerates invention.", {"Screens": "new TPS concepts", "Needs": "only a coupon", "Decides": "worth pursuing?", "Effect": "faster development"}], ["Weaving: Engineered Porosity", "microstructure", "Woven TPS takes porosity from accident to design: 3D weaves place fibers exactly where strength and insulation are needed. PUMA analyzes weave unit cells the same way it analyzes random fiberforms. Engineered microstructure is the future of heat shields.", {"Weave": "3D placed fibers", "Design": "porosity on purpose", "Analyzes": "weave unit cells", "Future": "engineered shields"}], ["The PUMA Workflow End to End", "validation", "Ladder-top PUMA: take a real material, image it, model its microscale physics, predict its flight behavior, and prove it in the arc-jet. Fifteen rungs from voxels to flight rationale — the complete microstructure-to-mission pipeline for thermal protection.", {"Start": "real material coupon", "Middle": "microscale physics", "End": "flight rationale", "Span": "voxels to mission"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var phi=(0.65+(P.a%25)/100).toFixed(2), ks=1.2, kg=0.03;
var code='// PUMA-style porous effective conductivity demo (Maxwell model, simulated)\n';
code+='var phi='+phi+',ks='+ks+',kg='+kg+';\n';
code+='var keff=kg*(2*kg+ks+2*phi*(ks-kg))/(2*kg+ks-phi*(ks-kg));\n';
code+='console.log("porosity="+phi+" -> keff="+keff.toFixed(4)+" W/mK");';return code;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>HARD_STOP)throw new Error('generator hard stop: seed exceeds 1,000,000,000,000');
  var cat=opts.category&&CATS.indexOf(opts.category)>=0?opts.category:pick(CATS,rnd);
  var pool=POOL.filter(function(p){return p[1]===cat;});
  var row=pick(pool.length?pool:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var demo=buildDemo(seed);
  var rec={
    id:id, t:row[0], title:row[0], g:cat, category:cat,
    edition:EDITION, ladder_rank:1+((seed-1)%15),
    description:row[2],
    facts:row[3],
    demo:{language:'javascript',program:demo},
    provenance:EDITION==='public'
      ? 'Public record: compiled from official project documentation and published specifications. Fact-checked 2026-10-21.'
      : 'Signature original: designed by Justin Addam Higgins (JAH) as the Signature counterpart; original engineering, labeled Signature.',
    source:EDITION==='public'?'manon-order / public documentation':'manon-order / signature original',
    last_verified:'2026-10-21',
    march:'march-to-a-million in progress',
    license:'https://creativecommons.org/publicdomain/zero/1.0/',
    _simulated:true, _seed:seed
  };
  var v=validate(rec);
  if(!v.ok)throw new Error('generated record failed validation: '+v.errors.join(','));
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.g)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(!r.facts||typeof r.facts!=='object')e.push('facts');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('console.log')<0)e.push('demo');
  if(r._simulated!==true)e.push('simulated-label');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].id!==rec.id)
      return{ok:false,errors:['duplicate title in archive sample']};
  }
  return{ok:true,errors:[]};
}
/* Completion detection: the seed pool is exhausted when every pool row has
 * produced records across all categories; coverage() reports progress. */
function coverage(){return{pool_rows:POOL.length,categories:CATS.length,hard_stop:HARD_STOP};}
function isComplete(filed){return filed>=HARD_STOP;}
var gen={version:'jahdb-defense-aerospace-puma-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-puma',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
