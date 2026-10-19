(function(){'use strict';
/* JAH incident-after-action-reviews generator — jahdb-incident-after-action-reviews-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IAAR-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Incident After-Action Reviews", "Core Concepts of Incident After-Action Reviews", "Essential Vocabulary for Incident After-Action Reviews", "Your First Incident After-Action Reviews Project", "Beginner Mistakes in Incident After-Action Reviews (and How to Avoid Them)", "The Tools You Need for Incident After-Action Reviews", "Myths vs. Facts in Incident After-Action Reviews", "When to Start Incident After-Action Reviews", "Measuring the Basics in Incident After-Action Reviews", "Safety First in Incident After-Action Reviews", "Where to Find Help with Incident After-Action Reviews"], "Compounded": ["The Incident After-Action Reviews Workflow, Step by Step", "A Incident After-Action Reviews Decision Framework", "Incident After-Action Reviews Cost and Budget Planning", "Scheduling Incident After-Action Reviews Work", "Quality Checks for Incident After-Action Reviews", "Incident After-Action Reviews Troubleshooting Guide", "Intermediate Incident After-Action Reviews Skills", "Incident After-Action Reviews in Real-World Cases", "Comparing Incident After-Action Reviews Options", "Documenting Your Incident After-Action Reviews Work", "Collaborating on Incident After-Action Reviews", "Scaling Up Incident After-Action Reviews"], "Advanced": ["Advanced Incident After-Action Reviews Techniques", "Incident After-Action Reviews Edge Cases and Exceptions", "Auditing and Verifying Incident After-Action Reviews", "Automating Incident After-Action Reviews", "Incident After-Action Reviews Long-Term Strategy", "Teaching Incident After-Action Reviews to Others", "Ethics and Responsibility in Incident After-Action Reviews", "Integrating Incident After-Action Reviews with Other Systems", "The Incident After-Action Reviews Frontier: What Comes Next", "The Incident After-Action Reviews Master Checklist", "Incident After-Action Reviews Capstone Review: Putting It All Together"]};
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
    demo:{kind:"incident-after-action-reviews-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-incident-after-action-reviews-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("incident-after-action-reviews",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
