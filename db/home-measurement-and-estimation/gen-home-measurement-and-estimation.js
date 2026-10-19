(function(){'use strict';
/* JAH home-measurement-and-estimation generator — jahdb-home-measurement-and-estimation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HMAE-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Home Measurement and Estimation", "Core Concepts of Home Measurement and Estimation", "Essential Vocabulary for Home Measurement and Estimation", "Your First Home Measurement and Estimation Project", "Beginner Mistakes in Home Measurement and Estimation (and How to Avoid Them)", "The Tools You Need for Home Measurement and Estimation", "Myths vs. Facts in Home Measurement and Estimation", "When to Start Home Measurement and Estimation", "Measuring the Basics in Home Measurement and Estimation", "Safety First in Home Measurement and Estimation", "Where to Find Help with Home Measurement and Estimation"], "Compounded": ["The Home Measurement and Estimation Workflow, Step by Step", "A Home Measurement and Estimation Decision Framework", "Home Measurement and Estimation Cost and Budget Planning", "Scheduling Home Measurement and Estimation Work", "Quality Checks for Home Measurement and Estimation", "Home Measurement and Estimation Troubleshooting Guide", "Intermediate Home Measurement and Estimation Skills", "Home Measurement and Estimation in Real-World Cases", "Comparing Home Measurement and Estimation Options", "Documenting Your Home Measurement and Estimation Work", "Collaborating on Home Measurement and Estimation", "Scaling Up Home Measurement and Estimation"], "Advanced": ["Advanced Home Measurement and Estimation Techniques", "Home Measurement and Estimation Edge Cases and Exceptions", "Auditing and Verifying Home Measurement and Estimation", "Automating Home Measurement and Estimation", "Home Measurement and Estimation Long-Term Strategy", "Teaching Home Measurement and Estimation to Others", "Ethics and Responsibility in Home Measurement and Estimation", "Integrating Home Measurement and Estimation with Other Systems", "The Home Measurement and Estimation Frontier: What Comes Next", "The Home Measurement and Estimation Master Checklist", "Home Measurement and Estimation Capstone Review: Putting It All Together"]};
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
    demo:{kind:"home-measurement-and-estimation-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-home-measurement-and-estimation-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("home-measurement-and-estimation",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
