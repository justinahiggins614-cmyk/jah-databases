(function(){'use strict';
/* JAH home-energy-audit-signature generator — jahdb-home-energy-audit-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HEAS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Home Energy Audit (Signature Edition)", "Core Concepts of Home Energy Audit (Signature Edition)", "Essential Vocabulary for Home Energy Audit (Signature Edition)", "Your First Home Energy Audit Project (Signature Edition)", "Beginner Mistakes in Home Energy Audit (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Home Energy Audit (Signature Edition)", "Myths vs. Facts in Home Energy Audit (Signature Edition)", "When to Start Home Energy Audit (Signature Edition)", "Measuring the Basics in Home Energy Audit (Signature Edition)", "Safety First in Home Energy Audit (Signature Edition)", "Where to Find Help with Home Energy Audit (Signature Edition)"], "Compounded": ["The Home Energy Audit Workflow, Step by Step (Signature Edition)", "A Home Energy Audit Decision Framework (Signature Edition)", "Home Energy Audit Cost and Budget Planning (Signature Edition)", "Scheduling Home Energy Audit Work (Signature Edition)", "Quality Checks for Home Energy Audit (Signature Edition)", "Home Energy Audit Troubleshooting Guide (Signature Edition)", "Intermediate Home Energy Audit Skills (Signature Edition)", "Home Energy Audit in Real-World Cases (Signature Edition)", "Comparing Home Energy Audit Options (Signature Edition)", "Documenting Your Home Energy Audit Work (Signature Edition)", "Collaborating on Home Energy Audit (Signature Edition)", "Scaling Up Home Energy Audit (Signature Edition)"], "Advanced": ["Advanced Home Energy Audit Techniques (Signature Edition)", "Home Energy Audit Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Home Energy Audit (Signature Edition)", "Automating Home Energy Audit (Signature Edition)", "Home Energy Audit Long-Term Strategy (Signature Edition)", "Teaching Home Energy Audit to Others (Signature Edition)", "Ethics and Responsibility in Home Energy Audit (Signature Edition)", "Integrating Home Energy Audit with Other Systems (Signature Edition)", "The Home Energy Audit Frontier: What Comes Next (Signature Edition)", "The Home Energy Audit Master Checklist (Signature Edition)", "Home Energy Audit Capstone Review: Putting It All Together (Signature Edition)"]};
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
    description:'SAMPLE RECORD (generated — structural sample). A Signature-original sample of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"home-energy-audit-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-home-energy-audit-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("home-energy-audit-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
