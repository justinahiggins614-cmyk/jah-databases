(function(){'use strict';
/* JAH Personal Organization Database generator — jahdb-personal-organization-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PERSOS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Capture Habit (Signature Edition)", "The Master Task List (Signature Edition)", "The Two-Minute Rule (Signature Edition)", "Single Next Actions (Signature Edition)", "Calendars vs Task Lists (Signature Edition)", "The Daily Top Three (Signature Edition)", "Decluttering Surfaces (Signature Edition)", "The Inbox Zero Method (Signature Edition)", "Paper vs Digital Systems (Signature Edition)", "Weekly Review Basics (Signature Edition)", "Habit Stacking (Signature Edition)"], "Compounded": ["Time Blocking (Signature Edition)", "The Eisenhower Matrix (Signature Edition)", "Project Lists and Support Files (Signature Edition)", "Tickler Files and Reminders (Signature Edition)", "Email Triage Systems (Signature Edition)", "Context-Based Task Lists (Signature Edition)", "The PARA Method (Signature Edition)", "Routines and Checklists (Signature Edition)", "Delegation and Waiting-For Lists (Signature Edition)", "Energy Management (Signature Edition)", "Saying No Gracefully (Signature Edition)", "Travel and Errand Batching (Signature Edition)"], "Advanced": ["The Weekly Review (Full Protocol) (Signature Edition)", "Goal Decomposition Systems (Signature Edition)", "Personal Knowledge Capture (Signature Edition)", "Attention Audits (Signature Edition)", "Systems Maintenance and Pruning (Signature Edition)", "Organizing Shared Households (Signature Edition)", "Digital File Hygiene (Signature Edition)", "Long-Term Archive Strategy (Signature Edition)", "Crisis Reorganization (Signature Edition)", "Teaching Organization to Others (Signature Edition)", "The Annual Life Review (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — organization method demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — organization method',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A organization method of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"personal-organization-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-personal-organization-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("personal-organization-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
