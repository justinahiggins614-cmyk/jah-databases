(function(){'use strict';
/* JAH Signature Database Administration Support Database generator — jahdb-database-administration-support-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DATAASS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Database Administration Support (Signature Edition)", "Getting Started with Database Administration Support in Plain Steps (Signature Edition)", "Database Administration Support Glossary: Key Terms Explained (Signature Edition)", "Why Database Administration Support Matters: The Real-World Payoff (Signature Edition)", "Database Administration Support for Absolute Beginners (Signature Edition)", "The History and Context of Database Administration Support (Signature Edition)", "Database Administration Support: Common Myths Debunked (Signature Edition)", "The Five Building Blocks of Database Administration Support (Signature Edition)", "Database Administration Support in Everyday Life (Signature Edition)", "Database Administration Support Basics Quiz and Answer Key (Signature Edition)", "A First Project in Database Administration Support (Signature Edition)", "Database Administration Support: What Success Looks Like (Signature Edition)"],
"Compounded": ["Database Administration Support Step-by-Step Playbook (Signature Edition)", "Database Administration Support Tools and Resources Directory (Signature Edition)", "Database Administration Support Checklists You Can Use Today (Signature Edition)", "The 10 Most Common Database Administration Support Mistakes (Signature Edition)", "Database Administration Support Cost and Budget Guide (Signature Edition)", "Database Administration Support Safety, Risk, and What Can Go Wrong (Signature Edition)", "Database Administration Support Troubleshooting Guide (Signature Edition)", "Database Administration Support for Busy People: The 80/20 Version (Signature Edition)", "Database Administration Support Decision Framework (Signature Edition)", "Database Administration Support: Comparing Your Options (Signature Edition)", "Database Administration Support Templates and Worksheets (Signature Edition)", "Database Administration Support Case Studies: Three Real Situations (Signature Edition)"],
"Advanced": ["Advanced Database Administration Support Techniques (Signature Edition)", "Database Administration Support Metrics: How to Measure Progress (Signature Edition)", "Database Administration Support Systems and Automation (Signature Edition)", "Database Administration Support Expert Interview Playbook (Signature Edition)", "Database Administration Support Edge Cases and What to Do (Signature Edition)", "Teaching Database Administration Support to Others (Signature Edition)", "Database Administration Support Research Review: What the Evidence Says (Signature Edition)", "Database Administration Support Planning Your Next 12 Months (Signature Edition)", "Database Administration Support Ethics and Responsibility (Signature Edition)", "Database Administration Support Mastery Capstone Project (Signature Edition)"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — support record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — support record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A support record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"database-administration-support-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("database-administration-support-signature",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
