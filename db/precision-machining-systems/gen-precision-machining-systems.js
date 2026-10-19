(function(){'use strict';
/* JAH Precision Machining Systems Database generator — jahdb-precision-machining-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PMS-";
var FIELDS=["cutting physics", "machine tools", "tooling", "workholding", "CNC programming", "metrology"];
var TOPICS=[
    {t: "Cutting Physics", b: "Shear zones, chip formation, cutting forces: Merchant's model relating speed, feed, and tool geometry to forces."},
    {t: "Tool Materials", b: "High-speed steel, carbide, ceramic, CBN, diamond: hardness vs toughness per workpiece material."},
    {t: "Tool Wear", b: "Flank, crater, built-up edge: wear mechanisms and Taylor's tool-life equation (VT^n = C) scheduling changes."},
    {t: "Machine Tool Design", b: "Beds, ways, spindles, ballscrews: the stiffness and thermal loop determining what the machine can hold."},
    {t: "CNC Controls", b: "G-code, interpolation, look-ahead: the control theory inside every machining center."},
    {t: "Milling Strategies", b: "Climb vs conventional, trochoidal, high-efficiency milling: toolpaths balancing speed against tool life."},
    {t: "Turning", b: "Lathes and Swiss-types: the rotational processes making shafts, threads, and precision bores."},
    {t: "Grinding", b: "Abrasive machining for sub-micron finishes and hardened steels: wheel specification as its own science."},
    {t: "Workholding", b: "Vises, chucks, fixtures, vacuum: holding without distorting \u2014 the most underestimated half of precision."},
    {t: "5-Axis Machining", b: "Simultaneous contouring of complex geometry: kinematics, collision avoidance, and the parts it unlocks."},
    {t: "Metrology", b: "CMMs, indicators, surface plates, interferometers: the measurement chain proving every tolerance."},
    {t: "Process Control", b: "SPC, capability indices (Cp/Cpk), and in-process probing: keeping processes centered over production runs."}
];
var PRINCIPLES=[
    {n: "Rigidity is accuracy", e: "", s: "The machine-tool loop (tool-workpiece stiffness) decides achievable tolerance more than the control does."},
    {n: "Heat is the enemy", e: "", s: "Thermal growth dwarfs many tolerances: temperature control and compensation are precision's price."},
    {n: "Measure to prove", e: "", s: "CMM, interferometry, and SPC: tolerance without measurement is a wish."}
];
var USES=["Selecting cutting parameters", "Specifying machine tools", "Designing fixtures", "Proving tolerances with metrology"];
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
    id:id, t:tp.t, g:field, name:"Precision Machining Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Precision Machining Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-precision-machining-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-precision-machining-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("precision-machining-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
