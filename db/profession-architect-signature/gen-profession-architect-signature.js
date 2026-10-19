(function(){'use strict';
/* JAH Signature Architect Profession Database generator — "jahdb-profession-architect-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PARS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["What Architects Do (Signature Edition)", "History of Architecture (Signature Edition)", "Core Design Skills (Signature Edition)", "Architecture School and the ARE (Signature Edition)", "Licensure: The Stamp (Signature Edition)", "Tools of the Trade (Signature Edition)", "A Day in the Life (Signature Edition)", "Firms and Practice Settings (Signature Edition)", "Architectural Ethics (Signature Edition)", "Pay and Career Outlook (Signature Edition)", "Giants of Architecture (Signature Edition)", "Getting Started (Signature Edition)"], "Compounded": ["The Design Process (Signature Edition)", "Construction Documents (Signature Edition)", "Structure: The Engineer's Duet (Signature Edition)", "Sustainable Design (Signature Edition)", "The Client Relationship (Signature Edition)", "Construction Administration (Signature Edition)", "Design Competitions (Signature Edition)", "Architectural Specialties (Signature Edition)", "Running the Firm (Signature Edition)", "Urban Design (Signature Edition)", "The Future: Computation and Robotics (Signature Edition)", "The Presentation: Selling the Design (Signature Edition)"], "Advanced": ["The Design Principal (Signature Edition)", "The Technical Master (Signature Edition)", "The Pritzker Prize (Signature Edition)", "Teaching Architecture (Signature Edition)", "The Architect's Legacy (Signature Edition)", "The Architect's Philosophy (Signature Edition)", "The Master Builder (Signature Edition)", "The Profession's Impact (Signature Edition)", "Sacred Architecture (Signature Edition)", "The Architect's Life (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — profession-architect-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original profession record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original profession record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-profession-architect-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("profession-architect-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
