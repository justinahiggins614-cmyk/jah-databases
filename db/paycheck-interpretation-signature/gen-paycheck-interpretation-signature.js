(function(){'use strict';
/* JAH paycheck-interpretation-signature generator — jahdb-paycheck-interpretation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PIS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Paycheck Interpretation (Signature Edition)", "Core Concepts of Paycheck Interpretation (Signature Edition)", "Essential Vocabulary for Paycheck Interpretation (Signature Edition)", "Your First Paycheck Interpretation Project (Signature Edition)", "Beginner Mistakes in Paycheck Interpretation (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Paycheck Interpretation (Signature Edition)", "Myths vs. Facts in Paycheck Interpretation (Signature Edition)", "When to Start Paycheck Interpretation (Signature Edition)", "Measuring the Basics in Paycheck Interpretation (Signature Edition)", "Safety First in Paycheck Interpretation (Signature Edition)", "Where to Find Help with Paycheck Interpretation (Signature Edition)"], "Compounded": ["The Paycheck Interpretation Workflow, Step by Step (Signature Edition)", "A Paycheck Interpretation Decision Framework (Signature Edition)", "Paycheck Interpretation Cost and Budget Planning (Signature Edition)", "Scheduling Paycheck Interpretation Work (Signature Edition)", "Quality Checks for Paycheck Interpretation (Signature Edition)", "Paycheck Interpretation Troubleshooting Guide (Signature Edition)", "Intermediate Paycheck Interpretation Skills (Signature Edition)", "Paycheck Interpretation in Real-World Cases (Signature Edition)", "Comparing Paycheck Interpretation Options (Signature Edition)", "Documenting Your Paycheck Interpretation Work (Signature Edition)", "Collaborating on Paycheck Interpretation (Signature Edition)", "Scaling Up Paycheck Interpretation (Signature Edition)"], "Advanced": ["Advanced Paycheck Interpretation Techniques (Signature Edition)", "Paycheck Interpretation Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Paycheck Interpretation (Signature Edition)", "Automating Paycheck Interpretation (Signature Edition)", "Paycheck Interpretation Long-Term Strategy (Signature Edition)", "Teaching Paycheck Interpretation to Others (Signature Edition)", "Ethics and Responsibility in Paycheck Interpretation (Signature Edition)", "Integrating Paycheck Interpretation with Other Systems (Signature Edition)", "The Paycheck Interpretation Frontier: What Comes Next (Signature Edition)", "The Paycheck Interpretation Master Checklist (Signature Edition)", "Paycheck Interpretation Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"paycheck-interpretation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-paycheck-interpretation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("paycheck-interpretation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
