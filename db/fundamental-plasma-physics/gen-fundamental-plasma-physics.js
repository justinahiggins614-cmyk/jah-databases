(function(){'use strict';
/* JAH Fundamentals of Plasma Physics Database generator — jahdb-fundamental-plasma-physics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PP2-";
var FIELDS=["plasma basics", "single-particle motion", "MHD", "waves", "fusion", "space plasmas"];
var TOPICS=[
    {t: "What Plasma Is", b: "Ionized gas where collective electromagnetic effects dominate: 99% of visible matter, from stars to neon signs."},
    {t: "Debye Shielding", b: "Each charge surrounds itself with opposite charges within \u03bb_D: beyond that, the plasma looks neutral \u2014 quasineutrality."},
    {t: "Plasma Frequency", b: "Displaced electrons slosh back at \u03c9_p: below this frequency plasmas reflect (ionosphere), above they transmit."},
    {t: "Single-Particle Motion", b: "Gyration around field lines, E\u00d7B drift, magnetic mirrors: the orbit theory behind confinement and auroras."},
    {t: "Magnetohydrodynamics", b: "Treating plasma as a conducting fluid: Alfv\u00e9n waves, frozen-in flux, and the instabilities fusion must tame."},
    {t: "Plasma Waves", b: "Langmuir, ion-acoustic, whistler modes: plasmas support wave zoo far richer than any neutral gas."},
    {t: "Landau Damping", b: "Wave-particle resonance drains wave energy collisionlessly \u2014 a purely kinetic effect with no fluid analogue."},
    {t: "Magnetic Confinement Fusion", b: "Tokamaks and stellarators bend field lines into bottles: ITER aims for burning plasma at 150 million \u00b0C."},
    {t: "Inertial Confinement Fusion", b: "Laser-crushed pellets (NIF's 2022 ignition) achieve Lawson conditions for billionths of a second."},
    {t: "Plasma Processing", b: "Etching chips, coating tools, treating surfaces: low-temperature plasmas are manufacturing's invisible workhorse."},
    {t: "Space Plasmas", b: "Solar wind, magnetospheres, auroras: Earth's magnetic shield deflects the Sun's plasma stream \u2014 space weather's stage."},
    {t: "Plasma Diagnostics", b: "Langmuir probes, interferometry, Thomson scattering, spectroscopy: measuring the unmeasurable in million-degree matter."}
];
var PRINCIPLES=[
    {n: "Debye shielding", e: "\u03bb_D = \u221a(\u03b5\u2080kT/ne\u00b2)", s: "Plasmas screen electric fields beyond the Debye length \u2014 collective behavior's defining scale."},
    {n: "Plasma frequency", e: "\u03c9_p = \u221a(ne\u00b2/(m\u03b5\u2080))", s: "Electrons oscillate collectively at a density-set frequency \u2014 the plasma's heartbeat."},
    {n: "Lawson criterion", e: "n\u00b7\u03c4 > ~10\u00b2\u2070 s/m\u00b3 (D-T)", s: "Fusion breakeven needs density times confinement time past this product."}
];
var USES=["Designing fusion experiments", "Etching semiconductor wafers", "Modeling space weather", "Building plasma thrusters"];
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
    id:id, t:tp.t, g:field, name:"Plasma Physics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Plasma Physics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-plasma-physics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-plasma-physics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-plasma-physics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
