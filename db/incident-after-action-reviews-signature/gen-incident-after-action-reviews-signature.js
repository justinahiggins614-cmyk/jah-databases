(function(){'use strict';
/* JAH incident-after-action-reviews-signature generator — jahdb-incident-after-action-reviews-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IAARS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Incident After-Action Reviews (Signature Edition)", "Core Concepts of Incident After-Action Reviews (Signature Edition)", "Essential Vocabulary for Incident After-Action Reviews (Signature Edition)", "Your First Incident After-Action Reviews Project (Signature Edition)", "Beginner Mistakes in Incident After-Action Reviews (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Incident After-Action Reviews (Signature Edition)", "Myths vs. Facts in Incident After-Action Reviews (Signature Edition)", "When to Start Incident After-Action Reviews (Signature Edition)", "Measuring the Basics in Incident After-Action Reviews (Signature Edition)", "Safety First in Incident After-Action Reviews (Signature Edition)", "Where to Find Help with Incident After-Action Reviews (Signature Edition)"], "Compounded": ["The Incident After-Action Reviews Workflow, Step by Step (Signature Edition)", "A Incident After-Action Reviews Decision Framework (Signature Edition)", "Incident After-Action Reviews Cost and Budget Planning (Signature Edition)", "Scheduling Incident After-Action Reviews Work (Signature Edition)", "Quality Checks for Incident After-Action Reviews (Signature Edition)", "Incident After-Action Reviews Troubleshooting Guide (Signature Edition)", "Intermediate Incident After-Action Reviews Skills (Signature Edition)", "Incident After-Action Reviews in Real-World Cases (Signature Edition)", "Comparing Incident After-Action Reviews Options (Signature Edition)", "Documenting Your Incident After-Action Reviews Work (Signature Edition)", "Collaborating on Incident After-Action Reviews (Signature Edition)", "Scaling Up Incident After-Action Reviews (Signature Edition)"], "Advanced": ["Advanced Incident After-Action Reviews Techniques (Signature Edition)", "Incident After-Action Reviews Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Incident After-Action Reviews (Signature Edition)", "Automating Incident After-Action Reviews (Signature Edition)", "Incident After-Action Reviews Long-Term Strategy (Signature Edition)", "Teaching Incident After-Action Reviews to Others (Signature Edition)", "Ethics and Responsibility in Incident After-Action Reviews (Signature Edition)", "Integrating Incident After-Action Reviews with Other Systems (Signature Edition)", "The Incident After-Action Reviews Frontier: What Comes Next (Signature Edition)", "The Incident After-Action Reviews Master Checklist (Signature Edition)", "Incident After-Action Reviews Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"incident-after-action-reviews-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-incident-after-action-reviews-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("incident-after-action-reviews-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
