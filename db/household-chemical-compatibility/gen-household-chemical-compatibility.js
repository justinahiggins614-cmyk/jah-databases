(function(){'use strict';
/* JAH household-chemical-compatibility generator — jahdb-household-chemical-compatibility-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HCC-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Household Chemical Compatibility", "Core Concepts of Household Chemical Compatibility", "Essential Vocabulary for Household Chemical Compatibility", "Your First Household Chemical Compatibility Project", "Beginner Mistakes in Household Chemical Compatibility (and How to Avoid Them)", "The Tools You Need for Household Chemical Compatibility", "Myths vs. Facts in Household Chemical Compatibility", "When to Start Household Chemical Compatibility", "Measuring the Basics in Household Chemical Compatibility", "Safety First in Household Chemical Compatibility", "Where to Find Help with Household Chemical Compatibility"], "Compounded": ["The Household Chemical Compatibility Workflow, Step by Step", "A Household Chemical Compatibility Decision Framework", "Household Chemical Compatibility Cost and Budget Planning", "Scheduling Household Chemical Compatibility Work", "Quality Checks for Household Chemical Compatibility", "Household Chemical Compatibility Troubleshooting Guide", "Intermediate Household Chemical Compatibility Skills", "Household Chemical Compatibility in Real-World Cases", "Comparing Household Chemical Compatibility Options", "Documenting Your Household Chemical Compatibility Work", "Collaborating on Household Chemical Compatibility", "Scaling Up Household Chemical Compatibility"], "Advanced": ["Advanced Household Chemical Compatibility Techniques", "Household Chemical Compatibility Edge Cases and Exceptions", "Auditing and Verifying Household Chemical Compatibility", "Automating Household Chemical Compatibility", "Household Chemical Compatibility Long-Term Strategy", "Teaching Household Chemical Compatibility to Others", "Ethics and Responsibility in Household Chemical Compatibility", "Integrating Household Chemical Compatibility with Other Systems", "The Household Chemical Compatibility Frontier: What Comes Next", "The Household Chemical Compatibility Master Checklist", "Household Chemical Compatibility Capstone Review: Putting It All Together"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — problem-solving guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — problem-solving guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A public-record sample of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"household-chemical-compatibility-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-household-chemical-compatibility-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("household-chemical-compatibility",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
