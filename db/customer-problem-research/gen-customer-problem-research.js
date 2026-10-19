(function(){'use strict';
/* JAH customer-problem-research generator — jahdb-customer-problem-research-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPR-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Customer Problem Research", "Core Concepts of Customer Problem Research", "Essential Vocabulary for Customer Problem Research", "Your First Customer Problem Research Project", "Beginner Mistakes in Customer Problem Research (and How to Avoid Them)", "The Tools You Need for Customer Problem Research", "Myths vs. Facts in Customer Problem Research", "When to Start Customer Problem Research", "Measuring the Basics in Customer Problem Research", "Safety First in Customer Problem Research", "Where to Find Help with Customer Problem Research"], "Compounded": ["The Customer Problem Research Workflow, Step by Step", "A Customer Problem Research Decision Framework", "Customer Problem Research Cost and Budget Planning", "Scheduling Customer Problem Research Work", "Quality Checks for Customer Problem Research", "Customer Problem Research Troubleshooting Guide", "Intermediate Customer Problem Research Skills", "Customer Problem Research in Real-World Cases", "Comparing Customer Problem Research Options", "Documenting Your Customer Problem Research Work", "Collaborating on Customer Problem Research", "Scaling Up Customer Problem Research"], "Advanced": ["Advanced Customer Problem Research Techniques", "Customer Problem Research Edge Cases and Exceptions", "Auditing and Verifying Customer Problem Research", "Automating Customer Problem Research", "Customer Problem Research Long-Term Strategy", "Teaching Customer Problem Research to Others", "Ethics and Responsibility in Customer Problem Research", "Integrating Customer Problem Research with Other Systems", "The Customer Problem Research Frontier: What Comes Next", "The Customer Problem Research Master Checklist", "Customer Problem Research Capstone Review: Putting It All Together"]};
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
    demo:{kind:"customer-problem-research-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-customer-problem-research-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("customer-problem-research",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
