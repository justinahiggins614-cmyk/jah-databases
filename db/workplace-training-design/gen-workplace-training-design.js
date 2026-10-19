(function(){'use strict';
/* JAH workplace-training-design generator — jahdb-workplace-training-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WTD-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Workplace Training Design", "Core Concepts of Workplace Training Design", "Essential Vocabulary for Workplace Training Design", "Your First Workplace Training Design Project", "Beginner Mistakes in Workplace Training Design (and How to Avoid Them)", "The Tools You Need for Workplace Training Design", "Myths vs. Facts in Workplace Training Design", "When to Start Workplace Training Design", "Measuring the Basics in Workplace Training Design", "Safety First in Workplace Training Design", "Where to Find Help with Workplace Training Design"], "Compounded": ["The Workplace Training Design Workflow, Step by Step", "A Workplace Training Design Decision Framework", "Workplace Training Design Cost and Budget Planning", "Scheduling Workplace Training Design Work", "Quality Checks for Workplace Training Design", "Workplace Training Design Troubleshooting Guide", "Intermediate Workplace Training Design Skills", "Workplace Training Design in Real-World Cases", "Comparing Workplace Training Design Options", "Documenting Your Workplace Training Design Work", "Collaborating on Workplace Training Design", "Scaling Up Workplace Training Design"], "Advanced": ["Advanced Workplace Training Design Techniques", "Workplace Training Design Edge Cases and Exceptions", "Auditing and Verifying Workplace Training Design", "Automating Workplace Training Design", "Workplace Training Design Long-Term Strategy", "Teaching Workplace Training Design to Others", "Ethics and Responsibility in Workplace Training Design", "Integrating Workplace Training Design with Other Systems", "The Workplace Training Design Frontier: What Comes Next", "The Workplace Training Design Master Checklist", "Workplace Training Design Capstone Review: Putting It All Together"]};
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
    demo:{kind:"workplace-training-design-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-workplace-training-design-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("workplace-training-design",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
