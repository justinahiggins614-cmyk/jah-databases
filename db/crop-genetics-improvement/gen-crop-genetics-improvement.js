(function(){'use strict';
/* JAH Crop Genetics Improvement Database generator — jahdb-crop-genetics-improvement-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGI-";
var FIELDS=["breeding methods", "marker-assisted selection", "hybrid vigor", "disease resistance", "abiotic stress", "biotech traits"];
var TOPICS=[
    {t: "How Breeding Works", b: "Cross, select, stabilize: pedigree, bulk, and single-seed-descent methods move traits into elite backgrounds over generations."},
    {t: "Hybrid Vigor", b: "F1 hybrids outyield parents in corn, rice, vegetables: heterosis exploited through male-sterile and inbred-line systems."},
    {t: "Heritability", b: "The fraction of variation that's genetic sets selection response: high-heritability traits (maturity) respond fast, low ones (yield) slowly."},
    {t: "Marker-Assisted Selection", b: "DNA markers tag desired alleles: select seedlings in the lab instead of waiting for field phenotypes \u2014 years saved."},
    {t: "Genomic Selection", b: "Genome-wide markers predict breeding values: dairy-cattle-proven math now accelerating corn, wheat, and rice."},
    {t: "Disease Resistance Genes", b: "R-genes recognize pathogens; pyramids of multiple genes slow the boom-and-bust of resistance breakdown."},
    {t: "Drought and Heat Tolerance", b: "Root architecture, osmotic adjustment, stay-green: the physiological traits breeders stack for climate resilience."},
    {t: "Quality Traits", b: "Protein, oil, milling, and cooking quality: end-use traits that decide market acceptance beyond the farm gate."},
    {t: "Biotech Traits", b: "Bt insect resistance, herbicide tolerance: single-gene transformations with global adoption and ongoing stewardship debates."},
    {t: "Gene Editing (CRISPR)", b: "Targeted edits without foreign DNA: accelerating what breeding does, with evolving regulatory treatment worldwide."},
    {t: "Seed Systems", b: "Breeder \u2192 foundation \u2192 certified seed: the multiplication chain that delivers genetics to farmers' fields."},
    {t: "Regional Variety Trials", b: "Multi-location testing proves which varieties win where: the data behind every seed recommendation."}
];
var PRINCIPLES=[
    {n: "Yield is the final exam", e: "", s: "All traits serve yield stability: disease resistance and drought tolerance are yield insurance, not ornaments."},
    {n: "Local adaptation wins", e: "", s: "Varieties selected in the target environment beat global champions: G\u00d7E interaction is the breeder's reality."},
    {n: "Diversity is the raw material", e: "", s: "Narrow germplasm stalls progress: genebanks and wild relatives are the reserves improvement draws on."}
];
var USES=["Selecting regional wheat varieties", "Breeding disease-resistant rice", "Planning hybrid seed production", "Evaluating biotech traits"];
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
    id:id, t:tp.t, g:field, name:"Crop Genetics Improvement"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Crop Genetics Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-crop-genetics-improvement-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-crop-genetics-improvement-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("crop-genetics-improvement",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
