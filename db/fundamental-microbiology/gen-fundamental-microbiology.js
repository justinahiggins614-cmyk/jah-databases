(function(){'use strict';
/* JAH Fundamentals of Microbiology Database generator — jahdb-fundamental-microbiology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MIC-";
var FIELDS=["bacterial structure", "growth", "viruses", "fungi and parasites", "microbial ecology", "applied microbiology"];
var TOPICS=[
    {t: "The Microbial World", b: "Bacteria, archaea, fungi, protists, viruses: most of life's diversity is microscopic, and microbes run Earth's biogeochemistry."},
    {t: "Prokaryotic Cell Structure", b: "No nucleus, but sophisticated: cell walls (Gram +/\u2212), flagella, pili, plasmids, and endospores for survival."},
    {t: "Bacterial Growth", b: "Lag, log, stationary, death phases: batch cultures trace a predictable curve governed by nutrients and waste."},
    {t: "Culturing the Unculturable", b: "Most microbes resist lab culture; metagenomics now reads communities straight from environmental DNA."},
    {t: "Antibiotics and Resistance", b: "\u03b2-lactams, aminoglycosides, and others each attack bacterial weak points; resistance evolves by selection \u2014 stewardship matters."},
    {t: "Viruses: Not Quite Alive", b: "Obligate intracellular parasites of nucleic acid plus protein: lytic vs lysogenic cycles, and why antibiotics can't touch them."},
    {t: "Bacteriophages", b: "Viruses that eat bacteria: the most abundant biological entities on Earth, now returning as precision antibacterials."},
    {t: "Fungi: Decomposers and Partners", b: "Yeasts, molds, and mycorrhizae digest the indigestible and trade nutrients with plants \u2014 plus antibiotics and bread."},
    {t: "The Human Microbiome", b: "Trillions of gut microbes digest fiber, train immunity, and make vitamins: an organ we acquire, not inherit."},
    {t: "Microbial Ecology", b: "Nitrogen fixation, decomposition, and ocean photosynthesis: microbes drive the cycles macro-life depends on."},
    {t: "Sterilization and Disinfection", b: "Autoclaves, filtration, and chemical agents each kill by defined mechanisms \u2014 validated, not assumed."},
    {t: "Industrial Microbiology", b: "Fermentation makes insulin, enzymes, biofuels, and cheese: engineered microbes as chemical factories."}
];
var PRINCIPLES=[
    {n: "Exponential growth", e: "N = N\u2080\u00b72^(t/g)", s: "Binary fission doubles populations every generation time g \u2014 explosive mathematics."},
    {n: "Monod kinetics", e: "\u03bc = \u03bcmax\u00b7S/(Ks + S)", s: "Microbial growth rate saturates with limiting nutrient, mirroring enzyme kinetics."},
    {n: "Koch's postulates", e: "isolate \u2192 inoculate \u2192 re-isolate", s: "The classical proof that a microbe causes a disease."}
];
var USES=["Diagnosing infectious disease", "Designing antibiotic stewardship", "Running fermentation processes", "Testing food and water safety"];
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
    id:id, t:tp.t, g:field, name:"Microbiology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Microbiology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-microbiology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-microbiology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-microbiology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
