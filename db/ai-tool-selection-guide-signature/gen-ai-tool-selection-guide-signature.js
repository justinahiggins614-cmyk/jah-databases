(function(){'use strict';
/* JAH AI Tool Selection Guide Database generator — jahdb-ai-tool-selection-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AITSGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Defining Your Needs (Signature Edition)", "AI Chatbots Compared (Signature Edition)", "Free vs Paid Tiers (Signature Edition)", "Image Generators (Signature Edition)", "Coding Assistants (Signature Edition)", "Writing Assistants (Signature Edition)", "Meeting Assistants (Signature Edition)", "Research Assistants (Signature Edition)", "Automation Platforms (Signature Edition)", "Privacy Evaluation (Signature Edition)", "Cost Modeling (Signature Edition)"], "Compounded": ["Integration Fit (Signature Edition)", "Trial Methodology (Signature Edition)", "Vendor Stability (Signature Edition)", "For Individuals (Signature Edition)", "For Small Teams (Signature Edition)", "For Enterprises (Signature Edition)", "Avoiding Tool Sprawl (Signature Edition)", "Teaching Tool Selection (Signature Edition)", "The Annual Tool Audit (Signature Edition)", "Voice Assistants (Signature Edition)", "Video Generators (Signature Edition)", "Data Analysis Tools (Signature Edition)"], "Advanced": ["Customer Service AI (Signature Edition)", "Sales AI Tools (Signature Edition)", "HR AI Tools (Signature Edition)", "Legal AI Tools (Signature Edition)", "Design AI Tools (Signature Edition)", "Music and Audio AI (Signature Edition)", "Translation Tools (Signature Edition)", "Note-Taking AI (Signature Edition)", "Project Management AI (Signature Edition)", "Security AI Tools (Signature Edition)", "Build vs Buy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — tool guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — tool guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tool guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"ai-tool-selection-guide-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-ai-tool-selection-guide-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-tool-selection-guide-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
