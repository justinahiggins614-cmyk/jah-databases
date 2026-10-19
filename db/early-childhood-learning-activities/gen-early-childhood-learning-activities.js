(function(){'use strict';
/* JAH early-childhood-learning-activities generator — jahdb-early-childhood-learning-activities-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ECLA-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Early Childhood Learning Activities", "Core Concepts of Early Childhood Learning Activities", "Essential Vocabulary for Early Childhood Learning Activities", "Your First Early Childhood Learning Activities Project", "Beginner Mistakes in Early Childhood Learning Activities (and How to Avoid Them)", "The Tools You Need for Early Childhood Learning Activities", "Myths vs. Facts in Early Childhood Learning Activities", "When to Start Early Childhood Learning Activities", "Measuring the Basics in Early Childhood Learning Activities", "Safety First in Early Childhood Learning Activities", "Where to Find Help with Early Childhood Learning Activities"], "Compounded": ["The Early Childhood Learning Activities Workflow, Step by Step", "A Early Childhood Learning Activities Decision Framework", "Early Childhood Learning Activities Cost and Budget Planning", "Scheduling Early Childhood Learning Activities Work", "Quality Checks for Early Childhood Learning Activities", "Early Childhood Learning Activities Troubleshooting Guide", "Intermediate Early Childhood Learning Activities Skills", "Early Childhood Learning Activities in Real-World Cases", "Comparing Early Childhood Learning Activities Options", "Documenting Your Early Childhood Learning Activities Work", "Collaborating on Early Childhood Learning Activities", "Scaling Up Early Childhood Learning Activities"], "Advanced": ["Advanced Early Childhood Learning Activities Techniques", "Early Childhood Learning Activities Edge Cases and Exceptions", "Auditing and Verifying Early Childhood Learning Activities", "Automating Early Childhood Learning Activities", "Early Childhood Learning Activities Long-Term Strategy", "Teaching Early Childhood Learning Activities to Others", "Ethics and Responsibility in Early Childhood Learning Activities", "Integrating Early Childhood Learning Activities with Other Systems", "The Early Childhood Learning Activities Frontier: What Comes Next", "The Early Childhood Learning Activities Master Checklist", "Early Childhood Learning Activities Capstone Review: Putting It All Together"]};
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
    demo:{kind:"early-childhood-learning-activities-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-early-childhood-learning-activities-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("early-childhood-learning-activities",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
