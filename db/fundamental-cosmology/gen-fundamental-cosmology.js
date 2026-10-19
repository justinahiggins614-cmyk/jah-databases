(function(){'use strict';
/* JAH Fundamentals of Cosmology Database generator — jahdb-fundamental-cosmology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COS-";
var FIELDS=["expansion", "Big Bang", "cosmic microwave background", "structure formation", "dark energy", "early universe"];
var TOPICS=[
    {t: "The Cosmological Principle", b: "On large scales the universe is homogeneous and isotropic: the simplifying assumption that makes cosmology possible."},
    {t: "Hubble's Discovery", b: "1929: galaxies recede with v \u221d d \u2014 the universe is expanding, so it was smaller, denser, hotter in the past."},
    {t: "The Big Bang Model", b: "Hot, dense origin ~13.8 billion years ago: expansion, cooling, and nucleosynthesis in one framework."},
    {t: "Cosmic Microwave Background", b: "The 2.725-K afterglow of recombination (380,000 years): the Big Bang's baby photo, uniform to 1 part in 100,000."},
    {t: "CMB Anisotropies", b: "Tiny temperature ripples are the seeds of galaxies; their pattern measures curvature, matter, and dark energy precisely."},
    {t: "Big Bang Nucleosynthesis", b: "The first minutes forged H, He, and Li in predicted ratios \u2014 matching observations is a pillar of the model."},
    {t: "Structure Formation", b: "Gravity amplifies quantum fluctuations into the cosmic web: dark matter scaffolding, galaxies as decoration."},
    {t: "Dark Energy", b: "1998: expansion accelerates, driven by ~68% of the cosmic budget \u2014 the biggest mystery in physics."},
    {t: "Inflation", b: "A fraction-of-a-second exponential expansion explains flatness, uniformity, and the seed fluctuations \u2014 the leading early-universe theory."},
    {t: "The Fate Question", b: "Open, flat, or closed; Big Freeze, Crunch, or Rip: dark energy's nature decides the ending."},
    {t: "Cosmic Timeline", b: "Inflation \u2192 nucleosynthesis \u2192 recombination \u2192 first stars \u2192 galaxies \u2192 now: 13.8 billion years in one story."},
    {t: "Testing Cosmology", b: "Supernovae, BAO, lensing, and CMB polarization cross-check the \u039bCDM model \u2014 precision cosmology's ongoing audit."}
];
var PRINCIPLES=[
    {n: "Hubble's law", e: "v = H\u2080\u00b7d", s: "Recession velocity grows with distance \u2014 the observational fact of expansion."},
    {n: "Friedmann equation", e: "H\u00b2 = (8\u03c0G/3)\u00b7\u03c1 \u2212 k/a\u00b2", s: "General relativity's equation for an expanding homogeneous universe."},
    {n: "Redshift", e: "1 + z = \u03bb_obs/\u03bb_emit", s: "Stretching of light measures cosmic expansion directly."}
];
var USES=["Interpreting deep-sky surveys", "Calibrating cosmic distance scales", "Testing dark-energy models", "Teaching the universe's history"];
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
    id:id, t:tp.t, g:field, name:"Cosmology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Cosmology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-cosmology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-cosmology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-cosmology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
