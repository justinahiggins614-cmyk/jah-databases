(function(){'use strict';
/* JAH Fundamentals of Evolution Database generator — jahdb-fundamental-evolution-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVO-";
var FIELDS=["natural selection", "genetic drift", "speciation", "phylogeny", "human evolution", "evidence"];
var TOPICS=[
    {t: "Darwin's Core Idea", b: "Variation, heritability, differential survival: given these three, evolution by natural selection is a logical necessity."},
    {t: "The Modern Synthesis", b: "Mendel's genetics fused with Darwin's selection: population genetics made evolution quantitative in the 1930s\u201340s."},
    {t: "Natural Selection in Action", b: "Peppered moths, antibiotic resistance, Darwin's finches: selection observed in real time, not just inferred."},
    {t: "Genetic Drift", b: "Random sampling of gametes shifts allele frequencies \u2014 powerful in small populations, the null hypothesis of evolution."},
    {t: "Mutation as Raw Material", b: "Without new variants selection has nothing to act on; mutation rates are tuned by evolution itself."},
    {t: "Gene Flow and Migration", b: "Migrants carry alleles between populations, homogenizing differences \u2014 isolation is what lets divergence proceed."},
    {t: "Speciation", b: "Reproductive isolation \u2014 geographic, behavioral, genetic \u2014 splits one lineage into two: allopatric, sympatric, and hybrid routes."},
    {t: "Phylogenetic Trees", b: "Shared derived traits nest species into trees; DNA now resolves relationships morphology only guessed at."},
    {t: "Convergent Evolution", b: "Dolphins and ichthyosaurs, wings of bats and birds: similar problems evolve similar solutions independently."},
    {t: "Coevolution", b: "Predators and prey, flowers and pollinators, hosts and parasites evolve against each other \u2014 Red Queen arms races."},
    {t: "Human Evolution", b: "Bipedalism, brain expansion, and culture: the fossil and genomic record of Homo sapiens' last 7 million years."},
    {t: "Evidence Consilience", b: "Fossils, DNA, biogeography, embryology, and observed selection all converge \u2014 evolution is among science's best-supported theories."}
];
var PRINCIPLES=[
    {n: "Selection response", e: "R = h\u00b2\u00b7S", s: "The breeder's equation: response equals heritability times the selection differential."},
    {n: "Fitness", e: "w = survival \u00d7 reproduction", s: "Natural selection favors variants that leave the most descendants \u2014 nothing more."},
    {n: "Molecular clock", e: "divergence \u221d time", s: "Neutral mutations accumulate steadily, dating splits between lineages."}
];
var USES=["Breeding crops and livestock", "Managing antibiotic resistance", "Reconstructing evolutionary trees", "Conserving genetic diversity"];
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
    id:id, t:tp.t, g:field, name:"Evolution"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Evolution demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-evolution-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-evolution-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-evolution",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
