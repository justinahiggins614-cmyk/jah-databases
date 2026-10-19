(function(){'use strict';
/* JAH Signature Thermal Management Design Database generator — jahdb-thermal-management-design-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-THERMDS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Thermal Management Design (Signature Edition)", "Getting Started with Thermal Management Design in Plain Steps (Signature Edition)", "Thermal Management Design Glossary: Key Terms Explained (Signature Edition)", "Why Thermal Management Design Matters: The Real-World Payoff (Signature Edition)", "Thermal Management Design for Absolute Beginners (Signature Edition)", "The History and Context of Thermal Management Design (Signature Edition)", "Thermal Management Design: Common Myths Debunked (Signature Edition)", "The Five Building Blocks of Thermal Management Design (Signature Edition)", "Thermal Management Design in Everyday Life (Signature Edition)", "Thermal Management Design Basics Quiz and Answer Key (Signature Edition)", "A First Project in Thermal Management Design (Signature Edition)", "Thermal Management Design: What Success Looks Like (Signature Edition)"],
"Compounded": ["Thermal Management Design Step-by-Step Playbook (Signature Edition)", "Thermal Management Design Tools and Resources Directory (Signature Edition)", "Thermal Management Design Checklists You Can Use Today (Signature Edition)", "The 10 Most Common Thermal Management Design Mistakes (Signature Edition)", "Thermal Management Design Cost and Budget Guide (Signature Edition)", "Thermal Management Design Safety, Risk, and What Can Go Wrong (Signature Edition)", "Thermal Management Design Troubleshooting Guide (Signature Edition)", "Thermal Management Design for Busy People: The 80/20 Version (Signature Edition)", "Thermal Management Design Decision Framework (Signature Edition)", "Thermal Management Design: Comparing Your Options (Signature Edition)", "Thermal Management Design Templates and Worksheets (Signature Edition)", "Thermal Management Design Case Studies: Three Real Situations (Signature Edition)"],
"Advanced": ["Advanced Thermal Management Design Techniques (Signature Edition)", "Thermal Management Design Metrics: How to Measure Progress (Signature Edition)", "Thermal Management Design Systems and Automation (Signature Edition)", "Thermal Management Design Expert Interview Playbook (Signature Edition)", "Thermal Management Design Edge Cases and What to Do (Signature Edition)", "Teaching Thermal Management Design to Others (Signature Edition)", "Thermal Management Design Research Review: What the Evidence Says (Signature Edition)", "Thermal Management Design Planning Your Next 12 Months (Signature Edition)", "Thermal Management Design Ethics and Responsibility (Signature Edition)", "Thermal Management Design Mastery Capstone Project (Signature Edition)"],
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
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"thermal-management-design-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("thermal-management-design-signature",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
