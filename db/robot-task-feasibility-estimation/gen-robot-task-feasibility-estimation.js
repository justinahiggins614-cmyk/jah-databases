(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["capability", "resources", "environment", "safety", "readiness"];
var PREFIX='JAH-RTF-';
var USE="Used by task planners and fleet managers to accept only tasks likely to succeed.";
var FLD=[["factor", "Factor"], ["estimated_by", "Estimated by"], ["threshold", "Threshold"]];
var DEMO="# {title} - feasibility score (python3)\nscores=[{d1}, {d2}, {d3}]\navg=sum(scores)/len(scores)\nprint(\"factor scores:\", scores, \"avg=%.2f\" % avg)\nprint(\"FEASIBLE\" if avg >= 0.7 and min(scores) >= 0.4 else \"NOT FEASIBLE\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["capability", "Reachability", "Whether the target poses lie inside the arm's reachable workspace.", "Reachability", "workspace query", "all key poses", "0.9", "0.85", "0.95"], ["resources", "Payload Margin", "Whether the object mass plus tool stays under the rated payload with margin.", "Payload Margin", "mass estimate", "<= 80% rated", "0.8", "0.9", "0.75"], ["environment", "Cycle-time Budget", "Whether the task fits in the allowed time at realistic speeds.", "Cycle-time Budget", "time model", "<= budget", "0.85", "0.8", "0.9"], ["safety", "Grasp Quality", "Whether sampled grasps score above the stability threshold.", "Grasp Quality", "grasp sampler", "> 0.7 score", "0.75", "0.8", "0.7"], ["readiness", "Path Clearance", "Whether a collision-free path exists with clearance margin.", "Path Clearance", "motion planner", "> 5 cm", "0.9", "0.85", "0.8"], ["capability", "Power Budget", "Whether the task's energy fits the battery with reserve.", "Power Budget", "energy model", "<= 70% pack", "0.8", "0.85", "0.75"], ["resources", "Thermal Budget", "Whether motors stay under temperature limits for the task duration.", "Thermal Budget", "thermal model", "< limits", "0.85", "0.8", "0.9"], ["environment", "Precision Requirement", "Whether the task's tolerance exceeds the robot's repeatability.", "Precision Requirement", "spec compare", "tolerance > 3x repeatability", "0.7", "0.9", "0.8"], ["safety", "Sensor Coverage", "Whether sensors can observe the task area throughout execution.", "Sensor Coverage", "visibility check", "full coverage", "0.9", "0.8", "0.85"], ["readiness", "Communication Range", "Whether the link budget supports teleoperation or telemetry.", "Communication Range", "link model", "> 10 dB margin", "0.85", "0.9", "0.8"], ["capability", "Battery Endurance", "Whether the battery lasts the whole task plus return-to-base.", "Battery Endurance", "discharge model", "> 120% task energy", "0.8", "0.85", "0.9"], ["resources", "Compute Headroom", "Whether onboard compute handles perception and planning in real time.", "Compute Headroom", "profiling", "< 70% load", "0.75", "0.8", "0.85"], ["environment", "Environmental Tolerance", "Whether temperature, dust, and moisture stay within ratings.", "Environmental Tolerance", "env spec", "within ratings", "0.9", "0.85", "0.8"], ["safety", "Safety Margin", "Whether the task keeps required separation from people and hazards.", "Safety Margin", "safety check", "margins met", "0.95", "0.9", "0.9"], ["readiness", "Human Proximity", "Whether nearby humans change speed limits or require supervision.", "Human Proximity", "scene analysis", "per safety plan", "0.8", "0.85", "0.75"], ["capability", "Tool Availability", "Whether the right end-effector is mounted or in the tool changer.", "Tool Availability", "inventory", "tool present", "1.0", "0.9", "0.9"], ["resources", "Calibration Freshness", "Whether calibration is recent enough for the task's precision.", "Calibration Freshness", "cal log", "< interval", "0.85", "0.9", "0.8"], ["environment", "Software Compatibility", "Whether the task's skill version matches the deployed stack.", "Software Compatibility", "version check", "compatible", "0.9", "0.95", "0.9"], ["safety", "Regulatory Clearance", "Whether the task is permitted in this jurisdiction and site.", "Regulatory Clearance", "permits", "cleared", "1.0", "0.9", "0.95"], ["readiness", "Fallback Existence", "Whether a safe fallback exists if the task fails midway.", "Fallback Existence", "plan B", "fallback defined", "0.8", "0.85", "0.75"]];
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
var gen={version:'jahdb-robot-task-feasibility-estimation-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('robot-task-feasibility-estimation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
