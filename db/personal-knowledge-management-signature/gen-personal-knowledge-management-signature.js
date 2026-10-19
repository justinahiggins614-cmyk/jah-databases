(function(){'use strict';
/* JAH Personal Knowledge Management Database generator — jahdb-personal-knowledge-management-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PERSKMS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Why Manage Knowledge (Signature Edition)", "Capture Habits (Signature Edition)", "Atomic Notes (Signature Edition)", "Writing in Your Words (Signature Edition)", "Linking Notes (Signature Edition)", "Zettelkasten Method (Signature Edition)", "PARA Organization (Signature Edition)", "Choosing Tools (Signature Edition)", "Weekly Reviews (Signature Edition)", "Retrieval Strategies (Signature Edition)", "Notes to Output (Signature Edition)"], "Compounded": ["Teaching PKM (Signature Edition)", "The Annual Knowledge Review (Signature Edition)", "Digital vs Analog (Signature Edition)", "The Commonplace Book (Signature Edition)", "Reading Workflows (Signature Edition)", "Meeting Notes (Signature Edition)", "Project Notes (Signature Edition)", "Literature Notes (Signature Edition)", "Fleeting Notes (Signature Edition)", "Evergreen Notes (Signature Edition)", "Maps of Content (Signature Edition)", "Search Strategies (Signature Edition)"], "Advanced": ["Tagging (Signature Edition)", "Daily Notes (Signature Edition)", "Spaced Repetition (Signature Edition)", "Thinking Tools (Signature Edition)", "Collaboration (Signature Edition)", "Privacy and Security (Signature Edition)", "Mobile Capture (Signature Edition)", "Avoiding Over-Engineering (Signature Edition)", "Measuring Value (Signature Edition)", "Starting Over (Signature Edition)", "The Knowledge Legacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — PKM guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — PKM guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A PKM guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"personal-knowledge-management-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-personal-knowledge-management-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("personal-knowledge-management-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
