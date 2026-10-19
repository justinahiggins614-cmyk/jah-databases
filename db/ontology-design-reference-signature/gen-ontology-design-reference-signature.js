(function(){'use strict';
/* JAH Signature Ontology Design Reference Database generator — jahdb-ontology-design-reference-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ONTODRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Ontology Design Reference (Signature Edition)", "Getting Started with Ontology Design Reference in Plain Steps (Signature Edition)", "Ontology Design Reference Glossary: Key Terms Explained (Signature Edition)", "Why Ontology Design Reference Matters: The Real-World Payoff (Signature Edition)", "Ontology Design Reference for Absolute Beginners (Signature Edition)", "The History and Context of Ontology Design Reference (Signature Edition)", "Ontology Design Reference: Common Myths Debunked (Signature Edition)", "The Five Building Blocks of Ontology Design Reference (Signature Edition)", "Ontology Design Reference in Everyday Life (Signature Edition)", "Ontology Design Reference Basics Quiz and Answer Key (Signature Edition)", "A First Project in Ontology Design Reference (Signature Edition)", "Ontology Design Reference: What Success Looks Like (Signature Edition)"],
"Compounded": ["Ontology Design Reference Step-by-Step Playbook (Signature Edition)", "Ontology Design Reference Tools and Resources Directory (Signature Edition)", "Ontology Design Reference Checklists You Can Use Today (Signature Edition)", "The 10 Most Common Ontology Design Reference Mistakes (Signature Edition)", "Ontology Design Reference Cost and Budget Guide (Signature Edition)", "Ontology Design Reference Safety, Risk, and What Can Go Wrong (Signature Edition)", "Ontology Design Reference Troubleshooting Guide (Signature Edition)", "Ontology Design Reference for Busy People: The 80/20 Version (Signature Edition)", "Ontology Design Reference Decision Framework (Signature Edition)", "Ontology Design Reference: Comparing Your Options (Signature Edition)", "Ontology Design Reference Templates and Worksheets (Signature Edition)", "Ontology Design Reference Case Studies: Three Real Situations (Signature Edition)"],
"Advanced": ["Advanced Ontology Design Reference Techniques (Signature Edition)", "Ontology Design Reference Metrics: How to Measure Progress (Signature Edition)", "Ontology Design Reference Systems and Automation (Signature Edition)", "Ontology Design Reference Expert Interview Playbook (Signature Edition)", "Ontology Design Reference Edge Cases and What to Do (Signature Edition)", "Teaching Ontology Design Reference to Others (Signature Edition)", "Ontology Design Reference Research Review: What the Evidence Says (Signature Edition)", "Ontology Design Reference Planning Your Next 12 Months (Signature Edition)", "Ontology Design Reference Ethics and Responsibility (Signature Edition)", "Ontology Design Reference Mastery Capstone Project (Signature Edition)"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — design reference sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — design reference',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A design reference of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"ontology-design-reference-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("ontology-design-reference-signature",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
