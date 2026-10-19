(function(){'use strict';
/* JAH personal-milestone-planning generator — jahdb-personal-milestone-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PMP-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Personal Milestone Planning", "Core Concepts of Personal Milestone Planning", "Essential Vocabulary for Personal Milestone Planning", "Your First Personal Milestone Planning Project", "Beginner Mistakes in Personal Milestone Planning (and How to Avoid Them)", "The Tools You Need for Personal Milestone Planning", "Myths vs. Facts in Personal Milestone Planning", "When to Start Personal Milestone Planning", "Measuring the Basics in Personal Milestone Planning", "Safety First in Personal Milestone Planning", "Where to Find Help with Personal Milestone Planning"], "Compounded": ["The Personal Milestone Planning Workflow, Step by Step", "A Personal Milestone Planning Decision Framework", "Personal Milestone Planning Cost and Budget Planning", "Scheduling Personal Milestone Planning Work", "Quality Checks for Personal Milestone Planning", "Personal Milestone Planning Troubleshooting Guide", "Intermediate Personal Milestone Planning Skills", "Personal Milestone Planning in Real-World Cases", "Comparing Personal Milestone Planning Options", "Documenting Your Personal Milestone Planning Work", "Collaborating on Personal Milestone Planning", "Scaling Up Personal Milestone Planning"], "Advanced": ["Advanced Personal Milestone Planning Techniques", "Personal Milestone Planning Edge Cases and Exceptions", "Auditing and Verifying Personal Milestone Planning", "Automating Personal Milestone Planning", "Personal Milestone Planning Long-Term Strategy", "Teaching Personal Milestone Planning to Others", "Ethics and Responsibility in Personal Milestone Planning", "Integrating Personal Milestone Planning with Other Systems", "The Personal Milestone Planning Frontier: What Comes Next", "The Personal Milestone Planning Master Checklist", "Personal Milestone Planning Capstone Review: Putting It All Together"]};
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
    demo:{kind:"personal-milestone-planning-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-personal-milestone-planning-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("personal-milestone-planning",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
