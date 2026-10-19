(function(){'use strict';
/* JAH laboratory-result-terminology generator — jahdb-laboratory-result-terminology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LRT-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Laboratory Result Terminology", "Core Concepts of Laboratory Result Terminology", "Essential Vocabulary for Laboratory Result Terminology", "Your First Laboratory Result Terminology Project", "Beginner Mistakes in Laboratory Result Terminology (and How to Avoid Them)", "The Tools You Need for Laboratory Result Terminology", "Myths vs. Facts in Laboratory Result Terminology", "When to Start Laboratory Result Terminology", "Measuring the Basics in Laboratory Result Terminology", "Safety First in Laboratory Result Terminology", "Where to Find Help with Laboratory Result Terminology"], "Compounded": ["The Laboratory Result Terminology Workflow, Step by Step", "A Laboratory Result Terminology Decision Framework", "Laboratory Result Terminology Cost and Budget Planning", "Scheduling Laboratory Result Terminology Work", "Quality Checks for Laboratory Result Terminology", "Laboratory Result Terminology Troubleshooting Guide", "Intermediate Laboratory Result Terminology Skills", "Laboratory Result Terminology in Real-World Cases", "Comparing Laboratory Result Terminology Options", "Documenting Your Laboratory Result Terminology Work", "Collaborating on Laboratory Result Terminology", "Scaling Up Laboratory Result Terminology"], "Advanced": ["Advanced Laboratory Result Terminology Techniques", "Laboratory Result Terminology Edge Cases and Exceptions", "Auditing and Verifying Laboratory Result Terminology", "Automating Laboratory Result Terminology", "Laboratory Result Terminology Long-Term Strategy", "Teaching Laboratory Result Terminology to Others", "Ethics and Responsibility in Laboratory Result Terminology", "Integrating Laboratory Result Terminology with Other Systems", "The Laboratory Result Terminology Frontier: What Comes Next", "The Laboratory Result Terminology Master Checklist", "Laboratory Result Terminology Capstone Review: Putting It All Together"]};
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
    demo:{kind:"laboratory-result-terminology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-laboratory-result-terminology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("laboratory-result-terminology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
