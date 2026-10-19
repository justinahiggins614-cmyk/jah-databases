(function(){'use strict';
/* JAH Food Preservation Science Database generator — jahdb-food-preservation-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FPS-";
var FIELDS=["thermal methods", "dehydration", "refrigeration", "chemical preservation", "packaging", "hurdle technology"];
var TOPICS=[
    {t: "Spoilage Mechanisms", b: "Microbial growth, enzymatic browning, oxidation, staling: the four horsemen every method fights."},
    {t: "Water Activity", b: "aw measures water available to microbes: salt, sugar, and drying all work by lowering it."},
    {t: "Canning and Retort", b: "12-D botulinum cook for low-acid foods: the thermal process that made year-round food possible."},
    {t: "Pasteurization", b: "Gentle heat for milk, juice, beer: killing pathogens while keeping flavor \u2014 HTST vs UHT trade-offs."},
    {t: "Dehydration", b: "Sun, spray, freeze drying: removing water concentrates flavor and stops microbes \u2014 rehydration quality is the art."},
    {t: "Freezing", b: "Fast freezing makes small ice crystals (quality); the cold chain's unbroken discipline keeps it safe."},
    {t: "Fermentation as Preservation", b: "Acid, alcohol, and salt from microbes: the oldest preservation technologies, still essential."},
    {t: "Chemical Preservatives", b: "Sorbates, benzoates, nitrites, sulfites: each targets specific spoilage with specific safety evaluations."},
    {t: "Modified Atmosphere Packaging", b: "Flushing oxygen for nitrogen/CO\u2082: bakery, meat, and produce shelf life extended by gas."},
    {t: "Irradiation", b: "Cold pasteurization with ionizing energy: approved, effective, and misunderstood \u2014 the labeling debate."},
    {t: "Hurdle Technology", b: "Combining mild hurdles (pH + aw + MAP + chill) for safety with fresh-like quality: modern minimal processing."},
    {t: "Shelf-Life Testing", b: "Microbial challenge, sensory panels, and accelerated storage: proving the 'best by' date scientifically."}
];
var PRINCIPLES=[
    {n: "Every method is a hurdle", e: "", s: "Heat, cold, dryness, acidity, salt: combined hurdles beat any single one \u2014 Leistner's insight."},
    {n: "Water activity rules microbes", e: "", s: "Below aw 0.85 most pathogens stop, below 0.60 almost everything stops: dryness as preservation."},
    {n: "Shelf life is validated, not declared", e: "", s: "Challenge studies and accelerated aging prove the date on the package."}
];
var USES=["Designing thermal processes", "Setting shelf-life dates", "Formulating preserved foods", "Troubleshooting spoilage"];
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
    id:id, t:tp.t, g:field, name:"Food Preservation Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Food Preservation Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-food-preservation-science-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-food-preservation-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("food-preservation-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
