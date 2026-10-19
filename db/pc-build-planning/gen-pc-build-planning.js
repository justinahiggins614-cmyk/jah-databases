(function(){'use strict';
/* JAH Public PC Build Planning Database generator — jahdb-pc-build-planning-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PCBP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of PC Build Planning", "Getting Started with PC Build Planning in Plain Steps", "PC Build Planning Glossary: Key Terms Explained", "Why PC Build Planning Matters: The Real-World Payoff", "PC Build Planning for Absolute Beginners", "The History and Context of PC Build Planning", "PC Build Planning: Common Myths Debunked", "The Five Building Blocks of PC Build Planning", "PC Build Planning in Everyday Life", "PC Build Planning Basics Quiz and Answer Key", "A First Project in PC Build Planning", "PC Build Planning: What Success Looks Like"],
"Compounded": ["PC Build Planning Step-by-Step Playbook", "PC Build Planning Tools and Resources Directory", "PC Build Planning Checklists You Can Use Today", "The 10 Most Common PC Build Planning Mistakes", "PC Build Planning Cost and Budget Guide", "PC Build Planning Safety, Risk, and What Can Go Wrong", "PC Build Planning Troubleshooting Guide", "PC Build Planning for Busy People: The 80/20 Version", "PC Build Planning Decision Framework", "PC Build Planning: Comparing Your Options", "PC Build Planning Templates and Worksheets", "PC Build Planning Case Studies: Three Real Situations"],
"Advanced": ["Advanced PC Build Planning Techniques", "PC Build Planning Metrics: How to Measure Progress", "PC Build Planning Systems and Automation", "PC Build Planning Expert Interview Playbook", "PC Build Planning Edge Cases and What to Do", "Teaching PC Build Planning to Others", "PC Build Planning Research Review: What the Evidence Says", "PC Build Planning Planning Your Next 12 Months", "PC Build Planning Ethics and Responsibility", "PC Build Planning Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — planning guide sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — planning guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A planning guide of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"pc-build-planning-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("pc-build-planning",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
