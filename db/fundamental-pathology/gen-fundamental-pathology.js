(function(){'use strict';
/* JAH Fundamentals of Pathology Database generator — jahdb-fundamental-pathology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PAT-";
var FIELDS=["cell injury", "inflammation", "healing", "neoplasia", "genetic disease", "diagnostic methods"];
var TOPICS=[
    {t: "What Pathology Studies", b: "Pathology is disease's science: causes (etiology), mechanisms (pathogenesis), structural changes, and clinical consequences."},
    {t: "Cell Injury: Reversible vs Irreversible", b: "Swelling and fatty change can reverse; membrane failure and mitochondrial collapse cannot \u2014 the point of no return."},
    {t: "Necrosis vs Apoptosis", b: "Necrosis is messy accidental death (inflammation follows); apoptosis is tidy programmed suicide \u2014 morphology tells them apart."},
    {t: "Acute Inflammation", b: "Vasodilation, permeability, neutrophil emigration: the vascular-exudative response that walls off and destroys invaders."},
    {t: "Chronic Inflammation", b: "Macrophages, lymphocytes, fibrosis: when acute resolution fails, granulomas and scarring remodel tissue permanently."},
    {t: "Tissue Repair", b: "Regeneration restores (liver), scarring patches (heart): healing outcome depends on the tissue's proliferative capacity."},
    {t: "Hemodynamic Disorders", b: "Thrombosis, embolism, infarction, shock: when blood misbehaves, Virchow's triad (stasis, injury, hypercoagulability) explains why."},
    {t: "Neoplasia: Benign vs Malignant", b: "Benign tumors stay put; malignant ones invade and metastasize \u2014 anaplasia, invasion, and spread define cancer."},
    {t: "Carcinogenesis", b: "Multistep genetic damage (oncogenes on, suppressors off) plus epigenetics and chronic inflammation build malignancy over years."},
    {t: "Grading and Staging", b: "Grade describes differentiation, stage describes spread (TNM): together they predict prognosis and guide therapy."},
    {t: "Genetic and Developmental Disease", b: "Single-gene disorders (sickle cell), chromosomal (Down), and multifactorial diseases each follow distinct patterns."},
    {t: "How Diagnoses Are Made", b: "Biopsy, cytology, immunohistochemistry, and molecular tests: the pathologist's verdict rests on tissue evidence."}
];
var PRINCIPLES=[
    {n: "Virchow's dictum", e: "omnis cellula e cellula", s: "All cells come from cells \u2014 disease is disordered cellular life, not mystical imbalance."},
    {n: "Inflammation cardinal signs", e: "rubor, tumor, calor, dolor", s: "Redness, swelling, heat, pain: Celsus described the vascular response 2,000 years ago."},
    {n: "Hallmarks of cancer", e: "sustained proliferation, evading suppressors, ...", s: "Hanahan and Weinberg's framework organizes malignancy's acquired capabilities."}
];
var USES=["Diagnosing cancers from biopsies", "Staging tumors for treatment", "Investigating cause of death", "Screening with Pap smears"];
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
    id:id, t:tp.t, g:field, name:"Pathology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Pathology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-pathology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-pathology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-pathology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
