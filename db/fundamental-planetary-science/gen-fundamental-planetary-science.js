(function(){'use strict';
/* JAH Fundamentals of Planetary Science Database generator — jahdb-fundamental-planetary-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PS2-";
var FIELDS=["formation", "terrestrial planets", "gas giants", "moons", "small bodies", "exoplanets"];
var TOPICS=[
    {t: "How Planets Form", b: "The solar nebula's dust settled, stuck, and grew: core accretion built giants, photoevaporation sculpted the leftovers."},
    {t: "Differentiation", b: "Melting lets iron sink and rock float: cores, mantles, and crusts are gravity-sorted layers."},
    {t: "Terrestrial Planets", b: "Mercury, Venus, Earth, Mars: small, rocky, cratered or volcanic \u2014 four experiments in rocky-planet evolution."},
    {t: "Why Venus and Mars Differ", b: "Runaway greenhouse (Venus) vs atmospheric loss (Mars): Earth's habitability looks increasingly like luck plus feedbacks."},
    {t: "Gas Giants", b: "Jupiter and Saturn: hydrogen-helium envelopes over deep interiors, with magnetic fields dwarfing Earth's."},
    {t: "Ice Giants", b: "Uranus and Neptune: water-ammonia mantles, tilted fields, supersonic winds \u2014 the least understood planets."},
    {t: "Moons as Worlds", b: "Europa's ocean, Enceladus's geysers, Titan's methane lakes, Io's volcanoes: moons outshine planets for astrobiology."},
    {t: "Asteroids and Comets", b: "Leftover building blocks: rubble piles, differentiated fragments, and icy dirtballs \u2014 the solar system's fossil record."},
    {t: "Impact Cratering", b: "Hypervelocity impacts excavate, melt, and eject: crater counting dates surfaces across the solar system."},
    {t: "Planetary Atmospheres", b: "Retention (escape velocity vs thermal speed), greenhouse physics, and photochemistry explain every planet's sky."},
    {t: "Exoplanets", b: "Transits and radial velocities have found 5,000+ worlds: hot Jupiters, super-Earths, and systems stranger than imagined."},
    {t: "Habitability", b: "Liquid water, energy, nutrients, stability: the requirements list guiding the search for life beyond Earth."}
];
var PRINCIPLES=[
    {n: "Accretion", e: "planetesimals \u2192 planets", s: "Gravity assembles dust to pebbles to planetesimals to planets over millions of years."},
    {n: "Hydrostatic equilibrium (planets)", e: "dP/dr = \u2212\u03c1g", s: "Interior structure balances weight against pressure \u2014 core, mantle, crust from density."},
    {n: "Habitable zone", e: "liquid-water orbit range", s: "The distance band where a planet can keep surface water \u2014 habitability's first filter."}
];
var USES=["Planning planetary missions", "Interpreting rover and orbiter data", "Assessing exoplanet habitability", "Modeling impact hazards"];
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
    id:id, t:tp.t, g:field, name:"Planetary Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Planetary Science demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-planetary-science-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-planetary-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-planetary-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
