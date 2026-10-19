(function(){'use strict';
/* JAH Public Information Extraction Database generator — jahdb-information-extraction-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INFOE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Information Extraction", "Getting Started with Information Extraction in Plain Steps", "Information Extraction Glossary: Key Terms Explained", "Why Information Extraction Matters: The Real-World Payoff", "Information Extraction for Absolute Beginners", "The History and Context of Information Extraction", "Information Extraction: Common Myths Debunked", "The Five Building Blocks of Information Extraction", "Information Extraction in Everyday Life", "Information Extraction Basics Quiz and Answer Key", "A First Project in Information Extraction", "Information Extraction: What Success Looks Like"],
"Compounded": ["Information Extraction Step-by-Step Playbook", "Information Extraction Tools and Resources Directory", "Information Extraction Checklists You Can Use Today", "The 10 Most Common Information Extraction Mistakes", "Information Extraction Cost and Budget Guide", "Information Extraction Safety, Risk, and What Can Go Wrong", "Information Extraction Troubleshooting Guide", "Information Extraction for Busy People: The 80/20 Version", "Information Extraction Decision Framework", "Information Extraction: Comparing Your Options", "Information Extraction Templates and Worksheets", "Information Extraction Case Studies: Three Real Situations"],
"Advanced": ["Advanced Information Extraction Techniques", "Information Extraction Metrics: How to Measure Progress", "Information Extraction Systems and Automation", "Information Extraction Expert Interview Playbook", "Information Extraction Edge Cases and What to Do", "Teaching Information Extraction to Others", "Information Extraction Research Review: What the Evidence Says", "Information Extraction Planning Your Next 12 Months", "Information Extraction Ethics and Responsibility", "Information Extraction Mastery Capstone Project"],
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
    demo:{kind:"information-extraction-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("information-extraction",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
