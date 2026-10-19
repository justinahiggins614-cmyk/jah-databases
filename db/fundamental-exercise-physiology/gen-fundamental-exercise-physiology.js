(function(){'use strict';
/* JAH Fundamentals of Exercise Physiology Database generator — jahdb-fundamental-exercise-physiology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EP-";
var FIELDS=["muscle physiology", "cardiovascular response", "respiratory response", "energy systems", "training adaptation", "environment and fatigue"];
var TOPICS=[
    {t: "Muscle Fiber Types", b: "Slow-twitch fibers endure, fast-twitch fibers explode: training shifts the mix and every sport selects its fibers."},
    {t: "How Muscles Contract", b: "Motor neurons fire, calcium floods the sarcomere, myosin cross-bridges cycle \u2014 the sliding-filament engine of all movement."},
    {t: "The Three Energy Systems", b: "Phosphocreatine (seconds), glycolysis (minutes), oxidative phosphorylation (hours) layer to fund every effort from a jump to a marathon."},
    {t: "Cardiac Output During Exercise", b: "Heart rate \u00d7 stroke volume climbs from ~5 to 20+ L/min in athletes \u2014 the central pump sets the aerobic ceiling."},
    {t: "VO2max: The Aerobic Ceiling", b: "Maximum oxygen uptake integrates lungs, heart, blood, and muscle; trainable by ~15\u201325%, largely set by genetics."},
    {t: "Lactate Threshold", b: "The pace where lactate accumulates marks sustainable intensity \u2014 the single best predictor of endurance performance."},
    {t: "Strength Adaptation", b: "Early strength gains are neural (better recruitment); lasting gains add muscle protein \u2014 hypertrophy follows tension and volume."},
    {t: "Endurance Adaptation", b: "Mitochondria multiply, capillaries grow, and fat oxidation rises: the cellular renovations behind every trained athlete."},
    {t: "Heat, Altitude, and Environment", b: "Heat strains cooling, altitude thins oxygen, cold raises cost \u2014 acclimatization protocols buy back performance."},
    {t: "Fatigue Mechanisms", b: "Central (brain) and peripheral (muscle) fatigue interact; glycogen depletion, heat, and dehydration each pull the plug differently."},
    {t: "Recovery Science", b: "Sleep, protein timing, and load management rebuild what training breaks; adaptation happens during recovery, not during the workout."},
    {t: "Exercise Prescription", b: "FITT \u2014 frequency, intensity, time, type \u2014 plus progression turns physiology into programs for health, sport, and rehab."}
];
var PRINCIPLES=[
    {n: "Fick principle", e: "VO2 = Q \u00d7 (a\u2212v)O2 difference", s: "Oxygen uptake equals cardiac output times tissue extraction \u2014 the master equation of aerobic fitness."},
    {n: "Sliding filament", e: "force \u221d cross-bridge cycling", s: "Muscles shorten as myosin heads ratchet along actin \u2014 calcium-gated contraction."},
    {n: "Overload principle", e: "adaptation follows progressive overload", s: "Fitness improves only when training stress exceeds accustomed levels, then recovers."}
];
var USES=["Designing endurance training plans", "Building strength programs", "Prescribing exercise for health", "Managing heat and altitude exposure"];
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
    id:id, t:tp.t, g:field, name:"Exercise Physiology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Exercise Physiology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-exercise-physiology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-exercise-physiology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-exercise-physiology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
