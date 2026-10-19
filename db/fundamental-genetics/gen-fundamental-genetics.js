(function(){'use strict';
/* JAH Fundamentals of Genetics Database generator — jahdb-fundamental-genetics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GEN-";
var FIELDS=["Mendelian genetics", "DNA structure", "gene expression", "mutation", "population genetics", "genetic technology"];
var TOPICS=[
    {t: "Mendel's Laws", b: "Segregation and independent assortment from pea crosses: the statistical rules of inheritance, rediscovered in 1900."},
    {t: "Chromosomes Carry Genes", b: "Sutton and Boveri's insight plus Morgan's fruit flies: genes sit in linear order on chromosomes \u2014 linkage maps followed."},
    {t: "DNA Double Helix", b: "Watson-Crick base pairing (A-T, G-C) explains both copying and information storage in one elegant structure."},
    {t: "Replication", b: "Semi-conservative copying with proofreading polymerases: ~1 error per 10\u2079 bases, the fidelity life depends on."},
    {t: "Transcription and the Genetic Code", b: "RNA polymerase copies genes; triplet codons translate to amino acids \u2014 a code nearly universal across life."},
    {t: "Gene Regulation", b: "Operons, transcription factors, enhancers, and epigenetic marks decide which genes fire, where, and when."},
    {t: "Mutation: Source of Variation", b: "Point mutations, indels, and chromosomal rearrangements supply raw material; most are neutral or harmful, a few beneficial."},
    {t: "Modes of Inheritance", b: "Autosomal dominant/recessive, X-linked, and mitochondrial patterns predict family risk \u2014 the counselor's toolkit."},
    {t: "Pedigree Analysis", b: "Reading family trees reveals inheritance mode and recurrence risk for genetic counseling."},
    {t: "Population Genetics", b: "Hardy-Weinberg equilibrium, selection coefficients, and drift equations describe evolution at the allele level."},
    {t: "Quantitative Traits", b: "Height, yield, and IQ-like traits follow polygenic models: many small-effect loci plus environment."},
    {t: "Genetic Technologies", b: "PCR amplifies, sequencing reads, CRISPR edits, and GWAS associates \u2014 the toolkit remaking medicine and agriculture."}
];
var PRINCIPLES=[
    {n: "Segregation", e: "1:2:1 genotype ratio", s: "Each parent contributes one of two alleles at random \u2014 Mendel's first law."},
    {n: "Hardy-Weinberg", e: "p\u00b2 + 2pq + q\u00b2 = 1", s: "Without selection, migration, or drift, allele frequencies stay constant generation after generation."},
    {n: "Central dogma", e: "DNA \u2192 RNA \u2192 protein", s: "Genetic information flows from sequence to functional molecule."}
];
var USES=["Counseling inherited-disease risk", "Breeding improved crops", "Tracing ancestry and relatedness", "Screening newborns for disorders"];
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
    id:id, t:tp.t, g:field, name:"Genetics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Genetics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-genetics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-genetics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-genetics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
