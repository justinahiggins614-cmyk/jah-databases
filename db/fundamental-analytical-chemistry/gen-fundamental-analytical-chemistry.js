(function(){'use strict';
/* JAH Fundamentals of Analytical Chemistry Database generator — jahdb-fundamental-analytical-chemistry-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AC-";
var FIELDS=["sampling", "statistics", "titrimetry", "spectroscopy", "chromatography", "electroanalysis"];
var TOPICS=[
    {t: "The Analytical Process", b: "Define the problem, sample representatively, prepare, measure, validate: analysis fails most often at sampling, not at the instrument."},
    {t: "Sampling: The Critical Step", b: "A measurement is only as good as its sample: heterogeneity demands proper increments, and the sampling variance usually dominates."},
    {t: "Statistics of Measurement", b: "Mean, standard deviation, confidence intervals, t-tests: quantifying uncertainty is what separates analysis from guessing."},
    {t: "Calibration Strategies", b: "External standards, standard additions, and internal standards each defeat different matrix effects \u2014 choose by the interference."},
    {t: "Titrimetry", b: "Stoichiometric reactions to a visible or potentiometric endpoint: still the most accurate routine method for many analytes."},
    {t: "Gravimetry", b: "Weighing a pure precipitate: slow, but a primary method needing no calibration standards."},
    {t: "Atomic Spectroscopy", b: "Flame AA, ICP-OES, and ICP-MS atomize samples to count elements down to parts-per-trillion \u2014 the metals workhorses."},
    {t: "Molecular Spectroscopy", b: "UV-Vis, IR, and fluorescence identify and quantify molecules by their light absorption and emission fingerprints."},
    {t: "Chromatography: Separation First", b: "GC and HPLC separate mixtures so detectors see one compound at a time \u2014 resolution, not sensitivity, is usually the limit."},
    {t: "Mass Spectrometry", b: "Ionize, separate by mass-to-charge, detect: MS identifies unknowns and quantifies traces across chemistry, forensics, and pharma."},
    {t: "Electroanalytical Methods", b: "Potentiometry (pH electrodes), voltammetry, and coulometry measure redox-active species with simple, rugged instruments."},
    {t: "Quality Assurance", b: "Blanks, duplicates, spikes, and control charts prove data are valid: QA is the documented conscience of the laboratory."}
];
var PRINCIPLES=[
    {n: "Beer-Lambert law", e: "A = \u03b5\u00b7b\u00b7c", s: "Absorbance is proportional to concentration \u2014 the quantitative basis of spectrophotometry."},
    {n: "Calibration", e: "signal = m\u00b7c + b", s: "Standards of known concentration convert instrument response into quantity."},
    {n: "Detection limit", e: "LOD = 3\u00b7s_blank/slope", s: "The smallest distinguishable signal is three blank standard deviations above noise."}
];
var USES=["Testing drinking-water safety", "Assaying pharmaceutical purity", "Monitoring industrial emissions", "Analyzing forensic evidence"];
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
    id:id, t:tp.t, g:field, name:"Analytical Chemistry"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Analytical Chemistry demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-analytical-chemistry-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-analytical-chemistry-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-analytical-chemistry",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
