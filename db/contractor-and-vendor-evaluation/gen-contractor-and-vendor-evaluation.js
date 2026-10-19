(function(){'use strict';
/* JAH Public Contractor and Vendor Evaluation Database generator — jahdb-contractor-and-vendor-evaluation-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CONTAVE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Contractor and Vendor Evaluation", "Getting Started with Contractor and Vendor Evaluation in Plain Steps", "Contractor and Vendor Evaluation Glossary: Key Terms Explained", "Why Contractor and Vendor Evaluation Matters: The Real-World Payoff", "Contractor and Vendor Evaluation for Absolute Beginners", "The History and Context of Contractor and Vendor Evaluation", "Contractor and Vendor Evaluation: Common Myths Debunked", "The Five Building Blocks of Contractor and Vendor Evaluation", "Contractor and Vendor Evaluation in Everyday Life", "Contractor and Vendor Evaluation Basics Quiz and Answer Key", "A First Project in Contractor and Vendor Evaluation", "Contractor and Vendor Evaluation: What Success Looks Like"],
"Compounded": ["Contractor and Vendor Evaluation Step-by-Step Playbook", "Contractor and Vendor Evaluation Tools and Resources Directory", "Contractor and Vendor Evaluation Checklists You Can Use Today", "The 10 Most Common Contractor and Vendor Evaluation Mistakes", "Contractor and Vendor Evaluation Cost and Budget Guide", "Contractor and Vendor Evaluation Safety, Risk, and What Can Go Wrong", "Contractor and Vendor Evaluation Troubleshooting Guide", "Contractor and Vendor Evaluation for Busy People: The 80/20 Version", "Contractor and Vendor Evaluation Decision Framework", "Contractor and Vendor Evaluation: Comparing Your Options", "Contractor and Vendor Evaluation Templates and Worksheets", "Contractor and Vendor Evaluation Case Studies: Three Real Situations"],
"Advanced": ["Advanced Contractor and Vendor Evaluation Techniques", "Contractor and Vendor Evaluation Metrics: How to Measure Progress", "Contractor and Vendor Evaluation Systems and Automation", "Contractor and Vendor Evaluation Expert Interview Playbook", "Contractor and Vendor Evaluation Edge Cases and What to Do", "Teaching Contractor and Vendor Evaluation to Others", "Contractor and Vendor Evaluation Research Review: What the Evidence Says", "Contractor and Vendor Evaluation Planning Your Next 12 Months", "Contractor and Vendor Evaluation Ethics and Responsibility", "Contractor and Vendor Evaluation Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — evaluation guide sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — evaluation guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A evaluation guide of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"contractor-and-vendor-evaluation-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("contractor-and-vendor-evaluation",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
