(function(){'use strict';
/* JAH workplace-assistive-technology generator — jahdb-workplace-assistive-technology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WAT-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Workplace Assistive Technology", "Core Concepts of Workplace Assistive Technology", "Essential Vocabulary for Workplace Assistive Technology", "Your First Workplace Assistive Technology Project", "Beginner Mistakes in Workplace Assistive Technology (and How to Avoid Them)", "The Tools You Need for Workplace Assistive Technology", "Myths vs. Facts in Workplace Assistive Technology", "When to Start Workplace Assistive Technology", "Measuring the Basics in Workplace Assistive Technology", "Safety First in Workplace Assistive Technology", "Where to Find Help with Workplace Assistive Technology"], "Compounded": ["The Workplace Assistive Technology Workflow, Step by Step", "A Workplace Assistive Technology Decision Framework", "Workplace Assistive Technology Cost and Budget Planning", "Scheduling Workplace Assistive Technology Work", "Quality Checks for Workplace Assistive Technology", "Workplace Assistive Technology Troubleshooting Guide", "Intermediate Workplace Assistive Technology Skills", "Workplace Assistive Technology in Real-World Cases", "Comparing Workplace Assistive Technology Options", "Documenting Your Workplace Assistive Technology Work", "Collaborating on Workplace Assistive Technology", "Scaling Up Workplace Assistive Technology"], "Advanced": ["Advanced Workplace Assistive Technology Techniques", "Workplace Assistive Technology Edge Cases and Exceptions", "Auditing and Verifying Workplace Assistive Technology", "Automating Workplace Assistive Technology", "Workplace Assistive Technology Long-Term Strategy", "Teaching Workplace Assistive Technology to Others", "Ethics and Responsibility in Workplace Assistive Technology", "Integrating Workplace Assistive Technology with Other Systems", "The Workplace Assistive Technology Frontier: What Comes Next", "The Workplace Assistive Technology Master Checklist", "Workplace Assistive Technology Capstone Review: Putting It All Together"]};
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
    demo:{kind:"workplace-assistive-technology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-workplace-assistive-technology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("workplace-assistive-technology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
