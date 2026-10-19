(function(){'use strict';
/* JAH Public Research Data Cleaning Database generator — jahdb-research-data-cleaning-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RESEDC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Research Data Cleaning", "Getting Started with Research Data Cleaning in Plain Steps", "Research Data Cleaning Glossary: Key Terms Explained", "Why Research Data Cleaning Matters: The Real-World Payoff", "Research Data Cleaning for Absolute Beginners", "The History and Context of Research Data Cleaning", "Research Data Cleaning: Common Myths Debunked", "The Five Building Blocks of Research Data Cleaning", "Research Data Cleaning in Everyday Life", "Research Data Cleaning Basics Quiz and Answer Key", "A First Project in Research Data Cleaning", "Research Data Cleaning: What Success Looks Like"],
"Compounded": ["Research Data Cleaning Step-by-Step Playbook", "Research Data Cleaning Tools and Resources Directory", "Research Data Cleaning Checklists You Can Use Today", "The 10 Most Common Research Data Cleaning Mistakes", "Research Data Cleaning Cost and Budget Guide", "Research Data Cleaning Safety, Risk, and What Can Go Wrong", "Research Data Cleaning Troubleshooting Guide", "Research Data Cleaning for Busy People: The 80/20 Version", "Research Data Cleaning Decision Framework", "Research Data Cleaning: Comparing Your Options", "Research Data Cleaning Templates and Worksheets", "Research Data Cleaning Case Studies: Three Real Situations"],
"Advanced": ["Advanced Research Data Cleaning Techniques", "Research Data Cleaning Metrics: How to Measure Progress", "Research Data Cleaning Systems and Automation", "Research Data Cleaning Expert Interview Playbook", "Research Data Cleaning Edge Cases and What to Do", "Teaching Research Data Cleaning to Others", "Research Data Cleaning Research Review: What the Evidence Says", "Research Data Cleaning Planning Your Next 12 Months", "Research Data Cleaning Ethics and Responsibility", "Research Data Cleaning Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — technique record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technique record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"research-data-cleaning-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("research-data-cleaning",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
