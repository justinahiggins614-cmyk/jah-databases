(function(){'use strict';
/* JAH Waiting-Time Management Database generator — jahdb-waiting-time-management-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WAITTMS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Mapping Your Waiting Time (Signature Edition)", "The Waiting Kit (Signature Edition)", "The Micro-Task List (Signature Edition)", "Appointment Buffer Strategy (Signature Edition)", "Queue Tactics (Signature Edition)", "Hold Music Productivity (Signature Edition)", "Traffic and Transit Waits (Signature Edition)", "The Waiting Mindset (Signature Edition)", "Waiting With Kids (Signature Edition)", "Medical Office Waits (Signature Edition)", "Government Office Waits (Signature Edition)"], "Compounded": ["Airport and Travel Delays (Signature Edition)", "The Fifteen-Minute Learning Block (Signature Edition)", "Reading in Fragments (Signature Edition)", "Audio Learning Systems (Signature Edition)", "Planning During Waits (Signature Edition)", "Correspondence Bursts (Signature Edition)", "Exercise in Small Waits (Signature Edition)", "Social Waiting (Signature Edition)", "Digital Queue Tools (Signature Edition)", "Negotiating Wait Times (Signature Edition)", "Waiting and Deadlines (Signature Edition)", "The Waiting Audit (Signature Edition)"], "Advanced": ["Teaching Kids to Wait (Signature Edition)", "Long-Delay Contingency Plans (Signature Edition)", "Waiting as Rest (Signature Edition)", "Group and Family Coordination (Signature Edition)", "Seasonal and Event Waits (Signature Edition)", "Professional Waiting Rooms (Signature Edition)", "Emergency Room Triage Waits (Signature Edition)", "The Annual Waiting Review (Signature Edition)", "Waiting During Travel Connections (Signature Edition)", "Complaint and Feedback Loops (Signature Edition)", "The Zero-Wait Lifestyle Design (Signature Edition)"]};
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
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"waiting-time-management-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-waiting-time-management-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("waiting-time-management-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
