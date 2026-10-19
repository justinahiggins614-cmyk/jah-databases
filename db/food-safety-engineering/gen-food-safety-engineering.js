(function(){'use strict';
/* JAH Food Safety Engineering Database generator — jahdb-food-safety-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FSE-";
var FIELDS=["hazards", "HACCP", "thermal processing", "allergens", "sanitation", "traceability"];
var TOPICS=[
    {t: "Biological Hazards", b: "Salmonella, Listeria, E. coli, norovirus: the pathogens behind recalls \u2014 growth conditions and kill parameters for each."},
    {t: "Chemical Hazards", b: "Mycotoxins, heavy metals, pesticide residues, migrants from packaging: chemistry's contribution to the hazard list."},
    {t: "Physical Hazards", b: "Metal, glass, plastic fragments: detection (metal detectors, X-ray) and prevention at the source."},
    {t: "HACCP: The System", b: "Hazard analysis, critical control points, limits, monitoring, corrective actions, verification, records \u2014 the seven principles."},
    {t: "Thermal Processing", b: "Pasteurization, sterilization, retort: D-values, z-values, and F\u2080 calculations proving the process kills."},
    {t: "Refrigeration and Cold Chain", b: "Temperature control from farm to fork: time-temperature abuse is the most common failure mode."},
    {t: "Allergen Management", b: "The major allergens, labeling law (FALCPA/FALMA), cleaning validation, and dedicated-line economics."},
    {t: "Sanitation Chemistry", b: "Detergents, sanitizers (chlorine, quat, peracetic acid), CIP systems: the chemistry of clean food-contact surfaces."},
    {t: "Environmental Monitoring", b: "Listeria hunting in drains and equipment: seek-and-destroy programs for ready-to-eat plants."},
    {t: "Traceability", b: "Lot tracking from ingredient to consumer: recall speed is measured in hours, enabled by records."},
    {t: "Food Defense", b: "Intentional adulteration: vulnerability assessments and mitigation for deliberate threats."},
    {t: "Regulations", b: "FSMA preventive controls, FDA Food Code, EU 178/2002: the legal frameworks plants operate inside."}
];
var PRINCIPLES=[
    {n: "Hazards are analyzed, not assumed", e: "", s: "Biological, chemical, physical, allergen: systematic hazard analysis precedes every control."},
    {n: "Validation proves the kill step", e: "", s: "Thermal processes must demonstrate log reductions with data: inoculated-pack studies, not assumptions."},
    {n: "Allergens are managed by separation", e: "", s: "Cleaning validation and scheduling segregate allergens: shared lines need proof, not hope."}
];
var USES=["Writing HACCP plans", "Validating thermal processes", "Managing allergen programs", "Investigating contamination"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Food Safety Engineering"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Food Safety Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-food-safety-engineering-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-food-safety-engineering-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("food-safety-engineering",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
