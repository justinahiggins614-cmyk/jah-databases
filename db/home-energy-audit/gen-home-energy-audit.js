(function(){'use strict';
/* JAH home-energy-audit generator — jahdb-home-energy-audit-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HEA-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Home Energy Audit", "Core Concepts of Home Energy Audit", "Essential Vocabulary for Home Energy Audit", "Your First Home Energy Audit Project", "Beginner Mistakes in Home Energy Audit (and How to Avoid Them)", "The Tools You Need for Home Energy Audit", "Myths vs. Facts in Home Energy Audit", "When to Start Home Energy Audit", "Measuring the Basics in Home Energy Audit", "Safety First in Home Energy Audit", "Where to Find Help with Home Energy Audit"], "Compounded": ["The Home Energy Audit Workflow, Step by Step", "A Home Energy Audit Decision Framework", "Home Energy Audit Cost and Budget Planning", "Scheduling Home Energy Audit Work", "Quality Checks for Home Energy Audit", "Home Energy Audit Troubleshooting Guide", "Intermediate Home Energy Audit Skills", "Home Energy Audit in Real-World Cases", "Comparing Home Energy Audit Options", "Documenting Your Home Energy Audit Work", "Collaborating on Home Energy Audit", "Scaling Up Home Energy Audit"], "Advanced": ["Advanced Home Energy Audit Techniques", "Home Energy Audit Edge Cases and Exceptions", "Auditing and Verifying Home Energy Audit", "Automating Home Energy Audit", "Home Energy Audit Long-Term Strategy", "Teaching Home Energy Audit to Others", "Ethics and Responsibility in Home Energy Audit", "Integrating Home Energy Audit with Other Systems", "The Home Energy Audit Frontier: What Comes Next", "The Home Energy Audit Master Checklist", "Home Energy Audit Capstone Review: Putting It All Together"]};
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
    demo:{kind:"home-energy-audit-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-home-energy-audit-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("home-energy-audit",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
