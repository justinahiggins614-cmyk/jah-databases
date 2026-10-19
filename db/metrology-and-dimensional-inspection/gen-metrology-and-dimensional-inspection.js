(function(){'use strict';
/* JAH Public Metrology and Dimensional Inspection Database generator — jahdb-metrology-and-dimensional-inspection-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-METRADI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Metrology and Dimensional Inspection", "Getting Started with Metrology and Dimensional Inspection in Plain Steps", "Metrology and Dimensional Inspection Glossary: Key Terms Explained", "Why Metrology and Dimensional Inspection Matters: The Real-World Payoff", "Metrology and Dimensional Inspection for Absolute Beginners", "The History and Context of Metrology and Dimensional Inspection", "Metrology and Dimensional Inspection: Common Myths Debunked", "The Five Building Blocks of Metrology and Dimensional Inspection", "Metrology and Dimensional Inspection in Everyday Life", "Metrology and Dimensional Inspection Basics Quiz and Answer Key", "A First Project in Metrology and Dimensional Inspection", "Metrology and Dimensional Inspection: What Success Looks Like"],
"Compounded": ["Metrology and Dimensional Inspection Step-by-Step Playbook", "Metrology and Dimensional Inspection Tools and Resources Directory", "Metrology and Dimensional Inspection Checklists You Can Use Today", "The 10 Most Common Metrology and Dimensional Inspection Mistakes", "Metrology and Dimensional Inspection Cost and Budget Guide", "Metrology and Dimensional Inspection Safety, Risk, and What Can Go Wrong", "Metrology and Dimensional Inspection Troubleshooting Guide", "Metrology and Dimensional Inspection for Busy People: The 80/20 Version", "Metrology and Dimensional Inspection Decision Framework", "Metrology and Dimensional Inspection: Comparing Your Options", "Metrology and Dimensional Inspection Templates and Worksheets", "Metrology and Dimensional Inspection Case Studies: Three Real Situations"],
"Advanced": ["Advanced Metrology and Dimensional Inspection Techniques", "Metrology and Dimensional Inspection Metrics: How to Measure Progress", "Metrology and Dimensional Inspection Systems and Automation", "Metrology and Dimensional Inspection Expert Interview Playbook", "Metrology and Dimensional Inspection Edge Cases and What to Do", "Teaching Metrology and Dimensional Inspection to Others", "Metrology and Dimensional Inspection Research Review: What the Evidence Says", "Metrology and Dimensional Inspection Planning Your Next 12 Months", "Metrology and Dimensional Inspection Ethics and Responsibility", "Metrology and Dimensional Inspection Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — inspection record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — inspection record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A inspection record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"metrology-and-dimensional-inspection-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("metrology-and-dimensional-inspection",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
