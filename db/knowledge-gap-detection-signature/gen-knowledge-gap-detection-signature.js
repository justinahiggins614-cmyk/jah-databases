(function(){'use strict';
/* JAH knowledge-gap-detection-signature generator — jahdb-knowledge-gap-detection-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KGDS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Knowledge Gap Detection (Signature Edition)", "Core Concepts of Knowledge Gap Detection (Signature Edition)", "Essential Vocabulary for Knowledge Gap Detection (Signature Edition)", "Your First Knowledge Gap Detection Project (Signature Edition)", "Beginner Mistakes in Knowledge Gap Detection (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Knowledge Gap Detection (Signature Edition)", "Myths vs. Facts in Knowledge Gap Detection (Signature Edition)", "When to Start Knowledge Gap Detection (Signature Edition)", "Measuring the Basics in Knowledge Gap Detection (Signature Edition)", "Safety First in Knowledge Gap Detection (Signature Edition)", "Where to Find Help with Knowledge Gap Detection (Signature Edition)"], "Compounded": ["The Knowledge Gap Detection Workflow, Step by Step (Signature Edition)", "A Knowledge Gap Detection Decision Framework (Signature Edition)", "Knowledge Gap Detection Cost and Budget Planning (Signature Edition)", "Scheduling Knowledge Gap Detection Work (Signature Edition)", "Quality Checks for Knowledge Gap Detection (Signature Edition)", "Knowledge Gap Detection Troubleshooting Guide (Signature Edition)", "Intermediate Knowledge Gap Detection Skills (Signature Edition)", "Knowledge Gap Detection in Real-World Cases (Signature Edition)", "Comparing Knowledge Gap Detection Options (Signature Edition)", "Documenting Your Knowledge Gap Detection Work (Signature Edition)", "Collaborating on Knowledge Gap Detection (Signature Edition)", "Scaling Up Knowledge Gap Detection (Signature Edition)"], "Advanced": ["Advanced Knowledge Gap Detection Techniques (Signature Edition)", "Knowledge Gap Detection Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Knowledge Gap Detection (Signature Edition)", "Automating Knowledge Gap Detection (Signature Edition)", "Knowledge Gap Detection Long-Term Strategy (Signature Edition)", "Teaching Knowledge Gap Detection to Others (Signature Edition)", "Ethics and Responsibility in Knowledge Gap Detection (Signature Edition)", "Integrating Knowledge Gap Detection with Other Systems (Signature Edition)", "The Knowledge Gap Detection Frontier: What Comes Next (Signature Edition)", "The Knowledge Gap Detection Master Checklist (Signature Edition)", "Knowledge Gap Detection Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"knowledge-gap-detection-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-knowledge-gap-detection-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("knowledge-gap-detection-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
