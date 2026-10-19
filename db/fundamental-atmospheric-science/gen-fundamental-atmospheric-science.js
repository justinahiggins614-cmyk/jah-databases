(function(){'use strict';
/* JAH Fundamentals of Atmospheric Science Database generator — jahdb-fundamental-atmospheric-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AS2-";
var FIELDS=["atmospheric structure", "thermodynamics", "clouds", "dynamics", "weather systems", "climate"];
var TOPICS=[
    {t: "Layers of the Atmosphere", b: "Troposphere, stratosphere, mesosphere, thermosphere: temperature inversions divide layers with distinct chemistry and motion."},
    {t: "The Ideal Gas at Scale", b: "Pressure, temperature, and density linked by gas law plus hydrostatics: the vertical structure of the sky."},
    {t: "Heating the Atmosphere", b: "Solar shortwave in, infrared out: the surface-atmosphere radiation budget sets climate, and greenhouse gases throttle the exit."},
    {t: "Adiabatic Processes", b: "Rising air expands and cools without heat exchange: the dry and moist lapse rates explain mountains' clouds and deserts' heat."},
    {t: "Cloud Formation", b: "Saturation, condensation nuclei, and lift: every cloud is air cooled to its dew point around microscopic seeds."},
    {t: "Precipitation", b: "Collision-coalescence (warm clouds) and Bergeron ice-crystal growth (cold clouds) fatten droplets until gravity wins."},
    {t: "Global Circulation", b: "Hadley, Ferrel, and polar cells plus jet streams: differential heating plus rotation organizes planetary winds."},
    {t: "Mid-Latitude Storms", b: "Baroclinic instability along the polar front spawns cyclones: the weather systems of temperate zones."},
    {t: "Thunderstorms and Tornadoes", b: "CAPE (instability) plus wind shear builds supercells; mesocyclones tighten into tornadoes \u2014 forecasting saves lives."},
    {t: "Tropical Cyclones", b: "Warm ocean + Coriolis + low shear = hurricanes: heat engines with 200-km/h winds, steered by the subtropical ridge."},
    {t: "Weather Forecasting", b: "Numerical models integrate fluid equations forward from observed initial conditions; ensembles quantify the uncertainty."},
    {t: "Climate vs Weather", b: "Weather is days, climate is decades: boundary conditions (greenhouse gases, aerosols, orbits) set the statistics weather samples."}
];
var PRINCIPLES=[
    {n: "Hydrostatic balance", e: "dP/dz = \u2212\u03c1g", s: "Pressure falls with height balancing air's weight \u2014 the atmosphere's vertical structure."},
    {n: "Adiabatic lapse rate", e: "\u0393_d = g/c_p \u2248 9.8\u00b0C/km", s: "Rising dry air cools at nearly 10\u00b0C per kilometer \u2014 the engine of clouds and storms."},
    {n: "Geostrophic balance", e: "Coriolis = pressure gradient", s: "Large-scale winds blow along isobars, balancing the two great horizontal forces."}
];
var USES=["Forecasting severe weather", "Modeling climate change", "Planning aviation routes", "Assessing air quality"];
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
    id:id, t:tp.t, g:field, name:"Atmospheric Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Atmospheric Science demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-atmospheric-science-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-atmospheric-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-atmospheric-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
