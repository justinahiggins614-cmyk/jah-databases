(function(){'use strict';
/* JAH Signature Argentina Travel Guide Database generator — "jahdb-guide-argentina-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GARGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Argentina: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Argentina (Signature Edition)", "Getting to Argentina (Signature Edition)", "Getting Around Argentina (Signature Edition)", "Where to Stay in Argentina (Signature Edition)", "Money, Costs, and Budgeting for Argentina (Signature Edition)", "Language Essentials for Argentina (Signature Edition)", "Safety and Health in Argentina (Signature Edition)", "Customs and Etiquette in Argentina (Signature Edition)", "What to Pack for Argentina (Signature Edition)", "Your First Day in Argentina: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Argentina (Signature Edition)"], "Compounded": ["Argentina: Buenos Aires (Signature Edition)", "Argentina: Patagonia (Signature Edition)", "Argentina: Iguaçu Falls (Signature Edition)", "Argentina: Perito Moreno (Signature Edition)", "Argentina: The MALBA (Signature Edition)", "Argentina: The Evita Museum (Signature Edition)", "Argentina Neighborhood Deep-Dive: Buenos Aires (Palermo) (Signature Edition)", "Argentina Neighborhood Deep-Dive: El Chaltén (Signature Edition)", "Argentina Neighborhood Deep-Dive: Mendoza (Signature Edition)", "Eating in Argentina: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Argentina (Signature Edition)", "Parks, Water, and Green Escapes in Argentina (Signature Edition)"], "Advanced": ["Hidden Gems of Argentina (Signature Edition)", "Argentina in Three Days: The Essential Itinerary (Signature Edition)", "Argentina in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Argentina: Tigre from Buenos Aires (Signature Edition)", "Day Trip from Argentina: La Plata from Buenos Aires (Signature Edition)", "Photography and Viewpoints in Argentina (Signature Edition)", "Nightlife and Evenings in Argentina (Signature Edition)", "Festivals and Events Calendar for Argentina (Signature Edition)", "Argentina with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Argentina (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-argentina-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-argentina-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-argentina-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
