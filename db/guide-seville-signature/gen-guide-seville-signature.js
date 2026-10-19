(function(){'use strict';
/* JAH Signature Seville Travel Guide Database generator — "jahdb-guide-seville-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GSEVS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Seville: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Seville (Signature Edition)", "Getting to Seville (Signature Edition)", "Getting Around Seville (Signature Edition)", "Where to Stay in Seville (Signature Edition)", "Money, Costs, and Budgeting for Seville (Signature Edition)", "Language Essentials for Seville (Signature Edition)", "Safety and Health in Seville (Signature Edition)", "Customs and Etiquette in Seville (Signature Edition)", "What to Pack for Seville (Signature Edition)", "Your First Day in Seville: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Seville (Signature Edition)"], "Compounded": ["Seville: Seville Cathedral (Signature Edition)", "Seville: The Alcázar (Signature Edition)", "Seville: Plaza de España (Signature Edition)", "Seville: The Giralda (Signature Edition)", "Seville: Museum of Fine Arts (Signature Edition)", "Seville: The Archive of the Indies (Signature Edition)", "Seville Neighborhood Deep-Dive: Santa Cruz (Signature Edition)", "Seville Neighborhood Deep-Dive: Triana (Signature Edition)", "Seville Neighborhood Deep-Dive: Arenal (Signature Edition)", "Eating in Seville: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Seville (Signature Edition)", "Parks, Water, and Green Escapes in Seville (Signature Edition)"], "Advanced": ["Hidden Gems of Seville (Signature Edition)", "Seville in Three Days: The Essential Itinerary (Signature Edition)", "Seville in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Seville: Córdoba (Signature Edition)", "Day Trip from Seville: Cádiz (Signature Edition)", "Photography and Viewpoints in Seville (Signature Edition)", "Nightlife and Evenings in Seville (Signature Edition)", "Festivals and Events Calendar for Seville (Signature Edition)", "Seville with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Seville (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-seville-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-seville-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-seville-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
