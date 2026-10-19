(function(){'use strict';
/* JAH Public Account Compromise Recovery Database generator — jahdb-account-compromise-recovery-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ACCOCR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Account Compromise Recovery", "Getting Started with Account Compromise Recovery in Plain Steps", "Account Compromise Recovery Glossary: Key Terms Explained", "Why Account Compromise Recovery Matters: The Real-World Payoff", "Account Compromise Recovery for Absolute Beginners", "The History and Context of Account Compromise Recovery", "Account Compromise Recovery: Common Myths Debunked", "The Five Building Blocks of Account Compromise Recovery", "Account Compromise Recovery in Everyday Life", "Account Compromise Recovery Basics Quiz and Answer Key", "A First Project in Account Compromise Recovery", "Account Compromise Recovery: What Success Looks Like"],
"Compounded": ["Account Compromise Recovery Step-by-Step Playbook", "Account Compromise Recovery Tools and Resources Directory", "Account Compromise Recovery Checklists You Can Use Today", "The 10 Most Common Account Compromise Recovery Mistakes", "Account Compromise Recovery Cost and Budget Guide", "Account Compromise Recovery Safety, Risk, and What Can Go Wrong", "Account Compromise Recovery Troubleshooting Guide", "Account Compromise Recovery for Busy People: The 80/20 Version", "Account Compromise Recovery Decision Framework", "Account Compromise Recovery: Comparing Your Options", "Account Compromise Recovery Templates and Worksheets", "Account Compromise Recovery Case Studies: Three Real Situations"],
"Advanced": ["Advanced Account Compromise Recovery Techniques", "Account Compromise Recovery Metrics: How to Measure Progress", "Account Compromise Recovery Systems and Automation", "Account Compromise Recovery Expert Interview Playbook", "Account Compromise Recovery Edge Cases and What to Do", "Teaching Account Compromise Recovery to Others", "Account Compromise Recovery Research Review: What the Evidence Says", "Account Compromise Recovery Planning Your Next 12 Months", "Account Compromise Recovery Ethics and Responsibility", "Account Compromise Recovery Mastery Capstone Project"],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — recovery guide sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — recovery guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A recovery guide of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"account-compromise-recovery-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("account-compromise-recovery",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
