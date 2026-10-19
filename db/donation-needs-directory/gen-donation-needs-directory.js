(function(){'use strict';
/* JAH Public Donation Needs Directory Database generator — jahdb-donation-needs-directory-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DONAND-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Donation Needs Directory", "Getting Started with Donation Needs Directory in Plain Steps", "Donation Needs Directory Glossary: Key Terms Explained", "Why Donation Needs Directory Matters: The Real-World Payoff", "Donation Needs Directory for Absolute Beginners", "The History and Context of Donation Needs Directory", "Donation Needs Directory: Common Myths Debunked", "The Five Building Blocks of Donation Needs Directory", "Donation Needs Directory in Everyday Life", "Donation Needs Directory Basics Quiz and Answer Key", "A First Project in Donation Needs Directory", "Donation Needs Directory: What Success Looks Like"],
"Compounded": ["Donation Needs Directory Step-by-Step Playbook", "Donation Needs Directory Tools and Resources Directory", "Donation Needs Directory Checklists You Can Use Today", "The 10 Most Common Donation Needs Directory Mistakes", "Donation Needs Directory Cost and Budget Guide", "Donation Needs Directory Safety, Risk, and What Can Go Wrong", "Donation Needs Directory Troubleshooting Guide", "Donation Needs Directory for Busy People: The 80/20 Version", "Donation Needs Directory Decision Framework", "Donation Needs Directory: Comparing Your Options", "Donation Needs Directory Templates and Worksheets", "Donation Needs Directory Case Studies: Three Real Situations"],
"Advanced": ["Advanced Donation Needs Directory Techniques", "Donation Needs Directory Metrics: How to Measure Progress", "Donation Needs Directory Systems and Automation", "Donation Needs Directory Expert Interview Playbook", "Donation Needs Directory Edge Cases and What to Do", "Teaching Donation Needs Directory to Others", "Donation Needs Directory Research Review: What the Evidence Says", "Donation Needs Directory Planning Your Next 12 Months", "Donation Needs Directory Ethics and Responsibility", "Donation Needs Directory Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — directory record sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — directory record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A directory record of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"donation-needs-directory-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("donation-needs-directory",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
