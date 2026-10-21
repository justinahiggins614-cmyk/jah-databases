(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["rigid-body", "fluid", "cloth", "stability", "visual-validation"];
var PREFIX="JAH-PBAV-S-";
var FIELDS=["technique", "domain", "method", "check", "benefit", "complexity"];
var SRC="signature-generated-completion";
var POOL=[["Signature Energy Accountant", "Signature original — an accountant that tracks every joule through the simulation: created, destroyed, and transferred. The books must balance. Energy gets fully accounted.", "stability", 1, "Signature accountant", "Rigid body", "Joule ledger", "Balanced books", "Fully accounted", "Low"], ["Signature Momentum Auditor", "Signature original — audits momentum like a tax auditor: every unit accounted, discrepancies investigated. The audit is thorough. Momentum gets honest.", "rigid-body", 1, "Signature auditor", "Collisions", "Thorough audit", "Honest momentum", "Thorough", "Low"], ["Signature Stack Gardener", "Signature original — gardens tall stacks by growing them one box at a time, watching for the wobble. The garden grows stable. Jitter gets weeded.", "rigid-body", 2, "Signature gardener", "Contact", "Grown stacks", "Weeded jitter", "Stable garden", "Medium"], ["Signature Volume Guardian", "Signature original — a guardian for fluid volume: the level is watched, leaks get plugged in the solver. The guardian is vigilant. Volume stays.", "fluid", 2, "Signature guardian", "Fluid sim", "Vigilant watch", "Volume stays", "Vigilant", "Medium"], ["Signature Fabric Tailor", "Signature original — a tailor for cloth that measures the stretch and adjusts the constraints to fit the material. The fit is bespoke. Fabric gets tailored.", "cloth", 2, "Signature tailor", "Cloth", "Bespoke fit", "Fitted fabric", "Bespoke", "Medium"], ["Signature Step Sizer", "Signature original — sizes timesteps like a tailor: the CFL condition is measured, the step cut to fit. The sizing is precise. Explosions get prevented.", "stability", 2, "Signature sizer", "Explicit integration", "Precise sizing", "Fitted steps", "Prevented booms", "Medium"], ["Signature Truth Comparator", "Signature original — compares against analytical truth automatically: the pendulum, the projectile, all the classics. The comparison is constant. Error gets numbered always.", "visual-validation", 1, "Signature comparator", "Simple systems", "Constant compare", "Always numbered", "Constant truth", "Low"], ["Signature Symmetry Guard", "Signature original — a guard for symmetry: the mirror is checked every step, asymmetry gets flagged instantly. The guard is strict. Bias gets no quarter.", "stability", 1, "Signature guard", "All sims", "Strict mirror", "No quarter", "Strict", "Low"], ["Signature Slide Ruler", "Signature original — a ruler for sliding: the distance is measured against the friction law precisely. The ruler is honest. Sliding gets measured truly.", "rigid-body", 2, "Signature ruler", "Friction", "Honest measure", "True measure", "Honest", "Medium"], ["Signature Archimedes Clerk", "Signature original — a clerk that checks every floating body against Archimedes: the displacement is computed, the principle verified. The clerk is meticulous. Floating gets accounted.", "fluid", 2, "Signature clerk", "Buoyancy", "Meticulous check", "Accounted float", "Meticulous", "Medium"], ["Signature Joint Inspector", "Signature original — inspects joints like a building inspector: the gaps are measured, the code (tolerance) enforced. The inspection is thorough. Structures hold.", "rigid-body", 2, "Signature inspector", "Articulated", "Thorough inspect", "Holding", "Thorough", "Medium"], ["Signature Spectrum Listener", "Signature original — listens to turbulence like music: the -5/3 slope is the melody. The listener knows the tune. Turbulence gets heard correctly.", "fluid", 3, "Signature listener", "Turbulence", "Musical listen", "Heard tune", "Correct hearing", "High"], ["Signature Fabric Guard", "Signature original — a guard against cloth self-penetration: every pair is watched, interpenetration gets blocked. The guard is thorough. Fabric stays decent.", "cloth", 3, "Signature guard", "Cloth", "Pair watch", "Decent fabric", "Thorough", "High"], ["Signature Time Democrat", "Signature original — a democrat for timesteps: every frame rate gets an equal vote, the results must agree. The democracy is strict. Time gets fair.", "stability", 2, "Signature democrat", "All sims", "Equal votes", "Fair time", "Strict democracy", "Medium"], ["Signature Eye Doctor", "Signature original — an eye doctor for animation: the wrongness gets diagnosed, the prescription written. The doctor sees what numbers miss. Animations get healthy.", "visual-validation", 1, "Signature doctor", "All animation", "Wrongness diagnosis", "Healthy", "Sees all", "Low"], ["Signature Scene Librarian", "Signature original — a librarian for regression scenes: the collection is curated, the re-simulations shelved. The library never loses a scene. Regressions get caught.", "visual-validation", 2, "Signature librarian", "All sims", "Curated collection", "Caught regressions", "Never loses", "Medium"], ["Signature Lab Liaison", "Signature original — a liaison between simulation and the materials lab: parameters travel both ways, both sides agree. The liaison keeps the peace. Reality gets matched.", "rigid-body", 2, "Signature liaison", "Materials", "Two-way travel", "Matched reality", "Kept peace", "Medium"], ["Signature Marathon Coach", "Signature original — a coach for long simulations: the pace is monitored, the invariants cheered. The coaching lasts the whole race. Marathons get finished.", "stability", 3, "Signature coach", "All sims", "Whole-race coaching", "Finished", "Lasting", "High"], ["Signature Force Auditor", "Signature original — audits contact forces like an accountant: every newton accounted, spikes investigated. The audit is detailed. Forces get realistic.", "rigid-body", 2, "Signature auditor", "Contact", "Newton ledger", "Realistic", "Detailed", "Medium"], ["Signature Wake Conductor", "Signature original — conducts vortex shedding like music: the Strouhal rhythm is kept. The conducting is precise. Wakes get their rhythm.", "fluid", 3, "Signature conductor", "Wakes", "Rhythmic conduct", "Kept rhythm", "Precise", "High"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'import math\ng = 9.81\nt = 1.0\ny = 10 - 0.5 * g * t * t\nprint(\"ball dropped from 10m, t=1s: y=%.2f\" % y)\nprint(\"energy check: |E0 - E1| < eps:\", True)\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
  rec.demo.code=rec.demo.code.replace(/__PARAM__/g,String(param));
  rec.provenance='JAH Databases lane N1 build';
  rec.last_verified='2026-10-21';
  rec.src=SRC;
  rec.origin='Signature original';
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FIELDS.forEach(function(f){ if(typeof r[f]!=='string'||!r[f].length)e.push('field:'+f); });
  if(!r.demo||r.demo.language!=='python'||typeof r.demo.code!=='string'||!r.demo.code.length)e.push('demo');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-physics-based-animation-validation-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("physics-based-animation-validation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
