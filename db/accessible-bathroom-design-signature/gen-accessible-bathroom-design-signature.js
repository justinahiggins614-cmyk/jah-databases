(function(){'use strict';
/* JAH accessible-bathroom-design-signature generator — jahdb-accessible-bathroom-design-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ABDS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Accessible Bathroom Design (Signature Edition)", "Core Concepts of Accessible Bathroom Design (Signature Edition)", "Essential Vocabulary for Accessible Bathroom Design (Signature Edition)", "Your First Accessible Bathroom Design Project (Signature Edition)", "Beginner Mistakes in Accessible Bathroom Design (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Accessible Bathroom Design (Signature Edition)", "Myths vs. Facts in Accessible Bathroom Design (Signature Edition)", "When to Start Accessible Bathroom Design (Signature Edition)", "Measuring the Basics in Accessible Bathroom Design (Signature Edition)", "Safety First in Accessible Bathroom Design (Signature Edition)", "Where to Find Help with Accessible Bathroom Design (Signature Edition)"], "Compounded": ["The Accessible Bathroom Design Workflow, Step by Step (Signature Edition)", "A Accessible Bathroom Design Decision Framework (Signature Edition)", "Accessible Bathroom Design Cost and Budget Planning (Signature Edition)", "Scheduling Accessible Bathroom Design Work (Signature Edition)", "Quality Checks for Accessible Bathroom Design (Signature Edition)", "Accessible Bathroom Design Troubleshooting Guide (Signature Edition)", "Intermediate Accessible Bathroom Design Skills (Signature Edition)", "Accessible Bathroom Design in Real-World Cases (Signature Edition)", "Comparing Accessible Bathroom Design Options (Signature Edition)", "Documenting Your Accessible Bathroom Design Work (Signature Edition)", "Collaborating on Accessible Bathroom Design (Signature Edition)", "Scaling Up Accessible Bathroom Design (Signature Edition)"], "Advanced": ["Advanced Accessible Bathroom Design Techniques (Signature Edition)", "Accessible Bathroom Design Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Accessible Bathroom Design (Signature Edition)", "Automating Accessible Bathroom Design (Signature Edition)", "Accessible Bathroom Design Long-Term Strategy (Signature Edition)", "Teaching Accessible Bathroom Design to Others (Signature Edition)", "Ethics and Responsibility in Accessible Bathroom Design (Signature Edition)", "Integrating Accessible Bathroom Design with Other Systems (Signature Edition)", "The Accessible Bathroom Design Frontier: What Comes Next (Signature Edition)", "The Accessible Bathroom Design Master Checklist (Signature Edition)", "Accessible Bathroom Design Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"accessible-bathroom-design-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-accessible-bathroom-design-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("accessible-bathroom-design-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
