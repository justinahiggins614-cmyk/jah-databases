(function(){'use strict';
/* JAH Fundamentals of Synthetic Biology Database generator — jahdb-fundamental-synthetic-biology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SB-";
var FIELDS=["genetic parts", "circuits", "chassis organisms", "genome engineering", "cell-free systems", "biosafety"];
var TOPICS=[
    {t: "Biology as Engineering Substrate", b: "Synthetic biology treats DNA as code and cells as chassis: specify function, assemble genetic parts, debug in vivo."},
    {t: "Parts, Devices, Systems", b: "Promoters, ribosome-binding sites, and terminators are parts; sensors and logic gates are devices; pathways are systems \u2014 abstraction hierarchy borrowed from electronics."},
    {t: "The Central Dogma in Practice", b: "Transcription and translation rates are tunable dials: promoter strength and RBS strength set how much protein each gene makes."},
    {t: "Genetic Toggle Switches", b: "Two mutually repressing genes form a bistable memory bit \u2014 the first synthetic circuit and proof that biology computes."},
    {t: "Oscillators: The Repressilator", b: "Three repressors in a ring blink in sequence, a molecular clock showing that feedback topology programs dynamics."},
    {t: "CRISPR as an Engineering Tool", b: "Programmable guide RNAs direct Cas proteins to cut, activate, or repress any targeted sequence \u2014 search-and-edit for genomes."},
    {t: "Chassis Organisms", b: "E. coli, yeast, and Bacillus are the workhorse hosts: well-mapped, fast-growing, and genetically tractable platforms."},
    {t: "Metabolic Pathway Engineering", b: "Rewiring metabolism makes microbes produce artemisinin, insulin, and biofuels \u2014 balancing flux so the cell survives its new job."},
    {t: "Cell-Free Systems", b: "Extracts of transcription-translation machinery run genetic programs without living cells: faster prototyping, easier containment."},
    {t: "Burden and Evolutionary Stability", b: "Cells mutate away costly circuits; burden-aware design and selection circuits keep engineered functions alive over generations."},
    {t: "Biosafety and Biocontainment", b: "Kill switches, auxotrophy, and recoded genomes contain engineered organisms; risk assessment scales with the organism and the environment."},
    {t: "Biosecurity and Governance", b: "DNA synthesis screening and international norms guard against misuse \u2014 engineering life carries responsibilities chemistry never did."}
];
var PRINCIPLES=[
    {n: "Central dogma", e: "DNA \u2192 RNA \u2192 protein", s: "Information flows from gene to transcript to functional protein \u2014 the operating system of the cell."},
    {n: "Hill-function regulation", e: "output = max\u00b7[I]^n/(K^n + [I]^n)", s: "Genetic switches and sensors follow sigmoidal dose-response curves."},
    {n: "Growth burden", e: "growth \u221d 1/(1 + burden)", s: "Every synthetic circuit taxes its host; burden slows growth and invites mutation."}
];
var USES=["Designing microbial drug factories", "Building biosensor circuits", "Engineering contained cell-free diagnostics", "Assessing engineered-organism safety"];
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
    id:id, t:tp.t, g:field, name:"Synthetic Biology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Synthetic Biology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-synthetic-biology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-synthetic-biology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-synthetic-biology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
