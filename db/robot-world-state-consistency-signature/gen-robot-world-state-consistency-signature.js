(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["objects", "poses", "physics", "semantics", "temporal"];
var PREFIX='JAH-RWS-S-';
var USE="Used by robot perception and planning teams to catch hallucinations before acting on them.";
var FLD=[["check", "Check"], ["invariant", "Invariant"], ["on_violation", "On violation"]];
var DEMO="# {title} - check pass rate (python3)\nchecks={d1}\nfailed={d2}\nmax_fail={d3}\nprint(\"failed checks: %d/%d\" % (failed, checks))\nprint(\"WORLD MODEL OK\" if failed <= max_fail else \"RELOCALIZE\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["objects", "Object Permanence", "Objects continue to exist when occluded; tracks persist through brief hiding.", "Object Permanence", "exists when unseen", "keep track alive", "200", "3", "5"], ["poses", "Pose Continuity", "Object poses change smoothly; teleportation indicates a tracking error.", "Pose Continuity", "smooth motion", "flag jump", "500", "8", "10"], ["physics", "Collision-free State", "No two solid objects interpenetrate in the world model.", "Collision-free State", "no overlap", "resolve or replan", "150", "2", "4"], ["semantics", "Support Relation", "Every object rests on a support or is held; floating objects are errors.", "Support Relation", "supported", "find support", "120", "4", "6"], ["temporal", "Grasp Stability", "A held object moves rigidly with the gripper; slip triggers regrasp.", "Grasp Stability", "rigid attach", "regrasp", "80", "5", "8"], ["objects", "Kinematic Feasibility", "Planned arm configurations respect joint limits and reachability.", "Kinematic Feasibility", "reachable", "replan", "300", "6", "10"], ["poses", "Joint Limit Respect", "Commanded joints never exceed software limits.", "Joint Limit Respect", "within limits", "clamp + warn", "400", "2", "5"], ["physics", "Velocity Bound", "No part of the robot exceeds its rated speed.", "Velocity Bound", "speed caps", "slow down", "350", "7", "12"], ["semantics", "Occlusion Reasoning", "The model explains missing detections by known occluders before deleting tracks.", "Occlusion Reasoning", "explained absence", "keep occluded tracks", "180", "6", "10"], ["temporal", "Multi-view Agreement", "Cameras observing the same object agree on its pose within tolerance.", "Multi-view Agreement", "consistent poses", "fuse or flag", "220", "5", "8"], ["objects", "Temporal Coherence", "World state evolves consistently with the last state plus applied actions.", "Temporal Coherence", "causal update", "rollback", "600", "9", "15"], ["poses", "Semantic Label Stability", "Object labels do not flicker between frames without cause.", "Semantic Label Stability", "stable labels", "smooth labels", "250", "10", "15"], ["physics", "Count Conservation", "The number of tracked objects changes only via observed entry/exit.", "Count Conservation", "conserved count", "audit", "100", "3", "5"], ["semantics", "Containment Logic", "Objects inside containers move with them; contents are listed, not lost.", "Containment Logic", "nested state", "update container", "90", "4", "6"], ["temporal", "Attachment Graph", "Grasp and assembly attachments form a consistent tree with no cycles.", "Attachment Graph", "acyclic graph", "break cycle", "70", "2", "4"], ["objects", "Force Closure", "Grasps satisfy force closure so the object cannot escape the fingers.", "Force Closure", "stable grasp", "regrasp", "60", "6", "10"], ["poses", "Reachability", "Target poses are within the arm's reachable workspace.", "Reachability", "in workspace", "move base or reject", "200", "5", "8"], ["physics", "Map Alignment", "Live sensor data aligns with the stored map within tolerance.", "Map Alignment", "aligned", "relocalize", "150", "7", "12"], ["semantics", "Dynamic Obstacle Update", "Moving obstacles refresh fast enough that plans never go stale.", "Dynamic Obstacle Update", "fresh obstacles", "replan", "400", "8", "12"], ["temporal", "Belief Convergence", "Uncertainty shrinks with more observations; growing uncertainty triggers caution.", "Belief Convergence", "converging", "slow down", "120", "4", "8"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-robot-world-state-consistency-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('robot-world-state-consistency-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
