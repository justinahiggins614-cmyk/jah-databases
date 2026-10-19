(function(){'use strict';
/* JAH Public Public Transit Route Planning Database generator — jahdb-public-transit-route-planning-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PUBLTRP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Public Transit Route Planning", "Getting Started with Public Transit Route Planning in Plain Steps", "Public Transit Route Planning Glossary: Key Terms Explained", "Why Public Transit Route Planning Matters: The Real-World Payoff", "Public Transit Route Planning for Absolute Beginners", "The History and Context of Public Transit Route Planning", "Public Transit Route Planning: Common Myths Debunked", "The Five Building Blocks of Public Transit Route Planning", "Public Transit Route Planning in Everyday Life", "Public Transit Route Planning Basics Quiz and Answer Key", "A First Project in Public Transit Route Planning", "Public Transit Route Planning: What Success Looks Like"],
"Compounded": ["Public Transit Route Planning Step-by-Step Playbook", "Public Transit Route Planning Tools and Resources Directory", "Public Transit Route Planning Checklists You Can Use Today", "The 10 Most Common Public Transit Route Planning Mistakes", "Public Transit Route Planning Cost and Budget Guide", "Public Transit Route Planning Safety, Risk, and What Can Go Wrong", "Public Transit Route Planning Troubleshooting Guide", "Public Transit Route Planning for Busy People: The 80/20 Version", "Public Transit Route Planning Decision Framework", "Public Transit Route Planning: Comparing Your Options", "Public Transit Route Planning Templates and Worksheets", "Public Transit Route Planning Case Studies: Three Real Situations"],
"Advanced": ["Advanced Public Transit Route Planning Techniques", "Public Transit Route Planning Metrics: How to Measure Progress", "Public Transit Route Planning Systems and Automation", "Public Transit Route Planning Expert Interview Playbook", "Public Transit Route Planning Edge Cases and What to Do", "Teaching Public Transit Route Planning to Others", "Public Transit Route Planning Research Review: What the Evidence Says", "Public Transit Route Planning Planning Your Next 12 Months", "Public Transit Route Planning Ethics and Responsibility", "Public Transit Route Planning Mastery Capstone Project"],
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
    demo:{kind:"public-transit-route-planning-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("public-transit-route-planning",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
