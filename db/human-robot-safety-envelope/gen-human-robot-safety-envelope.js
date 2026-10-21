(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["monitoring", "limiting", "stopping", "sensing", "procedures"];
var PREFIX='JAH-HRSE-';
var USE="Used by robotics integrators and safety engineers certifying collaborative robot cells.";
var FLD=[["envelope", "Envelope"], ["standard", "Standard"], ["limit", "Limit"]];
var DEMO="# {title} - protective separation distance (python3)\nv={d1}\nT={d2}\nmin_d={d3}\nC=0.5\nS=v*T + C\nprint(\"required separation: %.2f m\" % S)\nprint(\"SAFE\" if S <= min_d else \"INCREASE SEPARATION\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["monitoring", "Speed and Separation Monitoring", "Slows or stops the robot based on the measured distance to the nearest human.", "Speed and Separation Monitoring", "ISO/TS 15066", "speed scales with separation", "1.5", "0.5", "2.0"], ["limiting", "Power and Force Limiting", "Caps contact force and pressure so any accidental touch stays below pain thresholds.", "Power and Force Limiting", "ISO/TS 15066", "150 N transient, 80 N quasi-static", "1.0", "0.3", "1.5"], ["stopping", "Safety-Rated Monitored Stop", "Halts the robot in a monitored standstill that resumes only when the area is clear.", "Safety-Rated Monitored Stop", "ISO 10218", "stop category 2", "0.8", "0.4", "1.2"], ["sensing", "Hand Guiding", "Lets operators physically guide the robot at reduced speed with an enabling device held.", "Hand Guiding", "ISO 10218", "250 mm/s max", "0.25", "0.2", "0.8"], ["procedures", "Protective Stop", "Triggers a controlled stop on any safety-violation signal before harm can occur.", "Protective Stop", "ISO 10218", "stop category 1", "2.0", "0.3", "2.5"], ["monitoring", "Reduced Speed Mode", "Caps TCP speed during teaching and maintenance so operators can stay close.", "Reduced Speed Mode", "ISO 10218", "250 mm/s", "0.25", "0.5", "1.0"], ["limiting", "Workspace Zoning", "Divides the cell into zones with different speed limits and access rules.", "Workspace Zoning", "ANSI/RIA R15.06", "zone-dependent", "1.2", "0.6", "2.0"], ["stopping", "Collision Force Threshold", "Sets per-body-region force limits from biomechanical data; exceeding them stops motion.", "Collision Force Threshold", "ISO/TS 15066", "body-region table", "1.0", "0.25", "1.4"], ["sensing", "Pressure Limit", "Limits contact pressure (force over area) to prevent bruising on clamping contacts.", "Pressure Limit", "ISO/TS 15066", "region-specific kPa", "0.9", "0.3", "1.3"], ["procedures", "Pinch Point Guard", "Eliminates or guards shear and pinch points where body parts could be trapped.", "Pinch Point Guard", "ISO 10218", "no accessible pinch", "0.5", "0.4", "1.0"], ["monitoring", "Emergency Stop Category 0", "Immediate power removal for the fastest stop when every millisecond counts.", "Emergency Stop Category 0", "IEC 60204-1", "uncontrolled stop", "2.5", "0.2", "3.0"], ["limiting", "Emergency Stop Category 1", "Controlled stop with power maintained for braking, then power removal.", "Emergency Stop Category 1", "IEC 60204-1", "controlled stop", "2.0", "0.35", "2.6"], ["stopping", "Enabling Device", "Three-position switch that must be deliberately held for motion in manual modes.", "Enabling Device", "IEC 60204-1", "motion only while held", "0.3", "0.3", "0.9"], ["sensing", "Presence Sensing", "Detects humans entering the cell and triggers the configured protective reaction.", "Presence Sensing", "ISO 13855", "reaction before reach", "1.4", "0.45", "2.2"], ["procedures", "Light Curtain Zone", "Optoelectronic curtain that stops the robot when a beam is broken.", "Light Curtain Zone", "IEC 61496", "muting only when safe", "1.1", "0.4", "1.8"], ["monitoring", "Laser Scanner Field", "Scans a protective field around mobile robots, slowing then stopping on intrusion.", "Laser Scanner Field", "IEC 61496", "fields per speed", "1.6", "0.5", "2.4"], ["limiting", "Torque Limiting", "Caps joint torques in software and hardware so impacts stay gentle.", "Torque Limiting", "ISO/TS 15066", "joint torque caps", "0.7", "0.3", "1.2"], ["stopping", "Soft-axis Limits", "Software joint limits inside the hard stops, keeping the arm away from singularities and people.", "Soft-axis Limits", "ISO 10218", "inside hard limits", "0.6", "0.35", "1.1"], ["sensing", "Human Detection Envelope", "Fuses vision and lidar to maintain a tracked bubble around each nearby human.", "Human Detection Envelope", "internal spec", "tracked per person", "1.3", "0.5", "2.1"], ["procedures", "Post-collision Response", "Defines the retract-and-report behavior after any contact event is detected.", "Post-collision Response", "internal spec", "retract + log", "0.4", "0.25", "1.0"]];
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
var gen={version:'jahdb-human-robot-safety-envelope-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('human-robot-safety-envelope',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
