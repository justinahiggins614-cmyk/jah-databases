(function(){'use strict';
/* JAH Public Metadata Standards Database generator — jahdb-metadata-standards-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-METAS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Metadata Standards", "Getting Started with Metadata Standards in Plain Steps", "Metadata Standards Glossary: Key Terms Explained", "Why Metadata Standards Matters: The Real-World Payoff", "Metadata Standards for Absolute Beginners", "The History and Context of Metadata Standards", "Metadata Standards: Common Myths Debunked", "The Five Building Blocks of Metadata Standards", "Metadata Standards in Everyday Life", "Metadata Standards Basics Quiz and Answer Key", "A First Project in Metadata Standards", "Metadata Standards: What Success Looks Like"],
"Compounded": ["Metadata Standards Step-by-Step Playbook", "Metadata Standards Tools and Resources Directory", "Metadata Standards Checklists You Can Use Today", "The 10 Most Common Metadata Standards Mistakes", "Metadata Standards Cost and Budget Guide", "Metadata Standards Safety, Risk, and What Can Go Wrong", "Metadata Standards Troubleshooting Guide", "Metadata Standards for Busy People: The 80/20 Version", "Metadata Standards Decision Framework", "Metadata Standards: Comparing Your Options", "Metadata Standards Templates and Worksheets", "Metadata Standards Case Studies: Three Real Situations"],
"Advanced": ["Advanced Metadata Standards Techniques", "Metadata Standards Metrics: How to Measure Progress", "Metadata Standards Systems and Automation", "Metadata Standards Expert Interview Playbook", "Metadata Standards Edge Cases and What to Do", "Teaching Metadata Standards to Others", "Metadata Standards Research Review: What the Evidence Says", "Metadata Standards Planning Your Next 12 Months", "Metadata Standards Ethics and Responsibility", "Metadata Standards Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — standards record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — standards record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A standards record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"metadata-standards-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("metadata-standards",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
