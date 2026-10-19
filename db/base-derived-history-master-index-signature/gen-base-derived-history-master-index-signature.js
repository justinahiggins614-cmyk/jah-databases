(function(){'use strict';
/* JAH Signature History Master Index Database generator — "jahdb-base-derived-history-master-index-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BHIS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The History Master Index (Signature Edition)", "How to Use This Index (Signature Edition)", "Members: Ancient Egypt and Ancient China (Signature Edition)", "Members: Ancient Greece and Ancient Rome (Signature Edition)", "Members: Medieval Europe and the Ottoman Empire (Signature Edition)", "Members: Renaissance and Age of Exploration (Signature Edition)", "Members: Industrial Revolution and World War II (Signature Edition)", "Members: Archaeology (Signature Edition)", "Member: Conflict Databases (Signature Edition)", "Members: The History Meta Pair (Signature Edition)", "Public vs Signature Editions in the Index (Signature Edition)", "The Timeline Map: 5,000 Years (Signature Edition)"], "Compounded": ["Comparing Empires (Signature Edition)", "The Silk Road Synthesis (Signature Edition)", "Plague Through the Eras (Signature Edition)", "Warfare's Evolution (Signature Edition)", "Trade Networks Across Eras (Signature Edition)", "The Printing Press Moment (Signature Edition)", "The Fall of Rome Debate (Signature Edition)", "The Voyages of 1492 (Signature Edition)", "The Steam Age (Signature Edition)", "The World Wars Remembered (Signature Edition)", "The Archaeology Method (Signature Edition)", "The Timeline Walk (Signature Edition)"], "Advanced": ["Historiography: How History Is Written (Signature Edition)", "The Master Timeline Synthesis (Signature Edition)", "Counterfactuals: The Labeled What-If (Signature Edition)", "Reading Primary Sources (Signature Edition)", "The Museum Synthesis (Signature Edition)", "Living History (Signature Edition)", "The Index as Teacher (Signature Edition)", "Cross-DB Verification for History (Signature Edition)", "The History Dossier (Signature Edition)", "The History Index Legacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — base-derived-history-master-index-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original master index record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original master index record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-base-derived-history-master-index-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("base-derived-history-master-index-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
