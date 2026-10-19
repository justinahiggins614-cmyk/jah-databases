(function(){'use strict';
/* JAH fare-and-pass-comparison generator — jahdb-fare-and-pass-comparison-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FAPC-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Fare and Pass Comparison", "Core Concepts of Fare and Pass Comparison", "Essential Vocabulary for Fare and Pass Comparison", "Your First Fare and Pass Comparison Project", "Beginner Mistakes in Fare and Pass Comparison (and How to Avoid Them)", "The Tools You Need for Fare and Pass Comparison", "Myths vs. Facts in Fare and Pass Comparison", "When to Start Fare and Pass Comparison", "Measuring the Basics in Fare and Pass Comparison", "Safety First in Fare and Pass Comparison", "Where to Find Help with Fare and Pass Comparison"], "Compounded": ["The Fare and Pass Comparison Workflow, Step by Step", "A Fare and Pass Comparison Decision Framework", "Fare and Pass Comparison Cost and Budget Planning", "Scheduling Fare and Pass Comparison Work", "Quality Checks for Fare and Pass Comparison", "Fare and Pass Comparison Troubleshooting Guide", "Intermediate Fare and Pass Comparison Skills", "Fare and Pass Comparison in Real-World Cases", "Comparing Fare and Pass Comparison Options", "Documenting Your Fare and Pass Comparison Work", "Collaborating on Fare and Pass Comparison", "Scaling Up Fare and Pass Comparison"], "Advanced": ["Advanced Fare and Pass Comparison Techniques", "Fare and Pass Comparison Edge Cases and Exceptions", "Auditing and Verifying Fare and Pass Comparison", "Automating Fare and Pass Comparison", "Fare and Pass Comparison Long-Term Strategy", "Teaching Fare and Pass Comparison to Others", "Ethics and Responsibility in Fare and Pass Comparison", "Integrating Fare and Pass Comparison with Other Systems", "The Fare and Pass Comparison Frontier: What Comes Next", "The Fare and Pass Comparison Master Checklist", "Fare and Pass Comparison Capstone Review: Putting It All Together"]};
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
    demo:{kind:"fare-and-pass-comparison-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-fare-and-pass-comparison-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fare-and-pass-comparison",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
