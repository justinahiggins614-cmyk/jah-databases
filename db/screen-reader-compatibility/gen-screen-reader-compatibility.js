(function(){'use strict';
/* JAH screen-reader-compatibility generator — jahdb-screen-reader-compatibility-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SRC-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Getting Started with Screen Reader Compatibility", "Core Concepts of Screen Reader Compatibility", "Essential Vocabulary for Screen Reader Compatibility", "Your First Screen Reader Compatibility Project", "Beginner Mistakes in Screen Reader Compatibility (and How to Avoid Them)", "The Tools You Need for Screen Reader Compatibility", "Myths vs. Facts in Screen Reader Compatibility", "When to Start Screen Reader Compatibility", "Measuring the Basics in Screen Reader Compatibility", "Safety First in Screen Reader Compatibility", "Where to Find Help with Screen Reader Compatibility"], "Compounded": ["The Screen Reader Compatibility Workflow, Step by Step", "A Screen Reader Compatibility Decision Framework", "Screen Reader Compatibility Cost and Budget Planning", "Scheduling Screen Reader Compatibility Work", "Quality Checks for Screen Reader Compatibility", "Screen Reader Compatibility Troubleshooting Guide", "Intermediate Screen Reader Compatibility Skills", "Screen Reader Compatibility in Real-World Cases", "Comparing Screen Reader Compatibility Options", "Documenting Your Screen Reader Compatibility Work", "Collaborating on Screen Reader Compatibility", "Scaling Up Screen Reader Compatibility"], "Advanced": ["Advanced Screen Reader Compatibility Techniques", "Screen Reader Compatibility Edge Cases and Exceptions", "Auditing and Verifying Screen Reader Compatibility", "Automating Screen Reader Compatibility", "Screen Reader Compatibility Long-Term Strategy", "Teaching Screen Reader Compatibility to Others", "Ethics and Responsibility in Screen Reader Compatibility", "Integrating Screen Reader Compatibility with Other Systems", "The Screen Reader Compatibility Frontier: What Comes Next", "The Screen Reader Compatibility Master Checklist", "Screen Reader Compatibility Capstone Review: Putting It All Together"]};
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
    demo:{kind:"screen-reader-compatibility-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-screen-reader-compatibility-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("screen-reader-compatibility",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
