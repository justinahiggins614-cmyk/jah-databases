(function(){'use strict';
/* JAH customer-problem-research-signature generator — jahdb-customer-problem-research-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPRS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Customer Problem Research (Signature Edition)", "Core Concepts of Customer Problem Research (Signature Edition)", "Essential Vocabulary for Customer Problem Research (Signature Edition)", "Your First Customer Problem Research Project (Signature Edition)", "Beginner Mistakes in Customer Problem Research (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Customer Problem Research (Signature Edition)", "Myths vs. Facts in Customer Problem Research (Signature Edition)", "When to Start Customer Problem Research (Signature Edition)", "Measuring the Basics in Customer Problem Research (Signature Edition)", "Safety First in Customer Problem Research (Signature Edition)", "Where to Find Help with Customer Problem Research (Signature Edition)"], "Compounded": ["The Customer Problem Research Workflow, Step by Step (Signature Edition)", "A Customer Problem Research Decision Framework (Signature Edition)", "Customer Problem Research Cost and Budget Planning (Signature Edition)", "Scheduling Customer Problem Research Work (Signature Edition)", "Quality Checks for Customer Problem Research (Signature Edition)", "Customer Problem Research Troubleshooting Guide (Signature Edition)", "Intermediate Customer Problem Research Skills (Signature Edition)", "Customer Problem Research in Real-World Cases (Signature Edition)", "Comparing Customer Problem Research Options (Signature Edition)", "Documenting Your Customer Problem Research Work (Signature Edition)", "Collaborating on Customer Problem Research (Signature Edition)", "Scaling Up Customer Problem Research (Signature Edition)"], "Advanced": ["Advanced Customer Problem Research Techniques (Signature Edition)", "Customer Problem Research Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Customer Problem Research (Signature Edition)", "Automating Customer Problem Research (Signature Edition)", "Customer Problem Research Long-Term Strategy (Signature Edition)", "Teaching Customer Problem Research to Others (Signature Edition)", "Ethics and Responsibility in Customer Problem Research (Signature Edition)", "Integrating Customer Problem Research with Other Systems (Signature Edition)", "The Customer Problem Research Frontier: What Comes Next (Signature Edition)", "The Customer Problem Research Master Checklist (Signature Edition)", "Customer Problem Research Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"customer-problem-research-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-customer-problem-research-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("customer-problem-research-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
