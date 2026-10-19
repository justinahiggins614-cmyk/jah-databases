(function(){'use strict';
/* JAH Fundamentals of Classical Mechanics Database generator — jahdb-fundamental-classical-mechanics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CM2-";
var FIELDS=["kinematics", "Newton's laws", "work and energy", "momentum", "rotation", "Lagrangian mechanics"];
var TOPICS=[
    {t: "Kinematics: Describing Motion", b: "Position, velocity, acceleration as vectors and their calculus relations: the language before the laws."},
    {t: "Newton's Three Laws", b: "Inertia, F = ma, action-reaction: three statements that predicted everything from tides to planets for 200 years."},
    {t: "Friction and Drag", b: "Real motion fights \u03bcN friction and \u00bd\u03c1v\u00b2CdA drag \u2014 why the ideal laws need these corrections to match the world."},
    {t: "Work and Kinetic Energy", b: "Work is force through distance; the work-energy theorem (W_net = \u0394K) turns dynamics into bookkeeping."},
    {t: "Potential Energy", b: "Gravity (mgh) and springs (\u00bdkx\u00b2) store work as configuration \u2014 conservative forces make energy accounting possible."},
    {t: "Conservation Laws", b: "Energy, momentum, angular momentum conserved when symmetries hold (Noether's theorem): the deepest truths in mechanics."},
    {t: "Momentum and Collisions", b: "Impulse changes momentum; elastic collisions conserve kinetic energy too \u2014 the analysis behind crash safety and billiards."},
    {t: "Rotation", b: "Torque is rotational force, moment of inertia is rotational mass: \u03c4 = I\u03b1 mirrors F = ma for spinning bodies."},
    {t: "Angular Momentum", b: "Ice skaters spin faster pulling in arms because L = I\u03c9 is conserved \u2014 the same law stabilizing bicycles and planets."},
    {t: "Oscillations", b: "Springs and pendulums obey x\u0308 = \u2212\u03c9\u00b2x: simple harmonic motion is nature's favorite vibration, from atoms to bridges."},
    {t: "Gravity and Orbits", b: "Newton's 1/r\u00b2 law plus F = ma yields Kepler's ellipses: the same physics drops apples and steers spacecraft."},
    {t: "Lagrangian Mechanics", b: "Minimizing action S = \u222bL dt reproduces Newton's laws in any coordinates \u2014 the formulation that generalizes to all of physics."}
];
var PRINCIPLES=[
    {n: "Newton's second law", e: "F = m\u00b7a", s: "Force equals mass times acceleration \u2014 the equation that launched modern physics."},
    {n: "Conservation of energy", e: "E_total = constant (isolated)", s: "Energy's constancy constrains every possible motion."},
    {n: "Euler-Lagrange", e: "d/dt(\u2202L/\u2202q\u0307) \u2212 \u2202L/\u2202q = 0", s: "Stationary action generates the equations of motion for any coordinates."}
];
var USES=["Designing vehicle suspensions", "Planning spacecraft trajectories", "Analyzing structural vibrations", "Engineering amusement rides"];
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
    id:id, t:tp.t, g:field, name:"Classical Mechanics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Classical Mechanics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-classical-mechanics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-classical-mechanics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-classical-mechanics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
