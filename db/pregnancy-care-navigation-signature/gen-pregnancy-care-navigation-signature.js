(function(){'use strict';
/* JAH pregnancy-care-navigation-signature generator — jahdb-pregnancy-care-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PCNS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Pregnancy Care Navigation (Signature Edition)", "Core Concepts of Pregnancy Care Navigation (Signature Edition)", "Essential Vocabulary for Pregnancy Care Navigation (Signature Edition)", "Your First Pregnancy Care Navigation Project (Signature Edition)", "Beginner Mistakes in Pregnancy Care Navigation (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Pregnancy Care Navigation (Signature Edition)", "Myths vs. Facts in Pregnancy Care Navigation (Signature Edition)", "When to Start Pregnancy Care Navigation (Signature Edition)", "Measuring the Basics in Pregnancy Care Navigation (Signature Edition)", "Safety First in Pregnancy Care Navigation (Signature Edition)", "Where to Find Help with Pregnancy Care Navigation (Signature Edition)"], "Compounded": ["The Pregnancy Care Navigation Workflow, Step by Step (Signature Edition)", "A Pregnancy Care Navigation Decision Framework (Signature Edition)", "Pregnancy Care Navigation Cost and Budget Planning (Signature Edition)", "Scheduling Pregnancy Care Navigation Work (Signature Edition)", "Quality Checks for Pregnancy Care Navigation (Signature Edition)", "Pregnancy Care Navigation Troubleshooting Guide (Signature Edition)", "Intermediate Pregnancy Care Navigation Skills (Signature Edition)", "Pregnancy Care Navigation in Real-World Cases (Signature Edition)", "Comparing Pregnancy Care Navigation Options (Signature Edition)", "Documenting Your Pregnancy Care Navigation Work (Signature Edition)", "Collaborating on Pregnancy Care Navigation (Signature Edition)", "Scaling Up Pregnancy Care Navigation (Signature Edition)"], "Advanced": ["Advanced Pregnancy Care Navigation Techniques (Signature Edition)", "Pregnancy Care Navigation Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Pregnancy Care Navigation (Signature Edition)", "Automating Pregnancy Care Navigation (Signature Edition)", "Pregnancy Care Navigation Long-Term Strategy (Signature Edition)", "Teaching Pregnancy Care Navigation to Others (Signature Edition)", "Ethics and Responsibility in Pregnancy Care Navigation (Signature Edition)", "Integrating Pregnancy Care Navigation with Other Systems (Signature Edition)", "The Pregnancy Care Navigation Frontier: What Comes Next (Signature Edition)", "The Pregnancy Care Navigation Master Checklist (Signature Edition)", "Pregnancy Care Navigation Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"pregnancy-care-navigation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-pregnancy-care-navigation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("pregnancy-care-navigation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
