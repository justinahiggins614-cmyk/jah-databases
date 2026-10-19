(function(){'use strict';
/* JAH Fundamentals of Soil Science Database generator — jahdb-fundamental-soil-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SS2-";
var FIELDS=["soil formation", "texture and structure", "chemistry", "biology", "water", "management"];
var TOPICS=[
    {t: "What Soil Is", b: "Weathered rock plus organic matter plus water plus air plus life: a four-phase system, not just dirt."},
    {t: "The Five Forming Factors", b: "Climate, organisms, relief, parent material, time (CLORPT): the same rock makes different soils under different skies."},
    {t: "Soil Horizons", b: "O, A, E, B, C, R: layered profiles record formation history \u2014 reading them is reading the land's biography."},
    {t: "Texture: Sand, Silt, Clay", b: "Particle size sets everything: sand drains, silt holds, clay binds \u2014 the texture triangle names the mixture."},
    {t: "Structure and Pores", b: "Aggregates built by roots, fungi, and worms create the pore networks water and air travel through."},
    {t: "Cation Exchange Capacity", b: "Negative charges on clay and humus hold Ca, Mg, K, NH\u2084: CEC quantifies fertility's storage tank."},
    {t: "pH and Nutrient Availability", b: "Acidity locks up phosphorus and molybdenum, releases aluminum toxically: pH 6\u20137 keeps most nutrients available."},
    {t: "Soil Organic Matter", b: "Humus stores carbon, feeds microbes, and holds water: each 1% organic matter holds ~20,000 gallons per acre."},
    {t: "The Soil Food Web", b: "Bacteria, fungi, protozoa, nematodes, earthworms: decomposition and nutrient cycling run through this underground economy."},
    {t: "Water in Soil", b: "Field capacity, wilting point, available water: the moisture window plants actually drink from."},
    {t: "Erosion", b: "Water and wind strip topsoil far faster than it forms: conservation tillage, cover crops, and terraces keep it in place."},
    {t: "Soil Classification", b: "USDA Soil Taxonomy's 12 orders (Mollisols, Oxisols, ...) map the world's soils by formation and properties."}
];
var PRINCIPLES=[
    {n: "Texture triangle", e: "%sand + %silt + %clay = 100", s: "Particle-size fractions name every soil: loam is the balanced ideal."},
    {n: "Cation exchange", e: "CEC holds nutrients", s: "Clay and humus surfaces store nutrient cations, releasing them to roots \u2014 soil's pantry."},
    {n: "Water potential", e: "\u03c8 = gravity + matric + osmotic", s: "Water moves from high to low potential: the unified physics of soil moisture."}
];
var USES=["Testing farmland fertility", "Planning irrigation", "Preventing erosion", "Remediating contaminated land"];
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
    id:id, t:tp.t, g:field, name:"Soil Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Soil Science demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-soil-science-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-soil-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-soil-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
