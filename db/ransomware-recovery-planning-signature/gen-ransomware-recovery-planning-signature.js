(function(){'use strict';
/* JAH ransomware-recovery-planning-signature generator — jahdb-ransomware-recovery-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RRPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Ransomware Recovery Planning (Signature Edition)", "Core Concepts of Ransomware Recovery Planning (Signature Edition)", "Essential Vocabulary for Ransomware Recovery Planning (Signature Edition)", "Your First Ransomware Recovery Planning Project (Signature Edition)", "Beginner Mistakes in Ransomware Recovery Planning (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Ransomware Recovery Planning (Signature Edition)", "Myths vs. Facts in Ransomware Recovery Planning (Signature Edition)", "When to Start Ransomware Recovery Planning (Signature Edition)", "Measuring the Basics in Ransomware Recovery Planning (Signature Edition)", "Safety First in Ransomware Recovery Planning (Signature Edition)", "Where to Find Help with Ransomware Recovery Planning (Signature Edition)"], "Compounded": ["The Ransomware Recovery Planning Workflow, Step by Step (Signature Edition)", "A Ransomware Recovery Planning Decision Framework (Signature Edition)", "Ransomware Recovery Planning Cost and Budget Planning (Signature Edition)", "Scheduling Ransomware Recovery Planning Work (Signature Edition)", "Quality Checks for Ransomware Recovery Planning (Signature Edition)", "Ransomware Recovery Planning Troubleshooting Guide (Signature Edition)", "Intermediate Ransomware Recovery Planning Skills (Signature Edition)", "Ransomware Recovery Planning in Real-World Cases (Signature Edition)", "Comparing Ransomware Recovery Planning Options (Signature Edition)", "Documenting Your Ransomware Recovery Planning Work (Signature Edition)", "Collaborating on Ransomware Recovery Planning (Signature Edition)", "Scaling Up Ransomware Recovery Planning (Signature Edition)"], "Advanced": ["Advanced Ransomware Recovery Planning Techniques (Signature Edition)", "Ransomware Recovery Planning Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Ransomware Recovery Planning (Signature Edition)", "Automating Ransomware Recovery Planning (Signature Edition)", "Ransomware Recovery Planning Long-Term Strategy (Signature Edition)", "Teaching Ransomware Recovery Planning to Others (Signature Edition)", "Ethics and Responsibility in Ransomware Recovery Planning (Signature Edition)", "Integrating Ransomware Recovery Planning with Other Systems (Signature Edition)", "The Ransomware Recovery Planning Frontier: What Comes Next (Signature Edition)", "The Ransomware Recovery Planning Master Checklist (Signature Edition)", "Ransomware Recovery Planning Capstone Review: Putting It All Together (Signature Edition)"]};
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
    description:'SAMPLE RECORD (generated — structural sample). A Signature-original sample of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"ransomware-recovery-planning-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-ransomware-recovery-planning-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ransomware-recovery-planning-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
