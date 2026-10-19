(function(){'use strict';
/* JAH recruitment-process-design-signature generator — jahdb-recruitment-process-design-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RPDS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Recruitment Process Design (Signature Edition)", "Core Concepts of Recruitment Process Design (Signature Edition)", "Essential Vocabulary for Recruitment Process Design (Signature Edition)", "Your First Recruitment Process Design Project (Signature Edition)", "Beginner Mistakes in Recruitment Process Design (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Recruitment Process Design (Signature Edition)", "Myths vs. Facts in Recruitment Process Design (Signature Edition)", "When to Start Recruitment Process Design (Signature Edition)", "Measuring the Basics in Recruitment Process Design (Signature Edition)", "Safety First in Recruitment Process Design (Signature Edition)", "Where to Find Help with Recruitment Process Design (Signature Edition)"], "Compounded": ["The Recruitment Process Design Workflow, Step by Step (Signature Edition)", "A Recruitment Process Design Decision Framework (Signature Edition)", "Recruitment Process Design Cost and Budget Planning (Signature Edition)", "Scheduling Recruitment Process Design Work (Signature Edition)", "Quality Checks for Recruitment Process Design (Signature Edition)", "Recruitment Process Design Troubleshooting Guide (Signature Edition)", "Intermediate Recruitment Process Design Skills (Signature Edition)", "Recruitment Process Design in Real-World Cases (Signature Edition)", "Comparing Recruitment Process Design Options (Signature Edition)", "Documenting Your Recruitment Process Design Work (Signature Edition)", "Collaborating on Recruitment Process Design (Signature Edition)", "Scaling Up Recruitment Process Design (Signature Edition)"], "Advanced": ["Advanced Recruitment Process Design Techniques (Signature Edition)", "Recruitment Process Design Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Recruitment Process Design (Signature Edition)", "Automating Recruitment Process Design (Signature Edition)", "Recruitment Process Design Long-Term Strategy (Signature Edition)", "Teaching Recruitment Process Design to Others (Signature Edition)", "Ethics and Responsibility in Recruitment Process Design (Signature Edition)", "Integrating Recruitment Process Design with Other Systems (Signature Edition)", "The Recruitment Process Design Frontier: What Comes Next (Signature Edition)", "The Recruitment Process Design Master Checklist (Signature Edition)", "Recruitment Process Design Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"recruitment-process-design-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-recruitment-process-design-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("recruitment-process-design-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
