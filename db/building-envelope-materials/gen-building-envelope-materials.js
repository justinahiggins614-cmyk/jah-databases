(function(){'use strict';
/* JAH Building Envelope Materials Database generator — jahdb-building-envelope-materials-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BEM-";
var FIELDS=["wall assemblies", "roofing", "glazing", "insulation", "air and vapor control", "cladding"];
var TOPICS=[
    {t: "What the Envelope Does", b: "Separates inside from outside across four controls \u2014 water, air, vapor, heat \u2014 while carrying structural and aesthetic duties."},
    {t: "Rainscreen Principle", b: "A vented cavity behind cladding equalizes pressure and drains intrusions: the most robust wall strategy in wet climates."},
    {t: "Insulation Types", b: "Fiberglass, mineral wool, cellulose, foam boards, spray foam: R-value per inch, fire, moisture, and environmental trade-offs."},
    {t: "Air Barriers", b: "Uncontrolled air leakage carries moisture into walls and wastes energy: blower-door testing (ACH50) verifies the invisible."},
    {t: "Vapor Control", b: "Vapor retarders belong on the warm side \u2014 which side is warm flips by climate: get it wrong and walls grow mold."},
    {t: "Windows and Glazing", b: "U-factor, SHGC, and visible transmittance quantify performance; low-E coatings and gas fills tune each independently."},
    {t: "Roofing Systems", b: "Asphalt, metal, membrane, tile: slope, climate, and lifespan pick the system; flashing details decide if it works."},
    {t: "Cladding Choices", b: "Brick, fiber-cement, wood, metal panels: durability, maintenance, and rainscreen compatibility ranked per exposure."},
    {t: "Thermal Bridging", b: "Steel studs and concrete slabs short-circuit insulation: breaks and exterior continuous insulation fix the weak points."},
    {t: "Moisture Forensics", b: "Stains, efflorescence, and rot patterns diagnose envelope failures \u2014 reading buildings like medical cases."},
    {t: "Climate-Specific Design", b: "Hot-humid, cold, marine, and mixed climates each demand different layer sequences: one wall does not fit all."},
    {t: "Retrofit Strategies", b: "Exterior insulation, air sealing, and window upgrades transform existing buildings \u2014 the biggest energy prize in construction."}
];
var PRINCIPLES=[
    {n: "Control layers in order", e: "", s: "Rain, air, vapor, thermal \u2014 in the right sequence for the climate: misplaced vapor retarders rot walls."},
    {n: "Drain the rain", e: "", s: "Every cladding leaks a little: drained and ventilated cavities (rainscreens) manage what barriers cannot stop."},
    {n: "Continuity wins", e: "", s: "Insulation, air barrier, and water control must be continuous: gaps and compressions are where envelopes fail."}
];
var USES=["Designing wall assemblies", "Specifying window performance", "Diagnosing moisture failures", "Planning deep-energy retrofits"];
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
    id:id, t:tp.t, g:field, name:"Building Envelope Materials"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Building Envelope Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-building-envelope-materials-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-building-envelope-materials-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("building-envelope-materials",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
