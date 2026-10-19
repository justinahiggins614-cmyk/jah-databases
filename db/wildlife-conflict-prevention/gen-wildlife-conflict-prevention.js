(function(){'use strict';
/* JAH Public Wildlife Conflict Prevention Database generator — jahdb-wildlife-conflict-prevention-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WILDCP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Wildlife Conflict Prevention", "Getting Started with Wildlife Conflict Prevention in Plain Steps", "Wildlife Conflict Prevention Glossary: Key Terms Explained", "Why Wildlife Conflict Prevention Matters: The Real-World Payoff", "Wildlife Conflict Prevention for Absolute Beginners", "The History and Context of Wildlife Conflict Prevention", "Wildlife Conflict Prevention: Common Myths Debunked", "The Five Building Blocks of Wildlife Conflict Prevention", "Wildlife Conflict Prevention in Everyday Life", "Wildlife Conflict Prevention Basics Quiz and Answer Key", "A First Project in Wildlife Conflict Prevention", "Wildlife Conflict Prevention: What Success Looks Like"],
"Compounded": ["Wildlife Conflict Prevention Step-by-Step Playbook", "Wildlife Conflict Prevention Tools and Resources Directory", "Wildlife Conflict Prevention Checklists You Can Use Today", "The 10 Most Common Wildlife Conflict Prevention Mistakes", "Wildlife Conflict Prevention Cost and Budget Guide", "Wildlife Conflict Prevention Safety, Risk, and What Can Go Wrong", "Wildlife Conflict Prevention Troubleshooting Guide", "Wildlife Conflict Prevention for Busy People: The 80/20 Version", "Wildlife Conflict Prevention Decision Framework", "Wildlife Conflict Prevention: Comparing Your Options", "Wildlife Conflict Prevention Templates and Worksheets", "Wildlife Conflict Prevention Case Studies: Three Real Situations"],
"Advanced": ["Advanced Wildlife Conflict Prevention Techniques", "Wildlife Conflict Prevention Metrics: How to Measure Progress", "Wildlife Conflict Prevention Systems and Automation", "Wildlife Conflict Prevention Expert Interview Playbook", "Wildlife Conflict Prevention Edge Cases and What to Do", "Teaching Wildlife Conflict Prevention to Others", "Wildlife Conflict Prevention Research Review: What the Evidence Says", "Wildlife Conflict Prevention Planning Your Next 12 Months", "Wildlife Conflict Prevention Ethics and Responsibility", "Wildlife Conflict Prevention Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — prevention record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — prevention record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A prevention record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"wildlife-conflict-prevention-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("wildlife-conflict-prevention",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
