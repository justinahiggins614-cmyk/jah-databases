(function(){'use strict';
/* JAH Signature Startup Cost Estimation Database generator — jahdb-startup-cost-estimation-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STARCES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Startup Cost Estimation (Signature Edition)", "Getting Started with Startup Cost Estimation in Plain Steps (Signature Edition)", "Startup Cost Estimation Glossary: Key Terms Explained (Signature Edition)", "Why Startup Cost Estimation Matters: The Real-World Payoff (Signature Edition)", "Startup Cost Estimation for Absolute Beginners (Signature Edition)", "The History and Context of Startup Cost Estimation (Signature Edition)", "Startup Cost Estimation: Common Myths Debunked (Signature Edition)", "The Five Building Blocks of Startup Cost Estimation (Signature Edition)", "Startup Cost Estimation in Everyday Life (Signature Edition)", "Startup Cost Estimation Basics Quiz and Answer Key (Signature Edition)", "A First Project in Startup Cost Estimation (Signature Edition)", "Startup Cost Estimation: What Success Looks Like (Signature Edition)"],
"Compounded": ["Startup Cost Estimation Step-by-Step Playbook (Signature Edition)", "Startup Cost Estimation Tools and Resources Directory (Signature Edition)", "Startup Cost Estimation Checklists You Can Use Today (Signature Edition)", "The 10 Most Common Startup Cost Estimation Mistakes (Signature Edition)", "Startup Cost Estimation Cost and Budget Guide (Signature Edition)", "Startup Cost Estimation Safety, Risk, and What Can Go Wrong (Signature Edition)", "Startup Cost Estimation Troubleshooting Guide (Signature Edition)", "Startup Cost Estimation for Busy People: The 80/20 Version (Signature Edition)", "Startup Cost Estimation Decision Framework (Signature Edition)", "Startup Cost Estimation: Comparing Your Options (Signature Edition)", "Startup Cost Estimation Templates and Worksheets (Signature Edition)", "Startup Cost Estimation Case Studies: Three Real Situations (Signature Edition)"],
"Advanced": ["Advanced Startup Cost Estimation Techniques (Signature Edition)", "Startup Cost Estimation Metrics: How to Measure Progress (Signature Edition)", "Startup Cost Estimation Systems and Automation (Signature Edition)", "Startup Cost Estimation Expert Interview Playbook (Signature Edition)", "Startup Cost Estimation Edge Cases and What to Do (Signature Edition)", "Teaching Startup Cost Estimation to Others (Signature Edition)", "Startup Cost Estimation Research Review: What the Evidence Says (Signature Edition)", "Startup Cost Estimation Planning Your Next 12 Months (Signature Edition)", "Startup Cost Estimation Ethics and Responsibility (Signature Edition)", "Startup Cost Estimation Mastery Capstone Project (Signature Edition)"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — estimation guide sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — estimation guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A estimation guide of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"startup-cost-estimation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("startup-cost-estimation-signature",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
