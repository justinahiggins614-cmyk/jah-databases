(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["logs", "recordings", "traces", "reports", "audit"];
var PREFIX='JAH-RAO-';
var USE="Used by safety investigators, insurers, and regulators reconstructing robot incidents.";
var FLD=[["evidence", "Evidence"], ["captures", "Captures"], ["retention", "Retention"]];
var DEMO="# {title} - evidence completeness (python3)\npresent={d1}\nrequired={d2}\nmin_pct={d3}\npct=100.0*present/required\nprint(\"evidence items: %d/%d (%.0f%%)\" % (present, required, pct))\nprint(\"COMPLETE\" if pct >= min_pct else \"INCOMPLETE\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["logs", "Telemetry Log", "Time-stamped joint states, velocities, and commands at full rate.", "Telemetry Log", "motion truth", "2 years", "48", "50", "90.0"], ["recordings", "Video Recording", "Onboard camera footage synchronized to telemetry.", "Video Recording", "visual context", "1 year", "45", "50", "85.0"], ["traces", "Event Log", "Discrete events: mode changes, faults, operator inputs.", "Event Log", "state changes", "2 years", "49", "50", "95.0"], ["reports", "Decision Trace", "The planner's options, costs, and chosen action at each decision.", "Decision Trace", "why it acted", "2 years", "42", "50", "80.0"], ["audit", "Sensor Snapshot", "Raw sensor frames captured around anomalies for forensics.", "Sensor Snapshot", "ground truth", "1 year", "40", "50", "75.0"], ["logs", "Map Diff", "Changes the robot made to its map during the mission.", "Map Diff", "world updates", "2 years", "44", "50", "85.0"], ["recordings", "Incident Report", "Structured report filed automatically when safety thresholds trip.", "Incident Report", "incidents", "7 years", "38", "40", "90.0"], ["traces", "Operator Override Log", "Every human takeover with timestamp, reason, and resulting command.", "Operator Override Log", "interventions", "2 years", "47", "50", "90.0"], ["reports", "Performance Metrics", "Task success, cycle time, and energy per mission for trend analysis.", "Performance Metrics", "KPIs", "3 years", "46", "50", "90.0"], ["audit", "Anomaly Flags", "Detector outputs marking unusual sensor or behavior patterns.", "Anomaly Flags", "early warnings", "2 years", "43", "50", "80.0"], ["logs", "Calibration Records", "When each sensor was last calibrated and the resulting parameters.", "Calibration Records", "trust basis", "life of robot", "50", "50", "100.0"], ["recordings", "Software Version Manifest", "Exact software, model, and config versions running during the mission.", "Software Version Manifest", "reproducibility", "7 years", "49", "50", "95.0"], ["traces", "Mission Plan", "The task plan as approved before execution.", "Mission Plan", "intent", "2 years", "48", "50", "95.0"], ["reports", "Execution Timeline", "Planned vs actual timing per mission phase.", "Execution Timeline", "schedule adherence", "2 years", "45", "50", "85.0"], ["audit", "Communication Log", "Messages sent and received, including dropouts and retries.", "Communication Log", "connectivity", "1 year", "41", "50", "75.0"], ["logs", "Power Profile", "Battery voltage, current, and temperature over the mission.", "Power Profile", "energy truth", "2 years", "44", "50", "85.0"], ["recordings", "Safety Interlock Log", "Every interlock engagement with cause and release.", "Safety Interlock Log", "safety events", "7 years", "39", "40", "95.0"], ["traces", "Maintenance History", "Repairs, part swaps, and inspections across the robot's life.", "Maintenance History", "health", "life of robot", "50", "50", "100.0"], ["reports", "Witness Statement", "Human observations recorded after an incident.", "Witness Statement", "context", "7 years", "30", "40", "70.0"], ["audit", "Audit Trail", "Tamper-evident hash-chained log of all the above for legal defensibility.", "Audit Trail", "integrity", "7 years", "48", "50", "95.0"]];
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
var gen={version:'jahdb-robot-autonomous-operation-evidence-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('robot-autonomous-operation-evidence',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
