(function(){'use strict';
/* JAH laboratory-result-terminology-signature generator — jahdb-laboratory-result-terminology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LRTS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Laboratory Result Terminology (Signature Edition)", "Core Concepts of Laboratory Result Terminology (Signature Edition)", "Essential Vocabulary for Laboratory Result Terminology (Signature Edition)", "Your First Laboratory Result Terminology Project (Signature Edition)", "Beginner Mistakes in Laboratory Result Terminology (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Laboratory Result Terminology (Signature Edition)", "Myths vs. Facts in Laboratory Result Terminology (Signature Edition)", "When to Start Laboratory Result Terminology (Signature Edition)", "Measuring the Basics in Laboratory Result Terminology (Signature Edition)", "Safety First in Laboratory Result Terminology (Signature Edition)", "Where to Find Help with Laboratory Result Terminology (Signature Edition)"], "Compounded": ["The Laboratory Result Terminology Workflow, Step by Step (Signature Edition)", "A Laboratory Result Terminology Decision Framework (Signature Edition)", "Laboratory Result Terminology Cost and Budget Planning (Signature Edition)", "Scheduling Laboratory Result Terminology Work (Signature Edition)", "Quality Checks for Laboratory Result Terminology (Signature Edition)", "Laboratory Result Terminology Troubleshooting Guide (Signature Edition)", "Intermediate Laboratory Result Terminology Skills (Signature Edition)", "Laboratory Result Terminology in Real-World Cases (Signature Edition)", "Comparing Laboratory Result Terminology Options (Signature Edition)", "Documenting Your Laboratory Result Terminology Work (Signature Edition)", "Collaborating on Laboratory Result Terminology (Signature Edition)", "Scaling Up Laboratory Result Terminology (Signature Edition)"], "Advanced": ["Advanced Laboratory Result Terminology Techniques (Signature Edition)", "Laboratory Result Terminology Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Laboratory Result Terminology (Signature Edition)", "Automating Laboratory Result Terminology (Signature Edition)", "Laboratory Result Terminology Long-Term Strategy (Signature Edition)", "Teaching Laboratory Result Terminology to Others (Signature Edition)", "Ethics and Responsibility in Laboratory Result Terminology (Signature Edition)", "Integrating Laboratory Result Terminology with Other Systems (Signature Edition)", "The Laboratory Result Terminology Frontier: What Comes Next (Signature Edition)", "The Laboratory Result Terminology Master Checklist (Signature Edition)", "Laboratory Result Terminology Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"laboratory-result-terminology-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-laboratory-result-terminology-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("laboratory-result-terminology-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
