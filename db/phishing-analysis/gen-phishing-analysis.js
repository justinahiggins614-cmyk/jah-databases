(function(){'use strict';
/* JAH phishing-analysis generator — jahdb-phishing-analysis-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PA-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Phishing Analysis", "Core Concepts of Phishing Analysis", "Essential Vocabulary for Phishing Analysis", "Your First Phishing Analysis Project", "Beginner Mistakes in Phishing Analysis (and How to Avoid Them)", "The Tools You Need for Phishing Analysis", "Myths vs. Facts in Phishing Analysis", "When to Start Phishing Analysis", "Measuring the Basics in Phishing Analysis", "Safety First in Phishing Analysis", "Where to Find Help with Phishing Analysis"], "Compounded": ["The Phishing Analysis Workflow, Step by Step", "A Phishing Analysis Decision Framework", "Phishing Analysis Cost and Budget Planning", "Scheduling Phishing Analysis Work", "Quality Checks for Phishing Analysis", "Phishing Analysis Troubleshooting Guide", "Intermediate Phishing Analysis Skills", "Phishing Analysis in Real-World Cases", "Comparing Phishing Analysis Options", "Documenting Your Phishing Analysis Work", "Collaborating on Phishing Analysis", "Scaling Up Phishing Analysis"], "Advanced": ["Advanced Phishing Analysis Techniques", "Phishing Analysis Edge Cases and Exceptions", "Auditing and Verifying Phishing Analysis", "Automating Phishing Analysis", "Phishing Analysis Long-Term Strategy", "Teaching Phishing Analysis to Others", "Ethics and Responsibility in Phishing Analysis", "Integrating Phishing Analysis with Other Systems", "The Phishing Analysis Frontier: What Comes Next", "The Phishing Analysis Master Checklist", "Phishing Analysis Capstone Review: Putting It All Together"]};
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
    demo:{kind:"phishing-analysis-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-phishing-analysis-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("phishing-analysis",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
