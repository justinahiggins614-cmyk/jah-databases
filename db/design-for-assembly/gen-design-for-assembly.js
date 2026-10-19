(function(){'use strict';
/* JAH design-for-assembly generator — jahdb-design-for-assembly-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DFA-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Design for Assembly", "Core Concepts of Design for Assembly", "Essential Vocabulary for Design for Assembly", "Your First Design for Assembly Project", "Beginner Mistakes in Design for Assembly (and How to Avoid Them)", "The Tools You Need for Design for Assembly", "Myths vs. Facts in Design for Assembly", "When to Start Design for Assembly", "Measuring the Basics in Design for Assembly", "Safety First in Design for Assembly", "Where to Find Help with Design for Assembly"], "Compounded": ["The Design for Assembly Workflow, Step by Step", "A Design for Assembly Decision Framework", "Design for Assembly Cost and Budget Planning", "Scheduling Design for Assembly Work", "Quality Checks for Design for Assembly", "Design for Assembly Troubleshooting Guide", "Intermediate Design for Assembly Skills", "Design for Assembly in Real-World Cases", "Comparing Design for Assembly Options", "Documenting Your Design for Assembly Work", "Collaborating on Design for Assembly", "Scaling Up Design for Assembly"], "Advanced": ["Advanced Design for Assembly Techniques", "Design for Assembly Edge Cases and Exceptions", "Auditing and Verifying Design for Assembly", "Automating Design for Assembly", "Design for Assembly Long-Term Strategy", "Teaching Design for Assembly to Others", "Ethics and Responsibility in Design for Assembly", "Integrating Design for Assembly with Other Systems", "The Design for Assembly Frontier: What Comes Next", "The Design for Assembly Master Checklist", "Design for Assembly Capstone Review: Putting It All Together"]};
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
    demo:{kind:"design-for-assembly-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-design-for-assembly-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("design-for-assembly",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
