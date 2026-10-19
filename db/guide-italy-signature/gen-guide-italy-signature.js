(function(){'use strict';
/* JAH Signature Italy Travel Guide Database generator — "jahdb-guide-italy-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GITAS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Italy: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Italy (Signature Edition)", "Getting to Italy (Signature Edition)", "Getting Around Italy (Signature Edition)", "Where to Stay in Italy (Signature Edition)", "Money, Costs, and Budgeting for Italy (Signature Edition)", "Language Essentials for Italy (Signature Edition)", "Safety and Health in Italy (Signature Edition)", "Customs and Etiquette in Italy (Signature Edition)", "What to Pack for Italy (Signature Edition)", "Your First Day in Italy: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Italy (Signature Edition)"], "Compounded": ["Italy: Rome (Signature Edition)", "Italy: Florence (Signature Edition)", "Italy: Venice (Signature Edition)", "Italy: The Amalfi Coast (Signature Edition)", "Italy: The Vatican Museums (Signature Edition)", "Italy: The Uffizi (Signature Edition)", "Italy Neighborhood Deep-Dive: Rome (Signature Edition)", "Italy Neighborhood Deep-Dive: Florence (Signature Edition)", "Italy Neighborhood Deep-Dive: The Amalfi Coast (Signature Edition)", "Eating in Italy: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Italy (Signature Edition)", "Parks, Water, and Green Escapes in Italy (Signature Edition)"], "Advanced": ["Hidden Gems of Italy (Signature Edition)", "Italy in Three Days: The Essential Itinerary (Signature Edition)", "Italy in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Italy: Pompeii from Naples (Signature Edition)", "Day Trip from Italy: The Cinque Terre (Signature Edition)", "Photography and Viewpoints in Italy (Signature Edition)", "Nightlife and Evenings in Italy (Signature Edition)", "Festivals and Events Calendar for Italy (Signature Edition)", "Italy with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Italy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-italy-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original travel guide record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original travel guide record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-guide-italy-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-italy-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
