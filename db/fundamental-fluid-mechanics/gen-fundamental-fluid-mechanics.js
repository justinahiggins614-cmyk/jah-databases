(function(){'use strict';
/* JAH Fundamentals of Fluid Mechanics Database generator — jahdb-fundamental-fluid-mechanics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FM-";
var FIELDS=["fluid statics", "pressure and buoyancy", "viscosity", "Bernoulli and energy", "pipe flow", "turbulence and drag"];
var TOPICS=[
    {t: "What Counts as a Fluid", b: "Fluids are substances that flow under any shear stress: liquids keep volume while gases expand to fill containers \u2014 both obey the same motion laws."},
    {t: "Pressure in Still Fluids", b: "Pressure acts equally in all directions at a point and grows with depth; dams are thicker at the base because water pressure doubles every 10 meters of depth."},
    {t: "Buoyancy and Archimedes", b: "A submerged body feels an upward force equal to the weight of displaced fluid \u2014 the reason steel ships float and balloons rise."},
    {t: "Viscosity: Fluid Friction", b: "Viscosity is internal friction between fluid layers; honey pours slowly because its viscosity is thousands of times water's."},
    {t: "Bernoulli's Principle", b: "Faster flow means lower pressure: the trade-off that lifts airplane wings, curves baseballs, and atomizes perfume in sprayers."},
    {t: "Continuity: What Goes In Comes Out", b: "Incompressible flow through a pipe speeds up where the pipe narrows (A\u2081v\u2081 = A\u2082v\u2082) \u2014 the physics behind nozzles and Venturi meters."},
    {t: "Laminar vs Turbulent Flow", b: "Below Reynolds number ~2300 in pipes, flow is smooth and layered; above it, chaotic eddies dominate and friction jumps."},
    {t: "Pipe Flow and Head Loss", b: "Friction steals pressure along pipes (Darcy\u2013Weisbach); engineers size pumps to overcome it in water systems and oil pipelines."},
    {t: "Drag and Lift", b: "Drag resists motion through fluid while lift acts perpendicular; streamlining cuts drag, which is why cars, planes, and swimsuits are shaped as they are."},
    {t: "Boundary Layers", b: "Fluid sticks to surfaces (no-slip), creating a thin slow layer where most friction and heat transfer happen \u2014 the key to aircraft and ship design."},
    {t: "Compressible Flow", b: "Near the speed of sound, air itself compresses: shock waves form, drag spikes, and jet inlets must be shaped for supersonic physics."},
    {t: "Dimensional Analysis", b: "Dimensionless numbers (Reynolds, Mach, Froude) let small model tests predict full-scale ships, planes, and dams reliably."}
];
var PRINCIPLES=[
    {n: "Hydrostatic pressure", e: "P = \u03c1 * g * h", s: "Pressure in a still fluid grows linearly with depth."},
    {n: "Bernoulli's equation", e: "P + \u00bd\u03c1v\u00b2 + \u03c1gh = constant", s: "Along a streamline, pressure trades off against speed and elevation."},
    {n: "Reynolds number", e: "Re = \u03c1 * v * D / \u03bc", s: "The dimensionless ratio of inertial to viscous forces predicts laminar vs turbulent flow."}
];
var USES=["Sizing water pipes and pumps", "Shaping airplane wings and car bodies", "Designing dams and spillways", "Predicting weather and ocean currents"];
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
    id:id, t:tp.t, g:field, name:"Fluid Mechanics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Fluid Mechanics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-fluid-mechanics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-fluid-mechanics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-fluid-mechanics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
