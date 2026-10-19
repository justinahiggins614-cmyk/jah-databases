(function(){'use strict';
/* JAH personal-problem-solving generator — jahdb-personal-problem-solving-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Personal Problem-Solving", "Core Concepts of Personal Problem-Solving", "Essential Vocabulary for Personal Problem-Solving", "Your First Personal Problem-Solving Project", "Beginner Mistakes in Personal Problem-Solving (and How to Avoid Them)", "The Tools You Need for Personal Problem-Solving", "Myths vs. Facts in Personal Problem-Solving", "When to Start Personal Problem-Solving", "Measuring the Basics in Personal Problem-Solving", "Safety First in Personal Problem-Solving", "Where to Find Help with Personal Problem-Solving"], "Compounded": ["The Personal Problem-Solving Workflow, Step by Step", "A Personal Problem-Solving Decision Framework", "Personal Problem-Solving Cost and Budget Planning", "Scheduling Personal Problem-Solving Work", "Quality Checks for Personal Problem-Solving", "Personal Problem-Solving Troubleshooting Guide", "Intermediate Personal Problem-Solving Skills", "Personal Problem-Solving in Real-World Cases", "Comparing Personal Problem-Solving Options", "Documenting Your Personal Problem-Solving Work", "Collaborating on Personal Problem-Solving", "Scaling Up Personal Problem-Solving"], "Advanced": ["Advanced Personal Problem-Solving Techniques", "Personal Problem-Solving Edge Cases and Exceptions", "Auditing and Verifying Personal Problem-Solving", "Automating Personal Problem-Solving", "Personal Problem-Solving Long-Term Strategy", "Teaching Personal Problem-Solving to Others", "Ethics and Responsibility in Personal Problem-Solving", "Integrating Personal Problem-Solving with Other Systems", "The Personal Problem-Solving Frontier: What Comes Next", "The Personal Problem-Solving Master Checklist", "Personal Problem-Solving Capstone Review: Putting It All Together"]};
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
    demo:{kind:"personal-problem-solving-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-personal-problem-solving-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("personal-problem-solving",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
