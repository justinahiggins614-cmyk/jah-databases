(function(){'use strict';
/* JAH controlled-vocabulary-management-signature generator — jahdb-controlled-vocabulary-management-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CVMS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Controlled Vocabulary Management (Signature Edition)", "Core Concepts of Controlled Vocabulary Management (Signature Edition)", "Essential Vocabulary for Controlled Vocabulary Management (Signature Edition)", "Your First Controlled Vocabulary Management Project (Signature Edition)", "Beginner Mistakes in Controlled Vocabulary Management (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Controlled Vocabulary Management (Signature Edition)", "Myths vs. Facts in Controlled Vocabulary Management (Signature Edition)", "When to Start Controlled Vocabulary Management (Signature Edition)", "Measuring the Basics in Controlled Vocabulary Management (Signature Edition)", "Safety First in Controlled Vocabulary Management (Signature Edition)", "Where to Find Help with Controlled Vocabulary Management (Signature Edition)"], "Compounded": ["The Controlled Vocabulary Management Workflow, Step by Step (Signature Edition)", "A Controlled Vocabulary Management Decision Framework (Signature Edition)", "Controlled Vocabulary Management Cost and Budget Planning (Signature Edition)", "Scheduling Controlled Vocabulary Management Work (Signature Edition)", "Quality Checks for Controlled Vocabulary Management (Signature Edition)", "Controlled Vocabulary Management Troubleshooting Guide (Signature Edition)", "Intermediate Controlled Vocabulary Management Skills (Signature Edition)", "Controlled Vocabulary Management in Real-World Cases (Signature Edition)", "Comparing Controlled Vocabulary Management Options (Signature Edition)", "Documenting Your Controlled Vocabulary Management Work (Signature Edition)", "Collaborating on Controlled Vocabulary Management (Signature Edition)", "Scaling Up Controlled Vocabulary Management (Signature Edition)"], "Advanced": ["Advanced Controlled Vocabulary Management Techniques (Signature Edition)", "Controlled Vocabulary Management Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Controlled Vocabulary Management (Signature Edition)", "Automating Controlled Vocabulary Management (Signature Edition)", "Controlled Vocabulary Management Long-Term Strategy (Signature Edition)", "Teaching Controlled Vocabulary Management to Others (Signature Edition)", "Ethics and Responsibility in Controlled Vocabulary Management (Signature Edition)", "Integrating Controlled Vocabulary Management with Other Systems (Signature Edition)", "The Controlled Vocabulary Management Frontier: What Comes Next (Signature Edition)", "The Controlled Vocabulary Management Master Checklist (Signature Edition)", "Controlled Vocabulary Management Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"controlled-vocabulary-management-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-controlled-vocabulary-management-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("controlled-vocabulary-management-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
