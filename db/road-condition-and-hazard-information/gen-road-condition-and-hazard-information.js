(function(){'use strict';
/* JAH Public Road Condition and Hazard Information Database generator — jahdb-road-condition-and-hazard-information-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ROADCAH-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Road Condition and Hazard Information", "Getting Started with Road Condition and Hazard Information in Plain Steps", "Road Condition and Hazard Information Glossary: Key Terms Explained", "Why Road Condition and Hazard Information Matters: The Real-World Payoff", "Road Condition and Hazard Information for Absolute Beginners", "The History and Context of Road Condition and Hazard Information", "Road Condition and Hazard Information: Common Myths Debunked", "The Five Building Blocks of Road Condition and Hazard Information", "Road Condition and Hazard Information in Everyday Life", "Road Condition and Hazard Information Basics Quiz and Answer Key", "A First Project in Road Condition and Hazard Information", "Road Condition and Hazard Information: What Success Looks Like"],
"Compounded": ["Road Condition and Hazard Information Step-by-Step Playbook", "Road Condition and Hazard Information Tools and Resources Directory", "Road Condition and Hazard Information Checklists You Can Use Today", "The 10 Most Common Road Condition and Hazard Information Mistakes", "Road Condition and Hazard Information Cost and Budget Guide", "Road Condition and Hazard Information Safety, Risk, and What Can Go Wrong", "Road Condition and Hazard Information Troubleshooting Guide", "Road Condition and Hazard Information for Busy People: The 80/20 Version", "Road Condition and Hazard Information Decision Framework", "Road Condition and Hazard Information: Comparing Your Options", "Road Condition and Hazard Information Templates and Worksheets", "Road Condition and Hazard Information Case Studies: Three Real Situations"],
"Advanced": ["Advanced Road Condition and Hazard Information Techniques", "Road Condition and Hazard Information Metrics: How to Measure Progress", "Road Condition and Hazard Information Systems and Automation", "Road Condition and Hazard Information Expert Interview Playbook", "Road Condition and Hazard Information Edge Cases and What to Do", "Teaching Road Condition and Hazard Information to Others", "Road Condition and Hazard Information Research Review: What the Evidence Says", "Road Condition and Hazard Information Planning Your Next 12 Months", "Road Condition and Hazard Information Ethics and Responsibility", "Road Condition and Hazard Information Mastery Capstone Project"],
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
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"road-condition-and-hazard-information-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("road-condition-and-hazard-information",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
