(function(){'use strict';
/* JAH Fundamentals of Control Theory Database generator — jahdb-fundamental-control-theory-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CT-";
var FIELDS=["feedback concepts", "system modeling", "stability", "PID control", "frequency response", "state-space methods"];
var TOPICS=[
    {t: "Open Loop vs Closed Loop", b: "Open-loop control acts blind (a toaster timer); closed-loop control measures the result and corrects (a thermostat) \u2014 feedback is the whole difference."},
    {t: "The Feedback Idea", b: "Measure the output, compare to the goal, and drive the error toward zero: this single loop underlies cruise control, autopilots, and blood-sugar regulation."},
    {t: "Modeling Dynamic Systems", b: "Differential equations capture how systems evolve; the transfer function G(s) = output/input in the Laplace domain turns calculus into algebra."},
    {t: "First and Second Order Responses", b: "First-order systems creep exponentially to target; second-order systems can overshoot and ring like a spring \u2014 damping ratio tells which."},
    {t: "Stability: Will It Blow Up", b: "A system is stable if bounded inputs give bounded outputs; poles in the right half-plane mean exponentially growing oscillation \u2014 always forbidden."},
    {t: "Routh-Hurwitz and Root Locus", b: "Algebraic tests (Routh-Hurwitz) and graphical ones (root locus) reveal stability without solving differential equations."},
    {t: "PID: The Workhorse Controller", b: "Proportional reacts now, integral kills lingering error, derivative anticipates: tuned PID runs most of the world's industrial loops."},
    {t: "Tuning PID in Practice", b: "Ziegler-Nichols and relay methods find workable gains experimentally; anti-windup keeps the integrator from saturating during large moves."},
    {t: "Frequency Response and Bode Plots", b: "Driving a system with sine waves of rising frequency reveals gain and phase margins \u2014 the standard robustness check before deployment."},
    {t: "State-Space Control", b: "Representing systems as \u1e8b = Ax + Bu unlocks modern methods: pole placement, observers, and optimal LQR control for multivariable plants."},
    {t: "Digital and Sampled Control", b: "Computers control in discrete steps; sampling must respect Nyquist, and discretization turns continuous designs into difference equations."},
    {t: "Nonlinear and Adaptive Control", b: "Real systems saturate and change: gain scheduling, sliding-mode, and adaptive controllers extend control beyond linear assumptions."}
];
var PRINCIPLES=[
    {n: "PID control law", e: "u = Kp\u00b7e + Ki\u00b7\u222be + Kd\u00b7de/dt", s: "Proportional, integral, and derivative terms combine to drive error to zero."},
    {n: "Closed-loop transfer", e: "T = G / (1 + G\u00b7H)", s: "Feedback divides the open-loop response by one plus the loop gain."},
    {n: "Stability condition", e: "all poles in left half-plane", s: "A linear system is stable exactly when every pole has negative real part."}
];
var USES=["Tuning industrial temperature and pressure loops", "Building drone and aircraft autopilots", "Stabilizing power grids", "Regulating insulin pumps and prosthetics"];
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
    id:id, t:tp.t, g:field, name:"Control Theory"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Control Theory demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-control-theory-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-control-theory-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-control-theory",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
