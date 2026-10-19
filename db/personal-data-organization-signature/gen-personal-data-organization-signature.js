(function(){'use strict';
/* JAH personal-data-organization-signature generator — jahdb-personal-data-organization-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PDOS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Personal Data Organization (Signature Edition)", "Core Concepts of Personal Data Organization (Signature Edition)", "Essential Vocabulary for Personal Data Organization (Signature Edition)", "Your First Personal Data Organization Project (Signature Edition)", "Beginner Mistakes in Personal Data Organization (and How to Avoid Them) (Signature Edition)", "The Tools You Need for Personal Data Organization (Signature Edition)", "Myths vs. Facts in Personal Data Organization (Signature Edition)", "When to Start Personal Data Organization (Signature Edition)", "Measuring the Basics in Personal Data Organization (Signature Edition)", "Safety First in Personal Data Organization (Signature Edition)", "Where to Find Help with Personal Data Organization (Signature Edition)"], "Compounded": ["The Personal Data Organization Workflow, Step by Step (Signature Edition)", "A Personal Data Organization Decision Framework (Signature Edition)", "Personal Data Organization Cost and Budget Planning (Signature Edition)", "Scheduling Personal Data Organization Work (Signature Edition)", "Quality Checks for Personal Data Organization (Signature Edition)", "Personal Data Organization Troubleshooting Guide (Signature Edition)", "Intermediate Personal Data Organization Skills (Signature Edition)", "Personal Data Organization in Real-World Cases (Signature Edition)", "Comparing Personal Data Organization Options (Signature Edition)", "Documenting Your Personal Data Organization Work (Signature Edition)", "Collaborating on Personal Data Organization (Signature Edition)", "Scaling Up Personal Data Organization (Signature Edition)"], "Advanced": ["Advanced Personal Data Organization Techniques (Signature Edition)", "Personal Data Organization Edge Cases and Exceptions (Signature Edition)", "Auditing and Verifying Personal Data Organization (Signature Edition)", "Automating Personal Data Organization (Signature Edition)", "Personal Data Organization Long-Term Strategy (Signature Edition)", "Teaching Personal Data Organization to Others (Signature Edition)", "Ethics and Responsibility in Personal Data Organization (Signature Edition)", "Integrating Personal Data Organization with Other Systems (Signature Edition)", "The Personal Data Organization Frontier: What Comes Next (Signature Edition)", "The Personal Data Organization Master Checklist (Signature Edition)", "Personal Data Organization Capstone Review: Putting It All Together (Signature Edition)"]};
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
    demo:{kind:"personal-data-organization-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-personal-data-organization-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("personal-data-organization-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
