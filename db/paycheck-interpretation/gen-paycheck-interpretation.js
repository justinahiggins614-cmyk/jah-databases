(function(){'use strict';
/* JAH paycheck-interpretation generator — jahdb-paycheck-interpretation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PI-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Paycheck Interpretation", "Core Concepts of Paycheck Interpretation", "Essential Vocabulary for Paycheck Interpretation", "Your First Paycheck Interpretation Project", "Beginner Mistakes in Paycheck Interpretation (and How to Avoid Them)", "The Tools You Need for Paycheck Interpretation", "Myths vs. Facts in Paycheck Interpretation", "When to Start Paycheck Interpretation", "Measuring the Basics in Paycheck Interpretation", "Safety First in Paycheck Interpretation", "Where to Find Help with Paycheck Interpretation"], "Compounded": ["The Paycheck Interpretation Workflow, Step by Step", "A Paycheck Interpretation Decision Framework", "Paycheck Interpretation Cost and Budget Planning", "Scheduling Paycheck Interpretation Work", "Quality Checks for Paycheck Interpretation", "Paycheck Interpretation Troubleshooting Guide", "Intermediate Paycheck Interpretation Skills", "Paycheck Interpretation in Real-World Cases", "Comparing Paycheck Interpretation Options", "Documenting Your Paycheck Interpretation Work", "Collaborating on Paycheck Interpretation", "Scaling Up Paycheck Interpretation"], "Advanced": ["Advanced Paycheck Interpretation Techniques", "Paycheck Interpretation Edge Cases and Exceptions", "Auditing and Verifying Paycheck Interpretation", "Automating Paycheck Interpretation", "Paycheck Interpretation Long-Term Strategy", "Teaching Paycheck Interpretation to Others", "Ethics and Responsibility in Paycheck Interpretation", "Integrating Paycheck Interpretation with Other Systems", "The Paycheck Interpretation Frontier: What Comes Next", "The Paycheck Interpretation Master Checklist", "Paycheck Interpretation Capstone Review: Putting It All Together"]};
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
    demo:{kind:"paycheck-interpretation-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-paycheck-interpretation-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("paycheck-interpretation",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
