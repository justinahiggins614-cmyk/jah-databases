(function(){'use strict';
/* JAH Public Unmet Community Needs Analysis Database generator — jahdb-unmet-community-needs-analysis-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UNMECNA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Unmet Community Needs Analysis", "Getting Started with Unmet Community Needs Analysis in Plain Steps", "Unmet Community Needs Analysis Glossary: Key Terms Explained", "Why Unmet Community Needs Analysis Matters: The Real-World Payoff", "Unmet Community Needs Analysis for Absolute Beginners", "The History and Context of Unmet Community Needs Analysis", "Unmet Community Needs Analysis: Common Myths Debunked", "The Five Building Blocks of Unmet Community Needs Analysis", "Unmet Community Needs Analysis in Everyday Life", "Unmet Community Needs Analysis Basics Quiz and Answer Key", "A First Project in Unmet Community Needs Analysis", "Unmet Community Needs Analysis: What Success Looks Like"],
"Compounded": ["Unmet Community Needs Analysis Step-by-Step Playbook", "Unmet Community Needs Analysis Tools and Resources Directory", "Unmet Community Needs Analysis Checklists You Can Use Today", "The 10 Most Common Unmet Community Needs Analysis Mistakes", "Unmet Community Needs Analysis Cost and Budget Guide", "Unmet Community Needs Analysis Safety, Risk, and What Can Go Wrong", "Unmet Community Needs Analysis Troubleshooting Guide", "Unmet Community Needs Analysis for Busy People: The 80/20 Version", "Unmet Community Needs Analysis Decision Framework", "Unmet Community Needs Analysis: Comparing Your Options", "Unmet Community Needs Analysis Templates and Worksheets", "Unmet Community Needs Analysis Case Studies: Three Real Situations"],
"Advanced": ["Advanced Unmet Community Needs Analysis Techniques", "Unmet Community Needs Analysis Metrics: How to Measure Progress", "Unmet Community Needs Analysis Systems and Automation", "Unmet Community Needs Analysis Expert Interview Playbook", "Unmet Community Needs Analysis Edge Cases and What to Do", "Teaching Unmet Community Needs Analysis to Others", "Unmet Community Needs Analysis Research Review: What the Evidence Says", "Unmet Community Needs Analysis Planning Your Next 12 Months", "Unmet Community Needs Analysis Ethics and Responsibility", "Unmet Community Needs Analysis Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — analysis record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — analysis record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A analysis record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unmet-community-needs-analysis-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("unmet-community-needs-analysis",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
