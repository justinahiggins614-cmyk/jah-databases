(function(){'use strict';
/* JAH Signature Delhi Travel Guide Database generator — "jahdb-guide-delhi-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GDELS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Delhi: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Delhi (Signature Edition)", "Getting to Delhi (Signature Edition)", "Getting Around Delhi (Signature Edition)", "Where to Stay in Delhi (Signature Edition)", "Money, Costs, and Budgeting for Delhi (Signature Edition)", "Language Essentials for Delhi (Signature Edition)", "Safety and Health in Delhi (Signature Edition)", "Customs and Etiquette in Delhi (Signature Edition)", "What to Pack for Delhi (Signature Edition)", "Your First Day in Delhi: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Delhi (Signature Edition)"], "Compounded": ["Delhi: Red Fort (Signature Edition)", "Delhi: Humayun’s Tomb (Signature Edition)", "Delhi: Qutub Minar (Signature Edition)", "Delhi: India Gate (Signature Edition)", "Delhi: National Museum (Signature Edition)", "Delhi: Gandhi Smriti (Signature Edition)", "Delhi Neighborhood Deep-Dive: Connaught Place (Signature Edition)", "Delhi Neighborhood Deep-Dive: Hauz Khas (Signature Edition)", "Delhi Neighborhood Deep-Dive: Karol Bagh (Signature Edition)", "Eating in Delhi: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Delhi (Signature Edition)", "Parks, Water, and Green Escapes in Delhi (Signature Edition)"], "Advanced": ["Hidden Gems of Delhi (Signature Edition)", "Delhi in Three Days: The Essential Itinerary (Signature Edition)", "Delhi in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Delhi: Agra (Signature Edition)", "Day Trip from Delhi: Jaipur (Signature Edition)", "Photography and Viewpoints in Delhi (Signature Edition)", "Nightlife and Evenings in Delhi (Signature Edition)", "Festivals and Events Calendar for Delhi (Signature Edition)", "Delhi with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Delhi (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-delhi-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-delhi-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-delhi-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
