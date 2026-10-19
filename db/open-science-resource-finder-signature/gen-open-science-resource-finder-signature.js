(function(){'use strict';
/* JAH Signature Open Science Resource Finder Database generator — jahdb-open-science-resource-finder-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OPENSR1-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Open Science Resource Finder (Signature Edition)", "Getting Started with Open Science Resource Finder in Plain Steps (Signature Edition)", "Open Science Resource Finder Glossary: Key Terms Explained (Signature Edition)", "Why Open Science Resource Finder Matters: The Real-World Payoff (Signature Edition)", "Open Science Resource Finder for Absolute Beginners (Signature Edition)", "The History and Context of Open Science Resource Finder (Signature Edition)", "Open Science Resource Finder: Common Myths Debunked (Signature Edition)", "The Five Building Blocks of Open Science Resource Finder (Signature Edition)", "Open Science Resource Finder in Everyday Life (Signature Edition)", "Open Science Resource Finder Basics Quiz and Answer Key (Signature Edition)", "A First Project in Open Science Resource Finder (Signature Edition)", "Open Science Resource Finder: What Success Looks Like (Signature Edition)"],
"Compounded": ["Open Science Resource Finder Step-by-Step Playbook (Signature Edition)", "Open Science Resource Finder Tools and Resources Directory (Signature Edition)", "Open Science Resource Finder Checklists You Can Use Today (Signature Edition)", "The 10 Most Common Open Science Resource Finder Mistakes (Signature Edition)", "Open Science Resource Finder Cost and Budget Guide (Signature Edition)", "Open Science Resource Finder Safety, Risk, and What Can Go Wrong (Signature Edition)", "Open Science Resource Finder Troubleshooting Guide (Signature Edition)", "Open Science Resource Finder for Busy People: The 80/20 Version (Signature Edition)", "Open Science Resource Finder Decision Framework (Signature Edition)", "Open Science Resource Finder: Comparing Your Options (Signature Edition)", "Open Science Resource Finder Templates and Worksheets (Signature Edition)", "Open Science Resource Finder Case Studies: Three Real Situations (Signature Edition)"],
"Advanced": ["Advanced Open Science Resource Finder Techniques (Signature Edition)", "Open Science Resource Finder Metrics: How to Measure Progress (Signature Edition)", "Open Science Resource Finder Systems and Automation (Signature Edition)", "Open Science Resource Finder Expert Interview Playbook (Signature Edition)", "Open Science Resource Finder Edge Cases and What to Do (Signature Edition)", "Teaching Open Science Resource Finder to Others (Signature Edition)", "Open Science Resource Finder Research Review: What the Evidence Says (Signature Edition)", "Open Science Resource Finder Planning Your Next 12 Months (Signature Edition)", "Open Science Resource Finder Ethics and Responsibility (Signature Edition)", "Open Science Resource Finder Mastery Capstone Project (Signature Edition)"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — resource record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — resource record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A resource record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"open-science-resource-finder-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("open-science-resource-finder-signature",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
