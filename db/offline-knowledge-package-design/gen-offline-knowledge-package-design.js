(function(){'use strict';
/* JAH offline-knowledge-package-design generator — jahdb-offline-knowledge-package-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OKPD-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Offline Knowledge Package Design", "Core Concepts of Offline Knowledge Package Design", "Essential Vocabulary for Offline Knowledge Package Design", "Your First Offline Knowledge Package Design Project", "Beginner Mistakes in Offline Knowledge Package Design (and How to Avoid Them)", "The Tools You Need for Offline Knowledge Package Design", "Myths vs. Facts in Offline Knowledge Package Design", "When to Start Offline Knowledge Package Design", "Measuring the Basics in Offline Knowledge Package Design", "Safety First in Offline Knowledge Package Design", "Where to Find Help with Offline Knowledge Package Design"], "Compounded": ["The Offline Knowledge Package Design Workflow, Step by Step", "A Offline Knowledge Package Design Decision Framework", "Offline Knowledge Package Design Cost and Budget Planning", "Scheduling Offline Knowledge Package Design Work", "Quality Checks for Offline Knowledge Package Design", "Offline Knowledge Package Design Troubleshooting Guide", "Intermediate Offline Knowledge Package Design Skills", "Offline Knowledge Package Design in Real-World Cases", "Comparing Offline Knowledge Package Design Options", "Documenting Your Offline Knowledge Package Design Work", "Collaborating on Offline Knowledge Package Design", "Scaling Up Offline Knowledge Package Design"], "Advanced": ["Advanced Offline Knowledge Package Design Techniques", "Offline Knowledge Package Design Edge Cases and Exceptions", "Auditing and Verifying Offline Knowledge Package Design", "Automating Offline Knowledge Package Design", "Offline Knowledge Package Design Long-Term Strategy", "Teaching Offline Knowledge Package Design to Others", "Ethics and Responsibility in Offline Knowledge Package Design", "Integrating Offline Knowledge Package Design with Other Systems", "The Offline Knowledge Package Design Frontier: What Comes Next", "The Offline Knowledge Package Design Master Checklist", "Offline Knowledge Package Design Capstone Review: Putting It All Together"]};
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
    demo:{kind:"offline-knowledge-package-design-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-offline-knowledge-package-design-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("offline-knowledge-package-design",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
