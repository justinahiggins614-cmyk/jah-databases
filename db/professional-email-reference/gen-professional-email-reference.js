(function(){'use strict';
/* JAH professional-email-reference generator — jahdb-professional-email-reference-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PER-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Professional Email Reference", "Core Concepts of Professional Email Reference", "Essential Vocabulary for Professional Email Reference", "Your First Professional Email Reference Project", "Beginner Mistakes in Professional Email Reference (and How to Avoid Them)", "The Tools You Need for Professional Email Reference", "Myths vs. Facts in Professional Email Reference", "When to Start Professional Email Reference", "Measuring the Basics in Professional Email Reference", "Safety First in Professional Email Reference", "Where to Find Help with Professional Email Reference"], "Compounded": ["The Professional Email Reference Workflow, Step by Step", "A Professional Email Reference Decision Framework", "Professional Email Reference Cost and Budget Planning", "Scheduling Professional Email Reference Work", "Quality Checks for Professional Email Reference", "Professional Email Reference Troubleshooting Guide", "Intermediate Professional Email Reference Skills", "Professional Email Reference in Real-World Cases", "Comparing Professional Email Reference Options", "Documenting Your Professional Email Reference Work", "Collaborating on Professional Email Reference", "Scaling Up Professional Email Reference"], "Advanced": ["Advanced Professional Email Reference Techniques", "Professional Email Reference Edge Cases and Exceptions", "Auditing and Verifying Professional Email Reference", "Automating Professional Email Reference", "Professional Email Reference Long-Term Strategy", "Teaching Professional Email Reference to Others", "Ethics and Responsibility in Professional Email Reference", "Integrating Professional Email Reference with Other Systems", "The Professional Email Reference Frontier: What Comes Next", "The Professional Email Reference Master Checklist", "Professional Email Reference Capstone Review: Putting It All Together"]};
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
    demo:{kind:"professional-email-reference-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-professional-email-reference-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("professional-email-reference",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
