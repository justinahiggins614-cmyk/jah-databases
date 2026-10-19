(function(){'use strict';
/* JAH Fundamentals of Oceanography Database generator — jahdb-fundamental-oceanography-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OCE-";
var FIELDS=["physical oceanography", "waves", "chemistry", "marine geology", "marine biology", "climate role"];
var TOPICS=[
    {t: "The Ocean's Scale", b: "71% of Earth's surface, 97% of its water, average depth 3.7 km: the ocean is the planet's dominant feature."},
    {t: "Seawater Properties", b: "Salinity (~35 psu), temperature, and pressure set density: the equation of state drives all ocean motion."},
    {t: "Surface Currents and Gyres", b: "Wind plus Coriolis organizes surface flow into five great gyres \u2014 and concentrates humanity's plastic in their centers."},
    {t: "The Deep Conveyor", b: "North Atlantic deep-water formation pulls a global loop: the thermohaline circulation redistributes heat over millennia."},
    {t: "Waves", b: "Wind fetch, duration, and speed build waves; dispersion sorts them by wavelength \u2014 tsunamis and tides are different physics entirely."},
    {t: "Tides", b: "Moon and Sun gravity plus Earth's rotation: semidiurnal, diurnal, and spring-neap cycles predictable centuries ahead."},
    {t: "Ocean Chemistry", b: "Major ions stay constant (Marcet's principle); nutrients (N, P, Fe) limit life \u2014 iron fertilization experiments proved it."},
    {t: "Ocean Acidification", b: "Absorbing a third of fossil CO\u2082 has dropped surface pH ~0.1: chemistry now hostile to shell-builders."},
    {t: "Marine Food Webs", b: "Phytoplankton \u2192 zooplankton \u2192 fish: ocean productivity starts with microscopic plants in sunlit surface waters."},
    {t: "Seafloor Geology", b: "Mid-ocean ridges create crust, trenches destroy it: plate tectonics was proven on the ocean floor."},
    {t: "The Ocean and Climate", b: "Oceans store 90%+ of warming's heat and drive El Ni\u00f1o: climate models live or die on ocean physics."},
    {t: "Exploring the Deep", b: "Submersibles, floats (Argo), and satellites map the least-known habitat on Earth \u2014 most seafloor is still unmapped."}
];
var PRINCIPLES=[
    {n: "Thermohaline circulation", e: "density-driven global conveyor", s: "Temperature and salinity differences drive the deep ocean's thousand-year overturning."},
    {n: "Coriolis deflection", e: "F = \u22122m(v \u00d7 \u03a9)", s: "Earth's rotation curves currents right in the north, left in the south \u2014 gyres result."},
    {n: "Carbonate chemistry", e: "CO\u2082 + H\u2082O \u21cc H\u2082CO\u2083", s: "Ocean acidification is this equilibrium shifting as atmospheric CO\u2082 dissolves."}
];
var USES=["Forecasting hurricanes and El Ni\u00f1o", "Planning offshore operations", "Managing fisheries", "Tracking ocean acidification"];
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
    id:id, t:tp.t, g:field, name:"Oceanography"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Oceanography demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-oceanography-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-oceanography-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-oceanography",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
