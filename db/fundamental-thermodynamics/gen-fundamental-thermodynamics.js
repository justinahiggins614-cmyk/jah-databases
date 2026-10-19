(function(){'use strict';
/* JAH Fundamentals of Thermodynamics Database generator — jahdb-fundamental-thermodynamics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-THE-";
var FIELDS=["temperature and heat", "the first law", "the second law", "entropy", "heat engines", "refrigeration and heat pumps"];
var TOPICS=[
    {t: "Temperature and Thermal Equilibrium", b: "Temperature measures average molecular kinetic energy; the zeroth law says systems in mutual equilibrium share one temperature \u2014 the basis of thermometry."},
    {t: "Heat, Work, and Internal Energy", b: "Heat is energy transferred by temperature difference, work is organized energy transfer, and internal energy is the stored sum at the molecular scale."},
    {t: "The First Law", b: "Energy cannot be created or destroyed, only converted: every joule of heat entering a system either does work or raises internal energy."},
    {t: "The Second Law", b: "Heat flows spontaneously from hot to cold, never the reverse unaided; every real process pays an entropy tax that can never be refunded."},
    {t: "Entropy Explained", b: "Entropy counts microscopic arrangements: ordered energy spreads into disorder, which is why broken eggs never reassemble and engines never reach 100% efficiency."},
    {t: "Carnot and Maximum Efficiency", b: "Sadi Carnot proved the ceiling for heat engines depends only on the hot and cold reservoir temperatures \u2014 a limit no design can beat."},
    {t: "Heat Engines in Practice", b: "Steam plants, car engines, and gas turbines all burn fuel to make heat flow do work; real efficiencies run 25\u201360% against Carnot limits."},
    {t: "Refrigerators and Heat Pumps", b: "Run a heat engine backward and it pumps heat uphill: refrigerators move heat out of food, heat pumps move outdoor heat indoors at 3\u20135\u00d7 the efficiency of resistance heat."},
    {t: "Phase Changes and Latent Heat", b: "Melting and boiling absorb large latent heat without temperature change \u2014 why sweating cools you and steam burns are severe."},
    {t: "The Ideal Gas Law", b: "PV = nRT ties pressure, volume, and temperature for dilute gases, predicting everything from tire pressure rise to balloon lift."},
    {t: "Statistical View: Boltzmann", b: "Macroscopic laws emerge from molecular statistics: entropy S = k\u00b7ln(W) counts microstates, grounding thermodynamics in probability."},
    {t: "Exergy: Useful Energy", b: "Not all energy is equal: exergy measures the convertible fraction, which is why waste heat near room temperature is nearly worthless for work."}
];
var PRINCIPLES=[
    {n: "First law", e: "\u0394U = Q \u2212 W", s: "Energy is conserved: heat in minus work out changes internal energy."},
    {n: "Carnot efficiency", e: "\u03b7 = 1 \u2212 Tc/Th", s: "No heat engine between temperatures Th and Tc can beat this efficiency."},
    {n: "Entropy and the second law", e: "\u0394S_universe \u2265 0", s: "The entropy of an isolated system never decreases; it defines time's arrow."}
];
var USES=["Sizing power-plant steam cycles", "Designing refrigerators and heat pumps", "Improving car engine fuel economy", "Managing data-center waste heat"];
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
    id:id, t:tp.t, g:field, name:"Thermodynamics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Thermodynamics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-thermodynamics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-thermodynamics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-thermodynamics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
