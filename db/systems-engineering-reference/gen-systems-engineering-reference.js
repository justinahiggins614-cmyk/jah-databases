(function(){'use strict';
/* JAH systems-engineering-reference generator — jahdb-systems-engineering-reference-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SER-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Systems Engineering Reference", "Core Concepts of Systems Engineering Reference", "Essential Vocabulary for Systems Engineering Reference", "Your First Systems Engineering Reference Project", "Beginner Mistakes in Systems Engineering Reference (and How to Avoid Them)", "The Tools You Need for Systems Engineering Reference", "Myths vs. Facts in Systems Engineering Reference", "When to Start Systems Engineering Reference", "Measuring the Basics in Systems Engineering Reference", "Safety First in Systems Engineering Reference", "Where to Find Help with Systems Engineering Reference"], "Compounded": ["The Systems Engineering Reference Workflow, Step by Step", "A Systems Engineering Reference Decision Framework", "Systems Engineering Reference Cost and Budget Planning", "Scheduling Systems Engineering Reference Work", "Quality Checks for Systems Engineering Reference", "Systems Engineering Reference Troubleshooting Guide", "Intermediate Systems Engineering Reference Skills", "Systems Engineering Reference in Real-World Cases", "Comparing Systems Engineering Reference Options", "Documenting Your Systems Engineering Reference Work", "Collaborating on Systems Engineering Reference", "Scaling Up Systems Engineering Reference"], "Advanced": ["Advanced Systems Engineering Reference Techniques", "Systems Engineering Reference Edge Cases and Exceptions", "Auditing and Verifying Systems Engineering Reference", "Automating Systems Engineering Reference", "Systems Engineering Reference Long-Term Strategy", "Teaching Systems Engineering Reference to Others", "Ethics and Responsibility in Systems Engineering Reference", "Integrating Systems Engineering Reference with Other Systems", "The Systems Engineering Reference Frontier: What Comes Next", "The Systems Engineering Reference Master Checklist", "Systems Engineering Reference Capstone Review: Putting It All Together"]};
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
    demo:{kind:"systems-engineering-reference-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-systems-engineering-reference-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("systems-engineering-reference",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
