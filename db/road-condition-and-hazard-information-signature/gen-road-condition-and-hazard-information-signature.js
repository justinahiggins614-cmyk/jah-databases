(function(){'use strict';
/* JAH Signature Road Condition and Hazard Information Database generator — jahdb-road-condition-and-hazard-information-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ROADCA1-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Road Condition and Hazard Information (Signature Edition)", "Getting Started with Road Condition and Hazard Information in Plain Steps (Signature Edition)", "Road Condition and Hazard Information Glossary: Key Terms Explained (Signature Edition)", "Why Road Condition and Hazard Information Matters: The Real-World Payoff (Signature Edition)", "Road Condition and Hazard Information for Absolute Beginners (Signature Edition)", "The History and Context of Road Condition and Hazard Information (Signature Edition)", "Road Condition and Hazard Information: Common Myths Debunked (Signature Edition)", "The Five Building Blocks of Road Condition and Hazard Information (Signature Edition)", "Road Condition and Hazard Information in Everyday Life (Signature Edition)", "Road Condition and Hazard Information Basics Quiz and Answer Key (Signature Edition)", "A First Project in Road Condition and Hazard Information (Signature Edition)", "Road Condition and Hazard Information: What Success Looks Like (Signature Edition)"],
"Compounded": ["Road Condition and Hazard Information Step-by-Step Playbook (Signature Edition)", "Road Condition and Hazard Information Tools and Resources Directory (Signature Edition)", "Road Condition and Hazard Information Checklists You Can Use Today (Signature Edition)", "The 10 Most Common Road Condition and Hazard Information Mistakes (Signature Edition)", "Road Condition and Hazard Information Cost and Budget Guide (Signature Edition)", "Road Condition and Hazard Information Safety, Risk, and What Can Go Wrong (Signature Edition)", "Road Condition and Hazard Information Troubleshooting Guide (Signature Edition)", "Road Condition and Hazard Information for Busy People: The 80/20 Version (Signature Edition)", "Road Condition and Hazard Information Decision Framework (Signature Edition)", "Road Condition and Hazard Information: Comparing Your Options (Signature Edition)", "Road Condition and Hazard Information Templates and Worksheets (Signature Edition)", "Road Condition and Hazard Information Case Studies: Three Real Situations (Signature Edition)"],
"Advanced": ["Advanced Road Condition and Hazard Information Techniques (Signature Edition)", "Road Condition and Hazard Information Metrics: How to Measure Progress (Signature Edition)", "Road Condition and Hazard Information Systems and Automation (Signature Edition)", "Road Condition and Hazard Information Expert Interview Playbook (Signature Edition)", "Road Condition and Hazard Information Edge Cases and What to Do (Signature Edition)", "Teaching Road Condition and Hazard Information to Others (Signature Edition)", "Road Condition and Hazard Information Research Review: What the Evidence Says (Signature Edition)", "Road Condition and Hazard Information Planning Your Next 12 Months (Signature Edition)", "Road Condition and Hazard Information Ethics and Responsibility (Signature Edition)", "Road Condition and Hazard Information Mastery Capstone Project (Signature Edition)"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — information record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — information record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A information record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"road-condition-and-hazard-information-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("road-condition-and-hazard-information-signature",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
