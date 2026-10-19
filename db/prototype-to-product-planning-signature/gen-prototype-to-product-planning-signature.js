(function(){'use strict';
/* JAH prototype-to-product-planning-signature generator — jahdb-prototype-to-product-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PTPPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Prototype-to-Product Planning (Signature Edition)", "Core Concepts of Prototype-to-Product Planning (Signature Edition)", "Essential Vocabulary for Prototype-to-Product Planning (Signature Edition)", "Your First Prototype-to-Product Planning Project (Signature Edition)", "Beginner Mistakes in Prototype-to-Product Planning (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Prototype-to-Product Planning (Signature Edition)", "Myths vs. Facts in Prototype-to-Product Planning (Signature Edition)", "When to Start Prototype-to-Product Planning (Signature Edition)", "Measuring the Basics in Prototype-to-Product Planning (Signature Edition)", "Safety First in Prototype-to-Product Planning (Signature Edition)", "Where to Find Help with Prototype-to-Product Planning (Signature Edition)"], "Compounded": ["The Prototype-to-Product Planning Workflow, Step by Step (Signature Edition)", "A Prototype-to-Product Planning Decision Framework (Signature Edition)", "Prototype-to-Product Planning Cost and Budget Planning (Signature Edition)", "Scheduling Prototype-to-Product Planning Work (Signature Edition)", "Quality Checks for Prototype-to-Product Planning (Signature Edition)", "Prototype-to-Product Planning Troubleshooting Guide (Signature Edition)", "Intermediate Prototype-to-Product Planning Skills (Signature Edition)", "Prototype-to-Product Planning in Real-World Cases (Signature Edition)", "Comparing Prototype-to-Product Planning Options (Signature Edition)", "Documenting Your Prototype-to-Product Planning Work (Signature Edition)", "Collaborating on Prototype-to-Product Planning (Signature Edition)", "Scaling Up Prototype-to-Product Planning (Signature Edition)"], "Advanced": ["Advanced Prototype-to-Product Planning Techniques (Signature Edition)", "Prototype-to-Product Planning Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Prototype-to-Product Planning (Signature Edition)", "Automating Prototype-to-Product Planning (Signature Edition)", "Prototype-to-Product Planning Long-Term Strategy (Signature Edition)", "Teaching Prototype-to-Product Planning to Others (Signature Edition)", "Ethics and Responsibility in Prototype-to-Product Planning (Signature Edition)", "Integrating Prototype-to-Product Planning with Other Systems (Signature Edition)", "The Prototype-to-Product Planning Frontier: What Comes Next (Signature Edition)", "The Prototype-to-Product Planning Master Checklist (Signature Edition)", "Prototype-to-Product Planning Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"prototype-to-product-planning-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-prototype-to-product-planning-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("prototype-to-product-planning-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
