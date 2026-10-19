(function(){'use strict';
/* JAH personal-problem-solving-signature generator — jahdb-personal-problem-solving-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PPSS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Personal Problem-Solving (Signature Edition)", "Core Concepts of Personal Problem-Solving (Signature Edition)", "Essential Vocabulary for Personal Problem-Solving (Signature Edition)", "Your First Personal Problem-Solving Project (Signature Edition)", "Beginner Mistakes in Personal Problem-Solving (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Personal Problem-Solving (Signature Edition)", "Myths vs. Facts in Personal Problem-Solving (Signature Edition)", "When to Start Personal Problem-Solving (Signature Edition)", "Measuring the Basics in Personal Problem-Solving (Signature Edition)", "Safety First in Personal Problem-Solving (Signature Edition)", "Where to Find Help with Personal Problem-Solving (Signature Edition)"], "Compounded": ["The Personal Problem-Solving Workflow, Step by Step (Signature Edition)", "A Personal Problem-Solving Decision Framework (Signature Edition)", "Personal Problem-Solving Cost and Budget Planning (Signature Edition)", "Scheduling Personal Problem-Solving Work (Signature Edition)", "Quality Checks for Personal Problem-Solving (Signature Edition)", "Personal Problem-Solving Troubleshooting Guide (Signature Edition)", "Intermediate Personal Problem-Solving Skills (Signature Edition)", "Personal Problem-Solving in Real-World Cases (Signature Edition)", "Comparing Personal Problem-Solving Options (Signature Edition)", "Documenting Your Personal Problem-Solving Work (Signature Edition)", "Collaborating on Personal Problem-Solving (Signature Edition)", "Scaling Up Personal Problem-Solving (Signature Edition)"], "Advanced": ["Advanced Personal Problem-Solving Techniques (Signature Edition)", "Personal Problem-Solving Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Personal Problem-Solving (Signature Edition)", "Automating Personal Problem-Solving (Signature Edition)", "Personal Problem-Solving Long-Term Strategy (Signature Edition)", "Teaching Personal Problem-Solving to Others (Signature Edition)", "Ethics and Responsibility in Personal Problem-Solving (Signature Edition)", "Integrating Personal Problem-Solving with Other Systems (Signature Edition)", "The Personal Problem-Solving Frontier: What Comes Next (Signature Edition)", "The Personal Problem-Solving Master Checklist (Signature Edition)", "Personal Problem-Solving Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"personal-problem-solving-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-personal-problem-solving-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("personal-problem-solving-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
