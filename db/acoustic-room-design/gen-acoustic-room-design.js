(function(){'use strict';
/* JAH Acoustic Room Design Database generator — jahdb-acoustic-room-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ARD-";
var FIELDS=["room acoustics", "concert halls", "studios", "classrooms", "offices", "noise control"];
var TOPICS=[
    {t: "Reverberation Time", b: "Sabine's equation (T = 0.161V/A): the master metric \u2014 2 s for symphony, 0.5 s for speech, 0.3 s for studios."},
    {t: "Early Reflections", b: "The first 50 ms shape clarity and intimacy: reflector panels delivering useful early energy to seats."},
    {t: "Concert Hall Shapes", b: "Shoebox (Vienna), vineyard (Berlin), fan: geometries trading intimacy, envelopment, and capacity."},
    {t: "Recording Studios", b: "Dead control rooms, live tracking rooms, isolation: designing for microphones, not ears."},
    {t: "Classroom Acoustics", b: "0.6 s RT, 35 dBA background, +15 dB signal-to-noise: the ANSI standard for learning spaces."},
    {t: "Office Acoustics", b: "Speech privacy (articulation index), masking systems, and absorption: open plans that don't destroy concentration."},
    {t: "Absorption Materials", b: "Porous absorbers (high frequencies), panel/membrane (lows), Helmholtz resonators (tuned): the toolkit by frequency."},
    {t: "Diffusion", b: "Quadratic-residue and skyline diffusers scattering reflections: envelopment without deadness."},
    {t: "Sound Isolation", b: "Mass law, double-stud walls, floating floors: STC/IIC ratings and the flanking paths that defeat them."},
    {t: "HVAC Noise", b: "Duct silencers, low-velocity design, vibration isolation: the mechanical systems behind NC-25 silence."},
    {t: "Measurement", b: "RT60, STI, NC curves: verifying the design with microphones, not opinions."},
    {t: "Case Studies", b: "Famous halls' dimensions and materials: learning from the rooms the world agrees sound right."}
];
var PRINCIPLES=[
    {n: "Geometry first, treatment second", e: "", s: "Room shape and volume set the acoustic destiny: absorption fixes problems geometry should have prevented."},
    {n: "One room, one purpose", e: "", s: "Concert warmth, speech clarity, and recording deadness conflict: program the acoustic before drawing the room."},
    {n: "Silence the noise floor", e: "", s: "HVAC and traffic noise set the baseline: NC curves must be met before any finish matters."}
];
var USES=["Designing concert halls", "Treating recording studios", "Fixing classroom acoustics", "Planning office sound masking"];
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
    id:id, t:tp.t, g:field, name:"Acoustic Room Design"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Acoustic Room Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-acoustic-room-design-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-acoustic-room-design-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("acoustic-room-design",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
