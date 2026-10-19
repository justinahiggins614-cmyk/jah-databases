(function(){'use strict';
/* JAH Flavor Chemistry Systems Database generator — jahdb-flavor-chemistry-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FCS-";
var FIELDS=["aroma compounds", "taste physiology", "Maillard", "fermentation flavors", "formulation", "sensory science"];
var TOPICS=[
    {t: "Taste Physiology", b: "Taste buds, receptors (T1R, T2R), and the gustatory cortex: how molecules become perceptions."},
    {t: "Smell: Orthonasal and Retronasal", b: "Sniffing vs chewing release: retronasal aroma during eating is most of 'taste' \u2014 the nose does the work."},
    {t: "Key Aroma Compounds", b: "Vanillin, isoamyl acetate, diacetyl, geosmin: character-impact compounds that define foods at trace levels."},
    {t: "The Maillard Reaction", b: "Amino acids plus reducing sugars above 140\u00b0C: the browning chemistry behind bread crust, seared meat, and coffee."},
    {t: "Caramelization", b: "Sugar pyrolysis: distinct from Maillard, the chemistry of dulce de leche and dark beer color."},
    {t: "Fermentation Flavors", b: "Esters, higher alcohols, diacetyl, sulfur compounds: yeast and bacteria as flavor factories \u2014 managed, not accidental."},
    {t: "Lipid Oxidation", b: "Rancidity's chemistry: unsaturated fats plus oxygen make off-flavors \u2014 antioxidants and packaging fight it."},
    {t: "Taste Modifiers", b: "Sweeteners, salt replacers, bitterness blockers, kokumi: the toolkit for healthier formulations that still delight."},
    {t: "Natural vs Artificial", b: "Regulatory definitions and consumer perception vs chemical identity: the same molecule, different stories."},
    {t: "Flavor Formulation", b: "Compounding houses balance top, middle, and base notes: perfumery's discipline applied to food."},
    {t: "Sensory Science", b: "Triangle tests, descriptive panels, and hedonic scales: measuring the subjective with statistical rigor."},
    {t: "Flavor and Health", b: "Sugar, salt, and fat reduction through flavor technology: making healthy food craveable."}
];
var PRINCIPLES=[
    {n: "Aroma is chemistry you smell", e: "", s: "Each key odorant has a threshold and character: GC-olfactometry finds the few compounds that matter among hundreds."},
    {n: "Taste is five plus texture", e: "", s: "Sweet, sour, salty, bitter, umami \u2014 plus trigeminal heat and mouthfeel: flavor is multisensory by definition."},
    {n: "Dose makes the flavor", e: "", s: "The same compound delights at ppb and disgusts at ppm: formulation is concentration discipline."}
];
var USES=["Formulating natural flavors", "Troubleshooting off-flavors", "Reducing sugar and salt", "Running sensory panels"];
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
    id:id, t:tp.t, g:field, name:"Flavor Chemistry Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Flavor Chemistry Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-flavor-chemistry-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-flavor-chemistry-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("flavor-chemistry-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
