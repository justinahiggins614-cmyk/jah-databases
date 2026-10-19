(function(){'use strict';
/* JAH Semiconductor Fabrication Systems Database generator — jahdb-semiconductor-fabrication-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SFS-";
var FIELDS=["lithography", "deposition", "etch", "doping", "metrology", "yield"];
var TOPICS=[
    {t: "The Fab", b: "Bays, cleanrooms (ISO 3), and $20B price tags: the most complex manufacturing environment ever built."},
    {t: "Wafers", b: "Czochralski silicon, 300-mm standard, crystal orientation: the substrate everything builds on."},
    {t: "Oxidation and Diffusion", b: "Growing SiO\u2082 and driving dopants: the thermal processes forming transistors' foundations."},
    {t: "Ion Implantation", b: "Shooting dopants into silicon with precision: dose, energy, and annealing activating the junctions."},
    {t: "Lithography", b: "From i-line to EUV: patterning billions of features \u2014 the critical, costliest step."},
    {t: "Etch", b: "Plasma carving of trenches and vias: anisotropy, selectivity, and the atomic-scale control required."},
    {t: "Deposition", b: "CVD, PVD, ALD, epitaxy: building the transistor's layers atom by atom."},
    {t: "CMP", b: "Chemical-mechanical polishing flattening each layer: without planarity, multilayer chips are impossible."},
    {t: "Metrology", b: "CD-SEM, overlay, ellipsometry: measuring nanometers in-line to control the process."},
    {t: "Yield Engineering", b: "Defect Pareto, process control, binning: the statistical war for good die."},
    {t: "Packaging", b: "From wafer to BGA/chiplets: dicing, bonding, and advanced packaging (2.5-D, 3-D) continuing scaling."},
    {t: "Economics", b: "Cost per wafer, learning curves, and the foundry model: the business physics of Moore's law."}
];
var PRINCIPLES=[
    {n: "Yield is the product", e: "", s: "A fab sells good die per wafer: defect density, not transistor count, decides profitability."},
    {n: "Contamination is measured in atoms", e: "", s: "A single particle kills a die: cleanroom discipline and chemical purity are the factory's religion."},
    {n: "Process integration rules", e: "", s: "Individual steps are easy; making 1,400 of them work together is the actual technology."}
];
var USES=["Planning process flows", "Troubleshooting yield excursions", "Specifying fab equipment", "Modeling chip cost"];
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
    id:id, t:tp.t, g:field, name:"Semiconductor Fabrication Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Semiconductor Fab Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-semiconductor-fabrication-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-semiconductor-fabrication-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("semiconductor-fabrication-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
