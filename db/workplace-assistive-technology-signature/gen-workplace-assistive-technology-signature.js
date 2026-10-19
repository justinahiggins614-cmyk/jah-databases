(function(){'use strict';
/* JAH workplace-assistive-technology-signature generator — jahdb-workplace-assistive-technology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WATS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Workplace Assistive Technology (Signature Edition)", "Core Concepts of Workplace Assistive Technology (Signature Edition)", "Essential Vocabulary for Workplace Assistive Technology (Signature Edition)", "Your First Workplace Assistive Technology Project (Signature Edition)", "Beginner Mistakes in Workplace Assistive Technology (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Workplace Assistive Technology (Signature Edition)", "Myths vs. Facts in Workplace Assistive Technology (Signature Edition)", "When to Start Workplace Assistive Technology (Signature Edition)", "Measuring the Basics in Workplace Assistive Technology (Signature Edition)", "Safety First in Workplace Assistive Technology (Signature Edition)", "Where to Find Help with Workplace Assistive Technology (Signature Edition)"], "Compounded": ["The Workplace Assistive Technology Workflow, Step by Step (Signature Edition)", "A Workplace Assistive Technology Decision Framework (Signature Edition)", "Workplace Assistive Technology Cost and Budget Planning (Signature Edition)", "Scheduling Workplace Assistive Technology Work (Signature Edition)", "Quality Checks for Workplace Assistive Technology (Signature Edition)", "Workplace Assistive Technology Troubleshooting Guide (Signature Edition)", "Intermediate Workplace Assistive Technology Skills (Signature Edition)", "Workplace Assistive Technology in Real-World Cases (Signature Edition)", "Comparing Workplace Assistive Technology Options (Signature Edition)", "Documenting Your Workplace Assistive Technology Work (Signature Edition)", "Collaborating on Workplace Assistive Technology (Signature Edition)", "Scaling Up Workplace Assistive Technology (Signature Edition)"], "Advanced": ["Advanced Workplace Assistive Technology Techniques (Signature Edition)", "Workplace Assistive Technology Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Workplace Assistive Technology (Signature Edition)", "Automating Workplace Assistive Technology (Signature Edition)", "Workplace Assistive Technology Long-Term Strategy (Signature Edition)", "Teaching Workplace Assistive Technology to Others (Signature Edition)", "Ethics and Responsibility in Workplace Assistive Technology (Signature Edition)", "Integrating Workplace Assistive Technology with Other Systems (Signature Edition)", "The Workplace Assistive Technology Frontier: What Comes Next (Signature Edition)", "The Workplace Assistive Technology Master Checklist (Signature Edition)", "Workplace Assistive Technology Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"workplace-assistive-technology-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-workplace-assistive-technology-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("workplace-assistive-technology-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
