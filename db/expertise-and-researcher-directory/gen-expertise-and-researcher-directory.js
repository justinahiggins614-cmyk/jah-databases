(function(){'use strict';
/* JAH Public Expertise and Researcher Directory Database generator — jahdb-expertise-and-researcher-directory-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Sample records are clearly labeled and never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EXPEARD-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
"Foundations": ["The Essentials of Expertise and Researcher Directory", "Getting Started with Expertise and Researcher Directory in Plain Steps", "Expertise and Researcher Directory Glossary: Key Terms Explained", "Why Expertise and Researcher Directory Matters: The Real-World Payoff", "Expertise and Researcher Directory for Absolute Beginners", "The History and Context of Expertise and Researcher Directory", "Expertise and Researcher Directory: Common Myths Debunked", "The Five Building Blocks of Expertise and Researcher Directory", "Expertise and Researcher Directory in Everyday Life", "Expertise and Researcher Directory Basics Quiz and Answer Key", "A First Project in Expertise and Researcher Directory", "Expertise and Researcher Directory: What Success Looks Like"],
"Compounded": ["Expertise and Researcher Directory Step-by-Step Playbook", "Expertise and Researcher Directory Tools and Resources Directory", "Expertise and Researcher Directory Checklists You Can Use Today", "The 10 Most Common Expertise and Researcher Directory Mistakes", "Expertise and Researcher Directory Cost and Budget Guide", "Expertise and Researcher Directory Safety, Risk, and What Can Go Wrong", "Expertise and Researcher Directory Troubleshooting Guide", "Expertise and Researcher Directory for Busy People: The 80/20 Version", "Expertise and Researcher Directory Decision Framework", "Expertise and Researcher Directory: Comparing Your Options", "Expertise and Researcher Directory Templates and Worksheets", "Expertise and Researcher Directory Case Studies: Three Real Situations"],
"Advanced": ["Advanced Expertise and Researcher Directory Techniques", "Expertise and Researcher Directory Metrics: How to Measure Progress", "Expertise and Researcher Directory Systems and Automation", "Expertise and Researcher Directory Expert Interview Playbook", "Expertise and Researcher Directory Edge Cases and What to Do", "Teaching Expertise and Researcher Directory to Others", "Expertise and Researcher Directory Research Review: What the Evidence Says", "Expertise and Researcher Directory Planning Your Next 12 Months", "Expertise and Researcher Directory Ethics and Responsibility", "Expertise and Researcher Directory Mastery Capstone Project"],
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
    demo:{kind:"expertise-and-researcher-directory-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){JAHDB.registerGenerator("expertise-and-researcher-directory",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
