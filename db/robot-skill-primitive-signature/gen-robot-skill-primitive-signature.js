(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["grasping", "assembly", "locomotion", "inspection", "handover"];
var PREFIX='JAH-RSP-S-';
var USE="Used by robotics engineers building task plans from reusable, tested building blocks.";
var FLD=[["primitive", "Primitive"], ["motion", "Motion"], ["sensor", "Sensor"]];
var DEMO="# {title} - cycle time and throughput (python3)\nmove={d1}\nprocess={d2}\ntarget={d3}\ncycle=move+process\nper_hour=3600.0/cycle\nprint(\"cycle: %.1fs -> %.0f/hr\" % (cycle, per_hour))\nprint(\"TARGET MET\" if per_hour >= target else \"TOO SLOW\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["grasping", "Pick", "Moves to a grasp pose, closes the gripper, and lifts the object clear.", "Pick", "approach-grasp-lift", "force + vision", "2.0", "1.0", "900"], ["assembly", "Place", "Carries a held object to a target pose and releases it precisely.", "Place", "transport-release", "vision", "2.5", "1.0", "800"], ["locomotion", "Insert", "Aligns and pushes a part into a hole or slot with compliant force control.", "Insert", "align-push", "force/torque", "3.0", "2.0", "500"], ["inspection", "Screw-driving", "Drives a screw with controlled torque and depth, detecting cross-threading.", "Screw-driving", "rotate-feed", "torque", "4.0", "3.0", "400"], ["handover", "Push", "Shoves an object along a surface to a target without grasping.", "Push", "planar push", "tactile", "2.0", "2.0", "700"], ["grasping", "Pull", "Draws an object toward the robot, e.g. opening drawers or doors.", "Pull", "pull", "force", "2.5", "1.5", "750"], ["assembly", "Grasp", "Forms a stable grasp chosen from a grasp sampler for the object shape.", "Grasp", "close fingers", "tactile", "1.5", "1.0", "1000"], ["locomotion", "Release", "Opens the gripper at the right moment with retract motion to avoid disturbance.", "Release", "open-retract", "vision", "1.0", "0.5", "1200"], ["inspection", "Wipe", "Moves a tool over a surface with constant normal force for cleaning or polishing.", "Wipe", "planar sweep", "force", "5.0", "3.0", "350"], ["handover", "Pour", "Tilts a container to pour a controlled amount using weight feedback.", "Pour", "tilt", "force/weight", "4.0", "2.0", "450"], ["grasping", "Cut", "Drives a blade along a path with feed force matched to material.", "Cut", "linear cut", "force", "3.5", "2.5", "400"], ["assembly", "Stir", "Circulates a tool in a container to mix contents uniformly.", "Stir", "circular", "torque", "6.0", "2.0", "300"], ["locomotion", "Fold", "Manipulates deformable material through a fold sequence.", "Fold", "fold trajectory", "vision", "5.0", "3.0", "350"], ["inspection", "Stack", "Places objects in a stable stack, checking alignment each layer.", "Stack", "place-check", "vision", "3.0", "2.0", "500"], ["handover", "Sort", "Classifies items by vision and routes each to its bin.", "Sort", "pick-classify-place", "vision", "2.5", "2.5", "600"], ["grasping", "Scan", "Sweeps a sensor over an area to build a map or find defects.", "Scan", "raster", "camera/lidar", "8.0", "2.0", "250"], ["assembly", "Press", "Applies controlled force along an axis, e.g. pressing connectors.", "Press", "linear press", "force", "2.0", "1.5", "800"], ["locomotion", "Twist", "Rotates a grasped object, e.g. opening jars or valves.", "Twist", "rotate", "torque", "3.0", "2.0", "500"], ["inspection", "Lift", "Raises a payload vertically with posture optimized for the load.", "Lift", "vertical lift", "force", "2.5", "1.0", "850"], ["handover", "Handover", "Transfers an object to a human with approach, offer, and release-on-grasp.", "Handover", "offer-release", "force + vision", "3.0", "2.0", "550"]];
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
var gen={version:'jahdb-robot-skill-primitive-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('robot-skill-primitive-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
