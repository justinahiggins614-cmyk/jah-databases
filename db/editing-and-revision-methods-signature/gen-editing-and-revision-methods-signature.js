(function(){'use strict';
/* JAH Editing and Revision Methods Database generator — jahdb-editing-and-revision-methods-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EDITARMS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Editing Levels (Signature Edition)", "Cooling the Draft (Signature Edition)", "Structural Revision (Signature Edition)", "Cutting (Signature Edition)", "Line Editing (Signature Edition)", "Copyediting (Signature Edition)", "Proofreading (Signature Edition)", "Self-Editing (Signature Edition)", "Getting Feedback (Signature Edition)", "Editing Others (Signature Edition)", "Style Guides (Signature Edition)"], "Compounded": ["Teaching Editing (Signature Edition)", "The Editing Checklist (Signature Edition)", "Developmental Editing (Signature Edition)", "Paragraph Power (Signature Edition)", "Sentence Variety (Signature Edition)", "Active Voice (Signature Edition)", "Word Choice (Signature Edition)", "Dialogue Editing (Signature Edition)", "Show vs Tell (Signature Edition)", "Openings (Signature Edition)", "Endings (Signature Edition)", "Titles (Signature Edition)"], "Advanced": ["Fact-Checking (Signature Edition)", "Permissions (Signature Edition)", "Working With Editors (Signature Edition)", "Revision Timelines (Signature Edition)", "Editing Software (Signature Edition)", "The Final Read (Signature Edition)", "Publishing Prep (Signature Edition)", "Editing Poetry (Signature Edition)", "Editing Nonfiction (Signature Edition)", "The Editor's Career (Signature Edition)", "Self-Publishing Editing (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — editing guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — editing guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A editing guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"editing-and-revision-methods-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-editing-and-revision-methods-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("editing-and-revision-methods-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
