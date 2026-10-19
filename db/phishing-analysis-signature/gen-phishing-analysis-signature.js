(function(){'use strict';
/* JAH phishing-analysis-signature generator — jahdb-phishing-analysis-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PAS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Phishing Analysis (Signature Edition)", "Core Concepts of Phishing Analysis (Signature Edition)", "Essential Vocabulary for Phishing Analysis (Signature Edition)", "Your First Phishing Analysis Project (Signature Edition)", "Beginner Mistakes in Phishing Analysis (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Phishing Analysis (Signature Edition)", "Myths vs. Facts in Phishing Analysis (Signature Edition)", "When to Start Phishing Analysis (Signature Edition)", "Measuring the Basics in Phishing Analysis (Signature Edition)", "Safety First in Phishing Analysis (Signature Edition)", "Where to Find Help with Phishing Analysis (Signature Edition)"], "Compounded": ["The Phishing Analysis Workflow, Step by Step (Signature Edition)", "A Phishing Analysis Decision Framework (Signature Edition)", "Phishing Analysis Cost and Budget Planning (Signature Edition)", "Scheduling Phishing Analysis Work (Signature Edition)", "Quality Checks for Phishing Analysis (Signature Edition)", "Phishing Analysis Troubleshooting Guide (Signature Edition)", "Intermediate Phishing Analysis Skills (Signature Edition)", "Phishing Analysis in Real-World Cases (Signature Edition)", "Comparing Phishing Analysis Options (Signature Edition)", "Documenting Your Phishing Analysis Work (Signature Edition)", "Collaborating on Phishing Analysis (Signature Edition)", "Scaling Up Phishing Analysis (Signature Edition)"], "Advanced": ["Advanced Phishing Analysis Techniques (Signature Edition)", "Phishing Analysis Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Phishing Analysis (Signature Edition)", "Automating Phishing Analysis (Signature Edition)", "Phishing Analysis Long-Term Strategy (Signature Edition)", "Teaching Phishing Analysis to Others (Signature Edition)", "Ethics and Responsibility in Phishing Analysis (Signature Edition)", "Integrating Phishing Analysis with Other Systems (Signature Edition)", "The Phishing Analysis Frontier: What Comes Next (Signature Edition)", "The Phishing Analysis Master Checklist (Signature Edition)", "Phishing Analysis Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"phishing-analysis-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-phishing-analysis-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("phishing-analysis-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
