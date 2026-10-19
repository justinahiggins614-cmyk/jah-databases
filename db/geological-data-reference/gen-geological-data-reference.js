(function(){'use strict';
/* JAH geological-data-reference generator — jahdb-geological-data-reference-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GDR-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Geological Data Reference", "Core Concepts of Geological Data Reference", "Essential Vocabulary for Geological Data Reference", "Your First Geological Data Reference Project", "Beginner Mistakes in Geological Data Reference (and How to Avoid Them)", "The Tools You Need for Geological Data Reference", "Myths vs. Facts in Geological Data Reference", "When to Start Geological Data Reference", "Measuring the Basics in Geological Data Reference", "Safety First in Geological Data Reference", "Where to Find Help with Geological Data Reference"], "Compounded": ["The Geological Data Reference Workflow, Step by Step", "A Geological Data Reference Decision Framework", "Geological Data Reference Cost and Budget Planning", "Scheduling Geological Data Reference Work", "Quality Checks for Geological Data Reference", "Geological Data Reference Troubleshooting Guide", "Intermediate Geological Data Reference Skills", "Geological Data Reference in Real-World Cases", "Comparing Geological Data Reference Options", "Documenting Your Geological Data Reference Work", "Collaborating on Geological Data Reference", "Scaling Up Geological Data Reference"], "Advanced": ["Advanced Geological Data Reference Techniques", "Geological Data Reference Edge Cases and Exceptions", "Auditing and Verifying Geological Data Reference", "Automating Geological Data Reference", "Geological Data Reference Long-Term Strategy", "Teaching Geological Data Reference to Others", "Ethics and Responsibility in Geological Data Reference", "Integrating Geological Data Reference with Other Systems", "The Geological Data Reference Frontier: What Comes Next", "The Geological Data Reference Master Checklist", "Geological Data Reference Capstone Review: Putting It All Together"]};
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
    demo:{kind:"geological-data-reference-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-geological-data-reference-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("geological-data-reference",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
