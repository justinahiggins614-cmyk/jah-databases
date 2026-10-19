(function(){'use strict';
/* JAH data-provenance-tracking-signature generator — jahdb-data-provenance-tracking-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DPTS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Data Provenance Tracking (Signature Edition)", "Core Concepts of Data Provenance Tracking (Signature Edition)", "Essential Vocabulary for Data Provenance Tracking (Signature Edition)", "Your First Data Provenance Tracking Project (Signature Edition)", "Beginner Mistakes in Data Provenance Tracking (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Data Provenance Tracking (Signature Edition)", "Myths vs. Facts in Data Provenance Tracking (Signature Edition)", "When to Start Data Provenance Tracking (Signature Edition)", "Measuring the Basics in Data Provenance Tracking (Signature Edition)", "Safety First in Data Provenance Tracking (Signature Edition)", "Where to Find Help with Data Provenance Tracking (Signature Edition)"], "Compounded": ["The Data Provenance Tracking Workflow, Step by Step (Signature Edition)", "A Data Provenance Tracking Decision Framework (Signature Edition)", "Data Provenance Tracking Cost and Budget Planning (Signature Edition)", "Scheduling Data Provenance Tracking Work (Signature Edition)", "Quality Checks for Data Provenance Tracking (Signature Edition)", "Data Provenance Tracking Troubleshooting Guide (Signature Edition)", "Intermediate Data Provenance Tracking Skills (Signature Edition)", "Data Provenance Tracking in Real-World Cases (Signature Edition)", "Comparing Data Provenance Tracking Options (Signature Edition)", "Documenting Your Data Provenance Tracking Work (Signature Edition)", "Collaborating on Data Provenance Tracking (Signature Edition)", "Scaling Up Data Provenance Tracking (Signature Edition)"], "Advanced": ["Advanced Data Provenance Tracking Techniques (Signature Edition)", "Data Provenance Tracking Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Data Provenance Tracking (Signature Edition)", "Automating Data Provenance Tracking (Signature Edition)", "Data Provenance Tracking Long-Term Strategy (Signature Edition)", "Teaching Data Provenance Tracking to Others (Signature Edition)", "Ethics and Responsibility in Data Provenance Tracking (Signature Edition)", "Integrating Data Provenance Tracking with Other Systems (Signature Edition)", "The Data Provenance Tracking Frontier: What Comes Next (Signature Edition)", "The Data Provenance Tracking Master Checklist (Signature Edition)", "Data Provenance Tracking Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"data-provenance-tracking-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-data-provenance-tracking-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("data-provenance-tracking-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
