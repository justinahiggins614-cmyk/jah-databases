(function(){'use strict';
/* JAH pregnancy-care-navigation generator — jahdb-pregnancy-care-navigation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PCN-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Pregnancy Care Navigation", "Core Concepts of Pregnancy Care Navigation", "Essential Vocabulary for Pregnancy Care Navigation", "Your First Pregnancy Care Navigation Project", "Beginner Mistakes in Pregnancy Care Navigation (and How to Avoid Them)", "The Tools You Need for Pregnancy Care Navigation", "Myths vs. Facts in Pregnancy Care Navigation", "When to Start Pregnancy Care Navigation", "Measuring the Basics in Pregnancy Care Navigation", "Safety First in Pregnancy Care Navigation", "Where to Find Help with Pregnancy Care Navigation"], "Compounded": ["The Pregnancy Care Navigation Workflow, Step by Step", "A Pregnancy Care Navigation Decision Framework", "Pregnancy Care Navigation Cost and Budget Planning", "Scheduling Pregnancy Care Navigation Work", "Quality Checks for Pregnancy Care Navigation", "Pregnancy Care Navigation Troubleshooting Guide", "Intermediate Pregnancy Care Navigation Skills", "Pregnancy Care Navigation in Real-World Cases", "Comparing Pregnancy Care Navigation Options", "Documenting Your Pregnancy Care Navigation Work", "Collaborating on Pregnancy Care Navigation", "Scaling Up Pregnancy Care Navigation"], "Advanced": ["Advanced Pregnancy Care Navigation Techniques", "Pregnancy Care Navigation Edge Cases and Exceptions", "Auditing and Verifying Pregnancy Care Navigation", "Automating Pregnancy Care Navigation", "Pregnancy Care Navigation Long-Term Strategy", "Teaching Pregnancy Care Navigation to Others", "Ethics and Responsibility in Pregnancy Care Navigation", "Integrating Pregnancy Care Navigation with Other Systems", "The Pregnancy Care Navigation Frontier: What Comes Next", "The Pregnancy Care Navigation Master Checklist", "Pregnancy Care Navigation Capstone Review: Putting It All Together"]};
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
    demo:{kind:"pregnancy-care-navigation-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-pregnancy-care-navigation-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("pregnancy-care-navigation",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
