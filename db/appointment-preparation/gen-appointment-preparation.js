(function(){'use strict';
/* JAH appointment-preparation generator — jahdb-appointment-preparation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AP-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Appointment Preparation", "Core Concepts of Appointment Preparation", "Essential Vocabulary for Appointment Preparation", "Your First Appointment Preparation Project", "Beginner Mistakes in Appointment Preparation (and How to Avoid Them)", "The Tools You Need for Appointment Preparation", "Myths vs. Facts in Appointment Preparation", "When to Start Appointment Preparation", "Measuring the Basics in Appointment Preparation", "Safety First in Appointment Preparation", "Where to Find Help with Appointment Preparation"], "Compounded": ["The Appointment Preparation Workflow, Step by Step", "A Appointment Preparation Decision Framework", "Appointment Preparation Cost and Budget Planning", "Scheduling Appointment Preparation Work", "Quality Checks for Appointment Preparation", "Appointment Preparation Troubleshooting Guide", "Intermediate Appointment Preparation Skills", "Appointment Preparation in Real-World Cases", "Comparing Appointment Preparation Options", "Documenting Your Appointment Preparation Work", "Collaborating on Appointment Preparation", "Scaling Up Appointment Preparation"], "Advanced": ["Advanced Appointment Preparation Techniques", "Appointment Preparation Edge Cases and Exceptions", "Auditing and Verifying Appointment Preparation", "Automating Appointment Preparation", "Appointment Preparation Long-Term Strategy", "Teaching Appointment Preparation to Others", "Ethics and Responsibility in Appointment Preparation", "Integrating Appointment Preparation with Other Systems", "The Appointment Preparation Frontier: What Comes Next", "The Appointment Preparation Master Checklist", "Appointment Preparation Capstone Review: Putting It All Together"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — problem-solving guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — problem-solving guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A public-record sample of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"appointment-preparation-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-appointment-preparation-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("appointment-preparation",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
