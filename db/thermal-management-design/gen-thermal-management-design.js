(function(){'use strict';
/* JAH Public Thermal Management Design Database generator — jahdb-thermal-management-design-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-THERMD-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Thermal Management Design", "Getting Started with Thermal Management Design in Plain Steps", "Thermal Management Design Glossary: Key Terms Explained", "Why Thermal Management Design Matters: The Real-World Payoff", "Thermal Management Design for Absolute Beginners", "The History and Context of Thermal Management Design", "Thermal Management Design: Common Myths Debunked", "The Five Building Blocks of Thermal Management Design", "Thermal Management Design in Everyday Life", "Thermal Management Design Basics Quiz and Answer Key", "A First Project in Thermal Management Design", "Thermal Management Design: What Success Looks Like"],
"Compounded": ["Thermal Management Design Step-by-Step Playbook", "Thermal Management Design Tools and Resources Directory", "Thermal Management Design Checklists You Can Use Today", "The 10 Most Common Thermal Management Design Mistakes", "Thermal Management Design Cost and Budget Guide", "Thermal Management Design Safety, Risk, and What Can Go Wrong", "Thermal Management Design Troubleshooting Guide", "Thermal Management Design for Busy People: The 80/20 Version", "Thermal Management Design Decision Framework", "Thermal Management Design: Comparing Your Options", "Thermal Management Design Templates and Worksheets", "Thermal Management Design Case Studies: Three Real Situations"],
"Advanced": ["Advanced Thermal Management Design Techniques", "Thermal Management Design Metrics: How to Measure Progress", "Thermal Management Design Systems and Automation", "Thermal Management Design Expert Interview Playbook", "Thermal Management Design Edge Cases and What to Do", "Teaching Thermal Management Design to Others", "Thermal Management Design Research Review: What the Evidence Says", "Thermal Management Design Planning Your Next 12 Months", "Thermal Management Design Ethics and Responsibility", "Thermal Management Design Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — design record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — design record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A design record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"thermal-management-design-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("thermal-management-design",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
