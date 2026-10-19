(function(){'use strict';
/* JAH Waiting-Time Management Database generator — jahdb-waiting-time-management-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WAITTM-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Mapping Your Waiting Time", "The Waiting Kit", "The Micro-Task List", "Appointment Buffer Strategy", "Queue Tactics", "Hold Music Productivity", "Traffic and Transit Waits", "The Waiting Mindset", "Waiting With Kids", "Medical Office Waits", "Government Office Waits"], "Compounded": ["Airport and Travel Delays", "The Fifteen-Minute Learning Block", "Reading in Fragments", "Audio Learning Systems", "Planning During Waits", "Correspondence Bursts", "Exercise in Small Waits", "Social Waiting", "Digital Queue Tools", "Negotiating Wait Times", "Waiting and Deadlines", "The Waiting Audit"], "Advanced": ["Teaching Kids to Wait", "Long-Delay Contingency Plans", "Waiting as Rest", "Group and Family Coordination", "Seasonal and Event Waits", "Professional Waiting Rooms", "Emergency Room Triage Waits", "The Annual Waiting Review", "Waiting During Travel Connections", "Complaint and Feedback Loops", "The Zero-Wait Lifestyle Design"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — waiting strategy demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — waiting strategy',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A waiting strategy of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"waiting-time-management-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-waiting-time-management-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("waiting-time-management",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
