(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["locomotion", "comfort", "wayfinding", "multi-user", "accessibility"];
var PREFIX='JAH-VIRTUA2-S-';
var USE="Used by VR designers and metaverse builders to move users without motion sickness.";
var FLD=[["technique", "Technique"], ["locomotion", "Locomotion"], ["comfort", "Comfort"]];
var DEMO="# {title} - comfort score (python3)\nscores=[{d1}, {d2}, {d3}]\navg=sum(scores)/len(scores)\nprint(\"comfort subscores:\", scores, \"avg=%.1f/10\" % avg)\nprint(\"COMFORTABLE\" if avg >= 7.0 else \"ADD COMFORT OPTIONS\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["locomotion", "Teleportation", "Jumps the user to a targeted spot, the gold standard for comfort.", "Teleportation", "discrete", "very high", "9", "9", "8"], ["comfort", "Smooth Locomotion", "Continuous thumbstick movement like a game, immersive but nausea-prone.", "Smooth Locomotion", "continuous", "low", "4", "5", "6"], ["wayfinding", "Arm-swinger", "Arm swinging propels the user; physical effort reduces sickness.", "Arm-swinger", "physical", "medium", "6", "7", "6"], ["multi-user", "Redirected Walking", "Subtly rotates the virtual world so users walk in circles physically.", "Redirected Walking", "natural walking", "high", "8", "7", "8"], ["accessibility", "Waypoint Graph", "Moves users along authored paths between points of interest.", "Waypoint Graph", "guided", "very high", "9", "8", "9"], ["locomotion", "Free-fly", "Unconstrained 3D flight for inspection and creative tools.", "Free-fly", "flight", "low", "5", "4", "5"], ["comfort", "Climbing", "Grab-and-pull climbing on marked surfaces.", "Climbing", "physical", "medium", "6", "6", "7"], ["wayfinding", "Vehicle Traversal", "Drives or flies a virtual vehicle with its own motion model.", "Vehicle Traversal", "vehicular", "medium", "6", "7", "6"], ["multi-user", "Portal Jump", "Steps through portals linking distant locations instantly.", "Portal Jump", "discrete", "high", "8", "8", "7"], ["accessibility", "Snap Turning", "Rotates view in fixed increments to avoid smooth-turn nausea.", "Snap Turning", "discrete", "high", "8", "9", "7"], ["locomotion", "Vignette Comfort", "Narrows the field of view during movement to cut vection.", "Vignette Comfort", "assist", "high", "8", "7", "8"], ["comfort", "Collision Boundaries", "Blocks walking through walls with gentle slide or fade.", "Collision Boundaries", "constraint", "high", "7", "8", "8"], ["wayfinding", "Stair Handling", "Smoothly steps users up stairs without climbing motion.", "Stair Handling", "assisted", "high", "8", "8", "7"], ["multi-user", "Elevator Zones", "Lifts users between floors in a comfortable capsule metaphor.", "Elevator Zones", "assisted", "very high", "9", "9", "8"], ["accessibility", "Map Wayfinding", "Shows a 2D/3D map with a you-are-here marker and route.", "Map Wayfinding", "UI aid", "very high", "9", "8", "9"], ["locomotion", "Minimap Aid", "Heads-up minimap keeps orientation during exploration.", "Minimap Aid", "UI aid", "very high", "9", "9", "8"], ["comfort", "Landmark Beacons", "Highlights distant landmarks to guide navigation.", "Landmark Beacons", "guidance", "very high", "9", "8", "9"], ["wayfinding", "Guided Tour Path", "Auto-tours the user through highlights with narration.", "Guided Tour Path", "guided", "very high", "10", "9", "9"], ["multi-user", "Multi-user Follow", "Lets users follow a guide's avatar through the space.", "Multi-user Follow", "social", "high", "8", "8", "7"], ["accessibility", "Accessibility Seated Mode", "Full navigation from a seated position with adjusted eye height.", "Accessibility Seated Mode", "seated", "very high", "9", "9", "9"]];
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
var gen={version:'jahdb-virtual-environment-navigation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('virtual-environment-navigation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
