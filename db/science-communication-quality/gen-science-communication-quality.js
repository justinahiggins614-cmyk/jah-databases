(function(){'use strict';
/* JAH Public Science Communication Quality Database generator — jahdb-science-communication-quality-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCIECQ-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Science Communication Quality", "Getting Started with Science Communication Quality in Plain Steps", "Science Communication Quality Glossary: Key Terms Explained", "Why Science Communication Quality Matters: The Real-World Payoff", "Science Communication Quality for Absolute Beginners", "The History and Context of Science Communication Quality", "Science Communication Quality: Common Myths Debunked", "The Five Building Blocks of Science Communication Quality", "Science Communication Quality in Everyday Life", "Science Communication Quality Basics Quiz and Answer Key", "A First Project in Science Communication Quality", "Science Communication Quality: What Success Looks Like"],
"Compounded": ["Science Communication Quality Step-by-Step Playbook", "Science Communication Quality Tools and Resources Directory", "Science Communication Quality Checklists You Can Use Today", "The 10 Most Common Science Communication Quality Mistakes", "Science Communication Quality Cost and Budget Guide", "Science Communication Quality Safety, Risk, and What Can Go Wrong", "Science Communication Quality Troubleshooting Guide", "Science Communication Quality for Busy People: The 80/20 Version", "Science Communication Quality Decision Framework", "Science Communication Quality: Comparing Your Options", "Science Communication Quality Templates and Worksheets", "Science Communication Quality Case Studies: Three Real Situations"],
"Advanced": ["Advanced Science Communication Quality Techniques", "Science Communication Quality Metrics: How to Measure Progress", "Science Communication Quality Systems and Automation", "Science Communication Quality Expert Interview Playbook", "Science Communication Quality Edge Cases and What to Do", "Teaching Science Communication Quality to Others", "Science Communication Quality Research Review: What the Evidence Says", "Science Communication Quality Planning Your Next 12 Months", "Science Communication Quality Ethics and Responsibility", "Science Communication Quality Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — quality record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — quality record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A quality record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"science-communication-quality-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("science-communication-quality",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
