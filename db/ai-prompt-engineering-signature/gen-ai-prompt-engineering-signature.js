(function(){'use strict';
/* JAH AI Prompt Engineering Database generator — jahdb-ai-prompt-engineering-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AIPES-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Prompt Anatomy (Signature Edition)", "Being Specific (Signature Edition)", "Context Setting (Signature Edition)", "Few-Shot Examples (Signature Edition)", "Zero-Shot Instructions (Signature Edition)", "Chain of Thought (Signature Edition)", "Role Prompting (Signature Edition)", "Format Constraints (Signature Edition)", "Decomposing Tasks (Signature Edition)", "Iterative Refinement (Signature Edition)", "System Prompts (Signature Edition)"], "Compounded": ["Prompt Templates (Signature Edition)", "Image Prompting (Signature Edition)", "Code Prompting (Signature Edition)", "Prompt Injection Awareness (Signature Edition)", "Evaluating Outputs (Signature Edition)", "Prompt Libraries (Signature Edition)", "Collaborative Prompting (Signature Edition)", "Domain Prompting (Signature Edition)", "Multilingual Prompting (Signature Edition)", "Long Context Use (Signature Edition)", "Prompt Chaining (Signature Edition)", "Negative Prompts (Signature Edition)"], "Advanced": ["Tone and Style Control (Signature Edition)", "Prompt Testing (Signature Edition)", "Cost Awareness (Signature Edition)", "Teaching Prompting (Signature Edition)", "Prompt Anti-Patterns (Signature Edition)", "Staying Current (Signature Edition)", "The Prompt Audit (Signature Edition)", "Prompt Versioning (Signature Edition)", "Few-Shot Selection (Signature Edition)", "Instruction Hierarchy (Signature Edition)", "Prompt Debugging (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — prompting guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — prompting guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A prompting guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"ai-prompt-engineering-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-ai-prompt-engineering-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-prompt-engineering-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
