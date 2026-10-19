(function(){'use strict';
/* JAH AI Basics Literacy Database generator — jahdb-ai-basics-literacy-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AIBLS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["What AI Actually Is (Signature Edition)", "Machine Learning Basics (Signature Edition)", "Neural Networks (Signature Edition)", "Large Language Models (Signature Edition)", "What AI Does Well (Signature Edition)", "What AI Does Poorly (Signature Edition)", "Prompting Basics (Signature Edition)", "Prompting Advanced (Signature Edition)", "Verifying AI Output (Signature Edition)", "AI in Daily Life (Signature Edition)", "AI in Work (Signature Edition)"], "Compounded": ["AI in Education (Signature Edition)", "AI in Healthcare (Signature Edition)", "AI in Business (Signature Edition)", "AI Ethics Basics (Signature Edition)", "AI Safety Concepts (Signature Edition)", "Generative AI (Signature Edition)", "Computer Vision (Signature Edition)", "AI and Jobs (Signature Edition)", "Learning AI Deeper (Signature Edition)", "AI History (Signature Edition)", "Data and AI (Signature Edition)", "AI Limitations (Signature Edition)"], "Advanced": ["Evaluating AI Tools (Signature Edition)", "AI Privacy (Signature Edition)", "AI and Creativity (Signature Edition)", "AI Regulation (Signature Edition)", "AI for Kids (Signature Edition)", "AI Myths (Signature Edition)", "Building With AI (Signature Edition)", "AI Communities (Signature Edition)", "Teaching AI Literacy (Signature Edition)", "Staying Current (Signature Edition)", "The Annual AI Review (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — AI literacy guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — AI literacy guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A AI literacy guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"ai-basics-literacy-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-ai-basics-literacy-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-basics-literacy-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
