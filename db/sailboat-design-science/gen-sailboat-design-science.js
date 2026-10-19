(function(){'use strict';
/* JAH Sailboat Design Science Database generator — jahdb-sailboat-design-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SDS-";
var FIELDS=["hull design", "sail aerodynamics", "stability", "keels and rudders", "rigging", "performance prediction"];
var TOPICS=[
    {t: "How Sails Work", b: "Angle of attack, lift, and drag on cambered airfoils: beating to windward is tacking across the wind's eye."},
    {t: "Points of Sail", b: "Close-hauled to running: sail trim, apparent wind, and polar diagrams for every angle."},
    {t: "Hull Hydrodynamics", b: "Wave-making resistance, frictional drag, form drag: why long thin hulls slip through water efficiently."},
    {t: "Hull Speed", b: "1.34 \u00d7 \u221awaterline length: the wave-trap limiting displacement hulls \u2014 and how planing hulls escape it."},
    {t: "Stability", b: "Form stability (beam) vs ballast stability (keel): righting-moment curves and the angle of vanishing stability."},
    {t: "Keels and Rudders", b: "Fin keels with bulbs, spade rudders: underwater foils balancing the sail plan's forces."},
    {t: "Rig Types", b: "Sloop, cutter, ketch: sail plans balancing power, handling, and crew demands."},
    {t: "Sail Materials", b: "Dacron to carbon laminates: stretch resistance holding airfoil shape under load."},
    {t: "Velocity Prediction Programs", b: "VPPs integrating aero and hydro models: the software behind racing ratings and design optimization."},
    {t: "Foiling", b: "America's Cup foils lifting hulls clear: 50-knot sailing by eliminating hydrodynamic drag."},
    {t: "Cruising Design", b: "Tankage, motion comfort, and systems independence: the liveaboard engineering racers ignore."},
    {t: "Seamanship Systems", b: "Reefing, storm tactics, and self-steering: the operational knowledge completing the design."}
];
var PRINCIPLES=[
    {n: "Lift drives, drag limits", e: "", s: "Sails are wings, keels are underwater wings: the boat is two lifting surfaces fighting each other's drag."},
    {n: "Stability is righting moment", e: "", s: "Ballast times lever arm vs heeling moment: the physics keeping the mast up."},
    {n: "Displacement sets the speed limit", e: "", s: "Hull speed \u2248 1.34\u221aLWL: waterline length caps displacement sailing \u2014 planing and foiling break the rule."}
];
var USES=["Designing cruising sailboats", "Optimizing racing sail plans", "Analyzing stability", "Predicting boat performance"];
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
    id:id, t:tp.t, g:field, name:"Sailboat Design Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Sailboat Design Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-sailboat-design-science-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-sailboat-design-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("sailboat-design-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
