(function(){'use strict';
/* JAH research-question-design generator — jahdb-research-question-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RQD-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Research Question Design", "Core Concepts of Research Question Design", "Essential Vocabulary for Research Question Design", "Your First Research Question Design Project", "Beginner Mistakes in Research Question Design (and How to Avoid Them)", "The Tools You Need for Research Question Design", "Myths vs. Facts in Research Question Design", "When to Start Research Question Design", "Measuring the Basics in Research Question Design", "Safety First in Research Question Design", "Where to Find Help with Research Question Design"], "Compounded": ["The Research Question Design Workflow, Step by Step", "A Research Question Design Decision Framework", "Research Question Design Cost and Budget Planning", "Scheduling Research Question Design Work", "Quality Checks for Research Question Design", "Research Question Design Troubleshooting Guide", "Intermediate Research Question Design Skills", "Research Question Design in Real-World Cases", "Comparing Research Question Design Options", "Documenting Your Research Question Design Work", "Collaborating on Research Question Design", "Scaling Up Research Question Design"], "Advanced": ["Advanced Research Question Design Techniques", "Research Question Design Edge Cases and Exceptions", "Auditing and Verifying Research Question Design", "Automating Research Question Design", "Research Question Design Long-Term Strategy", "Teaching Research Question Design to Others", "Ethics and Responsibility in Research Question Design", "Integrating Research Question Design with Other Systems", "The Research Question Design Frontier: What Comes Next", "The Research Question Design Master Checklist", "Research Question Design Capstone Review: Putting It All Together"]};
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
    demo:{kind:"research-question-design-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-research-question-design-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("research-question-design",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
